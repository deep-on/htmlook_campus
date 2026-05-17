# Installation

> macOS Apple Silicon · 5 minutes · no sign-up.

## 1. Requirements

- macOS 12 (Monterey) or later
- Apple Silicon (M1 / M2 / M3 / M4)
- ~200 MB disk
- Windows build: coming. Intel Mac build: on the roadmap

## 2. Download

Direct link: **<https://htmlook.app/download/pro-mac>**

The download is ~11 MB. Signed and notarised by Apple.

## 3. First open

1. Open the DMG.
2. Drag **HTMLook Pro.app** onto the `Applications` shortcut. If you already have an older HTMLook Pro, Finder will offer *Replace* — accept; your data lives in your workspace folders, not in the app.
3. Launch from Applications or Spotlight. The first launch may show *"HTMLook Pro" was downloaded from the Internet* — click **Open**.

## 4. Permissions you may see

Permissions are asked only when a feature actually needs them.

| Prompt | When it appears | Why |
|---|---|---|
| **Microphone** | First voice memo | To record into your workspace. The recording stays on your device. |
| **Files and Folders** | Opening a workspace outside common dirs | macOS scopes file access per app + folder. Pick *Allow*. |
| **App Management** | Auto-update wants to swap the bundle | macOS Sequoia and later. Grant once in System Settings → Privacy & Security → App Management → toggle HTMLook Pro on. The updater also walks you to the right pane. |

You can revoke any of these later in System Settings. The app degrades gracefully.

## 5. Auto-update

HTMLook Pro checks for updates in the background on launch. When a newer build is available you'll see an update glyph in the top-right of the window. Click → download → restart. Your workspaces, settings, and notes are not touched.

## 6. Optional CLIs HTMLook Pro can drive

Not required to run the app. Install only the ones you want to use:

- `ffmpeg` → video scene detection, chapter preview
- `LibreOffice` → DOCX / PPTX rendering and conversion
- `Quarto` → `.qmd` rendering
- `Pandoc` → richer Markdown export
- Agent CLIs (`claude`, `codex`, `gemini`) → run inside HTMLook's terminal as a paired AI

If you call a feature without its tool installed, HTMLook shows a friendly toast with a **Install now** button — one click and it handles the install with a progress modal.

## Next

- [Quick start →](Quick-Start.md)
- [Workspace →](Workspace.md)
- [UI Overview →](UI-Overview.md)
