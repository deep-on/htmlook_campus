# Cohort Retention Walkthrough · 30-min Walkthrough

> A guided demo asset — ready to record straight through.

## 1. Run the notebook
1. `pip install marimo polars plotly`
2. `marimo edit notebook.py` → http://localhost:2718

## 2. Reactive slider demo
1. Move the cohort_window slider from 4 to 6
2. The heatmap recomputes automatically (sub-second)
3. The +10pp / +19pp figures in the hypothesis-check cell update on their own

## 3. HTMLook pane pair
1. Left: edit notebook.py
2. Right: the marimo localhost:2718 iframe (auto-refresh)
3. Line cite: pick a cell line and ask the AI "why is it computed this way?"

## 4. Export the result
- `marimo export html notebook.py --output report.html`
