# Quarto Profile

학술 / 데이터 / 기술문서용 [Quarto](https://quarto.org) HTMLook Profile.

## 시작

```bash
quarto preview        # http://localhost:4848 (live)
quarto render         # 정적 빌드 → _output/
```

## HTMLook 활용

- **xlsx_cite ⭐**: 본문 표의 셀 ↔ 원본 xlsx — 양방향 cite. 표 셀 변경 → AI 가 본문 코멘트 자동 업데이트.
- **Region cite**: 그림 / 코드 블록 캡처 → AI 에게 캡션 보강.
- **Pane pair**: `.qmd` ↔ `quarto preview` localhost:4848.

## 외부 의존

- Quarto CLI (https://quarto.org/docs/get-started/) — GPL-2.0
- PDF 출력 = TinyTeX (`quarto install tinytex`)
- Python / R cell 실행 = 별도 환경

## 라이선스

본 Profile = MIT (deep-on). Quarto CLI = GPL-2.0 (사용자가 별도 설치).
