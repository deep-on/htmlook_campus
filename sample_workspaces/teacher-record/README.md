# teacher-record — HTMLook + LLM for term-end student summaries

A 15-second polished "학생 관찰 기록부" teaser that demonstrates the
**term-end record-book** workflow: keep raw `daily-notes.md` on the
left pane and `student-records.md` on the right pane while asking
an LLM to group the notes by student name and draft a 3-4 sentence
term-end summary for each.

The fictional school is **햇살초등학교 (Sunny Elementary)**, Class
3-1, Term 1, 2026, teacher 김민지. The teaser preview shows the
finished record book.

## What you get

- `index.html` — the 15-s "학생 관찰 기록부" teaser. Notebook beige
  + ink-slate + 형광 노랑 highlight palette. Four scenes: class
  roll with three highlighted students, raw daily-note pad,
  auto-grouped 3-column view, and the bound record book with the
  "학기말 종합 의견 · 2026 1학기" watermark.
- `prompts.txt` — five English LLM prompts: "group + draft", "fill
  the quiet student", plus three follow-ups.
- `brand.txt` — class-3-1 palette + voice guardrails.
- `hyperframes.json`, `meta.json` — HyperFrames scaffold.

## The workflow it shows

You are an elementary homeroom teacher writing the term-end record
book the week before report cards. You have a year of one-line
daily notes, but they are interleaved by date, not by student.
Without HTMLook you'd be cmd-F'ing every name three times. With
HTMLook:

1. Open the workspace. **Left pane = `daily-notes.md`** (raw,
   chronological, one note per line). **Right pane =
   `student-records.md`** (empty record book). Sidebar shows both.
2. Ask the LLM in the bottom terminal: *"Group these notes by
   student name and draft a 3-4 sentence term-end summary for each."*
   The LLM cites every note tagged 민준 / 서윤 / 지후 and
   `apply_edit`s a row per student in the record book.
3. Pause. Pick a quiet student (서윤). Ask the LLM to **pull only
   her notes and refine her row**. Right pane reloads with four
   highlighted sentences and a single one-line recommendation
   ("발표 기회를 짧게라도 정기적으로").

## Try it

Open this folder as a workspace in **HTMLook Pro**. Replace
`daily-notes.md` with your own term notes, attach the HTMLook MCP
to your LLM, and copy `[1]` from `prompts.txt`.

The LLM will:

1. `htmlook_pane_pair` → notes (left) + record book (right).
2. `htmlook_active_file` → know which side it's writing into.
3. `htmlook_cite("left", "민준 ×3, 서윤 ×3, 지후 ×2")` to anchor
   the per-student buckets.
4. `htmlook_apply_edit` to land one row per student, then a second
   pass to deepen one student's row with cited evidence.
5. Hot-reload — right pane re-renders the patched record book.

## Why this matters

Term-end record books are the slowest piece of teacher prep,
because the input is interleaved (one note per kid, scattered
across 16 weeks) and the output is grouped (one paragraph per kid,
rendered in the same voice). HTMLook keeps the raw notes on
screen so the LLM only writes from evidence it can cite.

## Why HTMLook

Same four moves as `dev-pr-docs`, `teacher-quiz`, and
`teacher-newsletter` (dual-pane MCP, `cite`, `apply_edit`,
auto-reload) — except the right pane is now a printable record
book, and the artifact is the 학기말 종합 의견 page that lands
inside the report card. **Same primitives, new craft.**
