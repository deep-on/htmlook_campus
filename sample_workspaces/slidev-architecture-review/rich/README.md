# slidev · Architecture Review / ADR (rich)

A complete ADR-style architecture review for **Tideglass** — a fictional
fleet-telemetry platform deciding how to scale its read path (ADR-073).
14-slide narrative arc:

context → current pain → forces → proposed change → alternatives →
decision matrix → decision → consequences → mitigations/rollout →
open questions → accepted.

Uses Slidev `statement` / `two-cols` / `center` layouts, four mermaid
diagrams (current state, proposed topology, rollout phases), and weighted
decision-matrix tables. Edit `slides.md` and preview with the Slidev pane
(md ↔ live HMR).

```bash
npx slidev slides.md
```

Swap Tideglass for your own system — the ADR skeleton (context → options →
matrix → decision → consequences → mitigations) is the reusable part.
