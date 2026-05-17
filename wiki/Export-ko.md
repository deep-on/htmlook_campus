# Export

> 메뉴 하나에 모든 포맷. Skill 로 확장 가능.

## 위치

뷰어 툴바 우상단의 다운로드 아이콘. 클릭 → 포맷 드롭다운. 단축키: ⌘E (Export 메뉴) → ⏎ 로 선택.

## 빌트인 포맷

| 포맷 | 아이콘 | 결과 |
|---|---|---|
| **PDF** | file | 활성 탭의 print-rendered PDF |
| **Print** | printer | OS 인쇄 대화상자 (PDF 와 동일 렌더러) |
| **DOCX** | file | 가능한 한 Word doc (pandoc) |
| **Markdown** | file | 어떤 렌더러에서든 정돈된 마크다운 (turndown 기반) |
| **Markdown (Smart)** | feather | pandoc 으로 polish — 휴리스틱 정리, footnote 복원 |
| **HTML** | code | asset 인라인된 self-contained `.html` |

## Skill 등록 포맷 (동적)

divider 아래는 로드된 skill 이 선언한 모든 포맷. v1.0.9 동봉:

- **mp4** — animated SVG → mp4 (SVG-animate skill)
- **svg** — 렌더된 다이어그램 passthrough
- **pptx** — heading 으로부터 slide deck (Slide-Deck skill)

skill 추가/제거 시 리스트 라이브 업데이트.

## 인쇄 머리/꼬리말

`Settings → Viewer → printHeader` / `printFooter` 가 토큰 `{filename}` · `{date}` · `{page}` · `{pages}` 지원. 빈 문자열이면 그 줄 출력 안 함.

렌더러가 print 렌더 직전에 `@page @top-center` / `@bottom-center` CSS 로 변환. PDF export 와 Print 동일.

## 파일별 저장 위치

각 export 의 첫 사용 시 저장 위치 묻기. 디렉토리는 워크스페이스 + 포맷 단위로 기억 — 다음 PDF 는 같은 폴더로 (변경하지 않으면).

## MCP 노출 export

- `htmlook_export_active { format }` — 동일 export 파이프라인을 프로그램적으로 시작. `format` 인자는 드롭다운 내부 키 (`pdf` · `print` · `docx` · `md` · `smart-md` · `html` + skill 등록 키).

도구가 출력 파일 절대 경로 반환. 비대화형 export 완료 시 사용자 toast.

## Round-trip

`Markdown` / `Markdown (Smart)` 는 WYSIWYG 에디터와 round-trip — export 된 `.md` 열기 · 편집 · 저장 시 (whitespace 제외) 동일 마크다운.

`HTML` export 는 뷰어가 내부적으로 쓰는 inline-asset 파이프라인 — 상대 `<img src>` · `<script src>` · `<link href>` 모두 인라인 → self-contained 파일.

## 다음

- [Settings →](Settings-ko.md)
- [단축키 →](Keyboard-Shortcuts-ko.md)
