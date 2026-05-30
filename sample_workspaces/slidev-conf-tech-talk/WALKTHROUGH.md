# Conf Tech Talk Walkthrough · 30-min Walkthrough

> 🌟 **Wave A · High Quality** — marketing / demo asset. Suitable for direct demo recording.

## 1. Run the slides
```bash
pnpm install
pnpm dev   # http://localhost:3030
```

## 2. Pane pair · live HMR
- Left: edit slides.md
- Right: localhost:3030
- Changes reflect in the slides instantly

## 3. Presentation build
- `slidev export --output talk.pdf` — includes speaker notes
- `slidev build` — static site for archive
