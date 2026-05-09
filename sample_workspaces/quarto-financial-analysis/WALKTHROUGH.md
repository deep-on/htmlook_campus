# DCF Valuation Walkthrough · 30-min Walkthrough

> 🌟 **Wave A · High Quality** — 마케팅 / 데모 자산. 직접 demo recording 가능.

## 1. 환경 설정
1. `quarto preview index.qmd` → http://localhost:4848
2. HTMLook 에서 워크스페이스 열기

## 2. xlsx_cite 시그니처 데모 (90초)
1. `data/financial_model.csv` 의 Y3 EBITDA 셀 선택 (현재 3.8)
2. HTMLook AI: "이 셀이 본문 어디에서 cite 되는지 표시"
3. AI 가 본문의 "**Y3 EBITDA: $3.8M**" 자동 highlight
4. 셀을 5.0 으로 변경 + Save
5. 본문이 자동 갱신 — Y3 행 + Sensitivity table 모두

## 3. Multi-target apply_edit
1. AI Chat: "Acme → MyCompany 로 모든 sections 일괄 변경"
2. AI 가 5 sections 동시 수정

## 4. PDF 출력
- `quarto render index.qmd --to pdf`
- TinyTeX 자동 설치, 1분 소요
