# 에러 & 복구

> HTMLook 이 emit 하는 모든 에러 코드 + 의미 + 대응.

## 에러 응답 shape

HTMLook 은 JSON-RPC. 실패한 tool call:

```jsonc
{
  "jsonrpc": "2.0",
  "id": 17,
  "error": {
    "code": -32000,
    "message": "MULTIPLE_MATCHES: 'Sign up' occurs 8 times",
    "data": {
      "kind": "MULTIPLE_MATCHES",
      "count": 8,
      "path": "site/hero.html"
    }
  }
}
```

`error.message` 가 사람용 prefix. `error.data.kind` 가 머신 안정 코드. 둘 다 사용 — `kind` 는 버전 간 안정, 메시지 문구는 아님.

## 코드 reference

### 편집 / 파일 에러

| `kind` | 의미 | 복구 |
|---|---|---|
| `MULTIPLE_MATCHES` | `find` 가 >5× 발생 | `find` 좁히기 (긴 맥락); 또는 selector 기반 `select_element` + `replace_in_active` |
| `NO_MATCH` | `find` 부재 | 현재 파일 내용 재읽기. `find_in_active` 먼저 |
| `PATH_OUT_OF_SCOPE` | 워크스페이스 root 바깥 | 워크스페이스 안 경로 사용 |
| `FILE_NOT_FOUND` | 대상 존재 안 함 | `workspace_files` / `active_file` 먼저 |
| `STALE_HASH` | 읽고 쓰는 사이 파일 변경 | 재읽기, 재계획 |

### 권한 / 동의

| `kind` | 의미 | 복구 |
|---|---|---|
| `PERMISSION_REFUSED` | 사용자가 동의 모달 "No" | 이 세션 안에서 같은 호출 재시도 말 것. `show_toast` 로 거부 surface |
| `PERMISSION_PENDING` | 동의 모달 아직 열림 | block, 재발행 말 것. 사용자 클릭 시 원 호출이 resolve |
| `WORKSPACE_DENIED` | 워크스페이스 전체에서 tool 해제됨 | *Settings → Permissions* 에서 재활성 권유 |

### Capture / DOM

| `kind` | 의미 | 복구 |
|---|---|---|
| `SELECTOR_NOT_FOUND` | CSS selector 미매치 | `layout_map` 으로 실제 selector 찾기 |
| `TEXT_NOT_FOUND` | `capture_text_match` 가 문자열 못 찾음 | `find_in_active` 로 렌더 뷰에 문자열 존재 확인 |
| `ZERO_SIZE_ELEMENT` | selector 는 매치되지만 `display: none` / 0×0 | `visual_overlap_check` 로 진단 |
| `VIEWPORT_DETACHED` | 탭이 현재 보이지 않음 | `focus_tab` 먼저 |

### Rate limit / 상태

| `kind` | 의미 | 복구 |
|---|---|---|
| `RATE_LIMITED` | 토큰 버킷 소진 (도구별 초당 8) | ~125 ms back off. retry-loop **말 것** |
| `TOOL_DISABLED` | 이 빌드에서 명시적 비활성 | 재시도 말고 다른 접근 |
| `INTERNAL_ERROR` | 백엔드 panic | `show_toast` 로 사용자에게 보고. 디버깅 시 `/tmp/htmlook-debug.log` 마지막 10 줄 |

### 외부 의존성

| `kind` | 의미 | 복구 |
|---|---|---|
| `DEPENDENCY_MISSING` | 외부 도구 (ffmpeg, soffice 등) PATH 에 없음 | 사용자에게 이미 친화 toast. 채팅에 설치 명령 표시. 사용자가 설치 확인 전 재시도 말 것 |
| `DEPENDENCY_HUNG` | 시작됐지만 N 초간 출력 없음 | 진행 toast 표시. 중단 여부 사용자에게 |

### Q&A / 협업

| `kind` | 의미 | 복구 |
|---|---|---|
| `TIMED_OUT` | `agent_question_ask` deadline 경과 | 답 없음으로 처리. best-effort 또는 사용자 escalate |
| `UNKNOWN_AGENT` | `agent_message_post` 의 `to` 가 연결된 에이전트 미매치 | `agent_message_list` 로 확인. `to: "any"` fallback |

## DEPENDENCY_MISSING envelope

에러이자 UX 순간이라 특별 처리.

`error.message` 가 `DEPENDENCY_MISSING:` prefix + JSON:

```jsonc
{
  "dep_id": "ffmpeg",
  "dep_label": "FFmpeg",
  "purpose": "비디오 씬 감지",
  "install_via": "brew install ffmpeg",
  "brew_present": true
}
```

사용자가 HTMLook 에서 actionable toast 봄 — **지금 설치** / **명령어 복사** / **닫기**. 에이전트 역할: *왜* 필요했는지, *무엇이* 일어날지, ffmpeg 설치가 ~30 s 걸린다는 것 설명.

`brew_present: false` 면 toast 가 Homebrew 먼저 설치 (~3 분). 인내 — 설치 중 원 호출 재시도 말 것.

## 복구 패턴

### Idempotent retry

```python
for attempt in range(3):
    res = call_tool(...)
    if res.ok: break
    if res.kind == "RATE_LIMITED":
        sleep(0.15 * (attempt + 1))
        continue
    break  # 다른 에러는 재시도 의미 없음
```

### Cascade 인식 retry

`apply_edit` 가 `STALE_HASH` 로 실패하면 `active_file` 로 재 fetch + 재계획 — 같은 find/replace 맹목 재시도 말 것.

### 정중하게 포기

같은 작업 2회 실패 후 *사용자에게 surface*:

```
show_toast({
  message: "두 번 시도했지만 이 변경을 자동 적용할 수 없습니다.",
  level: "warning"
})
chatpanel_post({
  text: "…를 변경하려 했지만 파일이 바뀌었습니다. 직접 하시겠어요, 아니면 다른 접근?"
})
```

## 자기 실패 audit

`audit_log_query({ ok: false, agent: "claude", since: today_start })` 가 오늘의 도구 실패 반환. 주기적 self-review — 많은 실패 클러스터는 버그가 아니라 워크스페이스의 잘못된 멘탈 모델 신호.

## 버그 보고

`INTERNAL_ERROR` 만나면 사용자에게 `/tmp/htmlook-debug.log` 마지막 ~500 줄을 `kdk3606@deep-on.com` 으로 이메일 요청. pre-launch 단계라 repo private.

## 끝

[개요](AI-Overview-ko.md) · [도구 카탈로그](AI-Tool-Catalog-ko.md) · [Home](Home-ko.md) 로
