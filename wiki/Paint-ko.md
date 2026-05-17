# Paint

> 뷰어 위 투명 스케치 캔버스. ⌘⌥P 토글. 동그라미 치고, 가리키고, 보내는 용도.

## 왜 있나

"내가 말하는 게 이거다" 의 절반은 제스처 — *이 열* · *이 추세* · *이 정렬 어긋남*. Paint 가 표시할 layer 를 주고, 결과를 저장하고, AI 어시스턴트의 이미지 첨부로 바로 보냅니다.

## 토글과 기본

| 동작 | 단축키 |
|---|---|
| Paint 모드 토글 | ⌘⌥P |
| Undo / Redo | ⌘Z / ⌘⇧Z (탭당 50-step 히스토리) |
| 캔버스 지우기 | Paint 툴바의 휴지통 |
| PNG export | 다운로드 아이콘 |

캔버스는 탭별. 스케치는 마지막 stroke 후 5 s 자동 저장. 위치: `<workspace>/.htmlook/sketches/`.

## 도구

| 도구 | 메모 |
|---|---|
| **펜** | freehand. Apple Pencil + 트랙패드용 압력 곡선. |
| **지우개 (S / M / L)** | 8 / 16 / 32 px. 스트로크만 — 아래 뷰어는 안 건드림. |
| **사각형** | 드래그로 그리기. *Fill* 토글. |
| **타원** | 사각형과 동일하지만 타원. |
| **직선** | Shift 로 15° 스냅. |
| **화살표** | 방향 토글 → / ← / ↔. |
| **텍스트** | 클릭으로 배치. 크기 **S / L**. ⏎ 로 확정. |

## 색 + 두께

툴바의 swatch. 두께: thin / medium / thick / heavy. 워크스페이스별 저장.

## Export 해상도

PNG export 는 1280 × 720 cap. retina 인식이라 캡처도 선명. 출력은 alpha-free RGB — 다른 도구에 paste 시 투명 surprise 없음.

## AI 어시스턴트에 첨부

Paint 열린 상태에서 AI 어시스턴트의 📎 가 현재 캔버스를 별도 Save 없이 잡음. 다음 메시지에 실림.

저장된 PNG 를 `.htmlook/sketches/` (사이드바) 에서 직접 입력 박스로 드래그도 가능.

## 다음

- [음성 메모 →](Voice-Memos-ko.md)
- [Export →](Export-ko.md)
