# 20 · student-notes — 강의 슬라이드 → 노트북 + 플래시카드

> 영상: `demo/persona_units/student-notes/renders/student-notes_voiced_bgm.en+ko.mp4`

학생이 좌측에 강의 슬라이드를, 우측에 study notebook 을, 사이드바에
flashcards.md 를 띄우고 한 cite 로 두 파일을 동시에 patch.

## 사전 준비

- HTMLook Pro
- (선택) LLM

## 단계

### 1. [VIEW] 좌측 lecture, 우측 notebook, 사이드바 flashcards

- 좌측: `20-student-notes/lecture.md` (Bio 201 Week 5 — Synapses)
- 우측: `20-student-notes/notebook.md`
- 사이드바: `20-student-notes/flashcards.md`

### 2. [AI] slide 5 cite + notebook + flashcards 동시 patch

좌측 lecture.md 의 *## Slide 5* 영역 드래그-선택. (또는 slide 2-4 통째로.)

LLM 에:

> *"이 슬라이드 영역 cite 해서 (a) notebook.md 의 Week 5 영역에 3 bullet
> summary + worked example 추가, (b) flashcards.md 에 Q&A 카드 4 개 추가.
> 한 round trip 으로."*

LLM 이:
1. `htmlook_cite` 로 slide 영역 anchor
2. `htmlook_apply_edit` 두 번 (notebook.md + flashcards.md)
3. notebook 의 exam-prep checklist 체크박스도 동기화

### 3. [AI] flashcard 한 장 보강

사이드바 flashcards.md 에서 *Q3* 카드 드래그.

LLM 에:

> *"이 카드 답변이 너무 짧아. 예시 한 줄 추가."*

`htmlook_apply_edit` → flashcards.md 의 Q3 영역 patch.

### 4. [VIEW] 우측 reload

- notebook 에 3 bullet + worked example
- flashcards 에 Q1-Q4 (4 카드)
- exam-prep checklist 4 항목 모두 체크

### 5. [AI 없는 사용자] before/after 비교

- 좌측 셋: `20-student-notes/before/{notebook.md,flashcards.md}`
- 우측 셋: `20-student-notes/after/{notebook.md,flashcards.md}`

## 검증 포인트

- ✅ `htmlook_pane_pair` (lecture + notebook)
- ✅ `htmlook_cite` (slide anchor)
- ✅ `htmlook_apply_edit` (notebook + flashcards 두 파일 동시)
- ⚠️ 영상의 *"deck reloads"* 는 flashcards.md 의 markdown reload 로 매핑

## 다음 페르소나

`21-kid-coding/` — 어린이 코딩, star.py + turtle 결과
