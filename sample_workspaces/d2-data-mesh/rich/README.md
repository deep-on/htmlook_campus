# d2 · Data Mesh (rich)

A four-domain data mesh for the fictional **Quillwind** data platform.
Each domain (Sales, Product, Finance, Ops) owns its raw sources, a
hexagon **data product**, and an SQL/REST **output port**. All domains
build on one self-serve platform (ingestion + storage, catalog, IAM,
SLA/lineage monitor), register their ports in the shared catalog, and a
cross-domain analytics consumer discovers and joins products (revenue per
cohort) through the catalog.

A federated governance council applies org-wide schema / SLA / PII policy
via dashed edges into the platform's IAM and observability — enforced by
the platform, not a central team. A Markdown note states the four mesh
principles.

Shapes: hexagons (data products / governance), cylinders (sources /
storage), a queue (event stream), nested domain containers, and dashed
policy edges.

Preview the diagram with the D2 pane (`.d2` ↔ live SVG), or:

```bash
d2 --layout elk architecture.d2 architecture.svg
```
