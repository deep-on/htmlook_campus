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

    return new Response('not found', { status: 404, headers: cors });
  },
};
