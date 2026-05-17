# Visual Capture

> 사용자가 실제로 보는 것을 읽기. `apply_edit` + `capture_diff` 와 체이닝할 때 가장 강력.

## Capture 표면

| 도구 | 사용 시점 |
|---|---|
| `capture_viewport` | 활성 pane 전체 |
| `capture_selector` | CSS selector 가 있을 때 |
| `capture_active_element` | 사용자가 방금 클릭한 요소 |
| `capture_text_match` | 화면에 보이는 문자열 인용 가능 |
| `capture_rect` | 좌표 알 때 |
| `capture_diff` | 방금 캡처한 두 PNG 비교 |
| `capture_video_frame_region` | 활성 비디오의 주어진 시간 sub-region |
| `capture_pdf_region` | PDF 페이지의 sub-사각형 |
| `region_current_png` | 사용자가 마지막 수동 캡처한 영역 재가져오기 |

## 반환 envelope

이미지 도구는 **두 MCP content block** + JSON sibling text block 반환:

- `image/png` content block — bitmap
- `text` content block — capture 묘사 JSON

JSON sibling 은 **flat** (nested `scope` 없음) 이고 `base64` 는 stripped (PNG 는 이미지 블록, JSON 에 중복 안 됨):

```jsonc
{
  "pane":      "active",     // "active" | "primary" | "secondary"
  "full_page": false,         // true 면 페이지를 한 장 긴 이미지로 렌더
  "width":     1280,
  "height":    720,
  // 도구별 extra 는 flat top-level:
  "selector":      ".hero",      // capture_selector
  "match_count":   1,             // capture_selector / _text_match
  "matched_index": 0,             // _text_match / _selector 다중 시
  "text":          "Sign up",     // _text_match
  "tag":           "BUTTON",      // _active_element
  "rect":          { "x":0,"y":0,"w":300,"h":120 }, // _rect / _video_frame_region
  "timestamp_sec": 14.7,          // _video_frame_region
  "page":          3,             // _pdf_region
  "scale":         1.5            // _pdf_region
}
```

참고: `mime` 필드 · `captured_at` · `scope` 래퍼 없음 — 이전 초안에 잘못 적힘.

## "Before / After" 패턴

```text
1. capture_selector(".cta") → before.png + JSON sibling
2. 편집 계획
3. apply_edit(path, find, replace)
4. (뷰어 리로드 이벤트 자동 발화)
5. capture_selector(".cta") → after.png
6. capture_diff(before_base64, after_base64, threshold)
```

## capture_diff

```jsonc
{
  "tool": "htmlook_capture_diff",
  "args": {
    "before_base64": "iVBORw0…",
    "after_base64":  "iVBORw0…",
    "threshold":     0.1                  // 옵션, 기본 0.1
  }
}
```

이미지 + JSON 반환:

```jsonc
{
  "width":         1280,
  "height":        720,
  "changed_pixels": 234,
  "total_pixels":   921600,
  "changed_ratio":  0.00025,
  "bbox":           [120, 480, 160, 40],   // 옵션 [x, y, w, h]
  "threshold":      0.1
}
```

`did_change` 필드 없음 — `changed_pixels > 0` 또는 `bbox != null` 로 추론. 이미지 블록은 diff 시각화.

## visual_overlap_check

활성 pane 의 레이아웃 이슈 반환:

```jsonc
{
  "pane":     "active",
  "viewport": { "w": 1280, "h": 720 },
  "scanned":  142,
  "issues": [
    {
      "kind":   "text-truncation",        // | horizontal-overflow | vertical-overflow | zero-size | element-overlap
      "tag":    "H1",
      "text":   "Welcome to…",
      "bbox":   { "x": 120, "y": 80, "w": 400, "h": 32 },
      "detail": "text-overflow: ellipsis"
    }
  ]
}
```

필드는 `bbox` (rect 아님). kind 값은 위와 같이 하이픈 (`text-truncation`, `text-truncated` 아님).

## layout_map

`kind` 로 태그된 구조 entry 의 단일 flat 리스트:

```jsonc
{
  "pane":     "active",
  "viewport": { "w": 1280, "h": 720 },
  "entries": [
    { "kind": "landmark", "tag": "HEADER",  "bbox": { "x":0,"y":0,"w":1280,"h":80 }, "selector": "header" },
    { "kind": "heading",  "tag": "H1",      "bbox": {…}, "text": "Hello",  "selector": "h1" },
    { "kind": "button",   "tag": "BUTTON",  "bbox": {…}, "text": "Sign up", "selector": "#cta button:nth-child(1)" },
    { "kind": "link",     "tag": "A",       "bbox": {…}, "text": "Pricing","href": "/pricing", "selector": "nav a:nth-child(2)" },
    { "kind": "image",    "tag": "IMG",     "bbox": {…}, "src": "hero.png","selector": "img.hero" }
  ],
  "total":     142,
  "truncated": false
}
```

세션 시작 시 한 번 → "페이지 한눈에". 한 이터레이션이 cap 될 수 있음 — `truncated` 확인.

## select_element + capture_active_element

```text
select_element({ selector: ".cta button" })
  → { selector, matched_index, match_count, tag, id, class, bbox } 반환
capture_active_element({ padding: 8 })
  → 선택된 요소를 bbox 주변 N px padding 과 함께 캡처
```

## Rate limit

Capture 도구는 burst 8, 초당 8 refill token-bucket, **도구별 키** (`capture_viewport` 와 `capture_selector` 가 독립 bucket). 소진 시 평문 에러
`rate-limited: <tool_name> burst exhausted. Retry after ~<ms> ms.` 명시 ms back off.

## 실패 모드

| 메시지 prefix | 의미 |
|---|---|
| `selector "<sel>" matched no elements in <pane> pane` | selector 가 0 노드 |
| `text "<t>" not found in <pane> pane (mode=<mode>)` | text-match 쿼리가 화면에 없음 |
| `no <pane> viewer pane available — open a file first` | 타겟 pane 미마운트 |
| `<pane> viewer is not same-origin…` | iframe srcdoc / asset:// 장벽이 DOM 접근 차단 |
| `rate-limited: <tool_name> burst exhausted…` | token bucket 소진 |

## Capture 하지 *말아야* 할 때

- **"레이아웃 이해하려고"** capture 하지 말 것 — `layout_map` 으로 답이면 더 작고 결정론적.
- 변경 없이 **연속 2회 capture** 하지 말 것 — 두 번째 호출이 같은 PNG.
- 요소 이름 가능할 때 **viewport capture** 하지 말 것 — 타이트 크롭이 작고 diff 가 더 유용.

## 다음

- [Apply-edit 왕복 →](AI-Apply-Edit-ko.md)
- [프롬프트 패턴 →](AI-Prompt-Patterns-ko.md)
