# 19 · teacher-record — 일일 노트 → 학생별 종합 의견

> 영상: `demo/persona_units/teacher-record/renders/teacher-record_voiced_bgm.en+ko.mp4`

선생님이 일주일치 일일 노트를 cite 해서 학생별로 group 한 후 학기말 종합
의견 (4 문장 / 학생) 을 한번에 작성. 조용한 학생 1 명을 다시 cite 해서 행
한 줄 보강.

## 사전 준비

- HTMLook Pro
- (선택) LLM

## 단계

### 1. [VIEW] 좌측 daily.md, 우측 record.md

- 좌측: `19-teacher-record/daily.md` — 4 일치 일일 노트
- 우측: `19-teacher-record/record.md` — 학생 3 명 (민호 / 지수 / 서연) 빈 자리

### 2. [AI] 일일 노트 전체 cite + 학생별 grouping

좌측 daily.md 전체 또는 *## 4월 22일* 부터 *## 4월 29일* 까지 드래그-선택.

LLM 에:

> *"이 일일 노트를 학생별로 group 해서 우측 record.md 의 민호/지수/서연 각
> 각에 4 문장 종합 의견을 작성. 일일 노트 날짜를 인라인으로 cite (4/22, 4/24)
> 형태로 남길 것."*

LLM 이:
1. `htmlook_selection_text` 로 노트 영역 anchor
2. 학생별 grouping
3. `htmlook_apply_edit` 으로 record.md 의 3 영역 동시 patch

### 3. [AI] 조용한 학생 — 보강

서연이 대상 일일 노트만 cite (좌측 4/22, 4/24, 4/28, 4/29 의 *서연* 라인 4 줄
드래그-선택).

LLM 에:

> *"서연이의 일주일 변화를 발표/짝활동/감정표현 각 단계로 짚어주고, 다음
> 구간 제안까지 포함."*

`htmlook_apply_edit` → record.md 의 *## 서연* 영역 한 단락 보강.

### 4. [VIEW] 우측 reload

- 학생 3 명 모두 4 문장 종합 의견 + 다음 구간 제안
- 일일 노트 날짜 (4/22, 4/24, 4/28, 4/29) 가 인라인으로 남아 추적 가능

### 5. [AI 없는 사용자] before/after 비교

- 좌측: `19-teacher-record/before/record.md`
- 우측: `19-teacher-record/after/record.md`

## 검증 포인트

- ✅ `htmlook_pane_pair` (daily + record)
- ✅ `htmlook_selection_text` (학생별 행 묶기)
- ✅ `htmlook_apply_edit` (record 의 학생 3 영역 multi-region)
- ⚠️ Kokoro recap / Whisper align 은 외부 CLI

## 다음 페르소나

`20-student-notes/` — 강의 슬라이드 → 노트북 + 플래시카드
