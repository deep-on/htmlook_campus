# 도구 카탈로그

> HTMLook MCP 서버가 노출하는 모든 도구를 목적별로 그룹화. 스키마 / 파라미터 디테일은 링크된 서브 페이지.
>
> **정식 source**: 연결된 MCP 서버에 `tools/list` 호출. 아래는 hand-maintained 라 빌드 1-2 개 뒤처질 수 있음 — 오리엔테이션 용으로 보고, 정확한 parameter shape 과 신규 도구는 live 응답으로.

가독성 위해 `htmlook_` prefix 없이 표기. 실제 wire 명은 `htmlook_<name>`.

## 1. 워크스페이스 · 탭 · 윈도우

| 도구 | 반환 / 효과 |
|---|---|
| `ping` | `{ version, build_id, started_at }` |
| `workspace_info` | 현재 워크스페이스 `{ root, name, opened_at, tab_count }` |
| `workspace_files` | 워크스페이스 파일 재귀 리스트 (paged) |
| `workspace_tree` | 트리 표현 |
| `workspace_tools` | `.htmlook/tools.json` 등록 도구 |
| `search_workspace` | 전체 텍스트 검색 (and-or, 파일/경로 필터) |
| `active_file` | 활성 탭 경로 + 기본 메타 |
| `active_file_thumbnail` | 활성 탭의 PNG preview |
| `open_file` | 경로 열기 (새 또는 기존 탭) |
| `create_file` | 내용과 함께 생성 |
| `close_tab` | id 또는 경로로 탭 닫기 |
| `focus_tab` | 탭 포커스 |
| `set_view_mode` | `single` / `dual` / `code` / `present` |
| `set_dual_view` | dual-view 파일 + sync-scroll 설정 |
| `pane_pair` | 어떤 두 파일이 페어인지 |
| `present_mode_toggle` | present 모드 토글 |
| `new_window` | 새 윈도우 |
| `zoom` | 뷰어 줌 0.5 .. 3.0 |
| `outline` | heading outline (`.md`, `.html`, `.pdf`) |
| `hyperframes` | 현재 파일의 hyperframe 링크 |

## 2. 선택 · 요소 · 네비게이션

| 도구 | 용도 |
|---|---|
| `selection_text` | 현재 선택 평문 |
| `selection_html` | 현재 선택 HTML |
| `selection_scope` | 선택 포함 요소 |
| `sidebar_selection` | 사이드바 현재 선택 파일들 |
| `element_active` | 현재 선택 요소 정보 |
| `select_element` | CSS selector 로 프로그램적 선택 |
| `select_text_range` | 활성 문서 내 텍스트 범위 선택 |
| `highlight_element` | 강조 (시각만, 선택 아님) |
| `scroll_to` | 요소 / 라인 / 페이지로 스크롤 |
| `jump_to_line` | 라인 N 점프 |
| `find_in_active` | 검색, offset 과 함께 매치 반환 |
| `replace_in_active` | 제자리 치환 |
| `computed_style_get` | 요소의 computed CSS |
| `visual_overlap_check` | text-truncation / overflow / zero-size 감지 |
| `layout_map` | landmark / heading / button / link / form 조사 |

## 3. Visual Capture

| 도구 | 반환 |
|---|---|
| `capture_viewport` | 활성 pane PNG |
| `capture_selector` | CSS selector 로 요소 PNG |
| `capture_active_element` | 선택된 요소 PNG |
| `capture_text_match` | 매치 텍스트 포함 요소 PNG |
| `capture_rect` | 사각 영역 PNG |
| `capture_diff` | 두 PNG diff + bbox |
| `region_current_png` | 사용자가 마지막 캡처한 영역 |

전체 가이드: [Visual Capture](AI-Visual-Capture-ko.md)

## 4. Apply-edit 군

| 도구 | 효과 |
|---|---|
| `apply_edit` | 활성 파일에서 find + replace + audit |
| `insert_at_selection` | 커서 / 선택 위치 삽입 |
| `replace_in_active` | 활성 파일에 특화된 치환 |
| `create_file` | 새 파일 작성 |
| `cite` / `citation_anchor` | `htmlook://` anchor 떨어뜨림 |

전체 가이드: [Apply-edit 왕복](AI-Apply-Edit-ko.md)

## 5. Annotation · Sketch · Paint

| 도구 | 효과 |
|---|---|
| `annotation_add` / `annotation_list` | 워크스페이스 주석 (note + 경계) |
| `view_state_snapshot` / `view_state_restore` | 뷰어 상태 저장/복원 |
| `paint_enable` / `paint_disable` / `paint_dimensions` | paint 캔버스 토글/크기 |
| `sketch_add_shape` / `sketch_set_color` / `sketch_set_stroke` | 프로그램적 paint |
| `sketch_undo` / `sketch_redo` / `sketch_clear` / `sketch_save` | 히스토리 + 저장 |
| `sketch_current_png` | 현재 스케치 base64 |
| `highlight_element` | 부드러운 시각 강조 |

## 6. PDF 도구

| 도구 | 효과 |
|---|---|
| `pdf_highlight_add` / `pdf_highlight_clear` | 영구 하이라이트 |
| `pdf_comment_add` | 하이라이트에 묶인 코멘트 |
| `pdf_citation_anchor` | 현재 PDF 페이지 인용 |
| `pdf_text_spans` | 페이지의 모든 텍스트 span + bbox |
| `capture_pdf_region` | 페이지 sub-사각형 PNG |

전체 가이드: [PDF 도구](AI-PDF-Tools-ko.md)

## 7. 오디오 · 비디오 · 음성

### 음성 메모
| 도구 | 효과 |
|---|---|
| `voice_record_start` / `_record_stop` | 시작 / 정지 |
| `voice_list` / `_workspace_all` | 메모 목록 |
| `voice_get_bytes` | 파일 base64 |
| `voice_rename` / `_delete` | 관리 |
| `voice_transcript_get` / `_transcript_set` | transcript sidecar 읽기/쓰기 |
| `voice_search` | transcript 검색 |
| `audio_segment_create` | `<file>.segments.json` 추가 |
| `audio_quote_extract` | transcript 에서 quote 검색 |
| `audio_waveform_get` | 음량 envelope (Web Audio decoded) |

### 비디오
| 도구 | 효과 |
|---|---|
| `video_info` | 코덱 + 길이 + 크기 |
| `video_position` / `video_seek` | playhead 읽기/설정 |
| `video_clip_range` | 클립 정의 |
| `video_bookmarks` | `<file>.bookmarks.json` |
| `video_chapter_create` | 챕터 추가 |
| `video_review_marker_add` | 리뷰 마커 추가 |
| `video_subtitle_align` | .vtt / .srt offset |
| `video_scene_detect` | ffmpeg `select=gt(scene,..)` 파싱 |
| `capture_video_frame_region` | 프레임 → 크롭 PNG |

전체 가이드: [오디오/비디오 도구](AI-Audio-Video-Tools-ko.md)

## 8. 터미널 & 프로세스

| 도구 | 효과 |
|---|---|
| `terminal_buffer_get` | 활성 터미널 스크롤백 |
| `terminal_process_tree` | 활성 터미널 프로세스 트리 |
| `link` / `links` | 외부 URL 열기 |

> v1.0.9 는 blast radius 제한 위해 `terminal_run_managed` 와 `send_keys` 명시 제외.

## 9. 협업 · audit

| 도구 | 효과 |
|---|---|
| `agent_message_post` / `agent_message_list` | cross-agent JSONL 메시지 |
| `agent_question_ask` / `agent_answer_post` | 구조화된 Q&A |
| `audit_log_query` | `<workspace>/.htmlook/audit-log.jsonl` 읽기 |

전체 가이드: [다중 에이전트 협업](AI-Collaboration-ko.md)

## 10. UI 훅

| 도구 | 효과 |
|---|---|
| `show_toast` | 사용자 윈도우의 toast |
| `confirm` | yes/no 모달 |
| `request_user_input` | 프롬프트 + 값 반환 |
| `wait_for_user_action` | 사용자 클릭에서 block |
| `chatpanel_post` | ChatPanel 에 메시지 push |
| `export_active` | Export 메뉴 프로그램적 트리거 |
| `print_active` | Print 트리거 |
| `insert_at_selection` | (위에도 표시) |

## 11. 영역 & 스크린샷

| 도구 | 효과 |
|---|---|
| `region_current_png` | 사용자가 마지막 캡처한 영역 |
| `active_file_thumbnail` | 일반 thumbnail (≠ 영역) |

## 여기 없는 이름 (deferred)

- `terminal_run_managed`, `send_keys` — 임의 프로세스/키스트로크 (v1.0.9 out of scope)
- `semantic_search`, `visual_search` — embedding 인프라 (별도 트랙)
- `audio_speaker_map`, `pdf_figure_detect`, `pdf_table_extract` — ML-heavy (v1.0.10+)
- `responsive_probe` — hidden-iframe 라이프사이클 복잡 (v1.0.10)

## 다음

- [Visual Capture →](AI-Visual-Capture-ko.md)
- [Apply-edit 왕복 →](AI-Apply-Edit-ko.md)
