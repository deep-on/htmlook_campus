---
title: Python SDK
description: Install and use the pylon package for Python 3.10+.
sidebar:
  order: 2
---

The official Python SDK, `pylon`, supports Python 3.10 and newer with full type
hints. New to Pylon? Start with the [quickstart](/guides/quickstart/).

## Install

```bash
pip install pylon
```

## Initialize

```python
import os
from pylon import Pylon

client = Pylon(api_key=os.environ["PYLON_API_KEY"])
```

The client reads `PYLON_API_KEY` from the environment if you omit `api_key`.

## Create and track a shipment

```python
shipment = client.shipments.create(
    origin={"postal_code": "94107", "country": "US"},
    destination={"postal_code": "10001", "country": "US"},
    packages=[{"weight_grams": 800, "length_cm": 20, "width_cm": 15, "height_cm": 5}],
)

tracking = client.shipments.tracking(shipment.id)
print(tracking.latest.status)
```

## Error handling

Errors raise `PylonError`, whose `type` matches the
[REST error format](/reference/api/):

```python
from pylon import PylonError

try:
    client.shipments.create(...)
except PylonError as err:
    if err.type == "rate_limited":
        # back off and retry
        ...
    else:
        raise
```

## Pagination

`list` returns an iterator that fetches pages lazily:

```python
for shipment in client.shipments.list():
    print(shipment.id)
```

## Async

An async client is available for `asyncio` apps:

```python
from pylon import AsyncPylon

client = AsyncPylon(api_key=os.environ["PYLON_API_KEY"])
shipment = await client.shipments.create(...)
```

Working in Node instead? See the [JavaScript / TypeScript SDK](/sdk/javascript/).
For every endpoint, see the [REST API reference](/reference/api/).
