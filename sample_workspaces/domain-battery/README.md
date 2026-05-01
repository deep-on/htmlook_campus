# domain-battery — HTMLook + Battery Bench 2026 (LLM-agnostic)

A 15-second polished result-teaser for a fictional EV-battery
competitive benchmark, generated end-to-end inside HTMLook by a
**domain analyst** (persona P7). Same workflow scaffold as
`hf-claude` and `hf-llama` — the LLM brand is up to you. **Bring
your own LLM** (Claude, Llama, GPT, or any local runtime); the
HTMLook MCP keeps the dual-pane / cite / apply_edit / auto-reload
moves identical regardless.

## What you get

- `index.html` — the completed 15 s teaser ("Battery Bench 2026", deep-navy + lime + amber, kinetic numbers + bar chart + vendor silhouettes + wordmark outro). Open it in HTMLook to see the full result.
- `prompts.txt` — five English prompts to feed any LLM, from the basic ask to refinement variants.
- `brand.txt` — the fictional Battery Bench 2026 palette + copy guardrails.
- `hyperframes.json`, `meta.json` — HyperFrames scaffold.

## The persona — P7 Domain Analyst

You are an EV-battery analyst comparing cells and packs across
vendors (CATL, LG ES, Samsung SDI, Panasonic). Your usual deliverable
is a competitive-analysis report that reads like a boardroom brief:
three benchmark numbers, a small bar chart, vendor logos, one
clear narrative.

The pain: stitching numbers from PDF datasheets into a draft, then
asking the LLM "redo this row with the citation I just pulled." The
LLM never sees what you see — until HTMLook's dual pane and `cite`
hand it the exact PDF region + the exact draft section.

## Try it

Open this folder as a workspace in **HTMLook Pro**. The sidebar
should show a HyperFrames banner with one composition. Then in the
bottom terminal, pick any LLM:

```bash
# any of these works — HTMLook MCP is LLM-agnostic
claude --continue
ollama run llama3.2
codex
```

Paste the [1] prompt from `prompts.txt`. With the HTMLook MCP
attached, the LLM will:

1. Call `htmlook_pane_pair` → see the dual-pane state (left=html, right=video placeholder)
2. Call `htmlook_active_file` → identify the empty `index.html` to fill
3. Call `htmlook_apply_edit` 4 times to insert each scene (intro tag, kinetic numbers, bar-chart row, wordmark outro)
4. Wait for `npx hyperframes preview` hot-reload to land each version on the right pane
5. Run `npx hyperframes lint && npx hyperframes render` for the final mp4

When the render lands in `renders/index.mp4`, the HTMLook sidebar
banner flips from `watching…` to `rendered 1/1` and the right pane
auto-reloads to play the v1 result.

## Refinement loop (this is where HTMLook earns its keep)

Pause the right pane, find a beat that feels off — a benchmark
number that lands too quickly, a vendor silhouette that's too dim.
Use `htmlook_cite` with a time range, then ask the LLM:

```text
Look at the right pane around 0:06 — "320 Wh/kg" snaps in too
fast. Slow the digit stagger from 0.04 → 0.08, and hold the value
for 0.6 s longer. Same scene window.
```

The LLM re-edits, HF re-renders, the right pane reloads. **Same
four HTMLook moves regardless of which LLM you picked**: dual-pane
MCP, cite, apply_edit, auto-reload.

## The boardroom-brief loop (the wider scenario)

The 15 s teaser inside this workspace is the *fancy result*. The
60-second walkthrough in `demo/persona_units/domain-battery/` shows
the wider workflow that ends here: a markdown competitive-analysis
report on the left, vendor PDF datasheets on the right, the LLM
citing a specific table region, recomputing one row, and finally
shipping the polished teaser as the cover animation for the brief.

## Why HTMLook?

Domain reports break the moment the LLM hallucinates a number it
can't see. HTMLook fixes that by handing the LLM the exact region
of the exact PDF and the exact draft section — through `cite` and
`active_file`. The LLM brand is up to you; the MCP moves don't
change. Run any of `hf-claude` / `hf-llama` / `domain-battery`
side by side and you'll see identical HTMLook moves regardless of
which LLM is driving.

**HTMLook is the LLM-agnostic hub. Bring your own.**
