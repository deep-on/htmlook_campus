# d2 · SaaS Multi-Tenant Isolation (rich)

Three coexisting isolation tiers for the fictional **Tessellate Cloud**
platform, fed by one tenant router that resolves `tenant_id` from the
subdomain + JWT and fans out by plan:

- **Pool** — shared app + Postgres (row-level security) + namespaced Redis.
- **Hybrid** — pooled app, schema-per-tenant Postgres (`search_path`).
- **Silo** — dedicated app stack + database per enterprise tenant
  (Vireo, Marlin).

A control plane (tenant registry, per-tenant KMS keys, usage metering)
wires across all tiers, with dashed envelope-encryption edges from the
silo databases. A Markdown table summarizes the cost / blast-radius /
compliance tradeoffs.

Shapes: cloud, hexagon routers, cylinders, a queue (Redis), nested
containers, and dashed control-plane edges.

Preview the diagram with the D2 pane (`.d2` ↔ live SVG), or:

```bash
d2 --layout elk architecture.d2 architecture.svg
```
