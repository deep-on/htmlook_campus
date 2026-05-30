# marimo · Retail Demand Forecast (rich)

A reactive marimo notebook forecasting 14 days of SKU demand for the
fictional **Harborline Retail**. Eight cells: imports → synthetic sales →
summary → history plot → seasonal-naive forecast → actual-vs-forecast plot →
reorder takeaway. Self-contained (synthetic data, no CSV needed).

```bash
pip install marimo numpy pandas matplotlib
marimo edit notebook.py     # reactive editor
marimo run  notebook.py     # app mode
```

Replace the synthetic block with `pd.read_csv("sales.csv")` to use real data.
