# Step 4 · Editing (Paint / Region / Element Pick)

<p align="center">
  <a href="README.md">English</a> | <b>한국어</b> | <a href="README.ja.md">日本語</a> | <a href="README.de.md">Deutsch</a> | <a href="README.fr.md">Français</a> | <a href="README.es.md">Español</a> | <a href="README.pt.md">Português</a> | <a href="README.it.md">Italiano</a>
</p>

> 화면 위에서 *어떤 영역인가* 를 LLM 에 알려주는 4 가지 방법.
> ~ 5 분.

HTMLook 의 가장 차별적인 부분. AI 에 *"여기 고쳐줘"* 라고 말할 때 *여기* 가
무엇인지를 painter 같은 도구로 직접 짚을 수 있습니다.

이번 step 끝나면: region 드래그 → cite anchor → AI prompt 라는 핵심 사이클을
직접 한번 실행해 봤을 것입니다.

## 4.1 · 4 가지 선택 방법 요약

| 방법 | 진입 | 용도 |
|---|---|---|
| **element pick** | preview 에서 클릭 | 단일 DOM 노드 (button / heading / paragraph) |
| **range select** | preview 에서 드래그 | 텍스트 범위 (sentence / phrase) |
| **region paint** ⭐ | ⌘shift+R 후 사각형 드래그 | 시각적 영역 (chart / 일러스트 영역) |
| **outline pick** | 우측 Outline 패널 클릭 | 헤딩 단위 |

영상: [BASIC #6 · Pick what you see.](../videos/features/06-basic-06-html-4mode.mp4)
(30 s)

## 4.2 · ⭐ Region cite — 가장 핵심

Step 4 에서 가장 중요한 동작. AI 와의 첫 *공동 언어* 입니다.

1. HTML 또는 PDF 파일 하나 열기 (예: [`../05-command/personas/01-hf-claude/landing.html`](../05-command/personas/01-hf-claude/landing.html))
2. ⌘shift+R 로 region paint 모드 진입
3. preview 위에서 사각형 드래그 → 영역이 magenta accent 로 highlight
4. 우측 AI 패널에 자동으로 cite anchor 가 첨부됨
5. AI 에 *"여기 좀 고쳐줘 — Apex 의 가치 (edge compute) 를 한 줄로"*

LLM 이 (MCP 가 연결됐다면):
- `htmlook_region_current_png` 로 영역의 PNG 를 가져옴 (vision 모델)
- `htmlook_active_file` + `htmlook_cite` 로 매칭 텍스트 anchor 를 확보
- `htmlook_apply_edit` 로 patch 적용

> 영상: [BASIC #5 ⭐ · Drag. Tell the LLM.](../videos/features/05-basic-05-region-cite.mp4)
> (30 s · AI 진입점)

## 4.3 · Element pick

preview 에서 element 위에 hover → 윤곽선 → 클릭 → 선택. 단축키 ⌘E 로 모드 토글.

선택된 element 의 outerHTML 은 `htmlook_selection_html` 로 LLM 이 읽음 →
patch 후 `htmlook_apply_edit`.

## 4.4 · Sentence-id (영상 / 텍스트 안에서 문장 단위)

긴 transcript / paper 에서 문장 #N 을 직접 cite:

1. 영상 / 긴 md 열기
2. 우측 패널 *Sentence Map* 토글 → 문장에 N 번호 표기
3. 클릭 → cite anchor `sentence:5` 가 AI 패널에 첨부

> 영상: [ADV · Click sentence 5. Clip ships.](../videos/features/14-advanced-08-sentence-id.mp4)
> (30 s)

## 4.5 · Range select — 그냥 드래그

가장 일반적. preview 에서 텍스트 드래그 → 자동으로 selection_text /
selection_html 둘 다 사용 가능.

## ✅ Step 4 체크포인트

- region paint 모드를 ⌘shift+R 로 켜서 사각형 한번 그려봤다.
- 그려진 영역이 AI 패널에 cite anchor 로 첨부되는 것을 확인.
- AI 에 한 마디 보내서 patch 받음 (응답이 *어딘가* 에 cite 가 있어야 함).

다 맞으면 → [Step 5 · command (terminal / chat / apply)](../05-command/)

## 더 자세히

- [`../03-byom-setup/AI_GUIDE.md`](../03-byom-setup/AI_GUIDE.md) — MCP 도구
  목록 (selection / region / element / cite).
- [`../05-command/personas/`](../05-command/personas/) — 26 페르소나 walkthrough
  (각 페르소나가 region/element/sentence cite 중 어떤 패턴 쓰는지 다양).
