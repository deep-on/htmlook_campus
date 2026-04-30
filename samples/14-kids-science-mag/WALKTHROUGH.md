# 14 · kids-science-mag — 어른용 과학 단락 → kids portrait

> 영상: `demo/persona_units/kids-science-mag/renders/kids-science-mag_voiced_bgm.en+ko.mp4`

어른용 과학 텍스트를 cite 해서 9:16 portrait kids magazine 페이지로 변환.
호기심 한 줄 + 3 단계 실험 + glossary 가 동시에 채워짐. glossary chip 단어를
다시 cite 해서 더 쉬운 표현으로 한번 더 patch.

## 사전 준비

- HTMLook Pro
- (선택) LLM

## 단계

### 1. [VIEW] 좌측 source.md, 우측 page.html

- 좌측: `14-kids-science-mag/source.md` (어른용 영문 과학 단락)
- 우측: `14-kids-science-mag/page.html` (호기심/실험/glossary 자리만 있음)

### 2. [AI] paragraph 1 cite + kids paraphrase

좌측 source.md 의 첫 단락 드래그-선택.

LLM 에:

> *"이 어른용 단락을 초등 4-6학년 수준으로 paraphrase 해서 우측 page 의
> 호기심 버블 + 실험 3단계 + glossary 까지 한번에 채워줘. 한국어, 따뜻한 톤."*

LLM 이:
1. `htmlook_selection_text` 로 단락 확보
2. `htmlook_apply_edit` 로 page.html 의 3 영역 동시 patch

### 3. [AI] glossary chip 다시 cite — 더 쉬운 단어

좌측에서 *surface tension* 행 또는 우측 page 의 *표면장력* chip 드래그.

LLM 에:

> *"glossary 가 아직 어려워. 더 쉬운 표현으로 한번 더 줄여."*

`htmlook_apply_edit` 으로 glossary 영역만 patch — *"단위 길이 당 힘 (N/m)"* 같은
표현을 *"물 표면이 자기 자신을 잡아당기는 힘"* 으로 교체.

### 4. [VIEW] 우측 reload

- 호기심 한 줄, 실험 3단계, glossary 모두 친근한 한국어
- portrait 9:16 letterboxed 카드로 보임

### 5. [AI 없는 사용자] before/after 비교

- 좌측: `14-kids-science-mag/before/page.html` (academic glossary)
- 우측: `14-kids-science-mag/after/page.html` (kid-friendly)

## 검증 포인트

- ✅ `htmlook_pane_pair` (md + portrait html)
- ✅ `htmlook_selection_text` (단락 + chip)
- ✅ `htmlook_apply_edit` (multi-region: bubble + 실험 + glossary)
- ⚠️ Kokoro voice / Whisper align 은 외부 CLI

## 다음 페르소나

`15-picture-book/` — 그림책 한 줄 운율 다듬기
