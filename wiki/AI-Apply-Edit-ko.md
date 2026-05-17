# Apply-edit 왕복

> 파일 변경. 뷰어 재로드. 검증. Audit. 가장 많이 쓰이는 워크플로우.

## 패턴

```text
1. capture_selector(".cta")              ← before
2. apply_edit(find, replace)             ← 변경
3. (htmlook:apply-edit-reload 이벤트로 뷰어 자동 reload)
4. capture_selector(".cta")              ← after
5. capture_diff(before, after)           ← 검증
   ↳ audit_log 에 apply_edit 행 자동 기록
```

자동 reload 는 백엔드가 `apply_edit` 성공 후 emit 하는 Tauri 이벤트. 프론트엔드가 listen → 파일 재읽기 → 활성 탭 `rawContent` 갱신. Race condition 없음.

## apply_edit shape

```jsonc
{
  "tool": "htmlook_apply_edit",
  "args": {
    "path": "/abs/path/to/file.html",   // optional; default = active file
    "find":     "Sign up free",
    "replace":  "Start free trial",
    "scope":    "active_file"            // active_file | selection | whole_file
  }
}
```

반환:

```jsonc
{
  "ok": true,
  "edits_applied": 1,
  "before_hash": "ab12…",
  "after_hash":  "cd34…",
  "diff_summary": "1 replacement, 14 → 17 chars"
}
```

find 문자열이 모호하면 (>5 매치) HTMLook 이 `MULTIPLE_MATCHES` 에러 + 카운트 반환. find 좁히거나 `scope: "selection"`.

## insert_at_selection

찾지 않고 *추가* 만 할 때:

```jsonc
{
  "tool": "htmlook_insert_at_selection",
  "args": {
    "text": "<p>2026-05-17 업데이트.</p>",
    "where": "after"   // before | after | replace
  }
}
```

뷰어에 활성 선택 또는 커서 위치 필요 (`htmlook_selection_text` 가 non-empty).

## create_file

```jsonc
{
  "tool": "htmlook_create_file",
  "args": {
    "path":    "drafts/q3-plan.md",
    "content": "# Q3 plan\n\n…"
  }
}
```

`path` 는 워크스페이스 root 기준. `path_guard` 가 바깥 traversal 거부.

## find 문자열이 신뢰 어려울 때

속성 · 공백 · 생성 ID 가 있는 HTML 에선:

1. `select_element({ selector })` + `replace_in_active({ text })`
2. `select_text_range({ start, end })` + `insert_at_selection`
3. 최후 수단: `selection_html` 가져와 mutate 후 `replace_in_active` 로 쓰기

## Audit log

모든 성공한 `apply_edit` 가 `<workspace>/.htmlook/audit-log.jsonl` 에 `{ ts, tool, path, find_len, replace_len, agent }` append. `audit_log_query({ since: "2026-05-17T00:00:00Z", tool: "htmlook_apply_edit" })` 로 조회.

다른 에이전트와 워크스페이스 공유 시 ([다중 에이전트 협업](AI-Collaboration-ko.md)) 편집 재적용 전 이거 확인 — race 가능성.

## 실패 모드

| 코드 | 의미 |
|---|---|
| `MULTIPLE_MATCHES` | `find` 가 >5× 발생. 좁힐 것 |
| `NO_MATCH` | `find` 부재 |
| `PATH_OUT_OF_SCOPE` | 대상 파일이 워크스페이스 root 바깥 |
| `PERMISSION_REFUSED` | 사용자가 동의 모달 "거부" |
| `RATE_LIMITED` | 토큰 버킷 소진. back off |
| `DEPENDENCY_MISSING` | 필요한 외부 도구 없음 (apply_edit 엔 드묾) |

응답 전략은 [에러 & 복구](AI-Errors-Recovery-ko.md) 참조.

## 다음

- [다중 에이전트 협업 →](AI-Collaboration-ko.md)
- [에러 & 복구 →](AI-Errors-Recovery-ko.md)
