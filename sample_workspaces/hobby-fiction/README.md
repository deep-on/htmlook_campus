# hobby-fiction — HTMLook + LLM for fiction outlines + scenes in one view

A 15-second polished "Chapter 1" teaser that demonstrates the
**hobby author** workflow: keep `outline.md` (plot + characters)
on the left pane and `chapter-1.md` (the actual finished scene)
on the right pane while asking an LLM to write the next scene
in the right voice, the right register, and with the right
pinned plot beats.

The fictional novella is **"화성의 마지막 편지" (The Last Letter
from Mars)** — a one-chapter SF mystery the writer is finishing
on a weekend.

## What you get

- `index.html` — the completed 15-s "Chapter 1" teaser. Warm
  parchment background with ink-slate text + rose accents.
  Four scenes: book-cover title → typewriter dialogue reveal
  → 3-character consistency chips → "Chapter 1 · 단편" wordmark.
- `prompts.txt` — five Korean LLM prompts: write the scene from
  outline, character consistency check, dialogue tighten, plot
  pin, end-of-chapter beat.
- `brand.txt` — the parchment palette + voice guardrails (no
  Hollywood beats, no exclamation pile-ups, slow careful pace).
- `hyperframes.json`, `meta.json` — HyperFrames scaffold.

## The workflow it shows

You are a hobby fiction writer working on a single chapter on
a Saturday afternoon. Without HTMLook this is one editor, a
forgotten outline doc in a different tab, and the LLM losing
track of which character said what. With HTMLook:

1. Open the workspace. **Left pane = `outline.md`** (plot
   beats, character cards, one-scene memo). **Right pane =
   `chapter-1.md`** (the prose, in progress). The sidebar
   shows the outline + chapter + a `characters/` folder.
2. Ask the LLM in the bottom terminal in Korean:
   *"Mars colony 마지막 통신 장면을 outline 의 plot point 그대로
   대화 + 묘사로 써 줘."* The LLM cites the relevant plot beat
   on the left, names the three characters, and starts writing
   into the right pane in the voice already established in the
   chapter so far.
3. Pause. Cite **Dr. Han** on the left character card. Ask the
   LLM to verify the new scene matches her speech pattern —
   formal, terse, never says her own first name. The LLM runs
   a consistency check and quotes the lines that drift.

## Try it

Open this folder as a workspace in **HTMLook Pro**. Place
`outline.md` and `chapter-1.md` and let the right pane render
the scene as it grows. Attach the HTMLook MCP to your LLM
(Claude, Codex, Llama via Ollama, Gemini, GPT). Drop the `[1]`
prompt from `prompts.txt` into the terminal pane.

With the HTMLook MCP attached, the LLM will:

1. Call `htmlook_pane_pair` → see the outline (left) and the
   chapter (right).
2. Call `htmlook_active_file` → identify which file is in focus.
3. Call `htmlook_cite("left", "L24-L38")` to pin the plot beat
   and the three character cards.
4. Call `htmlook_apply_edit` to insert the new scene at the
   end of `chapter-1.md`.
5. Hot-reload kicks in — the right pane re-renders the longer
   chapter and the writer reads the new scene in place.

## Why this matters

Outlines and finished prose almost never live in the same
window. The outline is "the plan", the chapter is "the work",
and the LLM rarely sees both at the same time. HTMLook puts
them side by side and lets the LLM trace which plot beat each
paragraph is delivering — so the next scene matches what was
promised on page one.

## Why HTMLook

The same four HTMLook moves you saw in `hf-claude` and
`dev-pr-docs` (dual-pane MCP, `cite`, `apply_edit`,
auto-reload) work here too — except the right pane is now a
chapter file instead of a docs file, and the artifact is a
finished 1500-word scene instead of a docs patch. **Same
primitives, new craft.**
