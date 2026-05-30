# DCF Valuation Walkthrough

A short demo walkthrough of the Brightwave DCF report.

## 1. Setup
1. `quarto preview index.qmd` → http://localhost:4848
2. Open the workspace in HTMLook

## 2. Cell-citation demo (90 sec)
1. Select the Y3 EBITDA cell in `data/financial_model.csv` (currently 3.8)
2. Ask HTMLook AI: "Show where this cell is cited in the body"
3. The AI highlights "**Y3 EBITDA: $3.8M**" in the prose
4. Change the cell to 5.0 and Save
5. The body updates automatically — both the Y3 row and the sensitivity table

## 3. Multi-target edit
1. AI Chat: "Rename Brightwave → MyCompany across all sections"
2. The AI edits every section at once

## 4. PDF output
- `quarto render index.qmd --to pdf`
- TinyTeX installs automatically; takes about a minute
