# Viewer · Markdown Editor

> The biggest pane. Different renderer per file type, full WYSIWYG for Markdown in Pro.

![Viewer with Preview / Source / Split toggles](images/04-viewer.png)

## Renderers by file type

| Type | Renderer | Editing? |
|---|---|---|
| `.md` `.markdown` `.mdx` | WYSIWYG Markdown editor | Yes — full in Pro, read-only render in Easier |
| `.html` `.htm` | Self-contained iframe (relative assets inlined) | View only (use Source view to edit raw HTML) |
| `.qmd` | Quarto render → iframe | View only |
| `.pdf` | PDF renderer with text layer | Highlight + comment in Pro |
| `.docx` `.pptx` `.xlsx` | LibreOffice → PDF → render | View only |
| `.svg` | Inline render | Source view to edit |
| `.json` `.csv` `.tsv` | Table + tree view | View only |
| Images | Native viewer with zoom, fit, pan | — |
| Video | Custom player (see below) | — |
| Audio (`.m4a` etc.) | Generic "Preview not available" card. Voice memos play through the doc-bound **Voice Player** drawer — open the document the memo was recorded against (see [Voice memos](Voice-Memos.md)). | — |
| Source code | Syntax-highlighted code | Source view to edit |
| Unknown | Hex / text fallback | — |

## Markdown WYSIWYG (Pro)

The editor *renders* Markdown but you *type into the render*. It feels like a normal word processor while still emitting clean Markdown.

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
`**bold**`, `*em*`, `_em_`, `` `code` ``, `~~strike~~`, `~sub~`, `^sup^`.

### Selection wrap

Select text, hit `*` `_` `` ` `` to wrap. Hit `[` `(` `{` `'` `"` to surround and re-select the inside.

### Engineering symbols

Outside code blocks, `-> <- => <-> <=> >= <= != +-` rewrite to `→ ← ⇒ ↔ ⇔ ≥ ≤ ≠ ±`.

### Links — ⌘K

Selection-aware link dialog. If a selection exists it pre-fills the text field. If the caret is inside an existing `<a>` you can edit the URL or *Remove* the link. Otherwise you get a fresh insert. The classic `[text](url.md)` autocorrect also still works.

### Code blocks

Caret inside a fenced block → top-right corner shows a **language picker**. Pick from a curated list or type freely. The selection round-trips to ```` ```python ```` etc. Any language an Extension registers appears in the picker automatically.

### Images

Selected image → popover with *alt text* + *align* (left / center / right / none). Alignment writes inline style so it round-trips through Markdown save/load.

### Footnotes

`[^id]: body…` defines a footnote, `[^id]` references it. The editor renumbers and renders a `Footnotes` section at the end automatically. Round-trips through save / load.

### Paste

⌘V tries image → HTML (sanitised — Word's clutter is stripped) → text. ⌘⇧V always plain-text.

### Auto-save

1.5 s after the last keystroke, the file writes. Untitled tabs skip auto-save and ask for a destination on ⌘S.

### Print / PDF header & footer

*Settings → Viewer → Print header / Print footer* accept tokens — `{filename}`, `{date}`, `{page}`, `{pages}`. Empty string suppresses the line.

## PDF viewer

Continuous scroll, zoom controls in the toolbar, *Find in PDF* (⌘F), highlight tool with colour picker. Highlights persist next to the PDF, so they travel when you move or share the file. Comments attach to a highlight and show in the right margin.

## Video / audio player

Built-in player:

- Scrubber with bookmark markers
- Speed control (0.5× → 2×)
- *Mark moment* — append to the file's bookmark sidecar
- Transcript panel — appears when a transcript sidecar exists
- Chapter strip below the seek bar
- AB-loop range tool

## Find bar

⌘F inside the viewer. ⏎ next, ⇧⏎ previous, ⌘G next. Live-incremental, regex toggle, case toggle. Closing clears the highlights.

## Next

- [Terminal →](Terminal.md)
- [Export →](Export.md)
