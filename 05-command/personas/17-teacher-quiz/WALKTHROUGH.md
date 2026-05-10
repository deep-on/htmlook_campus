# 17 · teacher-quiz — 챕터 → 5 객관식 + 2 주관식 + rubric

> 영상: `demo/persona_units/teacher-quiz/renders/teacher-quiz_voiced_bgm.en+ko.mp4`

선생님이 6학년 과학 5장 노트를 cite 해서 평가지 (객관식 5 / 주관식 2 / 정답
/ 채점 기준) 를 한번에 작성. 어휘 섹션 cite 로 난이도 mix 조정.

## 사전 준비

- HTMLook Pro
- (선택) LLM

## 단계

### 1. [VIEW] 좌측 chapter.md, 우측 quiz.md

- 좌측: `17-teacher-quiz/chapter.md` (6학년 5장 «빛과 그림자»)
- 우측: `17-teacher-quiz/quiz.md` (빈 평가지 scaffold)

### 2. [AI] 챕터 cite + 평가지 초안

좌측 chapter.md 전체 또는 *## 핵심 개념* 섹션 드래그-선택.

LLM 에:

> *"이 챕터를 바탕으로 객관식 5문항 + 주관식 2문항 + 정답 + 해설을 우측
> quiz.md 에 채워줘. 6학년 1학기 어휘 수준."*

LLM 이 `htmlook_apply_edit` 으로 객관식 / 주관식 / 정답 영역 동시 patch.

### 3. [AI] 어휘 섹션 cite + 난이도 조정

좌측 *## 어휘* 섹션 드래그.

LLM 에:

> *"객관식 5문항 난이도를 쉬움 2 / 보통 2 / 어려움 1 로 mix 해주고,
> rubric 표 하나 추가."*

`htmlook_apply_edit` → 객관식 각 문항 앞에 `**(쉬움)** / **(보통)** / **(어려움)**` 라벨,
*## 채점 기준* 영역에 표 추가.

### 4. [VIEW] 우측 reload

- 객관식 5 + 주관식 2 + 정답 + 채점 기준 (총 18점, 합격선 12점)
- 인쇄 가능한 한 페이지 분량

### 5. [AI 없는 사용자] before/after 비교

- 좌측: `17-teacher-quiz/before/quiz.md`
- 우측: `17-teacher-quiz/after/quiz.md`

## 검증 포인트

- ✅ `htmlook_pane_pair` (chapter + quiz)
- ✅ `htmlook_cite` (핵심 개념 / 어휘 섹션)
- ✅ `htmlook_apply_edit` (multi-region: 객관식 + 주관식 + 정답 + rubric)
- ⚠️ Kokoro recap / Whisper align 은 외부 CLI

## 다음 페르소나

`18-teacher-newsletter/` — 학구 정책 → 학부모 친화 newsletter
