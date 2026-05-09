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
    # User Funnel · Acme · Q3

    5-step funnel for ~10k weekly signups. Identify largest drop-off + simulate
    uplift impact on D30 retained users (= ARR proxy).
    """)
    return

@app.cell
def __(pl):
    funnel = pl.DataFrame({
        "step":      ["signup",   "verify",  "activate", "D7",    "D30"],
        "users":     [10_000,     8_200,     4_920,      3_198,   1_919],
        "step_conv": [1.000,      0.820,     0.600,      0.650,   0.600],
    })
    funnel
    return funnel,

@app.cell
def __(mo):
    mo.md("""
    ## Drop-off ranking

    | step               | drop  |
    |--------------------|-------|
    | verify → activate  | **40%** ⚠ largest leak |
    | signup → verify    | 18%   |
    | D7 → D30           | 40% (cohort retention) |
    | activate → D7      | 35%   |

    Hypothesis: activate is gated by a 12-step setup wizard. **Cut to 5 steps**
    → expected step_conv 0.60 → 0.78 (analogous to mobile onboarding cut).
    """)
    return

@app.cell
def __(mo):
    activate_uplift = mo.ui.slider(start=0.0, stop=0.30, value=0.18, step=0.02, label="activate uplift (Δ step_conv)")
    activate_uplift
    return activate_uplift,

@app.cell
def __(activate_uplift, mo):
    new_d30 = round(10_000 * 0.82 * (0.60 + activate_uplift.value) * 0.65 * 0.60)
    delta = new_d30 - 1919
    mo.md(f"""
    ## Simulator

    With activate uplift +{activate_uplift.value:.2f}: D30 retained users = **{new_d30:,}**
    (vs baseline 1,919 → +{delta:,}, **{delta/1919*100:.0f}% lift**).

    Assuming $40 ARPU/year, ARR impact ≈ **${delta * 40 / 1000:.0f}k** annualized.
    """)
    return

if __name__ == "__main__":
    app.run()
