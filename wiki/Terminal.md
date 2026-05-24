# Terminal

> A real terminal inside the app, designed so an AI assistant (Claude / Codex / Gemini) sits *with* you in the same workspace.

![Terminal panel with Claude / Codex / Gemini / Shell presets](images/05-terminal.png)

## Toggle and dock

| Action | Shortcut |
|---|---|
| Show / hide terminal | ⌘J |
| New tab in current preset | ⌘T |
| Close active tab | ⌘W (when terminal focused) |
| Cycle tabs | ⌃⇥ / ⌃⇧⇥ |
| Split active pane top/bottom | ⌘D |
| Split active pane left/right | ⌘⇧D |
| Cycle dock position (bottom / right / left / center) | Activity Bar icon, or drag the grip |

You can resize the panel via the drag handle on its inner edge.

## Presets (the four "+" buttons)

The preset toolbar opens new tabs preconfigured to run a specific CLI:

| Preset | Command | Letter mark |
|---|---|---|
| Claude | `claude` | **Cl** |
| Codex | `codex` | **Cx** |
| Gemini | `gemini` | **Gm** |
| Shell | (your `$SHELL`, default `zsh`) | **Sh** |

The letter mark appears on the tab. It animates while output is streaming. The preset's launch command is editable in *Settings → Terminal → Preset commands*.

At narrow widths the toolbar collapses: button labels disappear, only the brand letter marks remain.

## "Save as preset" — the bookmark icon button

After you've typed a useful one-shot prompt at an AI in a terminal tab (e.g. "summarize the last test output and propose a fix"), click the bookmark icon to save it. It becomes a new button on the preset toolbar that pastes that exact prompt into the active terminal with one click.

These live in the workspace under `.htmlook/`.

## Korean IME

Korean composition works the way you expect: typing `다` produces `다`, not `ㄷㅏ`, even right after switching IME modes. Pre-edit composition shows in place. If you ever see a regression, capture an `IME_DEBUG=true` log (Settings → Terminal) and let us know.

## Pane management

Each tab can hold up to **6 panes** in a Tmux-like grid. Split with ⌘D / ⌘⇧D. The active pane has a slightly brighter border. Click any pane to focus. Cycle with `Cmd+[` / `Cmd+]`.

## Process tree on the tab

The terminal tracks what's running in each tab — `claude`, `codex`, `gemini`, plain shell — and reflects it in the tab's letter mark. When the AI is generating output, the mark gently pulses.

## OSC 7 cwd

If your shell emits OSC 7 (`bash` auto-includes it; for `zsh` add the snippet to your `.zshrc`), the tab title shows the compressed cwd (e.g. `~/W/htmlook`). The brand letter mark stays on the left of the title.

## Send selection to terminal

Highlight text in the viewer, hit ⌘⌥⇧T (or *View → Send Selection to Terminal*), and it's pasted into the active terminal pane. Useful for "run this command" code samples in docs.

## Context menu

Right-click anywhere in the terminal panel for: *Copy* / *Paste* / *Select all* / *Clear scrollback* / *Reset terminal* / *Rename tab* / *Move to new window*.

## Persistence — tmux backend (v1.0.14+)

Terminals are now backed by **tmux** instead of raw PTY ownership. Sessions outlive the app process: close HTMLook, reopen, and you land in the same scrollback.

Turn on in **Settings → Terminal → Persistence → tmux**. (The legacy *visual buffer* mode is still available — restore the rendered output without keeping the shell alive.)

### What tmux mode gets you

- **Reattach in place** — close the app, reopen, every pane's scrollback returns. The tab labels reflect the *real* foreground process (`claude`, `codex`, your shell), not what HTMLook *thinks* should be there.
- **Preset auto-resume** — a tab created with the Claude / Codex preset notices that the workspace already has a session and quietly resumes it instead of starting fresh.
- **Reattach survives Korean folder names** — your tmux sessions reattach to the same workspace whether your folder is `~/Works/project` or `~/Works/배터리진단`.

### In-buffer search

`⌘F` opens a search overlay inside the active pane. Hit counter shows `M of N`; `↵` walks forward, `⇧↵` backward, `⎋` closes.

### Sync input across panes

Open the pane context menu (⌃ click the pane header) → *Sync input with…* → pick the other panes. A green band marks every pane in the sync group. Type once, every pane receives the keystrokes. Useful for `git pull` in three repos at once, etc.

### Drag-swap panes

Drag a pane header onto another pane header to swap positions.

### Detach a pane into its own window

`⌘D` on the focused pane (when terminal is focused) or *Pane context menu → Move to new window*. The tmux session moves with the pane — same scrollback, same running command.

### Workspace tmux popover

ActivityBar tmux button shows every htmlook tmux session on the machine — *This workspace* + *Other workspaces*. Click an orphan to attach back; click a live pane row to focus it in the current window.

### Keyboard selection mode

`⌃⇧K` enters block-selection mode in the active pane:

| Key | Action |
|---|---|
| Arrow keys | Move cursor |
| Shift + arrow | Extend selection |
| Home / End / PgUp / PgDn | Navigate by line / page |
| `⌘C` | Copy selected text |
| `⎋` | Exit selection mode |

You can change the binding in Settings → Terminal → *Selection mode shortcut*.

### Tab close → left neighbour

Closing the rightmost terminal tab moves focus to its **left neighbour**, matching macOS Terminal / iTerm. Previously this jumped back to tab 0.

### Korean-named workspaces

Terminal panes work in Korean-named workspaces (`/Users/you/Works/배터리진단`) the same as any other path. v1.0.14 fixed a freeze that previously occurred when opening such a workspace.

## Next

- [AI Assistant →](ChatPanel-BYOM.md)
- [Extensions →](Skills.md)
