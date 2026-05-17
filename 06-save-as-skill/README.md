# Step 6 · Save-as-Skill (capture a workflow)

<p align="center">
  <b>English</b> | <a href="README.ko.md">한국어</a> | <a href="README.ja.md">日本語</a> | <a href="README.de.md">Deutsch</a> | <a href="README.fr.md">Français</a> | <a href="README.es.md">Español</a> | <a href="README.pt.md">Português</a> | <a href="README.it.md">Italiano</a>
</p>

> The cite + apply_edit cycle you learned in Step 5 — *the app
> remembers it*. Next time, one click re-runs it.
> ~ 5 min.

By the end of this step you'll have one tool of your own registered in
the workspace and showing up in the sidebar's *Tools* section (or in
the ⌘K quick launcher · Add wizard).

## 6.1 · *Save as Skill* — entry

When your last LLM exchange / apply_edit cycle went well, click the top
*⋯* of the right-hand AI panel → **Save as Skill**.

The dialog asks for three lines:

| Field | Example |
|---|---|
| Name | *Tighten subtitle* |
| When to use | *when a subtitle is too short, expand it to one line* |
| Default prompt | *Expand the subtitle in the current cite region to Apex's value (edge compute, fast deploy) and apply_edit* |

> Video: [ADV · Add a tool. Three fields.](../videos/features/12-advanced-06-tool-wizard.mp4) (30 s)

## 6.2 · Where it lives

`.htmlook/skills/<name>.skill.json` (inside the workspace, v0.3 spec).
Share the workspace and your teammates get the skill too.

To use it everywhere (every workspace) — **Settings → Skills → Promote
to global**.

## 6.3 · Calling it from the Add wizard

⌘K or the *+* button in the sidebar → the catalog plus your own skills
show up as cards. Click a card → it runs automatically using the
current selection context.

## 6.4 · Skill v0.3 spec — what's inside

```json
{
  "name": "tighten-subtitle",
  "version": "0.3",
  "description": "...",
  "default_prompt": "...",
  "needs": ["selection_html", "active_file"],
  "produces": ["apply_edit"]
}
```

`needs` / `produces` are MCP tool names. Full spec in the HTMLook main
repo at `docs/skills/v0.3.md` (published at v1.0 GA).

## 6.5 · Skill vs Profile

- **Skill** = a captured *action* (single prompt + tool combination).
  Workspace-local or user-global.
- **Profile** = a bundle of *tools + seed content + Skills* together.
  v1.0 ships 8 of these ([Step 7](../07-bundled-profiles/)).

How to write your own Profile is in [Step 8 · extend](../08-extend/).

## ✅ Step 6 checkpoint

- You opened the *Save as Skill* dialog on the right-hand AI panel.
- You filled the three lines and saved one skill.
- You can see the skill as a card in ⌘K and clicking it re-runs.

All three? → [Step 7 · bundled profiles](../07-bundled-profiles/)

## Further reading

- [`../05-command/personas/`](../05-command/personas/) — imagine each
  persona being saved as a skill. The pattern starts to click.
