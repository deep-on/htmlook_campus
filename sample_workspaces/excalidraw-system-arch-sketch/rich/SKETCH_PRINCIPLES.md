# Five-Minute Sketch Principles · Cirrus

A fast whiteboard sketch — the step before building a formal diagram
(D2/Mermaid).

## Do
- It should be drawable in five minutes (if not, it's too detailed).
- Boxes + arrows only — no UML/BPMN.
- Fit it on a single page.
- Use it as the input for the next (formal) step.

## Don't
- Too many colors — keep to 1-2 accents (cache = yellow, db = blue, roughly).
- Icon libraries — the hand-drawn (rough stroke) look is the point.
- Excessive layers / groups — keep it flat.

## Example collection (diagrams/)
- `api-quick.excalidraw` — REST API + Postgres + Redis cache
- `data-pipeline.excalidraw` — Kafka → Spark → BigQuery ETL flow
- `event-flow.excalidraw` — Kafka producer/consumer fanout
- `auth-flow.excalidraw` — OAuth 2.1 + PKCE dance
- `k8s-quick.excalidraw` — ingress → Service → pods + HPA
