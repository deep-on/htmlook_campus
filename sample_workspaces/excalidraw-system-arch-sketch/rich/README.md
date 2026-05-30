<!-- Wave A · High Quality -->
# Excalidraw · System Architecture Sketch (rich)

Five fast, hand-drawn whiteboard sketches for **Cirrus** (a photo-sharing API).
The kind of box-and-arrow drawing you make in the first five minutes of a design
review — before reaching for a formal D2 or Mermaid diagram. Rough stroke,
1–2 accent colors, one page each.

## diagrams/
- `api-quick.excalidraw` — REST API + load balancer + Postgres primary/replica
  + Redis cache-aside.
- `data-pipeline.excalidraw` — upload-event ETL: Kafka ingest → Spark →
  BigQuery → dashboards, with a dead-letter queue.
- `event-flow.excalidraw` — Kafka topic `photo.uploaded` fanning out to
  thumbnailer / feed-fanout / moderation consumer groups.
- `auth-flow.excalidraw` — OAuth 2.1 + PKCE dance between user, app, auth
  server, and resource API.
- `k8s-quick.excalidraw` — namespace topology: ingress → Service → 3 api pods
  with an HPA.

Open any `.excalidraw` in the Excalidraw pane to redraw live during standup,
or export to SVG/PNG to drop into the meeting notes. See `SKETCH_PRINCIPLES.md`
for the keep-it-fast rules.
