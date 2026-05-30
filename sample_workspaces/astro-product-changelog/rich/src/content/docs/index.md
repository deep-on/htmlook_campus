---
title: What's new in Tideline
description: New features, changes, and fixes across recent Tideline releases.
---

This is the changelog for **Tideline**, the product analytics platform. Every
release that changes behavior you can see gets an entry here. We group changes
with a small legend:

- `+` **added** — new capability
- `~` **changed** — existing behavior adjusted
- `!` **breaking** — requires action before or after upgrade
- `fix` — a bug fixed

## Recent releases

- [**v3.0.0**](/releases/v3-0-0/) — Funnels v2 and the new query engine. Includes
  one breaking change to saved-report URLs.
- [**v2.8.0**](/releases/v2-8-0/) — Scheduled email reports and a faster events
  table.
- [**v2.7.1**](/releases/v2-7-1/) — Hotfix for timezone handling in cohort
  charts.

## How we version

Tideline follows semantic versioning. A **major** bump (like
[v3.0.0](/releases/v3-0-0/)) means at least one breaking change with a documented
migration. **Minor** bumps add features without breaking anything. **Patch**
bumps, like [v2.7.1](/releases/v2-7-1/), are fixes only.

Self-hosted customers should read the breaking-change notes on a major release
*before* upgrading. Cloud workspaces are migrated automatically.
