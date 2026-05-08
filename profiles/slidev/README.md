# Slidev Profile

Vue + Vite + Markdown 슬라이드 도구 [Slidev](https://sli.dev) 용 HTMLook Profile.

## 설치 (HTMLook Pro)

```
File → Install Profile from URL → https://github.com/deep-on/htmlook_campus/tree/main/profiles/slidev
```

또는 New Workspace Wizard 의 카탈로그에서 "Slidev" 선택.

## 시드 콘텐츠

`seed/slides.md` 와 `seed/package.json` 이 새 워크스페이스에 깔립니다.

```bash
pnpm install
pnpm dev   # http://localhost:3030
```

## HTMLook 활용 팁

- **Pane pair**: 좌측 `slides.md` 편집, 우측 viewer 가 `http://localhost:3030` iframe.
- **Region cite**: 한 슬라이드의 영역 캡처 → AI 에게 수정 지시.
- **Multi-target apply_edit**: 여러 슬라이드 footer 일괄 수정.

## 외부 의존

- Node 18+
- `pnpm` 또는 `npm` (lockfile 은 자유)

## 라이선스

본 Profile = MIT (deep-on).
Slidev 자체 = MIT (Anthony Fu / Slidev contributors).
