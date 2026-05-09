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

async function listAll(env, prefix) {
  const out = [];
  let cursor;
  do {
    const r = await env.COUNTERS.list({ prefix, cursor });
    for (const k of r.keys) out.push(k.name);
    cursor = r.list_complete ? null : r.cursor;
  } while (cursor);
  return out;
}

/**
 * Compute the monitoring digest + send via Resend. Shared between
 * the wrangler.toml cron trigger and the /admin/test-cron endpoint.
 * Returns { sent, status, attention } so the test endpoint can echo
 * the result.
 */
async function runDailyDigest(env) {
  if (!env.RESEND_API_KEY || !env.ALERT_EMAIL) {
    return { sent: false, reason: 'RESEND_API_KEY or ALERT_EMAIL not set' };
  }
  const purchaseKeys = await listAll(env, 'purchase:');
  const stats = { active: 0, ending: 0, canceled: 0, dunning: 0, refunded: 0, paused: 0, manual: 0 };
  for (const k of purchaseKeys) {
    const raw = await env.COUNTERS.get(k);
    if (!raw) continue;
    try {
      const r = JSON.parse(raw);
      if (r.status === 'active') stats.active += 1;
      else if (r.status === 'ending') stats.ending += 1;
      else if (r.status === 'canceled') stats.canceled += 1;
      if (r.dunning) stats.dunning += 1;
      if (r.ended_reason === 'refunded') stats.refunded += 1;
      if (r.ended_reason === 'paused') stats.paused += 1;
      if (r.customer_id === 'manual' || r.event_type === 'manual.write') stats.manual += 1;
    } catch { /* ignore */ }
  }
  const trials = (await listAll(env, 'trial:')).length;
  const customers = (await listAll(env, 'cust:')).length;
  const unresolvedKeys = await listAll(env, 'webhook_unresolved:');
  const unknownKeys = await listAll(env, 'webhook_unknown:');
  const unresolved = unresolvedKeys.length;
  const unknown = unknownKeys.length;

  async function tail(keys, n) {
    const slice = keys.slice(-n);
    const out = [];
    for (const k of slice) {
      const raw = await env.COUNTERS.get(k);
      try { out.push({ key: k, value: JSON.parse(raw) }); }
      catch { out.push({ key: k, value: raw }); }
    }
    return out;
  }
  const unresolvedSamples = unresolved ? await tail(unresolvedKeys, 5) : [];
  const unknownSamples = unknown ? await tail(unknownKeys, 5) : [];

  const attention = unresolved > 0 || unknown > 0 || stats.dunning > 0;
  const today = new Date().toISOString().slice(0, 10);
  const subject = `${attention ? '[ATTENTION] ' : ''}HTMLook daily stats — ${today}`;

  const lines = [
    `HTMLook daily monitoring digest — ${today}`,
    ``,
    `Purchases (total ${purchaseKeys.length})`,
    `  active     : ${stats.active}`,
    `  ending     : ${stats.ending}    ← cancel-at-period-end`,
    `  canceled   : ${stats.canceled}`,
    `  dunning    : ${stats.dunning}    ← failed-payment retry window`,
    `  refunded   : ${stats.refunded}`,
    `  paused     : ${stats.paused}`,
    `  manual     : ${stats.manual}    ← admin/wrangler-written`,
    ``,
    `Trials in flight   : ${trials}`,
    `Customer email cache: ${customers}`,
    ``,
    `Webhook health`,
    `  unresolved (7d) : ${unresolved}    ${unresolved === 0 ? '✓' : '⚠ check Paddle API key'}`,
    `  unknown    (30d): ${unknown}    ${unknown === 0 ? '✓' : '⚠ new Paddle event type appeared'}`,
  ];
  if (unresolvedSamples.length) {
    lines.push(``, `Recent unresolved samples:`);
    for (const s of unresolvedSamples) {
      lines.push(`  ${s.key}`);
      lines.push(`    ${JSON.stringify(s.value).slice(0, 240)}`);
    }
  }
  if (unknownSamples.length) {
    lines.push(``, `Recent unknown samples:`);
    for (const s of unknownSamples) {
      lines.push(`  ${s.key}`);
      lines.push(`    ${JSON.stringify(s.value).slice(0, 240)}`);
    }
  }
  lines.push(``, `Generated: ${new Date().toISOString()}`);
  const text = lines.join('\n');

  const fromAddr = env.ALERT_FROM ?? 'HTMLook Monitor <monitor@htmlook.app>';
  const resp = await fetch('https://api.resend.com/emails', {
    method: 'POST',
    headers: {
      'Authorization': `Bearer ${env.RESEND_API_KEY}`,
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      from: fromAddr,
      to: env.ALERT_EMAIL,
      subject,
      text,
    }),
  });
  const ok = resp.ok;
  let errBody = '';
  if (!ok) errBody = await resp.text();
  return { sent: ok, status: resp.status, attention, subject, error: ok ? null : errBody.slice(0, 500) };
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
        // Worker mis-configured — return 5xx so Paddle keeps retrying
        // until secret is set (don't silently lose events).
        return new Response('webhook secret not configured', { status: 503 });
      }
      // Paddle signature: "ts=<unix>;h1=<hex>". h1 = HMAC_SHA256(secret, ts + ":" + body).
      const tsMatch = sig.match(/ts=(\d+)/);
      const h1Match = sig.match(/h1=([a-f0-9]+)/);
      if (!tsMatch || !h1Match) {
        return new Response('bad signature header', { status: 400 });
      }
      const ts = tsMatch[1];
      const h1 = h1Match[1];
      // Replay protection: reject events with timestamps > 5min off
      // from now. Paddle delivers within seconds; anything older is
      // either a captured-and-replayed payload or a clock-drift bug.
      const tsNum = parseInt(ts, 10);
      const nowSec = Math.floor(Date.now() / 1000);
      if (Number.isFinite(tsNum) && Math.abs(nowSec - tsNum) > 300) {
        return new Response('signature timestamp too old/new', { status: 401 });
      }
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

      // Source-of-truth event time from Paddle. Used for KV ordering
      // (out-of-order webhook protection) instead of Worker's wall
      // clock. ISO-8601 string → unix seconds.
      const eventOccurredAt = (() => {
        const iso = evt?.occurred_at ?? evt?.data?.occurred_at ?? '';
        const t = iso ? Math.floor(Date.parse(iso) / 1000) : nowSec;
        return Number.isFinite(t) ? t : nowSec;
      })();

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

      // Out-of-order webhook protection — only apply incoming events
      // whose Paddle-side `occurred_at` is newer than the last record's
      // `occurred_at`. Returns the existing record if older event
      // received, otherwise null + caller proceeds with new write.
      async function shouldSkipForOrder(emailKey, incomingOccurred) {
        const cur = await env.COUNTERS.get(emailKey);
        if (!cur) return null;
        try {
          const r = JSON.parse(cur);
          if (typeof r.occurred_at === 'number' && r.occurred_at > incomingOccurred) {
            return r; // skip — KV has newer
          }
        } catch { /* fallthrough */ }
        return null;
      }

      if (eventType === 'customer.created' || eventType === 'customer.updated') {
        const email = evt?.data?.email ?? '';
        const customerId = evt?.data?.id ?? '';
        if (email && customerId) {
          await env.COUNTERS.put(`cust:${customerId}`, email, { expirationTtl: 30 * 86400 });
        }
        return new Response('ok', { status: 200 });
      }

      // ── ACTIVATE events ──────────────────────────────────────────
      if (eventType === 'transaction.completed' || eventType === 'subscription.created' || eventType === 'subscription.activated') {
        const email = await resolveEmail(evt?.data ?? {});
        const priceId = evt?.data?.items?.[0]?.price?.id
                    ?? evt?.data?.items?.[0]?.price_id
                    ?? '';
        if (!email) {
          // Tell Paddle to retry; also leave diagnostic crumb so we
          // can audit unresolved events without enabling tail.
          await env.COUNTERS.put(
            `webhook_unresolved:${Date.now()}`,
            JSON.stringify({ eventType, customer_id: evt?.data?.customer_id, raw_excerpt: raw.slice(0, 1000) }),
            { expirationTtl: 7 * 86400 },
          );
          return new Response('email unresolved (retry)', { status: 503 });
        }
        const emailKey = `purchase:${email.toLowerCase()}`;
        const skip = await shouldSkipForOrder(emailKey, eventOccurredAt);
        if (skip) return new Response('older event ignored', { status: 200 });
        // Period end: from subscription event. transaction.completed
        // doesn't carry period info but should still mark active.
        const currentPeriodEnd = (() => {
          const iso = evt?.data?.current_billing_period?.ends_at ?? '';
          const t = iso ? Math.floor(Date.parse(iso) / 1000) : 0;
          return Number.isFinite(t) ? t : 0;
        })();
        // Preserve first_paid_at across the entire customer lifecycle.
        // Once set on the very first activation, never overwrite —
        // even after a refund + re-subscribe cycle. This locks the
        // 14-day refund window to the FIRST payment per email,
        // closing the "refund + re-subscribe + refund" abuse loop.
        const existingRaw = await env.COUNTERS.get(emailKey);
        let firstPaidAt = nowSec;
        if (existingRaw) {
          try {
            const existing = JSON.parse(existingRaw);
            if (typeof existing.first_paid_at === 'number' && existing.first_paid_at > 0) {
              firstPaidAt = existing.first_paid_at;
            }
          } catch { /* ignore */ }
        }
        const record = {
          email,
          priceId,
          ts: nowSec,
          occurred_at: eventOccurredAt,
          status: 'active',
          first_paid_at: firstPaidAt,
          current_period_end: currentPeriodEnd,
          customer_id: evt?.data?.customer_id ?? '',
          transaction_id: evt?.data?.id ?? '',
          event_type: eventType,
        };
        await env.COUNTERS.put(emailKey, JSON.stringify(record));
        return new Response('ok', { status: 200 });
      }

      // ── CANCEL-AT-PERIOD-END events (still active until effective_at) ──
      // Paddle's standard "cancel" event when user clicks Cancel in the
      // customer portal: scheduled_change.action='cancel' with
      // scheduled_change.effective_at in the future.
      if (eventType === 'subscription.canceled' || eventType === 'subscription.cancelled') {
        const email = await resolveEmail(evt?.data ?? {});
        if (!email) {
          return new Response('email unresolved (retry)', { status: 503 });
        }
        const emailKey = `purchase:${email.toLowerCase()}`;
        const skip = await shouldSkipForOrder(emailKey, eventOccurredAt);
        if (skip) return new Response('older event ignored', { status: 200 });
        const cur = await env.COUNTERS.get(emailKey);
        const r = cur ? JSON.parse(cur) : { email };
        // first_paid_at is set once on activation and preserved across
        // all subsequent state transitions — never overwrite here.
        // Two flavors of cancel:
        //   - cancel-at-period-end: subscription.status === 'active'
        //     and scheduled_change.effective_at points to next billing.
        //     User keeps Pro until that moment.
        //   - immediate cancel: subscription.status === 'canceled' and
        //     no scheduled_change (or effective_at = now). User loses
        //     Pro immediately (refund / chargeback / dunning end).
        const subStatus = evt?.data?.status ?? '';
        const scheduledChange = evt?.data?.scheduled_change ?? null;
        const effectiveIso = scheduledChange?.effective_at
                          ?? evt?.data?.canceled_at
                          ?? '';
        const effectiveAt = effectiveIso ? Math.floor(Date.parse(effectiveIso) / 1000) : nowSec;
        if (subStatus === 'active' && scheduledChange?.action === 'cancel' && effectiveAt > nowSec) {
          r.status = 'ending';
          r.effective_at = effectiveAt;
          r.canceled_at = nowSec;
          r.ended_reason = 'user_canceled';
        } else {
          r.status = 'canceled';
          r.effective_at = effectiveAt;
          r.canceled_at = nowSec;
          r.ended_reason = r.ended_reason ?? 'user_canceled';
        }
        r.ts = nowSec;
        r.occurred_at = eventOccurredAt;
        r.event_type = eventType;
        await env.COUNTERS.put(emailKey, JSON.stringify(r));
        return new Response('ok', { status: 200 });
      }

      // ── PAUSE / RESUME ───────────────────────────────────────────
      if (eventType === 'subscription.paused') {
        const email = await resolveEmail(evt?.data ?? {});
        if (!email) return new Response('email unresolved (retry)', { status: 503 });
        const emailKey = `purchase:${email.toLowerCase()}`;
        const skip = await shouldSkipForOrder(emailKey, eventOccurredAt);
        if (skip) return new Response('older event ignored', { status: 200 });
        const cur = await env.COUNTERS.get(emailKey);
        const r = cur ? JSON.parse(cur) : { email };
        // first_paid_at is set once on activation and preserved across
        // all subsequent state transitions — never overwrite here.
        r.status = 'canceled'; // paused = no Pro privilege
        r.ts = nowSec;
        r.occurred_at = eventOccurredAt;
        r.ended_reason = 'paused';
        r.event_type = eventType;
        await env.COUNTERS.put(emailKey, JSON.stringify(r));
        return new Response('ok', { status: 200 });
      }
      if (eventType === 'subscription.resumed') {
        const email = await resolveEmail(evt?.data ?? {});
        if (!email) return new Response('email unresolved (retry)', { status: 503 });
        const emailKey = `purchase:${email.toLowerCase()}`;
        const skip = await shouldSkipForOrder(emailKey, eventOccurredAt);
        if (skip) return new Response('older event ignored', { status: 200 });
        const cur = await env.COUNTERS.get(emailKey);
        const r = cur ? JSON.parse(cur) : { email };
        // first_paid_at is set once on activation and preserved across
        // all subsequent state transitions — never overwrite here.
        r.status = 'active';
        r.ts = nowSec;
        r.occurred_at = eventOccurredAt;
        r.ended_reason = null;
        r.event_type = eventType;
        await env.COUNTERS.put(emailKey, JSON.stringify(r));
        return new Response('ok', { status: 200 });
      }

      // ── DUNNING — payment failed but not yet given up ────────────
      // Don't change status; Paddle's dunning will retry. If dunning
      // ultimately fails, subscription.canceled will follow.
      if (eventType === 'transaction.payment_failed' || eventType === 'subscription.past_due') {
        const email = await resolveEmail(evt?.data ?? {});
        if (!email) return new Response('email unresolved (retry)', { status: 503 });
        const emailKey = `purchase:${email.toLowerCase()}`;
        const cur = await env.COUNTERS.get(emailKey);
        if (cur) {
          const r = JSON.parse(cur);
          r.dunning = true;
          r.dunning_started_at = r.dunning_started_at ?? nowSec;
          r.event_type = eventType;
          // Don't bump ts/occurred_at — keep ordering for activate/cancel
          await env.COUNTERS.put(emailKey, JSON.stringify(r));
        }
        return new Response('ok', { status: 200 });
      }

      // ── REFUND / CHARGEBACK — immediate cancel ───────────────────
      // Paddle Billing v2 emits adjustment.created with action='refund'
      // or transaction.refunded; chargebacks similarly. Both flip the
      // user to canceled immediately regardless of period.
      if (eventType === 'transaction.refunded' || eventType === 'adjustment.created' || eventType === 'transaction.chargeback') {
        // adjustment.created has multiple actions (refund, credit, ...).
        // Only refund + chargeback flip status.
        const action = evt?.data?.action ?? '';
        if (eventType === 'adjustment.created' && action !== 'refund' && action !== 'chargeback') {
          return new Response('ok (non-refund adjustment)', { status: 200 });
        }
        const email = await resolveEmail(evt?.data ?? {});
        if (!email) return new Response('email unresolved (retry)', { status: 503 });
        const emailKey = `purchase:${email.toLowerCase()}`;
        const skip = await shouldSkipForOrder(emailKey, eventOccurredAt);
        if (skip) return new Response('older event ignored', { status: 200 });
        const cur = await env.COUNTERS.get(emailKey);
        const r = cur ? JSON.parse(cur) : { email };
        // first_paid_at is set once on activation and preserved across
        // all subsequent state transitions — never overwrite here.
        r.status = 'canceled';
        r.effective_at = nowSec;
        r.canceled_at = nowSec;
        r.ended_reason = (eventType === 'transaction.chargeback' || action === 'chargeback') ? 'chargeback' : 'refunded';
        r.ts = nowSec;
        r.occurred_at = eventOccurredAt;
        r.event_type = eventType;
        await env.COUNTERS.put(emailKey, JSON.stringify(r));
        return new Response('ok', { status: 200 });
      }

      // Unknown event — still 200 so Paddle doesn't retry, but log
      // for future event-name auditing.
      await env.COUNTERS.put(
        `webhook_unknown:${Date.now()}`,
        JSON.stringify({ eventType, raw_excerpt: raw.slice(0, 500) }),
        { expirationTtl: 30 * 86400 },
      );
      return new Response('ok (unhandled)', { status: 200 });
    }

    // ─────────────────────────────────────────────────────────────
    // Paddle Customer Portal session URL.
    //   GET /portal/<email>
    //   1. Look up the customer_id from the user's purchase record
    //   2. Hit Paddle's POST /customers/{id}/portal-sessions API
    //   3. Return { url } so the desktop app can open_external it
    //   The returned portal URL lets the customer cancel, change
    //   payment method, view invoices, request refund — all via
    //   Paddle's hosted UI, no per-feature build on our side.
    // ─────────────────────────────────────────────────────────────
    m = url.pathname.match(/^\/portal\/([^/]+)$/);
    if (m && request.method === 'GET') {
      const email = decodeURIComponent(m[1]).toLowerCase();
      const publicCors = {
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Methods': 'GET, OPTIONS',
        'Access-Control-Allow-Headers': 'Content-Type',
      };
      const raw = await env.COUNTERS.get(`purchase:${email}`);
      if (!raw) {
        return Response.json({ error: 'no purchase record for email' }, { status: 404, headers: publicCors });
      }
      const record = JSON.parse(raw);
      const customerId = record.customer_id;
      if (!customerId || customerId === 'manual') {
        // Manual KV write (admin unlock) has no real Paddle customer
        // ID. Fall back to a contact-support response so the desktop
        // app can show "email support to manage" instead of a 500.
        return Response.json({ error: 'no paddle customer id', fallback: 'mailto:support@htmlook.app' }, { status: 422, headers: publicCors });
      }
      const apiKey = env.PADDLE_API_KEY ?? '';
      if (!apiKey) {
        return Response.json({ error: 'paddle api key not configured' }, { status: 503, headers: publicCors });
      }
      try {
        const resp = await fetch(`https://api.paddle.com/customers/${customerId}/portal-sessions`, {
          method: 'POST',
          headers: {
            'Authorization': `Bearer ${apiKey}`,
            'Content-Type': 'application/json',
          },
          body: '{}',
        });
        if (!resp.ok) {
          const errText = await resp.text();
          return Response.json({ error: `paddle api ${resp.status}`, detail: errText.slice(0, 500) }, { status: 502, headers: publicCors });
        }
        const body = await resp.json();
        const portalUrl = body?.data?.urls?.general?.overview
                       ?? body?.data?.url
                       ?? '';
        if (!portalUrl) {
          return Response.json({ error: 'no portal url in response', detail: JSON.stringify(body).slice(0, 500) }, { status: 502, headers: publicCors });
        }
        return Response.json({ url: portalUrl }, { headers: publicCors });
      } catch (e) {
        return Response.json({ error: 'fetch failed', detail: String(e).slice(0, 200) }, { status: 502, headers: publicCors });
      }
    }

    m = url.pathname.match(/^\/purchase\/([^/]+)$/);
    if (m && request.method === 'GET') {
      // Read-only license-status lookup. Used by every HTMLook desktop
      // / mobile build to verify a purchase after browser checkout.
      const email = decodeURIComponent(m[1]).toLowerCase();
      const raw = await env.COUNTERS.get(`purchase:${email}`);
      const publicCors = {
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Methods': 'GET, OPTIONS',
        'Access-Control-Allow-Headers': 'Content-Type, Authorization',
      };
      if (!raw) {
        return Response.json({ email, status: 'none' }, { headers: publicCors });
      }
      const record = JSON.parse(raw);
      // Privacy-minimised public response — only the fields the desktop
      // client actually needs to gate features. customer_id and
      // transaction_id are kept server-side so an attacker who probes
      // arbitrary emails can't enumerate Paddle internal IDs. Edge
      // cache lowered from 30 s to 5 s so a freshly-paid user clicking
      // Verify within 30 s of payment isn't served stale 'none'.
      const minimal = {
        email: record.email,
        status: record.status,
        priceId: record.priceId,
        ts: record.ts,
        occurred_at: record.occurred_at,
        first_paid_at: record.first_paid_at,
        effective_at: record.effective_at,
        canceled_at: record.canceled_at,
        ended_reason: record.ended_reason,
        event_type: record.event_type,
      };
      return Response.json(minimal, { headers: { ...publicCors, 'Cache-Control': 'private, max-age=5' } });
    }

    // ─────────────────────────────────────────────────────────────
    // Admin monitoring endpoints. Auth: Bearer token via env
    // ADMIN_TOKEN. Returns aggregate counts and recent diagnostic
    // crumbs so the operator can see at a glance whether webhooks
    // are healthy without opening Paddle dashboard.
    //
    //   GET /admin/stats
    //     - purchases by status (active/ending/canceled)
    //     - trial signup count
    //     - webhook_unresolved count (last 7d, surfaces missing
    //       PADDLE_API_KEY or unrecognised payload shapes)
    //     - webhook_unknown count (last 30d, captures Paddle event
    //       types we haven't coded yet)
    //
    //   GET /admin/recent
    //     - latest 20 webhook_unresolved + webhook_unknown crumbs
    //       so the operator can sanity-check what's leaking.
    // ─────────────────────────────────────────────────────────────
    if (url.pathname === '/admin/stats' || url.pathname === '/admin/recent') {
      const adminToken = env.ADMIN_TOKEN ?? '';
      const auth = request.headers.get('Authorization') ?? '';
      const presented = auth.startsWith('Bearer ') ? auth.slice(7) : (url.searchParams.get('token') ?? '');
      if (!adminToken || presented !== adminToken) {
        return new Response('unauthorized', { status: 401 });
      }
      if (url.pathname === '/admin/stats') {
        // Stream the prefix listings — KV `list` is paginated. For v1
        // scale (single-digit thousand keys) one pass per prefix is
        // fine; revisit if usage grows.
        async function listAll(prefix) {
          const out = [];
          let cursor;
          do {
            const r = await env.COUNTERS.list({ prefix, cursor });
            for (const k of r.keys) out.push(k.name);
            cursor = r.list_complete ? null : r.cursor;
          } while (cursor);
          return out;
        }
        const purchaseKeys = await listAll('purchase:');
        const stats = { active: 0, ending: 0, canceled: 0, dunning: 0, refunded: 0, paused: 0, manual: 0 };
        for (const k of purchaseKeys) {
          const raw = await env.COUNTERS.get(k);
          if (!raw) continue;
          try {
            const r = JSON.parse(raw);
            if (r.status === 'active') stats.active += 1;
            else if (r.status === 'ending') stats.ending += 1;
            else if (r.status === 'canceled') stats.canceled += 1;
            if (r.dunning) stats.dunning += 1;
            if (r.ended_reason === 'refunded') stats.refunded += 1;
            if (r.ended_reason === 'paused') stats.paused += 1;
            if (r.customer_id === 'manual' || r.event_type === 'manual.write') stats.manual += 1;
          } catch { /* ignore corrupt records */ }
        }
        const trials = (await listAll('trial:')).length;
        const customers = (await listAll('cust:')).length;
        const unresolved = (await listAll('webhook_unresolved:')).length;
        const unknown = (await listAll('webhook_unknown:')).length;
        return Response.json({
          purchases: {
            total: purchaseKeys.length,
            ...stats,
          },
          trials,
          customers_cached: customers,
          webhook_unresolved_7d: unresolved,
          webhook_unknown_30d: unknown,
          generated_at: new Date().toISOString(),
        }, {
          headers: { 'Cache-Control': 'no-store' },
        });
      }
      if (url.pathname === '/admin/test-cron') {
        // Manually trigger the daily digest email — useful right after
        // setting RESEND_API_KEY to verify the pipe end-to-end without
        // waiting until 09:30 KST.
        const result = await runDailyDigest(env);
        return Response.json(result, { headers: { 'Cache-Control': 'no-store' } });
      }
      if (url.pathname === '/admin/recent') {
        async function listRecent(prefix, n) {
          const r = await env.COUNTERS.list({ prefix, limit: 100 });
          const items = [];
          for (const k of r.keys.slice(-n)) {
            const raw = await env.COUNTERS.get(k.name);
            try { items.push({ key: k.name, value: JSON.parse(raw) }); }
            catch { items.push({ key: k.name, value: raw }); }
          }
          return items;
        }
        return Response.json({
          unresolved: await listRecent('webhook_unresolved:', 10),
          unknown: await listRecent('webhook_unknown:', 10),
          generated_at: new Date().toISOString(),
        }, { headers: { 'Cache-Control': 'no-store' } });
      }
    }

    return new Response('not found', { status: 404, headers: cors });
  },

  /**
   * Daily monitoring digest. Triggered by the wrangler.toml cron
   * (30 0 * * * = 00:30 UTC ≈ 09:30 KST). Same logic as
   * /admin/test-cron — see runDailyDigest() above.
   */
  async scheduled(_event, env, _ctx) {
    const result = await runDailyDigest(env);
    if (result.sent) {
      console.log('[cron] sent:', result.subject);
    } else {
      console.error('[cron] failed:', result.reason ?? result.error);
    }
  },
};
