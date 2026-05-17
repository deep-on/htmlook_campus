# 오디오 / 비디오 도구

> 음성 메모 · transcript 검색 · 비디오 챕터 · 씬 감지 · 프레임 캡처 · 자막 align.

## 음성 메모 녹음

워크스페이스 마이크 레코더를 프로그램적으로 구동:

```jsonc
{ "tool": "htmlook_voice_record_start" }
// … 나중에 …
{ "tool": "htmlook_voice_record_stop" }
```

파일 경로 반환. `voice_list` 가 `.htmlook-voice/` 메모 enumerate. `voice_get_bytes` 가 파일을 base64 로 — 자체 STT provider 업로드.

M3+ MacBook Pro 클램쉘 모드 무음 마이크 버그는 자동 감지 — zero amplitude 가 지속되면 start 호출이 경고.

## Transcript sidecar

`voice_transcript_set` 가 `<file>.m4a.transcript.json` 작성:

```jsonc
{
  "tool": "htmlook_voice_transcript_set",
  "args": {
    "file_path": "voice_2026-05-17.m4a",
    "transcript": {
      "segments": [
        { "start_sec": 0.0, "end_sec": 2.4, "text": "안녕하세요" },
        { "start_sec": 2.4, "end_sec": 5.1, "text": "오늘 회의는 …" }
      ],
      "language": "ko",
      "provider": "whisper-large-v3"
    }
  }
}
```

음성 플레이어가 즉시 인식, 재생과 동기된 클릭 가능한 transcript 라인.

## audio_quote_extract

transcript 에서 시간 anchored 조각 검색:

```jsonc
{ "tool": "htmlook_audio_quote_extract",
  "args": { "file_path": "voice.m4a", "query": "회의실 예약", "limit": 5 } }
```

매치 segment + 타임코드 반환 — 사용자에게 시킹 링크와 함께 인용 가능.

## audio_segment_create

라벨 segment marker 추가. `<file>.segments.json`:

```jsonc
{ "tool": "htmlook_audio_segment_create",
  "args": {
    "file_path": "voice.m4a",
    "start_sec": 12.3,
    "end_sec":   45.0,
    "label":     "Q1 리뷰 섹션",
    "color":     "#ffc107"
  } }
```

"1시간 메모를 5 청크로 분할" 워크플로우에 유용.

## audio_waveform_get

```jsonc
{ "tool": "htmlook_audio_waveform_get",
  "args": { "file_path": "voice.m4a", "bin_count": 256 } }
```

Web Audio 디코드 음량 값 `bin_count` 개 (0..1). 저렴 — 썸네일 그리기 / 무음 구간 감지에.

## 비디오

### `video_info`

```jsonc
{ "tool": "htmlook_video_info", "args": { "file_path": "clip.mp4" } }
// → { "duration_sec": 142.5, "width": 1920, "height": 1080, "codec": "h264", "fps": 30 }
```

### `video_position`, `video_seek`

활성 비디오 뷰어 playhead 읽기/설정.

### `video_chapter_create`

챕터 추가. `<file>.chapters.json` (start_sec 정렬):

```jsonc
{ "tool": "htmlook_video_chapter_create",
  "args": { "file_path": "clip.mp4", "start_sec": 0,
            "title": "Intro", "color": "#22d3ee" } }
```

### `video_review_marker_add`

리뷰용 점 marker:

```jsonc
{ "tool": "htmlook_video_review_marker_add",
  "args": { "file_path": "clip.mp4", "time_sec": 73.4,
            "marker_kind": "issue", "note": "오디오 sync" } }
```

marker kind: `issue` · `accept` · `revise` · `note`. `<file>.bookmarks.json` 에 저장.

### `video_subtitle_align`

비디오 옆 `.vtt` / `.srt` 에 글로벌 offset. 자막 drift 보정:

```jsonc
{ "tool": "htmlook_video_subtitle_align",
  "args": { "subtitle_path": "clip.en.vtt", "offset_sec": -1.25 } }
```

In-place 재작성, 원본은 `.bak.<ts>` 로 보존.

### `video_scene_detect`

ffmpeg 기반 씬 감지:

```jsonc
{ "tool": "htmlook_video_scene_detect",
  "args": { "file_path": "clip.mp4", "threshold": 0.3, "limit": 50 } }
// → { "count": 12, "scene_times_sec": [0.0, 8.2, 14.7, …] }
```

PATH 에 ffmpeg 필요. 없으면 `DEPENDENCY_MISSING:` 에러 반환 (HTMLook 이 사용자에게 친화 toast + 원클릭 brew install).

### `capture_video_frame_region`

현재 프레임 (또는 특정 시간) 의 부분 사각형 캡처:

```jsonc
{ "tool": "htmlook_capture_video_frame_region",
  "args": {
    "file_path": "clip.mp4",
    "time_sec": 14.7,
    "rect": { "x": 100, "y": 80, "w": 400, "h": 220 }
  } }
```

표준 PNG envelope 반환. 클립 재인코딩보다 저렴 — "14.7초에 뭐 보였나" 에 완벽.

## 패턴

- **씬에서 챕터**: `video_scene_detect` → 각 cut 마다 프레임 캡처 → 그것으로 친화 제목 생성 → `video_chapter_create`
- **자막 품질 패스**: 자막 파일 읽기 + 각 cue 시작에서 프레임 캡처 → 불일치 요약
- **메모 digest**: `voice_workspace_all` → 각 메모 `audio_quote_extract({ query: "action item" })` → ChatPanel 로 digest

## 다음

- [Skill 작성 →](AI-Skill-Authoring-ko.md)
- [에러 & 복구 →](AI-Errors-Recovery-ko.md)
