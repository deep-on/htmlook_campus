# 23 · homework-helper — 직각삼각형 → step-by-step 풀이

> 영상: `demo/persona_units/homework-helper/renders/homework-helper_voiced_bgm.en+ko.mp4`

학생이 좌측 homework.md, 우측 solution.md, 사이드바 concepts.md 를 띄우고
문제 1 cite → 3-step 풀이 + 비슷한 문제 3 개 + 한 줄 개념 reminder 동시 작성.

## 사전 준비

- HTMLook Pro
- (선택) LLM (수식 markdown $a^2 + b^2 = c^2$ 형식 가능 모델)

## 단계

### 1. [VIEW] 좌측 homework, 우측 solution, 사이드바 concepts

- 좌측: `23-homework-helper/homework.md`
- 우측: `23-homework-helper/solution.md`
- 사이드바: `23-homework-helper/concepts.md`

### 2. [AI] 문제 1 cite + step-by-step 풀이

좌측 *## 문제* 의 1번 (직각변 5, 12) 드래그-선택.

LLM 에:

> *"이 문제를 step 1 (정리 적용) → step 2 (대입) → step 3 (제곱근) 으로 풀어
> 우측 solution 에. 그리고 사이드바 concepts.md 에 한 줄 reminder 추가."*

LLM 이:
1. `htmlook_cite` 로 문제 1 anchor
2. `htmlook_apply_edit` 두 번 — solution.md (Step 1-3) + concepts.md (피타고라스 정리 한 줄)

### 3. [AI] 비슷한 문제 3 개 추가

좌측 정답 (c=13) 영역 드래그-선택. LLM 에:

> *"같은 양식으로 풀 수 있는 비슷한 문제 3 개를 우측 solution 의 *비슷한 연습 문제* 영역에 추가."*

LLM 이 `htmlook_apply_edit` 으로 solution.md 의 연습 문제 영역 patch — 3-4-5, 8-15-17, 9-40-41 등 피타고라스 수.

### 4. [VIEW] 우측 reload

- solution.md 에 Step 1-3 풀이 + reminder + 연습 문제 3 개
- concepts.md 사이드바에 한 줄 개념 + 피타고라스 수 묶음

### 5. [AI 없는 사용자] before/after 비교

- 좌측: `23-homework-helper/before/{solution.md,concepts.md}`
- 우측: `23-homework-helper/after/{solution.md,concepts.md}`

## 검증 포인트

- ✅ `htmlook_pane_pair` (homework + solution)
- ✅ `htmlook_cite` (문제 영역)
- ✅ `htmlook_apply_edit` (solution + concepts 동시)
- ✅ 수식 markdown ($...$) 보존

## 다음 페르소나

`24-student-flashcard/` — 노트 → 9:16 portrait 플래시카드 viewport
