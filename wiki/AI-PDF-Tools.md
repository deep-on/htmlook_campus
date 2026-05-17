# PDF tools

> Six tools cover reading text, citing pages, capturing regions, and adding persistent highlights / comments.

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

Use it to "find the sentence that says X" — search the `spans` array yourself; PDF.js's getTextContent is what powers it. Empty / whitespace-only spans are filtered.

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

Returns the same envelope as other capture tools: `{ base64, width, height, page, rect, scale }`. Coordinates are PDF-points; the renderer scales internally.

## Annotation: persistent highlights + comments

Annotations land in `<file>.pdf.highlights.json` next to the PDF — same companion-file pattern as elsewhere. They survive `mv` and travel with the workspace.

### `pdf_highlight_add`

```jsonc
{
  "tool": "htmlook_pdf_highlight_add",
  "args": {
    "file_path": "/abs/path.pdf",
    "page":  3,
    "rects": [
      { "x": 72, "y": 100, "w": 200, "h": 14 }
    ],
    "color": "#fff59d",
    "label": "key claim"
  }
}
```

Multiple `rects` group as one highlight (useful when text spans lines).

### `pdf_highlight_clear`

```jsonc
{ "tool": "htmlook_pdf_highlight_clear",
  "args": { "file_path": "/abs/path.pdf", "page": 3 } }
```

Page-scoped clearance.

### `pdf_comment_add`

```jsonc
{
  "tool": "htmlook_pdf_comment_add",
  "args": {
    "file_path": "/abs/path.pdf",
    "highlight_id": "h_5f8e",         // returned by pdf_highlight_add
    "comment": "Cites the wrong quarter."
  }
}
```

Comments are attached to a highlight (you can have many per highlight). The viewer renders them in the right margin.

## Cite-a-page

### `pdf_citation_anchor`

Emit a `htmlook://` link that, when followed, opens the PDF at the same page + viewport you're seeing:

```jsonc
{ "tool": "htmlook_pdf_citation_anchor",
  "args": { "file_path": "abs/path.pdf", "page": 3 } }
```

Returns `htmlook://abs/path.pdf#page=3`. Drop the resulting link into a Markdown note, a chat message, or another viewer's content.

## What we don't include

- `pdf_figure_detect` — image / chart extraction (ML, deferred to v1.0.10+)
- `pdf_table_extract` — structured table out (ML, deferred)

If you need these, ask the user to run a separate tool (e.g. `tabula`) and `create_file` the JSON into the workspace; you can then `find_in_active` on the resulting file.

## Common loops

### "Quote and cite"

```
pdf_text_spans → find sentence
pdf_citation_anchor → link
agent_message_post (body: quote + link) → user can click through
```

### "Read this paragraph"

```
pdf_text_spans → identify bbox covering the paragraph
capture_pdf_region with that bbox → PNG
(pass the PNG as a vision content block to your LLM)
```

### "Mark and remember"

```
pdf_highlight_add → coloured rect persists
pdf_comment_add → explain why
(next session) pdf_highlight_clear if no longer relevant
```

## Next

- [Audio / video tools →](AI-Audio-Video-Tools.md)
- [Prompt patterns →](AI-Prompt-Patterns.md)
