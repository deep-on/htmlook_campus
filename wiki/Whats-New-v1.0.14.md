# What's New — v1.0.14

Released: **2026-05-24** · Download: [htmlook.app](https://htmlook.app)

Released-notes companion to the four-card highlight at
[htmlook.app/#whats-new](https://htmlook.app/#whats-new). The full
ChangeLog lives in the desktop repo as `CHANGELOG_v1.0.14.md`; this
page is the campus-facing reading order.

> Other languages: [한국어](Whats-New-v1.0.14-ko.md)

---

## At a glance

- **Multi-window tab mode** — every window snaps to one rect; Chrome-style tab strip with drag-reorder, color-coded workspaces, named layout save/restore.
- **AI consent that reads like English** — `"AI wants to: modify foo.md · Reversible: ⌘Z"` replaces the raw JSON dump. Six category defaults (Read / Capture / Annotate / Navigate / Write / Run) skip ~70% of modals automatically.
- **Terminal that survives restart** — tmux-backed sessions reattach with scrollback intact. In-buffer search `⌘F`, sync input across split panes, detach a pane into its own window, keyboard selection mode `⌃⇧K`.
- **Markdown WYSIWYG safety net** — edit-collapse guard, NFC/NFD path-form sweep, 196-document round-trip corpus locked to **zero drift**, gated by 1014 tests on every build.
- **Korean / Hangul polish** — workspace claim, recent list, sidecars, tab dedup, terminal `cwd` polling, and IME duplicate-write all repaired; Hangul-named folders work like any other path.
- **Sidecars moved into `.htmlook/<category>/`** — `*.annotations.json`, `*.bookmarks.json`, `*.clips.json`, `*.segments.json`, `*.chapters.json` no longer clutter your workspace root.
- **MCP bridge multi-instance fix** — dev + production no longer race on `~/.htmlook/mcp-bridge.port`; per-PID port file with ping-validated discovery.

---

## Multi-window tab mode

The previous v1.0.13 multi-window model treated every Pro window as
fully independent. v1.0.14 keeps that foundation but layers a "single
logical window" mode on top:

- `Settings → General → Window tabs → Tab mode: On`. Every open window
  snaps to the focused window's rect; drag / resize / +Add propagates
  so peers follow.
- Tab strip lives above the toolbar. Each tab = one workspace.
  Right-click for Focus / Move-out / Close. Hover for a preview card
  with the full workspace path.
- Color-coding paints each tab with a workspace-derived hue.
- Named layout save / restore at `~/.htmlook/window-layouts.json`.
  Restore honours Layout mode (Exact / Cascade 30 px).
- `⌘⌃1-9` jumps to the Nth window; `⌘⌃`` cycles forward.

→ Reference: [Tabs and Views](Tabs-and-Views.md)

---

## AI consent UX rewrite

The consent modal in ChatPanel used to dump raw JSON:

```
🔧 Allow LLM to run htmlook_apply_edit?
arguments
{"path": "/Users/.../foo.md", "find": "abc", "replace": "xyz"}
```

Now it reads:

```
● AI wants to: modify the active document
  Find-and-replace edit on the current file
  Scope        foo.md
  Category     write
  Reversible   Yes — ⌘Z undoes this
  ▸ Raw call — htmlook_apply_edit
```

- Tool descriptor map covers ~70 HTMLook MCP tools.
- New **Settings → AI → Permissions → Tool permission defaults**: each of
  six categories gets Auto / Ask / Block. Destructive tools (delete
  voice memo, close tab, clear annotations) always ask, regardless of
  default.
- Default policy: Read / Capture / Navigate → Auto, Annotate / Write /
  Run → Ask. Eliminates ~70% of modals in a normal session.

→ Reference: [AI Apply Edit](AI-Apply-Edit.md)

---

## Terminal — tmux backend + persistence

Terminals are now backed by tmux instead of raw PTY ownership. Closing
and reopening the app drops you back exactly where you left off.

- **Per-pane stable tmux naming** — `htmlook-<sha8>-tab<N>-pane<M>`,
  SHA8 of the NFC-normalised workspace path. Deterministic across
  restarts.
- **Preset auto-resume** — Claude / Codex / Gemini sessions detect the
  resume flag and skip the paste step on reattach.
- **In-buffer search** — `⌘F` opens the SearchAddon overlay with hit
  counter, `↵` / `⇧↵` to walk hits.
- **Sync input** — broadcast typing across a pane group (green band on
  participants).
- **Drag-swap panes** — drag a pane header onto another to swap.
- **Detach pane** — `⌘D` (or context menu) lifts the focused pane into
  its own new window; tmux session moves with it.
- **Keyboard selection mode** — `⌃⇧K` for arrow-key block selection,
  Shift+arrow extend, Home/End/PgUp/PgDn, `⌘C` copy. (Was `⌃⇧Space`
  before macOS Input Sources kept intercepting it.)
- **Tab close → left neighbour** — closing the rightmost tab moves
  focus left, not back to tab 0. Matches macOS Terminal / iTerm.
- **Hangul cwd freeze fix** — fork+exec for `lsof` no longer wedges
  the Tauri sync worker on Korean cwds.

→ Reference: [Terminal](Terminal.md)

---

## Markdown WYSIWYG safety net

A user-reported corruption thread led to a vertical fix slice:

- **Selective tilde escape** — Turndown no longer mis-reads `200~300%`
  as strikethrough.
- **Task list loose-paragraph preservation** — checkboxes survive when
  list items wrap in `<p>`.
- **Frontmatter / KaTeX / GFM-strikethrough rules** — three Turndown
  rules so YAML frontmatter, display + inline math, and `~~strike~~`
  survive a render → edit → save cycle.
- **File-watcher own-write echo dedup with NFC/NFD dual-key** — after
  saving, the macOS watcher used to fire the file back and the app
  reloaded its own write as raw markdown. Fixed.
- **Disk md backup before every write** — a timestamped copy goes to
  `~/.htmlook-backup/<basename>.<ts>.md` so a bad round-trip is
  recoverable.
- **Block-collapse guard** — a MutationObserver refuses to commit a
  write that drops the rendered block count to zero (the WKWebView
  contenteditable failure mode).
- **196-document round-trip corpus** — runs on every CI build with a
  9-bucket drift classifier. Current genuine drift: **0**.

→ Reference: [Markdown Editor](Markdown-Editor.md)

---

## Sidecars now live under `.htmlook/<category>/`

Five categories of co-located JSON sidecars used to clutter workspace
folders so badly that `ls` and Finder views were noisy:

- `*.annotations.json` — PDF annotations
- `*.bookmarks.json` — video bookmarks
- `*.clips.json` — video clips
- `*.segments.json` — audio segments
- `*.chapters.json` — audio / video chapters

All five now live under `<workspace>/.htmlook/<category>/<source>.json`
— invisible to the sidebar's hidden-folder filter and out of every
file picker.

- Read-time auto-migration: every read tries the new path first,
  rename-migrates legacy on miss.
- Eager scan on workspace claim moves all matching files in the
  background.
- Pretty-printed JSON now; empty bodies delete the file instead of
  being written back.

---

## Korean / Hangul polish

A long-tail dogfooding effort on a Hangul-named workspace surfaced
five separate NFD-vs-NFC alignment gaps. All five repaired:

1. **Voice memo indicator** — `voice_list_for_dir` returned NFD keys
   while JS `activeFileStem()` produced NFC; voice player + sidebar
   indicator both rendered empty for Hangul filenames.
2. **Workspace claim** — same Hangul workspace claimable twice under
   NFC + NFD forms by different windows.
3. **Recent workspaces** — same workspace as two entries.
4. **Sidecar paths** — `.htmlook/<category>/<name>.json` written
   under inconsistent forms.
5. **Tab dedup** — opening the same Hangul file from two sources
   created two tabs.

Plus the v1.0.14 ship-blocker: a Hangul cwd would cause
`proc_pidinfo` to return empty, falling back to `lsof` shell-out —
which was holding a Mutex through a 200–800 ms fork+exec and
beachballing every Tauri sync command behind it. Fixed by moving the
lsof off the sync worker (spawn_blocking) and dropping the lock
before the fork.

---

## MCP bridge multi-instance fix

When two Pro instances ran concurrently (dev + prod), the second to
start overwrote `~/.htmlook/mcp-bridge.port` with its own port. When
that instance closed, the file stayed pointing at a dead port, and
any `htmlook --mcp-server` subprocess spawned by Claude Code / Codex
CLI / Cursor connected to nothing.

Now: each instance also writes `~/.htmlook/bridges/<pid>.port`. A
drop guard removes it on graceful shutdown. The subprocess scans the
dir, ping-validates each candidate (`{"kind":"ping"}` → `"pong"`),
and uses the first live one. Stale files are pruned opportunistically.

Multi-instance dev workflows now just work.

---

## Quality gate — 1014 tests

The test suite expanded substantially this cycle:

- **vitest** (frontend + helpers): **814 passing**
- **cargo** (Rust, `pro` feature): **200 passing**
- **Total**: **1014**

Headline coverage:
- `md-roundtrip.test.ts` — 95 cases + a 196-doc workspace-corpus walk
  with a 9-bucket drift classifier.
- `terminal-tab-close.test.ts` — the regression case for the close-tab
  left-neighbour focus.
- `korean-jamo.test.ts` + `composer.test.ts` + `scenarios.test.ts` —
  72 cases covering the KoreanComposer state machine.
- `mcp_server`, `tools_manifest`, `llm_adapter::permissions`,
  `workspace_meta`, `tools_diag` — Rust-side coverage growing fastest.

Full catalog: [`docs/TEST_SUITE.md`](https://github.com/deep-on/htmlook/blob/main/docs/TEST_SUITE.md)
in the desktop repo.

---

## Smaller polish

- **License dev bypass** — `pnpm tauri dev` builds short-circuit to
  `'pro'` so dogfooding against an expired trial doesn't silently
  disable Edit / Save / AI affordances.
- **Settings polish** — `Saved ✓` flash on immediate-save settings,
  AI-tab named sections (Model / Capabilities / Permissions / Usage),
  Window-tabs settings wrapped in a card with proper hierarchy.
- **macOS chrome** — Settings moves to app menu, PRO badge inside
  toolbar, window min-size enforced, viewport pills auto-hide below
  1000 px, viewer AI-state chip top-right.
- **Sidebar polish** — Name column +12 px (Korean filenames stop
  truncating mid-syllable), drag-drop scoped per-window so a Finder
  drop into one window doesn't copy into every sidebar.

---

## Where to read more

- Full ChangeLog: `CHANGELOG_v1.0.14.md` in the desktop repo
- Test catalog: [`docs/TEST_SUITE.md`](https://github.com/deep-on/htmlook/blob/main/docs/TEST_SUITE.md)
- Round-trip testing deep-dive: [`docs/MD_ROUNDTRIP_TESTING.md`](https://github.com/deep-on/htmlook/blob/main/docs/MD_ROUNDTRIP_TESTING.md)
- Marketing-facing highlight: [htmlook.app/#whats-new](https://htmlook.app/#whats-new)
