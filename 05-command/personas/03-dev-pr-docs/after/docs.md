# Events API

The events endpoint returns the activity stream for the current workspace.

## Endpoint

`GET /api/events`

## Query parameters

| Name    | Type     | Required | Description                                                |
|---------|----------|----------|------------------------------------------------------------|
| `from`  | `string` | yes      | ISO-8601 timestamp. Returns events at or after this cursor. |
| `limit` | `number` | no       | Page size, default 50, max 200.                            |

> Renamed from `since` (unix ms) in PR #a3f1c20 — pass an ISO-8601 string instead.

## Example

```
GET /api/events?from=2026-04-29T00:00:00Z&limit=20
```

For the last 24 hours, use `new Date(Date.now() - 86_400_000).toISOString()`.

## Errors

- `400 from required` — the `from` parameter was missing.
- `400 invalid from` — the value did not parse as ISO-8601.
