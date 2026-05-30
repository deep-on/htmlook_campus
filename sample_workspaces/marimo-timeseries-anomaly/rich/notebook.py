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
        # Time-series Anomaly Detection

        Hourly **requests-per-minute** for an API service over 30 days. The series
        has a daily shape and a weekend lift. We detrend with a rolling baseline,
        score each point with a rolling **z-score**, cross-check with an **IQR**
        rule, and mark points that both methods agree are anomalous.

        Data is synthetic so it runs anywhere — replace the generator with
        `pd.read_csv("metrics.csv", parse_dates=["ts"])` to use your own metric.
        """
    )
    return


@app.cell
def __(np, pd):
    # 30 days × 24 hours of rpm: daily sinusoid + weekend lift + noise, with a
    # few injected anomalies (a spike, a sustained outage dip, and a blip).
    rng = np.random.default_rng(31)
    idx = pd.date_range("2026-04-01", periods=30 * 24, freq="h")
    hour = idx.hour.values
    dow = idx.dayofweek.values

    daily = 480 + 140 * np.sin((hour - 9) / 24 * 2 * np.pi)
    weekend = np.where(dow >= 5, 90, 0)
    noise = rng.normal(0, 18, len(idx))
    rpm = np.clip(daily + weekend + noise, 0, None)

    # Injected anomalies.
    rpm[18 * 24 + 14] += 950          # day-19 14:00 traffic spike
    rpm[22 * 24 + 3:22 * 24 + 6] = 8  # day-23 03:00–05:00 outage dip
    rpm[26 * 24 + 21] += 520          # day-27 21:00 blip

    series = pd.DataFrame({"rpm": rpm.round(1)}, index=idx)
    series.tail()
    return daily, dow, hour, idx, noise, rng, rpm, series, weekend


@app.cell
def __(mo, series):
    mo.md(
        f"""
        **{len(series):,} hourly points** ·
        mean **{series['rpm'].mean():.0f}** rpm ·
        min **{series['rpm'].min():.0f}** · max **{series['rpm'].max():.0f}**.
        """
    )
    return


@app.cell
def __(plt, series):
    fig, ax = plt.subplots(figsize=(9, 3))
    ax.plot(series.index, series["rpm"], lw=0.7)
    ax.set_title("Raw requests-per-minute (hourly)")
    ax.set_ylabel("rpm")
    fig
    return ax, fig


@app.cell
def __(series):
    # Deseasonalize first: a centered 24h window mixes the whole daily cycle into
    # any baseline, so subtract an hour-of-day median profile and detect on the
    # residual instead. The median profile resists the injected anomalies.
    hod = series.index.hour
    profile = series["rpm"].groupby(hod).median()
    baseline = series.index.hour.map(profile.to_dict())
    resid = series["rpm"].values - baseline.values
    stats = series.assign(baseline=baseline.round(1), resid=resid.round(1))
    stats.head()
    return baseline, hod, profile, resid, stats


@app.cell
def __(np, stats):
    # Robust z-score on the residual: median-centered, MAD-scaled. 1.4826 makes
    # MAD a consistent estimator of std for normal data, so |z| reads like sigmas.
    r = stats["resid"]
    center = r.median()
    mad = (r - center).abs().median()
    scale = 1.4826 * mad
    z = (r - center) / scale
    stats_z = stats.assign(z=z.round(2))
    stats_z[["rpm", "baseline", "resid", "z"]].head()
    return center, mad, r, scale, stats_z, z


@app.cell
def __(stats_z):
    # IQR rule on the same residual, as an independent second opinion.
    q1 = stats_z["resid"].quantile(0.25)
    q3 = stats_z["resid"].quantile(0.75)
    iqr = q3 - q1
    low_fence = q1 - 1.5 * iqr
    high_fence = q3 + 1.5 * iqr
    (round(q1, 1), round(q3, 1), round(low_fence, 1), round(high_fence, 1))
    return high_fence, iqr, low_fence, q1, q3


@app.cell
def __(high_fence, low_fence, stats_z):
    z_thresh = 3.5
    flagged = stats_z.copy()
    flagged["z_anom"] = flagged["z"].abs() > z_thresh
    flagged["iqr_anom"] = (flagged["resid"] < low_fence) | (flagged["resid"] > high_fence)
    # Confirmed = both methods agree.
    flagged["anomaly"] = flagged["z_anom"] & flagged["iqr_anom"]
    anomalies = flagged[flagged["anomaly"]].copy()
    anomalies["direction"] = ["spike" if zz > 0 else "drop" for zz in anomalies["z"]]
    anomalies[["rpm", "baseline", "resid", "z", "direction"]]
    return anomalies, flagged, z_thresh


@app.cell
def __(anomalies, mo, z_thresh):
    n_spike = int((anomalies["direction"] == "spike").sum())
    n_drop = int((anomalies["direction"] == "drop").sum())
    mo.md(
        f"""
        ## Anomaly flag table

        Confirmed by **both** the rolling z-score (|z| > {z_thresh}) **and** the IQR
        fence: **{len(anomalies)} points** — {n_spike} spike(s), {n_drop} drop(s).
        Requiring agreement between two independent methods keeps false positives
        from ordinary daily peaks low.
        """
    )
    return n_drop, n_spike


@app.cell
def __(anomalies, plt, series):
    fig2, ax2 = plt.subplots(figsize=(9, 3))
    ax2.plot(series.index, series["rpm"], lw=0.7, label="rpm", zorder=1)
    spikes = anomalies[anomalies["direction"] == "spike"]
    drops = anomalies[anomalies["direction"] == "drop"]
    ax2.scatter(spikes.index, spikes["rpm"], color="#C44E52", s=40, label="spike", zorder=3)
    ax2.scatter(drops.index, drops["rpm"], color="#8172B3", s=40, label="drop", zorder=3)
    ax2.legend()
    ax2.set_title("Detected anomalies")
    ax2.set_ylabel("rpm")
    fig2
    return ax2, drops, fig2, spikes


@app.cell
def __(mo):
    sensitivity = mo.ui.slider(
        start=2.0, stop=5.0, value=3.5, step=0.1,
        label="z-score threshold",
    )
    sensitivity
    return sensitivity,


@app.cell
def __(high_fence, low_fence, mo, sensitivity, stats_z):
    count = int(
        ((stats_z["z"].abs() > sensitivity.value)
         & ((stats_z["resid"] < low_fence) | (stats_z["resid"] > high_fence))).sum()
    )
    mo.md(
        f"""
        ## Sensitivity tuning

        At a z-score threshold of **{sensitivity.value:.1f}**, the detector confirms
        **{count}** anomalies. Lowering it surfaces subtler deviations at the cost
        of more pages during normal peak hours; 3.5 balances recall and noise for
        ops metrics.
        """
    )
    return count,


@app.cell
def __(anomalies, mo):
    worst = anomalies.loc[anomalies["z"].abs().idxmax()]
    when = worst.name.strftime("%Y-%m-%d %H:%M")
    mo.md(
        f"""
        ## Takeaway

        The most extreme event was a **{worst['direction']}** at **{when}**
        ({worst['rpm']:.0f} rpm vs an hour-of-day baseline of {worst['baseline']:.0f}).
        Deseasonalizing first, then requiring two methods to agree, keeps ordinary
        daily peaks quiet while still catching the spike and the outage dip. Route
        the flag table above into your alerting pipeline.
        """
    )
    return when, worst


if __name__ == "__main__":
    app.run()
