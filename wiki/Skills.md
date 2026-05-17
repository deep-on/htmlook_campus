# Skills

> Drop a `SKILL.md` into a folder. HTMLook treats it as a tool the AI can use.

## What a skill is

A skill is a plain markdown file with a YAML frontmatter that tells HTMLook how to invoke it and when. The body is the instructions the AI sees. Anyone — you, a coworker, the Deep-On team — can write one and drop it into the workspace.

```markdown
---
name: 회의록-정리
description: Speaker-by-speaker meeting note refinement
version: 1
tier: custom
trigger:
  workspace_kinds: [text, audio]
  hint: "meeting", "회의", "minutes"
tools: []
license: MIT
---

# What this does
Polishes raw meeting transcripts into a clean per-speaker summary…
```

## Where skills live

| Path | Scope | Notes |
|---|---|---|
| `<workspace>/.claude/skills/` | Workspace | Wins on name conflict |
| `<workspace>/.agents/skills/` | Workspace (cross-tool) | Compatible with Codex / Aider / Gemini CLI |
| `~/.claude/skills/` | Global | Personal collection |
| `~/.agents/skills/` | Global cross-tool | — |

HTMLook scans on launch and on filesystem change. Workspace files override global ones with the same `name:`.

## Tier badges

- **Verified** (🟦 cyan) — built-in, ships in the binary
- **Curated** (🟨 amber) — Deep-On reviewed (future marketplace)
- **Custom** (◯ neutral) — workspace-added

Shown next to each skill in the sidebar's *Power tools* expansion and as a chip in ChatPanel.

## Built-in skills (v1.0.9)

- **Mermaid** — renders ```` ```mermaid ```` / ```` ```mmd ```` blocks
- **D2** — renders ```` ```d2 ```` blocks
- **Smart Markdown** — pandoc-style polish on export
- **Pandoc Wrap** — DOCX / PDF passes through pandoc
- **Slide Deck** — pptx export from markdown sections

## How a skill becomes a tool

When the AI calls one, HTMLook does:

1. Read the skill's `tools:` array — declared sub-tools the skill needs
2. Inject the skill body into the system prompt
3. Set the model context so the skill's instructions are top-priority
4. Dispatch any tool calls back through the BYOM consent flow

The skill author can declare a custom `trigger:` block — `workspace_kinds` and freeform `hint` strings — that the top-5 selector uses to decide if the skill is relevant for this conversation.

## Add a skill from the UI

*Sidebar → Power tools → +Add*. The wizard asks for name, description, version, license, body. Output goes to `<workspace>/.htmlook/tools.json` and (optionally) a paired `SKILL.md`.

You can also `git clone` a skill collection into `.claude/skills/` and HTMLook picks it up on next file-watcher tick.

## Auto-migration

HTMLook tracks the schema version in `tools.json`. On startup it `migrate_if_needed()` — writes a backup next to the file (with timestamp suffix) and runs a forward migration. The current schema is v2.

## Markdown code-block dispatch

Skills can register a fenced-code language. When the markdown viewer sees ```` ```mmd ```` it routes the body to the Mermaid skill's renderer; ```` ```d2 ```` to the D2 skill. New languages register via the skill manifest, so adding "graphviz" is one workspace file.

## Export menu integration

Skills can also register **export formats**. The Skill manifest adds entries like `{ format: "mp4", label: "Animated SVG → mp4" }` that show up in the Export dropdown next to the built-ins.

## Errors

The Error-Copy table (`docs/SKILL_ERROR_COPY.md`) maps internal error codes to friendly user-facing strings, so a missing `tools:` field shows "Skill is missing a required field: tools" instead of a stack trace.

## Next

- [Export →](Export.md)
- [For AI Agents · Skill authoring →](AI-Skill-Authoring.md)
