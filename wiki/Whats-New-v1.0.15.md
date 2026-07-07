# What's New — v1.0.15

Released: **2026-05-25** · Download: [htmlook.app](https://htmlook.app)

> Other languages: [한국어](Whats-New-v1.0.15-ko.md)

v1.0.15 is a **hotfix**. The full feature set is the v1.0.14 one —
see [What's new in v1.0.14](Whats-New-v1.0.14.md) for the four
headline features (multi-window tab mode, AI consent UX, terminal
tmux persistence, markdown WYSIWYG safety net).

This page only covers what changed in the 24 hours between
v1.0.14 and v1.0.15.

---

## What changed

- **Terminal performance fix for Korean-named workspaces.** v1.0.14
  fixed a freeze that happened when opening a Korean-named workspace.
  Within the first day of dogfooding, that fix turned out to allow
  a different problem in the same area: with several terminal panes
  open, background polling could pile up and make the app feel
  sluggish. v1.0.15 keeps the freeze fix and removes the slowdown.

No new features. No UI changes. No keystrokes were touched.

---

## Upgrading

- v1.0.14 → v1.0.15: the auto-updater picks it up on the next
  launch of HTMLook Pro.
- v1.0.13 → v1.0.15: read the [v1.0.14 page](Whats-New-v1.0.14.md)
  first to see what the major changes are, then come back here for
  the hotfix note.
- Fresh install: download from [htmlook.app](https://htmlook.app).

---

## Where to go next

- [What's new in v1.0.14](Whats-New-v1.0.14.md) — the four headline features
- [Terminal](Terminal.md) — tmux persistence and the pane tools
- [Tabs and Views](Tabs-and-Views.md) — multi-window tab mode
