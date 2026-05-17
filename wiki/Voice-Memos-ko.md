# 음성 메모

> 상태바의 마이크 버튼. AAC 파일이 워크스페이스에. transcript 가 옆에.

## 녹음기 위치

상태바 우측: 마이크 글리프. 클릭 → 녹음 시작, 글리프가 빨갛게 변하고 옆에 입력 레벨 미터 막대.

다시 클릭 (또는 Settings 에서 바인드한 단축키) 으로 정지. 파일은 `<workspace>/.htmlook-voice/voice_<YYYYMMDD-HHMMSS>.m4a` (AAC) 로 떨어집니다.

## 첫 사용

macOS 가 앱당 한 번 마이크 권한 요청. 시스템 prompt 가 "녹음은 로컬에만 저장" 설명.

M3+ MacBook Pro 의 **클램쉘 모드 (lid 닫음) 에서 내부 마이크는 디지털 무음** — 알려진 macOS 버그. lid 열거나 외부 마이크 페어링. HTMLook 이 zero-amplitude 스트림 감지 시 1회 경고 toast.

## 재생 플레이어

`.m4a` 가 사이드바에서 선택될 때 또는 워크스페이스에 메모가 있고 플레이어를 dismiss 하지 않은 경우 하단 가장자리 **Voice Player**:

```
┌────────────────────────────────────────────────────┐
│  ▶  ◀ 1 / 5 ▶   memo_20260517-141900.m4a   00:42  │
│  ▁▂▅▆▇▆▅▃▁  ━━━━━━━●─────────────────  ⌃ ✏ ✕    │
└────────────────────────────────────────────────────┘
```

- ◀ / ▶ 워크스페이스 메모 순환
- waveform 으로 음량 envelope
- ⌃ 플레이어 접기 (배지 달린 ▶︎ 버튼만 남음)
- ✏ 이름 변경, ✕ 삭제

## Transcript

메모를 transcribe 하면 `<file>.m4a.transcript.json` 이 옆에 생성. 플레이어가 timecode 와 함께 인라인 표시. 문장 클릭 시 그 위치로 seek.

transcribe 방법:

- MCP-tool 에이전트가 `htmlook_voice_transcript_set` 호출
- 직접 작성한 skill 이 transcript JSON 게시
- 외부 STT 도구의 출력 수동 paste

빌트인 STT 엔진은 없음. 음성 파일은 본인 자산 — 로컬 Whisper, API, ElevenLabs Voice 같은 유료 서비스 모두 가능.

## Drag-out

사이드바 메모를 Finder · Mail · Slack · Notion 으로 드래그. .m4a 경로가 실림 — Mail 에 drop 하면 첨부.

## 검색

`htmlook_voice_search` 가 transcript (있을 때) 를 쿼리로 검색, 매치 메모를 timecode 와 반환. *워크스페이스 검색* 패널 (⌘⇧F) 에 표시.

## MCP 노출 도구

- `htmlook_voice_record_start` / `htmlook_voice_record_stop`
- `htmlook_voice_list` / `htmlook_voice_workspace_all`
- `htmlook_voice_get_bytes` — 파일 base64
- `htmlook_voice_rename` / `htmlook_voice_delete`
- `htmlook_voice_transcript_get` / `htmlook_voice_transcript_set`
- `htmlook_voice_search`
- `htmlook_audio_segment_create` / `htmlook_audio_quote_extract` / `htmlook_audio_waveform_get`

[AI Audio / Video Tools](AI-Audio-Video-Tools-ko.md) 참조.

## 프라이버시

음성 파일은 자체로 워크스페이스 폴더를 떠나지 않습니다. transcribe · chat 전송 같은 액션은 모두 명시적. 녹음 중에는 마이크 글리프가 빨갛게 — 상태가 항상 가시.

## 다음

- [Skills →](Skills-ko.md)
- [Settings →](Settings-ko.md)
