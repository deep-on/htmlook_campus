---
title: JavaScript / TypeScript SDK
description: Install and use the @pylon/sdk package in Node and the browser.
sidebar:
  order: 1
---

The official JavaScript SDK, `@pylon/sdk`, works in Node 18+ and modern
browsers. It ships with TypeScript types. New to Pylon? Do the
[quickstart](/guides/quickstart/) first.

## Install

```bash
npm install @pylon/sdk
```

## Initialize

```ts
import { Pylon } from "@pylon/sdk";

const pylon = new Pylon({
  apiKey: process.env.PYLON_API_KEY,
  // optional: override the default https://api.pylon.example/v1
  // baseUrl: "https://api.pylon.example/v1",
});
```

Never hard-code a key in browser code. For client-side use, proxy requests
through your own backend so the secret stays server-side.

## Create and track a shipment

```ts
const shipment = await pylon.shipments.create({
  origin: { postalCode: "94107", country: "US" },
  destination: { postalCode: "10001", country: "US" },
  packages: [{ weightGrams: 800, lengthCm: 20, widthCm: 15, heightCm: 5 }],
});

const tracking = await pylon.shipments.tracking(shipment.id);
console.log(tracking.latest.status);
```

## Error handling

API errors are thrown as `PylonError` with a typed `type` field that mirrors the
[REST error format](/reference/api/):

```ts
import { Pylon, PylonError } from "@pylon/sdk";

try {
  await pylon.shipments.create({ /* … */ });
} catch (err) {
  if (err instanceof PylonError && err.type === "rate_limited") {
    // back off and retry
  } else {
    throw err;
  }
}
```

## Pagination

`list` returns an async iterator that pages automatically:

```ts
for await (const shipment of pylon.shipments.list()) {
  console.log(shipment.id);
}
```

Prefer Python? See the [Python SDK](/sdk/python/). Need the raw HTTP surface?
See the [REST API reference](/reference/api/).
