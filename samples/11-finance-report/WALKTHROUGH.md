# 11 · finance-report — EBITDA B14 cite + CFO brief

> 영상: `demo/persona_units/finance-report/renders/finance-report_voiced_bgm.en+ko.mp4`

Q3 P&L xlsx 의 EBITDA 셀 (B14 plan, C14 actual) 을 cite 해서 CFO brief 한
단락을 작성. 모든 숫자는 `xlsx://q3.xlsx#cell` 인라인 anchor 로 역추적.

## 사전 준비

- HTMLook Pro
- (선택) LLM
- `q3.xlsx` 는 openpyxl 로 미리 생성됨 (Plan / Actual / Variance, EBITDA at row 14)

## 단계

### 1. [VIEW] 좌측 q3.xlsx, 우측 brief.md

- 좌측: `11-finance-report/q3.xlsx` (HTMLook xlsx 뷰어)
- 우측: `11-finance-report/brief.md` (Headline / Variances / Actions 비어 있음)

### 2. [AI] EBITDA 셀 cite + variance 계산

좌측 xlsx 에서 B14 (plan) 셀 클릭, 그 다음 C14 (actual) 셀까지 드래그-선택.

LLM 에:

> *"EBITDA plan vs actual variance 를 계산하고 우측 brief 의 Headline 에 한
> 단락으로 작성. 모든 숫자는 셀 anchor 인라인 링크로."*

LLM 이:
1. `htmlook_cite` 로 B14, C14 anchor 확보
2. variance = (34.6 - 31.0) / 31.0 = +11.6%
3. `htmlook_apply_edit` 로 Headline 영역 patch — `[$34.6M](xlsx://q3.xlsx#C14)` 형식

### 3. [AI] Revenue 행 추가 (row 6)

> *"Revenue 행 (B6/C6) 도 같은 형식으로 추가."*

→ Headline 두번째 문장 + Variances tracked 두번째 줄 patch.

### 4. [AI] G&A 행 추가 (row 11)

→ Variances tracked 세번째 줄 + Actions 1-3.

### 5. [VIEW] 우측 reload

- Headline 한 단락에 EBITDA / Revenue / G&A 모든 숫자가 anchor 링크로 표시됨
- Variances 체크박스 3 개 모두 채워짐
- Actions 1-3 추가됨
- Sign-off 라인 *"J. Han, CFO · 2026-04-30"*

### 6. [AI 없는 사용자] before/after 비교

- 좌측: `11-finance-report/before/brief.md`
- 우측: `11-finance-report/after/brief.md`

## 검증 포인트

- ✅ `htmlook_pane_pair` (xlsx + md)
- ✅ `htmlook_cite` (셀 anchor — B14, C14, B6, C6, B11, C11)
- ✅ `htmlook_apply_edit` (Headline + Variances + Actions multi-region)
- ✅ 인라인 cite anchor: `[$34.6M](xlsx://q3.xlsx#C14)` 형식 보존

## 다음 페르소나

`12-press-editor/` — 인터뷰 transcript 14:14 quote → 잡지 paragraph
