# HTMLook Campus

> HTMLook Pro 를 처음 사용하는 사람을 위한 **8 step 튜토리얼**. 한 step 씩
> 차례로 따라가면 30-40 분 안에 install → 첫 파일 → BYOM → editing →
> command → save-as-skill → bundled profiles → 자기 profile 작성까지 완주.

이 레포는 **HTMLook Pro v1.0 release-candidate** (정식 출시 2026 mid 예정)
기준으로 작성됐습니다. 데스크탑 앱은 [htmlook.app](https://htmlook.app) 에서
14 일 무료 체험. BYOM (Bring-Your-Own-Model) 이라 토큰 마진 0 — Claude · GPT ·
Gemini · DeepSeek · Mistral · Together · Groq · Cerebras · Ollama 어느 모델이든
사용자의 키로 직접 호출.

## Tutorial Path

위에서 아래로 순서대로. 각 step 은 앞 step 의 동작 위에 쌓입니다.

| Step | 폴더 | 무엇을 합니까 | 시간 |
|---|---|---|---|
| 1 | [`01-getting-started/`](01-getting-started/) | install · 첫 launch · drag-drop · open folder | 3 min |
| 2 | [`02-first-file/`](02-first-file/) | md / html / pdf / 영상 4 종 + 분할뷰 + outline | 5 min |
| 3 | [`03-byom-setup/`](03-byom-setup/) | vendor 1 개 골라서 키 등록 (또는 Ollama) | 5 min |
| 4 | [`04-editing/`](04-editing/) | element pick · region paint · sentence-id · cite anchor | 5 min |
| 5 | [`05-command/`](05-command/) | chat · terminal CLI · apply_edit · 26 페르소나 walkthrough | 10 min |
| 6 | [`06-save-as-skill/`](06-save-as-skill/) | 워크플로우 캡처 → ⌘K 카탈로그 카드 | 5 min |
| 7 | [`07-bundled-profiles/`](07-bundled-profiles/) | HyperFrames · Slidev · Quarto · D2 · Astro · Marimo · Excalidraw · Manim 둘러보기 | 5 min |
| 8 | [`08-extend/`](08-extend/) | 자기 profile 작성 + 카탈로그 PR | 선택 |

> 빠르게 둘러보기만 원하면 [`01-getting-started/LEARNING_PATH.md`](01-getting-started/LEARNING_PATH.md)
> 의 step → 영상 mapping 을 참고. 각 영상 30-70 초.

## Step 1 — 설치 + 첫 launch

[`01-getting-started/README.md`](01-getting-started/README.md) 부터 시작.

[htmlook.app](https://htmlook.app) 에서 .dmg 받고, Applications 로 끌고,
첫 파일을 drag-drop 해 보세요.

## Step 2 — 첫 파일 (HTML / MD / PDF / 영상)

[`02-first-file/README.md`](02-first-file/README.md). 4 가지 파일 종류를
분할뷰 + outline + thumbnail 로 navigate.

영상: BASIC #3 #4 #6 + ADV multi-pane / thumbnail / outline. mp4 본체는
[`videos/features/`](videos/features/).

## Step 3 — BYOM 설정 (한 vendor 만)

[`03-byom-setup/README.md`](03-byom-setup/README.md). 자세한 AI 가이드는
[`03-byom-setup/AI_GUIDE.md`](03-byom-setup/AI_GUIDE.md), 외부 MCP 클라이언트
샘플 설정은 [`03-byom-setup/.htmlook/mcp-config.example.json`](03-byom-setup/.htmlook/mcp-config.example.json).

## Step 4 — 화면 위에서 *어디인가* 짚기

[`04-editing/README.md`](04-editing/README.md). element pick · region paint ·
sentence-id · range select 4 가지. 핵심 영상: BASIC #5 ⭐ region-cite (AI
진입점).

## Step 5 — 명령으로 바꾸기 (cite + apply_edit)

[`05-command/README.md`](05-command/README.md). 캠퍼스의 deepest part — 26
페르소나 walkthrough 가 [`05-command/personas/`](05-command/personas/) 에
있습니다 (직군 별 grouping, 각 폴더에 follow-along WALKTHROUGH.md +
before/after).

페르소나 카탈로그: [`05-command/personas/INDEX.md`](05-command/personas/INDEX.md).

## Step 6 — 자주 쓰는 워크플로우 → Skill

[`06-save-as-skill/README.md`](06-save-as-skill/README.md). 우측 AI 패널
*Save as Skill* 다이얼로그. 3 줄로 끝.

## Step 7 — Bundled Profiles 8 종

[`07-bundled-profiles/README.md`](07-bundled-profiles/README.md). HyperFrames /
Slidev / Quarto / D2 / Astro Starlight / Marimo / Excalidraw / Manim. profile
시드 본체는 [`profiles/`](profiles/) (catalog.json 빌더가 직접 읽음).

## Step 8 — 자기 Profile 작성 + 영상 표준

[`08-extend/README.md`](08-extend/README.md). 자기 도메인 profile 을 만들고
카탈로그에 add. 영상 표준 + 역검증 절차는 [`08-extend/PRODUCTION.md`](08-extend/PRODUCTION.md),
17 feature 영상 카탈로그는 [`08-extend/FEATURES.md`](08-extend/FEATURES.md).

## 자료 위치 (참고)

캠퍼스 root 에 step 폴더 (01~08) 와 함께 다음 *공용 asset 디렉토리* 가
있습니다 (catalog.json + 앱이 이 경로를 직접 참조하므로 step 안으로 이동
하지 않음):

| 폴더 | 내용 |
|---|---|
| [`videos/`](videos/) | 17 feature mp4 + 26 페르소나 mp4 (총 ~340 MB) |
| [`profiles/`](profiles/) | 8 종 Profile 시드 (`profile.json` + `SKILL.md` + `seed/`) |
| [`sample_workspaces/`](sample_workspaces/) | 75 종 도메인 시드 (`hf-*` 26 + 7 프로파일×7) |
| [`catalog.json`](catalog.json) | 83 entries (8 profile + 75 workspace seed) — 앱 Wizard fresh-fetch (24 h cache) |
| [`scripts/`](scripts/) | `build-catalog.mjs` |
| [`infra/`](infra/) | 라이센스 worker (별도 서비스) |
| [`docs/`](docs/) | 생성 artifact 작업 공간 (gitignored) |

## 두 layer 의 학습 — 영상 + 인터랙티브

캠퍼스 영상은 *what (무엇이 되는지)*. HTMLook Pro 내장 인터랙티브
walkthrough (Settings → Tutorials) 는 *how (어떻게 하는지)*. 영상에 등장하는
17 feature 모두 인터랙티브 가이드가 1:1 매칭.

| Layer | 어디서 | 길이 | 역할 |
|---|---|---|---|
| 영상 (캠퍼스) | `videos/features/`, `videos/` | 30 s / 60-70 s | 결과 보여주기 |
| 인터랙티브 (앱) | HTMLook Pro · Settings → Tutorials | 4 step | 직접 따라하기 |

## 역검증 약속 (Reverse Verification)

이 캠퍼스의 모든 영상은 **실제 HTMLook 동작과 일치하는 claim 만** 합니다.
없는 기능은 광고하지 않습니다. 자세한 검증 절차 + fix 된 false claims 목록:
[`08-extend/PRODUCTION.md`](08-extend/PRODUCTION.md).

## 라이선스

- 코드 / 워크스루 텍스트: MIT
- 영상 mp4: CC BY 4.0 (사용 시 *"HTMLook Campus"* 출처 표기)
- 샘플 콘텐츠 (PDF / xlsx / md / html): CC0 / public domain — 모두 fictional placeholder

## 에디션

- **HTMLook Pro** (v1.0) — 파워 유저용. BYOM 채팅 + 내장 PTY terminal +
  CLI 어댑터 (claude / codex / gemini) + MCP bridge + paint canvas + region
  capture + element pick + save-as-skill + 8 bundled Profile + 49 seed.
- **HTMLook Easier** (v1.x 후속, planned) — 처음 쓰는 사람용. 번들 AI ·
  단순 UI · 학생 / 입문자 가격대.

## 상태

이 레포는 **HTMLook Pro v1.0 release-candidate** (정식 출시 2026 mid 예정)
와 동기화된 학습 자료. v1.0 GA 시점에 함께 public 전환 + 카탈로그 endpoint
(`htmlook.app/catalog`) 가 이 레포의 raw URL 을 fresh-fetch (24 h cache).
