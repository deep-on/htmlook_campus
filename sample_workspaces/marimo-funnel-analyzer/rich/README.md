# marimo · Product Funnel Analyzer (rich)

A reactive marimo notebook for a 5-stage acquisition funnel —
**signup → verify → activate → D7 → D30** — with a per-channel breakdown.
Twelve cells: imports → synthetic cohort (modeled per user, per channel) →
summary → funnel bar chart → drop-off ranking → largest-leak callout →
segment table → channel conversion chart → interactive uplift simulator →
revenue impact → takeaway. Self-contained (synthetic data, no CSV needed).

```bash
pip install marimo numpy pandas matplotlib
marimo edit notebook.py     # reactive editor
marimo run  notebook.py     # app mode
```

Replace the synthetic cohort block with `pd.read_csv("events.csv")` to use
your own per-user, per-stage event log.
