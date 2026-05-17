# Viewer · Markdown Editor

> The biggest pane. Different renderer per file type, full WYSIWYG for Markdown in Pro.

## Renderers by file type

| Type | Renderer | Editing? |
|---|---|---|
| `.md` `.markdown` `.mdx` | WYSIWYG Markdown editor | Yes — full in Pro, read-only render in Easier |
| `.html` `.htm` | iframe sandbox + relative-asset inlining | View only (use Code view to edit source) |
| `.qmd` | Quarto render → iframe | View only |
| `.pdf` | PDF.js with text layer | Highlight + comment via Pro tools |
| `.docx` `.pptx` `.xlsx` | LibreOffice → PDF → render | View only |
| `.svg` | Inline render | Code view to edit |
| `.json` `.csv` `.tsv` | Table + tree view | View only |
| Images | Native `<img>` with zoom, fit, pan | — |
| Video / audio | Custom player (see below) | — |
| Source code | Highlighted code (Shiki) | Code view to edit |
| Unknown | Hex / text fallback | — |

## Markdown WYSIWYG (Pro)

The editor renders Markdown but you type *into the render*. The features below are what makes it feel like a normal word processor while still emitting clean Markdown.

### Block-level autocorrect

| You type | You get |
|---|---|
| `# ` | H1 |
| `## ` … `###### ` | H2 .. H6 |
| `> ` | Blockquote |
| ```` ``` ```` then Enter | Fenced code (Tab cycles language) |
| `--- ` then Enter | Horizontal rule |
| `- [ ] ` | Task list (unchecked) |
| `- [x] ` | Task list (checked) |

### Inline autocorrect

Closing delimiters turn the matched span into formatting:
`**bold**`, `*em*`, `_em_`, `` `code` ``, `~~strike~~`, `~sub~`, `^sup^` (Pandoc).

### Selection wrap

Select text, hit `*` `_` `` ` `` to wrap. Hit `[` `(` `{` `'` `"` to surround and re-select the inside.

### Engineering symbols

`-> <- => <-> <=> >= <= != +-` rewrite to `→ ← ⇒ ↔ ⇔ ≥ ≤ ≠ ±` (outside code blocks only).

### Links · ⌘K

Selection-aware link dialog. If a selection exists it pre-fills the text field. If the caret is inside an existing `<a>` you can edit the URL or *Remove* the link. Otherwise you get a fresh insert. The classic `[text](url.md)` autocorrect also still works.

### Code blocks

Caret inside a fenced block → top-right corner shows a **language picker** pill. Pick from a curated list or type freely. The selection round-trips to ```` ```python ```` etc. The list is fed by the Skill manifest, so any language a workspace skill registers shows up automatically.

### Images

Selected image → popover with *alt text* + *align* (left / center / right / none). Alignment writes inline `style` and turndown preserves it as raw `<img>` on save.

### Footnotes

`[^id]: body…` defines a footnote, `[^id]` references it. The editor renumbers and renders a `Footnotes` section at the end automatically. Round-trips through save/load.

### Paste

⌘V follows a fallback chain: image → HTML (sanitised to strip Word's `mso-*` and `<o:p>` junk, keeping only allowed tags) → text. ⌘⇧V always plain-text. WKWebView's `paste` event sometimes silent-fails on text — we fall back to `clipboard.readText()` automatically.

### Auto-save

Tab-level `$effect` watches `modified + rawContent`, 1.5 s debounce → write. Untitled tabs skip auto-save.

### Print / PDF

`Settings → Viewer → printHeader / printFooter` accept tokens `{filename} {date} {page} {pages}`. Empty string suppresses the line.

## PDF viewer

Continuous scroll, zoom controls in the toolbar, *Find in PDF* (⌘F), highlight tool with colour picker. Highlights persist to `<file>.pdf.highlights.json` next to the PDF — same companion-file pattern as elsewhere. Comments attach to a highlight and surface in the right margin.

## Video / audio player

Built-in player has:

- Scrubber with bookmark markers
- Speed control (0.5× → 2×)
- *Mark moment* (⌘B inside player) → append to `<file>.bookmarks.json`
- Transcript panel (if `<file>.transcript.json` sibling exists)
- Chapter strip below the seek bar (from `<file>.chapters.json`)
- AB-loop range tool

## Find bar

⌘F opens a find bar inside the viewer. ⏎ next, ⇧⏎ previous, ⌘G next. Highlights persist while open; close clears them. Live-incremental, regex toggle, case toggle.

## Next

- [Terminal →](Terminal.md)
- [Export →](Export.md)
