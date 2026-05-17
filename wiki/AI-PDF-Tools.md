# PDF tools

> Reading text, citing pages, capturing regions, persistent highlights / comments.

## Read-only: text spans + region capture

### `pdf_text_spans`

Returns every text fragment of a page with screen-space coordinates (top-left origin, scale = 1):

```jsonc
{
  "tool": "htmlook_pdf_text_spans",
  "args": { "file_path": "/abs/path.pdf", "page": 3 }
}
```

```jsonc
{
  "file": "/abs/path.pdf",
  "page": 3,
  "viewport": { "width": 595, "height": 842 },
  "spans": [
    { "text": "Q3 Revenue", "x": 72, "y": 80, "w": 120, "h": 14, "font": "Helvetica-Bold" },
    …
  ]
}
```

Use it to "find the sentence that says X" — search the `spans` array yourself. `font` is optional; empty / whitespace-only spans are filtered.

### `capture_pdf_region`

Render a sub-rectangle of a page and return the cropped PNG (default scale 1.5 for crispness):

```jsonc
{
  "tool": "htmlook_capture_pdf_region",
  "args": {
    "file_path": "/abs/path.pdf",
    "page":  3,
    "rect":  { "x": 72, "y": 80, "w": 460, "h": 200 },   // optional, default = full page
    "scale": 1.5
  }
}
```

Returns the standard capture envelope (image content block + JSON sibling). Coordinates in the JSON sibling's `rect` are PDF-points at scale = 1; the renderer scales internally.

## Annotation: persistent highlights + comments

Annotations land in `<file>.pdf.highlights.json` next to the PDF — same companion-file pattern as elsewhere. They survive `mv` and travel with the workspace.

### `pdf_highlight_add`

```jsonc
{
  "tool": "htmlook_pdf_highlight_add",
  "args": {
    "file":  "/abs/path.pdf",
    "page":  3,
    "rect":  [72, 100, 200, 14],     // [x, y, w, h] — exactly 4 floats
    "color": "#fff59d",                // optional
    "note":  "key claim"               // optional
  }
}
```

- Argument is `file`, not `file_path`.
- `rect` is a single 4-tuple `[x, y, w, h]`, not an array of objects. One call → one rect → one highlight. Call multiple times if you need to highlight a multi-line span.
- Annotation label field is `note`, not `label`.

### `pdf_highlight_clear`

```jsonc
{ "tool": "htmlook_pdf_highlight_clear",
  "args": { "file": "/abs/path.pdf", "page": 3 } }
```

- Argument is `file`.
- `page` is optional — omit it to clear all pages.

### `pdf_comment_add`

```jsonc
{
  "tool": "htmlook_pdf_comment_add",
  "args": {
    "page":  3,
    "rect":  [72, 100, 200, 14],
    "note":  "Cites the wrong quarter.",
    "color": "#ffd54f"               // optional
  }
}
```

There's no `file_path` (uses the active PDF) and no `highlight_id` — you pass `page + rect + note` and the server creates the commented highlight in one shot. Field is `note`.

## Cite a page

### `pdf_citation_anchor`

Returns a link-sidecar entry for the given PDF page:

```jsonc
{
  "tool": "htmlook_pdf_citation_anchor",
  "args": {
    "pdf_path":    "/abs/path.pdf",        // NOT file_path
    "page":        3,
    "rect":        [72, 80, 460, 200],     // optional, narrows the citation
    "from_path":   "/abs/notes.md",        // optional, the citing file
    "from_anchor": "#sec-q3",              // optional
    "label":       "Q3 figures"            // optional
  }
}
```

Returns `{ id, total, path }` — the new entry's id (`L_*`), the updated total link count, and the absolute path of the link sidecar (e.g. `/abs/.htmlook/links.jsonl`). It does **not** return a `htmlook://` URL string. Resolve the link by reading the sidecar entry by `id`.

## What we don't include

- `pdf_figure_detect` — image / chart extraction (ML, deferred)
- `pdf_table_extract` — structured table out (ML, deferred)

If you need these, ask the user to run a separate tool (e.g. `tabula`) and `create_file` the JSON into the workspace; you can then `find_in_active` on the resulting file.

## Common loops

### "Read this paragraph"

```
pdf_text_spans → identify bbox covering the paragraph
capture_pdf_region with that bbox → PNG (image content block)
(pass the image to your reasoning step)
```

### "Mark and remember"

```
pdf_highlight_add → coloured rect persists
pdf_comment_add → explain why
(next session) pdf_highlight_clear if no longer relevant
```

### "Cite a page in a note"

```
pdf_citation_anchor → link entry id + sidecar path
agent_message_post body: "Q3 figures — see link <id>"
```

## Next

- [Audio / video tools →](AI-Audio-Video-Tools.md)
- [Prompt patterns →](AI-Prompt-Patterns.md)
