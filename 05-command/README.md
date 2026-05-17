# Step 5 · Command (Terminal / Chat / Apply)

<p align="center">
  <b>English</b> | <a href="README.ko.md">한국어</a> | <a href="README.ja.md">日本語</a> | <a href="README.de.md">Deutsch</a> | <a href="README.fr.md">Français</a> | <a href="README.es.md">Español</a> | <a href="README.pt.md">Português</a> | <a href="README.it.md">Italiano</a>
</p>

> Step 4 taught you how to point at *where*. This step turns that into
> *commands*. The cite + apply_edit cycle.
> ~ 10 min.

This is the deepest part of the campus — the 26 persona walkthroughs
live here ([`personas/`](personas/)). At first, just follow the one in
your domain.

## 5.1 · Four command patterns

| Pattern | Where | Input shape |
|---|---|---|
| **Chat (BYOM chat)** | Right-hand AI panel | natural language + auto-attached cite anchor |
| **Terminal CLI** | Toggle ⌘J, run `claude` / `codex` / `gemini` | shell prompt |
| **External MCP client** | Claude Code / Cursor / Windsurf / Zed | that client's chat box |
| **Inline cite link** | a `[B14](xlsx://q3.xlsx#B14)` in the response | click → jump to that anchor |

## 5.2 · The cite + apply_edit cycle

```
[pick an area from Step 4]
   → cite anchor attaches to the AI panel
   → natural-language prompt
   → LLM calls htmlook_apply_edit
   → file changes
   → file watcher auto-reloads the right pane
```

Four anchor videos (30 s each):

| # | Video | Pattern |
|---|---|---|
| 7 | [Cite the cell. Get the narrative.](../videos/features/07-advanced-01-xlsx-cite.mp4) | xlsx cell cite |
| 8 | [14:14 → paragraph.](../videos/features/08-advanced-02-live-cue-cite.mp4) | video-timestamp cite |
| 9 | [One cite. Three files.](../videos/features/09-advanced-03-multi-target.mp4) | one cite → patches in multiple files |
| 17 | [Cross-file anchors. Recorded.](../videos/features/17-advanced-11-cross-link.mp4) | `.htmlook/links.json` sidecar |

## 5.3 · Persona walkthroughs (26)

A *day-in-the-life* workflow per role / domain. 60–70 s mp4 + a
follow-along sample workspace + a step-by-step `WALKTHROUGH.md`.

Full catalog: [`personas/INDEX.md`](personas/INDEX.md). The recommended
order is grouped by role:

- **Dev**: [`personas/01-hf-claude/`](personas/01-hf-claude/) →
  [`02-hf-llama/`](personas/02-hf-llama/) →
  [`03-dev-pr-docs/`](personas/03-dev-pr-docs/)
- **Content**: [`personas/04-creator-podcast/`](personas/04-creator-podcast/) →
  [`12-press-editor/`](personas/12-press-editor/) →
  [`15-picture-book/`](personas/15-picture-book/) →
  [`22-hobby-fiction/`](personas/22-hobby-fiction/)
- **Analysis**: [`personas/09-data-analyst/`](personas/09-data-analyst/) →
  [`11-finance-report/`](personas/11-finance-report/) →
  [`10-research-notes/`](personas/10-research-notes/) →
  [`06-economy-analyst/`](personas/06-economy-analyst/)
- **Legal / translation**: [`personas/08-legal-redline/`](personas/08-legal-redline/) →
  [`07-translator-book/`](personas/07-translator-book/) →
  [`05-domain-battery/`](personas/05-domain-battery/)
- **Education (teachers)**: [`personas/17-teacher-quiz/`](personas/17-teacher-quiz/) →
  [`18-teacher-newsletter/`](personas/18-teacher-newsletter/) →
  [`19-teacher-record/`](personas/19-teacher-record/)
- **Education (students)**: [`personas/20-student-notes/`](personas/20-student-notes/) →
  [`24-student-flashcard/`](personas/24-student-flashcard/) →
  [`23-homework-helper/`](personas/23-homework-helper/) →
  [`21-kid-coding/`](personas/21-kid-coding/) →
  [`14-kids-science-mag/`](personas/14-kids-science-mag/)
- **Business**: [`personas/16-corp-deck/`](personas/16-corp-deck/) →
  [`13-product-prd/`](personas/13-product-prd/)
- **Everyday**: [`personas/25-recipe-card/`](personas/25-recipe-card/) →
  [`26-mobile-news/`](personas/26-mobile-news/)

## 5.4 · The follow-along pattern

Inside every persona folder:

- `WALKTHROUGH.md` — step-by-step (`[VIEW]` / `[AI]` markers)
- `before/` — pre-edit state (for visual comparison)
- `after/` — post-edit state (so users without AI can still see the result)
- the domain content files (md / html / pdf / xlsx / svg / py / mp3, …)

## 5.5 · LLM-agnostic — vendor swap

The same cite + apply_edit workflow runs identically across the 9
vendors. Add another vendor in [Step 3](../03-byom-setup/) and swap —
same result.

## ✅ Step 5 checkpoint

- You watched one persona video (60–70 s) close to your role.
- You followed the `[VIEW]` steps of that persona's `WALKTHROUGH.md`.
- (If you have AI set up) You ran the `[AI]` steps → the right pane
  reloaded.
- (If not) You compared `before/` vs `after/` in split view.

All done? → [Step 6 · save-as-skill](../06-save-as-skill/) — register a
recurring workflow in the app permanently.

## Further reading

- [`personas/INDEX.md`](personas/INDEX.md) — 26-persona catalog + video
  ↔ folder mapping.
- [`personas/README.md`](personas/README.md) — how to use the sample
  workspaces.
- [`../03-byom-setup/AI_GUIDE.md`](../03-byom-setup/AI_GUIDE.md) — the
  ~22 MCP tools + the AI-agent output tone guide.
