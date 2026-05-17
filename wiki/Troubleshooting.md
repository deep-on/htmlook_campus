# Troubleshooting

> Quick fixes for the issues we see most. If the symptom isn't here, capture `/tmp/htmlook-debug.log` and open a ticket.

## App won't launch

**Symptom**: clicking the icon does nothing, or the app immediately quits.

- Check `/tmp/htmlook-debug.log` for the most recent run
- Verify the bundle is stapled — `xcrun stapler validate "/Applications/HTMLook Pro.app"` should print *worked*
- macOS Sequoia: System Settings → Privacy & Security → App Management → toggle HTMLook Pro on
- Fully reset settings (worst-case): `rm -rf "~/Library/Application Support/com.deep-on.htmlook-pro/"` — your workspaces are unaffected

## Auto-update doesn't appear

- v1.0.7 and earlier can't auto-update (private repo issue + hardcoded version). Download v1.0.9 manually from `htmlook.app/download/pro-mac`
- For v1.0.8+: check `https://htmlook-releases.kdk3606.workers.dev/pro/latest.json` is reachable
- The updater also needs *App Management* permission on macOS 15 Sequoia and later

## "FFmpeg / LibreOffice / Quarto not installed" toast

Click *지금 설치* — HTMLook drives the install through Homebrew with a streaming log modal. If Homebrew itself is missing the modal installs that first.

If brew install hangs forever: it's almost certainly the sudo timestamp issue with cask packages. The cask packages (LibreOffice, Quarto) use the macOS pkg installer + osascript admin prompt instead of regular brew.

## Korean IME doubling

If you see `ㄷㅏ` instead of `다` in the terminal, capture an `IME_DEBUG=true` recording (Settings → Terminal → enable IME debug) and file an issue with the log. v1.0.9 fixed this class of bugs via the KoreanComposer state machine; a regression would indicate a new edge case.

## Voice meter shows zero / silent recordings

On M3+ MacBook Pro with the lid closed (clamshell mode), the **internal mic is digitally silent** — known macOS bug. Open the lid or use an external mic. HTMLook flags this with a one-time warning toast.

## CPU goes 100% on terminal close

Symptom: closing all terminal tabs leaves `login -pf` orphan processes consuming CPU. Cause: Tauri dev rebuild + terminal panel interaction. v1.0.8+ landed a fix that reaps orphans on tab close. If you see it on v1.0.9+, file an issue with `ps aux | grep login` output.

## Iframe-rendered HTML won't load relative CSS / JS

The viewer inlines relative assets into `srcdoc` because WKWebView's base-URL handling can't resolve them. If a page renders fine in a browser but blank in HTMLook, capture the HTML and check whether the resources are reachable from the file's directory. Open an issue with a minimal repro.

## Multi-window: changes in one don't reflect in another

Both windows watch the file system; the file-watcher debounce is ~300 ms. If you see persistent staleness:

- Click in the stale window to force a focus event (which re-syncs the active tab)
- Quit and reopen (workspaces restore)
- Filesystem corner case: check if your workspace lives on a network mount; SMB / NFS don't always fire FSEvents

## ChatPanel returns "no response"

- Check *Settings → AI · BYOM → Permissions* — your provider may have denied the request
- Inspect the BYOM provider's status page; HTMLook surfaces upstream errors as plain text
- The streaming response can be cancelled with ⌘. — if it doesn't resume, the response was actually cancelled by the provider, not by HTMLook

## Where to file issues

While the repo is private during pre-launch: e-mail the maintainer (`kdk3606@deep-on.com`) with `/tmp/htmlook-debug.log` and a description of what you were doing.

## Next

- [Settings →](Settings.md)
- Back to [Home](Home.md)
