# Apply-edit 왕복

> 파일 변경. 뷰어 재로드. 검증. Audit. 가장 많이 쓰이는 워크플로우.

## 패턴

```text
1. capture_selector(".cta")              ← before
2. apply_edit(path, find, replace)       ← 변경
3. (내부 이벤트로 뷰어 reload)
4. capture_selector(".cta")              ← after
5. capture_diff(before, after)           ← 검증
   ↳ audit_log 에 apply_edit 행 자동 기록
```

## apply_edit shape

```jsonc
{
  "tool": "htmlook_apply_edit",
  "args": {
    "path":    "/abs/path/to/file.html",   // 필수
    "find":    "Sign up free",
    "replace": "Start free trial"
  }
}
```

반환:

```jsonc
{
  "path":         "/abs/path/to/file.html",
  "applied":      true,
  "bytes_before": 8423,
  "bytes_after":  8426,
  "backup_path":  "/abs/path/to/.file.html.bak.20260517-031400"
}
```

성공한 편집마다 서버가 timestamped `.bak.<ts>` 를 원본 옆에 작성 — 필요 시 수동 롤백.

`find` 는 **정확히 한 번** 매치해야 함. 둘 이상 매치 시 평문 에러 형식:
`find string matched N places in /abs/path; expected exactly 1. Widen the context and retry.` find 좁히고 (주변 맥락 추가) 재시도. 참고: 이 에러들은 머신 판독 `kind` enum 없음 — 평문 prefix 로 매치.

`find` 부재 시: `find string not found in /abs/path. Widen the context…`.

Path 안전: 파일이 활성 워크스페이스 root 안으로 resolve 되어야. 바깥은 `refused: <p> is outside the current workspace. Open the file in HTMLook Pro first…` 로 거부.

## insert_at_selection

사용자 현재 선택 위치에 삽입:

```jsonc
{
  "tool": "htmlook_insert_at_selection",
  "args": { "html": "<p>2026-05-17 업데이트.</p>" }
}
```

단일 인자 `html` (string). 활성 뷰어 pane 에 선택이 존재해야.

## create_file

```jsonc
{
  "tool": "htmlook_create_file",
  "args": {
    "path":    "drafts/q3-plan.md",
    "content": "# Q3 plan\n\n…",
    "open":    true,         // 옵션: 새 파일을 탭으로 열기
    "position": "after"      // 옵션: 새 탭 위치
  }
}
```

`create_file` 은 `apply_edit` 처럼 워크스페이스 `path_guard` 제약 안 받음 — 절대 또는 워크스페이스-상대 경로 전달. 워크스페이스 안 유지는 caller 책임.

## find 가 신뢰 어려울 때

속성 · 공백 · 생성 ID 가 있는 HTML 에선:

1. `select_element({ selector })` + `replace_in_active({ … })`
2. `select_text_range({ start, end })` + `insert_at_selection({ html })`
3. 최후 수단: `selection_html` 가져와 mutate 후 `replace_in_active` 로 쓰기

## Audit log

성공한 모든 `apply_edit` 가 `<workspace>/.htmlook/audit-log.jsonl` 에 append. 각 라인: `{ tool, args, ts }`. 조회:

```jsonc
{
  "tool": "htmlook_audit_log_query",
  "args": {
    "tool":     "htmlook_apply_edit",   // 옵션 필터
    "since_ts": 1715900000000,           // 옵션 UNIX-ms 하한
    "limit":    50
  }
}
```

서버는 `tool` · `since_ts` · `limit` 만 필터 — `agent` · ok/error 분리 없음. per-entry 반환 형태는 `{ tool, args, ts }`.

다른 에이전트와 워크스페이스 공유 시 ([다중 에이전트 협업](AI-Collaboration-ko.md)) 편집 재적용 전 조회 — race 가능성.

## 실패 모드 (평문 prefix, `data.kind` 아님)

| 에러에 보일 prefix | 의미 | 복구 |
|---|---|---|
| `find string matched N places…` | 모호한 find | find 문자열 넓히기 |
| `find string not found in…` | find 부재 | 렌더러로 파일 재읽기. `find_in_active` 먼저 |
| `refused: <p> is outside the current workspace…` | 경로 traversal | 워크스페이스 안 경로 사용 |
| `canonicalize <p>: No such file or directory` | 파일 부재 | `workspace_files` / `active_file` 확인 |
| `refused: HTMLook is in Free Viewer mode…` | 트라이얼 만료 | 사용자에게 surface; 우회 불가 |
| `rate-limited: <tool_name> burst exhausted. Retry after ~<ms> ms.` | 도구별 token bucket | 명시 ms back off |
| `DEPENDENCY_MISSING:{…}` | 외부 도구 부재 | 특별 — [에러 & 복구](AI-Errors-Recovery-ko.md) 참조 |

## 다음

- [다중 에이전트 협업 →](AI-Collaboration-ko.md)
- [에러 & 복구 →](AI-Errors-Recovery-ko.md)
