<!-- Wave A · High Quality -->
# Quarto · DCF Valuation Report ⭐

5분 walkthrough 가능한 가상 SaaS (Acme · Series B) 의 5년 DCF 모델 + 본문이 xlsx 셀을 cite 해서 데이터 변경 시 prose 자동 갱신.

## 시드 콘텐츠

- `index.qmd` — Executive summary + DCF 본문 + 민감도 분석 6 sections
- `_quarto.yml` — HTML + PDF 양 format
- `data/financial_model.csv` — 5년 가정 (revenue / margin / WACC / terminal)
- `references.bib` — Damodaran / McKinsey 인용

## 빠르게 시작

```bash
quarto preview index.qmd        # http://localhost:4848 live
quarto render index.qmd --to pdf
```

## HTMLook 활용

- **xlsx_cite ⭐**: financial_model.csv 의 셀을 본문에서 cite. 셀 변경 → 본문 EBITDA / EV 자동 갱신.
- **Multi-target apply_edit**: 여러 sections 의 동일 회사명 일괄 변경 (Acme → 자기 회사).
- **Pane pair**: 좌 .qmd ↔ 우 quarto preview (localhost:4848).

## 외부 의존

- Quarto CLI · TinyTeX (PDF) · 한글 폰트 (Pretendard 권장)

## 데이터 swap

`data/financial_model.csv` 만 자기 회사 숫자로 교체 → render. WACC 는 default 8.5%, terminal growth 2%.
