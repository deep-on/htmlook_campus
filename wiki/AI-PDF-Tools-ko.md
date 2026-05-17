# PDF 도구

> 텍스트 읽기 · 페이지 인용 · 영역 캡처 · 영구 하이라이트/코멘트, 6 도구.

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

"X 라는 문장 찾기" 에 사용 — `spans` 배열 직접 검색. PDF.js getTextContent 가 backbone. 빈/공백 span 필터링.

### `capture_pdf_region`

페이지의 부분 사각형 렌더 + cropped PNG 반환 (기본 scale 1.5):

```jsonc
{
  "tool": "htmlook_capture_pdf_region",
  "args": {
    "file_path": "/abs/path.pdf",
    "page":  3,
    "rect":  { "x": 72, "y": 80, "w": 460, "h": 200 },   // optional, default = 페이지 전체
    "scale": 1.5
  }
}
```

다른 캡처 도구와 같은 envelope: `{ base64, width, height, page, rect, scale }`. 좌표는 PDF-points, 렌더러가 내부 스케일.

## 주석: 영구 하이라이트 + 코멘트

`<file>.pdf.highlights.json` 으로 PDF 옆 — 다른 곳과 동일 companion 패턴. `mv` 살아남고 워크스페이스 따라 이동.

### `pdf_highlight_add`

```jsonc
{
  "tool": "htmlook_pdf_highlight_add",
  "args": {
    "file_path": "/abs/path.pdf",
    "page":  3,
    "rects": [
      { "x": 72, "y": 100, "w": 200, "h": 14 }
    ],
    "color": "#fff59d",
    "label": "핵심 주장"
  }
}
```

여러 `rects` 가 하나의 하이라이트로 그룹 (텍스트가 줄 넘는 경우).

### `pdf_highlight_clear`

```jsonc
{ "tool": "htmlook_pdf_highlight_clear",
  "args": { "file_path": "/abs/path.pdf", "page": 3 } }
```

페이지 스코프 정리.

### `pdf_comment_add`

```jsonc
{
  "tool": "htmlook_pdf_comment_add",
  "args": {
    "file_path": "/abs/path.pdf",
    "highlight_id": "h_5f8e",         // pdf_highlight_add 가 반환
    "comment": "분기 잘못 인용."
  }
}
```

코멘트는 하이라이트에 attach (한 하이라이트에 여러 개 가능). 뷰어가 우측 마진에 렌더.

## 페이지 인용

### `pdf_citation_anchor`

따라가면 PDF 가 같은 페이지 + 뷰포트로 열리는 `htmlook://` 링크 emit:

```jsonc
{ "tool": "htmlook_pdf_citation_anchor",
  "args": { "file_path": "abs/path.pdf", "page": 3 } }
```

`htmlook://abs/path.pdf#page=3` 반환. 마크다운 노트 · 채팅 · 다른 뷰어 내용에 drop.

## 포함 안 한 것

- `pdf_figure_detect` — 이미지/차트 추출 (ML, v1.0.10+ deferred)
- `pdf_table_extract` — 구조화 테이블 (ML, deferred)

필요 시 사용자가 별도 도구 (예: `tabula`) 실행 → JSON 을 워크스페이스로 `create_file` → 결과 파일에 `find_in_active`.

## 자주 쓰는 루프

### "인용하고 cite"

```
pdf_text_spans → 문장 찾기
pdf_citation_anchor → 링크
agent_message_post (body: 인용 + 링크) → 사용자가 클릭
```

### "이 단락 읽기"

```
pdf_text_spans → 단락 덮는 bbox 식별
capture_pdf_region with that bbox → PNG
(PNG 를 LLM 에 vision content block 으로 전달)
```

### "마크하고 기억"

```
pdf_highlight_add → 색 사각형 영구
pdf_comment_add → 이유 설명
(다음 세션) 더 이상 관련 없으면 pdf_highlight_clear
```

## 다음

- [오디오 / 비디오 도구 →](AI-Audio-Video-Tools-ko.md)
- [프롬프트 패턴 →](AI-Prompt-Patterns-ko.md)
