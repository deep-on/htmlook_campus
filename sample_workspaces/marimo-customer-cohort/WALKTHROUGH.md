# Cohort Retention Walkthrough · 30-min Walkthrough

> 🌟 **Wave A · High Quality** — 마케팅 / 데모 자산. 직접 demo recording 가능.

## 1. 노트북 실행
1. `pip install marimo polars plotly`
2. `marimo edit notebook.py` → http://localhost:2718

## 2. Reactive 슬라이더 데모
1. cohort_window 슬라이더 = 4 → 6 으로 변경
2. heatmap 자동 재계산 (sub-second)
3. 가설 검증 cell 의 +10pp / +19pp 숫자 자동 갱신

## 3. HTMLook pane pair
1. 좌: notebook.py 편집
2. 우: marimo localhost:2718 iframe (자동 새로고침)
3. 라인 cite: 특정 cell 라인 → AI 에게 "왜 이렇게 계산?"

## 4. 결과 export
- `marimo export html notebook.py --output report.html`
