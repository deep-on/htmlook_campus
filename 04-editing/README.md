# Step 4 · Editing (Paint / Region / Element Pick)

<p align="center">
  <b>English</b> | <a href="README.ko.md">한국어</a> | <a href="README.ja.md">日本語</a> | <a href="README.de.md">Deutsch</a> | <a href="README.fr.md">Français</a> | <a href="README.es.md">Español</a> | <a href="README.pt.md">Português</a> | <a href="README.it.md">Italiano</a>
</p>

> Four ways to tell the LLM *which area on screen* you mean.
> ~ 5 min.

The single most distinctive part of HTMLook. When you say *"fix it here"*
to an AI, you can point at *here* directly — like a painter.

By the end of this step you'll have run the core cycle once yourself:
region drag → cite anchor → AI prompt.

## 4.1 · Four selection methods at a glance

| Method | How | Use for |
|---|---|---|
| **element pick** | click in the preview | a single DOM node (button / heading / paragraph) |
| **range select** | drag in the preview | a text range (sentence / phrase) |
| **region paint** ⭐ | ⌘Shift+R then drag a rectangle | a visual area (chart / illustration zone) |
| **outline pick** | click in the right-hand Outline panel | a heading-scoped section |

Video: [BASIC #6 · Pick what you see.](../videos/features/06-basic-06-html-4mode.mp4) (30 s)

## 4.2 · ⭐ Region cite — the keystone

The single most important move in Step 4. Your first *shared language*
with the AI.

1. Open an HTML or PDF file (e.g. [`../05-command/personas/01-hf-claude/landing.html`](../05-command/personas/01-hf-claude/landing.html)).
2. ⌘Shift+R enters region paint mode.
3. Drag a rectangle on the preview → the area highlights in magenta accent.
4. A cite anchor auto-attaches to the right-hand AI panel.
5. Tell the AI *"fix this — Apex's value (edge compute) in one line"*.

If MCP is connected, the LLM:
- pulls a PNG of the region via `htmlook_region_current_png` (vision
  models),
- secures the matching text anchor with `htmlook_active_file` +
  `htmlook_cite`,
- applies the patch with `htmlook_apply_edit`.

> Video: [BASIC #5 ⭐ · Drag. Tell the LLM.](../videos/features/05-basic-05-region-cite.mp4)
> (30 s · the AI entry point)

## 4.3 · Element pick

Hover over an element in the preview → outline appears → click → selected.
Toggle the mode with ⌘E.

The LLM reads the selected element's outerHTML via
`htmlook_selection_html`, patches, then commits with `htmlook_apply_edit`.

## 4.4 · Sentence-id (sentence-level inside long text / video)

Cite sentence #N directly in a long transcript or paper:

1. Open a video or long md.
2. Toggle *Sentence Map* in the right panel → sentences get N-numbered.
3. Click → cite anchor `sentence:5` attaches to the AI panel.

> Video: [ADV · Click sentence 5. Clip ships.](../videos/features/14-advanced-08-sentence-id.mp4)
> (30 s)

## 4.5 · Range select — just drag

The most common move. Drag text in the preview → both `selection_text`
and `selection_html` become available.

## ✅ Step 4 checkpoint

- You've entered region paint with ⌘Shift+R and drawn a rectangle.
- The drawn region attached as a cite anchor on the AI panel.
- You sent the AI a sentence and got a patch back (the response has a
  cite anchor *somewhere*).

All three? → [Step 5 · command (terminal / chat / apply)](../05-command/)

## Further reading

- [`../03-byom-setup/AI_GUIDE.md`](../03-byom-setup/AI_GUIDE.md) — the MCP
  tools (selection / region / element / cite).
- [`../05-command/personas/`](../05-command/personas/) — 26 persona
  walkthroughs (each persona favours a different region/element/sentence
  cite pattern).
