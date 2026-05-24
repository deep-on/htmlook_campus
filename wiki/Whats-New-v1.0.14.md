# What's New — v1.0.14

Released: **2026-05-24** · Download: [htmlook.app](https://htmlook.app)

> Other languages: [한국어](Whats-New-v1.0.14-ko.md)

This is the user-facing summary. Use it to learn what's changed when
you next launch the app.

---

## At a glance

- **Multi-window tab mode** — every Pro window snaps to one rect with a Chrome-style tab strip on top. Drag tabs to reorder, color tabs per workspace, save named layouts.
- **AI consent that reads like English** — the permission modal now says *"AI wants to: modify foo.md · Reversible: ⌘Z undoes this"* instead of a JSON dump. Six category defaults (Read / Capture / Navigate / Annotate / Write / Run) let most safe reads pass without prompting.
- **Terminal that survives restart** — turn on tmux persistence and your terminal sessions reattach with their scrollback when you reopen the app. New: in-buffer search ⌘F, sync input across panes, detach a pane into its own window, keyboard selection mode ⌃⇧K.
- **Markdown WYSIWYG safety net** — live Markdown editing is now safe to use on real workspace documents. Round-trip stability is verified on a large library of real Korean / English documents.
- **Korean filename polish** — workspace claim, the Recent list, sidecar files, tab dedup, terminal cwd tracking, and IME composition all work the same on Korean-named folders as on any other.
- **Sidecars moved into `.htmlook/<category>/`** — PDF annotations, video bookmarks, video clips, audio segments, and chapters no longer clutter your workspace root.

---

## Multi-window tab mode

Settings → General → **Window tabs → Tab mode**.

When Tab mode is on, every open Pro window snaps to the focused
window's rectangle. From that point on, dragging, resizing, or adding
a window applies to peers too — they follow.

- **Tab strip lives above the toolbar.** Each tab is one workspace.
- **Drag a tab** to reorder. Chrome-style insertion gap.
- **Right-click** a tab for *Focus · Move-out · Close*. Hover for a preview card with the full workspace path.
- **Color tabs** (Settings → General) paints each tab with a workspace-derived hue.
- **Save current layout** (also in Settings → General → Window tabs) names and stores the current set of windows + rects. Restore from the same panel.
- **`⌘⌃1` … `⌘⌃9`** jumps to the Nth window. **`⌘⌃`` cycles forward.
- **Move-out** (right-click → ↗) shifts a window +60/+60 from its current rect so it visibly separates from the stack.

When you turn Tab mode off, windows cascade 60 px apart so they
visibly separate without any manual dragging.

→ Reference: [Tabs and Views](Tabs-and-Views.md)

---

## AI consent — a permission modal that reads like English

The AI permission modal used to dump raw JSON. Now:

```
● AI wants to: modify the active document
  Find-and-replace edit on the current file
  Scope        foo.md
  Category     write
  Reversible   Yes — ⌘Z undoes this
  ▸ Raw call — htmlook_apply_edit
  [Deny] [Allow once] [Always (workspace)] [Always (everywhere)]
```

Settings → AI → Permissions → **Tool permission defaults** lets you
choose, per category, whether the assistant prompts you or not:

| Category | Default | What it covers |
|---|---|---|
| **Read** | Auto | Looking at your file list, the outline, the active file's content |
| **Capture** | Auto | Taking a screenshot of the viewer, a region, an element |
| **Navigate** | Auto | Scrolling, jumping between tabs, jumping to a line |
| **Annotate** | Ask | Adding PDF highlights, PDF comments |
| **Write** | Ask | Editing the active file, replacing text, creating files |
| **Run** | Ask | Pasting into the terminal, starting voice recording |

Destructive actions (deleting a voice memo, closing a tab, clearing
PDF highlights) always ask, regardless of the category default.

→ Reference: [AI Apply Edit](AI-Apply-Edit.md) · [Settings](Settings.md)

---

## Terminal that survives restart

Settings → Terminal → **Persistence → tmux**.

In tmux mode your sessions outlive the app process. Close HTMLook,
reopen, and every pane reappears with its scrollback intact.

Other terminal improvements this release:

- **In-buffer search** — `⌘F` opens an in-pane search overlay with a hit counter. `↵` walks forward, `⇧↵` backward.
- **Sync input across panes** — pane header context menu → *Sync input with…* paints participating panes with a green band and broadcasts your typing to every one of them.
- **Drag-swap panes** — drag one pane's header onto another to swap positions.
- **Detach a pane into a new window** — `⌘D` (or context menu → *Move to new window*) lifts the focused pane into its own window. Its session moves with it.
- **Keyboard selection mode** — `⌃⇧K` enters arrow-key selection in the active pane. Shift+arrows extend, Home/End/PgUp/PgDn navigate, `⌘C` copies, `⎋` exits.
- **Closing the rightmost tab** moves focus left (matching macOS Terminal and iTerm) instead of jumping back to tab 0.
- **Korean cwd works everywhere** — a freeze that previously occurred when opening a Korean-named workspace is fixed.

→ Reference: [Terminal](Terminal.md)

---

## Markdown WYSIWYG safety net

Live Markdown editing in HTMLook now treats your file with care:

- Round-trip stability is verified against a large library of real
  Korean and English workspace documents. None of them drift on
  edit → save → re-open.
- When the editor detects a problem mid-edit (the kind of state
  that previously could have produced a one-line corrupted file),
  it stops the save and warns you instead of writing the bad state
  to disk.
- A timestamped backup of the previous on-disk version is written
  to `~/.htmlook-backup/` before each save, so a bad round-trip is
  recoverable.

Specific symptoms that v1.0.14 fixes:

- Numbers like `200~300%` no longer get misread as strikethrough
  during a round-trip.
- Task-list checkboxes survive even when the item's text wraps to
  a paragraph.
- Saving a file no longer causes the live view to reload its own
  write as raw markdown text.

→ Reference: [Markdown Editor](Markdown-Editor.md)

---

## Sidecars moved into `.htmlook/<category>/`

Files HTMLook creates next to your media used to sit alongside them:

- `*.annotations.json` — PDF annotations
- `*.bookmarks.json` — video bookmarks
- `*.clips.json` — video clips
- `*.segments.json` — audio segments
- `*.chapters.json` — audio / video chapters

All five now live under `<workspace>/.htmlook/<category>/`. Your
workspace root stays clean. Existing files are migrated the first
time HTMLook reads them, in the background — you don't need to do
anything.

---

## Korean filename polish

If you've worked with Korean (or other multi-codepoint) filenames
inside HTMLook before, you may have hit:

- A voice memo indicator that didn't appear next to Korean-named files.
- A workspace that landed twice in the Recent list under the same name.
- Two tabs for the same Korean-named file when opened from different sources.
- A freeze when opening a workspace whose path contained Korean.

All of these are fixed. Korean-named folders and files behave the
same as ASCII paths everywhere in the app.

---

## Smaller polish

- **`Saved ✓` flash** — settings that save immediately (toggles,
  dropdowns) now show a small `Saved ✓` pill in the dialog header
  for 1.5 s after each change. No more guessing whether it took.
- **AI settings sub-sections** — the AI tab now reads as four
  named groups: *Model Connection* · *Capabilities* · *Permissions*
  · *Usage*. Same fields, clearer hierarchy.
- **macOS chrome polish** — Settings opens from the app menu (`⌘,`)
  where macOS users expect it, the PRO badge moved inside the
  toolbar, a minimum window size keeps the layout from breaking
  on resize.
- **Sidebar polish** — the Name column gets +12 px so Korean
  filenames stop truncating mid-syllable. Drag-and-drop into a
  window only affects that window's sidebar.

---

## Where to go next

- [Tabs and Views](Tabs-and-Views.md) — multi-window tab mode in full
- [Terminal](Terminal.md) — tmux persistence and the new pane tools
- [AI Apply Edit](AI-Apply-Edit.md) — the new consent modal in detail
- [Settings](Settings.md) — every new toggle, where to find it
