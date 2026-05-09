---
theme: default
title: Build Your First MCP Server (Workshop)
---

# Build Your First MCP Server

2-hour interactive workshop · 8 sections · live coding

[Setup checklist](https://workshop.example/setup)

---

## Agenda

| section | duration | activity |
|---------|----------|----------|
| 1. Why MCP | 10 min | concepts |
| 2. Setup | 15 min | hands-on |
| 3. First tool | 25 min | **live coding** |
| 4. Wiring to Claude | 20 min | hands-on |
| 5. Testing | 15 min | demo |
| 6. Production deploy | 15 min | walkthrough |
| 7. Q&A | 20 min | open |

---
layout: section
---

# Section 3 · First Tool

(25 min · live coding · checkpoint 4/8)

---

## Step 3a · install rmcp

```bash
cargo add rmcp tokio --features rmcp/server,rmcp/macros,rmcp/transport-io
```

<v-click>

✓ checkpoint — your `Cargo.toml` should now have `rmcp = "1.5"`.

</v-click>

---

## Step 3b · the echo tool

```rust {1-3|4-9|10-14|all}{lines:true}
use rmcp::{tool, tool_handler};
use serde_json::Value;

#[tool]
async fn echo(input: String) -> String {
    input
}

#[tokio::main]
async fn main() -> anyhow::Result<()> {
    rmcp::serve_stdio(echo_handler()).await?;
    Ok(())
}
```

---

## Step 3c · run + test

```bash
cargo run
# In another terminal:
mcp-inspector echo --message "hello"
# → "hello"
```

<v-click>

✓ checkpoint — if you see `"hello"` echoed back, you have a working MCP server.

</v-click>

---
layout: section
---

# Section 4 · Wiring to Claude

(20 min · follow-along)

---

## Add to ~/.claude.json

```json
{
  "mcpServers": {
    "echo-workshop": {
      "command": "cargo",
      "args": ["run", "--quiet", "--manifest-path", "<your-path>/Cargo.toml"]
    }
  }
}
```

Restart Claude Code · `claude mcp list` should show `echo-workshop`.

---
layout: center
---

# Break · 10 min

Re-join at the same link.
