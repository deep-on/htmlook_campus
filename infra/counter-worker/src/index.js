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
      if (eventType === 'transaction.completed' || eventType === 'subscription.created' || eventType === 'subscription.activated') {
        const email = evt?.data?.customer?.email
                  ?? evt?.data?.billing_details?.email
                  ?? '';
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
        }
      } else if (eventType === 'subscription.canceled' || eventType === 'subscription.cancelled' || eventType === 'transaction.payment_failed') {
        const email = evt?.data?.customer?.email ?? '';
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
      const email = decodeURIComponent(m[1]).toLowerCase();
      const raw = await env.COUNTERS.get(`purchase:${email}`);
      if (!raw) {
        return Response.json({ email, status: 'none' }, { headers: cors });
      }
      const record = JSON.parse(raw);
      return Response.json(record, { headers: { ...cors, 'Cache-Control': 'private, max-age=30' } });
    }

    return new Response('not found', { status: 404, headers: cors });
  },
};
