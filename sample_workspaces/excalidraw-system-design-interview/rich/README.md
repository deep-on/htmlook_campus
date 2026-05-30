<!-- Wave A · High Quality -->
# Excalidraw · System Design Interview (rich)

Two polished whiteboards for the most common system-design-interview warmups,
drawn the way you'd build them live on a call.

## diagrams/
- `url-shortener.excalidraw` — client → load balancer → API → Postgres (+ read
  replicas) with a Redis counter for ID generation and a Redis cache for the
  redirect read path, plus a click-analytics queue. Includes a capacity and
  trade-off panel (1.2k write / 12k read QPS, base62 7-char keyspace, CAP
  choice). 31 elements.
- `news-feed.excalidraw` — hybrid fanout: push for normal users, pull at read
  time for celebrities, with a feed cache (Redis sorted set), a fanout worker,
  the social graph, and a Cassandra post store. Includes a trade-off panel.
  31 elements.

See `INTERVIEW_GUIDE.md` for the 5-step approach and `WALKTHROUGH.md` for the
demo flow. Open either `.excalidraw` in the Excalidraw pane to draw along with
the candidate, or export to SVG/PNG to share after the session.
