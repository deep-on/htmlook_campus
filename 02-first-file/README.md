# Step 2 · First file (HTML / Markdown / PDF / video)

<p align="center">
  <b>English</b> | <a href="README.ko.md">한국어</a> | <a href="README.ja.md">日本語</a> | <a href="README.de.md">Deutsch</a> | <a href="README.fr.md">Français</a> | <a href="README.es.md">Español</a> | <a href="README.pt.md">Português</a> | <a href="README.it.md">Italiano</a>
</p>

> Learn the heart of HTMLook's *viewer*. The part that's already worthwhile
> without AI / MCP.
> ~ 5 min.

By the end of this step: you know how to read each of the four file kinds
(md / html / pdf / video) and how to navigate them with split view,
preview, and outline.

## 2.1 · Markdown live edit

1. Double-click any `.md` in the sidebar (e.g. [`../05-command/personas/03-dev-pr-docs/docs.md`](../05-command/personas/03-dev-pr-docs/docs.md)).
2. Toggle split view with ⌘\\ or *View → Split*.
3. Source on the left, preview on the right. Type on the left, the right
   refreshes live.

> Video: [BASIC #3 · Type left. See right. Live.](../videos/features/03-basic-03-md-live-edit.mp4) (30 s)

## 2.2 · HTML — click an element to edit it

1. Double-click an `.html` (e.g. [`../05-command/personas/01-hf-claude/landing.html`](../05-command/personas/01-hf-claude/landing.html)).
2. Default mode is preview. In split view, click an element directly →
   a text editor pops up.
3. Two-way sync — changes in preview land in source instantly.

> Video: [BASIC #4 · Click anything. Edit it.](../videos/features/04-basic-04-html-split.mp4) (30 s)

## 2.3 · HTML — four selection modes

In the same HTML file, ⌘E cycles through the four selection modes:

| Mode | What it picks |
|---|---|
| element | a single DOM node |
| range | a text range |
| region | a rectangular paint |
| outline | the heading tree |

Video: [BASIC #6 · Pick what you see.](../videos/features/06-basic-06-html-4mode.mp4) (30 s)

Whatever each mode picks becomes the cite-anchor entry point in
[Step 4 · editing](../04-editing/).

## 2.4 · PDF — pages + text layer

1. Double-click any `.pdf` (e.g. [`../05-command/personas/05-domain-battery/vendor.pdf`](../05-command/personas/05-domain-battery/vendor.pdf)).
2. Left-hand thumbnail navigator + right-hand page canvas + selectable
   text layer.
3. Drag-select a region → region cite (used in Step 4).

## 2.5 · Video — frame thumbnails + outline

1. Double-click any mp4 (e.g. [`../videos/features/01-basic-01-drop-open.mp4`](../videos/features/01-basic-01-drop-open.mp4)).
2. The video viewer shows a timeline with thumbnail previews.
3. ⌘Shift+T or hover gives you a 1-second frame preview (no scrubbing).

> Video: [ADV · Frame check. No scrub.](../videos/features/15-advanced-09-thumbnail.mp4) (30 s, advanced category)

## 2.6 · Outline — navigating a long document

The heading structure of any long md / html / PDF → Outline tab in the
right panel. Click a heading to jump there.

> Video: [ADV · Click §3.2. You're there.](../videos/features/16-advanced-10-outline.mp4) (30 s)

## 2.7 · Split view / multi-pane (⌘1 / ⌘2 / ⌘3 / ⌘J)

| Shortcut | Effect |
|---|---|
| ⌘1 | Preview only |
| ⌘2 | Source only |
| ⌘3 | Split (preview + source) |
| ⌘J | Toggle terminal panel |

Video: [ADV · Two keys. Three views.](../videos/features/10-advanced-04-multi-pane.mp4)
(30 s — the narration's *"Two keys"* was ⌘D + ⌘J in the original cut and
was corrected to ⌘1/⌘2/⌘3 + ⌘J for v1.0. Full lineage in
[`../08-extend/PRODUCTION.md`](../08-extend/PRODUCTION.md), in the *fixed
false claims* table.)

## ✅ Step 2 checkpoint

- You've opened one of each: md / html / pdf / video in split view.
- You've felt the difference between the four HTML modes (element / range
  / region / outline) by clicking directly.
- ⌘1 / ⌘2 / ⌘3 / ⌘J for layout toggling is muscle memory.

All three? → [Step 3 · BYOM setup](../03-byom-setup/) — pick one vendor
and register a key.
