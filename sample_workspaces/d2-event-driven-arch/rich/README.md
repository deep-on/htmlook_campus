# d2 · Event-Driven Architecture (rich)

The order platform for the fictional **Tidewell Commerce** business,
modelled as an event-driven system: producers publish through an
outbox + Debezium CDC, a 3-broker Kafka cluster carries the topics, a
SAGA orchestrator drives the order/payment/shipping flow, and a
compensation path unwinds failures. Includes a schema registry for
contract governance, an append-only event store for durable replay,
a dead-letter queue with manual redrive, and downstream projections
(fulfillment read-model, analytics, notifications).

Shapes map to roles: hexagons for services and the orchestrator,
cylinders for stores, queues for topics and the DLQ, a cloud for
ingress. Dashed edges mark out-of-band flows — CDC tailing, schema
register/fetch, durable archive/replay, compensation, and DLQ redrive.

Preview the diagram with the D2 pane (`.d2` ↔ live SVG), or:

```bash
d2 --layout elk architecture.d2 architecture.svg
```
