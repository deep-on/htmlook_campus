# hf-claude — HTMLook + HyperFrames + Claude (BYOM)

A 15-second polished product-launch teaser, generated end-to-end by
**Anthropic Claude** through the HTMLook MCP. The reference
HyperFrames workflow — `hf-llama` is the same scenario with a local
Llama swapped in. The point: **HTMLook's MCP abstracts the LLM**, so
your stack is the part you choose.

## What you get

- `index.html` — the completed 15 s teaser ("Acme Cloud", cyan+pink, "A" wordmark + acmecloud.dev outro). Open it in HTMLook to see the full result.
- `prompts.txt` — five Korean + five English prompts to feed Claude, from the basic ask to refinement variants.
- `brand.txt` — the fictional Acme Cloud palette + copy guardrails.
- `hyperframes.json`, `meta.json` — HyperFrames scaffold.

## Setup (one-time)

```bash
# 1. Get an Anthropic API key
#    https://console.anthropic.com/ → API Keys → Create Key

# 2. Set it where Claude Code (or any Anthropic client) can read it
export ANTHROPIC_API_KEY=sk-ant-api03-…

# 3. Install Claude Code (or use Claude Desktop with MCP enabled)
npm i -g @anthropic-ai/claude-code

# 4. Verify
claude --version
```

## Try it

Open this folder as a workspace in **HTMLook Pro**. The sidebar
should show a HyperFrames banner with one composition. Then in the
bottom terminal:

```bash
claude
> [paste the [1] prompt from prompts.txt]
```

With the HTMLook MCP attached, Claude will:

1. Call `htmlook_pane_pair` → see your dual-pane state (left=html, right=video placeholder)
2. Call `htmlook_active_file` → identify the empty `index.html` to fill
3. Call `htmlook_apply_edit` 3–4 times to insert each scene
4. Wait for `npx hyperframes preview` hot-reload to land each version on the right pane
5. Run `npx hyperframes lint && npx hyperframes render` for the final mp4

When the render lands in `renders/index.mp4`, the HTMLook sidebar
banner flips from `watching…` to `rendered 1/1` and the right pane
**auto-reloads** to play the v1 result.

## Refinement loop (this is where HTMLook earns its keep)

Pause the right pane, find a beat that's too short or too soft. Use
`htmlook_cite` with a time range or a sentence id, then ask Claude:

```text
이 영상의 3.0~5.5 초 구간 (htmlook_cite) 을 보면 "ship faster"
글자 stagger 가 너무 빠르게 들어와. 0.045 → 0.09 로 늘리고 scale
pulse 1.04 → 1.08 로 강조 — 전체 5 초 windows 는 그대로.
```

Claude re-edits, HF re-renders, the right pane reloads. **Identical 4
HTMLook moves as in hf-llama:** dual-pane MCP, cite, apply_edit,
auto-reload.

## Why Claude here?

- Strong long-context reasoning — comfortable with 124-line
  compositions + brand guardrails + design tokens in one prompt.
- Tool-use via MCP is first-class; no glue code.
- Clean diffs on `apply_edit` — claude tends to surgical-edit rather
  than rewrite, which keeps the timeline stable scene-to-scene.

## Why HTMLook?

The Claude stack works *because HTMLook's MCP abstracts the LLM
away*. Run `hf-claude` and `hf-llama` side by side — you'll see
identical HTMLook moves regardless of the LLM brand. **HTMLook is
the LLM-agnostic hub. Bring your own.**

---

# 한국어

## 무엇이 들어있나

15 초짜리 polish 결과물 — **Anthropic Claude** 가 HTMLook MCP 를 통해
end-to-end 로 생성한 Acme Cloud 가상 SaaS 의 키네틱 타이포 티저
(near-black + cyan→pink + "A" 워드마크 + acmecloud.dev outro).
핵심 메시지: **HTMLook MCP 는 LLM 을 가리는 어댑터**. 같은 워크플로우,
LLM 만 바꿔 끼우면 됨 — BYOM.

## 시작하기

```bash
export ANTHROPIC_API_KEY=sk-ant-api03-…
npm i -g @anthropic-ai/claude-code
```

이 폴더를 HTMLook Pro 워크스페이스로 열고, 터미널에서 `claude` 후
`prompts.txt` 의 [1] 프롬프트를 붙여넣으세요. HTMLook MCP 가 듀얼뷰 /
cite / apply_edit / auto-reload 4 가지를 그대로 처리합니다.

## 다듬기 (HTMLook 가 빛나는 지점)

우측 결과 영상에서 마음에 안 드는 구간을 일시정지 → `htmlook_cite`
로 정확히 인용 → Claude 에게 수정 요청 → `htmlook_apply_edit` →
사이드바 banner 가 `rendered 1/1` 로 자동 reload. **hf-llama 와
1:1 동일한 4 동작.**
