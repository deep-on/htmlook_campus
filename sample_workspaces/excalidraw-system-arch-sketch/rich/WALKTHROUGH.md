# System Architecture Sketch Walkthrough · 30-min Walkthrough

> **Wave A · High Quality** — marketing / demo asset. Suitable for a live demo
> recording.

Open the five **Cirrus** sketches in turn to show the "five-minute whiteboard"
flow.

## 1. The five-minute sketch, done right
- The first tool you reach for in a meeting — before building a formal diagram
  (D2/Mermaid).
- Five patterns in diagrams/: api-quick, data-pipeline, event-flow, auth-flow,
  k8s-quick.
- Rough stroke + 1-2 accent colors only — the "hand-drawn" feel is intentional.

## 2. Real use cases
- During standup, sketch a system change on the spot (open api-quick, add one
  cache box).
- Within five minutes of starting a design review, draw enough to kick off the
  discussion (add a consumer group to event-flow).
- Once the team agrees, move on to a formal diagram.

## 3. Demo flow (recording)
- api-quick → "what if we add a read replica here?" and add it on the spot.
- event-flow → draw one new consumer-group box + arrow to explain fanout.
- Export to SVG, paste it into the notes, and wrap up.
