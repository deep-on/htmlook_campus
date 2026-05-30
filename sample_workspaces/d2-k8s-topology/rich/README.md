# d2 · Kubernetes Topology (rich)

A production EKS topology for the fictional **Finch** checkout platform:
edge / app / data namespaces, an SQS-backed worker, and managed RDS +
Secrets Manager. Shows clusters, north-south vs. east-west traffic, a
dashed secret-fetch edge, and queue/cylinder shapes.

Preview the diagram with the D2 pane (`.d2` ↔ live SVG), or:

```bash
d2 --layout elk topology.d2 topology.svg
```
