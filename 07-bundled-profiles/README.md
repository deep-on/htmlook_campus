# Step 7 · Bundled Profiles (HyperFrames / Slidev + 6 more)

<p align="center">
  <b>English</b> | <a href="README.ko.md">한국어</a> | <a href="README.ja.md">日本語</a> | <a href="README.de.md">Deutsch</a> | <a href="README.fr.md">Français</a> | <a href="README.es.md">Español</a> | <a href="README.pt.md">Português</a> | <a href="README.it.md">Italiano</a>
</p>

> v1.0 ships with 8 *heavyweight Profiles* baked into the app. On first
> launch they auto-unpack to `~/.htmlook/profiles/_bundled-*`.
> ~ 5 min (just a tour — actually using each one is a tool-specific
> learning curve).

A Profile = external tool + Skill v0.3 bundle + seed content,
packaged together. Install it with one click from the New Workspace
Wizard (⌘⇧N) or a card in the Add wizard.

> The profile manifests themselves (profile.json + SKILL.md + seed/)
> live at [`../profiles/`](../profiles/) in the campus root — the
> catalog.json builder reads from there directly. This step is the
> guided tour around them.

## 7.1 · The 8 profile cards

| Profile | Category | Output | Tool license | Start at |
|---------|----------|--------|--------------|----------|
| HyperFrames | motion-graphics | mp4 (kinetic typography) | MIT | [`../profiles/hyperframes/`](../profiles/hyperframes/) |
| Slidev | presentation | HTML/PDF slides | MIT | [`../profiles/slidev/`](../profiles/slidev/) |
| Quarto | publishing | PDF/HTML/PPT/book | GPL-2.0 | [`../profiles/quarto/`](../profiles/quarto/) |
| D2 | diagram | SVG | MPL-2.0 | [`../profiles/d2/`](../profiles/d2/) |
| Astro Starlight | documentation | docs site | MIT | [`../profiles/astro-starlight/`](../profiles/astro-starlight/) |
| Marimo | notebook | reactive HTML | Apache-2.0 | [`../profiles/marimo/`](../profiles/marimo/) |
| Excalidraw | diagram | JSON/SVG/PNG | MIT | [`../profiles/excalidraw/`](../profiles/excalidraw/) |
| Manim | educational-animation | mp4 | BSD-3-Clause | [`../profiles/manim/`](../profiles/manim/) |

> **HTMLook does not bundle the tools themselves.** It ships the usage
> guides and Wizard integration. Each external tool is installed
> separately (the profile READMEs spell out the dependencies).

## 7.2 · Pick one and start

If this is your first time, go light:

- **Slidev** — `npx slidev` to install. One md file → HTML slides.
- **D2** — install a Go binary. txt → SVG diagram.
- **Excalidraw** — no install needed (HTMLook ships an in-app viewer).

The heavier ones:

- **HyperFrames** — Node + ffmpeg + Kokoro TTS (Python). The very tool
  the campus videos were made with.
- **Manim** — Python + LaTeX. Mathematical animation.
- **Quarto** — R / Python / Pandoc. Academic publishing.

## 7.3 · Install from the Add wizard

1. ⌘⇧N (New Workspace Wizard) or *+* in the sidebar (Add wizard).
2. Pick the profile card you want from the catalog.
3. *Install* — the seed folder is copied to your home directory.
4. *Open* — HTMLook opens that folder as a workspace and the profile's
   Skills land in the ⌘K catalog.

## 7.4 · Extra domain seeds (optional)

On top of the 8 profiles there are 75 workspace seeds in
[`../sample_workspaces/`](../sample_workspaces/) — every one is
prefixed so you can tell which profile it seeds at a glance:

- `hf-*/` (26 — HyperFrames, the full persona lineup used to produce
  the campus videos)
- `slidev-*/` (7) · `quarto-*/` (7) · `marimo-*/` (7) · `manim-*/` (7)
- `d2-*/` (7) · `excalidraw-*/` (7) · `astro-*/` (7)

`hf-claude/` and `hf-llama/` are the BYOM reference paths (Anthropic
Claude / local Llama). The other 24 (`hf-corp-deck/`,
`hf-teacher-quiz/`, `hf-kid-coding/`, …) are domain scenarios. Each
seed ships `index.html + hyperframes.json + brand.txt + prompts.txt
+ AGENTS.md + meta.json + README.md` as a full set, so an AI agent
can faithfully replay the workflow with the user's own BYOM model.

Full catalog: [`../catalog.json`](../catalog.json) — currently **83
entries** (8 profile + 75 workspace seed). The CI rebuilds it
automatically ([`../scripts/build-catalog.mjs`](../scripts/build-catalog.mjs)).

## ✅ Step 7 checkpoint

- You read one of the 8 profile READMEs.
- (Optional) You installed one external tool → used the Add wizard to
  install that profile's seed.
- (Optional) You browsed one seed in `sample_workspaces/` that's close
  to your domain.

All done? → [Step 8 · extend (writing your own Profile)](../08-extend/)

## Further reading

- The `SKILL.md` in each profile folder — the Skill v0.3 manifest the
  profile registers.
- [`../08-extend/PRODUCTION.md`](../08-extend/PRODUCTION.md) — the
  standard for producing campus videos with HyperFrames (all 17 + 26
  campus videos were made with this tool).
