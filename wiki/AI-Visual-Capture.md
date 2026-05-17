# Visual Capture

> Read what the user actually sees. Most powerful when chained with `apply_edit` + `capture_diff`.

## The capture surface (six tools)

| Tool | Use when |
|---|---|
| `capture_viewport` | You need the whole active pane |
| `capture_selector` | You can name a CSS selector (`#hero`, `.card:nth-child(2)`) |
| `capture_active_element` | The user just clicked an element; capture that |
| `capture_text_match` | You can quote a string the user can read on screen |
| `capture_rect` | You know coordinates (often after `region_current_png`) |
| `capture_diff` | Compare two PNGs you just captured |

All capture tools return:

```jsonc
{
  "base64": "iVBORw0KGgo…",      // image/png, NOT a data URL
  "mime": "image/png",
  "width": 1280,
  "height": 720,
  "captured_at": "2026-05-17T03:14:00Z",
  "scope": {                     // what got captured
    "kind": "selector",          // viewport | selector | active_element | text_match | rect
    "selector": ".hero",         // tool-specific
    "bbox": { "x": 0, "y": 0, "w": 1280, "h": 320 }
  }
}
```

Decode `base64` with your client's image-handling primitive — most MCP clients accept it as a vision content block directly.

## The "before / after" pattern

```text
1. capture_selector(".cta") → before.png
2. plan the edit (text colour change)
3. apply_edit("Sign up free", "Start free trial")
4. (wait ~150 ms for re-render)
5. capture_selector(".cta") → after.png
6. capture_diff(before, after, threshold=0.05) → bbox + did_change
```

The diff is computed in pure Rust on the `png` crate. The result includes a tight bounding box of changed pixels, useful for sanity check ("did my edit only touch the CTA, or did it cascade?").

## visual_overlap_check

Returns elements that:

- have **truncated** text (`text-overflow: ellipsis` active)
- **overflow** their container
- have **zero size** (likely a layout bug)
- **clip** content

```jsonc
{
  "issues": [
    { "selector": ".hero h1", "kind": "text-truncated", "rect": {…} },
    { "selector": "#cta-row",  "kind": "overflow-x",   "rect": {…} }
  ]
}
```

Useful for a pre-flight check before changing copy length.

## layout_map

Returns a structural survey:

```jsonc
{
  "landmarks":   [{ "role": "banner", "selector": "header" }, …],
  "headings":    [{ "level": 1, "text": "Hello", "selector": "h1" }, …],
  "buttons":     [{ "text": "Sign up", "selector": "#cta-row > button:nth-child(1)" }, …],
  "links":       [{ "text": "Pricing", "href": "/pricing", "selector": "nav a:nth-child(2)" }, …],
  "images":      [{ "alt": "hero", "src": "hero.png", "selector": "img.hero" }, …],
  "tables":      [{ "rows": 12, "cols": 4, "selector": "#data" }, …],
  "forms":       [{ "fields": 5, "selector": "form#contact" }, …]
}
```

Run it once at the start of a session to "see the page".

## select_element + capture_active_element

The fastest way to talk about a specific node:

```
htmlook_select_element({ selector: ".cta button" })
htmlook_capture_active_element({ padding: 8 })
```

Padding adds margin around the bounding box so the screenshot includes context.

## Rate limit

Capture tools share an 8-burst / 8-per-second token-bucket. A typical "before / 5 candidates / after" loop = 7 captures, well below the limit. If you bust the limit you get a friendly error — back off ~125 ms and continue.

## When *not* to capture

- **Don't capture to "understand layout"** if `layout_map` answers the question. Cheaper, smaller, deterministic.
- **Don't capture twice in a row** without an intervening change — your second call gives the same PNG you already have.
- **Don't capture the viewport** when you can name an element. Tight crops are 5–10× smaller and the diff is more useful.

## Next

- [Apply-edit round-trip →](AI-Apply-Edit.md)
- [Prompt patterns →](AI-Prompt-Patterns.md)
