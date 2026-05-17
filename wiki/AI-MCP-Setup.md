# MCP Setup

> Connecting your client to the running HTMLook Pro instance.

## Transport

HTMLook Pro launches an MCP server on every start. Two transports are exposed:

- **stdio** — preferred for spawned-child clients (Claude Code, Codex). The client spawns `htmlook --mcp-server` and talks JSON-RPC over stdin/stdout.
- **TCP** — `127.0.0.1:<port>` (port logged on launch, e.g. `[mcp-bridge] listening on 127.0.0.1:51586`). For clients that prefer a long-lived socket. Port is loopback-only and changes per app start.

You don't need to start anything yourself — HTMLook keeps the server alive while the app is running.

## Claude Code

The HTMLook MCP server is auto-registered when you install Claude Code with `htmlook_install_claude_code_mcp` (built into the app, also a Settings → Tools button), or manually:

```jsonc
// ~/.claude/mcp.json  (or workspace .claude/mcp.json)
{
  "mcpServers": {
    "htmlook": {
      "command": "/Applications/HTMLook Pro.app/Contents/MacOS/htmlook",
      "args": ["--mcp-server"]
    }
  }
}
```

Restart Claude Code. All tools appear under the `htmlook__*` namespace.

## Codex

```jsonc
// codex's MCP config
{
  "mcpServers": {
    "htmlook": {
      "command": "/Applications/HTMLook Pro.app/Contents/MacOS/htmlook",
      "args": ["--mcp-server"]
    }
  }
}
```

Same shape as Claude Code; Codex follows the standard MCP spec.

## Gemini CLI

Gemini CLI uses the same MCP spec. Drop the above stanza into `~/.gemini/mcp.json`. The tool surface looks identical from inside Gemini.

## Generic OpenAI-compatible client

Any tool that speaks the MCP wire format works. For example, in **Continue** or your own host:

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

## Workspace-aware behaviour

Every tool runs against the workspace the user is currently focused on. If they switch windows, the tools follow. If they switch tabs, `htmlook_active_file` returns the new tab.

For deterministic agents you may want to pin a workspace — there is no per-call workspace override, so coordinate with the user (or call `htmlook_focus_tab` first).

## First call: the consent modal

The first call to a *workspace-mutating* tool (`apply_edit`, `create_file`, `replace_in_active`, `voice_record_start`, etc.) triggers HTMLook's 4-button consent modal in the user's window:

- **Yes, once** — allow this one call
- **Yes, this workspace**
- **Yes, all workspaces**
- **No**

Until the user clicks, the tool call awaits. Until the modal is dismissed, the JSON-RPC response is held. Plan your prompts so the user expects the modal — name what you're about to do *before* you call the tool.

## Rate limiting

A token-bucket limiter (8 burst, 8 / sec refill) is applied per tool. Bursting through a Visual-Capture loop is fine; pounding the same tool 60×/s gets rejected with a friendly error you should treat as "back off briefly".

## Audit log

Every call appends an entry to `<workspace>/.htmlook/audit-log.jsonl`. Each line: `{ ts, tool, args_summary, agent }`. Query it with `htmlook_audit_log_query` to inspect your own history.

## Versioning

Check the running server with `htmlook_ping` — it returns `{ version, build_id, started_at }`. Use this if your prompt logic is version-sensitive.

## Next

- [Tool catalog →](AI-Tool-Catalog.md)
- [Visual Capture →](AI-Visual-Capture.md)
