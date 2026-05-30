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
        # Product Funnel · Weekly Signup Conversion

        A 5-stage acquisition funnel — **signup → verify → activate → D7 → D30** —
        broken down by acquisition channel. The data is synthetic so the notebook
        runs anywhere; swap in `events.csv` to use your own cohort.

        Goal: find the largest leak, then size the revenue impact of fixing it.
        """
    )
    return


@app.cell
def __(np, pd):
    # Synthetic weekly cohort: 10k signups split across 3 channels, each with
    # its own per-stage pass-through rate. We model users, not rates, so the
    # channel mix falls out naturally.
    rng = np.random.default_rng(11)
    stages = ["signup", "verify", "activate", "D7", "D30"]

    # Per-channel stage pass-through probabilities (signup is the entry = 1.0).
    channel_rates = {
        "paid_search": [1.00, 0.86, 0.58, 0.66, 0.61],
        "organic":     [1.00, 0.81, 0.64, 0.70, 0.64],
        "referral":    [1.00, 0.90, 0.71, 0.74, 0.69],
    }
    channel_signups = {"paid_search": 5200, "organic": 3300, "referral": 1500}

    rows = []
    for ch, n0 in channel_signups.items():
        counts = [n0]
        for p in channel_rates[ch][1:]:
            counts.append(int(rng.binomial(counts[-1], p)))
        for stage, c in zip(stages, counts):
            rows.append({"channel": ch, "stage": stage, "users": c})

    events = pd.DataFrame(rows)
    funnel = (
        events.groupby("stage")["users"].sum()
        .reindex(stages)
        .rename("users")
        .to_frame()
    )
    funnel["step_conv"] = (funnel["users"] / funnel["users"].shift(1)).fillna(1.0)
    funnel["overall"] = funnel["users"] / funnel["users"].iloc[0]
    funnel
    return channel_rates, channel_signups, ch, counts, events, funnel, n0, p, rng, rows, stages


@app.cell
def __(funnel, mo):
    top = funnel["users"].iloc[0]
    bottom = funnel["users"].iloc[-1]
    mo.md(
        f"""
        **{top:,} signups** entering the funnel ·
        **{bottom:,}** still retained at D30 ·
        end-to-end conversion **{bottom / top * 100:.1f}%**.
        """
    )
    return bottom, top


@app.cell
def __(funnel, plt, stages):
    # Classic funnel bar chart: width ∝ users at each stage, centered.
    fig, ax = plt.subplots(figsize=(8, 3.5))
    widths = funnel["users"].values
    y = range(len(stages))
    left = (widths.max() - widths) / 2
    ax.barh(y, widths, left=left, color="#4C72B0")
    ax.set_yticks(list(y))
    ax.set_yticklabels(stages)
    ax.invert_yaxis()
    for i, w in enumerate(widths):
        ax.text(widths.max() / 2, i, f"{int(w):,}", ha="center", va="center", color="white")
    ax.set_title("Acquisition funnel — users per stage")
    ax.set_xticks([])
    fig
    return ax, fig, i, left, w, widths, y


@app.cell
def __(funnel, pd, stages):
    # Drop-off ranking: which transition loses the most users (absolute + %).
    drops = []
    for prev, cur in zip(stages[:-1], stages[1:]):
        lost = int(funnel.loc[prev, "users"] - funnel.loc[cur, "users"])
        pct = lost / funnel.loc[prev, "users"]
        drops.append({"transition": f"{prev} → {cur}", "users_lost": lost, "drop_rate": pct})
    dropoff = pd.DataFrame(drops).sort_values("users_lost", ascending=False).reset_index(drop=True)
    dropoff
    return cur, dropoff, drops, lost, pct, prev


@app.cell
def __(dropoff, mo):
    worst = dropoff.iloc[0]
    mo.md(
        f"""
        ## Largest leak

        The **{worst['transition']}** step loses **{worst['users_lost']:,} users**
        ({worst['drop_rate'] * 100:.0f}% drop) — the single biggest opportunity.
        A common cause at activation is a long first-run setup; shortening it
        typically recovers a chunk of this leak.
        """
    )
    return worst,


@app.cell
def __(channel_rates, channel_signups, pd, stages):
    # Segment comparison: end-to-end conversion by channel.
    seg_rows = []
    for ch_name, rates in channel_rates.items():
        overall = 1.0
        for r in rates[1:]:
            overall *= r
        seg_rows.append(
            {
                "channel": ch_name,
                "signups": channel_signups[ch_name],
                "activate_conv": rates[2],
                "end_to_end": overall,
            }
        )
    segments = pd.DataFrame(seg_rows).sort_values("end_to_end", ascending=False).reset_index(drop=True)
    segments
    return ch_name, overall, r, rates, seg_rows, segments


@app.cell
def __(plt, segments):
    fig2, ax2 = plt.subplots(figsize=(8, 3))
    ax2.bar(segments["channel"], segments["end_to_end"] * 100, color="#55A868")
    for x, v in enumerate(segments["end_to_end"] * 100):
        ax2.text(x, v + 0.3, f"{v:.1f}%", ha="center")
    ax2.set_ylabel("end-to-end conversion %")
    ax2.set_title("Signup → D30 conversion by channel")
    fig2
    return ax2, fig2, v, x


@app.cell
def __(funnel, mo):
    uplift = mo.ui.slider(
        start=0.0, stop=0.30, value=0.15, step=0.01,
        label="activate step uplift (Δ pass-through)",
    )
    baseline_d30 = int(funnel["users"].iloc[-1])
    mo.md(f"Baseline D30 retained = **{baseline_d30:,}** users. Drag to simulate.")
    uplift
    return baseline_d30, uplift


@app.cell
def __(baseline_d30, funnel, mo, uplift):
    # Re-flow the funnel from 'activate' with the uplifted pass-through, holding
    # the downstream D7/D30 rates fixed.
    verify_users = funnel["users"].iloc[1]
    new_activate_rate = min(funnel["step_conv"].iloc[2] + uplift.value, 0.99)
    new_activate = verify_users * new_activate_rate
    new_d30 = new_activate * funnel["step_conv"].iloc[3] * funnel["step_conv"].iloc[4]
    delta = new_d30 - baseline_d30
    arpu = 40  # synthetic $/user/year
    mo.md(
        f"""
        ## Uplift simulator

        With an activate uplift of **+{uplift.value:.2f}**, projected D30 retained
        users rise to **{new_d30:,.0f}** (vs {baseline_d30:,} baseline,
        **+{delta:,.0f}**, **{delta / baseline_d30 * 100:.0f}% lift**).

        At a synthetic **${arpu}/user/yr**, that is ≈ **${delta * arpu / 1000:,.0f}k**
        of annualized retained revenue.
        """
    )
    return arpu, delta, new_activate, new_activate_rate, new_d30, verify_users


@app.cell
def __(dropoff, mo, segments):
    best_ch = segments.iloc[0]["channel"]
    leak = dropoff.iloc[0]["transition"]
    mo.md(
        f"""
        ## Takeaway

        The funnel's biggest leak is **{leak}** — fix activation first.
        **{best_ch}** is the strongest-converting channel end-to-end, so shifting
        budget toward it compounds with any activation win. Use the simulator
        above to set a target uplift and translate it into a revenue goal.
        """
    )
    return best_ch, leak


if __name__ == "__main__":
    app.run()
