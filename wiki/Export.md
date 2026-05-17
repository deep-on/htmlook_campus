# Export

> One menu, every format. Skill-extensible.

## Where to find it

Top-right of the viewer toolbar: a download icon. Click → format dropdown. Keyboard: ⌘E (Export menu) → ⏎ on the desired format.

## Built-in formats

| Format | Icon | What you get |
|---|---|---|
| **PDF** | file | print-rendered PDF of the active tab |
| **Print** | printer | OS print dialog (same renderer as PDF) |
| **DOCX** | file | best-effort Word doc (pandoc) |
| **Markdown** | file | clean Markdown from any renderer (turndown-driven) |
| **Markdown (Smart)** | feather | pandoc-polished Markdown — heuristic cleanup, footnote restoration |
| **HTML** | code | self-contained `.html` with inlined assets |

## Skill-registered formats (dynamic)

Below the divider, the dropdown lists every format declared by a loaded skill. v1.0.9 ships these:

- **mp4** — animated SVG → mp4 (via the SVG-animate skill)
- **svg** — passthrough export of a rendered diagram
- **pptx** — slide deck from headings (Slide-Deck skill)

The list updates live when skills are added or removed.

## Print header / footer

`Settings → Viewer → printHeader` and `printFooter` accept tokens — `{filename}`, `{date}`, `{page}`, `{pages}`. Empty string skips that line.

These flow into the `@page @top-center` / `@bottom-center` CSS rules that the renderer attaches before the print render. Identical wording in PDF export and Print.

## Per-file destination

Each export prompts for a destination on first use. The directory is remembered per format per workspace — your next PDF goes into the same folder unless you change it.

## MCP-exposed export

- `htmlook_export_active { format }` — kicks off the same export pipeline programmatically. The `format` argument matches the dropdown's internal key (`pdf`, `print`, `docx`, `md`, `smart-md`, `html`, plus any skill-registered key).

The tool returns the absolute path of the written file. A user-facing toast appears when a non-interactive export finishes.

## Round-trip

`Markdown` and `Markdown (Smart)` round-trip with the WYSIWYG editor — open the exported `.md`, edit it, save, and you get the same markdown back (modulo whitespace).

`HTML` export uses the same inline-assets pipeline the viewer uses internally — relative `<img src>`, `<script src>`, `<link href>` are inlined so the resulting file is self-contained.

## Next

- [Settings →](Settings.md)
- [Keyboard shortcuts →](Keyboard-Shortcuts.md)
