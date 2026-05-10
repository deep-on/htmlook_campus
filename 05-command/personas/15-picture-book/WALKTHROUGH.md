# 15 · picture-book — 그림책 운율 다듬기

> 영상: `demo/persona_units/picture-book/renders/picture-book_voiced_bgm.en+ko.mp4`

그림책 4쪽 spread 의 둘째 줄이 4-4 cadence 를 깨뜨림. cite + tighten 으로
음절 수 다듬기, 그리고 우면 캡션도 9 → 8 음절로 한 음절만 줄임.

## 사전 준비

- HTMLook Pro
- (선택) LLM (한국어 운율 인식이 정확한 모델 권장)

## 단계

### 1. [VIEW] 좌측 verse.md, 우측 spread.html

- 좌측: `15-picture-book/verse.md` (운율 메모 포함)
- 우측: `15-picture-book/spread.html` (좌면 운문 + 우면 일러 + 캡션)

### 2. [AI] 둘째 줄 cite + 음절 다듬기

좌측 verse.md 에서 둘째 줄 *"등껍질을 매고 길을 떠나는 친구들 모두 모여요."*
드래그-선택.

LLM 에:

> *"이 줄이 4-4 cadence 를 깨뜨려. 첫째/셋째 줄과 같은 길이로 다듬어줘.
> spread.html 의 둘째 `<p>` 도 동시에 patch."*

LLM 이:
1. `htmlook_selection_text` 로 줄 anchor
2. 새 줄: *"등껍질 메고 친구들이 모여."* (4-4-3 → 좀 더 짧게)
3. `htmlook_apply_edit` 으로 verse.md + spread.html 동시 patch

### 3. [AI] 우면 캡션 1 음절 줄이기

> *"우면 캡션 한 음절만 줄여서 그림과 호흡을 맞춰."*

원래: *"오늘은 받침에 대해 배우는 첫 시간이에요."*
바뀐 것: *"오늘은 받침을 배우는 첫 시간."*

`htmlook_apply_edit` → spread.html 의 `<p class="caption">` 영역.

### 4. [VIEW] 우측 reload

- 좌면 3 줄이 4-4 cadence 로 균질
- 우면 캡션이 짧아져 그림과 호흡 일치

### 5. [AI 없는 사용자] before/after 비교

- 좌측: `15-picture-book/before/spread.html`
- 우측: `15-picture-book/after/spread.html`

## 검증 포인트

- ✅ `htmlook_pane_pair` (verse + spread)
- ✅ `htmlook_selection_text` (한 줄 anchor)
- ✅ `htmlook_apply_edit` (verse.md + spread.html 동시)
- ⚠️ Kokoro verse 음성 / Whisper align 은 외부 CLI

## 다음 페르소나

`16-corp-deck/` — Q3 보고서 cite → 슬라이드 + 발표 노트
