# 04 · creator-podcast — quotable 20초 찾기 + kinetic 클립

> 영상: `demo/persona_units/creator-podcast/renders/creator-podcast_voiced_bgm.en+ko.mp4`

팟캐스트 인터뷰에서 *14:14 의 한 줄* 을 찾아 9:16 kinetic clip 으로 패키징.

## 사전 준비

- HTMLook Pro
- (선택) Claude / Llama 호환 클라이언트
- 인터뷰 transcript 는 외부에서 미리 word-level 로 transcribe 됐다고 가정
  (`npx hyperframes transcribe interview.wav`)

## 단계

### 1. [VIEW] 좌측 transcript, 우측 clip 프리뷰

- 좌측: `04-creator-podcast/transcript.md`
- 우측: `04-creator-podcast/clip.html`
- transcript 는 timestamp 가 인라인. clip 은 9:16 portrait 카드.

### 2. [AI] 가장 quotable 한 20초 찾기

LLM 에:

> *"좌측 transcript 에서 가장 quotable 한 20초 구간을 찾아 cite 해줘. 그 다음
> kinetic caption 으로 우측 clip 에 적용."*

LLM 이:

1. `htmlook_cite` 로 14:14 ~ 14:34 범위 anchor
2. *"The model is a commodity. The workflow around it is the product."* 추출
3. `htmlook_apply_edit` 로 clip.html 의 quote 영역 갱신

### 3. [VIEW] 우측 reload

- 자동 reload, 새 quote + timestamp badge 가 보임

### 4. [AI] 단어 한 개 retiming

- 우측 미리보기에서 *"moat"* 가 한 박자 늦게 들어옴
- 좌측에서 14:14 인근 한 단어 cite, LLM 에 *"한 stagger 만 당겨줘"*
- `htmlook_apply_edit` 로 clip.html 의 stagger CSS 또는 단어 줄바꿈 조정

### 5. [AI 없는 사용자] before/after 비교

- 좌측: `04-creator-podcast/before/clip.html`
- 우측: `04-creator-podcast/after/clip.html`

## 검증 포인트

- ✅ `htmlook_cite` (transcript timestamp 범위)
- ✅ `htmlook_apply_edit` (clip.html 갱신)
- ⚠️ HTMLook 은 waveform viewer 가 없습니다. transcript 의 timestamp 텍스트가
  cite anchor 입니다. 오디오 파형 시각 확인은 별도 도구 필요.
- ⚠️ Kokoro pull-quote / Whisper align 은 외부 CLI

## 다음 페르소나

`05-domain-battery/` — vendor 데이터시트 PDF cite + 차트 redraw
