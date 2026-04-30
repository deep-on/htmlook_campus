# 08 · legal-redline — 4 조항 cite + redline memo

> 영상: `demo/persona_units/legal-redline/renders/legal-redline_voiced_bgm.en+ko.mp4`

MSA (Master Services Agreement) 의 4 조항 (1.1 / 2.3 / 5.2 / 7.1) 을 PDF 에서
한 행씩 cite 해서 redline memo 를 채우고 deal-breaker 한 개 식별.

## 사전 준비

- HTMLook Pro
- (선택) LLM
- `contract.pdf` 는 reportlab 으로 미리 생성됨 (4 조항 1페이지)

## 단계

### 1. [VIEW] 좌측 contract.pdf, 우측 memo.md

- 좌측: `08-legal-redline/contract.pdf`
- 우측: `08-legal-redline/memo.md`
- memo 의 표는 risk/stance/counter language 가 모두 비어 있음

### 2. [AI] 1.1 cite + 등급화

좌측 PDF 에서 clause 1.1 영역 드래그-선택.

LLM 에:

> *"이 조항을 grade (low/medium/high) 와 stance (accept/counter/reject) 로
> 평가해서 우측 memo 의 1.1 행에 채워줘. counter language 가 필요하면 작성."*

LLM 이:
1. `htmlook_selection_text` 로 PDF 텍스트 확보
2. 등급 결정 (1.1 → LOW, accept as drafted)
3. `htmlook_apply_edit` 로 memo.md 의 1.1 행 patch

### 3. [AI] 2.3 / 5.2 / 7.1 — 같은 패턴

각 조항을 차례로 cite. 영상의 등급:

- 2.3 → **HIGH** (3 month liability cap — deal-breaker), counter 12 month
- 5.2 → MEDIUM (5년 confidentiality — trade secret 만 7년)
- 7.1 → MEDIUM (30 day cure — payment breach 만 15일)

### 4. [AI] Summary card prepend + talking points

> *"4 조항 모두 끝났어. summary card 한 단락을 memo 위에 prepend, deal-breaker
> 1 개 명시. partner-call talking points 4 개 적어줘."*

`htmlook_apply_edit` 로 memo 위쪽 Summary 영역 + 아래 checklist 동시 patch.

### 5. [VIEW] 우측 reload

- 표 4 행 모두 채워짐
- Summary 가 굵게 deal-breaker 강조
- talking points 4 개 체크박스로 표시

### 6. [AI 없는 사용자] before/after 비교

- 좌측: `08-legal-redline/before/memo.md`
- 우측: `08-legal-redline/after/memo.md`

## 검증 포인트

- ✅ `htmlook_pane_pair` (PDF + md memo)
- ✅ `htmlook_selection_text` (각 조항 영역)
- ✅ `htmlook_apply_edit` (memo 의 표 + summary + checklist multi-region)
- ⚠️ 영상의 *"Memo summary card prepend"* 는 multi-region apply_edit 로 처리

## 다음 페르소나

`09-data-analyst/` — SQL cite + chart redraw
