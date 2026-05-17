# Tabs & Views

> Tabs keep multiple files open. Views are how you arrange what one tab shows.

![Tab strip and view-mode toggles](images/03-tabs.png)

## Opening a file as a tab

| Way | Trigger |
|---|---|
| Sidebar single-click | Replaces the current tab |
| Sidebar double-click | Opens in a new tab |
| ⌘+click sidebar | Open in background tab |
| Drag file from Finder onto window | New tab |
| `htmlook://` link in viewer | Reuses or opens new tab |
| ⌘O / ⌘⇧O | OS open dialog (folder / file) |

## Tab strip behaviour

- ⌘⌥1..9 jumps to tab 1..9
- ⌘W closes the active tab (asks if modified)
- ⌘⇧T reopens last closed tab
- ⌘⌥→ next tab, ⌘⌥← previous
- Middle-click closes
- Drag horizontally to reorder
- Drag a tab off the strip → tear-out into a new window
- ● indicates unsaved changes
- Letter-mark glyph (Cl/Cx/Gm/Sh) appears for terminal tabs and gently animates while output is streaming

### Tab context menu (right-click)

- *Pin / Unpin* — pinned tabs survive "close all"
- *Close others*, *Close to the right*, *Close all*
- *Reveal in Finder*
- *Copy path*, *Copy relative path*
- *Open in terminal* (chdir to file's directory in the next free terminal tab)

## View modes (per active tab)

### Preview · ⌘1
Renders the file. Default for everything readable (Markdown rendered, PDF as PDF, video plays, etc.).

### Source · ⌘2
Raw source — Markdown text, HTML markup, JSON text, etc. Editing here writes back to the file.

### Split · ⌘3
Preview on the left, source on the right. Toggle **Sync scroll** in the toolbar to lock vertical positions.

### Gallery · ⌘G
Thumbnail grid of the workspace's files. Click a thumbnail to open.

### Paint (Pro) · ⌘⌥P
Transparent sketch canvas over the viewer. See [Paint](Paint.md).

### Present
Hides chrome (sidebar, tabs, status bar). *View → Present mode*. ⎋ to leave.

## Save model

Markdown and HTML tabs auto-save 1.5 s after the last keystroke. The status bar shows `●` while pending, `✓` after the write commits. ⌘S writes immediately.

Untitled tabs (drafts) don't auto-save — they ask for a destination on ⌘S.

## Reopening last session

HTMLook can restore the last set of tabs per workspace on launch. Settings → General → *On launch* → *Restore last session* (default) or *Start empty*.

## Next

- [Sidebar →](Sidebar.md)
- [Viewer →](Viewer.md)
