import marimo as mo

__generated_with = "0.10.0"
app = mo.App(width="medium")


@app.cell
def __():
    import marimo as mo
    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt
    return mo, np, pd, plt


@app.cell
def __(mo):
    mo.md(
        """
        # ML Feature Drift Monitor

        A churn model was trained on a **reference** sample and has now seen
        30 days of **current** production traffic. This notebook compares the two
        distributions feature-by-feature using the **Population Stability Index
        (PSI)** and a **two-sample KS test**, then flags features that have moved.

        Data is synthetic and self-contained — swap in your reference/current
        parquet exports to monitor a real model.
        """
    )
    return


@app.cell
def __(np, pd):
    # Build a reference window and a current window. Some features are stable,
    # others are deliberately shifted to simulate real-world drift.
    rng = np.random.default_rng(23)
    n_ref, n_cur = 8000, 6000

    reference = pd.DataFrame({
        "user_age":        rng.normal(42, 12, n_ref),
        "tenure_days":     rng.gamma(2.0, 90, n_ref),
        "n_sessions_30d":  rng.poisson(8, n_ref).astype(float),
        "price_tier":      rng.normal(3.0, 1.0, n_ref),
        "is_paying":       rng.binomial(1, 0.30, n_ref).astype(float),
    })

    current = pd.DataFrame({
        # younger acquisition wave → mean shifts down, variance up
        "user_age":        rng.normal(34, 14, n_cur),
        # tenure stable (steady base)
        "tenure_days":     rng.gamma(2.0, 92, n_cur),
        # engagement mildly up
        "n_sessions_30d":  rng.poisson(9, n_cur).astype(float),
        # pricing experiment widened the tiers
        "price_tier":      rng.normal(3.2, 1.4, n_cur),
        # paying mix essentially unchanged
        "is_paying":       rng.binomial(1, 0.31, n_cur).astype(float),
    })
    features = list(reference.columns)
    reference.describe().round(2)
    return current, features, n_cur, n_ref, reference, rng


@app.cell
def __(mo, n_cur, n_ref):
    mo.md(
        f"""
        Reference window: **{n_ref:,} rows** · current window: **{n_cur:,} rows**.
        Five features monitored. PSI bands: < 0.10 stable · 0.10–0.25 watch ·
        > 0.25 drift.
        """
    )
    return


@app.cell
def __(np):
    # PSI on fixed reference-quantile bins, with a small epsilon to avoid /0.
    def psi(ref, cur, bins=10):
        edges = np.quantile(ref, np.linspace(0, 1, bins + 1))
        edges[0], edges[-1] = -np.inf, np.inf
        edges = np.unique(edges)
        ref_pct = np.histogram(ref, bins=edges)[0] / len(ref)
        cur_pct = np.histogram(cur, bins=edges)[0] / len(cur)
        eps = 1e-6
        ref_pct = np.clip(ref_pct, eps, None)
        cur_pct = np.clip(cur_pct, eps, None)
        return float(np.sum((cur_pct - ref_pct) * np.log(cur_pct / ref_pct)))
    return psi,


@app.cell
def __(np):
    # Lightweight two-sample KS statistic (no scipy dependency).
    def ks_stat(ref, cur):
        all_vals = np.sort(np.concatenate([ref, cur]))
        cdf_ref = np.searchsorted(np.sort(ref), all_vals, side="right") / len(ref)
        cdf_cur = np.searchsorted(np.sort(cur), all_vals, side="right") / len(cur)
        return float(np.max(np.abs(cdf_ref - cdf_cur)))
    return ks_stat,


@app.cell
def __(current, features, ks_stat, pd, psi, reference):
    def band(p):
        if p > 0.25:
            return "drift"
        if p >= 0.10:
            return "watch"
        return "stable"

    records = []
    for f in features:
        p = psi(reference[f].values, current[f].values)
        k = ks_stat(reference[f].values, current[f].values)
        shift = current[f].mean() - reference[f].mean()
        records.append({"feature": f, "psi": round(p, 3), "ks": round(k, 3),
                        "mean_shift": round(shift, 2), "flag": band(p)})

    report = pd.DataFrame(records).sort_values("psi", ascending=False).reset_index(drop=True)
    report
    return band, f, k, p, records, report, shift


@app.cell
def __(mo, report):
    drifting = report[report["flag"] == "drift"]["feature"].tolist()
    watching = report[report["flag"] == "watch"]["feature"].tolist()
    mo.md(
        f"""
        ## Flag table summary

        - **Drift (PSI > 0.25):** {', '.join(f'`{x}`' for x in drifting) or 'none'}
        - **Watch (0.10–0.25):** {', '.join(f'`{x}`' for x in watching) or 'none'}
        - Everything else is within tolerance.
        """
    )
    return drifting, watching


@app.cell
def __(plt, report):
    # PSI bar chart with the decision bands drawn in.
    fig, ax = plt.subplots(figsize=(8, 3.2))
    colors = {"drift": "#C44E52", "watch": "#DD8452", "stable": "#55A868"}
    ax.bar(report["feature"], report["psi"], color=[colors[f] for f in report["flag"]])
    ax.axhline(0.10, color="grey", ls=":", lw=1)
    ax.axhline(0.25, color="black", ls="--", lw=1)
    ax.set_ylabel("PSI")
    ax.set_title("Population Stability Index by feature")
    ax.tick_params(axis="x", rotation=30)
    fig
    return ax, colors, fig


@app.cell
def __(current, plt, reference, report):
    # Overlay reference vs current histograms for the top-drift feature.
    top_feat = report.iloc[0]["feature"]
    fig2, ax2 = plt.subplots(figsize=(8, 3.2))
    ax2.hist(reference[top_feat], bins=30, density=True, alpha=0.5, label="reference")
    ax2.hist(current[top_feat], bins=30, density=True, alpha=0.5, label="current")
    ax2.legend()
    ax2.set_title(f"Distribution shift — {top_feat}")
    ax2.set_xlabel(top_feat)
    fig2
    return ax2, fig2, top_feat


@app.cell
def __(mo, report):
    sensitivity = mo.ui.slider(
        start=0.05, stop=0.40, value=0.25, step=0.01,
        label="PSI alert threshold",
    )
    sensitivity
    return sensitivity,


@app.cell
def __(mo, report, sensitivity):
    alerts = report[report["psi"] > sensitivity.value]["feature"].tolist()
    mo.md(
        f"""
        ## Alert tuning

        At a PSI threshold of **{sensitivity.value:.2f}**, the monitor would page on
        **{len(alerts)}** feature(s): {', '.join(f'`{x}`' for x in alerts) or 'none'}.

        Lowering the threshold catches drift earlier but increases noise; 0.25 is
        the conventional production default.
        """
    )
    return alerts,


@app.cell
def __(mo, report, top_feat):
    mo.md(
        f"""
        ## Takeaway

        The strongest drift is in **`{top_feat}`** (PSI {report.iloc[0]['psi']}),
        consistent with a shift in the acquisition mix rather than an ETL bug.
        Recommended next steps: retrain on a recent production window, A/B the
        retrained model against the frozen one on a holdout, and wire the PSI
        threshold above into automated alerting.
        """
    )
    return


if __name__ == "__main__":
    app.run()
