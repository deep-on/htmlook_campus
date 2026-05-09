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

    return new Response('not found', { status: 404, headers: cors });
  },
};
