# Installation

> macOS Apple Silicon · 5 minutes · no admin sign-up.

## 1. Requirements

- macOS 12 (Monterey) or later
- Apple Silicon (M1 / M2 / M3 / M4)
- ~200 MB disk
- Intel Mac build is on the roadmap (v1.0.x); for now the Apple-Silicon build runs under Rosetta but we don't recommend it for daily use

## 2. Download

Direct link: **<https://htmlook.app/download/pro-mac>**

That redirects to the latest signed + notarised DMG in our R2 bucket. The download is ~11 MB.

## 3. First open

1. Open the DMG.
2. Drag **HTMLook Pro.app** onto the `Applications` shortcut. If you already have an older HTMLook Pro, Finder offers *Replace* — accept; your data lives in your workspace folders, not in the .app.
3. Launch from Applications (or Spotlight). The first launch may show *"HTMLook Pro" was downloaded from the Internet* — click **Open**. The app is signed by *Deep-On Inc. (F4GL4XC335)* and notarised by Apple.

> Build verified with `spctl --assess -vv`:
> ```
> source=Notarized Developer ID
> origin=Developer ID Application: Deep-On Inc. (F4GL4XC335)
> ```

## 4. Permissions you may see

Permissions are asked lazily — only when a feature needs them.

| Prompt | When it appears | Why |
|---|---|---|
| **Microphone** | First voice memo | AAC recording for `.htmlook-voice/*.m4a`. The text below the system prompt explains the recording is local-only. |
| **Files and Folders** | Opening a workspace outside common dirs | macOS scopes file access per app + folder. Pick *Allow*. |
| **App Management** | Auto-update attempting to swap the bundle | macOS Sequoia and later. Grant once in System Settings → Privacy & Security → App Management → toggle HTMLook Pro on. The updater also shows an in-app hint. |

You can revoke any of these later in System Settings. The app degrades gracefully.

## 5. Auto-update

HTMLook Pro **v1.0.8 and later** check the manifest at <https://htmlook-releases.kdk3606.workers.dev/pro/latest.json> on launch. When a newer signed build is available you'll see the update glyph in the top-right. Click → download → restart. Your workspaces, settings, and sidecars are not touched.

> **v1.0.7 and earlier** can't auto-update — their build was pinned to a now-private GitHub Releases endpoint. Download v1.0.9 manually from the link above; drag-and-drop into `/Applications` and Finder will replace it.

## 6. Optional CLIs HTMLook Pro can drive

Not required to run the app. Install only the ones you want to use:

- `ffmpeg` → video scene detection, video chapter previews — `brew install ffmpeg`
- `soffice` (LibreOffice) → DOCX/PPTX → PDF conversion — `brew install --cask libreoffice`
- `quarto` → `.qmd` rendering — `brew install --cask quarto`
- `pandoc` → richer Markdown export — `brew install pandoc`
- Agent CLIs (`claude`, `codex`, `gemini`) → run inside HTMLook's terminal as a paired AI; install per the vendor docs

If you call a feature without its dependency installed, HTMLook surfaces a friendly toast with the install command + a one-click **지금 설치** button.

## Next

- [Workspace →](Workspace.md)
- [UI Overview →](UI-Overview.md)
