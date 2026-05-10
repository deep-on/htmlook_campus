# 24 · student-flashcard — 노트 → 9:16 portrait flashcard

> 영상: `demo/persona_units/student-flashcard/renders/student-flashcard_voiced_bgm.en+ko.mp4`

학생이 좌측에 강의 노트, 우측에 9:16 portrait flashcard viewport. 뉴런 섹션
cite → 5 카드 생성. 그 중 *synapse* 카드가 너무 쉬워서 한번 더 cite 해
강화.

## 사전 준비

- HTMLook Pro
- (선택) LLM

## 단계

### 1. [VIEW] 좌측 notes.md, 우측 cards.html

- 좌측: `24-student-flashcard/notes.md` (뉴런 / 시냅스 / 활동전위)
- 우측: `24-student-flashcard/cards.html` (9:16 portrait letterboxed, 빈 카드)

### 2. [AI] 뉴런 섹션 cite + 5 카드

좌측 *## 뉴런* 섹션 드래그-선택.

LLM 에:

> *"이 섹션 cite 해서 Q&A 카드 5 개 생성. 우측 cards.html 의 카드 자리에
> 한 카드씩 채워. 진도 표시 1/5 ~ 5/5."*

LLM 이 `htmlook_apply_edit` 으로 cards.html 의 `.q` / `.a` / `.progress` 영역
한 카드씩 patch (실제 데모는 한 카드 표시, 카드 데이터는 별도 markdown 에 5 개 적어
viewport 가 swipe 로 넘기는 구조).

### 3. [AI] synapse 카드 너무 쉬움 → 강화

우측 cards.html 의 카드 (현재 *synapse 란?*) 드래그-선택.

LLM 에:

> *"이 카드 너무 쉬워. 흥분성 vs 억제성 차이를 묻는 문제로 한 단계 어렵게 바꿔."*

LLM 이 `htmlook_apply_edit` → cards.html 의 `.q`, `.a` 영역 patch.
- 새 질문: *"흥분성 시냅스와 억제성 시냅스의 차이를 한 문장으로 설명."*
- 새 답: 탈분극 / 과분극 대비 + 한 줄 정리.

### 4. [VIEW] 우측 reload

- 9:16 portrait card 가 새 질문/답으로 표시
- 진도 *2 / 5* 그대로 유지

### 5. [AI 없는 사용자] before/after 비교

- 좌측: `24-student-flashcard/before/cards.html` (synapse 카드, 너무 쉬움)
- 우측: `24-student-flashcard/after/cards.html` (흥분성 vs 억제성, 강화)

## 검증 포인트

- ✅ `htmlook_pane_pair` (notes + portrait card)
- ✅ `htmlook_cite` (notes 섹션)
- ✅ `htmlook_apply_edit` (cards.html 의 Q/A 영역)
- ⚠️ TTS 카드 음성 / Whisper align 은 외부 CLI

## 다음 페르소나

`25-recipe-card/` — 레시피 → 9:16 portrait swipeable card
