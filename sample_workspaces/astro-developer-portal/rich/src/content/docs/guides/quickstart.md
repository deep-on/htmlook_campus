---
title: Quickstart
description: Authenticate and create your first Pylon shipment in five minutes.
sidebar:
  order: 1
---

This guide takes you from zero to a created shipment. For the bigger picture,
see the [overview](/); for full endpoint details, see the
[REST API reference](/reference/api/).

## 1. Get an API key

In the Pylon dashboard, open **Settings → API keys** and create a key. Keys
start with `pk_live_` (production) or `pk_test_` (sandbox). Use a test key while
you're integrating — test shipments never dispatch a real courier.

Store it in an environment variable so it never lands in source control:

```bash
export PYLON_API_KEY="pk_test_your_key_here"
```

## 2. Install an SDK

Pick your language:

```bash
# JavaScript / TypeScript
npm install @pylon/sdk
```

```bash
# Python
pip install pylon
```

Full SDK docs: [JavaScript / TypeScript](/sdk/javascript/) ·
[Python](/sdk/python/).

## 3. Create your first shipment

```js
import { Pylon } from "@pylon/sdk";

const pylon = new Pylon({ apiKey: process.env.PYLON_API_KEY });

const shipment = await pylon.shipments.create({
  origin: { postalCode: "94107", country: "US" },
  destination: { postalCode: "10001", country: "US" },
  packages: [{ weightGrams: 800, lengthCm: 20, widthCm: 15, heightCm: 5 }],
});

console.log(shipment.id, shipment.status); // shp_… created
```

## 4. Track it

A shipment emits tracking events as it moves. Fetch the latest status any time:

```js
const tracking = await pylon.shipments.tracking(shipment.id);
console.log(tracking.latest.status); // picked_up | in_transit | delivered
```

## Next steps

- Read the [REST API reference](/reference/api/) to see every field and
  endpoint the SDKs wrap.
- Move from a `pk_test_` to a `pk_live_` key when you're ready to dispatch real
  deliveries.
- Back to the [overview](/) for how shipments, packages, and tracking events fit
  together.
