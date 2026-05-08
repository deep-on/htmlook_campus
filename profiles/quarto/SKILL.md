---
name: quarto
description: Posit Quarto 출판 시스템 (.qmd → PDF/HTML/PPT/book) 워크플로우.
---

# Quarto 워크플로우

R Markdown + Bookdown 의 후속, 다중 출력. 학술 / 데이터 / 기술문서 표준화 도구.

## 발견 신호

- `_quarto.yml` (project mode)
- `.qmd` 파일 (single doc mode)
- `index.qmd`, `references.bib`, `_freeze/` 캐시

## 작업 패턴

1. **single doc**: `index.qmd` 의 frontmatter 에 format 지정 → `quarto render index.qmd`
2. **project**: `_quarto.yml` 에 `project.type: book / website / default` → `quarto preview` 가 watch.
3. **인용**: `references.bib` 등록 + `[@key]` syntax. CSL 스타일 frontmatter `csl: ieee.csl`.
4. **executable cells**: ```` ```{python} ```` / ```` ```{r} ```` — Jupyter 또는 knitr engine.

## HTMLook 시그니처 활용

- **xlsx_cite**: Quarto inline data table (`| cell |`) ↔ 원본 xlsx 셀 양방향 cite. 셀 변경 → 표 자동 갱신 패턴.
- **Region cite**: 그림 / 표 / 코드 블록 한 영역 캡처 → AI 에게 캡션 / 설명 / 본문 통합 요청.
- **Pane pair**: 좌 `.qmd` ↔ 우 rendered HTML (`quarto preview` 의 localhost:4848).

## 자주 쓰는 frontmatter

```yaml
---
title: "Q3 매출 분석"
author: "Vincent Kim"
date: "2026-05-08"
format:
  html:
    toc: true
    code-fold: true
  pdf:
    documentclass: article
    geometry: margin=1in
bibliography: references.bib
csl: ieee.csl
---
```

## 주의

- PDF 출력 = TinyTeX / TeX Live 필요 (`quarto install tinytex`).
- Jupyter engine 은 cells.json 의 outputs 가 `_freeze/` 에 캐시 — git 에 commit 권장 (재실행 안정).
- `quarto preview` 의 livereload 는 markdown 변경에는 빠르지만 코드 cell 재실행은 수동.

## 참조

- 공식: https://quarto.org
- GitHub: https://github.com/quarto-dev/quarto-cli (CLI: GPL-2.0)
- 라이선스: 본 Profile = MIT, Quarto CLI = GPL-2.0 (별도 설치)
