---
title: Create a Customer
sidebar: { order: 1, badge: { text: "POST", variant: "tip" } }
---

## `POST /v1/customers`

```bash
curl https://api.vellum.example/v1/customers \\
  -H "Authorization: Bearer $VELLUM_KEY" \\
  -d '{"email":"a@b.com","name":"Alice"}'
```

Returns a `cus_…` ID.
