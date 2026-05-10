# 07 · translator-book — 단락별 번역 + 이중 페이지

> 영상: `demo/persona_units/translator-book/renders/translator-book_voiced_bgm.en+ko.mp4`

영문 에세이 (3 단락) PDF 를 한국어로 옮기되 단락 단위 cite + apply_edit 로
저자 톤을 유지. 마지막 단락에 역주 1개 추가.

## 사전 준비

- HTMLook Pro
- (선택) LLM
- 원문 `source.pdf` 는 reportlab 으로 미리 생성됨 (1페이지)

## 단계

### 1. [VIEW] 좌측 PDF, 우측 한국어 draft

- 좌측: `07-translator-book/source.pdf`
- 우측: `07-translator-book/draft.md`
- draft 의 단락 1/2/3 은 비어 있음, glossary 도 비어 있음

### 2. [AI] 단락 1 cite + 한국어 옮김

좌측 PDF 에서 단락 1 영역을 드래그-선택.

LLM 에:

> *"이 단락의 한국어 번역을 작성해서 우측 draft.md 의 '## 단락 1' 아래에
> 끼워 넣어 줘. 저자의 산문 톤 유지, 'missing mile' 은 *잃어버린 1마일* 로."*

LLM 이:
1. `htmlook_selection_text` 로 PDF 영역 텍스트 확보
2. 한국어 번역 작성
3. `htmlook_apply_edit` 로 draft.md 의 해당 위치 patch

### 3. [AI] 단락 2, 3 + 역주

같은 패턴을 반복. 단락 3 에는:

> *"마지막에 역주 1개 추가. perform 의 연기하다/무대 보여주다 양 뜻을 어떻게
> 처리했는지 짧게."*

### 4. [AI] glossary 동기화

> *"draft.md 의 glossary 비어 있는 항목을 단락 1-3 본문에서 일관되게 사용된
> 어휘로 채워."*

`htmlook_apply_edit` 로 glossary 4 항목 채움.

### 5. [VIEW] 우측 reload

- 단락 1-3 + 역주 + glossary 가 모두 채워진 상태
- HTMLook 의 markdown 뷰어가 본문/glossary 모두 렌더

### 6. [AI 없는 사용자] before/after 비교

- 좌측: `07-translator-book/before/draft.md`
- 우측: `07-translator-book/after/draft.md`

## 검증 포인트

- ✅ `htmlook_pane_pair` (PDF + md)
- ✅ `htmlook_selection_text` (PDF 단락 영역)
- ✅ `htmlook_apply_edit` (draft 단락별 patch)
- ⚠️ "이중 페이지 인쇄" 는 외부 PDF 도구로 합쳐서 출력 (HTMLook 내장 아님)

## 다음 페르소나

`08-legal-redline/` — 계약서 4개 조항 cite + redline memo
