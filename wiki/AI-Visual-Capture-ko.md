# Visual Capture

> 사용자가 실제로 보는 것을 읽기. `apply_edit` + `capture_diff` 와 체이닝할 때 가장 강력.

## Capture 표면 (6 도구)

| 도구 | 사용 시점 |
|---|---|
| `capture_viewport` | 활성 pane 전체 |
| `capture_selector` | CSS selector 가 있을 때 (`#hero`, `.card:nth-child(2)`) |
| `capture_active_element` | 사용자가 방금 클릭한 요소 |
| `capture_text_match` | 화면에 보이는 문자열을 인용 가능할 때 |
| `capture_rect` | 좌표 알 때 (보통 `region_current_png` 다음) |
| `capture_diff` | 방금 캡처한 두 PNG 비교 |

모든 capture 도구 반환:

```jsonc
{
  "base64": "iVBORw0KGgo…",      // image/png, data URL 아님
  "mime": "image/png",
  "width": 1280,
  "height": 720,
  "captured_at": "2026-05-17T03:14:00Z",
  "scope": {                     // 캡처된 것
    "kind": "selector",          // viewport | selector | active_element | text_match | rect
    "selector": ".hero",         // 도구별
    "bbox": { "x": 0, "y": 0, "w": 1280, "h": 320 }
  }
}
```

`base64` 를 클라이언트의 이미지 처리 primitive 로 디코드 — 대부분 MCP 클라이언트가 vision content block 으로 직접 수용.

## "Before / After" 패턴

```text
1. capture_selector(".cta") → before.png
2. 편집 계획 (텍스트 색상 변경)
3. apply_edit("Sign up free", "Start free trial")
4. (~150 ms 재렌더 대기)
5. capture_selector(".cta") → after.png
6. capture_diff(before, after, threshold=0.05) → bbox + did_change
```

diff 는 `png` crate 위에 순수 Rust 로 계산. 변경 픽셀의 tight bounding box 포함 — sanity check 에 유용 ("내 편집이 CTA 만 건드렸나, cascade 됐나?").

## visual_overlap_check

다음 요소들 반환:

- **truncated** 텍스트 (`text-overflow: ellipsis` 활성)
- 컨테이너 **overflow**
- **zero size** (레이아웃 버그 가능)
- **clip** 된 내용

```jsonc
{
  "issues": [
    { "selector": ".hero h1", "kind": "text-truncated", "rect": {…} },
    { "selector": "#cta-row",  "kind": "overflow-x",   "rect": {…} }
  ]
}
```

카피 길이 변경 전 pre-flight check 에 유용.

## layout_map

구조 조사 반환:

```jsonc
{
  "landmarks":   [{ "role": "banner", "selector": "header" }, …],
  "headings":    [{ "level": 1, "text": "Hello", "selector": "h1" }, …],
  "buttons":     [{ "text": "Sign up", "selector": "#cta-row > button:nth-child(1)" }, …],
  "links":       [{ "text": "Pricing", "href": "/pricing", "selector": "nav a:nth-child(2)" }, …],
  "images":      [{ "alt": "hero", "src": "hero.png", "selector": "img.hero" }, …],
  "tables":      [{ "rows": 12, "cols": 4, "selector": "#data" }, …],
  "forms":       [{ "fields": 5, "selector": "form#contact" }, …]
}
```

세션 시작 시 한 번 호출 → "페이지 한눈에".

## select_element + capture_active_element

특정 노드를 빠르게 다루는 법:

```
htmlook_select_element({ selector: ".cta button" })
htmlook_capture_active_element({ padding: 8 })
```

padding 은 bounding box 주변 여백 — 스크린샷에 맥락 포함.

## Rate limit

Capture 도구가 8-burst / 8 per sec token-bucket 공유. 일반 "before / 5 candidates / after" 루프 = 7 capture, 한도 미만. 한도 초과 시 친화 에러 — ~125 ms back off 후 계속.

## Capture 하지 *말아야* 할 때

- **"레이아웃 이해하려고"** capture 하지 말 것 — `layout_map` 으로 답이면 더 싸고 작고 결정론적.
- 변경 없이 **연속 2회 capture** 하지 말 것 — 두 번째 호출이 같은 PNG.
- 요소 이름 가능할 때 **viewport capture** 하지 말 것 — 타이트 크롭이 5–10× 작고 diff 가 더 유용.

## 다음

- [Apply-edit 왕복 →](AI-Apply-Edit-ko.md)
- [프롬프트 패턴 →](AI-Prompt-Patterns-ko.md)
