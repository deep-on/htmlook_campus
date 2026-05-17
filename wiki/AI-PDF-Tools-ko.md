# PDF 도구

> 텍스트 읽기 · 페이지 인용 · 영역 캡처 · 영구 하이라이트 / 코멘트.

## 읽기 전용: 텍스트 span + 영역 캡처

### `pdf_text_spans`

페이지의 모든 텍스트 조각 + 스크린 좌표 (좌상 origin, scale = 1):

```jsonc
{
  "tool": "htmlook_pdf_text_spans",
  "args": { "file_path": "/abs/path.pdf", "page": 3 }
}
```

```jsonc
{
  "file": "/abs/path.pdf",
  "page": 3,
  "viewport": { "width": 595, "height": 842 },
  "spans": [
    { "text": "Q3 Revenue", "x": 72, "y": 80, "w": 120, "h": 14, "font": "Helvetica-Bold" },
    …
  ]
}
```

"X 라는 문장 찾기" 에 사용 — `spans` 배열 직접 검색. `font` 는 옵션. 빈/공백 span 필터링.

### `capture_pdf_region`

페이지의 부분 사각형 렌더 + cropped PNG 반환 (기본 scale 1.5):

```jsonc
{
  "tool": "htmlook_capture_pdf_region",
  "args": {
    "file_path": "/abs/path.pdf",
    "page":  3,
    "rect":  { "x": 72, "y": 80, "w": 460, "h": 200 },   // 옵션, 기본 = 페이지 전체
    "scale": 1.5
  }
}
```

표준 capture envelope (이미지 블록 + JSON sibling) 반환. JSON sibling 의 `rect` 좌표는 scale = 1 의 PDF-points; 렌더러가 내부 스케일.

## 주석: 영구 하이라이트 + 코멘트

`<file>.pdf.highlights.json` 으로 PDF 옆 — 다른 곳과 동일 companion 패턴. `mv` 살아남고 워크스페이스 따라 이동.

### `pdf_highlight_add`

```jsonc
{
  "tool": "htmlook_pdf_highlight_add",
  "args": {
    "file":  "/abs/path.pdf",
    "page":  3,
    "rect":  [72, 100, 200, 14],     // [x, y, w, h] — 정확히 4 float
    "color": "#fff59d",                // 옵션
    "note":  "핵심 주장"               // 옵션
  }
}
```

- 인자는 `file` (file_path 아님).
- `rect` 는 단일 4-tuple `[x, y, w, h]`, 객체 배열 아님. 1 호출 → 1 rect → 1 하이라이트. 멀티라인 span 강조하려면 여러 번 호출.
- 라벨 필드는 `note` (label 아님).

### `pdf_highlight_clear`

```jsonc
{ "tool": "htmlook_pdf_highlight_clear",
  "args": { "file": "/abs/path.pdf", "page": 3 } }
```

- 인자는 `file`.
- `page` 는 옵션 — 생략 시 모든 페이지 정리.

### `pdf_comment_add`

```jsonc
{
  "tool": "htmlook_pdf_comment_add",
  "args": {
    "page":  3,
    "rect":  [72, 100, 200, 14],
    "note":  "분기 잘못 인용.",
    "color": "#ffd54f"               // 옵션
  }
}
```

`file_path` 없음 (활성 PDF 사용), `highlight_id` 없음 — `page + rect + note` 전달 시 서버가 코멘트가 attach 된 하이라이트를 한 번에 생성. 필드는 `note`.

## 페이지 인용

### `pdf_citation_anchor`

주어진 PDF 페이지에 대한 link-sidecar 항목 반환:

```jsonc
{
  "tool": "htmlook_pdf_citation_anchor",
  "args": {
    "pdf_path":    "/abs/path.pdf",        // file_path 아님
    "page":        3,
    "rect":        [72, 80, 460, 200],     // 옵션, 인용 범위 좁힘
    "from_path":   "/abs/notes.md",        // 옵션, 인용 주체 파일
    "from_anchor": "#sec-q3",              // 옵션
    "label":       "Q3 figures"            // 옵션
  }
}
```

`{ id, total, path }` 반환 — 새 항목 id (`L_*`), 갱신된 링크 총수, 링크 sidecar 의 절대 경로 (예: `/abs/.htmlook/links.jsonl`). `htmlook://` URL 문자열은 반환 **안 함**. sidecar 항목을 `id` 로 읽어 링크 resolve.

## 포함 안 한 것

- `pdf_figure_detect` — 이미지/차트 추출 (ML, deferred)
- `pdf_table_extract` — 구조화 테이블 (ML, deferred)

필요 시 사용자가 별도 도구 (예: `tabula`) 실행 → JSON 을 워크스페이스로 `create_file` → 결과 파일에 `find_in_active`.

## 자주 쓰는 루프

### "이 단락 읽기"

```
pdf_text_spans → 단락 덮는 bbox 식별
capture_pdf_region with that bbox → PNG (이미지 블록)
(이미지를 reasoning 단계로 전달)
```

### "마크하고 기억"

```
pdf_highlight_add → 색 사각형 영구
pdf_comment_add → 이유 설명
(다음 세션) 더 이상 관련 없으면 pdf_highlight_clear
```

### "노트에 페이지 인용"

```
pdf_citation_anchor → 링크 항목 id + sidecar path
agent_message_post body: "Q3 figures — see link <id>"
```

## 다음

- [오디오 / 비디오 도구 →](AI-Audio-Video-Tools-ko.md)
- [프롬프트 패턴 →](AI-Prompt-Patterns-ko.md)
