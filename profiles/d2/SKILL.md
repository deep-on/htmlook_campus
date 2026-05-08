---
name: d2
description: D2 (Terraform-style 다이어그램) 워크플로우. .d2 → SVG live preview.
---

# D2 워크플로우

Mermaid 보다 모던한 syntax, 더 좋은 layout (ELK / TALA). dev-team 의 시스템 다이어그램 표준화에 적합.

## 발견 신호

- `.d2` 파일
- 폴더 구조: `diagram.d2` + 선택적 `*.d2` 임포트

## 작업 패턴

1. **단일 다이어그램**: `d2 diagram.d2 diagram.svg` — 정적 빌드.
2. **Watch 모드**: `d2 --watch diagram.d2 diagram.svg` — 변경 시 SVG 갱신 + 브라우저 reload.
3. **레이아웃 엔진**: 기본 `dagre` (작음). 복잡 그래프 = `elk` (cleaner). 상용 = `tala` (가장 좋지만 separate license).
4. **테마**: `--theme=0..200` (https://d2lang.com/tour/themes)

## D2 syntax 핵심

```d2
# 노드 + 엣지
backend -> database
backend -> cache: read-through

# 그룹 (container)
ingress: {
  alb -> waf
  waf -> backend
}

# 형태 / 스타일
backend.shape: hexagon
database.style.fill: "#0e639c"

# import
...@common.d2
```

## HTMLook 시그니처 활용

- **Pane pair**: 좌 `.d2` ↔ 우 SVG iframe (d2 watch 의 localhost:8080).
- **Region cite**: 다이어그램의 한 노드/그룹 영역 캡처 → AI 에게 "이 부분 더 명확하게 / 분리".
- **Multi-target apply_edit**: 여러 `.d2` 파일에서 같은 노드 이름 일괄 rename.

## 주의

- `tala` 레이아웃은 상용 license — 오픈소스 워크스페이스에선 `elk` 권장.
- 한글 라벨은 폰트 fallback 안 되면 깨질 수 있음 — `fonts: { regular: ... }` 으로 명시.
- `.d2` 파일 서로 import 시 순환 참조 주의.

## 참조

- 공식: https://d2lang.com
- Playground: https://play.d2lang.com
- GitHub: https://github.com/terrastruct/d2 (MPL-2.0)
- 라이선스: 본 Profile = MIT, D2 CLI = MPL-2.0 (별도 설치)
