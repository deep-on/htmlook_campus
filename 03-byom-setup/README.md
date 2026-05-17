# Step 3 · BYOM Setup (pick one vendor)

<p align="center">
  <b>English</b> | <a href="README.ko.md">한국어</a> | <a href="README.ja.md">日本語</a> | <a href="README.de.md">Deutsch</a> | <a href="README.fr.md">Français</a> | <a href="README.es.md">Español</a> | <a href="README.pt.md">Português</a> | <a href="README.it.md">Italiano</a>
</p>

> Bring-Your-Own-Model — you register the vendor key yourself. Zero markup
> on tokens.
> ~ 5 min.

HTMLook doesn't bundle an LLM; it just ships *adapters*. v1.0 supports 9
vendors: Claude / GPT / Gemini / DeepSeek / Mistral / Together / Groq /
Cerebras / Ollama (local). In this step you **pick one** and confirm it
works — you'll swap later in [Step 5](../05-command/).

## 3.1 · Three entry paths

There are three ways to call an LLM from HTMLook. All three expose the
same MCP tools (`htmlook_*`):

| Path | Where | Best for |
|---|---|---|
| **Built-in BYOM chat** ⭐ | Settings → Models → add key, then the right-hand AI panel | Newcomers |
| **Built-in Terminal + CLI** | Toggle ⌘J, run `claude` / `codex` / `gemini` | CLI-comfortable users |
| **External MCP client** | Merge into Claude Code / Cursor / Windsurf / Zed's mcp.json | Already using another client |

Full usage guide + the list of MCP tools: [`AI_GUIDE.md`](AI_GUIDE.md).

## 3.2 · Recommended: built-in BYOM chat

1. Top-right gear in HTMLook → **Settings → Models** tab.
2. Pick one vendor → *Add Provider*:
   - Anthropic Claude (most stable), or
   - OpenAI GPT, or
   - Google Gemini (largest free tier).
3. Paste the API key → *Test* — look for a 200 OK.
4. *Save* — the right-hand AI panel turns on.

> Video: [ADV · Swap the LLM. Keep the workflow.](../videos/features/13-advanced-07-mcp-swap.mp4)
> (30 s · LLM-agnostic via MCP)

## 3.3 · Ollama (local, no key)

If you don't want to send a key to an external service:

1. Install Ollama from [ollama.com](https://ollama.com).
2. `ollama pull llama3.2` (or any model you like).
3. HTMLook Settings → Models → *Add Provider* → Ollama → host
   `http://localhost:11434` (default).

## 3.4 · Using an external MCP client

If you're already on Claude Code / Cursor / Windsurf / Zed, merge the
contents of [`./.htmlook/mcp-config.example.json`](./.htmlook/mcp-config.example.json)
into your client's mcp.json. The HTMLook MCP server exposes ~22 `htmlook_*`
tools (cite, apply_edit, selection, region_current_png, outline, link,
video_*, …).

## 3.5 · First hello

Once the AI panel is on, type into the chat:

> *Summarise the first file in the current workspace in one line.*

Confirm the LLM pulls workspace context via the `htmlook_active_file`
MCP tool before answering. If the answer is workspace-blind, hit
**Settings → AI → Connect** once more, or — if you're using an external
MCP client — re-check the mcp.json merge.

## 3.6 · Auto-reload — after the model responds

When `apply_edit` writes to a file, the file watcher catches it and the
right pane of split view reloads automatically.

> Video: [ADV · It just reloaded.](../videos/features/11-advanced-05-auto-reload.mp4)
> (30 s)

## ✅ Step 3 checkpoint

- One vendor (or Ollama) is registered under Settings → Models.
- You sent a hello in chat and got an answer.
- The answer was workspace-aware.

Hitting issues? See the *debugging* section of [`AI_GUIDE.md`](AI_GUIDE.md).

All three? → [Step 4 · editing (paint / region / element pick)](../04-editing/)

## Further reading

- [`AI_GUIDE.md`](AI_GUIDE.md) — the ~22 MCP tools + the persona
  follow-along pattern + AI agent output tone.
- [`./.htmlook/mcp-config.example.json`](./.htmlook/mcp-config.example.json)
  — sample config for an external MCP client.
