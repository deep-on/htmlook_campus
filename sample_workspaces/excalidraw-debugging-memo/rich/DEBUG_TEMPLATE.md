# Debug Memo Template · Pebble

## Symptom
"~8% of Android push notifications never arrive · seen 2026-05-26"

## Hypothesis tree (verified top → bottom)

```
[ Symptom: 8% Android pushes lost ]
            |
   ┌────────┼─────────────────┐
   |        |                 |
[H1: FCM    [H2: payload     [H3: rate limiter
 token       exceeds 4KB      drops bursts
 expiry ✗]   limit ?]         silently ✓]
                                   |
                            [root: limiter sheds
                             on burst, no retry,
                             no metric]
                                   |
                            [fix: queue on limit
                             + backoff retry
                             + emit metric]
```

## Verification results
- H1 ✗ — tokens auto-refresh; logs show valid tokens at send time
- H2 ? — only 0.3% of payloads over 4KB — too small to explain 8% (on hold)
- H3 ✓ — limiter sheds requests on burst with no enqueue and no metric

## Fix
- PR-2041: enqueue on limit + retry with backoff + emit `push.dropped` metric
- Deployed: 2026-05-27
- Monitor: after 24h, close if drop rate is 0%

## Retrospective
- Prevent recurrence of this pattern (silent drop, no metric) → require a metric
  on every shedding path + add a load test.
