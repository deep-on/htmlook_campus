# Excalidraw · Debugging Memo Tree (rich)

A visual debugging trace for **Pebble** (a push-notification service): the
symptom *"~8% of Android pushes never arrive"* branches into three hypotheses,
each gets a verdict (ruled out / inconclusive / confirmed) and findings, and
the confirmed branch flows down to a root cause and the fix PR. 37 elements.

The flow reads top to bottom: **symptom → hypotheses → verdicts → findings →
root cause → fix**. Arrows show how the investigation narrowed to the rate
limiter silently dropping bursts.

Open `debug-tree.excalidraw` in the Excalidraw pane to extend the tree as you
investigate, or export to SVG/PNG to attach to the incident write-up. See
`DEBUG_TEMPLATE.md` for the reusable text version of this memo.
