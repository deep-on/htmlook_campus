---
title: acme run
sidebar: { order: 1 }
---

Execute the workflow defined in `acme.yaml`.

## Synopsis

```
acme run [--config <path>] [--env <name>] [--verbose] [--dry-run]
```

## Description

Reads `acme.yaml` (or path passed via `--config`), resolves dependencies, and executes steps in order. Failures abort by default; use `--continue-on-error` to override.

## Examples

```bash
# basic
acme run

# explicit config + verbose
acme run --config=prod.yaml --verbose

# dry run (print what would happen)
acme run --dry-run
```

## Output

Logs to stdout in human-readable form. Use `--format=json` for CI piping.

## Exit codes

| code | meaning |
|------|---------|
| 0    | success |
| 1    | step failed |
| 2    | config invalid |
| 130  | SIGINT (user) |
