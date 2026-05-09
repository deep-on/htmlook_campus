# Debug Memo Template

## 증상
"API returns 401 randomly · ~5% of authenticated requests"

## 가설 트리 (위 → 아래로 검증)

```
[ Symptom: 401 ~5% ]
       |
   ┌───┼───────────────┐
   |   |               |
[H1: token   [H2: scope    [H3: cache
 expired ✗]   mismatch ?]    desync ✓]
                                |
                         [why: redis evicted
                          on rebalance]
                                |
                         [fix: pin TTL
                          + warm read]
```

## 검증 결과
- H1 ✗ — token 발급 1분 전, 24h TTL
- H2 ? — 일부 endpoint 만 — 다음 단계 검증 (보류)
- H3 ✓ — `redis-cli info | grep evicted` 비정상

## 수정
- PR-1428: TTL pin + warm read on cache miss
- 배포: 2026-05-08
- 모니터: 24h 후 재발 안 하면 close

## 회고
- 이 패턴 (cache desync after rebalance) 다시 일어나지 않으려면 → chaos test 추가
