# Marimo Profile

Reactive Python notebook [Marimo](https://marimo.io) HTMLook Profile.

## 시작

```bash
pip install marimo polars
marimo edit notebook.py   # http://localhost:2718
```

## HTMLook 활용

- **Pane pair**: 좌 `.py` ↔ 우 live notebook.
- **xlsx_cite**: `pl.read_excel()` 결과 ↔ 원본 xlsx 양방향 cite.
- **Multi-target apply_edit**: 여러 notebook 의 preprocessing 일괄 수정.

## 외부 의존

- Python 3.10+
- Marimo (Apache-2.0)
- 데이터 lib (Polars / Pandas / NumPy 등 자유)

## 라이선스

본 Profile = MIT (deep-on). Marimo = Apache-2.0.
