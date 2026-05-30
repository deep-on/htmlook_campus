# Stripe-style API Docs Walkthrough · 30-min Walkthrough

> High-quality marketing / demo asset for the fictional **Vellum** commerce API. Ready for direct demo recording.

## 1. Run the site

```bash
pnpm install
pnpm dev   # http://localhost:4321
```

## 2. Add a new endpoint (multi-target signature)

1. Create `src/content/docs/orders/cancel.md`.
2. Ask the AI: "write a cancel endpoint in the same format as create.md and register it in the sidebar".
3. The AI edits the .md and astro.config.mjs together.

## 3. Build + deploy

- `pnpm build` → static site
- Deploy instantly to Cloudflare Pages / Vercel.
