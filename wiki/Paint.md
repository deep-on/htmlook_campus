# Paint

> A transparent sketch canvas on top of the viewer. ⌘⇧P toggles. Designed to circle, point, and send.

## Why it's there

Half of "explaining what you mean" is gesture — *this column*, *this trend*, *this misalignment*. Paint gives you a layer to mark on, save the result, and attach the result straight into ChatPanel as an image attachment.

## Toggle and basics

| Action | Shortcut |
|---|---|
| Toggle Paint mode | ⌘⇧P |
| Send canvas as attachment to ChatPanel | (Paint open) → 📎 in ChatPanel |
| Undo / Redo | ⌘Z / ⌘⇧Z (50-step history per tab) |
| Clear canvas | Trash icon in Paint toolbar |
| Export as PNG | Download icon (`.htmlook/sketches/...png`) |

The canvas is per-tab. Sketches auto-save 5 s after the last stroke to `.htmlook/sketches/<basename>.<timestamp>.png` so you don't lose work across reloads.

## Tools

| Tool | Notes |
|---|---|
| **Pen** | Free-hand stroke. Pressure curve set for Apple Pencil + trackpad. |
| **Eraser (S/M/L)** | 8 / 16 / 32 px diameter. Acts on strokes only — doesn't touch the underlying viewer. |
| **Rectangle** | Drag to draw. *Fill* toggle in the toolbar. |
| **Ellipse** | Same as rectangle but elliptical. |
| **Line** | Straight line, Shift snaps to 15° increments. |
| **Arrow** | Direction toggle: → / ← / ↔. |
| **Text** | Click to place. Sizes **S / L**. ⏎ commits. |

## Colour and stroke

Colour swatch in the toolbar. Stroke width: thin / medium / thick / heavy. Both persist per workspace.

## Export resolution

PNG export caps at 1280×720 to keep file sizes sane. The canvas is DPR-aware so retina captures still look sharp. Output is alpha-free RGB (so paste into web tools doesn't surprise users with transparency).

## Attaching to ChatPanel

With Paint open, the ChatPanel 📎 button picks up the current canvas without an extra Save step. The image lands in the next user message as a vision content block.

You can also drag the PNG from `.htmlook/sketches/` straight onto the ChatPanel input.

## Sketches as a workspace artifact

Files in `.htmlook/sketches/` are plain PNGs — `git`-friendly, copyable, attachable. There's no proprietary container.

## MCP-exposed tools (for AI agents)

- `htmlook_sketch_current_png` — capture the active sketch as base64
- `htmlook_sketch_clear` — wipe the canvas
- `htmlook_sketch_save` — force a save
- `htmlook_sketch_add_shape` — programmatic shape draw
- `htmlook_sketch_set_color`, `htmlook_sketch_set_stroke`, `htmlook_sketch_undo`, `htmlook_sketch_redo`

Combine with capture tools to do "highlight this region of the viewer, save, attach". See [AI Visual Capture](AI-Visual-Capture.md).

## Next

- [Voice memos →](Voice-Memos.md)
- [Skills →](Skills.md)
