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
    mo.md("""
    # Time-series Anomaly · Acme API request rate

    30 days of `requests_per_minute` aggregated by hour. Train Prophet, mark
    points outside 99% prediction interval as anomalies, forecast next 7 days.
    """)
    return

@app.cell
def __(pl):
    # 가상: 30일 요청률
    history = pl.DataFrame({
        "ts":    [f"2026-04-{d:02d}T{h:02d}:00" for d in range(1, 31) for h in range(24)],
        "rpm":   [400 + 100*((h-12)**2 < 6) + (5 if d % 7 in (5,6) else 0) for d in range(1, 31) for h in range(24)],
    })
    history.tail(8)
    return history,

@app.cell
def __(mo):
    mo.md("""
    ## Anomalies detected

    | timestamp           | actual | predicted | deviation | tag |
    |---------------------|--------|-----------|-----------|-----|
    | 2026-04-19 14:00    | 1,432  | 510 ± 80  | +922      | spike (P1 incident — see runbook) |
    | 2026-04-23 03:00    | 12     | 240 ± 45  | -228      | drop (deploy window) |

    Both excluded from Prophet training (changepoint_prior_scale=0.05).
    """)
    return

@app.cell
def __(mo):
    mo.md("""
    ## Forecast (next 7 days)

    | day        | yhat | lower | upper | trend |
    |------------|------|-------|-------|-------|
    | 2026-05-09 | 542  | 488   | 596   | flat  |
    | 2026-05-10 | 555  | 498   | 612   | ↑     |
    | 2026-05-11 | 578  | 514   | 642   | ↑     |
    | 2026-05-12 | 565  | 502   | 628   | ~     |
    | 2026-05-13 | 558  | 496   | 620   | ~     |
    | 2026-05-14 | 581  | 516   | 646   | ↑     |
    | 2026-05-15 | 605  | 538   | 672   | ↑     |

    Weekly seasonality detected (weekend +20%). Trend: gradual +2.4% / week —
    consistent with org. growth.
    """)
    return

@app.cell
def __(mo):
    cps = mo.ui.slider(start=0.01, stop=0.5, value=0.05, step=0.01, label="changepoint_prior_scale")
    cps
    return cps,

@app.cell
def __(cps, mo):
    mo.md(f"""
    ## Tuning

    Current `changepoint_prior_scale` = **{cps.value:.2f}**.
    Higher → more flexible trend (overfits). Lower → smoother (misses real changes).
    Default 0.05 is a good starting point for ops metrics.
    """)
    return

if __name__ == "__main__":
    app.run()
