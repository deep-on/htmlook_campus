# d2 · Disaster Recovery — Active/Passive (rich)

An active/passive multi-region DR topology for the fictional **Halcyon Pay**
service. `us-east-1` carries all live traffic (hot fleet, Aurora writer);
`us-west-2` runs as a warm standby (scaled-down ASG, Aurora reader) behind
a dashed, faded container. Route 53 health-checked failover routing sits
in front, Aurora global replication keeps RPO under 30 s, and continuous
versioned snapshots land in a cross-region S3 bucket.

A Markdown failover playbook documents the ~5-minute promote-and-cut-over
runbook (RTO 5 min · RPO < 30 s).

Shapes: cloud, hexagons, cylinders (databases / S3), a queue (cache),
dashed standby + snapshot edges, and per-region ops notes.

Preview the diagram with the D2 pane (`.d2` ↔ live SVG), or:

```bash
d2 --layout elk architecture.d2 architecture.svg
```
