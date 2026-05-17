# Settings

> ⌘, opens the Settings dialog. Workspace-scoped and global keys both live here.

## Tabs

| Tab | What's in it |
|---|---|
| **General** | Theme (system / light / dark), language (auto / en / ko), update channel (stable / staging), auto-save delay, telemetry (off by default and stays off) |
| **Viewer** | Print header / footer tokens, dual-view sync-scroll default, code-view default for `.md`, font family + size, OpenType features |
| **Terminal** | Preset commands (Claude / Codex / Gemini / Shell), preset prompt-to-text, shell environment, zsh-autosuggestions install button, font family + size, cursor style |
| **AI · BYOM** | Provider list with key per provider, default model, request timeout, vision toggle, system-prompt header, skill auto-inject limit |
| **Permissions** | The 4-button consent decisions; revoke / edit per-tool / per-workspace / global rows |
| **Power tools** | The `tools.json` editor; tier badges; add wizard; mark "detected" overrides |
| **Sidebar** | Default sort, hide dot-files, follow active file, multi-select max (default 200) |
| **Keyboard** | All shortcuts (see [Keyboard shortcuts](Keyboard-Shortcuts.md)) with rebind |
| **Voice** | Mic device override, sample rate, transcript provider hook |
| **About** | Build version, signing identity, manifest endpoint, "Check for updates" button |

## Scope: workspace vs global

Most fields show a small `W` / `G` badge to indicate scope. A workspace-scoped field falls back to the global value when empty; setting it pins it. *Settings → reset to global* on a workspace-scoped field clears the workspace override.

Workspace settings live in `<workspace>/.htmlook/settings.json`. Global lives in `~/Library/Application Support/com.deep-on.htmlook-pro/settings.json`.

## Update channel

`stable` = `pro/latest.json`. `staging` = `pro/staging/latest.json` — a separate manifest the ship pipeline writes when `publish-update.sh --staging` is used. You'd only flip to staging in a dev build to test the auto-update plumbing.

## App Management permission (macOS Sequoia+)

When the updater detects it can't swap the bundle, the in-app modal shows a *System Settings 열기* button that takes you to the right pane. Toggle HTMLook Pro on and click *Retry*.

## CLI tools auto-install

Settings → Power tools → *+Add* opens the BYOM tool wizard. Below it, *Auto-install dependencies* surfaces the consent flow that runs `brew install <tool>` (or `--cask`, or `pipx install …`, or `npm i -g …`) with streaming logs in a modal. Same plumbing the dependency-missing toasts use.

## Sign-in vs accounts

There's no sign-in for Pro. The only "account" concept is the BYOM provider you configure. Easier has a subscription account; Pro doesn't.

## Reset / nuke

*About → Reset settings* clears the global settings file (asks confirm). Workspace settings are unaffected — they live next to your workspace.

To fully reset, quit the app, then `rm -rf "~/Library/Application Support/com.deep-on.htmlook-pro/"`. Your workspaces are not touched.

## Next

- [Keyboard shortcuts →](Keyboard-Shortcuts.md)
- [Troubleshooting →](Troubleshooting.md)
