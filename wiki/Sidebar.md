# Sidebar

> Workspace-aware file tree with multi-select, drag-out, and tight Finder integration.

## Anatomy

```
┌──────────────────────┐
│ ▾ ~/Notes      ⊕ ⊟  │ ← workspace dropdown + new file + collapse all
├──────────────────────┤
│  Filter…       ⨯    │ ← live filter (path + filename, case-insensitive)
├──────────────────────┤
│  ▾ docs/             │
│    • intro.md        │
│    • plan.md   ●     │ ← ● = modified in editor
│  ▾ images/           │
│    • hero.png        │
│    • thumb.jpg       │
│  ▸ archive/          │ ← collapsed dir
│  • notes.html        │
├──────────────────────┤
│  12 files · 2 dirs   │ ← footer
└──────────────────────┘
```

## Workspace dropdown

The top button shows the current workspace name. Click → drop-down of recent workspaces + *Open folder…* (⌘⇧O) + *New workspace from folder…*. Each entry shows the absolute path on hover.

Pin a workspace with the ★ icon — pinned ones stay at the top.

## File ops

| Op | Shortcut / gesture |
|---|---|
| Open file | Click |
| Open in new tab | Double-click, or ⌘+click |
| Rename | Long-press the row (300 ms), or context menu → Rename |
| Duplicate | Context menu → Duplicate (adds ` copy` suffix) |
| Move to Trash | ⌫ (deletes the selection — confirms if 2+) |
| Reveal in Finder | Context menu, or *File → Reveal* |
| Open in terminal | Context menu — chdir to parent in next free terminal tab |
| New file in folder | Right-click folder → *New file* |
| New folder | Right-click folder → *New folder* |

## Multi-select

- ⌘+click toggles individual rows
- ⇧+click ranges from the focus row to the click target
- ⌘A selects every visible row (after filter)
- Cancel with ⎋ or by clicking blank space

Actions like Delete and Move-to-Trash apply to the entire selection. The context-menu *Delete* shows the count: `Delete (3)`. The confirm dialog lists up to 5 names + `… and N more`.

## Drag-out

Drag any file from the sidebar onto Finder, Mail, Slack, Notion, etc. The drop carries the actual file path. Drag an `.html` onto a webmail compose window to attach it. Drag a folder out to *copy* it.

## Filter

The filter box accepts plain text + a small grammar:

- `regression` → matches anywhere in path or filename
- `ext:pdf` → only `.pdf` files
- `dir:images` → only inside an `images/` directory
- `mod:>7d` → modified more than 7 days ago (negation: `mod:<24h`)

The query persists per workspace.

## Sort & group

Footer context-menu sets the active sort:

- Name (A→Z / Z→A)
- Modified date (newest / oldest)
- Size
- Type (folder-first, then by extension)

The choice is per-workspace and remembered.

## Extensions panel

The collapsible **Extensions** section at the bottom shows what HTMLook can do beyond opening files (Mermaid, D2, LibreOffice render, etc.). A coloured dot indicates each item is ready (solid) or needs its external tool installed (dim ring — click to install). See [Extensions](Skills.md) for the full list.

## Next

- [Viewer →](Viewer.md)
- [Tabs & Views →](Tabs-and-Views.md)
