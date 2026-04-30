# 26 · mobile-news — 1500 단어 기사 → 모바일 카드 4 장

> 영상: `demo/persona_units/mobile-news/renders/mobile-news_voiced_bgm.en+ko.mp4`

긴 기사를 좌측에, 9:16 portrait 카드 4 장 (TLDR / 핵심 데이터 / 헤드라인 인용
/ 출처) viewport 를 우측에 띄우고 한 번의 apply_edit 으로 4 카드 모두 채움.

## 사전 준비

- HTMLook Pro
- (선택) LLM

## 단계

### 1. [VIEW] 좌측 article.md, 우측 cards.html

- 좌측: `26-mobile-news/article.md` (약 1,500 단어)
- 우측: `26-mobile-news/cards.html` (4 카드 scaffold)

### 2. [AI] 리드 단락 cite + TLDR 카드

좌측 *## 리드* 단락 드래그-선택.

LLM 에:

> *"이 리드를 3 줄 요약 TLDR 카드로 채워. 그리고 article 전체를 살펴 카드
> 2/3/4 (핵심 데이터 / 헤드라인 인용 / 출처) 도 한 번에 채워."*

LLM 이:
1. `htmlook_cite` 로 리드 단락 anchor
2. 추가로 *## 핵심 데이터*, *## 헤드라인 인용*, *## 출처* 섹션도 cite
3. `htmlook_apply_edit` 으로 cards.html 의 4 카드 영역 모두 multi-region patch

### 3. [VIEW] 우측 reload

- TLDR 카드 = 3 줄 요약
- 데이터 카드 = 8.7 초 / 6 파일 / −44% / 18% (4 개)
- 인용 카드 = *"모델은 이미 commodity ..."* + 14:14 timecode
- 출처 카드 = 블로그 / 발표 영상 / 후기 페이지

### 4. [AI 없는 사용자] before/after 비교

- 좌측: `26-mobile-news/before/cards.html`
- 우측: `26-mobile-news/after/cards.html`

## 검증 포인트

- ✅ `htmlook_pane_pair` (article + cards)
- ✅ `htmlook_cite` (lead + 데이터 + 인용 + 출처)
- ✅ `htmlook_apply_edit` (4 카드 한 번에 multi-region)
- ⚠️ TTS TLDR 음성 / Whisper align 은 외부 CLI

## 다음 페르소나

이 페르소나가 마지막입니다. `01-hf-claude/` 로 돌아가 전체 패턴을 한 번 더
확인하거나, `sample_workspace/README.md` 의 인덱스를 참고하세요.
