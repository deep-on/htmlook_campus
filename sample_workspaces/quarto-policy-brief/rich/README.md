# quarto · Policy Brief (rich)

A complete data-driven policy brief — YAML front matter, executive summary,
background, a **data section that reads `data/regulation_matrix.csv` via a
pandas chunk** and renders both a table and a matplotlib bar chart, followed by
findings, a recommendation matrix, and methodology. The subject is a
comparison of five AI-regulation regimes (EU AI Act, NIST AI RMF, KR AI Act,
UK, Canada).

Preview / render:

```bash
quarto preview index.qmd   # live
quarto render  index.qmd   # → index.html
```

The CSV is self-contained — edit `data/regulation_matrix.csv` and re-render to
update every table and chart. Requires `pandas` and `matplotlib` in the Quarto
Python environment.
