/**
 * htmlook_campus · seed install + like counter (Cloudflare Worker).
 * Privacy: no PII, IP only for 24h dedup.
 */
const SEED_RX = /^[a-z0-9-]{1,80}$/;

function corsHeaders(origin, allowed) {
  const ok = allowed.includes(origin);
  return {
    'Access-Control-Allow-Origin': ok ? origin : 'null',
    'Access-Control-Allow-Methods': 'GET, POST, OPTIONS',
    'Access-Control-Allow-Headers': 'Content-Type',
    'Vary': 'Origin',
  };
}

async function increment(env, key) {
  const cur = parseInt((await env.COUNTERS.get(key)) ?? '0', 10);
  const next = cur + 1;
  await env.COUNTERS.put(key, String(next));
  return next;
}

export default {
  async fetch(request, env) {
    const url = new URL(request.url);
    const origin = request.headers.get('Origin') ?? '';
    const allowed = (env.ALLOWED_ORIGINS ?? '').split(',').map(s => s.trim());
    const cors = corsHeaders(origin, allowed);

    if (request.method === 'OPTIONS') return new Response(null, { status: 204, headers: cors });

    let m = url.pathname.match(/^\/c\/([^/]+)$/);
    if (m && request.method === 'POST') {
      const seed = m[1];
      if (!SEED_RX.test(seed)) return new Response('400', { status: 400, headers: cors });
      const installs = await increment(env, `inst:${seed}`);
      return Response.json({ seed, installs }, { headers: cors });
    }
    if (m && request.method === 'GET') {
      const seed = m[1];
      const installs = parseInt((await env.COUNTERS.get(`inst:${seed}`)) ?? '0', 10);
      const likes    = parseInt((await env.COUNTERS.get(`like:${seed}`)) ?? '0', 10);
      return Response.json({ seed, installs, likes }, { headers: cors });
    }

    m = url.pathname.match(/^\/like\/([^/]+)$/);
    if (m && request.method === 'POST') {
      const seed = m[1];
      if (!SEED_RX.test(seed)) return new Response('400', { status: 400, headers: cors });
      const ip = request.headers.get('CF-Connecting-IP') ?? 'anon';
      const dedupeKey = `voted:${seed}:${ip}`;
      if (await env.COUNTERS.get(dedupeKey)) {
        const likes = parseInt((await env.COUNTERS.get(`like:${seed}`)) ?? '0', 10);
        return Response.json({ seed, likes, voted: true }, { headers: cors });
      }
      await env.COUNTERS.put(dedupeKey, '1', { expirationTtl: 86400 });
      const likes = await increment(env, `like:${seed}`);
      return Response.json({ seed, likes, voted: true }, { headers: cors });
    }

    if (url.pathname === '/counts' && request.method === 'GET') {
      const list = await env.COUNTERS.list({ prefix: 'inst:' });
      const out = {};
      for (const k of list.keys) {
        const seed = k.name.slice(5);
        const installs = parseInt((await env.COUNTERS.get(k.name)) ?? '0', 10);
        const likes    = parseInt((await env.COUNTERS.get(`like:${seed}`)) ?? '0', 10);
        out[seed] = { installs, likes };
      }
      return Response.json(out, { headers: { ...cors, 'Cache-Control': 'public, max-age=300' } });
    }

    // ─────────────────────────────────────────────────────────────
    // Trial fingerprint endpoint — POST/GET /trial/<fp>
    //   Server-side 14-day trial. Survives uninstall/reinstall on
    //   the same machine because <fp> = SHA-256(machine-uid).
    //   Privacy: only the hex hash is stored, no PII.
    //   Storage: KV `trial:<fp>` → { fp, started_at }
    //   First POST creates the record (started_at = now).
    //   Subsequent calls return live { trial_active, days_remaining, ... }.
    //
    // The same endpoint serves GET so clients can refresh state
    // without creating a new record on a stale fingerprint.
    // ─────────────────────────────────────────────────────────────
    m = url.pathname.match(/^\/trial\/([a-f0-9]{16,128})$/);
    if (m && (request.method === 'POST' || request.method === 'GET')) {
      const fp = m[1];
      const now = Math.floor(Date.now() / 1000);
      const TRIAL_SECS = 14 * 24 * 60 * 60;
      const key = `trial:${fp}`;
      const existing = await env.COUNTERS.get(key);
      let record;
      if (existing) {
        record = JSON.parse(existing);
      } else {
        // First contact → start trial
        record = { fp, started_at: now };
        await env.COUNTERS.put(key, JSON.stringify(record));
      }
      const elapsed = now - record.started_at;
      const days_used = Math.floor(elapsed / 86400);
      const days_remaining = Math.max(0, Math.ceil((TRIAL_SECS - elapsed) / 86400));
      const expires_at = record.started_at + TRIAL_SECS;
      const trial_active = elapsed < TRIAL_SECS;
      return Response.json({
        fp,
        started_at: record.started_at,
        expires_at,
        days_used,
        days_remaining,
        trial_active,
      }, { headers: { ...cors, 'Cache-Control': 'private, max-age=3600' } });
    }

    // ─────────────────────────────────────────────────────────────
    // Paddle webhook → KV purchase record.
    //   POST /paddle/webhook
    //     Body: Paddle Notification payload (JSON)
    //     Header: Paddle-Signature: ts=...;h1=...
    //   Verifies HMAC signature using PADDLE_WEBHOOK_SECRET env, then
    //   for `transaction.completed` writes:
    //     KV `purchase:<email>` → { priceId, ts, status: 'active',
    //                                customer_id, transaction_id }
    //
    //   Privacy: stores email + Paddle IDs only, no card data
    //   (Paddle never forwards PCI data to webhooks).
    //
    //   GET /purchase/<email>
    //     Returns the stored purchase record so the desktop app can
    //     poll after the user completes browser checkout. Email is
    //     URL-encoded.
    // ─────────────────────────────────────────────────────────────
    if (url.pathname === '/paddle/webhook' && request.method === 'POST') {
      const sig = request.headers.get('Paddle-Signature') ?? '';
      const secret = env.PADDLE_WEBHOOK_SECRET ?? '';
      const raw = await request.text();
      if (!secret) {
        return new Response('webhook secret not configured', { status: 500 });
      }
      // Paddle signature: "ts=<unix>;h1=<hex>". h1 = HMAC_SHA256(secret, ts + ":" + body).
      const tsMatch = sig.match(/ts=(\d+)/);
      const h1Match = sig.match(/h1=([a-f0-9]+)/);
      if (!tsMatch || !h1Match) {
        return new Response('bad signature header', { status: 400 });
      }
      const ts = tsMatch[1];
      const h1 = h1Match[1];
      const enc = new TextEncoder();
      const key = await crypto.subtle.importKey(
        'raw', enc.encode(secret),
        { name: 'HMAC', hash: 'SHA-256' },
        false, ['sign'],
      );
      const mac = await crypto.subtle.sign('HMAC', key, enc.encode(`${ts}:${raw}`));
      const macHex = Array.from(new Uint8Array(mac)).map(b => b.toString(16).padStart(2, '0')).join('');
      if (macHex !== h1) {
        return new Response('signature mismatch', { status: 401 });
      }
      // Verified. Parse + record.
      let evt;
      try { evt = JSON.parse(raw); } catch { return new Response('bad json', { status: 400 }); }
      const eventType = evt?.event_type ?? '';

      // Paddle Billing v2 webhooks reference customer by `customer_id`
      // only — email is NOT in the payload. Look it up via the Paddle
      // API. Two fallbacks: `customer.created` events sometimes embed
      // email; we also keep a `cust:<id>` KV cache so transaction
      // events for known customers don't pay another API round trip.
      async function resolveEmail(data) {
        let email = data?.customer?.email
                ?? data?.billing_details?.email
                ?? '';
        if (email) return email;
        const customerId = data?.customer_id ?? '';
        if (!customerId) return '';
        // KV cache hit?
        const cached = await env.COUNTERS.get(`cust:${customerId}`);
        if (cached) return cached;
        // API lookup
        const apiKey = env.PADDLE_API_KEY ?? '';
        if (!apiKey) return '';
        try {
          const resp = await fetch(`https://api.paddle.com/customers/${customerId}`, {
            headers: { Authorization: `Bearer ${apiKey}` },
          });
          if (!resp.ok) return '';
          const body = await resp.json();
          email = body?.data?.email ?? '';
          if (email) {
            // 30-day cache so future events for this customer hit KV.
            await env.COUNTERS.put(`cust:${customerId}`, email, { expirationTtl: 30 * 86400 });
          }
          return email;
        } catch { return ''; }
      }

      if (eventType === 'customer.created' || eventType === 'customer.updated') {
        const email = evt?.data?.email ?? '';
        const customerId = evt?.data?.id ?? '';
        if (email && customerId) {
          await env.COUNTERS.put(`cust:${customerId}`, email, { expirationTtl: 30 * 86400 });
        }
        return new Response('ok', { status: 200 });
      }

      if (eventType === 'transaction.completed' || eventType === 'subscription.created' || eventType === 'subscription.activated') {
        const email = await resolveEmail(evt?.data ?? {});
        const priceId = evt?.data?.items?.[0]?.price?.id
                    ?? evt?.data?.items?.[0]?.price_id
                    ?? '';
        if (email) {
          const record = {
            email,
            priceId,
            ts: Math.floor(Date.now() / 1000),
            status: 'active',
            customer_id: evt?.data?.customer_id ?? '',
            transaction_id: evt?.data?.id ?? '',
            event_type: eventType,
          };
          await env.COUNTERS.put(`purchase:${email.toLowerCase()}`, JSON.stringify(record));
        } else {
          // Diagnostic crumb so we can audit why an event landed
          // without resolvable email. Short TTL so it doesn't fill KV.
          await env.COUNTERS.put(
            `webhook_unresolved:${Date.now()}`,
            JSON.stringify({ eventType, customer_id: evt?.data?.customer_id, raw_excerpt: raw.slice(0, 1000) }),
            { expirationTtl: 7 * 86400 },
          );
        }
      } else if (eventType === 'subscription.canceled' || eventType === 'subscription.cancelled' || eventType === 'transaction.payment_failed') {
        const email = await resolveEmail(evt?.data ?? {});
        if (email) {
          const cur = await env.COUNTERS.get(`purchase:${email.toLowerCase()}`);
          if (cur) {
            const r = JSON.parse(cur);
            r.status = 'canceled';
            r.ts = Math.floor(Date.now() / 1000);
            await env.COUNTERS.put(`purchase:${email.toLowerCase()}`, JSON.stringify(r));
          }
        }
      }
      return new Response('ok', { status: 200 });
    }

    m = url.pathname.match(/^\/purchase\/([^/]+)$/);
    if (m && request.method === 'GET') {
      // Read-only license-status lookup. Used by every HTMLook desktop
      // / mobile build to verify a purchase after browser checkout.
      // Explicitly allow ALL origins (including `tauri://localhost`
      // and future iOS/Android webviews) — the response carries no
      // secret data beyond the email already in the request URL.
      const email = decodeURIComponent(m[1]).toLowerCase();
      const raw = await env.COUNTERS.get(`purchase:${email}`);
      const publicCors = {
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Methods': 'GET, OPTIONS',
        'Access-Control-Allow-Headers': 'Content-Type',
      };
      if (!raw) {
        return Response.json({ email, status: 'none' }, { headers: publicCors });
      }
      const record = JSON.parse(raw);
      return Response.json(record, { headers: { ...publicCors, 'Cache-Control': 'private, max-age=30' } });
    }

    return new Response('not found', { status: 404, headers: cors });
  },
};
