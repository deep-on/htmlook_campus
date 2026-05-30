# Quarto · Epidemiology Surveillance · Weekly Bulletin (rich)

A fictional weekly respiratory-infection surveillance bulletin for the
**Riverdale National Health Surveillance Unit** (Wk 18, 2026). The report
walks from executive summary through methods, an executable data section,
results (age / geography / etiology), discussion, and recommendations.

## Files

- `index.qmd` — the bulletin. Includes an epidemic-threshold table and an
  epidemic-curve chart built live from the CSV with pandas + matplotlib.
- `data/weekly_cases.csv` — 18 weeks of synthetic national surveillance
  data: incidence per 100k, epidemic threshold, R(t), hospitalizations,
  and deaths.

## Render it

```bash
quarto preview index.qmd   # live-reloading preview
quarto render index.qmd    # one-shot HTML build
```

The two `{python}` chunks need `pandas` and `matplotlib`
(`pip install pandas matplotlib`).

## All data is fictional

Region names, case counts, and the outbreak itself are invented for
demonstration. Nothing here is a real public-health figure.
