# Bayesian Pricing Walkthrough · 30-min Walkthrough

> 🌟 **Wave A · High Quality** — 마케팅 / 데모 자산. 직접 demo recording 가능.

## 1. PyMC 환경
```bash
pip install marimo polars pymc arviz
marimo edit notebook.py
```

## 2. Posterior 시각화
1. ROPE width 슬라이더 = $0.5 → $1.0
2. P(best=$49) 자동 재계산
3. ROPE 표 즉시 갱신

## 3. 시그니처
- Marimo only — Jupyter 는 reactive 안 됨, 슬라이더 변경 시 셀 수동 재실행 필요
