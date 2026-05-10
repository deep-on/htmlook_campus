# Persona Workspaces — Step 5 follow-along set

> 26 페르소나 영상에 등장한 모든 워크플로우를 직접 따라할 수 있는 샘플 워크스페이스.
> [Step 5 · command](../README.md) 의 cite + apply_edit 흐름을 자기 도메인에서
> 적용해 봅니다. HTMLook Pro v1.0 release-candidate 기준.

## 시작하기

1. **HTMLook Pro 설치** — [htmlook.app](https://htmlook.app) 에서 .dmg 다운로드
   (14 일 무료 체험 · BYOM 토큰 마진 0)
2. 이 폴더 (`05-command/personas/`) 를 HTMLook 에서 *Open Folder* 로 열기
3. 좌측 사이드바에 26 개 페르소나 폴더가 보임 (`01-hf-claude/` ~ `26-mobile-news/`)
4. 각 폴더의 `WALKTHROUGH.md` 가 그 페르소나의 follow-along 가이드
5. AI 사용 시 [`../../03-byom-setup/AI_GUIDE.md`](../../03-byom-setup/AI_GUIDE.md)
   참고 — MCP 도구 노출, BYOM / Terminal CLI / 외부 클라이언트 연결 모두 동일

> 폭넓은 도구 시드를 원하면 상위 [`../../sample_workspaces/`](../../sample_workspaces/)
> (75 폴더 · marimo / d2 / manim / quarto / slidev / astro / excalidraw /
> hyperframes 도메인) 또는 앱 내 **Add wizard** 의 카탈로그 카드를 참고.

## 디렉토리 구조

```
05-command/personas/
├─ README.md           ← 이 파일
├─ INDEX.md            ← 26 페르소나 카탈로그 + 권장 시청 순서
├─ 01-hf-claude/
│   ├─ WALKTHROUGH.md
│   ├─ source files...
│   └─ before/after/  (LLM 없이도 비교 가능하도록)
├─ 02-hf-llama/
├─ ...
└─ 26-mobile-news/
```

## 페르소나 카테고리

| 그룹 | 페르소나 | 주요 워크플로우 |
|---|---|---|
| **개발** | hf-claude, hf-llama, dev-pr-docs | 코드 ↔ 결과 ↔ docs |
| **콘텐츠** | creator-podcast, press-editor, hobby-fiction, picture-book | 오디오/비디오 → 글 |
| **분석** | data-analyst, finance-report, research-notes, economy-analyst | 데이터 → narrative |
| **법무/번역** | legal-redline, translator-book, domain-battery | PDF cite → memo |
| **교육 (선생님)** | teacher-quiz, teacher-newsletter, teacher-record | 자료 → 인쇄물 |
| **교육 (학생)** | student-notes, student-flashcard, kid-coding, homework-helper, kids-science-mag | 노트 → 학습 |
| **비즈니스** | corp-deck, product-prd | 자료 → 발표/스펙 |
| **일상** | recipe-card, mobile-news | 글 → 시각화 |

전체 카탈로그 + 권장 순서는 [`INDEX.md`](INDEX.md) 참고.

## 필요한 것 / 선택 사항

**필수**: HTMLook Pro 만 있으면 모든 워크스페이스 탐색·뷰·분할뷰·영역선택·라이브 에디팅 가능.

**선택 (AI cite + apply_edit)** — 셋 중 어느 것이든 (자세한 설정은
[Step 3 · BYOM setup](../../03-byom-setup/) 참고):

- **HTMLook Pro 내장 BYOM 채팅** — Settings → Models 에서 키 등록만 하면
  Claude / GPT / Gemini / DeepSeek / Mistral / Together / Groq / Cerebras /
  Ollama 채팅 패널 활성화 (토큰 마진 0).
- **HTMLook Pro 내장 Terminal + CLI 어댑터** — ⌘J PTY 터미널에서
  `claude` / `codex` / `gemini` CLI 가 워크스페이스 컨텍스트 자동 주입
  (UserPromptSubmit hook).
- **외부 MCP 클라이언트** — Claude Code / Cursor / Windsurf / Zed 의
  `mcp.json` 에 [`../../03-byom-setup/.htmlook/mcp-config.example.json`](../../03-byom-setup/.htmlook/mcp-config.example.json) 병합.

각 페르소나 WALKTHROUGH.md 의 `[AI]` 표시된 단계는 LLM 필요. `[VIEW]` 단계는 HTMLook 단독으로 가능.

## A/B 비교 (LLM 없는 사용자용)

LLM apply_edit 결과를 미리 저장해 둔 페르소나는 `before/` `after/` 서브폴더가 있음.
LLM 없어도 두 상태를 분할뷰로 비교하면 워크플로우 결과를 시각적으로 이해 가능.

## 라이선스

샘플 콘텐츠 (텍스트, 이미지, PDF) 는 모두 fictional / public-domain / CC0.
실제 회사명, 인물명, 상표는 의도적으로 *Atlas / Apex / sample* 등 plain placeholder 로 대체.
