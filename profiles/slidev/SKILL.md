---
name: slidev
description: Vue + Vite + Markdown 슬라이드 도구 (Slidev) 워크플로우. .md 편집 → live HMR preview.
---

# Slidev 워크플로우

워크스페이스에 `slides.md` 가 있으면 Slidev. Vue/Vite/Markdown 한꺼번에 쓰는 모던 슬라이드.

## 발견 신호

- `slides.md` (entry)
- `package.json` 에 `@slidev/cli` dependency
- 폴더 구조: `slides.md` + 선택적 `components/` + `pages/` + `layouts/` + `public/`

## 작업 패턴

1. **새 슬라이드 추가**: `slides.md` 의 `---` 구분자 사이에 새 페이지. layout/transition 은 frontmatter 로.
2. **테마 전환**: frontmatter `theme:` 변경 → HMR 즉시 반영.
3. **코드 하이라이트**: ```` ```ts {1,3-5}{at:'click+1'} ```` 같은 라인 강조 + click step.
4. **Build / Export**: `slidev build` (PDF 생성은 `--export pdf`).

## HTMLook 시그니처 활용

- **Pane pair**: 좌측 `slides.md` 편집 ↔ 우측 viewer 가 `http://localhost:3030` iframe 으로 live HMR.
- **Region cite**: 슬라이드의 한 영역 (코드 블록 / 이미지) 을 캡처 → AI 에게 "이 부분 더 명확하게" 요청.
- **Multi-target apply_edit**: 여러 슬라이드의 같은 footer / disclaimer 를 한 번에 수정.

## 주의

- `slidev build` 는 Node 18+ 필요.
- frontmatter 의 `transition: slide-up` 같은 trans 는 Vue 내장만 지원.
- code block 의 라인 번호 highlight syntax `{1,3-5}` — comma 구분, range 는 hyphen.

## 참조

- 공식: https://sli.dev
- GitHub: https://github.com/slidevjs/slidev
- 라이선스: MIT
