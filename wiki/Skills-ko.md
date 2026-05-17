# Skills

> 폴더에 `SKILL.md` 를 떨어뜨리면 HTMLook 이 AI 가 쓸 수 있는 도구로 인식.

## Skill 이란

YAML frontmatter 가 invoke 방법 + 조건을 말하고, 본문은 AI 에게 보이는 지시문인 평범한 markdown 파일. 누구나 — 본인, 동료, Deep-On 팀 — 작성해서 워크스페이스에 떨어뜨리면 됨.

```markdown
---
name: 회의록-정리
description: Speaker-by-speaker meeting note refinement
version: 1
tier: custom
trigger:
  workspace_kinds: [text, audio]
  hint: "meeting", "회의", "minutes"
tools: []
license: MIT
---

# What this does
Polishes raw meeting transcripts into a clean per-speaker summary…
```

## Skill 위치

| 경로 | 스코프 | 비고 |
|---|---|---|
| `<workspace>/.claude/skills/` | 워크스페이스 | 이름 충돌 시 우승 |
| `<workspace>/.agents/skills/` | 워크스페이스 (cross-tool) | Codex · Aider · Gemini CLI 호환 |
| `~/.claude/skills/` | 글로벌 | 개인 컬렉션 |
| `~/.agents/skills/` | 글로벌 cross-tool | — |

HTMLook 이 launch 시 + 파일시스템 변경 시 스캔. 같은 `name:` 이면 워크스페이스가 글로벌 덮어씀.

## Tier 배지

- **Verified** (🟦 cyan) — built-in, 바이너리 동봉
- **Curated** (🟨 amber) — Deep-On 리뷰 (향후 마켓플레이스)
- **Custom** (◯ neutral) — 워크스페이스 추가

사이드바 *Power tools* expansion 옆 + ChatPanel chip 으로 표시.

## 빌트인 skill (v1.0.9)

- **Mermaid** — ```` ```mermaid ```` / ```` ```mmd ```` 블록 렌더
- **D2** — ```` ```d2 ```` 블록 렌더
- **Smart Markdown** — export 시 pandoc 스타일 polish
- **Pandoc Wrap** — DOCX / PDF 를 pandoc 으로
- **Slide Deck** — markdown section 으로부터 pptx export

## Skill 이 도구가 되는 흐름

AI 가 호출 시 HTMLook 이:

1. skill 의 `tools:` 배열 읽기 — 필요로 하는 sub-tool 들
2. skill 본문을 system prompt 에 inject
3. skill 지시를 top-priority 로 모델 컨텍스트 설정
4. 발생하는 tool call 은 BYOM 동의 흐름으로 dispatch

skill 작성자가 `trigger:` 블록 — `workspace_kinds` + 자유 형식 `hint` — 을 선언하면 top-5 selector 가 현재 대화 관련성 판단에 사용.

## UI 에서 skill 추가

*사이드바 → Power tools → +Add*. 마법사가 이름 · 설명 · 버전 · 라이선스 · 본문 묻기. `<workspace>/.htmlook/tools.json` + (선택) 짝맞는 `SKILL.md`.

`git clone` 으로 skill 컬렉션을 `.claude/skills/` 에 넣으면 다음 파일 watcher tick 에서 인식.

## 자동 마이그레이션

HTMLook 이 `tools.json` 의 스키마 버전을 추적. 시작 시 `migrate_if_needed()` — 타임스탬프 suffix 백업 작성 + forward 마이그레이션. 현재 스키마 v2.

## Markdown 코드블록 dispatch

skill 이 fenced-code 언어 등록 가능. markdown 뷰어가 ```` ```mmd ```` 를 보면 본문을 Mermaid skill 의 렌더러로 라우팅, ```` ```d2 ```` 는 D2 skill 로. 새 언어는 skill 매니페스트로 등록 — "graphviz" 추가 = 워크스페이스 파일 한 개.

## Export 메뉴 통합

skill 이 **export 포맷** 도 등록 가능. skill 매니페스트가 `{ format: "mp4", label: "Animated SVG → mp4" }` 추가 → Export 드롭다운에 빌트인 옆에 등장.

## 에러

Error-Copy 표 (`docs/SKILL_ERROR_COPY.md`) 가 내부 에러 코드를 친화 문자열로 매핑 — `tools:` 필드 누락 시 스택 트레이스 대신 "Skill is missing a required field: tools" 표시.

## 다음

- [Export →](Export-ko.md)
- [AI 에이전트용 · Skill 작성 →](AI-Skill-Authoring-ko.md)
