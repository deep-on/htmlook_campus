---
name: marimo
description: Reactive Python notebook (Marimo). Cell 의존성 자동 추적, .py-native 저장.
---

# Marimo 워크플로우

Jupyter 후속격 — 노트북이 그냥 `.py` 파일이라 git diff / Black 가능. Cell 변경 → 의존 cell 자동 재실행.

## 발견 신호

- `.py` 파일 안에 `import marimo as mo` + `app = mo.App()` 패턴
- 셀 = `@app.cell` 로 데코레이트된 함수
- `pyproject.toml` 또는 `requirements.txt` 에 `marimo`

## 작업 패턴

1. **edit 모드**: `marimo edit notebook.py` → http://localhost:2718 (live HMR)
2. **run 모드**: `marimo run notebook.py` (script 실행 — 인터랙티브 X)
3. **view 모드**: `marimo run notebook.py --headless` (CI 등)
4. **HTML 내보내기**: `marimo export html notebook.py --output report.html` (정적)

## 셀 패턴

```python
@app.cell
def __():
    import polars as pl
    import marimo as mo
    return mo, pl

@app.cell
def __(pl):
    df = pl.read_csv("data.csv")
    return (df,)

@app.cell
def __(df, mo):
    mo.ui.table(df)   # 인터랙티브 테이블 — 의존 셀 자동 갱신
    return
```

## HTMLook 시그니처 활용

- **Pane pair**: 좌 `.py` 편집 ↔ 우 marimo live (localhost:2718).
- **xlsx_cite**: `pl.read_excel(...)` 결과 셀 ↔ 원본 xlsx — AI 가 코멘트 셀에 인사이트 작성.
- **Multi-target apply_edit**: 여러 노트북에서 같은 import / preprocessing 일괄 수정.

## 주의

- Marimo 는 `.ipynb` 직접 못 열음 — `marimo convert notebook.ipynb` 으로 마이그레이션.
- 셀 사이 변수 이름 충돌 시 빨간 경고 — 의존성 그래프가 명시적이라 그렇.
- pip 설치는 시스템 Python 또는 venv 어디든 OK, conda 는 환경 격리 잘 작동.

## 참조

- 공식: https://marimo.io
- GitHub: https://github.com/marimo-team/marimo (Apache-2.0)
- 라이선스: 본 Profile = MIT, Marimo = Apache-2.0
