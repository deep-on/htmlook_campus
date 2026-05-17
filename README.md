# HTMLook Campus

<p align="center">
  <b>English</b> | <a href="README.ko.md">한국어</a> | <a href="README.ja.md">日本語</a> | <a href="README.de.md">Deutsch</a> | <a href="README.fr.md">Français</a> | <a href="README.es.md">Español</a> | <a href="README.pt.md">Português</a> | <a href="README.it.md">Italiano</a>
</p>

> An **8-step tutorial** for people new to HTMLook Pro. Walk one step at a time
> and you'll go from install → first file → BYOM → editing → command → save-as-skill
> → bundled profiles → writing your own profile in 30–40 minutes.

This repo tracks **HTMLook Pro v1.0 release-candidate** (GA mid 2026).
The desktop app is at [htmlook.app](https://htmlook.app) — 14-day free trial.
BYOM (Bring-Your-Own-Model) means zero token markup — Claude · GPT · Gemini ·
DeepSeek · Mistral · Together · Groq · Cerebras · Ollama, whichever model you
prefer, called directly with your own key.

## Tutorial Path

Top to bottom. Each step builds on the previous one.

| Step | Folder | What you do | Time |
|---|---|---|---|
| 1 | [`01-getting-started/`](01-getting-started/) | install · first launch · drag-drop · open folder | 3 min |
| 2 | [`02-first-file/`](02-first-file/) | md / html / pdf / video — 4 file types, split view, outline | 5 min |
| 3 | [`03-byom-setup/`](03-byom-setup/) | pick one vendor and register the key (or Ollama) | 5 min |
| 4 | [`04-editing/`](04-editing/) | element pick · region paint · sentence-id · cite anchor | 5 min |
| 5 | [`05-command/`](05-command/) | chat · terminal CLI · apply_edit · 26 persona walkthroughs | 10 min |
| 6 | [`06-save-as-skill/`](06-save-as-skill/) | capture a workflow → ⌘K catalog card | 5 min |
| 7 | [`07-bundled-profiles/`](07-bundled-profiles/) | HyperFrames · Slidev · Quarto · D2 · Astro Starlight · Marimo · Excalidraw · Manim | 5 min |
| 8 | [`08-extend/`](08-extend/) | write your own profile + submit a catalog PR | optional |

> If you just want a quick tour, see [`01-getting-started/LEARNING_PATH.md`](01-getting-started/LEARNING_PATH.md)
> for the step → video mapping. Each video is 30–70 seconds.

## Reference Manual (Wiki)

The 8-step tutorial shows you the flow *once, end-to-end*. The
[`wiki/`](wiki/) is the **feature-by-feature reference** you reach for
afterwards: Sidebar · Tabs · Viewer · Markdown editor · PDF · Video/Audio
player · Terminal · AI Assistant · Paint · Voice memos · Skill · Export ·
Settings · keyboard shortcuts. Two parallel tracks — one for human users,
one for AI assistants (MCP / schema).

| Track | Entry | Languages |
|---|---|---|
| Human-user manual | [`wiki/Home.md`](wiki/Home.md) · [Korean](wiki/Home-ko.md) | EN / KO |
| AI-assistant guide | [`wiki/AI-Overview.md`](wiki/AI-Overview.md) · [Korean](wiki/AI-Overview-ko.md) | EN / KO |

You walk the tutorial once; the wiki sits within arm's reach every day
(open it from the app via *Help → Documentation*).

## Editions

- **HTMLook Pro** (v1.0) — for power users. BYOM chat + built-in PTY terminal
  + CLI adapters (claude / codex / gemini) + MCP bridge + paint canvas +
  region capture + element pick + save-as-skill + 8 bundled profiles + 49 seeds.
- **HTMLook Easier** *(soon)* — entry-level edition, being redefined.

## Step 1 — Install + first launch

Start at [`01-getting-started/README.md`](01-getting-started/README.md).

Grab the .dmg from [htmlook.app](https://htmlook.app), drag to Applications,
and drag-drop your first file.

## Step 2 — First file (HTML / MD / PDF / video)

[`02-first-file/README.md`](02-first-file/README.md). Navigate four file
types with split view + outline + thumbnails.

Videos: BASIC #3 #4 #6 + ADV multi-pane / thumbnail / outline. mp4s
themselves live at [`videos/features/`](videos/features/).

## Step 3 — BYOM setup (just one vendor)

[`03-byom-setup/README.md`](03-byom-setup/README.md). For the full AI guide
see [`03-byom-setup/AI_GUIDE.md`](03-byom-setup/AI_GUIDE.md); a sample
configuration for an external MCP client is at
[`03-byom-setup/.htmlook/mcp-config.example.json`](03-byom-setup/.htmlook/mcp-config.example.json).

## Step 4 — Pointing *at* something on screen

[`04-editing/README.md`](04-editing/README.md). Four ways: element pick ·
region paint · sentence-id · range select. Anchor video: BASIC #5 ⭐ region-cite
(the AI entry point).

## Step 5 — Changing it through commands (cite + apply_edit)

[`05-command/README.md`](05-command/README.md). The deepest part of the
campus — 26 persona walkthroughs live at
[`05-command/personas/`](05-command/personas/) (grouped by role, each with a
follow-along WALKTHROUGH.md + before/after).

Persona catalog: [`05-command/personas/INDEX.md`](05-command/personas/INDEX.md).

## Step 6 — Repeated workflows → Skills

[`06-save-as-skill/README.md`](06-save-as-skill/README.md). Right-hand AI
panel, *Save as Skill* dialog. Three lines and you're done.

## Step 7 — The 8 Bundled Profiles

[`07-bundled-profiles/README.md`](07-bundled-profiles/README.md). HyperFrames /
Slidev / Quarto / D2 / Astro Starlight / Marimo / Excalidraw / Manim. The
profile seeds themselves live at [`profiles/`](profiles/) (the catalog.json
builder reads from there directly).

## Step 8 — Write your own Profile + video standard

[`08-extend/README.md`](08-extend/README.md). Build a profile for your own
domain and add it to the catalog. The video standard + reverse-verification
process is at [`08-extend/PRODUCTION.md`](08-extend/PRODUCTION.md); the
17-feature video catalog is at [`08-extend/FEATURES.md`](08-extend/FEATURES.md).

## Asset locations (reference)

Alongside the step folders (01~08), the campus root holds these *shared
asset directories* (catalog.json + the app reference them by path, so they
don't move into individual step folders):

| Folder | What |
|---|---|
| [`videos/`](videos/) | 17 feature mp4 + 26 persona mp4 (~340 MB total) |
| [`profiles/`](profiles/) | 8 profile seeds (`profile.json` + `SKILL.md` + `seed/`) |
| [`sample_workspaces/`](sample_workspaces/) | 75 domain seeds (`hf-*` 26 personas + 49 profile seeds) |
| [`catalog.json`](catalog.json) | 83 entries (8 profile + 75 workspace seed) — fresh-fetched by the app's Wizard (24 h cache) |
| [`scripts/`](scripts/) | `build-catalog.mjs` |
| [`infra/`](infra/) | license worker (separate service) |
| [`docs/`](docs/) | scratch space for generation artifacts (gitignored) |

## Two layers of learning — videos + interactive

The campus videos are *what (what's possible)*. The HTMLook Pro built-in
interactive walkthrough (*Help → Interactive Tutorials…*) is *how (how to do
it)*. Every one of the 17 features in the videos has a matching interactive
guide, one-to-one.

| Layer | Where | Length | Role |
|---|---|---|---|
| Video (campus) | `videos/features/`, `videos/` | 30 s / 60–70 s | shows the result |
| Interactive (app) | HTMLook Pro · Help → Interactive Tutorials… | 4 steps | hands-on practice |

## Reverse-verification promise

Every video in this campus only **claims things HTMLook actually does**.
Features that don't exist aren't advertised. Verification process + list of
fixed false claims: [`08-extend/PRODUCTION.md`](08-extend/PRODUCTION.md).

## Status

This repo tracks the **HTMLook Pro v1.0 release-candidate** (GA mid 2026)
as living teaching material. It will go public alongside v1.0 GA, when the
catalog endpoint (`htmlook.app/catalog`) starts fresh-fetching this repo's
raw URLs (24 h cache).

## License

- Code / walkthrough text: MIT
- Video mp4: CC BY 4.0 (attribute as *"HTMLook Campus"*)
- Sample content (PDF / xlsx / md / html): CC0 / public domain — all fictional placeholders
