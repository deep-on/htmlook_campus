---
title: API Reference
description: 전체 endpoint 사전.
sidebar: { order: 1, badge: { text: "v1.0" } }
---

## `GET /v1/ping`

서버 헬스 체크. 인증 불필요.

```json
{ "ok": true, "ts": "ISO8601" }
```

## `POST /v1/orders`

새 주문 생성. 인증 필요.

| 필드 | 타입 | 필수 | 설명 |
|------|------|------|------|
| `sku` | string | ✓ | SKU 코드 |
| `qty` | number | ✓ | 1 이상 |
| `customer_id` | string | ✓ | 기존 고객 |

응답: `201 Created` + 주문 객체.
