# legal-redline — HTMLook + LLM for clause-by-clause contract review

A 15-second polished contract redline memo that demonstrates the
**contract reviewer** workflow: keep the contract PDF on the left
pane and your redline memo on the right pane, while asking an LLM
to cite each clause, evaluate risk, draft counter-language, and
splice it back into the memo via `htmlook_apply_edit`. The right
pane auto-reloads after every clause.

The fictional contract is **Master Services Agreement v2 · Acme ×
Vault** — a Series-B startup (Vault) reviewing the standard MSA
sent over by a vendor (Acme).

## What you get

- `index.html` — the completed 15-s polished redline memo. Clean
  off-white background, navy body, color-coded risk highlights.
  Four scenes: title settle, three-column header reveal, four
  clauses entering with [original | risk | counter], summary
  card outro.
- `prompts.txt` — five English LLM prompts: one per clause
  reviewed (1.1, 2.3, 5.2, 7.1) plus an overall summary pass.
- `brand.txt` — the Vault Legal palette + copy guardrails.
- `hyperframes.json`, `meta.json` — HyperFrames scaffold.

## The workflow it shows

You are in-house counsel at a Series-B startup. A vendor has sent
over their standard Master Services Agreement v2 and you have two
hours to redline it before the partner call. Without HTMLook this
is a PDF reader, a Google Doc, a Slack thread, and twenty open
tabs of past redlines. With HTMLook:

1. Open the workspace. **Left pane = `acme-msa-v2.pdf`** (the
   contract, scrollable, clause-numbered). **Right pane =
   `redline-memo.md`** (your running memo with risk notes and
   counter-language). The sidebar shows the clause table of
   contents.
2. Ask the LLM in the bottom terminal:
   *"Read clause 2.3 (Liability) on the left. Grade risk for a
   Series-B startup. If above LOW, draft counter-language."*
   The LLM cites the clause, names the risk, drafts the
   counter, and shows the full row inline.
3. Approve. The LLM calls `htmlook_apply_edit` on
   `redline-memo.md`. The right pane reloads with the new clause
   row appended in the three-column format
   (Original | Risk | Counter).
4. **Iterate clause by clause.** Move to clause 5.2 (IP). Then
   7.1 (Termination). Each pass is one focused redline, not a
   whole-document rewrite.

## Try it

Open this folder as a workspace in **HTMLook Pro**. Place a real
contract at `acme-msa-v2.pdf` and a memo at `redline-memo.md`,
then attach the HTMLook MCP to your LLM of choice (Claude, Codex,
Llama via Ollama, Gemini, GPT, etc.). Drop the `[1]` prompt from
`prompts.txt` into the terminal pane.

With the HTMLook MCP attached, the LLM will:

1. Call `htmlook_pane_pair` → see the contract PDF (left) and the
   memo (right).
2. Call `htmlook_active_file` → identify which clause is open on
   the left.
3. Call `htmlook_cite("left", "clause 2.3")` to anchor the
   exact clause being graded.
4. Call `htmlook_apply_edit` on `redline-memo.md` with a new
   row containing original quote, risk grade, and counter.
5. Hot-reload kicks in — the right pane re-renders the patched
   memo and you scan all rows at a glance.

## Why this matters

Contract review is exactly the kind of work that should not be
one-shot. Every clause is its own decision; the LLM can grade
fast but you must approve. HTMLook keeps the original quote and
your redline on screen at the same time, lets the LLM cite the
exact clause span being graded, and reloads the memo after each
counter-language splice — so by the time you reach the partner
call, every clause is already a reviewable row.

## Why HTMLook

The same four HTMLook moves you saw in `hf-claude` and
`dev-pr-docs` (dual-pane MCP, `cite`, `apply_edit`, auto-reload)
work here too — except the right pane is now a redline memo
instead of a docs file, and the artifact is a printed memo
instead of a video. **Same primitives, new craft.**
