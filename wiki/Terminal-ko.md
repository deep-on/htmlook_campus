# 터미널

> 앱 안의 진짜 PTY. AI 에이전트 (Claude / Codex / Gemini) 가 같은 워크스페이스에 *함께* 앉도록 설계.

## 토글과 docking

| 동작 | 단축키 |
|---|---|
| 터미널 패널 표시 / 숨김 | ⌘\` |
| 현재 preset 으로 새 탭 | ⌘T |
| 활성 탭 닫기 | ⌘W (터미널 포커스 시) |
| 탭 순환 | ⌃⇥ / ⌃⇧⇥ |
| 활성 pane 좌우 split | ⌘D |
| 활성 pane 상하 split | ⌘⇧D |
| dock 위치 순환 (bottom / right / left / center) | Activity Bar 아이콘, 또는 grip 드래그 |

패널 안쪽 가장자리의 드래그 핸들로 크기 조절.

## Preset (네 개의 "+" 버튼)

preset 툴바가 특정 CLI 로 실행되는 새 탭을 엽니다:

| Preset | 명령 | Letter mark |
|---|---|---|
| Claude | `claude` | **Cl** |
| Codex | `codex` | **Cx** |
| Gemini | `gemini` | **Gm** |
| Shell | (`$SHELL`, 기본 `zsh`) | **Sh** |

탭에 letter mark 가 표시되고 출력이 stream 중일 때 애니메이션. 실행 명령은 *Settings → Terminal → Preset commands* 에서 편집.

폭이 좁아지면 툴바 collapse: 버튼 라벨 사라지고 brand letter mark 만 남음.

## "Save as skill" — 책갈피 아이콘 버튼

터미널 탭에서 유용한 one-shot 프롬프트를 실행한 다음 (예: "마지막 테스트 출력 요약 + fix 제안") 책갈피 아이콘을 누르면 *prompt preset* 으로 저장. 같은 프롬프트를 한 클릭에 활성 터미널로 paste 하는 새 버튼이 preset 툴바에 생성.

워크스페이스의 `.htmlook/prompt-presets.json` 에 저장.

## 한글 IME

터미널은 전용 state machine (KoreanComposer — v1.0.9 에서 추출) 으로 한글 조합 처리. `composedState { cho, jung, jong }` 추적, `0xAC00 + cho*21*28 + jung*28 + jong` 로 한글 syllable 합성. 복합자음 (ㄳ ㄵ ㄶ ㄺ …) + 복합모음 (ㅘ ㅙ ㅚ …) 처리.

v1.0.9 에서 fix 되어 그대로 유지되는 버그:
- 모드 토글 후 첫 jamo "다" 가 "ㄷㅏ" 로 분리 안 됨
- 아웃포커스 → 포커스 첫 글자 doubling
- single-character 한글의 `xterm.onData` doubling
- PTY write 순서 interleave (Promise-chain serializer)

회귀 발견 시 `IME_DEBUG=true` 로그 받아 issue.

## Pane 관리

각 탭이 Tmux 스타일 grid 로 최대 **6 pane**. ⌘D / ⌘⇧D 로 split. 활성 pane 은 살짝 밝은 border. 클릭으로 포커스. `Cmd+[` / `Cmd+]` 로 순환.

## 프로세스 트리 + buffer 읽기

각 탭이 프로세스 트리 노출 (*Cl/Cx/Gm/Sh* 글리프 + `htmlook_terminal_process_tree` MCP 도구가 사용). AI 에이전트나 앱 자체가 라이브 스크롤백을 `htmlook_terminal_buffer_get` 으로 읽기 가능 — "마지막 50줄 내용" 리뷰에 유용.

## OSC 7 cwd

셸이 OSC 7 emit 하면 (`bash` auto, `zsh` 은 `.zshrc` 추가) 탭 제목에 압축된 cwd (예: `~/W/htmlook`). brand letter mark 는 제목 왼쪽 유지.

## 활성 터미널에 프롬프트 보내기

`htmlook-pro:send-to-terminal` 윈도우 레벨 이벤트가 prompt-preset 버튼 + MCP 도구에서 사용. webview 렌더 preview 안에서:

```js
window.dispatchEvent(new CustomEvent('htmlook-pro:send-to-terminal', {
  detail: { text: 'pytest -q tests/test_failures.py' }
}));
```

## 컨텍스트 메뉴

터미널 어디든 우클릭 — *복사* / *붙여넣기* / *전체 선택* / *스크롤백 지우기* / *터미널 리셋* / *탭 이름 변경* / *새 윈도우로 이동*.

## 다음

- [ChatPanel · BYOM →](ChatPanel-BYOM-ko.md)
- [Skills →](Skills-ko.md)
