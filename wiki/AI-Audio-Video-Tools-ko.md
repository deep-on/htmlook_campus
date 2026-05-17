# 오디오 / 비디오 도구

> 음성 메모 · transcript 검색 · 비디오 챕터 · 씬 감지 · 프레임 캡처 · 자막 align.

## 음성 메모 녹음

```jsonc
{ "tool": "htmlook_voice_record_start",
  "args": { "file_path": "/abs/.htmlook-voice/note.m4a", "label": "Q3 sync" } }
// … 나중에 …
{ "tool": "htmlook_voice_record_stop" }
```

`_start` 의 두 인자 모두 옵션 — 생략 시 앱이 destination 과 라벨 선택. 파일 경로 반환. `voice_list` 가 `.htmlook-voice/` 메모 enumerate. `voice_get_bytes` 가 파일을 base64 로 — 자체 STT provider 업로드.

M3+ MacBook Pro 클램쉘 무음 마이크 버그는 자동 감지 — zero amplitude 지속 시 start 호출이 경고.

## Transcript sidecar

`voice_transcript_set` 가 메모 옆 `<file>.m4a.transcript.json` 작성. 인자는 **flat** — `transcript` 래퍼 없음:

```jsonc
{
  "tool": "htmlook_voice_transcript_set",
  "args": {
    "path":     "/abs/.htmlook-voice/note.m4a",   // path, file_path 아님
    "text":     "안녕하세요 오늘 회의는…",            // 필수, top-level
    "language": "ko",                              // 옵션
    "provider": "whisper-large-v3",                // 옵션
    "segments": [                                  // 옵션
      { "start_sec": 0.0, "end_sec": 2.4, "text": "안녕하세요" },
      { "start_sec": 2.4, "end_sec": 5.1, "text": "오늘 회의는 …" }
    ]
  }
}
```

음성 플레이어가 즉시 인식, 재생과 동기된 클릭 가능한 transcript 라인.

## audio_quote_extract

transcript 에서 시간 anchored 조각 검색:

```jsonc
{ "tool": "htmlook_audio_quote_extract",
  "args": { "file_path": "/abs/note.m4a", "query": "회의실 예약", "limit": 5 } }
```

반환: `{ transcript, query, count, hits: [{ text, start_sec?, end_sec?, speaker?, match_offset? }] }`.

## audio_segment_create

라벨 segment marker 추가. `<file>.segments.json`:

```jsonc
{ "tool": "htmlook_audio_segment_create",
  "args": {
    "file_path": "/abs/note.m4a",
    "start_sec": 12.3,
    "end_sec":   45.0,
    "label":     "Q1 리뷰 섹션",       // 옵션
    "reason":    "주요 결정 지점"       // 옵션
  } }
```

`color` 인자 없음.

## audio_waveform_get

```jsonc
{ "tool": "htmlook_audio_waveform_get",
  "args": { "file_path": "/abs/note.m4a", "bins": 256 } }
```

`bins` (`bin_count` 아님), 범위 16-4096, 기본 256. 반환: `{ bins, duration_sec, sample_rate, channels, peaks: number[] }` — `peaks` 는 mono envelope.

## 비디오

### `video_info`

```jsonc
{ "tool": "htmlook_video_info", "args": { "file_path": "/abs/clip.mp4" } }
// → { duration_sec, width, height, codec, fps, … }
```

### `video_position` / `video_seek`

활성 비디오 뷰어 playhead 읽기/설정.

### `video_chapter_create`

```jsonc
{ "tool": "htmlook_video_chapter_create",
  "args": {
    "file_path": "/abs/clip.mp4",
    "start_sec": 0,
    "end_sec":   72.5,           // 필수
    "title":     "Intro",
    "summary":   "Welcome + recap of last week"   // 옵션
  } }
```

`end_sec` 은 필수 (챕터는 anchor 점이 아닌 명시 범위). `color` 필드 없음.

### `video_review_marker_add`

```jsonc
{ "tool": "htmlook_video_review_marker_add",
  "args": {
    "file_path": "/abs/clip.mp4",
    "t_sec":     73.4,            // 인자 t_sec, time_sec 아님
    "kind":      "issue",          // 인자 kind, marker_kind 아님
    "note":      "오디오 sync"      // 옵션
  } }
```

`kind` 는 free-form 문자열 (관례: `issue` / `accept` / `revise` / `note`, 기본 `review`). `<file>.bookmarks.json` 저장.

### `video_subtitle_align`

비디오 옆 `.vtt` / `.srt` 에 글로벌 offset:

```jsonc
{ "tool": "htmlook_video_subtitle_align",
  "args": { "file_path": "/abs/clip.en.vtt", "offset_sec": -1.25 } }
```

`file_path` (subtitle_path 아님). 재작성은 **in-place** — `.bak.<ts>` 안 만듦. 되돌릴 일 있으면 직접 백업 유지.

### `video_scene_detect`

ffmpeg 기반 씬 감지:

```jsonc
{ "tool": "htmlook_video_scene_detect",
  "args": { "file_path": "/abs/clip.mp4", "threshold": 0.4, "limit": 100 } }
// → { count, scene_times_sec: [0.0, 8.2, 14.7, …] }
```

기본 `threshold` 0.4 (높을수록 적은 씬), 기본 `limit` 100. PATH 에 ffmpeg 필요. 없으면 `DEPENDENCY_MISSING:` prefix 에러 반환 (HTMLook 이 사용자에게 친화 toast + 원클릭 설치).

### `capture_video_frame_region`

프레임 (또는 특정 시간) 의 부분 사각형 캡처:

```jsonc
{ "tool": "htmlook_capture_video_frame_region",
  "args": {
    "file_path":      "/abs/clip.mp4",
    "timestamp_sec":  14.7,
    "rect":           { "x": 100, "y": 80, "w": 400, "h": 220 }
  } }
```

표준 capture envelope 반환 (이미지 블록 + JSON sibling, `timestamp_sec` + `rect` flat).

## 패턴

- **씬에서 챕터**: `video_scene_detect` → 각 cut 마다 프레임 캡처로 제목 생성 → `video_chapter_create` (다음 cut 을 `end_sec` 으로).
- **자막 품질 패스**: 자막 파일 읽기 + 각 cue 시작에서 프레임 캡처 → 불일치 요약.
- **메모 digest**: `voice_workspace_all` → 각 메모 `audio_quote_extract({ query: "action item" })` → `chatpanel_post` 로 ChatPanel digest.

## 다음

- [Skill 작성 →](AI-Skill-Authoring-ko.md)
- [에러 & 복구 →](AI-Errors-Recovery-ko.md)
