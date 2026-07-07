# What's New — v1.0.16

Released: **2026-05-26** · Download: [htmlook.app](https://htmlook.app)

> Other languages: [한국어](Whats-New-v1.0.16-ko.md)

v1.0.16 cleans up the window-close path end-to-end, smooths the
tmux terminal's drag-scroll across the panel edge, and stabilizes
the PPTX conversion chain. Plus a round of day-to-day paper-cut
fixes that showed up during dogfooding.

---

## Highlights

### 1. Window close, one clean motion

Every way to close — the red ❌ traffic-light, a per-tab ×, a
single-window app, or the last window in multi-window mode — now
goes through the same **Quit HTMLook Pro?** confirmation. While
the close runs, a small in-window progress indicator stays up so
you can see the close is on its way through, not stuck.

- **Unsaved-changes guard on every path.** If any tab in the
  window you're closing has unsaved changes, you're asked to
  confirm before the Quit dialog appears. Cancel returns you to
  the app with everything intact.
- **Per-tab × is per-tab.** When you have two or more tabs, the
  × on a tab closes only that tab (with the same unsaved-changes
  prompt). When you have a single tab, the × matches the
  traffic-light ❌ — it's the same as closing the app.
- **Tab strips stay in sync.** When you close a window in
  multi-window mode, the tab slot for that window in every other
  window's strip fades out in step with the window disappearing.
  No more lingering ghost tabs.
- **Re-opening the same workspace mid-close is safe.** If you
  click to re-open a workspace that's still cleaning up from a
  close, HTMLook Pro waits for the cleanup to finish and then
  opens it cleanly.

### 2. tmux terminal — drag-select past the panel edge

If you drag a selection in the tmux terminal and your cursor
crosses the bottom of the panel, the view now keeps scrolling so
the selection extends with it. Works in **vim**, **less**,
**htop**, and other alternate-buffer apps too — not just shell
output.

Wheel and drag no longer fight each other: if you wheel-scrolled
in the last five seconds, the next drag picks up from where the
view is, not where copy-mode last anchored.

### 3. Stale tmux session cleanup

Three ways to keep `tmux ls` honest after a session restart or
crash:

- **Kill button in the terminal popover** — manual sweep of the
  one you point at.
- **Settings → Terminal → Auto-sweep orphans** (default OFF) —
  prunes sessions that have been idle past a threshold whenever
  HTMLook Pro starts.
- **`htmlook --tmux-cleanup`** CLI subcommand — runs the same
  sweep from outside the app, useful in scripts.

### 4. PPTX conversion, with a Cancel button

The conversion chain is now **PowerPoint → LibreOffice**.
Keynote was dropped because of repeated Korean-font drift and
AutoRecover dialogs surfacing during conversion. PowerPoint
launches **silently in the background** so it doesn't take focus
from your work.

If a conversion runs past **30 seconds**, the loading card grows
a **Cancel** button so you can always bail out instead of being
stuck watching a spinner.

### 5. Daily polish

- **Sidebar Name column has an explicit width.** Drag the
  resize handle on the column header, or set
  *Settings → Sidebar → Name column width*. **Long-press** the
  Name-sort button to auto-fit the column to the current sidebar
  width.
- **Custom hint tooltips** for the small Sort / Zoom buttons sit
  **above the button** (not cropped at the bottom edge) with a
  minimal pill style.
- **New tabs and new windows no longer flash white** on open
  (dark and light themes both honored from the very first
  paint).
- **autoSave: off actually means off.** When you set autoSave to
  OFF, no saves happen — previously the timer kept running at
  1.5 s regardless.
- **Pasted-tab toggle.** Pasting outside a text field opens a
  new tab by default (Pasted). Turn it off in
  *Settings → Editor* if you'd rather paste only land on the
  clipboard.
- **Tab order stays stable.** New tabs always appear at the
  right; opening a workspace (including Hangul-named ones)
  never reshuffles existing tabs.
- **Terminal forward-delete** — `⌘⌫` (line-start) and `⌥⌫`
  (prior word) are forwarded to your shell.
- **Drag-select to clipboard.** A drag-selection in the
  terminal lands on the system clipboard automatically.
- **Faster workspace re-attach.** Workspaces with many terminal
  panes re-open with the active tab first; the rest hydrate as
  they come into view.

### 6. Workspace hygiene

- **Stale Office / Pages / LibreOffice lock files** (`~$file.docx`
  and friends) are quarantined into `.htmlook/lock-quarantine/`
  when you open a workspace (toggle in Settings).
- **`htmlook_apply_edit` backup files** now live in
  `.htmlook/file-backup/` so they don't clutter the sidebar.
- **Hangul folder and file names** match consistently between
  the sidebar, search, and tab order.

---

## Upgrading

- v1.0.15 → v1.0.16: the auto-updater picks it up on the next
  launch of HTMLook Pro.
- v1.0.14 → v1.0.16: same — the updater handles it. If you
  haven't read about v1.0.14, the [v1.0.14
  page](Whats-New-v1.0.14.md) covers the multi-window tab mode
  and the AI consent rewrite.
- Fresh install: download from [htmlook.app](https://htmlook.app).

---

## Learn more

- [v1.0.15 — hotfix](Whats-New-v1.0.15.md)
- [v1.0.14 — major release](Whats-New-v1.0.14.md)
- [Tabs and Views](Tabs-and-Views.md) — multi-window tab mode
- [Terminal](Terminal.md) — tmux backend, drag-select
- [Settings](Settings.md) — Name column, Auto-sweep, autoSave
