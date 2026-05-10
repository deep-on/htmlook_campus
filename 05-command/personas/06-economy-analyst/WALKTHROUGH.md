# 06 · economy-analyst — 9:16 portrait macro brief

> 영상: `demo/persona_units/economy-analyst/renders/economy-analyst_voiced_bgm.en+ko.mp4`

매크로 분석가가 좌측에 draft, 우측에 9:16 portrait 카드를 띄우고 hook 숫자
+ 차트 + 3 bullet 을 한번에 작성. bullet 순서를 *weakest → strongest* 로 뒤집는
역검증 단계 포함.

## 사전 준비

- HTMLook Pro
- (선택) LLM 클라이언트

## 단계

### 1. [VIEW] 좌측 draft, 우측 portrait card

- 좌측: `06-economy-analyst/draft.md`
- 우측: `06-economy-analyst/card.html`
- 우측은 letterboxed 9:16 portrait — 모바일 미리보기

### 2. [AI] hook + chart + bullets 채우기

LLM 에:

> *"draft.md 의 hook 숫자, chart spec, talking points 를 우측 portrait card
> 에 채워줘. 카드는 위에서 아래로 hook → bullets → chart → source."*

LLM 이 `htmlook_apply_edit` 로 card.html 의 영역들을 한번에 patch.

### 3. [AI] bullet 순서 flip — strongest first

좌측 draft 에서 talking points 블록 드래그-선택.

LLM 에:

> *"이 bullet 들이 weakest 가 위에 있어. strongest first 로 뒤집고 첫 줄을
> bold."*

`htmlook_apply_edit` → card.html 의 `<ul>` 영역 갱신.

### 4. [VIEW] 우측 reload

- 첫 bullet 이 *"Largest consensus miss since Q1 2024."* (bold)
- 두번째: ex-shelter
- 세번째: goods inflation

### 5. [AI 없는 사용자] before/after 비교

- 좌측: `06-economy-analyst/before/card.html`
- 우측: `06-economy-analyst/after/card.html`

## 검증 포인트

- ✅ `htmlook_pane_pair` (md draft + portrait html)
- ✅ `htmlook_selection_text` (bullet 블록)
- ✅ `htmlook_apply_edit` (multi-region patch)
- ⚠️ TTS / Whisper align 은 외부 CLI

## 다음 페르소나

`07-translator-book/` — PDF 한 단락씩 번역 + 이중 페이지
