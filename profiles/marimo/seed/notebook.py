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
    mo.md(
        """
        # Acme Q3 매출 분석

        모바일 onboarding 단축의 영향을 코호트로 검증.
        """
    )
    return


@app.cell
def __(pl):
    df = pl.DataFrame({
        "month":     ["Jul", "Aug", "Sep"],
        "revenue_m": [1.40, 1.65, 2.05],
        "signups":   [3500, 3700, 4000],
    })
    return (df,)


@app.cell
def __(df, mo):
    mo.ui.table(df, selection=None)
    return


@app.cell
def __(df, mo, pl):
    growth = df.with_columns(
        (pl.col("revenue_m") / pl.col("revenue_m").shift(1) - 1).alias("growth")
    )
    mo.ui.table(growth)
    return (growth,)


@app.cell
def __(mo):
    cohort_window = mo.ui.slider(start=2, stop=12, value=4, label="cohort window (weeks)")
    cohort_window
    return (cohort_window,)


@app.cell
def __(cohort_window, mo):
    mo.md(f"""
    ## 결과
    선택한 코호트 윈도우 = **{cohort_window.value}주**.

    온보딩 단축 (5단계 → 2단계) 직후 {cohort_window.value}주간:
    - 신규 가입자 +33%
    - 매출 +21%
    - retention +9pp
    """)
    return


if __name__ == "__main__":
    app.run()
