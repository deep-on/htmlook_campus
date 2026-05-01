# hf-llama — HTMLook + HyperFrames + Local Ollama Llama (BYOL)

A 15-second polished product-launch teaser, generated end-to-end by a
**local Llama 3.2** running on your own machine. Same workflow as
`hf-claude` — only the LLM swapped. The point: **HTMLook's MCP
abstracts the LLM**, so your stack is the part you choose.

## What you get

- `index.html` — the completed 15 s teaser ("Vault Local AI", amber+coral, padlock outro). Open it in HTMLook to see the full result.
- `prompts.txt` — five Korean + five English prompts to feed Llama, from the basic ask to refinement variants.
- `brand.txt` — the fictional Vault Local AI palette + copy guardrails.
- `hyperframes.json`, `meta.json` — HyperFrames scaffold.

## Setup (one-time)

```bash
# 1. Install Ollama
brew install ollama

# 2. Pull Llama 3.2 (≈2 GB)
ollama pull llama3.2

# 3. Start Ollama (background)
ollama serve &

# 4. Verify
ollama list   # should show llama3.2
```

## Try it

Open this folder as a workspace in **HTMLook Pro**. The sidebar
should show a HyperFrames banner with one composition. Then in the
bottom terminal:

```bash
ollama run llama3.2
>>> [paste the [1] prompt from prompts.txt]
```

With the HTMLook MCP attached, Llama will:

1. Call `htmlook_pane_pair` → see your dual-pane state (left=html, right=video placeholder)
2. Call `htmlook_active_file` → identify the empty `index.html` to fill
3. Call `htmlook_apply_edit` 3–4 times to insert each scene
4. Wait for `npx hyperframes preview` hot-reload to land each version on the right pane
5. Run `npx hyperframes lint && npx hyperframes render` for the final mp4

When the render lands in `renders/index.mp4`, the HTMLook sidebar
banner flips from `watching…` to `rendered 1/1` and the right pane
**auto-reloads** to play the v1 result.

## Refinement loop (this is where HTMLook earns its keep)

Pause the right pane, find a beat that's too short or too light. Use
`htmlook_cite` with a time range or a sentence id, then ask Llama:

```text
이 영상의 1.2~2.6 초 구간 (htmlook_cite) 을 보면 "Your AI" 글자
stagger 가 너무 빠르게 들어와. 0.045 → 0.09 로 늘려줘 — 5초 windows
는 그대로.
```

Llama re-edits, HF re-renders, the right pane reloads. **Same 4
HTMLook moves as in hf-claude:** dual-pane MCP, cite, apply_edit,
auto-reload.

## Why local?

- Code and prompts never leave your laptop — works for medical /
  legal / defense workflows where API egress is blocked.
- No token billing — generate as many variants as you like.
- Offline OK — works on a plane.

## Why HTMLook?

The local-LLM stack works *because HTMLook's MCP abstracts the LLM
away*. Run `hf-claude` and `hf-llama` side by side — you'll see
identical HTMLook moves regardless of the LLM brand. **HTMLook is
the LLM-agnostic hub. Bring your own.**

---

# 한국어

## 무엇이 들어있나

`hf-claude` 와 동일한 15 초 polish 결과물 — 단지 추론을 **로컬 Llama**
로. Vault Local AI 가상 SaaS 의 키네틱 타이포 티저 (검정 + amber→코럴
+ 자물쇠 outro). 핵심 메시지: **HTMLook MCP 는 LLM 을 가리는 어댑터**.
같은 워크플로우, LLM 만 바꿔 끼우면 됨 — BYOL.

## 시작하기

```bash
brew install ollama
ollama pull llama3.2
ollama serve &
```

이 폴더를 HTMLook Pro 워크스페이스로 열고, 터미널에서 `ollama run
llama3.2` 후 `prompts.txt` 의 [1] 프롬프트를 붙여넣으세요. HTMLook
MCP 가 듀얼뷰 / cite / apply_edit / auto-reload 4 가지를 그대로
처리합니다.

## 다듬기 (HTMLook 가 빛나는 지점)

우측 결과 영상에서 마음에 안 드는 구간을 일시정지 → `htmlook_cite`
로 정확히 인용 → Llama 에게 수정 요청 → `htmlook_apply_edit` →
사이드바 banner 가 `rendered 1/1` 로 자동 reload. **hf-claude 와
1:1 동일한 4 동작.**
