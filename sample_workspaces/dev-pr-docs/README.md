# dev-pr-docs — HTMLook + LLM for PR review with docs in the same view

A 15-second polished "PR shipped" teaser that demonstrates the
**developer review** workflow: keep the PR diff on the left pane and
`docs.md` on the right pane while asking an LLM to flag which doc
lines drift if the PR merges.

The fictional repo is **WorkflowKit** — a small open-source library
that has just shipped PR #847 (`feat(api): rename listJobs ->
queryJobs + paging cursor`).

## What you get

- `index.html` — the completed 15-s "PR shipped" teaser. Pure-black
  background with GitHub-green and terminal-cyan accents. Four scenes:
  intro tag, kinetic typography stats, faux git-graph merge, brand
  outro.
- `prompts.txt` — five English LLM prompts: one for "find drift",
  one for "draft a docs patch", plus three follow-ups.
- `brand.txt` — the WorkflowKit palette + copy guardrails.
- `hyperframes.json`, `meta.json` — HyperFrames scaffold.

## The workflow it shows

You are a backend / fullstack developer reviewing a PR that touches
real code AND should require docs updates. Without HTMLook this is
two terminals, two editors, and a lot of alt-tabbing. With HTMLook:

1. Open the workspace. **Left pane = `PR.diff`** (color-coded `+`/`-`
   lines). **Right pane = `docs/api.md`** (rendered markdown). The
   sidebar shows the PR's touched files.
2. Ask the LLM in the bottom terminal:
   *"Show which doc lines describe code that this diff changes."*
   The LLM cites diff hunks and the docs lines that reference them.
   The right pane scrolls to flagged sections.
3. Pause on a stale paragraph. Ask the LLM to **draft a docs patch**.
   The right pane reloads with the new wording highlighted.

## Try it

Open this folder as a workspace in **HTMLook Pro**. Place a real PR
diff at `PR.diff` and a docs file at `docs/api.md`, then attach the
HTMLook MCP to your LLM of choice (Claude, Codex, Llama via Ollama,
Gemini, GPT, etc.). Drop the `[1]` prompt from `prompts.txt` into
the terminal pane.

With the HTMLook MCP attached, the LLM will:

1. Call `htmlook_pane_pair` → see the diff (left) and the docs
   (right).
2. Call `htmlook_active_file` → identify which file is in focus.
3. Call `htmlook_cite("right", "L42-L58")` to anchor the stale
   paragraph in the docs.
4. Call `htmlook_apply_edit` to insert the rewritten markdown.
5. Hot-reload kicks in — the right pane re-renders the patched
   docs and you visually confirm.

## Why this matters

PRs that should update docs almost never do, because docs live in a
different mental window. HTMLook puts them on screen at the same
time, and lets the LLM trace the specific drift before merge — not
after the bug report.

## Why HTMLook

The same four HTMLook moves you saw in `hf-claude` and `hf-llama`
(dual-pane MCP, `cite`, `apply_edit`, auto-reload) work here too —
except the right pane is now a docs file instead of a video, and the
artifact is a docs patch instead of an mp4. **Same primitives, new
craft.**
