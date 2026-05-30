---
title: RFC 0001 · Event schema versioning
description: A versioning scheme for the events on Northwind's internal event bus.
---

- **Status:** Accepted
- **Author:** Priya Nadar
- **Created:** 2026-03-12
- **Tracking issue:** ENG-4471

This RFC follows the [RFC 0000 template](/rfcs/0000-template/). For the workflow
that moved it to *Accepted*, see the [RFC process](/).

## Summary

Add a required `schemaVersion` integer to every event published on the Northwind
event bus, and a registry that maps each event type and version to a JSON
Schema. Consumers declare the versions they understand; the bus rejects events
that no live consumer can read.

## Motivation

We have had three production incidents in six months caused by a producer
changing an event's shape without coordinating with consumers. In the worst
case (INC-882), a renamed field silently became `null` for two downstream
services for nine hours before anyone noticed.

Events today are untyped JSON blobs validated only by hope. We need a way to:

- evolve an event's shape without breaking existing consumers, and
- detect at publish time — not at 3 a.m. — that a change is incompatible.

## Detailed design

Every event gains two envelope fields:

```json
{
  "type": "order.placed",
  "schemaVersion": 3,
  "data": { "orderId": "...", "totalCents": 1299 }
}
```

A **schema registry** (a versioned directory of JSON Schema files,
`schemas/<type>/v<N>.json`) is the single source of truth. The publish client
validates `data` against the registered schema for `type` + `schemaVersion`
before the event leaves the producer. Validation failures are rejected locally
and never reach the bus.

Compatibility rules:

- **Additive changes** (new optional field) bump the minor behavior but keep the
  same `schemaVersion` — old consumers ignore unknown fields.
- **Breaking changes** (removed or renamed field, changed type, newly required
  field) require a new `schemaVersion`. The producer emits *both* versions
  during a migration window until every consumer has upgraded.

Consumers register the versions they support. The bus tracks live registrations
and refuses to accept an event whose version no registered consumer can read,
turning a silent data loss into a loud, immediate publish error.

## Drawbacks

- **Producer friction.** Every event change now needs a schema edit and, for
  breaking changes, a dual-publish window. This is deliberate cost — it is the
  coordination we are currently skipping.
- **Registry as a dependency.** The publish client must reach the registry (or a
  cached copy) to validate. We mitigate with a build-time bundled snapshot so
  publishing never blocks on a network call.
- **Migration windows linger.** Teams may leave dual-publishing on indefinitely.
  We add a dashboard of stale versions and a quarterly cleanup to counter this.

## Alternatives

- **Do nothing / convention only.** Rejected — three incidents show convention
  isn't enough.
- **Protobuf / Avro with a binary schema registry.** Stronger guarantees, but a
  large migration for our mostly-JS services. Revisit if JSON Schema proves
  insufficient.
- **Validate only in consumers.** Catches bad data too late (after it's on the
  bus) and duplicates logic across every consumer.

## Open questions

All resolved during review:

- *How are schemas reviewed?* Through the normal PR process on the `schemas/`
  directory, with the owning team as required reviewer. (Resolved.)
- *What about events already in flight during a deploy?* The dual-publish window
  covers them; a consumer always sees at least one version it understands.
  (Resolved.)

See the [RFC process](/) for how this proposal reached *Accepted*, or the
[template](/rfcs/0000-template/) to start your own.
