# Workspace

> Every folder you point HTMLook Pro at *is* a workspace. There's no database, no project file, no "import" step.

## The folder *is* the project

Open `~/Notes`, or your client folder, or an empty `~/Desktop/scratch`. That's a workspace. HTMLook Pro reads what's inside it, lays out tabs for the file types it recognises, and writes everything it generates *back into that folder* as plain files. Move the folder → the workspace moves with it. Send it to Dropbox / git / a USB stick → the workspace travels.

Drop multiple workspaces side-by-side: each one stays self-contained, with its own settings, AI permissions, and tool detection.

## File types HTMLook reads

| Category | Extensions |
|---|---|
| Web / structured | `.html`, `.htm`, `.svg`, `.json`, `.csv`, `.tsv` |
| Markdown family | `.md`, `.markdown`, `.mdx`, `.qmd` |
| Office (read-only render via LibreOffice / Quarto) | `.docx`, `.pptx`, `.xlsx` |
| PDF | `.pdf` |
| Images | `.png`, `.jpg`, `.jpeg`, `.gif`, `.webp`, `.avif`, `.heic` |
| Video | `.mp4`, `.mov`, `.webm` |
| Audio | `.m4a`, `.mp3`, `.wav`, `.aac` |
| Diagrams (via skills) | `.mmd` (Mermaid), `.d2` |
| Source (rendered as code) | most common languages |

Anything else opens in a hex/text fallback.

## Sidecar folders (the dot-prefixed siblings)

HTMLook keeps generated content in dot-prefixed folders next to your files. They are *yours* — version-control them or `.gitignore` them, your call.

| Sidecar | What lives there |
|---|---|
| `.htmlook/` | App-managed: `tools.json` (user-registered tools), `chat-history/`, `sketches/`, `agent-messages.jsonl`, `audit-log.jsonl`, paste assets, view-state snapshots |
| `.htmlook-voice/` | Voice memos (AAC `.m4a`) + matching `*.transcript.json` sidecars |
| `.claude/skills/` | Workspace-scoped skills, loaded into BYOM ChatPanel and the AI tool catalog |
| `.agents/skills/` | Cross-tool skills (Codex, Gemini, Aider compat) |

The global `~/.claude/skills/` (and `~/.agents/skills/`) is layered underneath — workspace files win on conflict.

## Companion files (next to your file)

For specific files HTMLook drops *sibling* files instead of using a sidecar — so the relationship is obvious in Finder and survives `mv`.

| Sibling pattern | Owner feature |
|---|---|
| `foo.mp4.segments.json` | audio/video segment markers |
| `foo.mp4.chapters.json` | video chapters |
| `foo.mp4.bookmarks.json` | review markers / scrub bookmarks |
| `foo.pdf.highlights.json` | PDF highlights + comments |
| `foo.m4a.transcript.json` | voice memo transcript |
| `foo.html.draft.md` | Markdown round-trip draft |

## Multi-window, multi-workspace

`File → New Window` (⌘N) opens a second independent window. Each window pins to one workspace root, has its own tab list, terminal panel, and ChatPanel. Two windows can sit on the same workspace without stepping on each other — file-watcher events propagate, sidecars are append-only.

## HyperFrames (lightweight cross-file links)

Inside a workspace, files can reference each other with `htmlook://` links: `[See the regression plot](htmlook://regression-results.html#sec-q3)` opens the target file in the same window, scrolling to the anchor. This is the substrate for the persona-video demo workflows — same workspace, multiple lenses.

## What gets synced to the cloud

Nothing, unless you opt in. No telemetry, no workspace upload. The only outbound traffic from a default install is:

- Auto-update check to `htmlook-releases.kdk3606.workers.dev/pro/latest.json`
- Whatever BYOM provider you configured (OpenAI, DeepSeek, etc.) when you actively use ChatPanel

You can run HTMLook Pro fully offline by skipping BYOM setup and the auto-update check.

## Next

- [UI Overview →](UI-Overview.md)
- [Pro vs Easier →](Pro-vs-Easier.md)
