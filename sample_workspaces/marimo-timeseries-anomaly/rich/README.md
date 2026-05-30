# marimo · Time-series Anomaly Detection (rich)

A reactive marimo notebook detecting anomalies in 30 days of hourly
requests-per-minute. Thirteen cells: imports → synthetic series with a daily
shape, weekend lift, and injected anomalies → summary → raw plot → rolling
mean/std + z-score → IQR fences → two-method flag table → flag summary →
anomaly-marked plot → interactive z-threshold tuner → takeaway. An anomaly is
confirmed only when the rolling z-score **and** the IQR rule agree, which keeps
ordinary daily peaks from firing. Self-contained (synthetic data, no CSV).

```bash
pip install marimo numpy pandas matplotlib
marimo edit notebook.py     # reactive editor
marimo run  notebook.py     # app mode
```

Replace the synthetic generator with
`pd.read_csv("metrics.csv", parse_dates=["ts"])` to use your own metric.
