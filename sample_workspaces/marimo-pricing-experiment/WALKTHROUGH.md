# Bayesian Pricing Walkthrough · 30-min Walkthrough

> A guided demo asset — ready to record straight through.

## 1. PyMC environment
```bash
pip install marimo polars pymc arviz
marimo edit notebook.py
```

## 2. Visualize the posterior
1. Move the ROPE-width slider from $0.5 to $1.0
2. P(best = $49) recomputes automatically
3. The ROPE table refreshes instantly

## 3. Signature move
- Marimo only — Jupyter isn't reactive; changing a slider there means re-running cells by hand
