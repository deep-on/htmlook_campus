---
name: astro-starlight
description: Astro Starlight 모던 docs 사이트 (.mdx → 멀티페이지 HTML).
---

# Astro Starlight 워크플로우

Docusaurus / VitePress 후속격, 2025 dev 커뮤니티 기본 docs 도구. Astro 0.x → 5.x 성숙.

## 발견 신호

- `astro.config.mjs` 안에 `@astrojs/starlight` integration
- `src/content/docs/` 하위 .md / .mdx 파일들
- `package.json` 에 `@astrojs/starlight`

## 작업 패턴

1. **새 페이지**: `src/content/docs/<slug>.md` 추가 → 사이드바 자동 등록.
2. **사이드바 그룹화**: `astro.config.mjs` 의 `starlight.sidebar` 에 `{ label, items }`.
3. **컴포넌트 임베드**: `.mdx` 파일에서 React/Vue/Svelte/Solid 컴포넌트 직접 사용.
4. **i18n**: `src/content/docs/<locale>/...` 구조 + `starlight.locales` 등록.

## HTMLook 시그니처 활용

- **Pane pair**: 좌 `.mdx` 편집 ↔ 우 `astro dev` (localhost:4321) live.
- **Multi-target apply_edit ⭐**: docs 사이트 전체에서 동일 용어 / 링크 일괄 수정.
- **Region cite**: 한 페이지의 코드 블록 / 다이어그램 → AI 에게 명확화.

## frontmatter 패턴

```yaml
---
title: API Reference
description: htmlook_apply_edit endpoint.
sidebar:
  order: 2
  badge: { text: "v1.0", variant: "tip" }
---
```

## 주의

- Starlight 는 `src/content/docs` 외부의 .md 는 자동 인식 X — explicit `content collection` 필요.
- MDX 컴포넌트 import 는 frontmatter 아래 가장 첫 줄에.
- Astro 5.x 부터 `astro:env` 환경 변수 — 이전 버전 코드와 호환 주의.

## 참조

- 공식: https://starlight.astro.build
- GitHub: https://github.com/withastro/starlight (MIT)
- 라이선스: 본 Profile = MIT, Astro/Starlight = MIT
