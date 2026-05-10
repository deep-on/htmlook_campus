# Events API

The events endpoint returns the activity stream for the current workspace.

## Endpoint

`GET /api/events`

## Query parameters

| Name    | Type      | Required | Description                               |
|---------|-----------|----------|-------------------------------------------|
| `since` | `number`  | yes      | Unix milliseconds. Returns events at or after this cursor. |
| `limit` | `number`  | no       | Page size, default 50, max 200.           |

## Example

```
GET /api/events?since=1714435200000&limit=20
```

The cursor must be an integer. Pass `Date.now() - 86_400_000` for the
last 24 hours of events.

## Errors

- `400 since required` — the `since` parameter was missing.
- `400 invalid since` — the value did not parse as an integer.
