---
name: excalidraw
description: Excalidraw 손그림 다이어그램 — JSON 저장, 버전관리, SVG/PNG export.
---

# Excalidraw 워크플로우

손그림 스타일 화이트보드. `.excalidraw` 파일이 JSON 이라 git diff / merge 가능. 75k+ stars, 2025 가장 인기 있는 ad-hoc 다이어그램 도구.

## 발견 신호

- `*.excalidraw` 또는 `*.excalidraw.png` (embed 모드)
- `*.excalidrawlib` (사용자 라이브러리)

## 작업 패턴

1. **편집**: https://excalidraw.com 또는 VS Code Excalidraw extension 또는 desktop app.
2. **저장 형식**:
   - `.excalidraw` (JSON-only, 가장 작음)
   - `.excalidraw.png` (PNG + JSON 메타 embed — 보존 + 미리보기 동시)
   - `.excalidraw.svg` (SVG export, 정적)
3. **라이브러리**: `.excalidrawlib` 으로 자주 쓰는 도형 묶음 — 팀 공유 가능.

## HTMLook 시그니처 활용

- **Region cite ⭐**: 다이어그램의 한 영역 (시스템 박스 / 흐름 화살표) 캡처 → AI 에게 "이 부분 글로 설명" / "이 박스 이름 다른 후보 5개".
- **Pane pair**: 좌 `.excalidraw` 파일 (또는 export 된 `.svg`) ↔ 우 viewer 가 SVG 렌더.
- **Multi-target**: 다이어그램 + 본문 md 둘 다에서 같은 컴포넌트 이름 일괄 변경.

## JSON 구조 (편집 시 참고)

```json
{
  "type": "excalidraw",
  "version": 2,
  "source": "https://excalidraw.com",
  "elements": [
    { "type": "rectangle", "x": 100, "y": 100, "width": 200, "height": 80 },
    { "type": "text", "text": "Backend", "x": 130, "y": 130 }
  ],
  "appState": { "viewBackgroundColor": "#ffffff" }
}
```

## 주의

- VS Code Excalidraw extension 은 `.excalidraw.png` 자동 embed — 가장 권장 형식.
- 라이브러리 import 는 https://libraries.excalidraw.com/ 에서 가져오기.
- 한글 텍스트는 폰트 fallback 필요 — embed 시 폰트 정보 보존됨.

## 참조

- 공식: https://excalidraw.com
- GitHub: https://github.com/excalidraw/excalidraw (MIT)
- 라이브러리: https://libraries.excalidraw.com
- 라이선스: 본 Profile = MIT, Excalidraw = MIT
