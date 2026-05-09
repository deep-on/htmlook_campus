---
title: Retrieve an Order
sidebar: { order: 2, badge: { text: "GET", variant: "note" } }
---

## `GET /v1/orders/:id`

```bash
curl https://api.acme.example/v1/orders/ord_42abc \\
  -H "Authorization: Bearer $ACME_KEY"
```

Returns the order object (same schema as create response).
