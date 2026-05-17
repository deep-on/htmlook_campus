# Export

> One menu, every format. Extension-extensible.

## Where to find it

Top-right of the viewer toolbar: a download icon. Click → format dropdown.

## Built-in formats

| Format | Icon | What you get |
|---|---|---|
| **PDF** | file | print-rendered PDF of the active tab |
| **Print** | printer | OS print dialog (same renderer as PDF) |
| **DOCX** | file | best-effort Word doc (requires Pandoc) |
| **Markdown** | file | clean Markdown from any renderer |
| **Markdown (Smart)** | feather | polished Markdown — heuristic cleanup, footnote restoration (requires Pandoc) |
| **HTML** | code | self-contained `.html` with inlined assets |

## Extension-registered formats

Below the divider, the dropdown lists every format an installed Extension adds. With the default set you'll see:

- **mp4** — animated SVG → mp4
- **svg** — diagram passthrough
- **pptx** — slide deck from your Markdown headings (requires LibreOffice)

The list updates live when Extensions are added or removed.

## Print header / footer

*Settings → Viewer → Print header* and *Print footer* accept tokens — `{filename}`, `{date}`, `{page}`, `{pages}`. Empty string skips that line.

These flow into both Print and PDF export with identical wording.

## Per-file destination

Each export prompts for a destination on first use. The directory is remembered per format per workspace — your next PDF goes into the same folder unless you change it.

## Round-trip

`Markdown` and `Markdown (Smart)` round-trip with the WYSIWYG editor — open the exported `.md`, edit it, save, and you get the same Markdown back (modulo whitespace).

`HTML` export inlines relative `<img src>` / `<script src>` / `<link href>` so the resulting file is self-contained — easy to email or attach.

## Missing a format?

If the dropdown is missing a format you expect, the underlying external tool may not be installed. Open *Settings → Tools* — the row with a dim ring next to the format's tool (LibreOffice for PPTX, Pandoc for Smart Markdown, etc.) has a one-click *Install* button.

## Next

- [Settings →](Settings.md)
- [Keyboard shortcuts →](Keyboard-Shortcuts.md)
