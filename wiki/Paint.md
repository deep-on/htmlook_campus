# Paint

> A transparent sketch canvas on top of the viewer. ⌘⌥P toggles. Circle, point, send.

## Why it's there

Half of "explaining what you mean" is gesture — *this column*, *this trend*, *this misalignment*. Paint gives you a layer to mark on, save the result, and drop it straight into the AI Assistant as an image attachment.

## Toggle and basics

| Action | Shortcut |
|---|---|
| Toggle Paint mode | ⌘⌥P |
| Undo / Redo | ⌘Z / ⌘⇧Z (50-step history per tab) |
| Clear canvas | Trash icon in Paint toolbar |
| Export as PNG | Download icon |

The canvas is per-tab. Sketches auto-save 5 s after the last stroke so you don't lose work across reloads. They land in `<workspace>/.htmlook/sketches/`.

## Tools

| Tool | Notes |
|---|---|
| **Pen** | Free-hand stroke. Pressure curve set for Apple Pencil + trackpad. |
| **Eraser (S / M / L)** | 8 / 16 / 32 px diameter. Acts on strokes only — doesn't touch the underlying viewer. |
| **Rectangle** | Drag to draw. *Fill* toggle in the toolbar. |
| **Ellipse** | Same as rectangle but elliptical. |
| **Line** | Straight line. Shift snaps to 15° increments. |
| **Arrow** | Direction toggle: → / ← / ↔. |
| **Text** | Click to place. Sizes **S / L**. ⏎ commits. |

## Colour and stroke

Colour swatch in the toolbar. Stroke width: thin / medium / thick / heavy. Both persist per workspace.

## Export resolution

PNG export caps at 1280 × 720 to keep file sizes sane. The canvas is retina-aware so captures still look sharp. Output is alpha-free RGB so pasting into other tools doesn't surprise anyone with transparency.

## Attaching to the AI Assistant

With Paint open, the AI Assistant's 📎 button picks up the current canvas — no extra Save step. The image lands in your next message.

You can also drag a saved PNG out of `.htmlook/sketches/` (in the sidebar) straight onto the input box.

## Next

- [Voice memos →](Voice-Memos.md)
- [Export →](Export.md)
