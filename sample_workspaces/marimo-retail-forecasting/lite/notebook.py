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

    14-day demand forecast for the top 100 SKUs at Harborline Retail ·
    Holt-Winters seasonal blended with intermittent-demand handling.""")
    return

if __name__ == "__main__":
    app.run()
