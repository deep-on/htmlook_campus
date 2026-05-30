# Tide Checkout Refactor · 4-Week Plan

## Before
- One `checkout-monolith` bundling cart / pricing / payments / inventory / tax /
  notifications
- Every change redeploys the whole thing; one slow path blocks all others

## Migration (4 weeks · zero downtime)

### W1 · carve out payments
- Extract payments behind an API gateway
- Dual-write so the monolith and the new service stay in sync

### W2 · carve out pricing + tax
- Extract pricing and tax as services
- Route a canary slice of traffic through the new path

### W3 · carve out inventory + notifications
- Move inventory and notifications onto the event bus
- Strangler-fig: new requests hit services, legacy paths fade out

### W4 · cutover + cleanup
- Cut over remaining traffic; remove monolith code paths
- Audit log review · close out the migration

## After
- Independently deployable services behind an API gateway
- Event bus for cross-service flows
- Each capability scales and ships on its own
