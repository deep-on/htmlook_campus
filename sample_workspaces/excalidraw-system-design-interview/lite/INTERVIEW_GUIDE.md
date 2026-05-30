# Interview Guide (self-review + 35-min mock)

A 5-step sketch for each problem:
1. Clarify requirements (5 min)
2. Capacity estimation (5 min)
3. API + data model (5 min)
4. High-level architecture (10 min)
5. Scaling + edge cases (10 min)

## URL Shortener — `diagrams/url-shortener.excalidraw`
- QPS estimate: 100M URL/day = 1,200 QPS write, 12,000 QPS read (10:1)
- DB: PostgreSQL primary + Redis counter (autoincrement)
- ID generation: base62(counter) — 7 chars covers 3.5T URLs
- Redirect latency target: <50ms p99

## Extra pattern notes
- CAP: state where you traded off
- Cache invalidation: write-through vs write-behind
- Backpressure: client throttle vs queue
