---
title: Create an Order
sidebar: { order: 1, badge: { text: "POST", variant: "tip" } }
---

## `POST /v1/orders`

Create a new order.

### Request

| field | type | required | description |
|-------|------|---------|-------------|
| `sku` | string | ✓ | SKU code |
| `qty` | integer | ✓ | ≥1 |
| `customer_id` | string | ✓ | existing customer |
| `currency` | string |   | ISO-4217, default `USD` |
| `metadata` | object |   | <=20 keys |

### Example

```bash
curl https://api.vellum.example/v1/orders \\
  -H "Authorization: Bearer $VELLUM_KEY" \\
  -H "Content-Type: application/json" \\
  -d '{"sku":"WIDGET-1","qty":3,"customer_id":"cus_abc"}'
```

```js
const order = await vellum.orders.create({
  sku: 'WIDGET-1', qty: 3, customer_id: 'cus_abc',
});
```

```python
order = vellum.orders.create(sku="WIDGET-1", qty=3, customer_id="cus_abc")
```

### Response · `201 Created`

```json
{
  "id": "ord_42abc",
  "object": "order",
  "sku": "WIDGET-1",
  "qty": 3,
  "amount": 8700,
  "currency": "USD",
  "status": "pending",
  "created": "2026-05-08T03:14:15Z"
}
```

### Errors

| code | when |
|------|------|
| `400` | invalid params |
| `401` | bad/expired key |
| `404` | customer not found |
| `429` | rate limited (100 req/min) |
