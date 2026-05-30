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
        # Harborline Retail · SKU Demand Forecast

        A 14-day demand forecast for the top SKUs, built on a seasonal
        moving-average baseline. The data here is synthetic so the notebook
        runs anywhere — swap in `sales.csv` to use your own.
        """
    )
    return


@app.cell
def __(np, pd):
    # Synthetic 180 days of daily units for one SKU: weekly seasonality,
    # mild upward trend, and noise.
    rng = np.random.default_rng(7)
    days = pd.date_range("2025-12-01", periods=180, freq="D")
    weekly = 12 + 6 * np.sin(np.arange(180) * 2 * np.pi / 7)
    trend = np.linspace(0, 8, 180)
    noise = rng.normal(0, 2.0, 180)
    units = np.clip(weekly + trend + noise, 0, None).round()
    sales = pd.DataFrame({"date": days, "units": units}).set_index("date")
    sales.tail()
    return days, noise, rng, sales, trend, units, weekly


@app.cell
def __(mo, sales):
    mo.md(
        f"""
        **{len(sales)} days** of history ·
        mean **{sales['units'].mean():.1f}** units/day ·
        peak **{int(sales['units'].max())}**.
        """
    )
    return


@app.cell
def __(plt, sales):
    fig, ax = plt.subplots(figsize=(8, 3))
    ax.plot(sales.index, sales["units"], lw=1)
    ax.set_title("Daily units sold")
    ax.set_ylabel("units")
    fig
    return ax, fig


@app.cell
def __(np, pd, sales):
    # Seasonal-naive + moving-average blend: for each future day, average the
    # last 4 same-weekday observations and nudge by the recent 7-day trend.
    horizon = 14
    history = sales["units"]
    last_date = history.index[-1]

    def forecast_day(target_date):
        wd = target_date.weekday()
        same_wd = history[history.index.weekday == wd]
        base = same_wd.tail(4).mean()
        recent_trend = history.tail(7).mean() - history.tail(14).head(7).mean()
        return max(base + recent_trend / 2, 0)

    future_idx = pd.date_range(last_date + pd.Timedelta(days=1), periods=horizon)
    preds = [forecast_day(d) for d in future_idx]
    forecast = pd.Series(preds, index=future_idx, name="forecast").round(1)
    forecast
    return forecast, forecast_day, future_idx, history, horizon, last_date


@app.cell
def __(forecast, plt, sales):
    fig2, ax2 = plt.subplots(figsize=(8, 3))
    ax2.plot(sales.index[-30:], sales["units"].tail(30), label="actual", lw=1)
    ax2.plot(forecast.index, forecast.values, label="forecast", lw=2, ls="--")
    ax2.axvline(sales.index[-1], color="grey", alpha=0.3)
    ax2.legend()
    ax2.set_title("Last 30 days + 14-day forecast")
    fig2
    return ax2, fig2


@app.cell
def __(forecast, mo):
    mo.md(
        f"""
        ## Takeaway

        Projected 14-day demand: **{forecast.sum():.0f} units**
        (avg **{forecast.mean():.1f}**/day). Use this to set the reorder
        point; widen safety stock on the weekend peaks.
        """
    )
    return


if __name__ == "__main__":
    app.run()
