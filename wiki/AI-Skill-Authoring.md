# Skill authoring (for AI)

> A skill is one markdown file. Drop it in `.claude/skills/`. HTMLook reads it on the next file-watcher tick.

## Why an agent should care

When you run inside HTMLook's ChatPanel, the loader injects the **top-5 relevant skills** into your system prompt. A well-written skill lets HTMLook offload prompt-engineering boilerplate from every conversation and into a versionable artifact.

## File location

`<workspace>/.claude/skills/` (workspace-scoped) or `~/.claude/skills/` (global). Workspace wins on `name:` conflict. The `.agents/skills/` siblings exist for Codex / Aider / Gemini CLI interop.

## Frontmatter contract

```yaml
---
name: meeting-notes-cleanup     # unique identifier, kebab-case
description: |                   # one-line summary, shown in the chip
  Polishes raw transcripts into per-speaker summaries.
version: 1                       # bump when behaviour changes
tier: custom                     # custom | curated | verified
license: MIT                     # SPDX identifier
trigger:                         # how the top-5 selector finds it
  workspace_kinds: [text, audio] # text / audio / video / pdf / image / code
  hint:                          # freeform strings; high weight when present
    - "meeting"
    - "회의"
    - "minutes"
tools: []                        # MCP tools the skill needs at runtime
claims:                          # language-keyed extra context
  ko: "회의록을 화자별로 정리합니다."
  en: "Cleans up meeting transcripts speaker by speaker."
---
```

Every field has a serde-default; partial frontmatter is fine.

## Body conventions

The body becomes part of your system prompt when the skill is injected. Treat it as the prompt template — keep it focused.

Pattern that works:

```markdown
# What this does
Polishes raw meeting transcripts into a per-speaker structured summary.

# When to use
- User has voice memo with multiple speakers
- Or transcribed meeting notes with speaker labels

# Output shape
- A markdown document with per-speaker H2 sections
- Each section: bullet decisions, action items, blockers
- Top of file: meeting date + attendees

# Tools you should call
- `htmlook_voice_transcript_get` → fetch transcript
- `htmlook_voice_workspace_all` → enumerate memos in workspace
- `htmlook_create_file` → write the polished note next to the memo
```

## Registering languages and formats

A skill can register:

- a code-block language: `code_block: { fence: "mmd", icon: "mermaid" }` → the markdown viewer routes ```` ```mmd ```` blocks here
- an export format: `export: { format: "pptx", label: "Slide deck" }` → appears in the Export dropdown

```yaml
code_block:
  fence: mermaid
  icon: mermaid
export:
  format: mp4
  label: Animated SVG → mp4
```

## Skill ↔ tool whitelisting

The `tools:` array constrains which MCP tools the skill is permitted to call when active. Use it as a defence-in-depth — even if the user has globally allowed `apply_edit`, a skill that doesn't declare it can't call it.

```yaml
tools:
  - htmlook_voice_transcript_get
  - htmlook_voice_workspace_all
  - htmlook_create_file
```

Empty list = no tools (read-only skill, transformation in the prompt only).

## Versioning + migration

HTMLook tracks schema version in `<workspace>/.htmlook/tools.json`. When you change a skill's frontmatter shape in a breaking way:

- Bump `version:`
- The next `tools_manifest` load runs `migrate_if_needed()` — writes a `tools.json.bak.<ts>` next to the live file before the in-place rewrite

## Authoring loop

1. Write `name`, `description`, `tools` first — the skeleton
2. Add the body — start with "When to use" and "Output shape"
3. Load `htmlook` in the user's app — *Settings → Power tools → Reload skills*
4. Test in ChatPanel with a prompt that should trigger your skill
5. Iterate; bump `version` when behaviour changes

## Skill marketplace (future)

`tier: curated` is reserved for skills that Deep-On has reviewed. A future marketplace ships these as a workspace-installable bundle. `tier: verified` is built-in.

For now, your skills go in `tier: custom`. Set the field; the badge in Sidebar reflects it.

## Next

- [Prompt patterns →](AI-Prompt-Patterns.md)
- [Errors & recovery →](AI-Errors-Recovery.md)
