# Excalidraw · Refactor Plan Board (rich)

A refactor plan for **Tide** (an e-commerce checkout): breaking a single
checkout monolith into independently deployable services, visualized
before/after and as a 4-week migration swimlane.

## diagrams/
- `before-after.excalidraw` — left: one `checkout-monolith` bundling cart /
  pricing / payments / inventory / tax / notifications. Right: the same
  capabilities extracted into services behind an API gateway, with an event
  bus. A "strangler-fig" arrow marks the transition. 43 elements.
- `migration-timeline.excalidraw` — a 4-week swimlane (Backend / Data / Ops ×
  W1–W4) showing carve-out order, dual-write data moves, and canary/cutover
  steps. 40 elements.

See `REFACTOR_PLAN.md` for the written plan. Open either `.excalidraw` in the
Excalidraw pane to adjust scope live, or export to SVG/PNG for the design doc.
Service boxes are grouped, so you can rearrange the target topology freely.
