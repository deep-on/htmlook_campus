# MCP 설정

> 클라이언트를 실행 중인 HTMLook Pro 인스턴스에 연결.

## 전송 방식

HTMLook Pro 가 매 시작마다 MCP 서버 launch. 두 transport 노출:

- **stdio** — spawned-child 클라이언트 (Claude Code · Codex) 에 권장. 클라이언트가 `htmlook --mcp-server` 를 spawn 하고 stdin/stdout 으로 JSON-RPC.
- **TCP** — `127.0.0.1:<port>` (launch 시 로그 출력, 예: `[mcp-bridge] listening on 127.0.0.1:51586`). 장수명 소켓 선호 클라이언트용. loopback only + 매 시작마다 포트 변경.

직접 시작할 필요 없음 — HTMLook 이 앱 실행 중 서버 유지.

## Claude Code

HTMLook MCP 서버는 `htmlook_install_claude_code_mcp` (앱 빌트인, Settings → Tools 버튼) 또는 수동으로 자동 등록:

```jsonc
// ~/.claude/mcp.json  (또는 워크스페이스 .claude/mcp.json)
{
  "mcpServers": {
    "htmlook": {
      "command": "/Applications/HTMLook Pro.app/Contents/MacOS/htmlook",
      "args": ["--mcp-server"]
    }
  }
}
```

Claude Code 재시작. 모든 도구가 `htmlook__*` 네임스페이스로.

## Codex

```jsonc
// codex 의 MCP config
{
  "mcpServers": {
    "htmlook": {
      "command": "/Applications/HTMLook Pro.app/Contents/MacOS/htmlook",
      "args": ["--mcp-server"]
    }
  }
}
```

Claude Code 와 동일 shape. Codex 는 표준 MCP spec 따름.

## Gemini CLI

Gemini CLI 도 동일 MCP spec. `~/.gemini/mcp.json` 에 위 stanza. Gemini 내부에서 도구 표면 동일.

## 일반 OpenAI-호환 클라이언트

MCP wire 포맷을 말하는 모든 도구. **Continue** 나 자체 호스트:

```python
from mcp.client import StdioServerParameters, stdio_client

params = StdioServerParameters(
    command="/Applications/HTMLook Pro.app/Contents/MacOS/htmlook",
    args=["--mcp-server"],
)

async with stdio_client(params) as session:
    tools = await session.list_tools()
    result = await session.call_tool("htmlook_active_file", {})
```

## 워크스페이스 인식

모든 도구가 사용자가 현재 포커스한 워크스페이스 기준 실행. 윈도우 전환 시 도구도 따라감. 탭 전환 시 `htmlook_active_file` 이 새 탭 반환.

결정론적 에이전트가 워크스페이스 pin 하려면 — per-call 워크스페이스 override 없으니 사용자와 조율 (또는 `htmlook_focus_tab` 먼저 호출).

## 첫 호출: 사용자가 보는 것

워크스페이스 변경 도구는 실행 전 세 가지 체크로 게이트됩니다:

1. **Free Viewer 라이선스 체크** — 트라이얼 만료 + 미업그레이드 시 편집 도구가 `refused: HTMLook is in Free Viewer mode (trial expired)…` 반환, 실행 안 됨.
2. **Path-guard 스코프 체크** — `apply_edit` 가 워크스페이스 root 바깥 경로 거부 (`refused: <p> is outside the current workspace…`). (참고: `create_file` 은 이걸 강제하지 않음 — caller 책임.)
3. **도구별 rate limit** — burst 8, 초당 8 refill token bucket, 도구별 키.

v1.0.9 의 MCP 쓰기 경로에 per-call "이번만 / 워크스페이스 / 모두 / 거부" 동의 모달은 없음. (다른 surface 에 동의 UI 가 있지만 v1.0.9 의 MCP 쓰기에는 적용 안 됨.) 도구가 그냥 실행된다고 가정하고 프롬프트 — 단 호출 *전에* 무엇을 할지 명시해서 사용자가 필요 시 interrupt 가능하도록.

## Rate limit

도구별 token-bucket (burst 8, 8/sec refill). Visual-Capture 루프 burst OK. 같은 도구 60×/s 두드리면 친화적 에러로 reject — "잠시 back off" 의미.

## Audit log

모든 호출이 `<workspace>/.htmlook/audit-log.jsonl` 에 append. 각 라인: `{ ts, tool, args_summary, agent }`. `htmlook_audit_log_query` 로 자기 히스토리 조회.

## 버전 체크

`htmlook_ping` 은 평문 `"pong"` 반환 — liveness 프로브로 유용하나 버전 없음. 빌드 버전 + 워크스페이스 경로는 `htmlook_workspace_info` 호출, 응답은 `{ app_version, launch_cwd, workspace_root }`.

## 다음

- [도구 카탈로그 →](AI-Tool-Catalog-ko.md)
- [Visual Capture →](AI-Visual-Capture-ko.md)
