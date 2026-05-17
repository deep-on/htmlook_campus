# Settings

> ⌘, opens the Settings dialog. Eight sections, the last six only appear in Pro.

## Sections

| Section | Where the controls live |
|---|---|
| **General** | Theme (System / Light / Dark), On launch (restore last session / start empty), language (auto + 한국어 + English + others), accent colour swatches (Default / Feature Accents / Persona Tones) |
| **Viewer** | Viewer theme (Built-in / From Persona Videos / Feature Accents), font family + size, OpenType features, print header / footer tokens (`{filename}` `{date}` `{page}` `{pages}`), dual-view sync-scroll default, code-view default for `.md` |
| **Files** | Workspace defaults, sidebar follow-active-file toggle, hide-dotfiles toggle, default sort, search exclusions |
| **Terminal** (Pro) | Preset commands (Claude / Codex / Gemini / Shell), Warp-style inline-suggest toggle, zsh-autosuggestions install button, terminal font + size, cursor style, OSC 7 cwd handling |
| **AI** (Pro) | BYOM providers — add / edit / remove. Each provider holds base URL + key + default model + vision toggle. Permission ledger lives here too (per-tool / per-workspace / global decisions you can revoke) |
| **Tools** (Pro) | The `tools.json` editor — built-in tools (Mermaid, D2, Quarto, LibreOffice, …), add-wizard for custom tools, tier badges, install dependencies via Homebrew |
| **Plans** | Subscription state (Easier) / Pro Solo trial state (Pro), upgrade buttons, license keys |
| **About** | Version, "Check for updates" button (Pro), system dependencies status (LibreOffice detected ✓ / not detected ●), library credits (pdf.js, LibreOffice for PPTX) |

## Scope: workspace vs global

Some settings — font size, accent color, code-view default, terminal preset commands, default sort — are *global* (apply to every workspace). Others — sidebar visibility, last-opened tab, tool permissions, AI provider state — are *workspace-scoped* and live inside the workspace's `.htmlook/` folder.

The dialog labels each control accordingly. Workspace overrides fall back to the global value when cleared.

## "Check for updates"

About → Check for updates does an explicit check now (Pro auto-checks on launch). A *Download & install* button appears when a newer build is signed and ready. Click → background download → relaunch.

If macOS Sequoia or later blocks the swap, the modal points you to **System Settings → Privacy & Security → App Management** with a button that opens the right pane.

## CLI tools (Pro only)

Tools → *+Add* opens the custom-tool wizard. Below it, *Install dependencies* triggers Homebrew with a streaming log modal. The same plumbing handles `brew install ffmpeg`, `brew install --cask libreoffice`, `brew install --cask quarto`, `brew install pandoc`, `pipx install <pkg>`, `npm i -g <pkg>` — pick the tool, click *Install*, watch the log.

Homebrew not installed yet? The first install offers to install Homebrew first (~3 minutes).

## Sign-in vs accounts

There is no sign-in on Pro. The only "account" is whichever AI provider you point Pro at in the AI section. Easier has a subscription account managed under Plans.

## Reset

About → Reset confirms, then clears settings. Workspace data (your files, sidecars, voice memos, sketches) stays intact — Reset only touches the app's own preferences.

## Next

- [Keyboard shortcuts →](Keyboard-Shortcuts.md)
- [Troubleshooting →](Troubleshooting.md)
