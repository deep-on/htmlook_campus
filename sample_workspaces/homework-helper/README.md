# homework-helper — HTMLook + LLM for cited problem → step-by-step solution + practice set

A 15-second polished homework page that demonstrates the **middle-school student doing math homework** workflow: keep the problem set on the left pane and the personal solution notebook on the right pane, then ask an LLM to cite a problem, walk through it step by step (statement → formula → substitution → answer), and append three similar practice problems — all in one round trip. The right pane reloads with the worked solution and the practice set.

The fictional class is **8th-grade geometry**, Homework #3, three Pythagorean Theorem problems due tomorrow.

## What you get

- `index.html` — the completed 15-s polished homework page. Paper-white background with mint margin tint, school-green and math-teal accents, highlighter-yellow on the key step. Four scenes: "문제 1" header with the right-triangle givens → 3 solution steps stagger (직각삼각형 ABC · 5² + 12² = c² · c = 13) → three similar practice problems stagger → "Pythagoras · 풀이 노트" wordmark.
- `prompts.txt` — five English LLM prompts: one for the main "cite problem + step-by-step" move, one for "add three similar practice problems", plus three follow-ups (verbatim cite, trickiest-problem sweep, check-my-attempt).
- `brand.txt` — the Pythagoras · 풀이 노트 palette + classroom-paper copy guardrails.
- `hyperframes.json`, `meta.json` — HyperFrames scaffold.

## The workflow it shows

You are a middle-school student stuck on math homework. Without HTMLook this is the worksheet PDF on one screen, a chat tab on another, and a paper notebook on the desk. Steps don't carry across, and the "show your work" part gets lost. With HTMLook:

1. Open the workspace. **Left pane = `homework.md`** (3 Pythagorean theorem problems with the givens for each). **Right pane = `solution.md`** (your blank solution page). The sidebar lists `concepts.md` (Pythagorean theorem reminder).
2. Ask the LLM in the bottom terminal: *"Cite problem 1. Walk me through the solution step by step, add a one-line concept reminder, and then give me three similar practice problems."* The LLM calls `htmlook_cite("left", "문제-1")`, then `htmlook_apply_edit` on `solution.md` with the steps + practice set in one round trip.
3. The right pane reloads with: the cited problem, three solution steps (formula → substitution → answer), the concept reminder, and three numbered practice problems (no solutions, so you can try them yourself).

## Try it

Open this folder as a workspace in **HTMLook Pro**. Drop a real `homework.md` and a blank `solution.md`, then attach the HTMLook MCP to your LLM of choice (Claude, Codex, Llama via Ollama, Gemini, GPT). Drop the `[1]` prompt from `prompts.txt` into the terminal pane.

With the HTMLook MCP attached, the LLM will:

1. Call `htmlook_pane_pair` → see the homework on the left and your solution page on the right.
2. Call `htmlook_cite("left", "문제-1")` to anchor problem 1.
3. Call `htmlook_apply_edit` on `solution.md` to append the step-by-step solution + concept reminder.
4. Call `htmlook_apply_edit` on `solution.md` again (or in the same diff) to append the practice set "비슷한 문제 3개".
5. Hot-reload kicks in — the right pane re-renders the page with all four sections in place.

## Why this matters

Homework help drifts: a tutor types an answer, you copy half of it, and the "show-your-work" steps disappear. HTMLook keeps the problem and the solution on one screen, and lets the LLM execute the cite → step-by-step → practice-set update in a single loop, so you end up with a notebook page you can actually study from.

## Why HTMLook

The same four HTMLook moves you saw in `dev-pr-docs`, `product-prd`, and `student-notes` (dual-pane MCP, `cite`, `apply_edit`, auto-reload) work here too — except the right pane is now a homework solution page, and the artifact is a step-by-step solution + a similar-problem practice set instead of a docs patch or a flashcard deck. **Same primitives, new craft.**
