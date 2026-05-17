# Skill 작성 (AI 용)

> Skill = markdown 한 파일. `.claude/skills/` 에 떨어뜨리면 HTMLook 이 다음 파일 watcher tick 에 인식.

## 에이전트가 신경 써야 할 이유

ChatPanel 안에서 실행 시 로더가 **top-5 관련 skill** 을 시스템 프롬프트에 inject. 잘 작성된 skill 이 매 대화의 프롬프트 보일러플레이트를 버전 관리 가능한 산출물로 옮김.

## 파일 위치

`<workspace>/.claude/skills/` (워크스페이스) 또는 `~/.claude/skills/` (글로벌). `name:` 충돌 시 워크스페이스 우승. `.agents/skills/` 형제는 Codex / Aider / Gemini CLI 호환.

## Frontmatter contract

```yaml
---
name: meeting-notes-cleanup     # 고유 식별자, kebab-case
description: |                   # 한 줄 요약, chip 에 표시
  화자별로 raw transcript 정리.
version: 1                       # 동작 변경 시 bump
tier: custom                     # custom | curated | verified
license: MIT                     # SPDX 식별자
trigger:                         # top-5 선택기가 찾는 방법
  workspace_kinds: [text, audio] # text / audio / video / pdf / image / code
  hint:                          # freeform 문자열; 매치 시 높은 가중치
    - "meeting"
    - "회의"
    - "minutes"
tools: []                        # 실행 시 필요한 MCP 도구
claims:                          # 언어별 추가 컨텍스트
  ko: "회의록을 화자별로 정리합니다."
  en: "Cleans up meeting transcripts speaker by speaker."
---
```

모든 필드 serde-default. 부분 frontmatter 도 OK.

## 본문 컨벤션

본문은 skill 이 inject 될 때 시스템 프롬프트의 일부. 프롬프트 템플릿으로 다루고 — 초점 유지.

동작하는 패턴:

```markdown
# 무엇을 하는가
화자가 여럿인 raw 회의 transcript 를 화자별 구조화 요약으로.

# 언제 사용
- 사용자가 화자 여럿 포함 음성 메모
- 또는 화자 라벨이 있는 transcribed 회의록

# 출력 모양
- 화자별 H2 섹션이 있는 markdown 문서
- 각 섹션: 결정 bullet, action item, blocker
- 파일 상단: 회의 날짜 + 참석자

# 호출해야 할 도구
- `htmlook_voice_transcript_get` → transcript 가져오기
- `htmlook_voice_workspace_all` → 워크스페이스 메모 enumerate
- `htmlook_create_file` → 메모 옆에 정리본 작성
```

## 언어 / 포맷 등록

skill 이 등록 가능:

- 코드블록 언어: `code_block: { fence: "mmd", icon: "mermaid" }` → markdown 뷰어가 ```` ```mmd ```` 블록을 여기로 라우팅
- export 포맷: `export: { format: "pptx", label: "Slide deck" }` → Export 드롭다운에 등장

```yaml
code_block:
  fence: mermaid
  icon: mermaid
export:
  format: mp4
  label: Animated SVG → mp4
```

## Skill ↔ tool whitelist

`tools:` 배열이 활성 상태일 때 skill 이 호출 허가받은 MCP 도구를 제한. defence-in-depth — 사용자가 글로벌하게 `apply_edit` 허용했더라도, 그것을 선언하지 않은 skill 은 호출 불가.

```yaml
tools:
  - htmlook_voice_transcript_get
  - htmlook_voice_workspace_all
  - htmlook_create_file
```

빈 리스트 = 도구 없음 (read-only skill, 프롬프트 내 변환만).

## 버전 + 마이그레이션

HTMLook 이 `<workspace>/.htmlook/tools.json` 의 스키마 버전 추적. skill frontmatter shape 을 breaking 변경 시:

- `version:` bump
- 다음 `tools_manifest` 로드가 `migrate_if_needed()` 실행 — in-place 재작성 전 `tools.json.bak.<ts>` 작성

## 작성 루프

1. `name`, `description`, `tools` 먼저 — 뼈대
2. 본문 추가 — "언제 사용" 과 "출력 모양" 부터
3. 앱에서 *Settings → Power tools → 스킬 재로드*
4. skill 트리거되어야 할 프롬프트로 ChatPanel 테스트
5. 반복; 동작 변경 시 `version` bump

## Skill 마켓플레이스 (미래)

`tier: curated` 는 Deep-On 리뷰 skill 예약. 미래 마켓플레이스가 워크스페이스 설치 가능 번들로 제공. `tier: verified` 는 빌트인.

지금은 작성한 skill 이 `tier: custom`. 필드 설정 → 사이드바 배지 반영.

## 다음

- [프롬프트 패턴 →](AI-Prompt-Patterns-ko.md)
- [에러 & 복구 →](AI-Errors-Recovery-ko.md)
