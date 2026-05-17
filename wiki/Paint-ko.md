# Paint

> 뷰어 위 투명 스케치 캔버스. ⌘⇧P 토글. 동그라미 치고, 가리키고, 보내는 용도.

## 왜 있나

"내가 말하는 게 이거다" 의 절반은 제스처 — *이 열* · *이 추세* · *이 정렬 어긋남*. Paint 가 표시할 layer 를 주고, 결과를 저장하고, ChatPanel 의 이미지 첨부로 바로 보내게 합니다.

## 토글과 기본

| 동작 | 단축키 |
|---|---|
| Paint 모드 토글 | ⌘⇧P |
| 캔버스를 ChatPanel 첨부로 | (Paint 열린 상태) → ChatPanel 의 📎 |
| Undo / Redo | ⌘Z / ⌘⇧Z (탭당 50-step 히스토리) |
| 캔버스 지우기 | Paint 툴바의 휴지통 |
| PNG export | 다운로드 아이콘 (`.htmlook/sketches/...png`) |

캔버스는 탭별. 스케치는 마지막 stroke 후 5 s debounce 로 `.htmlook/sketches/<basename>.<timestamp>.png` 에 자동 저장.

## 도구

| 도구 | 메모 |
|---|---|
| **펜** | freehand. Apple Pencil + 트랙패드용 압력 곡선. |
| **지우개 (S/M/L)** | 8 / 16 / 32 px. 스트로크만 — 아래 뷰어는 안 건드림. |
| **사각형** | 드래그로 그리기. *Fill* 토글. |
| **타원** | 사각형과 동일하지만 타원. |
| **직선** | Shift 로 15° 스냅. |
| **화살표** | 방향 토글 → / ← / ↔. |
| **텍스트** | 클릭으로 배치. 크기 **S / L**. ⏎ 로 확정. |

## 색 + 두께

툴바의 swatch. 두께: thin / medium / thick / heavy. 워크스페이스별 저장.

## Export 해상도

PNG export 는 1280×720 cap. DPR 인식이라 retina 캡처도 선명. 출력은 alpha-free RGB — 웹 도구에 paste 시 투명 surprise 없음.

## ChatPanel 첨부

Paint 열린 상태에서 ChatPanel 📎 가 별도 Save 없이 현재 캔버스를 잡음. 다음 user message 에 vision content block 으로 실림.

`.htmlook/sketches/` 에서 PNG 를 ChatPanel 입력 박스로 드래그도 가능.

## 워크스페이스 산출물

`.htmlook/sketches/` 의 파일들은 평범한 PNG — git 친화, 복사 가능, 첨부 가능. 자체 컨테이너 없음.

## MCP 노출 도구 (AI 에이전트용)

- `htmlook_sketch_current_png` — 활성 스케치 base64
- `htmlook_sketch_clear` — 캔버스 지우기
- `htmlook_sketch_save` — 강제 저장
- `htmlook_sketch_add_shape` — 프로그램적 도형 그리기
- `htmlook_sketch_set_color`, `htmlook_sketch_set_stroke`, `htmlook_sketch_undo`, `htmlook_sketch_redo`

capture 도구와 조합해 "뷰어 이 영역 하이라이트 → 저장 → 첨부" 흐름 구성. [AI Visual Capture](AI-Visual-Capture-ko.md) 참조.

## 다음

- [음성 메모 →](Voice-Memos-ko.md)
- [Skills →](Skills-ko.md)
