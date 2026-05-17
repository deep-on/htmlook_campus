# 뷰어 · 마크다운 에디터

> 가장 큰 영역. 파일 타입별 렌더러 + Pro 의 마크다운 풀 WYSIWYG.

## 파일 타입별 렌더러

| 타입 | 렌더러 | 편집 가능? |
|---|---|---|
| `.md` `.markdown` `.mdx` | WYSIWYG 마크다운 에디터 | 예 — Pro 풀, Easier 는 read-only |
| `.html` `.htm` | iframe sandbox + 상대 asset 인라인 | 보기 (코드뷰에서 소스 편집) |
| `.qmd` | Quarto 렌더 → iframe | 보기 |
| `.pdf` | PDF.js + text layer | Pro 도구로 하이라이트/코멘트 |
| `.docx` `.pptx` `.xlsx` | LibreOffice → PDF → 렌더 | 보기 |
| `.svg` | 인라인 렌더 | 코드뷰에서 편집 |
| `.json` `.csv` `.tsv` | 표 + 트리 뷰 | 보기 |
| 이미지 | native `<img>` + zoom · fit · pan | — |
| 비디오 / 오디오 | 자체 플레이어 (아래) | — |
| 소스 코드 | Shiki 하이라이트 | 코드뷰에서 편집 |
| 미지정 | hex / text fallback | — |

## Markdown WYSIWYG (Pro)

렌더 위에서 직접 타이핑. 일반 워드프로세서처럼 느껴지지만 출력은 깨끗한 마크다운.

### 블록 autocorrect

| 입력 | 결과 |
|---|---|
| `# ` | H1 |
| `## ` … `###### ` | H2 .. H6 |
| `> ` | Blockquote |
| ```` ``` ```` + Enter | Fenced code (Tab 으로 언어 순환) |
| `--- ` + Enter | 수평선 |
| `- [ ] ` | Task list (미체크) |
| `- [x] ` | Task list (체크) |

### 인라인 autocorrect

닫는 delimiter 가 포맷팅으로 변환:
`**bold**`, `*em*`, `_em_`, `` `code` ``, `~~strike~~`, `~sub~`, `^sup^` (Pandoc).

### 선택 wrap

텍스트 선택 후 `*` `_` `` ` `` 누르면 감쌈. `[` `(` `{` `'` `"` 누르면 양쪽 감싸고 안쪽 재선택.

### 공학 기호

`-> <- => <-> <=> >= <= != +-` 가 `→ ← ⇒ ↔ ⇔ ≥ ≤ ≠ ±` 으로 (코드블록 밖에서만).

### 링크 · ⌘K

선택 인식 링크 다이얼로그. 선택 있으면 텍스트 prefill. caret 이 `<a>` 안이면 URL 편집 또는 *Remove*. 아니면 새 삽입. `[text](url.md)` autocorrect 도 동작.

### 코드블록

caret 이 fenced 안 → 우상단 **언어 picker** pill. 큐레이션 리스트 또는 직접 타이핑. ```` ```python ```` 로 round-trip. Skill 매니페스트로 워크스페이스 skill 이 등록한 언어 자동 등장.

### 이미지

이미지 선택 → *alt text* + *정렬* (left / center / right / none) popover. 정렬은 인라인 `style` 작성, turndown 이 raw `<img>` 로 보존.

### Footnote

`[^id]: body…` 정의, `[^id]` 참조. 에디터가 번호 다시 매기고 마지막에 `Footnotes` 섹션 자동 렌더. 저장/로드 round-trip.

### Paste

⌘V fallback chain: 이미지 → HTML (Word 의 `mso-*`/`<o:p>` sanitize, 허용 태그만) → 텍스트. ⌘⇧V 는 항상 plain. WKWebView 의 `paste` 이벤트가 텍스트에서 silent-fail 시 `clipboard.readText()` fallback.

### 자동 저장

탭 단위 `$effect` 가 `modified + rawContent` 감시. 1.5 s debounce 후 저장. Untitled 탭은 자동 저장 안 함.

### 인쇄 / PDF

`Settings → Viewer → printHeader / printFooter` 에 토큰 `{filename} {date} {page} {pages}` 사용 가능. 빈 문자열이면 그 줄 미출력.

## PDF 뷰어

continuous scroll, 툴바 zoom, *Find in PDF* (⌘F), 색상 picker 가 있는 하이라이트 도구. 하이라이트는 PDF 옆 `<file>.pdf.highlights.json` 으로 저장 — 다른 곳과 동일 companion 패턴. 코멘트는 하이라이트에 붙고 우측 마진에 표시.

## 비디오 / 오디오 플레이어

빌트인 플레이어:

- 북마크 마커가 있는 스크러버
- 속도 컨트롤 (0.5× → 2×)
- *순간 마크* (플레이어 내부 ⌘B) → `<file>.bookmarks.json`
- transcript 패널 (`<file>.transcript.json` 이 있으면)
- seek bar 아래 챕터 strip (`<file>.chapters.json`)
- AB-loop 범위 도구

## Find bar

⌘F 로 뷰어 내 find. ⏎ 다음, ⇧⏎ 이전, ⌘G 다음. 라이브 증분, regex 토글, 대소문자 토글. 닫으면 highlight 정리.

## 다음

- [터미널 →](Terminal-ko.md)
- [Export →](Export-ko.md)
