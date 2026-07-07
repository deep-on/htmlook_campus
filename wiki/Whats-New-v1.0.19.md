# What's New — v1.0.19

Released: **2026-07-07** · Download: [htmlook.app](https://htmlook.app)

> 다른 언어: [한국어](Whats-New-v1.0.19-ko.md)

Three big themes this version: open a **remote server's folder (over SSH)
as a workspace**, a **real browser** built into the app, and HTMLook Pro
now **runs on Windows** too. On top of that: file compare, in-place
archives, PDF annotation, more languages, and a noticeably faster app.

---

## Remote workspace (SSH)

Connect to a remote server over SSH and open one of its folders as a
workspace. The sidebar, viewer, and terminal all point at that server, so
you open and edit its files just like a local folder and run a terminal
right there. Add, edit, and remove servers in Settings, and have the ones
you use often connect automatically on launch.

- **Move between places** — keep your local machine and several remotes
  connected at once and switch with the workspace switcher. Move, copy,
  and delete remote files too.
- **Connect anywhere** — plain Linux servers, plus Windows, WSL, and
  container hosts. If the server is missing what it needs, the app sets it
  up for you.

## In-app browser

Open a link or an address from a document in a browser tab without leaving
the app. Back, forward, home, bookmarks, history, and zoom — it works like
any browser.

- **Window for logins & CAPTCHAs** — when a login or a CAPTCHA is needed,
  it pops out into its own small window.
- **Let your AI drive the browser** — the AI you connect can operate this
  browser directly and handle web tasks for you.

## Now on Windows

HTMLook Pro now runs on Windows too. Double-click a file to open it, and
document conversion, voice recording, and the terminal all work the
Windows way.

## Compare files

Pick two files and set them side by side to see what changed. Changes are
colored line by line and word by word, with a minimap of the whole file at
a glance.

## Working with documents & files

- **Open & extract archives** — open a .zip inside the app, look through
  it, and extract it wherever you want.
- **Annotate PDFs** — mark up a PDF with rectangles, ellipses, pen, and
  text. The tool palette moves and resizes.
- **Two folders side by side** — split the sidebar in two to browse
  different folders together. Drag files onto a folder to move or copy
  them (hold ⌘ to switch move/copy), and make a new folder inside a
  subfolder.
- **Sharper find** — Korean and CJK matches land in exactly the right
  place, and PDF highlights follow the glyphs as you zoom.
- **Save & export location** — the Save As and Export dialogs open in the
  file's own folder (or the workspace folder for a new file).
- **Office conversion** — convert PowerPoint and Word documents with your
  installed Office (or a fallback) to preview them.

## Refinements

- **New look** — a lighter, calmer palette by day and a graphite tone by
  night, applied across the whole app. The terminal follows the app's
  day/night too.
- **Attach notes** — like voice memos, attach a short written note to a
  file.
- **More languages** — text throughout the app is set in Korean, English,
  Japanese, and Chinese.

## Faster, fewer stalls, more stable

Opening a new window and starting up are much quicker, and the brief pause
when opening and closing Settings is gone. The app uses less CPU when idle
and holds onto less memory over time, and it's hardened so it won't crash
on things like an unreadable file or a corrupt archive.
