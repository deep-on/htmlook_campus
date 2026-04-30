# 22 · hobby-fiction — outline → scene

> 영상: `demo/persona_units/hobby-fiction/renders/hobby-fiction_voiced_bgm.en+ko.mp4`

취미 작가가 좌측에 outline (등장인물 카드 + plot points + 톤 노트), 우측에
빈 chapter1.md 를 두고 *Mars 콜로니 마지막 송신* plot point 를 cite 해서
1500 단어 분량의 scene 작성. 등장인물 일관성 검사로 4 줄 dialogue 확인,
1 줄 drift 인라인 수정.

## 사전 준비

- HTMLook Pro
- (선택) LLM (장문 한국어 산문 가능 모델)

## 단계

### 1. [VIEW] 좌측 outline.md, 우측 chapter1.md

- 좌측: `22-hobby-fiction/outline.md` — 등장인물 / plot / 톤
- 우측: `22-hobby-fiction/chapter1.md` — 빈 1장

### 2. [AI] plot point 1 cite + scene 작성

좌측 *## Plot points* 의 1번 항목 *(Mars 콜로니 4 의 마지막 정기 송신이 14시 02분에 끊긴다)* 드래그-선택.

LLM 에:

> *"이 plot point 를 닥터 한 시점 3인칭 제한으로 풀어. 1500 단어 정도, 대화는
> 짧게, 노바 발화 앞에 (0.4초) 표시 유지. 4 plot points 전부 한 장 안에 흐르게."*

LLM 이:
1. `htmlook_cite` 로 plot points 영역 anchor
2. `htmlook_apply_edit` 으로 chapter1.md 본문 작성

### 3. [AI] 등장인물 일관성 검사

> *"좌측 등장인물 카드 cite 해서 우측 1장의 dialogue 4 줄을 검사해. 카이의
> 농담 톤 / 노바의 0.4초 / 닥터 한의 회의적 침착함 모두 일치하는지."*

LLM 이 outline 의 *## 등장인물 카드* 와 chapter1.md 의 dialogue 4 줄을 비교.
1 줄이 drift (예: 노바가 0.4초 표시 없이 말함) → `htmlook_apply_edit` 으로
한 줄 inline 수정.

### 4. [VIEW] 우측 reload

- chapter1.md 가 1500 단어 분량의 1장
- 노바의 모든 발화 앞에 *(0.4초)* 표시
- 마지막 plot point (보고할지 망설이는 한 장면) 도 1장 클로징에 포함

### 5. [AI 없는 사용자] before/after 비교

- 좌측: `22-hobby-fiction/before/chapter1.md`
- 우측: `22-hobby-fiction/after/chapter1.md`

## 검증 포인트

- ✅ `htmlook_pane_pair` (outline + chapter)
- ✅ `htmlook_cite` (plot point anchor)
- ✅ `htmlook_apply_edit` (1장 본문 + dialogue 한 줄 fix)
- ⚠️ Kokoro 새 passage 음성 / Whisper align 은 외부 CLI

## 다음 페르소나

`23-homework-helper/` — 직각삼각형 문제 → step-by-step 풀이
