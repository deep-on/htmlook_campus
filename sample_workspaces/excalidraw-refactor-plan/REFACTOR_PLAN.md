# Auth Refactor · 4-Week Plan

## Before
- JWT 1.0 (custom HMAC, no rotation, 12 CVE-likes)
- 6 client codebases all integrate differently
- 인시던트 history: token leaks 3, scope confusion 7

## Migration (4 weeks · zero downtime)

### W1 · dual-issue
- New OAuth 2.1 + PKCE issuer up
- Both old + new tokens accepted on validate
- Telemetry: which clients still send JWT 1.0

### W2 · client migration
- Update 6 client SDKs to OAuth 2.1
- Internal apps migrated; external SDKs ship in next minor

### W3 · deprecate JWT 1.0
- Validate path returns deprecation warning header for JWT 1.0
- Final cutover communication to remaining external integrators

### W4 · cleanup
- Remove JWT 1.0 issuer
- Remove dual-validate code
- Audit log review · close out CVE entries

## After
- OAuth 2.1 + PKCE
- Token rotation (15min access + 30day refresh)
- Audit log · scope policy · per-client rate limits
- Threat modeling exercise scheduled Q3

## Diagrams
- `diagrams/before-after.excalidraw` — side-by-side
- `diagrams/migration-timeline.excalidraw` — 4-week swimlane
