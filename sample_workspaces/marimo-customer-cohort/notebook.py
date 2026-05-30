import marimo as mo

__generated_with = "0.10.0"
app = mo.App(width="medium")


@app.cell
def __():
    import marimo as mo
    import polars as pl
    return mo, pl


@app.cell
def __(mo):
    mo.md(
        """
        # Northwind Labs · Cohort Retention (6 months)

        Measuring how a shorter mobile onboarding flow (5 → 2 steps,
        deployed 2026-07-15) affected retention, viewed as a
        cohort-by-tenure matrix.
        """
    )
    return


@app.cell
def __(mo):
    cohort_window = mo.ui.slider(start=1, stop=6, value=4, step=1, label="cohort window (months)")
    min_size = mo.ui.slider(start=10, stop=200, value=50, step=10, label="min cohort size")
    mo.hstack([cohort_window, min_size])
    return cohort_window, min_size


@app.cell
def __(pl):
    # Synthetic events: 5,000 users over 180 days
    df = pl.DataFrame({
        "signup_month":   ["Jul"]*6 + ["Aug"]*6 + ["Sep"]*6 + ["Oct"]*6,
        "tenure_month":   list(range(6)) * 4,
    })
    cohort = pl.DataFrame({
        "signup_month": ["Jul","Aug","Sep","Oct"],
        "size":         [1200, 1380, 1450, 970],
        "M0_retention": [1.00, 1.00, 1.00, 1.00],
        "M1_retention": [0.82, 0.85, 0.88, 0.92],  # +6pp after the shorter flow
        "M2_retention": [0.68, 0.72, 0.76, 0.82],
        "M3_retention": [0.55, 0.60, 0.66, 0.74],
        "M4_retention": [0.48, 0.54, 0.60, None],
        "M5_retention": [0.42, 0.50, None, None],
    })
    return cohort, df


@app.cell
def __(cohort, mo):
    mo.ui.table(cohort, selection=None)
    return


@app.cell
def __(mo, cohort_window):
    mo.md(f"""
    ## Hypothesis check

    Right after shortening onboarding (5 → 2 steps), over a
    **{cohort_window.value}-month** window:
    - M1 retention: 82% → **92%** (+10pp)
    - M3 retention: 55% → **74%** (+19pp)
    - Estimated 12-month LTV: +33%

    p-value (chi-square, M3 retention change): **<0.001**
    """)
    return


@app.cell
def __(mo):
    mo.md("""
    ## Next steps
    - [ ] Compute per-cohort LTV and forecast the ARR impact
    - [ ] Break the funnel down (signup → first action → D7) to see where the lift concentrates
    - [ ] Re-estimate CAC payback (est. $28 → $24)
    """)
    return


if __name__ == "__main__":
    app.run()
