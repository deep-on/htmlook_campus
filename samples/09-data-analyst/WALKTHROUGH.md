# 09 · data-analyst — SQL cite + chart redraw

> 영상: `demo/persona_units/data-analyst/renders/data-analyst_voiced_bgm.en+ko.mp4`

좌측에 SQL, 우측에 차트. cite 한 컬럼만 바꿔서 차트가 바로 redraw, 이상치
한 행 가중평균으로 묽히기.

## 사전 준비

- HTMLook Pro
- (선택) LLM
- 차트는 정적 SVG (`chart.svg`) — HTMLook 은 SQL 실행 엔진이 아닙니다.
  실제 데이터 fetch + 차트 redraw 는 외부 BI 도구가 처리한다고 가정.

## 단계

### 1. [VIEW] 좌측 SQL, 우측 chart.svg

- 좌측: `09-data-analyst/query.sql` (단일 series, MRR total 만)
- 우측: `09-data-analyst/chart.svg` (파란 라인 1 개)

### 2. [AI] 컬럼 cite + tier 별 분해

좌측 SQL 의 `SUM(monthly_recurring_revenue)` 영역을 드래그-선택.

LLM 에:

> *"이 컬럼을 tier 별로 분해해줘. SELECT 에 tier 추가, GROUP BY 에 tier 추가,
> 그 다음 chart.svg 도 3 series 로 다시 그려."*

LLM 이:
1. `htmlook_selection_text` 로 SQL 영역 anchor
2. SQL 수정: GROUP BY 1, 2 추가
3. `htmlook_apply_edit` 두 번 — query.sql + chart.svg

### 3. [VIEW] 우측 reload

- chart.svg 가 3 series (Enterprise / Pro / Starter) 로 redraw

### 4. [AI] 이상치 가중평균

> *"한 row 에 enterprise spike 가 있어. ACV 로 weighted average 처리해서
> spike 를 묽혀줘."*

LLM 이 query.sql 에 `SUM(mrr * acv) / SUM(acv)` 가중평균 식 추가, chart.svg
에서 spike 가 평탄해진 라인으로 다시 그림.

### 5. [VIEW] 우측 reload + 인사이트

- 차트 부제: *"+18% MoM weighted, driven by Enterprise."*

### 6. [AI 없는 사용자] before/after 비교

- 좌측: `09-data-analyst/before/query.sql` + `before/chart.svg`
- 우측: `09-data-analyst/after/query.sql` + `after/chart.svg`

## 검증 포인트

- ✅ `htmlook_pane_pair` (SQL + SVG)
- ✅ `htmlook_selection_text` (SQL 컬럼)
- ✅ `htmlook_apply_edit` (query + chart 동시)
- ⚠️ HTMLook 은 SQL 을 실행하지 않습니다. 실제 redraw 는 외부 BI 도구의
  결과를 SVG 로 갈아 끼우는 흐름입니다.

## 다음 페르소나

`10-research-notes/` — 논문 PDF cite + 노트 + bibliography
