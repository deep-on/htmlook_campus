# htmlook-campus-counter

Cloudflare Worker — anonymous install / like counter for htmlook_campus seeds.

## Deploy

```bash
cd infra/counter-worker
npx wrangler login
npx wrangler kv:namespace create COUNTERS
# paste returned id into wrangler.toml
npx wrangler deploy
```

Endpoint: `https://<your-subdomain>.workers.dev` or custom domain `htmlook.app/api/counter`.

## Custom domain (recommended)

Map `counter.htmlook.app` → this Worker via Cloudflare Pages route or Worker Routes.

## Env

- `ALLOWED_ORIGINS` — comma-separated allowlist (default: htmlook.app + localhost dev ports)
- `COUNTERS` — KV namespace (auto-bound)

## Privacy

- No PII stored. IP only used for like-vote 24h dedup (hashed in KV key, expires).
- No request body parsed.
- Counter resets are admin-only (KV CLI).

## Read API

```
GET https://counter.htmlook.app/c/quarto-financial-analysis
→ { "seed": "...", "installs": 42, "likes": 7 }

GET https://counter.htmlook.app/counts
→ bulk { seed: { installs, likes }, ... }  // cached 5min
```

## Wired into HTMLook

`src-tauri/src/pro_features/campus_catalog.rs` — `campus_template_install` fires
fire-and-forget POST to `/c/<seed>` after successful install. Result cached in
catalog metadata refresh.
