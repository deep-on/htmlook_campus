# Pro vs Easier

> Two variants ship from the same repo. Pick the right one for who uses it.

| | **HTMLook Pro** | **HTMLook Easier** |
|---|---|---|
| **Bundle ID** | `com.deep-on.htmlook-pro` | `com.deep-on.htmlook` |
| **Target user** | Power user, developer, prosumer with own AI keys | Novice / non-technical reader |
| **AI** | BYOM (Bring Your Own Model) — your OpenAI / DeepSeek / Mistral / Together / Groq / Cerebras / Ollama / Custom keys | Built-in subscription AI |
| **Terminal** | Full xterm.js terminal with PTY, Claude/Codex/Gemini presets, MCP bridge — 123 tools | (none) |
| **MCP server** | `htmlook` MCP server exposed over stdio + 127.0.0.1:* — drive every part of the app from an external agent | (none) |
| **Paint** | ⌘⇧P sketch canvas, 7 tools, undo 50, PNG export → attach to chat | (none) |
| **Voice memos** | AAC recording, transcript sidecars, MCP-exposed | (none) |
| **Skills system** | Workspace + global SKILL.md frontmatter loader, Tier badges, auto-inject top-5 into ChatPanel system prompt | (none) |
| **Markdown editor** | Full WYSIWYG with autocorrect, ⌘K links, code-block language picker, paste sanitizer, print header/footer | Read-only render |
| **Export** | PDF, Print, DOCX, Markdown, Markdown (Smart), HTML, plus dynamic skill-driven formats (mp4, svg, …) | PDF, Print, HTML |
| **Auto-update** | tauri-plugin-updater + R2 manifest + ed25519 signature verify | Same plumbing, different update channel |
| **License** | Pro Solo $7/mo, 14-day free trial; perpetual + BYOM | Subscription (subsidises the built-in AI) |
| **Privacy** | Nothing leaves the device except the BYOM calls you make yourself | Subscription AI calls our backend |

## When to choose Pro

Pick Pro when you tick any of these:

- Already paying for an AI you want to use (Anthropic, OpenAI, Together, Ollama on a local box, …)
- Comfortable with a terminal; want Claude/Codex/Gemini sitting *inside* the app
- Need an agent to operate the app via MCP (capture a region, apply an edit, leave audit trail)
- Care that nothing about your files leaves the device by default
- You're a designer / writer / engineer / researcher / lawyer / PM who annotates a lot and wants Paint + voice memos baked in

## When Easier is the right call

- You don't want to think about API keys, monthly LLM bills, or which model
- You read way more than you write
- You want HTMLook to "just have AI" — and you'll pay a monthly subscription for the convenience
- You're recommending the app to a family member / coworker who doesn't enjoy tools menus

## The honest tradeoff

Pro is more powerful and more honest about cost — you see the LLM bill, you pick the model, the app stays out of your wallet. Easier is more inviting on day one and the AI quality is consistent across users — you don't have to evaluate eight providers to get a good answer.

Both are fed by the same renderer, file watcher, and Markdown engine. A workspace opens in either build with identical fidelity. So if you ever want to switch you just install the other DMG and point it at the same folder — sidecars travel.

## Single binary, two roles

The split exists for taxonomy clarity, not technical lock-in. The single repo (`deep-on/htmlook`) builds both via cargo features (`pro` flag) + Vite multi-entry (`src/apps/AppEasier.svelte` vs `src/apps/AppPro.svelte`). Shared engine code lives under `src/lib/`. CI greps the Easier bundle to make sure no Pro-only symbol leaks in.

## Next

- [Installation →](Installation.md)
- [Workspace →](Workspace.md)
- [For AI Agents · Overview →](AI-Overview.md)
