# Troubleshooting

> Quick fixes for the issues we see most. If your symptom isn't here, let us know with the latest `/tmp/htmlook-debug.log` attached.

## App won't launch

- Verify the app is in `/Applications`, not still inside the DMG
- macOS Sequoia or later: open System Settings → Privacy & Security → App Management → toggle HTMLook Pro on
- Worst-case: quit the app, then `rm -rf "~/Library/Application Support/com.deep-on.htmlook-pro/"` — your workspaces are unaffected

## Auto-update doesn't appear

- Quit and restart the app — the check runs on launch
- macOS Sequoia and later need *App Management* permission (System Settings → Privacy & Security → App Management → HTMLook Pro on)
- If you're on a very old build (v1.0.7 or earlier), download the latest manually from `htmlook.app/download/pro-mac` — those builds couldn't auto-update

## "FFmpeg / LibreOffice / Quarto not installed" toast

Click **Install now** — HTMLook drives the install through Homebrew with a streaming log modal. If Homebrew itself is missing the modal installs that first.

If the install seems to hang on a cask package (LibreOffice, Quarto): grant macOS' admin password prompt that may have appeared in the background.

## Korean IME doubling

If you see `ㄷㅏ` instead of `다` in the terminal, capture the IME debug log (Settings → Terminal → enable IME debug) and let us know — recent builds fixed this class of bug but new edge cases happen.

## Voice meter shows zero / silent recordings

On M3 + MacBook Pro with the lid closed (clamshell mode), the internal mic is digitally silent — a known macOS quirk. Open the lid or use an external mic.

## iframe-rendered HTML won't load relative CSS / JS

HTMLook inlines relative assets so the page renders without needing a server. If a page renders fine in a browser but shows up blank inside HTMLook, the assets may not be reachable from the file's directory. Make sure the CSS / JS files are siblings (or in a sub-folder) of the `.html` file.

## Multi-window: changes in one don't reflect in another

Both windows watch the file system; updates take a beat to propagate. If you see persistent staleness:

- Click in the stale window to force a re-sync
- Quit and reopen (last-session restore brings tabs back)
- Workspaces on network mounts (SMB / NFS) don't always notify on change — local folders work best

## AI Assistant returns "no response"

- Check *Settings → AI* — your provider may have denied the request or hit a usage limit
- The streaming response can be cancelled with ⌘. — if it doesn't resume, the provider actually cancelled (not HTMLook)
- Try a different model from the same provider as a sanity check

## Where to send a bug report

Email `support@htmlook.app` with the latest `/tmp/htmlook-debug.log` attached, a one-line description of what you were doing, and which file types you had open.

## Next

- [Settings →](Settings.md)
- Back to [Home](Home.md)
