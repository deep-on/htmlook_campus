# Debug Memo Template · Pebble

## Symptom
"~8% of Android push notifications never arrive"

## Hypothesis tree (verified top → bottom)

```
[ Symptom: 8% pushes lost ]
       |
   ┌───┼───────────────┐
   |   |               |
[H1: token   [H2: payload   [H3: rate limiter
 expiry ✗]    too big ?]     drops bursts ✓]
                                |
                         [why: limiter sheds
                          on burst, no retry]
                                |
                         [fix: queue + backoff
                          + emit metric]
```

## Verification results
- H1 ✗ — tokens auto-refresh; valid at send time
- H2 ? — only 0.3% of payloads over the limit (on hold)
- H3 ✓ — limiter sheds on burst with no enqueue and no metric

## Fix
- PR-2041: enqueue on limit + retry with backoff + emit `push.dropped` metric
- Deployed: 2026-05-27
- Monitor: close if drop rate is 0% after 24h
