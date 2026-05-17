# UI Overview

> One diagram, every pane named. Bookmark this page.

```
┌──────────────────────────────────────────────────────────────────────┐
│  ⎙  ▼ workspace          file.md            ●  HTMLook Pro    🪟 ⊟ ⨯ │ ← Title bar
├──┬──────────────┬────────────────────────────────┬──────────────────┤
│A │  Sidebar     │  Tabs strip · ⌘1..9             │  ChatPanel       │
│c │              │ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ │   (⌘L toggle)   │
│t │   filter…    │                                 │                  │
│i │   ▾ docs/    │      Viewer                     │   System prompt  │
│v │     • intro.md│                                │   • Skill chips  │
│i │     • plan.md│      (Markdown / HTML / PDF /   │                  │
│t │   ▾ images/  │       image / video / audio /   │   ▸ "summarize…" │
│y │     • hero.png│      DOCX / PPTX / code)       │   ▸ tool call    │
│B │              │                                 │   ▸ response …   │
│a │              │                                 │                  │
│r │              │                                 │                  │
├──┴──────────────┴────────────────────────────────┴──────────────────┤
│  Terminal panel  (Cmd+`)  ⠿ + Claude + Codex + Gemini + Shell   ⊟  │ ← dockable
│  ─ tab 1 ─ tab 2 ─ tab 3 ─                                          │
│  $                                                                  │
├──────────────────────────────────────────────────────────────────────┤
│  ▣ 12 files · 1 modified ●   ⏺ rec 00:12   ▾ Easier mode      🟢 OK│ ← Status bar
└──────────────────────────────────────────────────────────────────────┘
```

## The six surfaces

### 1. Activity Bar (far left, 32 px)
Quick toggles: file list visibility, viewer/dual/code view modes, paint mode, present mode, terminal dock-position cycler. Hover gives a tooltip with the keyboard shortcut.

### 2. Sidebar
File tree of the current workspace + filter input + drag-out (`.html` → Finder), multi-select (⌘+click / ⇧+click), context-menu (rename, duplicate, reveal in Finder, open in terminal, delete N). Top dropdown switches between recently-opened workspaces.

→ Full page: [Sidebar](Sidebar.md)

### 3. Tabs strip
Open files become tabs. ⌘1..9 jump. Cmd+W closes. Modified dot (●) appears when unsaved. Right-click tab for *Pin*, *Close others*, *Reveal*, *Copy path*. Tab title shows the brand letter mark (Cl/Cx/Gm/Sh) for terminal tabs.

### 4. Viewer (centre, the biggest area)
Renders the active tab. The renderer switches automatically:

- `.md` → WYSIWYG Markdown editor with autocorrect, ⌘K link dialog, ⌘B/I/U inline formatting, code-block language picker, image popover (alt + align)
- `.html` → iframe sandbox with relative-asset inlining
- `.pdf` → PDF.js with text-layer + highlight tool
- video / audio → custom player with bookmarks + transcript
- everything else → either pretty render or syntax-highlighted code

Dual-view (⌘⇧D) splits left/right for side-by-side. Present mode (⌘⌥P) hides chrome.

→ Full page: [Viewer](Viewer.md)

### 5. Terminal panel
Dockable bottom / right / left / centre. Each tab is a real PTY (zsh by default) with optional preset (Claude / Codex / Gemini / Shell). Drives Korean IME correctly (KoreanComposer state machine). Cmd+\` toggles visibility. Cmd+T new tab. Cmd+D / Cmd+⇧D split panes.

→ Full page: [Terminal](Terminal.md)

### 6. ChatPanel
Bring-Your-Own-Model AI chat. ⌘L toggles. Tools auto-loaded from MCP + skill manifest. 4-button consent modal for the first tool call per workspace.

→ Full page: [ChatPanel · BYOM](ChatPanel-BYOM.md)

## Layered surfaces

- **Find bar**: ⌘F inside the viewer. ⌘G next match.
- **Paint canvas**: ⌘⇧P toggle. Pen / shapes / arrow / text, undo 50 steps, PNG export.
- **Voice player**: appears at bottom when a `.m4a` is selected. Multi-memo navigation, transcript view, waveform.
- **Region selector**: Cmd+⌥+R captures a screen rectangle to clipboard / Paint / AI.
- **Update notifier**: top-right corner when a newer build is on the manifest.

## View modes

| Mode | Shortcut | What it does |
|---|---|---|
| Single | ⌘1 | Default — one viewer pane |
| Dual | ⌘⇧D | Left/right side-by-side; sync-scroll toggle |
| Code | (Easier) ⌘⌥E (Pro) ⌘E | Raw source visible alongside render |
| Paint | ⌘⇧P | Sketch on top of viewer |
| Present | ⌘⌥P | Hide chrome, fullscreen viewer |

## What you tweak in [Settings](Settings.md)

Theme · font · terminal preset commands · BYOM provider/key · auto-save delay · update channel · sidebar collapse defaults · per-language code preferences · viewer toolbar visibility.

## Next

- [Tabs & Views →](Tabs-and-Views.md)
- [Sidebar →](Sidebar.md)
