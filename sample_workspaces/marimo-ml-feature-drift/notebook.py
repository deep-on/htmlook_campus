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
    # ML Feature Drift · churn-predictor v3.2

    Production model (XGBoost, churn prediction) deployed 30 days ago. Compare
    prod feature distributions against training set via PSI (Population Stability
    Index) + KS test.
    """)
    return

@app.cell
def __(pl):
    drift = pl.DataFrame({
        "feature":      ["user_age",  "campaign", "device", "geo_region", "price_tier", "tenure_days", "n_sessions_30d", "is_paying"],
        "psi":          [0.42,        0.31,       0.22,     0.15,         0.09,          0.07,          0.05,             0.02],
        "ks_pvalue":    [1e-12,       1e-8,       1e-5,     0.012,        0.18,          0.42,          0.71,             0.95],
        "severity":     ["high",      "high",     "medium", "low",        "low",         "low",         "ok",             "ok"],
    })
    drift
    return drift,

@app.cell
def __(mo):
    mo.md("""
    ## Findings

    **High-drift (PSI > 0.25)**:
    - `user_age` (0.42): population shift to younger users — likely TikTok ads campaign launched W2.
    - `campaign` (0.31): new acquisition channel mix.

    **Action items**:
    - [ ] Retrain with last 14 days of prod data
    - [ ] A/B compare retrained vs frozen on holdout
    - [ ] Add automated alerting at PSI > 0.25 threshold
    - [ ] Update model card lineage
    """)
    return

@app.cell
def __(mo):
    mo.md("""
    ## Lineage tree

    ```
    raw events (Kafka)
      └─ feature_store
          ├─ user_age          (← user.birthdate)
          ├─ campaign          (← attribution.last_touch)
          ├─ device            (← user_agent parser)
          └─ ...
              └─ churn-predictor v3.2 (training: 2026-01-15)
    ```

    `user.birthdate` ETL hasn't changed. Drift entirely from acquisition mix.
    """)
    return

if __name__ == "__main__":
    app.run()
