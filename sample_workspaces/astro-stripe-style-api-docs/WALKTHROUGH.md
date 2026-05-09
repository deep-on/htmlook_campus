# Stripe-style API Docs Walkthrough · 30-min Walkthrough

> 🌟 **Wave A · High Quality** — 마케팅 / 데모 자산. 직접 demo recording 가능.

## 1. 사이트 실행
```bash
pnpm install
pnpm dev   # http://localhost:4321
```

## 2. 새 endpoint 추가 (multi-target 시그니처)
1. `src/content/docs/orders/cancel.md` 신규
2. AI: "create.md 와 같은 형식으로 cancel endpoint 작성 + 사이드바 등록"
3. AI 가 .md + astro.config.mjs 동시 수정

## 3. 빌드 + 배포
- `pnpm build` → static site
- Cloudflare Pages / Vercel 즉시 배포 가능
