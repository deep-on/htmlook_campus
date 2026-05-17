# Terminal

> A real PTY inside the app, designed so an AI agent (Claude / Codex / Gemini) sits *with* you in the same workspace.

## Toggle and dock

| Action | Shortcut |
|---|---|
| Show / hide terminal panel | ⌘\` |
| New tab in current preset | ⌘T |
| Close active tab | ⌘W (when terminal focused) |
| Cycle tabs | ⌃⇥ / ⌃⇧⇥ |
| Split active pane horizontally | ⌘D |
| Split active pane vertically | ⌘⇧D |
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

## "Save as skill" — the bookmark icon button

After you've run a useful one-shot prompt against an AI in a terminal tab (e.g. "summarize the last test output and propose a fix"), click the bookmark icon to save it as a *prompt preset*. It becomes a new button on the preset toolbar that pastes that exact prompt into the active terminal in one click.

These live in `.htmlook/prompt-presets.json` per workspace.

## Korean IME

The terminal handles Korean composition through a dedicated state machine (KoreanComposer) — extracted in v1.0.9 — that tracks `composedState { cho, jung, jong }` and assembles Hangul syllables with `0xAC00 + cho*21*28 + jung*28 + jong`. It also handles compound consonants (ㄳ ㄵ ㄶ ㄺ …) and compound vowels (ㅘ ㅙ ㅚ …).

Previous bugs that were fixed and stay fixed in v1.0.9:
- Mode-toggle first jamo no longer splits "다" into "ㄷㅏ"
- Outfocus → infocus first-character doubling
- `xterm.onData` doubling for single-character Hangul
- PTY write order interleave (Promise-chain serialiser)

If you experience a regression, capture `IME_DEBUG=true` logs and file an issue.

## Pane management

Each tab can hold up to **6 panes** in a Tmux-like grid. Split with ⌘D / ⌘⇧D. The active pane has a slightly brighter border. Click any pane to focus. Cycle with `Cmd+[` / `Cmd+]`.

## Process tree + buffer reading

Each tab exposes its process tree (used by the *Cl/Cx/Gm/Sh* glyph + the `htmlook_terminal_process_tree` MCP tool). An AI agent or the app itself can read the live scrollback buffer via `htmlook_terminal_buffer_get` — useful for "what does the last 50 lines say" review.

## OSC 7 cwd

If your shell emits OSC 7 (`bash` auto-includes it; for `zsh` add to `.zshrc`), the tab title shows the compressed cwd (e.g. `~/W/htmlook`). The brand letter mark stays on the left of the title.

## Send prompt to active terminal

`htmlook-pro:send-to-terminal` is a window-level event used by the prompt-preset buttons and by MCP tools. From within a webview-rendered preview you can dispatch:

```js
window.dispatchEvent(new CustomEvent('htmlook-pro:send-to-terminal', {
  detail: { text: 'pytest -q tests/test_failures.py' }
}));
```

## Context menu

Right-click anywhere in the terminal panel for: *Copy* / *Paste* / *Select all* / *Clear scrollback* / *Reset terminal* / *Rename tab* / *Move to new window*.

## Next

- [ChatPanel · BYOM →](ChatPanel-BYOM.md)
- [Skills →](Skills.md)
