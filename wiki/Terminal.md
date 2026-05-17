# Terminal

> A real terminal inside the app, designed so an AI assistant (Claude / Codex / Gemini) sits *with* you in the same workspace.

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

## Next

- [AI Assistant →](ChatPanel-BYOM.md)
- [Extensions →](Skills.md)
