# Tabs & Views

> Tabs are how you keep multiple files open. Views are how you arrange what one tab shows.

## Opening a file as a tab

| Way | Trigger |
|---|---|
| Sidebar single-click | Replaces the current tab |
| Sidebar double-click | Opens in a new tab |
| ⌘+click sidebar | Open in background tab |
| Drag file from Finder onto window | New tab |
| `htmlook://` link in viewer | Reuses or opens new tab |
| MCP `htmlook_open_file` | Programmatic open |
| ⌘O | OS open dialog |

## Tab strip behaviour

- ⌘1..9 jumps to tab 1..9
- ⌘W closes the active tab (asks if modified)
- ⌘⇧T reopens last closed tab
- ⌘\` cycles forward, ⌘⇧\` cycles back
- Middle-click closes
- Drag horizontally to reorder
- Drag a tab off the strip → tear-out into a new window
- ● indicates unsaved changes; turns into × on hover for one-click close
- Letter-mark glyph (Cl/Cx/Gm/Sh) appears for terminal tabs and streams animate while output is arriving

### Tab context menu (right-click)

- *Pin / Unpin* — pinned tabs survive ⌘W-all
- *Close others*, *Close to the right*, *Close all*
- *Reveal in Finder*
- *Copy path*, *Copy relative path*
- *Open in terminal* (chdir to file's directory in the next free terminal tab)

## View modes (per active tab)

### Single (default · ⌘1 if remapped)
One viewer pane fills the centre.

### Dual (⌘⇧D)
Splits the centre into left/right. Each side can show a different file or the same file in a different mode (e.g. `.md` render on the left, raw source on the right). Toggle **Sync scroll** in the dual-view toolbar to lock vertical positions.

### Code (⌘E in Pro, ⌘⌥E in Easier)
Shows the file's raw source next to its rendered view. Works for `.md`, `.html`, `.json`, `.csv`, `.svg`. Editing the source updates the render live.

### Paint (⌘⇧P, Pro only)
Overlays a transparent sketch canvas on the viewer. Anything you draw is saved per-tab to `.htmlook/sketches/<basename>.<timestamp>.png`. See [Paint](Paint.md).

### Present (⌘⌥P)
Hides chrome (sidebar, tabs, status bar). Useful when projecting or recording. Press ⎋ to leave.

## Save model

Markdown and HTML tabs auto-save 1.5 s after the last keystroke. The status bar shows `●` while pending, `✓` after the write commits. ⌘S writes immediately.

Untitled tabs (drafts) don't auto-save — they ask for a destination on ⌘S.

## Reopening tab state

HTMLook restores tabs from the last session per workspace. The list lives in `.htmlook/session.json`. Clearing it is safe; you just lose the "what was open last time" memory for that workspace.

## Next

- [Sidebar →](Sidebar.md)
- [Viewer →](Viewer.md)
