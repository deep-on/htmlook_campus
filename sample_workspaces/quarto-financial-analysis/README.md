# Quarto · DCF Valuation Report

A 5-year DCF model for a fictional SaaS company (Brightwave · Series B). The
prose cites CSV cells, so changing the data updates the narrative automatically.

## Seed content

- `index.qmd` — executive summary + DCF body + sensitivity analysis (6 sections)
- `_quarto.yml` — both HTML and PDF formats
- `data/financial_model.csv` — 5-year assumptions (revenue / margin / WACC / terminal)
- `references.bib` — Damodaran / McKinsey citations

## Quick start

```bash
quarto preview index.qmd        # http://localhost:4848 live
quarto render index.qmd --to pdf
```

## Working in HTMLook

- **Cell citation**: cite a `financial_model.csv` cell in the prose. Change the
  cell and the EBITDA / EV figures in the body update.
- **Multi-target edit**: rename the company across every section in one pass
  (e.g. Brightwave → your own company).
- **Pane pair**: `.qmd` on the left, `quarto preview` on the right
  (localhost:4848).

## External dependencies

- Quarto CLI · TinyTeX (for PDF output)

## Swapping in your data

Replace the numbers in `data/financial_model.csv` with your own and re-render.
WACC defaults to 8.5%, terminal growth to 2%.
