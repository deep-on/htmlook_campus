# 25 · recipe-card — 레시피 → 9:16 portrait swipeable card

> 영상: `demo/persona_units/recipe-card/renders/recipe-card_voiced_bgm.en+ko.mp4`

레시피 markdown 을 cite 해서 9:16 portrait 카드로 변환. 재료 g 단위 표시,
4 단계 아이콘. step 3 가 너무 wordy 해서 한번 더 cite + tighten.

## 사전 준비

- HTMLook Pro
- (선택) LLM

## 단계

### 1. [VIEW] 좌측 recipe.md, 우측 card.html

- 좌측: `25-recipe-card/recipe.md` (떡볶이 30분 1인분)
- 우측: `25-recipe-card/card.html` (9:16 portrait)

### 2. [AI] 레시피 cite + 1 인분 카드

좌측 recipe.md 전체 드래그-선택.

LLM 에:

> *"이 레시피를 1인분 9:16 카드로 정리. 재료는 g 단위 한 줄, 단계는 4 step
> 아이콘 (🍲/🔪/⏱️/🥢)."*

LLM 이 `htmlook_apply_edit` 으로 card.html 의 `.ingredients`, `.steps` 영역 patch.

### 3. [AI] step 3 tighten

우측 카드의 step 3 (*"끓이고 맛이 떡 가운데까지 들어가게 충분히 익힌 다음 대파 30초"*) 드래그-선택.

LLM 에:

> *"step 3 너무 길어. 한 줄로."*

LLM 이 `htmlook_apply_edit` → step 3 영역만 *"5-7분 끓이고 마지막에 대파 30초"* 로 patch.

### 4. [VIEW] 우측 reload

- 4 step 그리드가 모두 short caption
- 9:16 portrait 카드, 인스타그램 사이즈

### 5. [AI 없는 사용자] before/after 비교

- 좌측: `25-recipe-card/before/card.html` (step 3 wordy)
- 우측: `25-recipe-card/after/card.html` (tightened)

## 검증 포인트

- ✅ `htmlook_pane_pair` (md + portrait card)
- ✅ `htmlook_selection_text` (step 3 영역)
- ✅ `htmlook_apply_edit` (step 3 한 영역만 patch)
- ⚠️ TTS 단계 음성 / Whisper align 은 외부 CLI

## 다음 페르소나

`26-mobile-news/` — 1500 단어 기사 → 모바일 카드 4 장
