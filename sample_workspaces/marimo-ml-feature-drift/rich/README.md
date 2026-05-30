# marimo · ML Feature Drift Monitor (rich)

A reactive marimo notebook comparing a **reference** feature sample against a
30-day **current** production window. Thirteen cells: imports → synthetic
reference/current frames → summary → PSI implementation → KS statistic →
per-feature flag table → flag summary → PSI bar chart with decision bands →
reference-vs-current histogram overlay → interactive alert-threshold tuner →
takeaway. Pure numpy/pandas (PSI and KS computed inline — no scipy), so it
runs anywhere.

```bash
pip install marimo numpy pandas matplotlib
marimo edit notebook.py     # reactive editor
marimo run  notebook.py     # app mode
```

Replace the synthetic frames with your reference/current parquet exports to
monitor a real model.
