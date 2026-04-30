# HTMLook Sample Workspace

> 26 페르소나 영상에 등장한 모든 워크플로우를 직접 따라할 수 있는 샘플 워크스페이스.

## 시작하기

1. **HTMLook Pro 설치** — [htmlook.deep-on.com](https://htmlook.deep-on.com) 또는 자체 빌드
2. 이 폴더 (`sample_workspace/`) 를 HTMLook 에서 *Open Folder* 로 열기
3. 좌측 사이드바에 26 개 페르소나 폴더가 보임 (`01-hf-claude/` ~ `26-mobile-news/`)
4. 각 폴더의 `WALKTHROUGH.md` 가 그 페르소나의 follow-along 가이드

## 디렉토리 구조

```
sample_workspace/
├─ README.md           ← 이 파일
├─ CLAUDE.md           ← AI 협업 instructions (Claude/Llama/etc)
├─ .htmlook/
│   └─ mcp-config.example.json   ← MCP 클라이언트 설정 샘플
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

## 필요한 것 / 선택 사항

**필수**: HTMLook Pro 만 있으면 모든 워크스페이스 탐색·뷰·분할뷰·영역선택·라이브 에디팅 가능.

**선택 (AI cite + apply_edit)**: MCP 호환 LLM 클라이언트
- Claude Code (CLI) — `~/.config/claude-code/mcp.json` 에 `.htmlook/mcp-config.example.json` 참고
- Cursor / Windsurf / Zed — 같은 패턴
- Ollama + 호환 클라이언트 — 로컬 LLM (Llama 3.2 등)

각 페르소나 WALKTHROUGH.md 의 `[AI]` 표시된 단계는 LLM 필요. `[VIEW]` 단계는 HTMLook 단독으로 가능.

## A/B 비교 (LLM 없는 사용자용)

LLM apply_edit 결과를 미리 저장해 둔 페르소나는 `before/` `after/` 서브폴더가 있음.
LLM 없어도 두 상태를 분할뷰로 비교하면 워크플로우 결과를 시각적으로 이해 가능.

## 라이선스

샘플 콘텐츠 (텍스트, 이미지, PDF) 는 모두 fictional / public-domain / CC0.
실제 회사명, 인물명, 상표는 의도적으로 *Atlas / Apex / sample* 등 plain placeholder 로 대체.
