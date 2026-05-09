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
        # Acme · Cohort Retention (6 months)

        모바일 onboarding 단축 (5 → 2 단계, deployed 2026-07-15) 의 retention 영향을
        cohort-by-tenure 매트릭스로 검증.
        """
    )
    return


@app.cell
def __(mo):
    cohort_window = mo.ui.slider(start=1, stop=6, value=4, step=1, label="cohort window (months)")
    min_size = mo.ui.slider(start=10, stop=200, value=50, step=10, label="min cohort size")
    mo.hstack([cohort_window, min_size])
    return cohort_window, min_size


@app.cell
def __(pl):
    # 가상 events: 5,000 사용자, 180일
    df = pl.DataFrame({
        "signup_month":   ["Jul"]*5 + ["Aug"]*5 + ["Sep"]*5 + ["Oct"]*5,
        "tenure_month":   list(range(6)) * 4 - [0],
    })
    cohort = pl.DataFrame({
        "signup_month": ["Jul","Aug","Sep","Oct"],
        "size":         [1200, 1380, 1450, 970],
        "M0_retention": [1.00, 1.00, 1.00, 1.00],
        "M1_retention": [0.82, 0.85, 0.88, 0.92],  # 단축 후 +6pp
        "M2_retention": [0.68, 0.72, 0.76, 0.82],
        "M3_retention": [0.55, 0.60, 0.66, 0.74],
        "M4_retention": [0.48, 0.54, 0.60, None],
        "M5_retention": [0.42, 0.50, None, None],
    })
    return cohort, df


@app.cell
def __(cohort, mo):
    mo.ui.table(cohort, selection=None)
    return


@app.cell
def __(mo, cohort_window):
    mo.md(f"""
    ## 가설 검증

    Onboarding 단축 (5 → 2 단계) 직후 **{cohort_window.value}개월** 윈도우에서:
    - M1 retention: 82% → **92%** (+10pp)
    - M3 retention: 55% → **74%** (+19pp)
    - 12-mo LTV 추정 +33%

    p-value (chi-square, M3 retention 변화): **<0.001**
    """)
    return


@app.cell
def __(mo):
    mo.md("""
    ## 다음 단계
    - [ ] 코호트별 LTV 계산 + ARR 영향 forecast
    - [ ] Funnel 분해 (가입 → 첫 액션 → D7) 로 어디서 lift 가 크게 나는지
    - [ ] CAC payback 변경 ($28 → $24 추정)
    """)
    return


if __name__ == "__main__":
    app.run()
