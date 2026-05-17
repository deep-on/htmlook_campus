# Wizards

> The setup wizards you'll meet along the way — what they ask, what they do, when they reappear.

A wizard is a short, modal sequence — usually 3 to 5 cards — that helps you get to the right state. They never trap you (every wizard has *Skip* / *Later*) and you can always re-launch them from the matching menu.

## First-run AI setup (Pro)

**Appears**: the first time you press ⌘I or click the AI Assistant glyph.
**Asks**: pick a provider (OpenAI / DeepSeek / Mistral / Together / Groq / Cerebras / Ollama / Custom) → paste API key → choose a default model → test the connection.
**Result**: an AI provider record under *Settings → AI*, ready to use.
**Re-launch**: *Settings → AI → + Add provider*.

Skip if you want; the AI Assistant panel stays usable for browsing past conversations and you can revisit setup anytime.

## First-launch onboarding (both builds)

**Appears**: the very first launch of the app.
**Asks**: which role best describes you (writer / engineer / researcher / PM / lawyer / designer / educator / data analyst / consultant + a "skip" option).
**Result**: HTMLook suggests one Tutorial that fits and unlocks a sample workspace for it.
**Re-launch**: *Help → Show first-launch onboarding*.

The role is a recommendation source only — nothing is locked behind it. You can do any tutorial regardless of what you picked.

## New Workspace Wizard (Pro · ⌘⇧N)

**Appears**: ⌘⇧N, or *File → New → Workspace Wizard…*.
**Asks**: pick a starting point — *Empty folder*, *From a template*, *From a Profile pack*, or *Clone from URL*. Then name + location.
**Result**: a fresh workspace folder, optionally seeded with a template's files.
**Tip**: Profile packs are pre-built workspaces for specific roles (e.g. "Consultant — client pitch deck") with the right Extensions enabled and sample files included.

## New from Template (⌘⇧T)

**Appears**: ⌘⇧T, or *File → New → From Template…*.
**Asks**: pick a template — Markdown article, Slide outline, Meeting note, Research one-pager, blank HTML, etc.
**Result**: a new file in the current workspace, opened as a tab.

## Add Extension wizard (Pro)

**Appears**: *Settings → Tools → + Add*.
**Asks**: name, description, version, license, what kind of thing it does (renderer for a code-block language? new Export format? AI helper?), and the recipe body.
**Result**: a Markdown file in the workspace's `.claude/skills/` ready to be invoked.
**Skip-able**: yes — you can keep using HTMLook with only the built-in Extensions.

## Profile install (Pro)

**Appears**: *File → New → Install from URL…*.
**Asks**: paste a Profile pack URL (or pick from the curated list).
**Result**: HTMLook downloads the pack into a new workspace folder and enables its Extensions.
**Where they come from**: the Profile catalogue, browsed in *File → Browse profiles…*

## Dependency install (any platform-tool consumer)

**Appears**: when you call a feature that needs an external tool (e.g. *Export → PowerPoint* needs LibreOffice) and the tool isn't installed.
**Asks**: shows the install command (`brew install --cask libreoffice`) with **Install now** / **Copy command** / **Close**.
**Result**: streams the install log live in a modal; on success the original feature runs.
**Re-launch**: *Settings → Tools → click the dim ring next to the missing tool*.

## App Management permission (macOS Sequoia +)

**Appears**: when auto-update tries to swap the bundle and macOS blocks it.
**Asks**: click *System Settings 열기* — toggles you straight to the right pane in System Settings.
**Result**: after you flip the toggle on, click *Retry* and the update proceeds.

## Save as preset (terminal)

**Appears**: when you click the bookmark icon in the terminal preset toolbar.
**Asks**: name + (optional) description for the prompt you just used.
**Result**: a new "+ <name>" button on the preset toolbar that pastes that exact prompt into the active terminal with one click.

## Why so many?

HTMLook's principle: never assume context. Every state that needs a value (API key, provider, target folder, missing dependency) gets its own short wizard, in plain language, with a *Skip* option. The trade-off is meeting more dialogs early — and meeting almost none after the first week.

## Next

- [Tutorials →](Tutorials.md)
- [Settings →](Settings.md)
