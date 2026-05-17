# ChatPanel · BYOM

> Bring Your Own Model. The right pane is a chat surface that calls *your* AI provider — never ours.

## Open and close

⌘L toggles the ChatPanel on the right side. First-launch you'll see the **FirstRunLLMSetup** wizard — a 5-card guided setup. After that ⌘L is just a panel toggle.

## Provider presets

HTMLook ships 8 OpenAI-compatible providers as one-click presets:

| Provider | Best for |
|---|---|
| OpenAI | Most capable, broad model lineup |
| DeepSeek | Cheap, fast, strong reasoning models |
| Mistral | EU-hosted, strong French + English |
| Together | Hosted open models with broad selection |
| Groq | Lowest-latency inference, Llama family |
| Cerebras | Very fast Llama / Qwen inference |
| Ollama | Local, no key needed |
| Custom | Any OpenAI-compatible URL |

You give it a base URL, key, and model name. The OpenAICompatibleAdapter handles streaming SSE, chunked tool-calls, and vendor-specific normalisation (DeepSeek's `reasoning_content`, Ollama's compact tool format).

## What lives in the panel

```
┌────────────────────────────┐
│  ⚙ AISettings  📜 history  │ ← top
├────────────────────────────┤
│  System prompt             │
│  · Skill chips (top-5)     │
├────────────────────────────┤
│  ▸ "summarize this doc"    │
│  ▸ tool: htmlook_outline   │
│  ▸ tool result …           │
│  ▸ assistant: …            │
├────────────────────────────┤
│  📎 attach   …input box…   │
│              ⏎  ⌘⏎ submit  │
└────────────────────────────┘
```

## Skills auto-injected

HTMLook's Skill loader picks the **top-5 relevant skills** for the current workspace + active file + recent history and injects their triggers into the system prompt. You see them as chips above the conversation. Click a chip to expand the skill body.

Skills live in `.claude/skills/` (workspace) and `~/.claude/skills/` (global). See [Skills](Skills.md).

## Tool dispatch + consent

When the assistant calls a tool (`htmlook_outline`, `htmlook_apply_edit`, etc.), the first call per tool per workspace shows the **4-button consent modal**:

- **Yes, once** — allow this one call
- **Yes, this workspace** — remember for this workspace
- **Yes, all workspaces** — global allow
- **No** — refuse

The decision lands in `permissions.json` (workspace) or the global key store. Revoke from *AISettings → Permissions*.

## Attachments

The 📎 button (or drag onto the input box) attaches:

- Image (`.png`, `.jpg`, …) → encoded as OpenAI vision content block
- PDF page (selected via the PDF viewer's *Send page to AI*) → as image
- Paint canvas snapshot (`⌘⇧P → 📎`) → as image
- Workspace file (text-like) → inline as a code block

The badge above the input shows the per-message attachment count.

## Chat history

Stored per workspace at `.htmlook/chat-history/<thread-id>.json`. The 📜 button opens the history drawer; pin a thread to keep it. Threads round-trip with markdown-friendly export.

## Cancel + retry

The streaming response can be cancelled with ⌘. (Command + period). The last user turn keeps a *Retry* affordance for one re-run.

## Privacy

Outbound only to the provider you configured. The system prompt + tool catalog + your message + relevant excerpts of the active file (if you reference it explicitly) form the call. HTMLook never proxies through any Deep-On server.

## Next

- [Skills →](Skills.md)
- [For AI Agents · MCP Setup →](AI-MCP-Setup.md)
