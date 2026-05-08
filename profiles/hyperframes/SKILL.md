---
name: hyperframes
description: HyperFrames kinetic typography 영상 합성 — md/json scene → mp4 + TTS narration.
---

# HyperFrames 워크플로우

마크다운 / JSON scene 파일을 영상 (mp4) 으로 합성. 시그니처 출력 = kinetic typography
+ 자동 내레이션 (Kokoro TTS, en/ko). `npx hyperframes` CLI 가 워크스페이스 내 manifest
를 읽어 `renders/` 에 mp4 출력.

## 발견 신호

- `hyperframes.json` (manifest, root)
- `scenes/` 또는 `scene.md` (콘텐츠)
- `package.json` 의 `hyperframes` dependency

## 작업 패턴

1. **scene 작성**: `scenes/<n>.md` 에 frontmatter (timing / accent / layout) + body 텍스트.
2. **렌더**: `npx hyperframes render` → `renders/<scene>.mp4`.
3. **내레이션 합성**: scene frontmatter 의 `narration:` 블록을 Kokoro TTS 가
   처리, mp4 에 mux.
4. **검수**: HTMLook 의 viewer 에서 mp4 미리보기 + Live-cue 로 timestamp ↔ scene
   라인 양방향.

## hyperframes.json 패턴

```json
{
  "version": 1,
  "resolution": "1920x1080",
  "fps": 30,
  "output_dir": "renders",
  "narration": {
    "enabled": true,
    "voice": "af_nova",
    "speed": 1.0
  },
  "scenes": ["scenes/01-hook.md", "scenes/02-step.md", "scenes/03-cta.md"]
}
```

## scene frontmatter 패턴

```yaml
---
duration_ms: 4000
accent: cyan
layout: hero
narration: |
  Code lands. Video updates. No alt-tab.
---

# Code lands.
## Video updates.
**No alt-tab.**
```

## HTMLook 시그니처 활용

- **Live-cue ⭐**: 렌더된 mp4 의 timestamp ↔ scene 의 라인 양방향 — 영상의
  특정 순간에서 어느 scene 줄이 활성인지 클릭 한 번에 보임.
- **Pane pair**: 좌 scene.md ↔ 우 mp4 viewer (자동 새로고침).
- **Multi-target apply_edit**: 여러 scene 의 같은 phrase 일괄 수정 (CTA / brand 변경).

## 외부 의존

- Node 18+, ffmpeg (mp4 인코딩 + audio mux).
- Kokoro TTS (Python lib, `pip install kokoro` 또는 docker).
- 렌더 시간: 1080p30 60s 영상 기준 약 2-3 분.

## 자주 만나는 이슈

- 폰트 fallback: 한글 narration 시 `font-family` 명시 필요 (Pretendard / 시스템 fallback).
- BGM 충돌: 사용자 mp3 + Kokoro narration mix 시 narration vol 1.4x boost 권장.
- Output dir 자동 생성 X — 첫 실행 전 `mkdir renders` 필요.

## 참조

- 본 Profile = MIT (deep-on)
- HyperFrames CLI = MIT (deep-on)
- Sample workspaces: `htmlook_campus/sample_workspaces/hf-claude/` 등 26 페르소나
