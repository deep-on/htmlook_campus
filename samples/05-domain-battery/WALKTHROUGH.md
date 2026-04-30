# 05 · domain-battery — vendor PDF cite + 차트 redo

> 영상: `demo/persona_units/domain-battery/renders/domain-battery_voiced_bgm.en+ko.mp4`

배터리 cell vendor 비교 brief 를 vendor 데이터시트 PDF 와 듀얼뷰로 작성하고,
PDF 의 cycle-life 행을 cite 해서 *8,000 → 8,200* 데이터 포인트 업데이트.

## 사전 준비

- HTMLook Pro
- (선택) Claude / Llama
- `vendor.pdf` 는 이미 워크스페이스에 있음 (reportlab 으로 생성된 1페이지 표)

## 단계

### 1. [VIEW] 좌측 brief, 우측 vendor.pdf

- 좌측: `05-domain-battery/brief.md`
- 우측: `05-domain-battery/vendor.pdf`
- HTMLook 의 PDF viewer 가 데이터시트를 렌더

### 2. [AI] 세 vendor 비교 + cite

LLM 에:

> *"vendor.pdf 의 cycle-life 행을 cite 해서 좌측 brief 에 세 vendor 비교 표
> 와 점수표를 작성해 줘. 차트도 ASCII 로."*

LLM 이:

1. `htmlook_cite` 로 PDF 의 cycle-life 행 anchor (row 4, column A)
2. brief.md 에 표 + 차트 작성
3. `htmlook_apply_edit`

### 3. [AI] PDF cell 한 개 cite — 8000 → 8200

좌측 brief 에서 *"8,000"* 숫자 드래그-선택 (또는 우측 PDF 의 해당 셀).

LLM 에:

> *"4월 reliability bulletin 에 따라 8000 cycles 가 8200 cycles 로 정정됐어.
> brief 와 cite anchor 둘 다 업데이트."*

LLM 이 `htmlook_apply_edit` 로 brief.md 의 숫자 + cite 텍스트 동시 patch.

### 4. [VIEW] 우측 reload

- brief 가 새 숫자 + 새 ranking 점수로 갱신됨
- (PDF 도 재생성된 버전으로 교체된 상태 — `after/vendor.pdf`)

### 5. [AI 없는 사용자] before/after 비교

- 좌측: `05-domain-battery/before/brief.md` + `before/vendor.pdf`
- 우측: `05-domain-battery/after/brief.md` + `after/vendor.pdf`

## 검증 포인트

- ✅ `htmlook_pane_pair` (md + pdf)
- ✅ `htmlook_cite` (PDF row anchor)
- ✅ `htmlook_apply_edit` (brief patch)
- ⚠️ Kokoro brief 음성, Whisper 자막은 외부 CLI

## 다음 페르소나

`06-economy-analyst/` — 9:16 portrait 매크로 brief 카드
