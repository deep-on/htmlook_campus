# Interview Guide (self-review + 35-min mock)

A 5-step sketch for each problem:
1. Clarify requirements (5 min)
2. Capacity estimation (5 min)
3. API + data model (5 min)
4. High-level architecture (10 min)
5. Scaling + edge cases (10 min)

## 1. URL Shortener — `diagrams/url-shortener.excalidraw`
- QPS estimate: 100M URL/day = 1,200 QPS write, 12,000 QPS read (10:1)
- DB: PostgreSQL primary + read replicas; Redis counter (INCR) for ID gen
- ID generation: base62(counter) — 7 chars covers 3.5T URLs
- Redirect latency target: <50ms p99 (cache hit → 301)
- CAP: redirects favor availability, shortening favors consistency

## 2. News Feed (Twitter-like) — `diagrams/news-feed.excalidraw`
- Push (precompute) vs Pull (compute on read) vs Hybrid
- Celebrities (>1M followers) = pull, normal users = push
- Feed cache: Redis sorted set, top 1000 per user
- Post store: Cassandra wide-row; fanout worker writes follower feeds
- Celebrity posts merge at read time (avoid the fanout storm)

## Extra pattern notes (cover verbally)
- Chat: persistent WebSocket connection + Cassandra message store + Redis presence
- Rate limiter: token bucket, Redis + Lua atomic, per-user/endpoint/IP
- Search: inverted index, shard by document, coordinator → shards → merge top-K
- Always call out CAP / cache invalidation / backpressure trade-offs
