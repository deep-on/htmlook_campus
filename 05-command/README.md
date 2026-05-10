# Step 5 · Command (Terminal / Chat / Apply)

> Step 4 에서 *어디* 를 짚는 법을 익혔으면, 이번 step 은 그것을 *명령* 으로
> 바꾸는 법. cite + apply_edit 사이클.
> ~ 10 분.

이번 step 이 캠퍼스의 deepest part — 26 페르소나 walkthrough 가 여기 들어
있습니다 ([`personas/`](personas/)). 처음에는 자기 도메인 1편만 따라 해도
충분.

## 5.1 · 4 가지 명령 패턴

| 패턴 | 어디서 | 입력 형태 |
|---|---|---|
| **Chat (BYOM 채팅)** | 우측 AI 패널 | 자연어 + cite anchor 자동 첨부 |
| **Terminal CLI** | ⌘J 토글, 그 안에서 `claude` / `codex` / `gemini` | shell prompt |
| **외부 MCP 클라이언트** | Claude Code / Cursor / Windsurf / Zed | 그 클라이언트의 채팅창 |
| **Inline cite link** | 응답 내 `[B14](xlsx://q3.xlsx#B14)` | 클릭 → 그 위치로 jump |

## 5.2 · Cite + apply_edit 사이클

```
[Step 4 에서 영역 짚기]
   → cite anchor 가 AI 패널에 첨부
   → 자연어 prompt
   → LLM 이 htmlook_apply_edit 호출
   → 파일 변경
   → file watcher 가 우측 pane 자동 reload
```

핵심 영상 4 편 (각 30 s):

| # | 영상 | 패턴 |
|---|---|---|
| 7 | [Cite the cell. Get the narrative.](../videos/features/07-advanced-01-xlsx-cite.mp4) | xlsx 셀 cite |
| 8 | [14:14 → paragraph.](../videos/features/08-advanced-02-live-cue-cite.mp4) | 영상 timestamp cite |
| 9 | [One cite. Three files.](../videos/features/09-advanced-03-multi-target.mp4) | 한 cite → 여러 파일 patch |
| 17 | [Cross-file anchors. Recorded.](../videos/features/17-advanced-11-cross-link.mp4) | `.htmlook/links.json` sidecar |

## 5.3 · 페르소나 walkthrough (26편)

자기 직군 / 도메인의 *1-day-in-the-life* 워크플로우. 60-70 초 mp4 +
follow-along 가능한 sample workspace + step-by-step `WALKTHROUGH.md`.

자세한 카탈로그: [`personas/INDEX.md`](personas/INDEX.md). 권장 순서는
직군 별로 grouping 돼 있습니다:

- **개발**: [`personas/01-hf-claude/`](personas/01-hf-claude/) →
  [`02-hf-llama/`](personas/02-hf-llama/) →
  [`03-dev-pr-docs/`](personas/03-dev-pr-docs/)
- **콘텐츠**: [`personas/04-creator-podcast/`](personas/04-creator-podcast/) →
  [`12-press-editor/`](personas/12-press-editor/) →
  [`15-picture-book/`](personas/15-picture-book/) →
  [`22-hobby-fiction/`](personas/22-hobby-fiction/)
- **분석**: [`personas/09-data-analyst/`](personas/09-data-analyst/) →
  [`11-finance-report/`](personas/11-finance-report/) →
  [`10-research-notes/`](personas/10-research-notes/) →
  [`06-economy-analyst/`](personas/06-economy-analyst/)
- **법무 / 번역**: [`personas/08-legal-redline/`](personas/08-legal-redline/) →
  [`07-translator-book/`](personas/07-translator-book/) →
  [`05-domain-battery/`](personas/05-domain-battery/)
- **교육 (선생님)**: [`personas/17-teacher-quiz/`](personas/17-teacher-quiz/) →
  [`18-teacher-newsletter/`](personas/18-teacher-newsletter/) →
  [`19-teacher-record/`](personas/19-teacher-record/)
- **교육 (학생)**: [`personas/20-student-notes/`](personas/20-student-notes/) →
  [`24-student-flashcard/`](personas/24-student-flashcard/) →
  [`23-homework-helper/`](personas/23-homework-helper/) →
  [`21-kid-coding/`](personas/21-kid-coding/) →
  [`14-kids-science-mag/`](personas/14-kids-science-mag/)
- **비즈니스**: [`personas/16-corp-deck/`](personas/16-corp-deck/) →
  [`13-product-prd/`](personas/13-product-prd/)
- **일상**: [`personas/25-recipe-card/`](personas/25-recipe-card/) →
  [`26-mobile-news/`](personas/26-mobile-news/)

## 5.4 · 따라하기 패턴

각 페르소나 폴더 안에:

- `WALKTHROUGH.md` — 단계별 가이드 (`[VIEW]` / `[AI]` 마크)
- `before/` — edit 전 상태 (시각 비교용)
- `after/` — edit 후 상태 (LLM 없는 사용자도 결과 확인)
- 도메인 콘텐츠 파일 (md / html / pdf / xlsx / svg / py / mp3 등)

## 5.5 · LLM-agnostic — vendor swap

같은 cite + apply_edit 워크플로우가 vendor 9 종 어디서나 동일하게 동작.
[Step 3](../03-byom-setup/) 에서 다른 vendor 추가하고 swap 해 보면 동일 결과.

## ✅ Step 5 체크포인트

- 자기 직군의 페르소나 1편 영상 (60-70 s) 시청.
- 그 페르소나 폴더의 `WALKTHROUGH.md` 의 `[VIEW]` 단계까지 따라함.
- (AI 있다면) `[AI]` 단계까지 실행 → 우측 pane 이 reload 되는 것 확인.
- (AI 없다면) `before/` 와 `after/` 를 분할뷰로 비교.

다 맞으면 → [Step 6 · save-as-skill](../06-save-as-skill/) — 자주 쓰는 워크플로우를
앱에 영구히 등록.

## 더 자세히

- [`personas/INDEX.md`](personas/INDEX.md) — 26 페르소나 카탈로그 + 영상 ↔ 폴더
  매핑.
- [`personas/README.md`](personas/README.md) — sample workspace 사용법.
- [`../03-byom-setup/AI_GUIDE.md`](../03-byom-setup/AI_GUIDE.md) — MCP 도구 22여종
  + AI agent 출력 톤 가이드.
