# HTMLook Campus

> HTMLook Pro 학습 자료의 모든 것 — **기본 6편 → 고급 11편 → 26 직군 페르소나
> + 49 sample workspace seed** 를 한곳에. 30 분 안에 첫 워크플로우 완료.

이 레포는 **HTMLook Pro v1.0 release-candidate (출시 2026 mid)** 기준으로
작성됐습니다. 데스크탑 앱은 [htmlook.app](https://htmlook.app) 에서 14일
무료 체험. BYOM (Bring-Your-Own-Model) 이라 토큰 마진 0 — Claude · GPT · Gemini ·
DeepSeek · Mistral · Together · Groq · Cerebras · Ollama 어느 모델이든
사용자의 키로 직접 호출.

> 처음이면 deep-dive 데모부터: [lv1](https://htmlook.app/demos/lv1.html) ·
> [lv2](https://htmlook.app/demos/lv2.html) · [lv3](https://htmlook.app/demos/lv3.html).

## 학습 순서 (권장)

이 캠퍼스는 *3-stage* 로 설계. 앞 단계가 다음 단계의 사전 지식이 됩니다.

> 📚 **[`docs/LEARNING_PATH.md`](docs/LEARNING_PATH.md)** — 전체 권장 순서 + 시간 추정

## Heavyweight Profiles (v1.0 카탈로그 · 8종 bundled)

도메인 워크스페이스 sample 외에 **본격 도구 8종** Profile 패키지 — HTMLook Pro
앱에 동봉되어 첫 launch 시 `~/.htmlook/profiles/_bundled-*` 에 자동 unpack.
**New Workspace Wizard** (⌘⇧N) 또는 **Add wizard** (탐색식 카탈로그) 에서
즉시 선택, `File → Profile → Install from URL` 로 외부 Profile 설치도
지원.

| Profile | 카테고리 | 출력 | 도구 라이선스 |
|---------|---------|------|-------------|
| [HyperFrames](profiles/hyperframes/) | motion-graphics | mp4 (kinetic typography) | MIT |
| [Slidev](profiles/slidev/) | presentation | HTML/PDF slides | MIT |
| [Quarto](profiles/quarto/) | publishing | PDF/HTML/PPT/book | GPL-2.0 |
| [D2](profiles/d2/) | diagram | SVG | MPL-2.0 |
| [Astro Starlight](profiles/astro-starlight/) | documentation | docs site | MIT |
| [Marimo](profiles/marimo/) | notebook | reactive HTML | Apache-2.0 |
| [Excalidraw](profiles/excalidraw/) | diagram | JSON/SVG/PNG | MIT |
| [Manim](profiles/manim/) | educational-animation | mp4 | BSD-3-Clause |

> 각 Profile = `profile.json` + `SKILL.md` + `seed/` 시드 콘텐츠. HTMLook 은 도구를
> 번들하지 않고 사용 가이드 / Wizard 통합만 제공 (사용자가 외부 도구는 별도 설치).

전체 카탈로그: [`catalog.json`](catalog.json) — 현재 **57 entries** (8 Profile +
49 workspace seed). CI 자동 갱신 (`scripts/build-catalog.mjs`).
워크스페이스 seed 본문은 [`sample_workspaces/`](sample_workspaces/) (75 폴더 ·
Wave A 11 high-quality + Wave B 24 mid + Wave C 14 light · marimo / d2 /
manim / quarto / slidev / astro / excalidraw / hyperframes 도메인 별).

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

1. **HTMLook Pro 설치** — [htmlook.app](https://htmlook.app) 에서 .dmg 다운로드
   (Mac 우선 출시 · Win / iPad 후속). **14 일 무료 체험** 모든 기능 활성화.
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
   `WALKTHROUGH.md` 따라하기. 추가로 `sample_workspaces/` 49 seed 카탈로그도
   Wizard 의 시드 카드로 한 클릭 설치 가능.

## 두 layer 의 학습 — 영상 + 인터랙티브

이 캠퍼스의 영상은 *what (무엇이 되는지)*. HTMLook Pro 내장 인터랙티브
walkthrough 는 *how (어떻게 하는지)*. 둘이 함께.

| Layer | 어디서 | 길이 | 역할 |
|---|---|---|---|
| 영상 (캠퍼스) | `videos/features/`, `videos/` | 30 s / 60-70 s | 결과 보여주기 |
| 인터랙티브 (앱) | HTMLook Pro · Settings → Tutorials | 4 step | 직접 따라하기 |

영상에 등장하는 17 feature 모두 인터랙티브 가이드가 1:1 매칭됩니다.

## AI 협업 (선택)

ADVANCED 영상 + Stage 3 페르소나 절반 정도가 LLM cite/apply_edit 흐름을 가정.
v1.0 부터는 다음 세 가지 중 어느 것이나 사용 가능:

- **HTMLook Pro 내장 BYOM 채팅 (권장)** — Settings → Models 에서 사용자가
  보유한 키 등록. Claude / GPT / Gemini / DeepSeek / Mistral / Together / Groq /
  Cerebras / Ollama (로컬) 9 vendor 지원. 토큰 마진 0 — 사용자가 vendor 에
  직접 결제. 내장 패널에서 cite anchor / apply_edit 흐름이 그대로 동작.
- **HTMLook Pro 내장 Terminal + CLI 어댑터** — ⌘J 토글 PTY 터미널에서
  `claude` · `codex` · `gemini` CLI 가 워크스페이스 컨텍스트로 자동 연결
  (UserPromptSubmit hook → htmlook --snapshot live state).
- **외부 MCP 클라이언트** — Claude Code / Cursor / Windsurf / Zed →
  `samples/.htmlook/mcp-config.example.json` 의 설정을 각 클라이언트 mcp.json 에
  병합. HTMLook Pro 의 MCP 서버는 `htmlook_*` 도구 22여종 (cite, apply_edit,
  selection, region_current_png, outline, link, video_*, …) 노출.

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

이 레포는 **HTMLook Pro v1.0 release-candidate** (정식 출시 2026 mid 예정)
와 동기화된 학습 자료. v1.0 GA 시점에 함께 public 전환 + 카탈로그 endpoint
(`htmlook.app/catalog`) 가 이 레포의 raw URL 을 fresh-fetch (24h cache).

## 에디션

- **HTMLook Pro** (v1.0) — 파워 유저용. BYOM 채팅 + 내장 PTY terminal +
  CLI 어댑터 (claude / codex / gemini) + MCP bridge + paint canvas + region
  capture + element pick + save-as-skill + 8 bundled Profile + 49 seed.
- **HTMLook Easier** (v1.x 후속, planned) — 처음 쓰는 사람용. 번들 AI ·
  단순 UI · 학생 / 입문자 가격대. 자세한 출시는 후속 발표.

## 관련 프로젝트

- **HTMLook Pro** 본 레포: 비공개 (v1.0 GA 시점에 공개 예정)
- 페르소나 영상 raw composition: HTMLook 본 레포의 `demo/persona_units/`
- Feature 영상 raw composition: `demo/feature_units/`
- Deep-dive 데모 페이지: [`htmlook.app/demos/lv1.html`](https://htmlook.app/demos/lv1.html) ·
  [`lv2.html`](https://htmlook.app/demos/lv2.html) ·
  [`lv3.html`](https://htmlook.app/demos/lv3.html)
