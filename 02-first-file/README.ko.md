# Step 2 · 첫 파일 (HTML / Markdown / PDF / 영상)

<p align="center">
  <a href="README.md">English</a> | <b>한국어</b> | <a href="README.ja.md">日本語</a> | <a href="README.de.md">Deutsch</a> | <a href="README.fr.md">Français</a> | <a href="README.es.md">Español</a> | <a href="README.pt.md">Português</a> | <a href="README.it.md">Italiano</a>
</p>

> HTMLook 의 *뷰어* 본질을 익힙니다. AI / MCP 없이도 가치가 있는 파트.
> ~ 5 분.

이번 step 끝나면: 4 가지 파일 종류 (md / html / pdf / 영상) 각각을 어떻게
읽고, 분할뷰 / 미리보기 / outline 으로 navigate 하는지 알게 됩니다.

## 2.1 · Markdown 라이브 에디트

1. 사이드바에서 임의의 `.md` 파일 (예: [`../05-command/personas/03-dev-pr-docs/docs.md`](../05-command/personas/03-dev-pr-docs/docs.md)) 더블클릭
2. ⌘\\ 또는 메뉴 *View → Split* 으로 분할뷰 토글
3. 좌측 source, 우측 preview. 좌측에서 타이핑하면 우측이 라이브 갱신

> 영상: [BASIC #3 · Type left. See right. Live.](../videos/features/03-basic-03-md-live-edit.mp4)
> (30 s)

## 2.2 · HTML — element 클릭해서 직접 수정

1. `.html` 파일 (예: [`../05-command/personas/01-hf-claude/landing.html`](../05-command/personas/01-hf-claude/landing.html))
   더블클릭
2. 기본 모드는 preview. 분할뷰에서 element 직접 클릭 → 텍스트 수정창이 뜸
3. 양방향 sync — preview 의 변경이 source 에 즉시 반영

> 영상: [BASIC #4 · Click anything. Edit it.](../videos/features/04-basic-04-html-split.mp4)
> (30 s)

## 2.3 · HTML 4가지 선택 모드

같은 HTML 파일에서 ⌘E 로 선택 모드 전환:

| 모드 | 동작 |
|---|---|
| element | 단일 DOM 노드 |
| range | 텍스트 범위 |
| region | 사각형 페인트 |
| outline | 헤딩 트리 |

영상: [BASIC #6 · Pick what you see.](../videos/features/06-basic-06-html-4mode.mp4) (30 s)

각 모드의 결과는 [Step 4 · editing](../04-editing/) 의 cite anchor 진입점입니다.

## 2.4 · PDF — 페이지 + 텍스트 layer

1. 임의의 `.pdf` 파일 (예: [`../05-command/personas/05-domain-battery/vendor.pdf`](../05-command/personas/05-domain-battery/vendor.pdf))
   더블클릭
2. 좌측 thumbnail navigator + 우측 페이지 캔버스 + 텍스트 selection 가능
3. 영역 드래그 → region cite (Step 4 에서 사용)

## 2.5 · 영상 — frame thumbnail + outline

1. 임의의 mp4 (예: [`../videos/features/01-basic-01-drop-open.mp4`](../videos/features/01-basic-01-drop-open.mp4))
   더블클릭
2. 영상 viewer 가 timeline + thumbnail 미리보기를 표시
3. ⌘shift+T 또는 hover 로 frame 위에 1 초 미리보기 (스크럽 없이)

> 영상: [ADV · Frame check. No scrub.](../videos/features/15-advanced-09-thumbnail.mp4)
> (30 s, advanced 카테고리)

## 2.6 · Outline — 큰 문서 navigate

긴 md / html / PDF 의 헤딩 구조 → 우측 패널의 Outline 탭. 헤딩 클릭하면
그 위치로 jump.

> 영상: [ADV · Click §3.2. You're there.](../videos/features/16-advanced-10-outline.mp4)
> (30 s)

## 2.7 · 분할뷰 / 멀티 pane (⌘1 / ⌘2 / ⌘3 / ⌘J)

| 단축키 | 효과 |
|---|---|
| ⌘1 | Preview only |
| ⌘2 | Source only |
| ⌘3 | Split (preview + source) |
| ⌘J | Terminal panel toggle |

영상: [ADV · Two keys. Three views.](../videos/features/10-advanced-04-multi-pane.mp4)
(30 s — 영상 narration 의 *"Two keys"* 는 ⌘D + ⌘J 였다가 v1.0 에서 ⌘1/⌘2/⌘3 + ⌘J 로 정정됐습니다. 자세한 lineage 는 [`../08-extend/PRODUCTION.md`](../08-extend/PRODUCTION.md) 의 *fix 된 false claims* 표 참고.)

## ✅ Step 2 체크포인트

- md / html / pdf / 영상 4 종을 분할뷰로 열어봤다.
- HTML 4 모드 (element / range / region / outline) 의 차이를 직접 클릭으로 체감.
- ⌘1 / ⌘2 / ⌘3 / ⌘J 로 화면 레이아웃 토글이 익숙해졌다.

다 맞으면 → [Step 3 · BYOM setup](../03-byom-setup/) — 한 vendor 만 골라서
key 등록.
