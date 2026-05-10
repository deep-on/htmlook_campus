# product-prd — HTMLook + LLM for parallel PRD ↔ wireframe ↔ ticket updates

A 15-second polished spec page that demonstrates the **senior product manager** workflow: keep the PRD `.md` on the left pane and the clickable wireframe HTML mockup on the right pane, then ask an LLM to cite a PRD section, suggest UX changes, apply edits to the wireframe HTML, and draft the matching engineering ticket. The right pane reloads in sync with the PRD edit; a ticket draft appears in the same loop.

The fictional product is **Lattice OS** — a SaaS workspace whose PRD `v0.3` is being lifted to `v0.4` ahead of the May 28 launch.

## What you get

- `index.html` — the completed 15-s polished spec page. Clean tech-white background, electric-blue and mint-green accents. Four scenes: product wordmark with version pill, three [requirement | wireframe icon | linked ticket] rows staggered in, "Ready for Eng review" stamp with PM initials, doc footer with PRD version and review date.
- `prompts.txt` — five English LLM prompts: one for the main "PRD section cite + parallel update" move, one for "draft a wireframe change", plus three follow-ups (sync ticket, run accessibility pass, reconcile conflict).
- `brand.txt` — the Lattice OS palette + product-spec copy guardrails.
- `hyperframes.json`, `meta.json` — HyperFrames scaffold.

## The workflow it shows

You are a senior PM closing a PRD before Eng review. Without HTMLook this is three windows: a Notion-flavoured spec doc, a Figma-style wireframe, and a Linear / Jira ticket. Edits drift between them every time someone touches one. With HTMLook:

1. Open the workspace. **Left pane = `prd.md`** (a structured PRD with goals, scope, acceptance criteria). **Right pane = `wireframe.html`** (a clickable rough sketch — buttons, fields, layout). The sidebar lists the PRD version, scope, and the sister `tickets.md` draft file.
2. Ask the LLM in the bottom terminal: *"Section 3.2 says we need saved filters in run history. Reflect this in the wireframe and draft the matching Linear ticket."* The LLM calls `htmlook_cite("left", "prd.md#3.2")`, edits the wireframe HTML to add a filter chip-rail, and drafts `PROD-1234` in `tickets.md` — all in one round trip.
3. The right pane reloads with the new wireframe component. The sidebar shows the new ticket. PRD `v0.3` becomes `v0.4`.

## Try it

Open this folder as a workspace in **HTMLook Pro**. Drop a real `prd.md` plus a hand-rough `wireframe.html` and a `tickets.md` file, then attach the HTMLook MCP to your LLM of choice (Claude, Codex, Llama via Ollama, Gemini, GPT). Drop the `[1]` prompt from `prompts.txt` into the terminal pane.

With the HTMLook MCP attached, the LLM will:

1. Call `htmlook_pane_pair` → see the PRD on the left and the wireframe on the right.
2. Call `htmlook_cite("left", "prd.md#3.2")` to anchor the requirement section.
3. Call `htmlook_apply_edit` on `wireframe.html` to add the filter chip-rail component.
4. Call `htmlook_apply_edit` on `tickets.md` in parallel to draft `PROD-1234` with scope, acceptance criteria, and a back-reference to the PRD section.
5. Hot-reload kicks in — the right pane re-renders the wireframe. PRD bumps to `v0.4`.

## Why this matters

PRDs, wireframes, and tickets always drift. The PM updates one, forgets the other two, and Eng review surfaces the conflict the day before launch. HTMLook keeps the three artefacts on one screen and lets the LLM execute the parallel update — PRD section → wireframe change → ticket draft — in a single loop, so the three never disagree.

## Why HTMLook

The same four HTMLook moves you saw in `dev-pr-docs` (dual-pane MCP, `cite`, `apply_edit`, auto-reload) work here too — except the right pane is now a clickable wireframe instead of a docs file, and the artifact is a synchronised PRD + wireframe + ticket triple instead of a docs patch. **Same primitives, new craft.**
