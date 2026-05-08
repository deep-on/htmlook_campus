# HTMLook Campus

> HTMLook Pro 학습 자료의 모든 것 — **기본 6편 → 고급 11편 → 26 직군 sample**
> 순서로 30 분 안에 첫 워크플로우 완료.

## 학습 순서 (권장)

이 캠퍼스는 *3-stage* 로 설계. 앞 단계가 다음 단계의 사전 지식이 됩니다.

> 📚 **[`docs/LEARNING_PATH.md`](docs/LEARNING_PATH.md)** — 전체 권장 순서 + 시간 추정

## Heavyweight Profiles (v1.0 카탈로그)

도메인 워크스페이스 sample 외에 **본격 도구 7종** Profile 패키지 — HTMLook Pro
의 New Workspace Wizard 에서 즉시 선택 / `File → Install Profile from URL` 로
지원.

| Profile | 카테고리 | 출력 | 도구 라이선스 |
|---------|---------|------|-------------|
| [Slidev](profiles/slidev/) | presentation | HTML/PDF slides | MIT |
| [Quarto](profiles/quarto/) | publishing | PDF/HTML/PPT/book | GPL-2.0 |
| [D2](profiles/d2/) | diagram | SVG | MPL-2.0 |
| [Astro Starlight](profiles/astro-starlight/) | documentation | docs site | MIT |
| [Marimo](profiles/marimo/) | notebook | reactive HTML | Apache-2.0 |
| [Excalidraw](profiles/excalidraw/) | diagram | JSON/SVG/PNG | MIT |
| [Manim](profiles/manim/) | educational-animation | mp4 | BSD-3-Clause |

> 각 Profile = `profile.json` + `SKILL.md` + `seed/` 시드 콘텐츠. HTMLook 은 도구를
> 번들하지 않고 사용 가이드 / Wizard 통합만 제공 (사용자가 도구는 별도 설치).

전체 카탈로그: [`catalog.json`](catalog.json) (CI 자동 갱신).

### Stage 1 · BASIC (6편) — 처음 보는 사람

HTMLook = 뷰어 본질. 워크스페이스 / AI 모두 없이도 가치. 30 초씩.

1. [Drop. Open. Done.](videos/features/01-basic-01-drop-open.mp4)
2. [Folder ready.](videos/features/02-basic-02-workspace.mp4)
3. [Type left. See right. Live.](videos/features/03-basic-03-md-live-edit.mp4)
4. [Click anything. Edit it.](videos/features/04-basic-04-html-split.mp4)
5. ⭐ [Drag. Tell the LLM.](videos/features/05-basic-05-region-cite.mp4)
6. [Pick what you see.](videos/features/06-basic-06-html-4mode.mp4)

### Stage 2 · ADVANCED (11편) — AI 협업 깊이

BASIC #5 에서 cite 개념을 만난 후, MCP 도구를 활용하는 11가지 패턴.

- 1차 (3편): xlsx-cite · live-cue · multi-target
- 2차 (4편): multi-pane · auto-reload · tool-wizard · MCP swap
- 3차 (4편): sentence-id · thumbnail · outline · cross-link

전체 catalog: [`docs/FEATURES.md`](docs/FEATURES.md)

### Stage 3 · Sample Workspaces (26 페르소나) — 도메인 별 deep dive

자기 직군의 *1-day-in-the-life* 워크플로우. 60-70 초 walkthrough 영상 +
따라하기 가능한 sample workspace + step-by-step `WALKTHROUGH.md`.

분류 (직군 별 시청 순서):

- **개발** (3): hf-claude · hf-llama · dev-pr-docs
- **콘텐츠** (4): creator-podcast · press-editor · picture-book · hobby-fiction
- **분석** (4): data-analyst · finance-report · research-notes · economy-analyst
- **법무/번역** (3): legal-redline · translator-book · domain-battery
- **교육 (선생님)** (3): teacher-quiz · teacher-newsletter · teacher-record
- **교육 (학생)** (5): student-notes · student-flashcard · homework-helper · kid-coding · kids-science-mag
- **비즈니스** (2): corp-deck · product-prd
- **일상** (2): recipe-card · mobile-news

전체 catalog: [`docs/INDEX.md`](docs/INDEX.md)

## 빠르게 시작

1. **HTMLook Pro 설치** — [htmlook.app](https://htmlook.app) (혹은 자체 빌드)
2. 이 레포 clone:
   ```bash
   git clone git@github.com:deep-on/htmlook_campus.git
   cd htmlook_campus
   ```
3. `videos/features/01-basic-01-drop-open.mp4` 부터 순서대로 시청
4. 각 BASIC / ADVANCED 영상 시청 후 — HTMLook Pro 의 **Settings → Tutorials**
   탭에서 같은 이름의 인터랙티브 가이드 실행 (실제 UI 위에 spotlight + tooltip,
   4 step)
5. Stage 3 → `samples/` 폴더를 HTMLook 에서 *Open Folder* 로 열고 자기 직군의
   `WALKTHROUGH.md` 따라하기

## 두 layer 의 학습 — 영상 + 인터랙티브

이 캠퍼스의 영상은 *what (무엇이 되는지)*. HTMLook Pro 내장 인터랙티브
walkthrough 는 *how (어떻게 하는지)*. 둘이 함께.

| Layer | 어디서 | 길이 | 역할 |
|---|---|---|---|
| 영상 (캠퍼스) | `videos/features/`, `videos/` | 30 s / 60-70 s | 결과 보여주기 |
| 인터랙티브 (앱) | HTMLook Pro · Settings → Tutorials | 4 step | 직접 따라하기 |

영상에 등장하는 17 feature 모두 인터랙티브 가이드가 1:1 매칭됩니다.

## AI 협업 (선택)

ADVANCED 영상 + Stage 3 페르소나 절반 정도가 MCP-aware LLM 클라이언트를 가정.
다음 둘 중 하나면 됩니다:

- **Claude Code / Cursor / Windsurf** — `samples/.htmlook/mcp-config.example.json`
  의 설정을 클라이언트 mcp.json 에 병합
- **로컬 Llama via Ollama** — 동일 설정으로 로컬 LLM 사용

LLM 없는 사용자도 각 페르소나 폴더의 `before/` `after/` 로 결과를 시각 비교 가능.

자세한 가이드: `samples/CLAUDE.md`

## 역검증 약속 (Reverse Verification)

이 캠퍼스의 모든 영상은 **실제 HTMLook 동작과 일치하는 claim 만** 합니다.
없는 기능은 광고하지 않습니다 (페르소나 26편 + feature 17편 모두 production
시점에 source-level 검증 통과).

자세한 검증 절차 + 이번 빌드에서 fix 된 false claims 목록: [`docs/PRODUCTION.md`](docs/PRODUCTION.md)

## 문서

- [`docs/LEARNING_PATH.md`](docs/LEARNING_PATH.md) — 전체 학습 순서 + 시간 추정
- [`docs/FEATURES.md`](docs/FEATURES.md) — 17 feature 영상 카탈로그 (hooks, accents)
- [`docs/INDEX.md`](docs/INDEX.md) — 26 페르소나 카탈로그
- [`docs/PRODUCTION.md`](docs/PRODUCTION.md) — 영상 제작 표준, 역검증 절차

## 라이선스

- 코드 / 워크스루 텍스트: MIT
- 영상 mp4: CC BY 4.0 (사용 시 *"HTMLook Campus"* 출처 표기)
- 샘플 콘텐츠 (PDF / xlsx / md / html): CC0 / public domain — 모두 fictional placeholder

## 상태

이 레포는 *private preview*. HTMLook Pro 정식 출시 시점에 public 전환 예정.

## 관련 프로젝트

- **HTMLook Pro** 본 레포: 비공개 (정식 출시 시 공개)
- 페르소나 영상 raw composition: HTMLook 본 레포의 `demo/persona_units/`
- Feature 영상 raw composition: `demo/feature_units/`
