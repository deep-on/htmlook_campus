# AI 에이전트용 · 개요

> 일반 파일시스템 대비 HTMLook 이 주는 것.

## 이 페이지를 읽는 이유

…내 런타임 (Claude / Codex / Gemini / OpenAI-호환 MCP 클라이언트) 이 곧 `htmlook` MCP 서버에 연결될 것. 이 트랙이 reference. 처음에 순차적으로 따라간 다음 [도구 카탈로그](AI-Tool-Catalog-ko.md) 를 일상 조회용으로 북마크.

## 한 문단 contract

HTMLook 이 MCP 로 **~100 도구** 노출. 각 호출은 실행 중인 HTMLook Pro 인스턴스 안에서, 사용자가 지금 보고 있는 워크스페이스 컨텍스트로 실행. 결과는 JSON-RPC 응답 또는 이미지 도구의 경우 `data:image/png;base64,…` payload + JSON sidecar. 워크스페이스 root 로 스코프 — 바깥 path traversal 은 `path_guard` 가 거부. 도구별 rate limit + 모든 호출의 append-only audit log.

## 데스크톱 앱 vs CLI

CLI 가 쉽게 못 주는 세 가지:

1. **Visual capture** — `htmlook_capture_viewport` / `_selector` / `_active_element` / `_rect` / `_text_match` / `_diff`. 사용자가 보는 것을 보고 작동. ".cta 클릭 → 스크린샷 → 편집 적용 → 다시 스크린샷 → diff" 왕복 가능.
2. **라이브 상태** — 어떤 탭이 활성, 무엇이 선택, 어느 영역이 방금 캡처. `htmlook_active_file` · `_element_active` · `_region_current_png` · `_selection_text` 가 "사용자 지금 뭘 보냐" 답함.
3. **다중 채널 협업** — 여러 에이전트가 워크스페이스 공유 시 `agent_message_post / list / question_ask / answer_post` 가 구조화된 채팅 + 포렌식 audit log.

## 도구 세트의 기둥

```
                    Capture                       Edit
                  (사용자가 보는                 (제자리에서
                   것을 읽기)                      변경)
                       │                            │
                       ▼                            ▼
              ┌──────────────────┐         ┌──────────────────┐
              │   ~100 tools     │ ◄──────►│  apply_edit      │
              │  ──────────────  │  audit  │  insert_at_      │
              │   여섯 기둥으로  │   log   │    selection     │
              │   조직됨         │         │   create_file    │
              └──────────────────┘         └──────────────────┘
                       ▲
                       │
   ┌────────────┬──────┴──────┬─────────────┬──────────────┐
   ▼            ▼             ▼             ▼              ▼
 Workspace   Visual /      Annotation    PDF / Audio /  Collaboration
   & Tabs    Capture       & Sketch         Video         & Audit
```

## 각 기둥에 들어있는 것

- **Workspace & Tabs** — `active_file` · `open_file` · `close_tab` · `focus_tab` · `workspace_files` · `workspace_info` · `workspace_tree` · `set_view_mode` · `set_dual_view` · `present_mode_toggle` · `pane_pair` · `new_window` · `confirm` · `show_toast` · `wait_for_user_action` · `request_user_input` · `chatpanel_post`
- **Visual / Capture** — `capture_viewport` · `capture_selector` · `capture_active_element` · `capture_text_match` · `capture_rect` · `capture_diff` · `region_current_png` · `active_file_thumbnail` · `layout_map` · `select_element` · `select_text_range` · `computed_style_get` · `visual_overlap_check` · `highlight_element` · `scroll_to` · `jump_to_line` · `find_in_active` · `replace_in_active` · `selection_text` · `selection_html` · `element_active` · `paint_*` · `sketch_*`
- **Annotation & Sketch** — `view_state_snapshot / restore` · `annotation_add / list` · 모든 `sketch_*` · `paint_*`
- **PDF tools** — `pdf_highlight_add / clear` · `pdf_citation_anchor` · `pdf_comment_add` · `pdf_text_spans` · `capture_pdf_region`
- **Audio / video tools** — `audio_segment_create` · `audio_quote_extract` · `audio_waveform_get` · `video_chapter_create` · `video_review_marker_add` · `video_subtitle_align` · `video_scene_detect` · `capture_video_frame_region` · `video_*` 컨트롤 (`info`, `seek`, `position`, `clip_range`, `bookmarks`) · `voice_*` 레코더
- **Collaboration & audit** — `agent_message_post / list` · `agent_question_ask` · `agent_answer_post` · `audit_log_query`

전체 reference: [도구 카탈로그](AI-Tool-Catalog-ko.md).

## "이것부터 시작" 루프

```
htmlook_workspace_info     # 어느 폴더?
htmlook_active_file        # 사용자가 무엇을?
htmlook_layout_map         # 페이지에 뭐가?
… 계획 …
htmlook_select_element     # 스코프 좁히기
htmlook_apply_edit         # 변경
htmlook_capture_selector   # 검증
htmlook_audit_log_query    # 흔적 (자동)
```

## 프라이버시와 capability

- 모든 게 사용자의 HTMLook Pro 프로세스 안에서 로컬 실행. Deep-On 서버 경유 없음.
- 쓰기 도구는 세 가지 체크로 게이트: Free Viewer 라이선스 · 워크스페이스 path-guard 스코프 · 도구별 rate limit. v1.0.9 의 MCP 쓰기 경로에는 per-call 동의 모달이 **없음** — 도구 호출 전에 채팅으로 무엇을 할지 명시해서 사용자가 필요 시 interrupt 가능하도록.
- `apply_edit` 로 워크스페이스 root 바깥 파일 못 읽음 (path_guard 거부). 임의 프로세스 exec 못 함. v1.0.9 에서 명시적 제외: `terminal_run_managed` · `send_keys` · semantic search · visual search.

## 다음

- [MCP 설정 →](AI-MCP-Setup-ko.md)
- [도구 카탈로그 →](AI-Tool-Catalog-ko.md)
