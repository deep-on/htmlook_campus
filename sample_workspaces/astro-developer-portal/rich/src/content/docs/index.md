---
title: Pylon Developer Hub
description: Build on the Pylon delivery platform — guides, SDKs, and the REST API.
---

**Pylon** is a delivery platform: you create shipments, attach packages, and
track them from pickup to delivery through a single API. This portal has
everything you need to integrate.

## Start here

- [**Quickstart**](/guides/quickstart/) — authenticate and create your first
  shipment in about five minutes.
- [**JavaScript / TypeScript SDK**](/sdk/javascript/) — the `@pylon/sdk`
  package for Node and the browser.
- [**Python SDK**](/sdk/python/) — the `pylon` package for Python 3.10+.
- [**REST API reference**](/reference/api/) — the underlying HTTP API every SDK
  wraps.

## How Pylon is organized

Three resources cover the whole platform:

- **Shipments** — a delivery from an origin to a destination. The top-level
  object you create.
- **Packages** — one or more parcels attached to a shipment, each with weight
  and dimensions.
- **Tracking events** — timestamped status updates (`picked_up`, `in_transit`,
  `delivered`) emitted as a shipment moves.

If you prefer to read code first, jump straight to the
[quickstart](/guides/quickstart/); if you want the full surface, the
[REST API reference](/reference/api/) lists every endpoint.

## Authentication in one line

Every request uses a secret API key sent as a bearer token. Keep keys
server-side. The [quickstart](/guides/quickstart/) shows where to find yours and
how the SDKs pick it up from the environment.
