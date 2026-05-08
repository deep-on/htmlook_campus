# D2 Profile

Terraform-style 모던 다이어그램 [D2](https://d2lang.com) HTMLook Profile.

## 시작

```bash
brew install d2          # macOS
d2 --watch diagram.d2 diagram.svg   # http://localhost:8080
```

## HTMLook 활용

- **Pane pair**: 좌 `.d2` ↔ 우 SVG (live).
- **Region cite ⭐**: 다이어그램 한 영역 → AI 에게 분리 / 명확화 지시.
- **Multi-target apply_edit**: 여러 `.d2` 동일 노드 rename.

## 외부 의존

- D2 CLI (https://d2lang.com/tour/install) — MPL-2.0
- Layout engines: dagre (내장), elk (내장), tala (상용 옵션)

## 라이선스

본 Profile = MIT (deep-on). D2 = MPL-2.0 (별도 설치).
