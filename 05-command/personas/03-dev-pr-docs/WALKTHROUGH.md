# 03 · dev-pr-docs — PR diff 와 stale docs 동시에 보고 patch

> 영상: `demo/persona_units/dev-pr-docs/renders/dev-pr-docs_voiced_bgm.en+ko.mp4`

PR 머지 시 *문서가 stale 됐다* 는 사실은 보통 한 두 주 뒤에 발견됩니다.
HTMLook + LLM 으로 PR 직후에 같은 화면에서 잡습니다.

## 사전 준비

- HTMLook Pro
- (선택) Claude / Llama / 호환 클라이언트

## 단계

### 1. [VIEW] 좌측 PR diff, 우측 docs

- 좌측: `03-dev-pr-docs/pr.diff` 더블클릭
- 우측: `03-dev-pr-docs/docs.md` 더블클릭
- diff 가 `since` → `from` 으로 query param 을 리네임 했음. docs 는 아직 `since`.

### 2. [AI] drift 찾기 요청

LLM 에:

> *"좌측 diff 와 우측 docs 를 비교해서 머지하면 stale 되는 문장을 모두 cite
> 해 줘."*

LLM 이 MCP 로:

1. `htmlook_pane_pair` 로 좌·우 파일 확보
2. diff 의 `since`→`from` hunk 와 docs 의 query parameters 표 / 예시 / 에러 섹션 매칭
3. `htmlook_cite` 로 stale 라인 anchor

### 3. [AI] docs patch + apply_edit

> *"위 stale 라인 모두 새 API (from, ISO-8601) 에 맞게 업데이트하고 PR 링크
> 한 줄 적어 줘."*

LLM 이 `htmlook_apply_edit` 로 docs.md 에 patch — `since` → `from`, 타입 number → string,
예시도 ISO-8601 로.

### 4. [VIEW] 우측 reload 확인

- 자동 reload, 새 docs 가 보임
- *"Renamed from since (unix ms) in PR #a3f1c20"* 같은 마이그레이션 노트가
  굵게 표시됨

### 5. [AI 없는 사용자] before/after 비교

- 좌측: `03-dev-pr-docs/before/docs.md`
- 우측: `03-dev-pr-docs/after/docs.md`

## 검증 포인트

- ✅ `htmlook_pane_pair` (PR + docs)
- ✅ `htmlook_cite` (diff hunk → docs line)
- ✅ `htmlook_apply_edit` (docs patch)
- ⚠️ Kokoro recap 단계는 외부 CLI (`npx hyperframes tts`)

## 다음 페르소나

`04-creator-podcast/` — 인터뷰 transcript 에서 quotable 20초 찾기
