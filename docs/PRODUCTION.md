# Production Notes

> 영상이 어떻게 만들어졌고 어떤 표준을 따르는지 기록. 새 영상 추가하거나
> 기존 영상 다시 빌드할 때 이 문서를 첫 참고로.

## 영상 구조 표준

### 길이

- **페르소나 영상 (26편)**: 60–70 s. 5-step refinement loop (hook → step1..5 → cta).
- **Feature spotlight 영상 (17편)**: 30 s. 단일 magic moment (hook → 5 demo
  beats → reprise → brand close).

### 해상도 / 프레임레이트

- 1920×1080 30 fps.
- 1.0× + 1.2× 두 변형 (페르소나 + feature 모두). 1.2× 는 video setpts/1.2 +
  audio atempo=1.2.

### 자막 (mov_text + sidecar VTT)

mp4 한 본에 영문(en) + 한글(ko) 두 mov_text 트랙을 mux. 두 변형:

- `_voiced_bgm.en+ko.mp4` — **ko default+forced** (한국어 청자용)
- `_voiced_bgm.en+ko.en-default.mp4` — **en default+forced** (영어 청자용)

각 mp4 옆에 sidecar VTT 두 개 (`<basename>.en.vtt`, `<basename>.ko.vtt`).
HTMLook Pro 의 subtitle-loader 는 sidecar를 자동 attach.

**Hook cue 타이밍**: cue #1 은 `00:00:00.100` 에서 시작 (0.000 이 아님).
Safari/QuickTime WebKit 이 첫 cue 를 0.000 에 둘 때 skip 하는 quirk 회피.

### Brand close

- 모든 영상 마지막 5 s 에 동일 footer:
  - Logo / wordmark
  - 슬로건 (영상별)
  - URL: **htmlook.app**
- 통일 팔레트: 검정 #0a0a0c base + 보라 #7c3aed nav + amber accent + 영상별
  per-video accent (cyan / mint / emerald / lime / magenta / rose / amber).

## 음성 + BGM 레시피

### TTS

- 엔진: **Kokoro-82M ONNX** via `npx hyperframes tts`
- 보이스: `af_nova` (영문, 자연스러운 alto)
- 입력: `narration_segments/0[1-7]_*.txt` (각 cue 별 1 파일)
- 출력: 같은 이름 `.wav` (24 kHz mono)

### BGM

- 소스: `assets/bgm_pix.mp3` (각 영상에 같은 트랙 사용 — 시리즈 일관성)
- 처리: highpass 180 Hz + treble +2 dB + bass -4 dB + **volume 0.08**
- amix weights 5:1 (voice : bgm)

### 믹싱

`/tmp/persona_pipeline.sh` (페르소나) / `/tmp/feature_pipeline.sh` (feature)
가 voice + BGM 을 합치고 video 와 mux. 둘은 동일 로직, 다른 디렉토리만:

```bash
/tmp/feature_pipeline.sh basic-01-drop-open 30 100 4000 9300 13700 17500 22500 25500
#                        <persona> <DUR>  D1  D2   D3   D4    D5    D6    D7
```

D1..D7 = 각 cue 의 adelay (ms). cue start = adelay 값.

### 자막 mux

`/tmp/feature_vtt_mux.py <persona> <D1..D7>` 가 mov_text en + ko 트랙을
mux 하고 두 변형 (.en+ko / .en+ko.en-default) 출력 + sidecar VTT 복사.

## Reverse Verification (역검증)

영상의 모든 claim 은 실제 HTMLook 동작과 일치해야 함. 허위광고 방지가
이 캠퍼스의 핵심 약속.

### 검증 절차

1. 영상 narration .txt 읽기
2. claim 추출 (예: "drag region → cite anchor", "⌘D split view")
3. HTMLook 소스에서 해당 기능 확인:
   - UI: `src/lib/components/`, `src/apps/AppPro.svelte`
   - MCP: `src-tauri/src/pro_features/mcp_server/server.rs` (도구 description)
   - **단축키**: `src-tauri/src/lib.rs` 의 Tauri menu accelerator (`MenuItemBuilder::with_id(...).accelerator("CmdOrCtrl+...")`)
     ⚠️ AppPro.svelte 의 keydown 만 보면 메뉴 단축키를 놓침. 단축키 검증은 lib.rs 부터.
4. 일치하지 않으면 narration 또는 composition 수정 → 재 TTS → 재 mix → 재 mux

### 이번 캠퍼스에서 fix 된 false claims

| 영상 | 문제 → 수정 |
|---|---|
| 페르소나 step 4 (모든 26편) | "Kokoro speaks. Whisper aligns." 가 in-app 동작인 듯 → "Hyperframes runs. Kokoro voices..." 로 외부 CLI 임을 명시 |
| creator-podcast | "audio + waveform on the left" → "transcript markdown on the left" (waveform viewer 없음) |
| press-editor | 동일 |
| data-analyst | "SQL → chart" → "SQL query + chart svg" (HTMLook 은 SQL 실행 안 함; LLM 이 SVG 작성) |
| kid-coding | "turtle drawing" → "svg drawing" (Python 실행 안 함) |
| basic-03 MD live edit | "preview-side double-click → inline edit" (없음) → 제거. source-side editing only |
| advanced-04 multi-pane | "⌘1/⌘2/⌘3" (없음) → 실제 단축키 ⌘D + ⌘J |
| advanced-10 outline | "dual-pane sync jump" (없음) → preview-only jump |
| advanced-11 cross-link | "rename → auto-rewrite" (없음) → ".htmlook/links.json sidecar 기록" |
| advanced-04 multi-pane | "⌘D + ⌘J" (⌘D 는 split terminal 임) → 실제 단축키 ⌘1 / ⌘2 / ⌘3 / ⌘J 로 정정. ⌘1 = Preview, ⌘2 = Source, ⌘3 = Split view, ⌘J = Terminal panel. Tauri 메뉴 accelerator 로 정의 (`src-tauri/src/lib.rs:1644-1655`) — 이전 audit 가 AppPro.svelte 의 keydown 만 보고 잘못 판단했던 점도 [`PRODUCTION.md`](PRODUCTION.md) 의 검증 절차에 반영함. |

## Sample Workspace 표준

`samples/` 의 각 페르소나 폴더 구조:

```
NN-<persona>/
├─ WALKTHROUGH.md       ← step-by-step follow-along (en + ko 혼합, [VIEW]/[AI] 마크)
├─ <source files>...    ← 사용자가 작업할 콘텐츠
├─ before/              ← edit 전 상태 (LLM 없이도 비교 가능)
└─ after/               ← edit 후 상태
```

**원칙:**
- 모든 콘텐츠는 fictional / public-domain. 실제 회사/인물명 사용 금지 (Apex /
  Atlas / Borealis 같은 placeholder).
- WALKTHROUGH 의 `[VIEW]` 단계는 HTMLook 단독으로 가능. `[AI]` 단계는
  MCP-aware LLM 클라이언트 필요.
- before/after 는 LLM 없는 사용자도 분할뷰로 결과를 시각 비교할 수 있게.

## Interactive Walkthrough (in-app)

HTMLook Pro 에 설정 다이얼로그 → **Tutorials** 탭이 있음. 17 편 feature 영상
각각에 대응하는 인터랙티브 가이드 (spotlight + tooltip + 4 step) 가 내장.

캠퍼스 사용자가 영상 본 후:
1. 영상 시청 (`videos/features/<name>.mp4`)
2. HTMLook Pro 열고 Settings → Tutorials → 같은 이름 Start
3. 실제 UI 위에서 spotlight 가이드 따라 직접 동작 수행

이 두 layer 가 함께 학습 효과를 만듦. 영상은 *what*, 인터랙티브는 *how*.

## 새 영상 추가 워크플로우

1. `demo/feature_units/<new-id>/` 디렉토리 생성 (또는 persona_units)
2. `narration_segments/0[1-7]_*.txt` 작성 (en, 자연 광고체)
3. TTS: `cd narration_segments && for f in 0*; do npx hyperframes tts $f.txt -o ${f%.txt}.wav; done`
4. ffprobe 로 wav 길이 확인 → cue start (D1..D7) 설계
5. composition `index.html` 작성 (기존 영상 참고)
6. lint: `npx hyperframes lint .` (0 errors 필수)
7. render: `npx hyperframes render . -o renders/index.en.mp4 -w 1`
8. mix: `/tmp/feature_pipeline.sh <id> 30 D1..D7`
9. ko 자막 작성 + mux: VTT 직접 작성 후 `/tmp/feature_vtt_mux.py <id> D1..D7`
10. 역검증: claim 모두 실제 HTMLook 기능에 부합?
11. 캠퍼스 repo: `videos/features/` 에 mp4 복사, `docs/FEATURES.md` 업데이트
12. (선택) `samples/` 에 follow-along 추가
13. (선택) `walkthrough-steps.ts` 에 인터랙티브 spec 추가

## 파일 명명 규칙

- 페르소나: `<persona>_voiced_bgm[.en|.en+ko|.en+ko.en-default][_1.2x].mp4`
- Feature: `<id>_voiced_bgm[...].mp4` (동일 패턴, id 가 다름)
- Sidecar VTT: `<basename>.<lang>.vtt`

## 참고 도구

- 페르소나 audit: `python3 /tmp/audit_all_transitions.py`
- Feature audit: `python3 /tmp/audit_all_features.py`
- 둘 다 cue gap (≥ 0.1 s) + voice 레벨 (≥ -20 dB) 검증.
