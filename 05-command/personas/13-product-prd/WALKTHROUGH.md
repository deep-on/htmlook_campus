# 13 · product-prd — PRD §3.2 cite + 와이어프레임 + 티켓 한번에

> 영상: `demo/persona_units/product-prd/renders/product-prd_voiced_bgm.en+ko.mp4`

PRD 한 섹션을 cite 하면 wireframe + tickets + PRD version 이 한 round trip 에
업데이트되는 multi-target apply_edit 시연.

## 사전 준비

- HTMLook Pro
- (선택) LLM

## 단계

### 1. [VIEW] 좌측 prd.md, 우측 wireframe.html, 사이드바 tickets.md

- 좌측: `13-product-prd/prd.md` (v0.3)
- 우측: `13-product-prd/wireframe.html` — chip-rail 자리만 stub 으로 표시됨
- (선택) 사이드바에 `tickets.md` 도 열어 두기

### 2. [AI] §3.2 cite + multi-target apply_edit

좌측 PRD 의 §3.2 chip-rail 섹션 드래그-선택.

LLM 에:

> *"이 섹션 cite 한 후 (a) wireframe 에 chip-rail 마운트, (b) tickets.md 에
> PROD-1234 ticket 작성, (c) PRD 버전을 0.3 → 0.4 로 올려줘. 한번에."*

LLM 이:
1. `htmlook_cite` 로 §3.2 anchor
2. `htmlook_apply_edit` 3 회 (또는 multi-target 한 번):
   - wireframe.html: stub `<div class="stub">` 제거 + `<nav class="chip-rail">` 추가
   - tickets.md: PROD-1234 prepend
   - prd.md: version 0.3 → 0.4, §3.2 아래에 *"Tracked by PROD-1234"* note

### 3. [VIEW] 우측 reload

- chip-rail 이 run table 위에 마운트 (Status / Machine / Operator / Shift + Clear)
- tickets.md 에 PROD-1234 추가
- prd.md 가 0.4 로 표시 + acceptance 첫 항목 체크

### 4. [AI 없는 사용자] before/after 비교

- 좌측 셋: `13-product-prd/before/{prd.md,wireframe.html,tickets.md}`
- 우측 셋: `13-product-prd/after/{prd.md,wireframe.html,tickets.md}`

## 검증 포인트

- ✅ `htmlook_pane_pair` (PRD + wireframe)
- ✅ `htmlook_cite` (PRD §3.2)
- ✅ `htmlook_apply_edit` (3 파일 동시 patch — multi-target)
- ✅ PRD 버전 bump + ticket 동기화

## 다음 페르소나

`14-kids-science-mag/` — 어른용 과학 단락 → kids portrait 매거진
