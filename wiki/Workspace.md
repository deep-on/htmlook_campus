# Workspace

> Every folder you point HTMLook Pro at *is* a workspace. There's no database, no project file, no "import" step.

## The folder *is* the project

Open `~/Notes`, or your client folder, or an empty `~/Desktop/scratch`. That's a workspace. HTMLook Pro reads what's inside, lays out tabs for the file types it recognises, and writes anything it generates *back into that folder* as plain files. Move the folder → the workspace moves with it. Send it to Dropbox / git / a USB stick → the workspace travels.

Drop multiple workspaces side-by-side: each one stays self-contained, with its own settings and tool detection.

## File types HTMLook reads

| Category | Extensions |
|---|---|
| Web / structured | `.html`, `.htm`, `.svg`, `.json`, `.csv`, `.tsv` |
| Markdown family | `.md`, `.markdown`, `.mdx`, `.qmd` |
| Office (read-only render) | `.docx`, `.pptx`, `.xlsx` (LibreOffice / Quarto must be installed) |
| PDF | `.pdf` |
| Images | `.png`, `.jpg`, `.jpeg`, `.gif`, `.webp`, `.avif`, `.heic` |
| Video | `.mp4`, `.mov`, `.webm` |
| Audio | `.m4a`, `.mp3`, `.wav`, `.aac` |
| Diagrams (via Extensions) | `.mmd` (Mermaid), `.d2` |
| Source code (rendered as code) | most common languages |

Anything else opens in a hex / text fallback.

## What HTMLook keeps next to your files

HTMLook keeps anything it generates as plain files in your workspace — so you can see it, version-control it, or `.gitignore` it as you prefer.

| Path | What lives there |
|---|---|
| `.htmlook/` | App-managed: sketches you draw, chat history, configuration, paste assets |
| `.htmlook-voice/` | Voice memos (`.m4a`) + optional transcript siblings |

For specific files HTMLook drops a *sibling* file next to it instead — so the relationship is obvious in Finder and survives `mv`.

| Sibling pattern | What it stores |
|---|---|
| `foo.m4a.transcript.json` | Voice memo transcript |
| `foo.pdf.highlights.json` | PDF highlights + comments |
| `foo.mp4.chapters.json` | Video chapters |
| `foo.mp4.bookmarks.json` | Video scrub bookmarks |

## Multi-window, multi-workspace

*File → New Window* (or ⌘⌥⇧N in Pro) opens a second independent window. Each window pins to one workspace root, has its own tab list, terminal, and AI Assistant. Two windows can sit on the same workspace without stepping on each other — file changes propagate.

## Cross-file links (HyperFrames)

Inside a workspace, files can reference each other. Click a `htmlook://` link in any file (`[See the plot](htmlook://results.html#sec-q3)`) and the target file opens in the same window, scrolled to the anchor. Useful for stitching report + raw data + chart into one navigable flow.

## What gets synced to the cloud

Nothing, unless you opt in. No telemetry, no workspace upload. The only outbound traffic from a default install is:

- The auto-update check on launch
- Whatever AI provider you configured (OpenAI, DeepSeek, etc.) when you actively use the AI Assistant

You can run HTMLook Pro fully offline by skipping AI provider setup.

## Next

- [UI Overview →](UI-Overview.md)
- [Quick start →](Quick-Start.md)
