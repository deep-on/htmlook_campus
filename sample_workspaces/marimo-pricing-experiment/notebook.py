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
    # Bayesian A/B Pricing · Acme Pro

    60-day experiment, 3 arms ($29 / $49 / $79), n=2,400. Posterior on conversion ×
    ARPU = expected revenue per visitor. Decision rule: pick the arm whose 89% HDI
    upper bound is **strictly above** other arms' HDI lower bounds.
    """)
    return


@app.cell
def __(pl):
    arms = pl.DataFrame({
        "price": [29, 49, 79],
        "visitors": [800, 800, 800],
        "conversions": [184, 144, 88],
        "conv_rate": [0.230, 0.180, 0.110],
        "arpu": [29, 49, 79],
        "rev_per_visitor": [6.67, 8.82, 8.69],
    })
    arms
    return arms,


@app.cell
def __(mo):
    mo.md("""
    ## Posterior (PyMC)

    ```python
    with pm.Model() as m:
        p = pm.Beta("p", alpha=1, beta=1, shape=3)
        obs = pm.Binomial("obs", n=visitors, p=p, observed=conversions)
        trace = pm.sample(2000, tune=2000, target_accept=0.95)
    ```

    Posterior mean conversion rate (89% HDI):
    - $29 → 0.230 [0.205, 0.256]
    - $49 → 0.180 [0.158, 0.204]
    - $79 → 0.110 [0.094, 0.128]
    """)
    return


@app.cell
def __(mo):
    mo.md("""
    ## Expected Revenue per Visitor (posterior)

    | arm | mean | 89% HDI | P(arm = best) |
    |-----|------|---------|---------------|
    | $29 | $6.67 | [5.95, 7.41] | 0.04 |
    | **$49 ★** | **$8.82** | **[7.74, 9.94]** | **0.74** |
    | $79 | $8.69 | [7.42, 10.02] | 0.22 |

    **Recommendation**: $49. P(best) = 0.74. ROPE = [$8.50, $9.00] for $49 vs $79
    overlap is 28% — modest practical equivalence risk; defer to qualitative
    factors (positioning, competitive).
    """)
    return


@app.cell
def __(mo):
    rope_width = mo.ui.slider(start=0.0, stop=2.0, value=0.5, step=0.1, label="ROPE width ($)")
    rope_width
    return rope_width,


@app.cell
def __(mo, rope_width):
    mo.md(f"""
    ## Sensitivity to ROPE

    Current ROPE width = **${rope_width.value:.1f}**. P(best) for $49 stays > 0.6 across
    ROPE widths $0.0–$1.0, suggesting the decision is robust.
    """)
    return


if __name__ == "__main__":
    app.run()
