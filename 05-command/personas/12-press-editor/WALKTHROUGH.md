# 12 · press-editor — 14:14 quote → 잡지 paragraph

> 영상: `demo/persona_units/press-editor/renders/press-editor_voiced_bgm.en+ko.mp4`

인터뷰 transcript 의 14:14 ~ 14:34 구간을 cite 해서 *Workflow Magazine #47*
의 cover quote 를 찾고, polish 한 paragraph 로 article 에 끼워 넣음.
print preview 에서 cite anchor (`14:14`) 가 인쇄에도 남음.

## 사전 준비

- HTMLook Pro
- (선택) LLM
- 인터뷰 transcript 는 외부에서 word-level 로 미리 transcribe 됨
  (`npx hyperframes transcribe interview.wav`)

## 단계

### 1. [VIEW] 좌측 transcript, 우측 article

- 좌측: `12-press-editor/transcript.md`
- 우측: `12-press-editor/article.html`
- transcript 에 timestamp + 화자 라벨 인라인

### 2. [AI] commoditised models 에 대한 가장 강한 quote 찾기

LLM 에:

> *"좌측 transcript 에서 commoditised models 에 대한 가장 강한 quote 한 줄을
> 찾아 cite 해. 그 다음 우측 article 의 lead paragraph 자리에 그 quote 와
> 짧은 셋업 paragraph 를 작성. cite anchor (timestamp) 는 인쇄에도 남도록 article
> 의 pullquote 안에 timecode 표시."*

LLM 이:
1. `htmlook_cite` 로 14:14 ~ 14:34 anchor
2. *"The model is a commodity. The workflow around it is the product."* 추출
3. `htmlook_apply_edit` 로 article.html 의 본문 영역 patch — `<blockquote class="pullquote">` 안에 `<div class="timecode">— J. Park, 14:14</div>` 보존

### 3. [AI] follow paragraph polish

> *"바로 다음 단락도 transcript 14:34, 14:48, 15:14 의 흐름을 한 단락으로 묶어
> polish 해줘."*

`htmlook_apply_edit` 로 article.html 의 follow paragraph 영역 patch.

### 4. [VIEW] 우측 reload + print preview

- pull-quote olive 색상, serif 타이포
- timecode `— J. Park, 14:14` 가 quote 아래에 남음
- print preview (브라우저 ⌘P) 에서도 timecode 가 인쇄됨

### 5. [AI 없는 사용자] before/after 비교

- 좌측: `12-press-editor/before/article.html`
- 우측: `12-press-editor/after/article.html`

## 검증 포인트

- ✅ `htmlook_pane_pair` (transcript + article)
- ✅ `htmlook_cite` (timestamp 범위)
- ✅ `htmlook_apply_edit` (pullquote + follow paragraph)
- ✅ cite anchor (timecode) 가 article HTML 안에 보존 → 인쇄에도 남음
- ⚠️ HTMLook 은 waveform/audio 뷰어가 없습니다. transcript 의 timestamp 텍스트가
  유일한 anchor.

## 다음 페르소나

`13-product-prd/` — PRD §3.2 cite + 와이어프레임 + 티켓 한번에
