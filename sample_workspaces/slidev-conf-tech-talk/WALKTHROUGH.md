# Conf Tech Talk Walkthrough · 30-min Walkthrough

> 🌟 **Wave A · High Quality** — 마케팅 / 데모 자산. 직접 demo recording 가능.

## 1. 슬라이드 실행
```bash
pnpm install
pnpm dev   # http://localhost:3030
```

## 2. Pane pair · live HMR
- 좌: slides.md 편집
- 우: localhost:3030
- 변경 즉시 슬라이드 반영

## 3. 발표용 빌드
- `slidev export --output talk.pdf` — speaker notes 포함
- `slidev build` — static site for archive
