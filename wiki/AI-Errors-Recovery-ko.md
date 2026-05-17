# 에러 & 복구

> HTMLook 이 실패를 어떻게 표면화하고, 실제 문자열은 어떻게 생겼고, 어떻게 대응할지.

## 실패의 shape

HTMLook 의 MCP 도구는 구조화된 `error.data.kind` enum 을 **반환하지 않습니다**. 거의 모든 실패는 두 가지 방식 중 하나로 표면화된 평문:

1. **MCP 에러로** (`error.message` 가 텍스트 담음, 머신 판독 `kind` 없음)
2. **`CallToolResult::success` 의 텍스트 본문이 prefix 로 시작** — `refused: …` 또는 `rate-limited: …` 같이

구조화된 유일한 예외는 `DEPENDENCY_MISSING:` (아래) — 그 prefix 뒤에 파싱 가능한 JSON payload.

그 외 모든 것에 대해 **메시지 prefix 로 패턴 매치**. 아래 표는 v1.0.9 빌드에서 실제 보일 prefix.

## Prefix 표

| 보일 prefix | 의미 | 대응 |
|---|---|---|
| `find string matched N places in <abs>; expected exactly 1.` | `apply_edit` find 가 모호 (>1 매치) | 주변 맥락 추가해 find 좁히기 |
| `find string not found in <abs>.` | `apply_edit` find 부재 | 렌더러로 파일 재읽기. `find_in_active` 먼저 |
| `refused: <p> is outside the current workspace. Open the file in HTMLook Pro first…` | path-guard 가 워크스페이스 바깥 대상 거부 | 워크스페이스 안 경로 사용 |
| `canonicalize <p>: No such file or directory` | 디스크에 대상 없음 | `workspace_files` / `active_file` 확인 |
| `refused: HTMLook is in Free Viewer mode (trial expired). Upgrade to Pro to enable edits.` | 라이선스 gate | 사용자에게 surface; 우회 불가 |
| `rate-limited: <tool_name> burst exhausted. Retry after ~<ms> ms.` | 도구별 token bucket (burst 8, 초당 8 refill, **도구별**) | 명시 ms back off; retry-loop 금지 |
| `selector "<sel>" matched no elements in <pane> pane` | `capture_selector` / `select_element` 가 0 매치 | `layout_map` 으로 실 selector 찾기 |
| `text "<t>" not found in <pane> pane (mode=<mode>)` | `capture_text_match` 의 quote 가 화면에 없음 | `find_in_active` 로 visibility 확인 |
| `no <pane> viewer pane available — open a file first` | 타겟 pane 미마운트 | 그 pane 에 파일 먼저 열기 |
| `<pane> viewer is not same-origin (cross-origin srcdoc, asset:// load barrier)…` | iframe 이 이 캡처의 DOM 접근 차단 | `capture_viewport` 또는 `capture_rect` 사용 |
| `DEPENDENCY_MISSING:{…}` | 외부 도구 부재 (ffmpeg / soffice / …) | 특별 — 아래 참조 |

이 표에 없는 prefix 면 일반 forwarded backend 에러 — 사용자에게 텍스트로 surface.

## DEPENDENCY_MISSING envelope

에러이자 UX 순간이라 특별 처리.

메시지 형태:

```
DEPENDENCY_MISSING:{"dep_id":"ffmpeg","dep_label":"FFmpeg","purpose":"비디오 씬 감지","install_via":"brew install ffmpeg","brew_present":true}
```

`DEPENDENCY_MISSING:` prefix 제거 후 JSON 파싱:

```jsonc
{
  "dep_id":       "ffmpeg",
  "dep_label":    "FFmpeg",
  "purpose":      "비디오 씬 감지",
  "install_via":  "brew install ffmpeg",
  "brew_present": true
}
```

동시에 사용자는 HTMLook 에 actionable toast 봄 — **지금 설치** / **명령어 복사** / **닫기**. 에이전트 역할: *왜* 필요했는지, *무엇이* 일어날지, ffmpeg 설치가 ~30 s 걸린다는 것 설명. 사용자가 설치 확인 전 원 호출 재시도 말 것 (toast 가 `htmlook:dependency-install-done` 이벤트를 publish, 앱이 내부 처리 — agent 측에선 사용자가 ping 할 때까지 대기가 더 쉬움).

`brew_present: false` 면 toast 가 Homebrew 먼저 설치 (~3 분). 인내 — 설치 중 재시도 말 것.

## 사용자에게 묻기

폴링 없이 사용자를 끼우는 작은 primitive 4 가지:

| 도구 | 인자 | 메모 |
|---|---|---|
| `htmlook_confirm` | `{ prompt, timeout_ms? }` | boolean 반환. 단일 `prompt` 문자열 — `title` / `message` 분리 없음. |
| `htmlook_request_user_input` | `{ prompt, default_value?, timeout_ms? }` | 문자열 반환 |
| `htmlook_wait_for_user_action` | `{ hint, timeout_ms? }` | 사용자 hint 버튼 클릭까지 block |
| `htmlook_show_toast` | `{ message, kind?: 'info'\|'success'\|'warn'\|'error', duration_ms? }` | fire-and-forget 알림. 필드는 `kind`, 유효 값 `info / success / warn / error` (`level: "warning"` 아님). |
| `htmlook_chatpanel_post` | `{ role: 'user'\|'assistant'\|'note', content }` | ChatPanel 대화 스트림에 메시지 push. `role` 필수, 필드는 `content` (text 아님). |

기본: "되돌릴 수 없는 액션" 에 `confirm`, "추정 어려운 값 필요" 에 `request_user_input`.

## 복구 패턴

### Idempotent retry + rate-limit back-off

```python
for attempt in range(3):
    res = call_tool(...)
    if not is_error(res):
        break
    msg = res.error.message
    if msg.startswith("rate-limited:"):
        # 메시지에서 "~Nms" 파싱
        retry_ms = parse_retry_ms(msg)
        sleep(retry_ms / 1000.0 * 1.2)   # 20% 안전 마진
        continue
    break  # 다른 에러는 변경 없이 재시도 무의미
```

### Cascade 인식 retry

`apply_edit` 가 파일이 바뀌어서 실패 (file-not-found, 또는 예상한 1 매치인데 여러 매치) 시 `active_file` 로 재 fetch + 재계획 — 같은 find/replace 맹목 재시도 말 것.

### 정중하게 포기

같은 작업 2회 실패 후 사용자에게 surface:

```
show_toast({
  message: "두 번 시도했지만 이 변경을 자동 적용할 수 없습니다.",
  kind:    "warn"
})
chatpanel_post({
  role:    "assistant",
  content: "…를 변경하려 했지만 파일이 바뀌었습니다. 직접 하시겠어요, 아니면 다른 접근?"
})
```

## 자기 실패 audit

`audit_log_query({ tool: "htmlook_apply_edit", since_ts: today_start_ms })` 가 오늘의 tool call 반환 (성공/실패는 서버 사이드 분리 안 됨 — 각 `args` 항목 검사하고 응답에서 본 내용과 cross-reference).

## 버그 보고

`INTERNAL_ERROR` (`-32603` JSON-RPC 코드) 또는 모르는 prefix 만나면 사용자에게 최신 `/tmp/htmlook-debug.log` 마지막 ~500 줄 첨부해서 support 로 이메일 요청.

## 끝

[개요](AI-Overview-ko.md) · [도구 카탈로그](AI-Tool-Catalog-ko.md) · [Home](Home-ko.md) 로
