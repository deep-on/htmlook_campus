# Quarto · Meta-analysis (Systematic Review) (rich)

A fictional systematic review and random-effects meta-analysis asking
whether **structured telephone follow-up reduces 30-day hospital
readmission**, by the **Northgate Evidence Synthesis Collaborative**. The
report follows IMRAD with a PRISMA flow diagram, a live pooled-estimate
calculation, a forest plot, heterogeneity statistics, subgroup analysis,
and a publication-bias check.

## Files

- `index.qmd` — the review. Two `{python}` chunks read the study CSV,
  compute a DerSimonian–Laird random-effects pooled risk ratio plus I²/τ²
  with pandas + numpy, and draw a forest plot with matplotlib. A `{mermaid}`
  block renders the PRISMA flow.
- `data/extracted_studies.csv` — 12 synthetic randomized trials: sample
  size, risk ratio, 95% CI bounds, weight, and prevention subgroup.

## Render it

```bash
quarto preview index.qmd   # live-reloading preview
quarto render index.qmd    # one-shot HTML build
```

The chunks need `pandas`, `numpy`, and `matplotlib`
(`pip install pandas numpy matplotlib`).

## All data is fictional

Study names, effect sizes, and the research question are invented for
demonstration. None of these trials exist.
