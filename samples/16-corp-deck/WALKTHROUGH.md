# 16 · corp-deck — 보고서 cite → 슬라이드 + 노트

> 영상: `demo/persona_units/corp-deck/renders/corp-deck_voiced_bgm.en+ko.mp4`

Q3 보고서의 KPI / Variance 섹션을 cite 해서 빈 deck 의 슬라이드 본문 + 발표
노트를 동시에 채움. multi-target apply_edit.

## 사전 준비

- HTMLook Pro
- (선택) LLM

## 단계

### 1. [VIEW] 좌측 q3-report.md, 우측 deck.html

- 좌측: `16-corp-deck/q3-report.md`
- 우측: `16-corp-deck/deck.html` (3 슬라이드 scaffold — cover / KPI / Variance)

### 2. [AI] KPI 섹션 cite + slide 2 채우기

좌측 보고서의 *## KPI* 섹션 드래그-선택.

LLM 에:

> *"이 KPI 섹션을 cite 해서 deck 의 slide 2 (KPI snapshot) 의 bullet 3 개,
> chart placeholder, 그리고 발표 노트 한 단락 동시에 채워줘."*

LLM 이:
1. `htmlook_cite` 로 §KPI anchor
2. `htmlook_apply_edit` 로 deck.html 의 slide 2 영역 — `<ul>`, `.chart`, `.notes` 동시 patch

### 3. [AI] Variance 섹션 cite + slide 3 채우기

같은 패턴으로 *## Variance* 섹션 cite → slide 3 (waterfall + 발표 노트).

> *"variance 의 4 driver (+$2.1M Revenue, +$2.0M S&M, +$0.2M G&A, −$0.7M CoGS)
> 를 bullet 으로 풀고, 발표 노트는 ops review 일정 (2026-05-12) 까지 포함."*

`htmlook_apply_edit` 으로 slide 3 영역 multi-region patch.

### 4. [AI] cover (slide 1) 의 발표 노트도 update

> *"slide 1 cover 의 발표 노트도 한 줄로 정리. headline 은 EBITDA +11.6%."*

### 5. [VIEW] 우측 reload

- 6 슬라이드 (영상에서는 6) — 본 sample 은 핵심 3 슬라이드만 시연
- 각 슬라이드의 본문 + 발표 노트 동기화됨

### 6. [AI 없는 사용자] before/after 비교

- 좌측: `16-corp-deck/before/deck.html`
- 우측: `16-corp-deck/after/deck.html`

## 검증 포인트

- ✅ `htmlook_pane_pair` (보고서 + deck)
- ✅ `htmlook_cite` (§KPI, §Variance)
- ✅ `htmlook_apply_edit` (deck 의 multi-region: bullets + chart + notes)
- ⚠️ Kokoro recap / Whisper align 은 외부 CLI

## 다음 페르소나

`17-teacher-quiz/` — 챕터 → 5 객관식 + 2 주관식 + rubric
