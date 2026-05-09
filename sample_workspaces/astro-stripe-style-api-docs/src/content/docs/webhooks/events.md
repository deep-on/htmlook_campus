---
title: Webhook events
sidebar: { order: 1 }
---

We POST events to your endpoint with HMAC-SHA256 signature in `Acme-Signature` header.

## Event types

- `order.created`
- `order.fulfilled`
- `order.cancelled`
- `customer.updated`

## Verify signature

```js
const expected = crypto.createHmac('sha256', secret).update(rawBody).digest('hex');
if (expected !== sig) return res.status(400).end();
```
