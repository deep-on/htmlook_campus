---
title: REST API reference
description: Endpoints, authentication, and error format for the Pylon REST API.
---

Every Pylon SDK is a thin wrapper over this HTTP API. If your language has no
SDK, you can call it directly. New here? Start with the
[quickstart](/guides/quickstart/) or the [overview](/).

## Base URL and auth

```
https://api.pylon.example/v1
```

Authenticate with a bearer token on every request:

```http
GET /v1/shipments/shp_123 HTTP/1.1
Host: api.pylon.example
Authorization: Bearer pk_test_your_key_here
```

Requests and responses are JSON. All timestamps are RFC 3339 in UTC.

## Shipments

| Method   | Path                         | Description                          |
|----------|------------------------------|--------------------------------------|
| `POST`   | `/v1/shipments`              | Create a shipment.                   |
| `GET`    | `/v1/shipments/{id}`         | Retrieve a shipment.                 |
| `GET`    | `/v1/shipments`              | List shipments (paginated).          |
| `GET`    | `/v1/shipments/{id}/tracking`| Get tracking events for a shipment.  |
| `POST`   | `/v1/shipments/{id}/cancel`  | Cancel an undispatched shipment.     |

### Create a shipment

```http
POST /v1/shipments
Content-Type: application/json

{
  "origin":      { "postalCode": "94107", "country": "US" },
  "destination": { "postalCode": "10001", "country": "US" },
  "packages":    [{ "weightGrams": 800, "lengthCm": 20, "widthCm": 15, "heightCm": 5 }]
}
```

The response includes a generated `id` (prefixed `shp_`) and a `status` of
`created`.

## Pagination

List endpoints return up to 50 items and a `nextCursor`. Pass it back as the
`cursor` query parameter to page forward; a `null` cursor means you've reached
the end.

## Errors

Errors use standard HTTP status codes with a consistent body:

```json
{
  "error": {
    "type": "invalid_request",
    "message": "packages must contain at least one item",
    "param": "packages"
  }
}
```

| Status | `type`                | Meaning                              |
|--------|-----------------------|--------------------------------------|
| 400    | `invalid_request`     | Malformed or missing parameters.     |
| 401    | `authentication_error`| Missing or invalid API key.          |
| 404    | `not_found`           | No resource with that id.            |
| 429    | `rate_limited`        | Too many requests — back off.        |

## Rate limits

Test keys allow 60 requests/minute; live keys allow 600. When limited, the
response includes a `Retry-After` header in seconds.

The [JavaScript](/sdk/javascript/) and [Python](/sdk/python/) SDKs surface these
errors as typed exceptions, so you rarely parse this body by hand.
