# slidev · Incident Postmortem (rich)

A complete blameless postmortem for **Brightwell Commerce** — a fictional
checkout 5xx outage (INC-2026-04-19). 14-slide narrative arc:

at-a-glance → impact → timeline → detection flow → 5-whys / root cause →
contributing factors → what went well → action items → lessons → close.

Uses Slidev `statement` / `section` / `two-cols` / `center` layouts, a
mermaid detection-flow diagram, and tables for the timeline and action
items. Edit `slides.md` and preview with the Slidev pane (md ↔ live HMR).

```bash
npx slidev slides.md
```

Swap Brightwell for your own incident — the section skeleton (impact →
timeline → root cause → factors → actions → lessons) is the reusable part.
