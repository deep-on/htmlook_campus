---
title: Retrieve an Order
sidebar: { order: 2, badge: { text: "GET", variant: "note" } }
---

## `GET /v1/orders/:id`

```bash
curl https://api.vellum.example/v1/orders/ord_42abc \\
  -H "Authorization: Bearer $VELLUM_KEY"
```

Returns the order object (same schema as the create response).
