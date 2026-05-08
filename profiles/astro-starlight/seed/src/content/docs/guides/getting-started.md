---
title: 시작하기
description: 5분 안에 첫 API 호출.
sidebar: { order: 1 }
---

## 1. 키 발급

대시보드 → API → "새 키 만들기" → 시크릿 1회 노출.

## 2. 첫 호출

```bash
curl https://api.acme.example/v1/ping \
  -H "Authorization: Bearer ${ACME_KEY}"
```

응답:

```json
{ "ok": true, "ts": "2026-05-08T03:14:15Z" }
```

## 3. SDK

```ts
import { Acme } from '@acme/sdk';
const client = new Acme({ apiKey: process.env.ACME_KEY });
await client.ping();
```

## 다음

- [통합 패턴](/guides/integration-patterns/)
- [Webhook 받기](/guides/webhooks/)
