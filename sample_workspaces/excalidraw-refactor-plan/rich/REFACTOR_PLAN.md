# Tide Checkout Refactor · 4-Week Plan

## Before
- One `checkout-monolith` bundling cart, pricing, payments, inventory, tax, notifications
- Single deploy: a payments change blocks a tax change
- Shared DB tables couple every team; release coordination is constant

## Migration (4 weeks · zero downtime, strangler-fig)

### W1 · extract Cart
- Carve cart out behind the API gateway
- Dual-write cart DB schema; canary 5% of cart traffic
- Telemetry: confirm parity between monolith and new cart service

### W2 · extract Payments
- Move payments service out with idempotency keys
- Backfill payment ledger; wire payments SLO alerts
- External integrators unaffected (gateway routes stay stable)

### W3 · extract Pricing / Tax
- Split pricing and tax rules into their own services
- Pricing read-model sync; load-test the new topology
- Deprecation warnings on any remaining monolith pricing routes

### W4 · cutover + cleanup
- Remove monolith routes; drop shared tables
- Decommission the old deploy
- Audit log review · close out coupling debt

## After
- Cart / Pricing / Payments / Inventory / Tax / Notify services behind an API gateway
- Each service owns its deploy and DB schema
- Event bus for cross-service notifications
- Dual-write rollback path kept ready through the cutover window

## Diagrams
- `diagrams/before-after.excalidraw` — monolith vs extracted services
- `diagrams/migration-timeline.excalidraw` — 4-week swimlane (Backend / Data / Ops)
