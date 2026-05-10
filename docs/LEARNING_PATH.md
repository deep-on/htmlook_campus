# Learning Path

> HTMLook 을 처음 접하는 사용자가 따라야 할 권장 순서. **BASIC → ADVANCED →
> Sample Workspaces** (선택: → Profile 카탈로그). 각 단계는 앞 단계의 개념 위에
> 쌓입니다. v1.0 release-candidate 기준.

## Stage 1 · BASIC (6편) — *처음 보는 사람*

HTMLook 의 *뷰어* 본질을 알리는 6편. 워크스페이스 / AI / MCP 모두 없이도
가치가 있다는 점. 30 초씩.

| # | 영상 | 핵심 약속 | 사전 지식 |
|---|---|---|---|
| 1 | [Drop. Open. Done.](../videos/features/01-basic-01-drop-open.mp4) | 어떤 파일이든 드래그 앤 드롭으로 열림 | 0 |
| 2 | [Folder ready.](../videos/features/02-basic-02-workspace.mp4) | 폴더 하나로 프로젝트 사이드바 자동 구성 | #1 |
| 3 | [Type left. See right. Live.](../videos/features/03-basic-03-md-live-edit.mp4) | 마크다운 라이브 에디팅 + 분할뷰 | #2 |
| 4 | [Click anything. Edit it.](../videos/features/04-basic-04-html-split.mp4) | HTML element 클릭 → 직접 수정 (양방향 sync) | #3 |
| 5 ⭐ | [Drag. Tell the LLM.](../videos/features/05-basic-05-region-cite.mp4) | 영역 드래그 → AI cite anchor (AI 진입점) | #4 |
| 6 | [Pick what you see.](../videos/features/06-basic-06-html-4mode.mp4) | HTML 선택 4가지 (element/range/region/outline) | #5 |

각 영상 시청 후 **HTMLook Pro 의 Settings → Tutorials** 에서 같은 이름의
인터랙티브 가이드를 실행하면 실제 UI 에서 직접 따라할 수 있습니다 (spotlight
+ tooltip 4 step).

## Stage 2 · ADVANCED (11편) — *AI 협업 깊이*

BASIC #5 에서 AI cite 개념을 처음 만난 사용자가 다음으로 볼 11편. 각 30 초,
HTMLook 의 MCP 도구 (htmlook_cite, htmlook_apply_edit 등) 를 활용하는 다양한
패턴.

### 1차 (3편) — magic moment 명확

| # | 영상 | MCP 도구 |
|---|---|---|
| 7 | [Cite the cell. Get the narrative.](../videos/features/07-advanced-01-xlsx-cite.mp4) | htmlook_cite (xlsx) + htmlook_apply_edit |
| 8 | [14:14 → paragraph.](../videos/features/08-advanced-02-live-cue-cite.mp4) | htmlook_cite (video) + htmlook_apply_edit |
| 9 | [One cite. Three files.](../videos/features/09-advanced-03-multi-target.mp4) | htmlook_cite + multi htmlook_apply_edit |

### 2차 (4편) — 차별점 강조

| # | 영상 | 도구/단축키 |
|---|---|---|
| 10 | [Two keys. Three views.](../videos/features/10-advanced-04-multi-pane.mp4) | ⌘D + ⌘J |
| 11 | [It just reloaded.](../videos/features/11-advanced-05-auto-reload.mp4) | file watcher |
| 12 | [Add a tool. Three fields.](../videos/features/12-advanced-06-tool-wizard.mp4) | htmlook_workspace_tools |
| 13 | [Swap the LLM. Keep the workflow.](../videos/features/13-advanced-07-mcp-swap.mp4) | MCP server (LLM-agnostic) |

### 3차 (4편) — 보강

| # | 영상 | MCP 도구 |
|---|---|---|
| 14 | [Click sentence 5. Clip ships.](../videos/features/14-advanced-08-sentence-id.mp4) | htmlook_cite (sentence:N) |
| 15 | [Frame check. No scrub.](../videos/features/15-advanced-09-thumbnail.mp4) | htmlook_active_file_thumbnail |
| 16 | [Click §3.2. You're there.](../videos/features/16-advanced-10-outline.mp4) | htmlook_outline |
| 17 | [Cross-file anchors. Recorded.](../videos/features/17-advanced-11-cross-link.mp4) | htmlook_link / htmlook_links |

## Stage 3 · Sample Workspaces (26 페르소나) — *도메인 별 deep dive*

BASIC + ADVANCED 로 도구 사용법을 익혔으면, 이제 **자기 도메인** 에서 실제
워크플로우 적용. 26 페르소나 각각 = 한 직군의 1-day-in-the-life. 60-70 초
walkthrough mp4 + 따라하기 sample workspace + step-by-step `WALKTHROUGH.md`.

### 권장 시청 순서 (직군 별 grouping)

#### 개발

[hf-claude](../samples/01-hf-claude/) → [hf-llama](../samples/02-hf-llama/) →
[dev-pr-docs](../samples/03-dev-pr-docs/)

#### 콘텐츠 제작

[creator-podcast](../samples/04-creator-podcast/) →
[press-editor](../samples/12-press-editor/) →
[picture-book](../samples/15-picture-book/) →
[hobby-fiction](../samples/22-hobby-fiction/)

#### 분석 / 리포팅

[data-analyst](../samples/09-data-analyst/) →
[finance-report](../samples/11-finance-report/) →
[research-notes](../samples/10-research-notes/) →
[economy-analyst](../samples/06-economy-analyst/)

#### 법무 / 번역

[legal-redline](../samples/08-legal-redline/) →
[translator-book](../samples/07-translator-book/) →
[domain-battery](../samples/05-domain-battery/)

#### 교육 (선생님)

[teacher-quiz](../samples/17-teacher-quiz/) →
[teacher-newsletter](../samples/18-teacher-newsletter/) →
[teacher-record](../samples/19-teacher-record/)

#### 교육 (학생)

[student-notes](../samples/20-student-notes/) →
[student-flashcard](../samples/24-student-flashcard/) →
[homework-helper](../samples/23-homework-helper/) →
[kid-coding](../samples/21-kid-coding/) →
[kids-science-mag](../samples/14-kids-science-mag/)

#### 비즈니스

[corp-deck](../samples/16-corp-deck/) →
[product-prd](../samples/13-product-prd/)

#### 일상

[recipe-card](../samples/25-recipe-card/) →
[mobile-news](../samples/26-mobile-news/)

### 따라하기 패턴

각 페르소나 폴더 안에:

- `WALKTHROUGH.md` — 단계별 가이드
- `before/` — edit 전 상태 (시각 비교용)
- `after/` — edit 후 상태 (LLM 없는 사용자도 결과 확인)
- 도메인 콘텐츠 파일들 (md / html / pdf / xlsx / svg / py / mp3 등)

## Stage 4 · Heavyweight Profiles (선택) — *본격 도구 8종*

26 페르소나로 HTMLook 활용 패턴을 익혔으면, 깊은 도구로 넘어가기. v1.0 부터
8 Profile 이 앱에 동봉되어 New Workspace Wizard / Add wizard 의 카드로 한
클릭 설치:

| Profile | 시작 시드 폴더 |
|---------|-------------|
| HyperFrames (motion-graphics) | [`profiles/hyperframes/`](../profiles/hyperframes/) |
| Slidev (presentation) | [`profiles/slidev/`](../profiles/slidev/) |
| Quarto (publishing) | [`profiles/quarto/`](../profiles/quarto/) |
| D2 (diagram) | [`profiles/d2/`](../profiles/d2/) |
| Astro Starlight (docs site) | [`profiles/astro-starlight/`](../profiles/astro-starlight/) |
| Marimo (notebook) | [`profiles/marimo/`](../profiles/marimo/) |
| Excalidraw (whiteboard) | [`profiles/excalidraw/`](../profiles/excalidraw/) |
| Manim (animation) | [`profiles/manim/`](../profiles/manim/) |

각 Profile 카테고리에 추가 시드 49 종이 [`sample_workspaces/`](../sample_workspaces/)
에 있음 (Wave A 11 high-quality + Wave B 24 mid + Wave C 14 light).

## 학습 시간 추정

- **Stage 1 (BASIC)**: 30 s × 6 = 3 min 시청 + 인터랙티브 가이드 30 s × 6 = 3 min · **합계 ~6 min**
- **Stage 2 (ADVANCED)**: 30 s × 11 = 5.5 min 시청 + 인터랙티브 30 s × 11 = 5.5 min · **합계 ~11 min**
- **Stage 3 (Sample Workspaces)**: 직군 1편 평균 60 s 영상 + 5–10 min 따라하기. 자기 직군 1편만 해도 충분 · **~10 min**
- **Stage 4 (Heavyweight Profile · 선택)**: 도구 1종 시드 5–15 min · 본격
  사용은 도구 자체 학습 시간 별도.

처음 onboarding **30 분 이내** 에 HTMLook 의 모든 핵심 기능 + 자기 도메인
워크플로우까지 학습 완료.

## 다음 단계

이 캠퍼스를 다 봤으면 더 깊은 Reference 로:

- [`docs/PRODUCTION.md`](PRODUCTION.md) — 영상이 어떻게 만들어졌는지 (역검증 원칙 포함)
- [`docs/FEATURES.md`](FEATURES.md) — 17 feature 영상 카탈로그 (hooks + accent)
- [`docs/INDEX.md`](INDEX.md) — 26 페르소나 카탈로그
- [`catalog.json`](../catalog.json) — Profile + workspace seed 카탈로그 (앱
  Wizard 가 fresh-fetch)
- Deep-dive 데모: [htmlook.app/demos/lv1.html](https://htmlook.app/demos/lv1.html) ·
  [lv2](https://htmlook.app/demos/lv2.html) · [lv3](https://htmlook.app/demos/lv3.html)
