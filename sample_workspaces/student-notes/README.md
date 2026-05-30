# student-notes — HTMLook + LLM for parallel lecture-cite ↔ notes ↔ flashcards

A 15-second polished study-page that demonstrates the **undergrad / high-school study-from-lecture** workflow: keep the lecture slide markdown on the left pane and the personal study notebook on the right pane, then ask an LLM to cite a slide, write a 3-bullet summary plus one worked example into `my-notes.md`, and in parallel append 4 Q/A flashcards into `flashcards.md` — both files updated in the same round trip. The right pane reloads with the new notes, and a flashcard deck appears.

The fictional course is **ML 301 — Deep Learning**, Lecture 5 (Self-Attention), nine days before the midterm.

## What you get

- `index.html` — the completed 15-s polished study page. Notebook-beige background, ink-slate text, highlighter yellow + purple highlight accents. Four scenes: "Lecture 5 — Self-Attention" header → 3-bullet summary stagger → flashcard Q→A flip 4 cards → "Notes · Week 5" wordmark.
- `prompts.txt` — five English LLM prompts: one for the main "cite slide + multi-target write" move, one for "refine a flashcard", plus three follow-ups (sweep prerequisites, exam-prep checklist, verbatim cite).
- `brand.txt` — the Notes · Week 5 palette + study-notebook copy guardrails.
- `hyperframes.json`, `meta.json` — HyperFrames scaffold.

## The workflow it shows

You are an undergrad studying for a midterm. Without HTMLook this is a Notion notebook on one screen, the slide PDF on another, and Anki in a third app. Edits don't carry across. With HTMLook:

1. Open the workspace. **Left pane = `lecture-slides.md`** (the lecturer's slides exported as markdown; slide 5 defines self-attention). **Right pane = `my-notes.md`** (your blank Week 5 page). The sidebar lists `flashcards.md` and `exam-prep.md`.
2. Ask the LLM in the bottom terminal: *"Cite slide 5. Write a 3-bullet summary plus a worked example into my-notes.md, and at the same time add four Q/A flashcards to flashcards.md."* The LLM calls `htmlook_cite("left", "slide-5")`, then `htmlook_apply_edit` on **both** `my-notes.md` and `flashcards.md` in one round trip.
3. The right pane reloads with the summary, the worked example, and two exam-style questions. The sidebar shows `flashcards.md` newly populated with four Q→A cards.

## Try it

Open this folder as a workspace in **HTMLook Pro**. Drop a real lecture export at `lecture-slides.md` and a blank `my-notes.md` plus a `flashcards.md` file, then attach the HTMLook MCP to your LLM of choice (Claude, Codex, Llama via Ollama, Gemini, GPT). Drop the `[1]` prompt from `prompts.txt` into the terminal pane.

With the HTMLook MCP attached, the LLM will:

1. Call `htmlook_pane_pair` → see the slides on the left and your notebook on the right.
2. Call `htmlook_cite("left", "slide-5")` to anchor the self-attention slide.
3. Call `htmlook_apply_edit` on `my-notes.md` to append the summary, example, and exam questions.
4. Call `htmlook_apply_edit` on `flashcards.md` in parallel to append four Q/A cards.
5. Hot-reload kicks in — the right pane re-renders the notebook page. The sidebar's flashcard count goes from 0 → 4.

## Why this matters

Studying drifts: you read a slide, write half a note, forget to make a flashcard, and the slide-fact never makes it to the exam. HTMLook keeps the lecture and the notebook on one screen and lets the LLM execute the parallel update — slide cite → summary → flashcards — in a single loop, so the three never disagree.

## Why HTMLook

The same four HTMLook moves you saw in `dev-pr-docs` and `product-prd` (dual-pane MCP, `cite`, `apply_edit`, auto-reload) work here too — except the right pane is now a study notebook instead of a docs file or wireframe, and the artifact is a synchronised notes + flashcards pair instead of a docs patch or a PRD/wireframe/ticket triple. **Same primitives, new craft.**
