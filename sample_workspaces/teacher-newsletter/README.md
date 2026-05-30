# teacher-newsletter — HTMLook + LLM for parent newsletters

A 15-second polished "가정통신문" teaser that demonstrates the
**elementary homeroom teacher** workflow: keep the district policy
PDF on the left pane and `newsletter.html` on the right pane while
asking an LLM to paraphrase formal language into a parent-friendly
note with a reply slip.

The fictional school is **햇살초등학교 (Sunny Elementary)**, Grade
3, Class 1, Spring term. The teaser preview shows the finished
parent note.

## What you get

- `index.html` — the 15-s "가정통신문" teaser. Cream + soft-blue
  palette on white paper. Four scenes: school crest header, three
  friendly bullets, ✓ / ✗ reply slip, date + 담임 signoff.
- `prompts.txt` — five English LLM prompts: "paraphrase the policy",
  "land the reply slip", plus three follow-ups.
- `brand.txt` — sunny-elem palette + copy guardrails.
- `hyperframes.json`, `meta.json` — HyperFrames scaffold.

## The workflow it shows

You are an elementary homeroom teacher writing the weekly parent
note. The district sent a stiff PDF that says "본 안내문이 도달한
날로부터 7일 이내에…" and parents skim past it. With HTMLook:

1. Open the workspace. **Left pane = `policy.pdf`** (formal memo
   from the district). **Right pane = `newsletter.html`** (empty
   draft). Sidebar shows both sources.
2. Ask the LLM in the bottom terminal: *"Read policy.pdf. Give me
   one headline plus three parent-friendly bullets. Keep the
   meaning. Drop the legal voice."* The LLM cites L1, L4, L9 and
   `apply_edit`s three warm bullets that say what parents need to
   do.
3. Pause. Ask the LLM to **add the meeting date and a reply slip**.
   Right pane reloads with bullet 2 highlighted with a date and a
   ✓ / ✗ slip with signature lines.

## Try it

Open this folder as a workspace in **HTMLook Pro**. Drop your
district memo at `policy.pdf`, attach the HTMLook MCP to your LLM,
and copy `[1]` from `prompts.txt`.

The LLM will:

1. `htmlook_pane_pair` → policy (left) + newsletter (right).
2. `htmlook_active_file` → know which side it's writing into.
3. `htmlook_cite("left", "L1, L4, L9")` to anchor the formal lines.
4. `htmlook_apply_edit` to land the three friendly bullets, then
   another pass for the date + reply slip.
5. Hot-reload — right pane re-renders the patched newsletter.

## Why this matters

A district memo is written for compliance, not for parents. Two
weeks of "send-back rate too low" follow-ups would have been
prevented if the friendly version had landed in the same view as
the formal one. HTMLook keeps the source on screen, so the LLM
only paraphrases what it can cite.

## Why HTMLook

Same four moves as `dev-pr-docs` and `teacher-quiz` (dual-pane MCP,
`cite`, `apply_edit`, auto-reload) — except the right pane is now a
parent newsletter, and the artifact is a printable note plus a
reply slip. **Same primitives, new craft.**
