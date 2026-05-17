# 터미널

> 앱 안의 진짜 터미널. AI 어시스턴트 (Claude / Codex / Gemini) 가 같은 워크스페이스에 *함께* 앉도록 설계.

## 토글과 docking

| 동작 | 단축키 |
|---|---|
| 터미널 표시 / 숨김 | ⌘J |
| 현재 preset 으로 새 탭 | ⌘T |
| 활성 탭 닫기 | ⌘W (터미널 포커스 시) |
| 탭 순환 | ⌃⇥ / ⌃⇧⇥ |
| 활성 pane 상하 split | ⌘D |
| 활성 pane 좌우 split | ⌘⇧D |
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

## "Save as preset" — 책갈피 아이콘 버튼

터미널 탭에서 유용한 one-shot 프롬프트를 입력한 다음 (예: "마지막 테스트 출력 요약 + fix 제안") 책갈피 아이콘을 누르면 저장. 같은 프롬프트를 한 클릭에 활성 터미널로 paste 하는 새 버튼이 preset 툴바에 생성.

워크스페이스의 `.htmlook/` 에 저장.

## 한글 IME

한글 조합이 예상대로 동작합니다 — `다` 입력 시 `다` 가 나오고 `ㄷㅏ` 가 아님. IME 모드 전환 직후도 마찬가지. 조합 중 pre-edit 가 제 자리에 표시. 회귀가 보이면 `IME_DEBUG=true` 로그 (Settings → Terminal) 캡쳐해서 알려주세요.

## Pane 관리

각 탭이 Tmux 스타일 grid 로 최대 **6 pane**. ⌘D / ⌘⇧D 로 split. 활성 pane 은 살짝 밝은 border. 클릭으로 포커스. `Cmd+[` / `Cmd+]` 로 순환.

## 탭의 프로세스 트리

터미널이 각 탭에서 무엇이 실행 중인지 (`claude` · `codex` · `gemini` · 일반 셸) 추적하고 letter mark 에 반영. AI 가 출력 생성 중일 때 mark 가 부드럽게 pulse.

## OSC 7 cwd

셸이 OSC 7 emit 하면 (`bash` auto, `zsh` 은 `.zshrc` 에 snippet 추가) 탭 제목에 압축된 cwd (예: `~/W/htmlook`). brand letter mark 는 제목 왼쪽 유지.

## 선택을 터미널로 보내기

뷰어에서 텍스트 하이라이트 → ⌘⌥⇧T (또는 *View → Send Selection to Terminal*) → 활성 터미널 pane 에 paste. 문서의 "이 명령 실행" 같은 코드 샘플에 유용.

## 컨텍스트 메뉴

터미널 어디든 우클릭 — *복사* / *붙여넣기* / *전체 선택* / *스크롤백 지우기* / *터미널 리셋* / *탭 이름 변경* / *새 윈도우로 이동*.

## 다음

- [AI 어시스턴트 →](ChatPanel-BYOM-ko.md)
- [확장 (Extensions) →](Skills-ko.md)
