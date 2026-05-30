---
theme: default
title: INC-2026-04-19 Postmortem
class: text-center
---

# INC-2026-04-19 · P0 Postmortem

42 minutes outage · 1.2 M req lost · ARR impact ~$8 k

Engineering · 2026-04-26

---
layout: section
---

# What happened

---

## Impact

- **Customers**: ~30% of API requests returned 5xx for 42 minutes
- **Revenue**: ~$8k ARR impact (tracked via failed checkout)
- **NPS**: -3 points week-over-week
- **Compliance**: 2 enterprise SLA breaches

---

## Timeline

| time  | event |
|-------|-------|
| 14:02 | Datadog alert fires (error rate >5%) |
| 14:05 | Oncall pages, acks |
| 14:09 | Incident channel opened, 4 engineers join |
| 14:12 | Hypothesis: db connection storm |
| 14:18 | Failover to replica · 5 min replication lag |
| 14:32 | Replica catches up, traffic gradually restored |
| 14:44 | Full recovery confirmed |

---
layout: two-cols
---

# 5 Whys

::default::

1. Why 5xx? **DB connections exhausted**
2. Why exhausted? **Pool size 100 hit**
3. Why pool ceiling? **Migration spawned 3× normal queries**
4. Why 3×? **Backfill ran during prod traffic peak**
5. Why during peak? **Migration playbook didn't gate by traffic**

::right::

# Root cause

**Migration playbook silent on traffic awareness.**

Documentation gap, not code gap.

---

## Action items

| # | item | owner | due |
|---|------|-------|-----|
| 1 | Add pool monitor + alert at 80% | SRE · Sue | 2026-05-03 |
| 2 | Update migration playbook · traffic gating | Eng · Joe | 2026-05-10 |
| 3 | Pool autoscaling spike | Backend · Mia | 2026-05-17 |
| 4 | Add chaos test · pool exhaustion | SRE · Sue | 2026-06-01 |

---
layout: center
---

# Lessons

- **Documentation matters** — code prevented the bug, docs didn't.
- **Failover worked** — 5min replication lag within RPO target.
- **Communication** — incident channel ramp-up was 7 min, target <5 min.
