# kid-coding — HTMLook + LLM for first Python turtle in the same view

A 15-second polished "My First Code" teaser that demonstrates the
**young coder** workflow: keep `star.py` (a 15-line turtle program)
on the left pane and the rendered turtle drawing on the right pane
while asking an LLM in friendly Korean to explain a `for` loop and
suggest the next challenge.

The fictional learner is **Minji (5학년)** — drawing her first star.

## What you get

- `index.html` — the completed 15-s "My First Code" teaser. Cream
  background with cyan + magenta + 노랑 accents. Four scenes:
  big "내 첫 코드" header → 5-step star draw → 4 stagger color
  stars → "다음 챌린지: 무지개별!" wordmark.
- `prompts.txt` — five Korean LLM prompts for kids: explain code,
  change angle, change color, debug, next challenge.
- `brand.txt` — the kid-coding palette + copy guardrails (kind,
  short, no jargon).
- `hyperframes.json`, `meta.json` — HyperFrames scaffold.

## The workflow it shows

You are an elementary-school student writing your first Python
program. Without HTMLook this is one terminal that prints a star
and zero feedback. With HTMLook:

1. Open the workspace. **Left pane = `star.py`** (15 lines).
   **Right pane = the rendered turtle drawing** (the star). The
   sidebar shows `star.py` and an `assets/` folder for the result.
2. Ask the LLM in the bottom terminal in Korean:
   *"이 부분이 뭐야?"* — point at the `for i in range(5)` line.
   The LLM replies in friendly Korean, the right pane refreshes,
   and the first star appears one stroke at a time.
3. Try the next challenge. Change `angle` from `144` to `72`.
   The right pane reloads — the star morphs into a 10-pointed
   variant. Try four different fill colors and stagger them.

## Try it

Open this folder as a workspace in **HTMLook Pro**. Place
`star.py` and let the right pane render the live turtle output.
Attach the HTMLook MCP to your LLM (Claude, Codex, Llama via
Ollama, Gemini, GPT). Drop the `[1]` prompt from `prompts.txt`
into the terminal pane.

With the HTMLook MCP attached, the LLM will:

1. Call `htmlook_pane_pair` → see the code (left) and the
   rendered turtle (right).
2. Call `htmlook_active_file` → identify `star.py`.
3. Call `htmlook_cite("left", "L7-L11")` to anchor the
   `for` loop the kid is asking about.
4. Reply in friendly Korean, no jargon — one sentence per
   line of code.
5. Call `htmlook_apply_edit` to swap `angle = 144` for
   `angle = 72` and hot-reload the right pane.

## Why this matters

A first Python program with `print("hello")` is invisible. A
first Python program that draws a star **and** has a kind tutor
explaining each line **and** suggests "now change one number"
is the moment a kid keeps coding. HTMLook turns one terminal
into code + result + tutor on screen at the same time.

## Why HTMLook

The same four HTMLook moves you saw in `hf-claude` and
`dev-pr-docs` (dual-pane MCP, `cite`, `apply_edit`,
auto-reload) work here too — except the right pane is now a
turtle drawing instead of a docs file, and the artifact is a
new color palette instead of a docs patch. **Same primitives,
new craft.**
