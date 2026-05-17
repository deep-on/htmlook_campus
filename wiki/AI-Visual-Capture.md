# Visual Capture

> Read what the user actually sees. Most powerful when chained with `apply_edit` + `capture_diff`.

## The capture surface

| Tool | Use when |
|---|---|
| `capture_viewport` | You need the whole active pane |
| `capture_selector` | You can name a CSS selector |
| `capture_active_element` | The user just clicked an element; capture that |
| `capture_text_match` | You can quote a visible string |
| `capture_rect` | You know coordinates |
| `capture_diff` | Compare two PNGs you just captured |
| `capture_video_frame_region` | A sub-region of the active video at a given time |
| `capture_pdf_region` | A sub-rectangle of a PDF page |
| `region_current_png` | Re-fetch the last region the user manually captured |

## Return envelope

Every image-bearing tool returns **two MCP content blocks** plus a JSON sibling text block:

- one `image/png` content block with the bitmap
- one `text` content block with a JSON object describing the capture

The JSON sibling's shape is **flat** (no nested `scope`) and stripped of `base64` (the PNG is the image block, not duplicated in JSON):

```jsonc
{
  "pane":      "active",     // "active" | "primary" | "secondary"
  "full_page": false,         // true if the page was rendered as one tall image
  "width":     1280,
  "height":    720,
  // per-tool extras follow, flat at the top level:
  "selector":      ".hero",      // capture_selector
  "match_count":   1,             // capture_selector / _text_match
  "matched_index": 0,             // _text_match / _selector when multiple
  "text":          "Sign up",     // _text_match
  "tag":           "BUTTON",      // _active_element
  "rect":          { "x":0,"y":0,"w":300,"h":120 }, // _rect / _video_frame_region
  "timestamp_sec": 14.7,          // _video_frame_region
  "page":          3,             // _pdf_region
  "scale":         1.5            // _pdf_region
}
```

Note: there is no `mime` field, no `captured_at`, no `scope` wrapper — these were misdocumented in earlier drafts.

## The "before / after" pattern

```text
1. capture_selector(".cta") → before.png + JSON sibling
2. plan the edit
3. apply_edit(path, find, replace)
4. (viewer reload event fires automatically)
5. capture_selector(".cta") → after.png
6. capture_diff(before_base64, after_base64, threshold)
```

## capture_diff

```jsonc
{
  "tool": "htmlook_capture_diff",
  "args": {
    "before_base64": "iVBORw0…",
    "after_base64":  "iVBORw0…",
    "threshold":     0.1                  // optional, default 0.1
  }
}
```

Returns image + JSON:

```jsonc
{
  "width":         1280,
  "height":        720,
  "changed_pixels": 234,
  "total_pixels":   921600,
  "changed_ratio":  0.00025,
  "bbox":           [120, 480, 160, 40],   // optional [x, y, w, h]
  "threshold":      0.1
}
```

No `did_change` field — infer from `changed_pixels > 0` or `bbox != null`. The image block holds a visualisation of the diff.

## visual_overlap_check

Returns layout issues on the active pane:

```jsonc
{
  "pane":     "active",
  "viewport": { "w": 1280, "h": 720 },
  "scanned":  142,
  "issues": [
    {
      "kind":   "text-truncation",        // | horizontal-overflow | vertical-overflow | zero-size | element-overlap
      "tag":    "H1",
      "text":   "Welcome to…",
      "bbox":   { "x": 120, "y": 80, "w": 400, "h": 32 },
      "detail": "text-overflow: ellipsis"
    }
  ]
}
```

Field is `bbox`, not `rect`. Kind values are hyphenated as listed above (`text-truncation`, not `text-truncated`).

## layout_map

Returns one flat list of structural entries, tagged by `kind`:

```jsonc
{
  "pane":     "active",
  "viewport": { "w": 1280, "h": 720 },
  "entries": [
    { "kind": "landmark", "tag": "HEADER",  "bbox": { "x":0,"y":0,"w":1280,"h":80 }, "selector": "header" },
    { "kind": "heading",  "tag": "H1",      "bbox": {…}, "text": "Hello",  "selector": "h1" },
    { "kind": "button",   "tag": "BUTTON",  "bbox": {…}, "text": "Sign up", "selector": "#cta button:nth-child(1)" },
    { "kind": "link",     "tag": "A",       "bbox": {…}, "text": "Pricing","href": "/pricing", "selector": "nav a:nth-child(2)" },
    { "kind": "image",    "tag": "IMG",     "bbox": {…}, "src": "hero.png","selector": "img.hero" }
  ],
  "total":     142,
  "truncated": false
}
```

Run it once at the start of a session to "see the page". One iteration may be capped — check `truncated`.

## select_element + capture_active_element

```text
select_element({ selector: ".cta button" })
  → returns { selector, matched_index, match_count, tag, id, class, bbox }
capture_active_element({ padding: 8 })
  → captures the selected element with N px padding around its bbox
```

## Rate limit

Capture tools use a token-bucket of 8 burst, 8 refill / sec, **keyed per tool name** (so `capture_viewport` and `capture_selector` have independent buckets). On exhaustion you get a plain-text error
`rate-limited: <tool_name> burst exhausted. Retry after ~<ms> ms.` Back off the specified ms.

## Failure modes

| Message prefix | Meaning |
|---|---|
| `selector "<sel>" matched no elements in <pane> pane` | The selector resolved zero nodes |
| `text "<t>" not found in <pane> pane (mode=<mode>)` | The text-match tool's query string isn't on screen |
| `no <pane> viewer pane available — open a file first` | The targeted pane isn't mounted |
| `<pane> viewer is not same-origin…` | iframe srcdoc / asset:// barrier blocks DOM access |
| `rate-limited: <tool_name> burst exhausted…` | Token bucket exhausted |

## When *not* to capture

- **Don't capture to "understand layout"** if `layout_map` answers the question. Smaller, deterministic.
- **Don't capture twice in a row** without an intervening change — your second call gives the same PNG.
- **Don't capture the viewport** when you can name an element. Tight crops are smaller and the diff is more useful.

## Next

- [Apply-edit round-trip →](AI-Apply-Edit.md)
- [Prompt patterns →](AI-Prompt-Patterns.md)
