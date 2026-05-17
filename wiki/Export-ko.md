# Export

> 메뉴 하나에 모든 포맷. 확장으로 더 추가 가능.

## 위치

뷰어 툴바 우상단의 다운로드 아이콘. 클릭 → 포맷 드롭다운.

## 빌트인 포맷

| 포맷 | 아이콘 | 결과 |
|---|---|---|
| **PDF** | file | 활성 탭의 print-rendered PDF |
| **Print** | printer | OS 인쇄 대화상자 (PDF 와 동일 렌더러) |
| **DOCX** | file | 가능한 한 Word doc (Pandoc 필요) |
| **Markdown** | file | 어떤 렌더러에서든 정돈된 마크다운 |
| **Markdown (Smart)** | feather | polish — 휴리스틱 정리, footnote 복원 (Pandoc 필요) |
| **HTML** | code | asset 인라인된 self-contained `.html` |

## 확장 등록 포맷

divider 아래는 설치된 확장이 추가한 모든 포맷. 기본 셋에서 보이는 것:

- **mp4** — animated SVG → mp4
- **svg** — 다이어그램 passthrough
- **pptx** — 마크다운 heading 으로부터 슬라이드 덱 (LibreOffice 필요)

확장 추가/제거 시 리스트 라이브 업데이트.

## 인쇄 머리/꼬리말

*Settings → Viewer → Print header / Print footer* 가 토큰 `{filename}` · `{date}` · `{page}` · `{pages}` 지원. 빈 문자열이면 그 줄 출력 안 함.

Print 와 PDF export 동일 문구.

## 파일별 저장 위치

각 export 의 첫 사용 시 저장 위치 묻기. 디렉토리는 워크스페이스 + 포맷 단위로 기억 — 다음 PDF 는 같은 폴더로 (변경하지 않으면).

## Round-trip

`Markdown` / `Markdown (Smart)` 는 WYSIWYG 에디터와 round-trip — export 된 `.md` 열기 · 편집 · 저장 시 (whitespace 제외) 동일 마크다운.

`HTML` export 는 상대 `<img src>` · `<script src>` · `<link href>` 모두 인라인 → self-contained 파일. 이메일/첨부 쉬움.

## 포맷이 안 보여요?

기대한 포맷이 드롭다운에 없으면 외부 도구가 미설치일 수 있음. *Settings → Tools* 열면 그 포맷의 도구 (PPTX 는 LibreOffice, Smart Markdown 은 Pandoc 등) 옆에 흐린 ring 이 있는 행에 원클릭 *Install* 버튼.

## 다음

- [Settings →](Settings-ko.md)
- [단축키 →](Keyboard-Shortcuts-ko.md)
