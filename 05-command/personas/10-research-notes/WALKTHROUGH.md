# 10 · research-notes — 논문 PDF cite + 노트 + bibliography

> 영상: `demo/persona_units/research-notes/renders/research-notes_voiced_bgm.en+ko.mp4`

논문 한 단락을 cite 하면 노트 한 줄 + bibliography 한 항목이 동시에 생기는
워크플로우.

## 사전 준비

- HTMLook Pro
- (선택) LLM
- `paper.pdf` 는 reportlab 으로 미리 생성됨 (Methods §3.2, Findings §4.1)

## 단계

### 1. [VIEW] 좌측 paper.pdf, 우측 notes.md

- 좌측: `10-research-notes/paper.pdf`
- 우측: `10-research-notes/notes.md` (Findings / Bibliography 비어 있음)

### 2. [AI] §3.2 methods cite + Operator 정의 추출

좌측 PDF 의 §3.2 영역 드래그-선택.

LLM 에:

> *"이 단락에서 'Operator' 정의를 정확히 quote 하고 우측 notes.md 의 Findings
> 표 #3 행에 anchor (p. 4, §3.2) + citekey 로 추가."*

LLM 이 `htmlook_cite` → page 4, §3.2 anchor 확보 → `htmlook_apply_edit` 으로
notes.md 의 표 한 줄 추가.

### 3. [AI] §4.1 findings — 한 문장 요약 + citekey 제안

같은 패턴으로 §4.1 cite. LLM 이:

- *"cold-junction protocol cuts σ from 6.3% to 1.7%"* 한 문장 요약
- citekey 제안: `park2026apparatus`
- bibliography 항목 자동 추가 (DOI 포함)

`htmlook_apply_edit` 로 notes.md 의 Findings 표 + Bibliography 영역 동시 patch.

### 4. [AI] §4.2 variance — 세번째 finding

> *"§4.2 도 같은 형식으로 추가."*

→ Findings 표 #2 행 + Open questions 한 줄 추가.

### 5. [VIEW] 우측 reload

- Findings 표 3 행 모두 채워짐
- Bibliography 1 항목
- Open questions 1 줄 추가
- 모든 anchor 가 paper.pdf 의 §3.2 / §4.1 / §4.2 로 역추적 가능

### 6. [AI 없는 사용자] before/after 비교

- 좌측: `10-research-notes/before/notes.md`
- 우측: `10-research-notes/after/notes.md`

## 검증 포인트

- ✅ `htmlook_pane_pair` (PDF + md)
- ✅ `htmlook_cite` (page + section anchor)
- ✅ `htmlook_apply_edit` (Findings + Bibliography multi-region)
- ⚠️ 영상의 *"three citation markers"* 는 표 행 단위 anchor 로 표현

## 다음 페르소나

`11-finance-report/` — Q3 xlsx EBITDA cite + CFO brief
