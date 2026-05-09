import marimo as mo
__generated_with = "0.10.0"
app = mo.App()

@app.cell
def __():
    import marimo as mo
    return mo,

@app.cell
def __(mo):
    mo.md("""# Retail · SKU Demand Forecast

    Top 100 SKU 의 14-day forecast · Holt-Winters seasonal × intermittent.""")
    return

if __name__ == "__main__":
    app.run()
