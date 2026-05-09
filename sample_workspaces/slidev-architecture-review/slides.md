---
theme: default
title: ADR-042 · Kafka vs SQS
class: text-center
---

# ADR-042

## Choose between Kafka and SQS for our event bus

Engineering review · 2026-05-08

---

## Context

Order pipeline currently uses Kafka. Volume: ~50 RPS sustained, 200 RPS peak. Pain points: ops cost ($1.8k/mo), expertise concentration (2 engineers).

We're scaling to mobile (10× volume) — re-evaluating.

---
layout: two-cols
---

# Options

::default::

**Option A: Stay on Kafka**
- + proven for our patterns
- + 100k+ msg/s ceiling
- − $$ ops + expertise
- − complex to scale

::right::

**Option B: Migrate to SQS** ✓
- + managed (no ops)
- + scales to org needs
- − DLQ ergonomics
- − 256 KB msg cap

---

## Decision criteria

| dim          | Kafka  | SQS  | Weight |
|--------------|--------|------|--------|
| Throughput   | 100k/s | 3k/s | 0.2    |
| Ops cost     | $$$    | $    | 0.3    |
| Engineer time| medium | low  | 0.3    |
| Reliability  | high   | high | 0.2    |

Weighted score: SQS 4.2 vs Kafka 3.1.

---

## Decision · SQS

Migrate over 6 weeks. Maintain Kafka for analytics.dispatched until Q3.

---

## Consequences

**Positive**
- Save $1.5k/mo ops + 30% engineer time
- New engineers ramp faster

**Negative**
- DLQ topology harder (need Lambda for advanced retry)
- 256 KB cap requires payload chunking for 0.4% of messages

**Mitigation**
- Build wrapper SDK for SQS w/ retry topology
- Fallback to S3 + pointer for oversize messages

---
layout: center
---

# Approved · 2026-05-08

Owner: Platform · Implementation Q3
