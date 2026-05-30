---
title: Skiff CLI
description: A workflow runner for production deployments
template: splash
hero:
  tagline: One YAML, every environment.
---

## Install

```bash
brew install skiff/tap/cli
# or: curl -fsSL https://skiff.example/install.sh | sh
```

## First run

```bash
skiff init my-app
cd my-app
skiff run --config=dev.yaml
```
