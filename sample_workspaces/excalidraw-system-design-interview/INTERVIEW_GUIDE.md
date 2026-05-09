# 인터뷰 가이드 (자기 검토 + 35분 모의)

각 문제마다 5단계 sketch:
1. 요구사항 명확화 (5min)
2. capacity estimation (5min)
3. API + data model (5min)
4. high-level architecture (10min)
5. scaling + edge cases (10min)

## 1. URL Shortener — `diagrams/url-shortener.excalidraw`
- QPS 추정: 100M URL/day = 1,200 QPS write, 12,000 QPS read (10:1)
- DB: PostgreSQL primary + Redis counter (autoincrement)
- ID 생성: base62(counter) — 7 chars covers 3.5T URLs
- 리다이렉트 latency 목표: <50ms p99

## 2. Chat (Slack-like) — `diagrams/chat.excalidraw`
- WebSocket 영구 연결 + 메시지 fanout
- 메시지 store: Cassandra wide-row (channel_id, ts)
- Presence: Redis pub/sub
- 서버 capacity: 10k concurrent / box

## 3. News Feed (Twitter-like) — `diagrams/news-feed.excalidraw`
- Push (precompute) vs Pull (compute on read) vs Hybrid
- 셀럽 (>1M followers) = pull, 일반 = push
- Feed cache: Redis sorted set, top 1000

## 4. Rate Limiter — `diagrams/rate-limiter.excalidraw`
- Token bucket vs Leaky bucket vs Sliding window
- Distributed: Redis with Lua atomic ops
- Strategy: per-user, per-endpoint, per-IP

## 5. Distributed Search (Elasticsearch-like) — `diagrams/search.excalidraw`
- Inverted index, sharding by document
- Query coordinator → shards → merge top-K
- Indexing: bulk + near-real-time

## 추가 패턴 메모
- CAP: 어디 trade-off 했는지 명시
- 캐시 invalidation: write-through vs write-behind
- Backpressure: 클라이언트 throttle vs queue
