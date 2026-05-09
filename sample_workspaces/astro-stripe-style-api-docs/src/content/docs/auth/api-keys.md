---
title: API keys
sidebar: { order: 1 }
---

API keys are the simplest way to authenticate. Use OAuth 2.1 (`/oauth/authorize`) for end-user-scoped access.

## Create

Dashboard → Developers → API keys → "Create new key". Secret keys begin `sk_live_…`. **Show only once.**

## Use

```bash
curl https://api.acme.example/v1/orders \\
  -H "Authorization: Bearer $ACME_KEY"
```

| key prefix | scope |
|------------|-------|
| `pk_live_` | publishable, client-side OK |
| `sk_live_` | secret, server-only |
| `sk_test_` | test mode |

## Rotate

Rotate keys monthly. POST `/v1/keys/rotate` returns new key + 24h grace on old.
