---
title: acme CLI
description: A workflow runner for production deployments
template: splash
hero:
  tagline: One YAML, every environment.
---

## Install

```bash
brew install acme/tap/cli
# or: curl -fsSL https://acme.dev/install.sh | sh
```

## First run

```bash
acme init my-app
cd my-app
acme run --config=dev.yaml
```
