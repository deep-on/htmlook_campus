# Step 7 · Bundled Profiles (HyperFrames / Slidev / 외 6종)

> v1.0 부터 8 종의 *Heavyweight Profile* 이 앱에 동봉. 첫 launch 시
> `~/.htmlook/profiles/_bundled-*` 에 자동 unpack.
> ~ 5 분 (둘러보기 — 본격 사용은 도구 별 학습).

Profile = 외부 도구 + Skill v0.3 묶음 + seed 콘텐츠 패키지. New Workspace
Wizard (⌘⇧N) 또는 Add wizard 의 카드로 한 클릭 설치.

> Profile manifest (profile.json + SKILL.md + seed/) 의 본체는 캠퍼스
> 루트 [`../profiles/`](../profiles/) 에 보관 — catalog.json 빌더가 이 경로를
> 직접 읽음. 본 step 은 그것들을 둘러보기 위한 가이드.

## 7.1 · 8 종 profile 카드

| Profile | 카테고리 | 출력 | 도구 라이선스 | 시작 |
|---------|---------|------|-------------|------|
| HyperFrames | motion-graphics | mp4 (kinetic typography) | MIT | [`../profiles/hyperframes/`](../profiles/hyperframes/) |
| Slidev | presentation | HTML/PDF slides | MIT | [`../profiles/slidev/`](../profiles/slidev/) |
| Quarto | publishing | PDF/HTML/PPT/book | GPL-2.0 | [`../profiles/quarto/`](../profiles/quarto/) |
| D2 | diagram | SVG | MPL-2.0 | [`../profiles/d2/`](../profiles/d2/) |
| Astro Starlight | documentation | docs site | MIT | [`../profiles/astro-starlight/`](../profiles/astro-starlight/) |
| Marimo | notebook | reactive HTML | Apache-2.0 | [`../profiles/marimo/`](../profiles/marimo/) |
| Excalidraw | diagram | JSON/SVG/PNG | MIT | [`../profiles/excalidraw/`](../profiles/excalidraw/) |
| Manim | educational-animation | mp4 | BSD-3-Clause | [`../profiles/manim/`](../profiles/manim/) |

> **HTMLook 은 도구를 번들하지 않습니다.** 사용 가이드 / Wizard 통합만 제공.
> 외부 도구는 별도 설치 (각 profile 의 README 에 dependency 명시).

## 7.2 · 한 개만 골라서 시작

처음이면 가장 가벼운 것:

- **Slidev** — `npx slidev` 로 설치. md 한 파일 → HTML 슬라이드.
- **D2** — Go binary 설치. txt → SVG 다이어그램.
- **Excalidraw** — 별도 설치 불필요 (HTMLook 내장 viewer).

복잡한 것:

- **HyperFrames** — Node + ffmpeg + Kokoro TTS (Python). 캠퍼스 영상 만든 도구.
- **Manim** — Python + LaTeX. 수학 애니메이션.
- **Quarto** — R / Python / Pandoc. 학술 publishing.

## 7.3 · Add wizard 에서 install

1. ⌘⇧N (New Workspace Wizard) 또는 사이드바 *+* (Add wizard)
2. 카탈로그 카드 중 원하는 profile 선택
3. *Install* — 시드 폴더가 사용자 home 으로 복사됨
4. *Open* — HTMLook 이 그 폴더를 워크스페이스로 열고 profile 의 Skill 들이
   ⌘K 카탈로그에 추가됨

## 7.4 · 추가 도메인 시드 (선택)

8 profile 위에 75 개 워크스페이스 시드가 [`../sample_workspaces/`](../sample_workspaces/)
에 있음 — 모두 prefix 로 매핑해 어느 profile 시드인지 한눈에:

- `hf-*/` (26 종 — HyperFrames, 캠퍼스 영상 제작에 쓰는 전체 페르소나 라인업)
- `slidev-*/` (7 종) · `quarto-*/` (7 종) · `marimo-*/` (7 종) · `manim-*/` (7 종)
- `d2-*/` (7 종) · `excalidraw-*/` (7 종) · `astro-*/` (7 종)

`hf-claude/` 와 `hf-llama/` 는 BYOM 레퍼런스 (Anthropic Claude / 로컬 Llama
경로). 나머지 24 종 (`hf-corp-deck/`, `hf-teacher-quiz/`, `hf-kid-coding/` …)
은 도메인 시나리오. 각 시드는 `index.html + hyperframes.json + brand.txt
+ prompts.txt + AGENTS.md + meta.json + README.md` 풀세트라 AI 에이전트가
사용자의 BYOM 모델로 그대로 워크플로 재현 가능.

전체 catalog: [`../catalog.json`](../catalog.json) — 현재 **83 entries**
(8 profile + 75 workspace seed). CI 자동 갱신
([`../scripts/build-catalog.mjs`](../scripts/build-catalog.mjs)).

## ✅ Step 7 체크포인트

- 8 profile 의 README 중 1 개를 읽어봄.
- (선택) 도구 1 개 외부 설치 → Add wizard 에서 그 profile 시드 install.
- (선택) `sample_workspaces/` 에서 자기 도메인 가까운 시드 1 개 둘러봄.

다 맞으면 → [Step 8 · extend (자기 Profile 작성)](../08-extend/)

## 더 자세히

- 각 profile 폴더의 `SKILL.md` — 그 profile 이 등록한 Skill v0.3 manifest.
- [`../08-extend/PRODUCTION.md`](../08-extend/PRODUCTION.md) — HyperFrames 으로
  영상 만드는 표준 (캠퍼스 영상 17 + 26 편 모두 이 도구로 제작).
