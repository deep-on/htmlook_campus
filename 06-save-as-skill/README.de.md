# Step 6 · Save-as-Skill (Workflow festhalten)

<p align="center">
  <a href="README.md">English</a> | <a href="README.ko.md">한국어</a> | <a href="README.ja.md">日本語</a> | <b>Deutsch</b> | <a href="README.fr.md">Français</a> | <a href="README.es.md">Español</a> | <a href="README.pt.md">Português</a> | <a href="README.it.md">Italiano</a>
</p>

> Den cite + apply_edit-Zyklus aus Step 5 — *die App merkt ihn sich*.
> Beim nächsten Mal ein Klick und er läuft wieder.
> ~ 5 min.

Am Ende dieses Schritts hast du ein eigenes Tool im Workspace
registriert; es taucht im *Tools*-Bereich der Sidebar (oder im ⌘K
Quick-Launcher · Add Wizard) auf.

## 6.1 · *Save as Skill* — Einstieg

Wenn deine letzte LLM-Runde / dein letzter apply_edit-Zyklus gut lief,
klick auf das *⋯* oben im AI-Panel rechts → **Save as Skill**.

Der Dialog will drei Zeilen:

| Feld | Beispiel |
|---|---|
| Name | *Tighten subtitle* |
| When to use | *wenn ein Subtitle zu kurz ist, auf eine Zeile ausdehnen* |
| Default prompt | *Den Subtitle in der aktuellen cite-Region auf Apex's Mehrwert (Edge Compute, schnelles Deployment) ausdehnen und apply_edit* |

> Video: [ADV · Add a tool. Three fields.](../videos/features/12-advanced-06-tool-wizard.mp4) (30 s)

## 6.2 · Wo es lebt

`.htmlook/skills/<name>.skill.json` (im Workspace, v0.3-Spec). Teil
den Workspace, und deine Kolleg:innen haben das Skill auch.

Damit du es überall (jeder Workspace) nutzt — **Settings → Skills →
Promote to global**.

## 6.3 · Aus dem Add Wizard aufrufen

⌘K oder *+* in der Sidebar → der Katalog plus deine eigenen Skills
erscheinen als Karten. Klick auf eine Karte → läuft automatisch mit
dem aktuellen Selection-Kontext.

## 6.4 · Skill-v0.3-Spec — was drin steckt

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

`needs` / `produces` sind MCP-Tool-Namen. Volle Spec im HTMLook-Haupt-
Repo unter `docs/skills/v0.3.md` (öffentlich ab v1.0 GA).

## 6.5 · Skill vs. Profile

- **Skill** = die Aufnahme einer *Handlung* (ein Prompt + Tool-Kombi).
  Workspace-lokal oder benutzerglobal.
- **Profile** = ein Bundle aus *Tools + Seed-Content + Skills*. v1.0
  liefert 8 davon mit ([Step 7](../07-bundled-profiles/)).

Wie du dein eigenes Profile schreibst, steht in
[Step 8 · extend](../08-extend/).

## ✅ Step 6 Checkpoint

- Du hast den *Save as Skill*-Dialog im rechten AI-Panel geöffnet.
- Du hast die drei Zeilen ausgefüllt und ein Skill gespeichert.
- Du siehst das Skill als Karte in ⌘K — Klick führt es erneut aus.

Alle drei? → [Step 7 · bundled profiles](../07-bundled-profiles/)

## Weiterlesen

- [`../05-command/personas/`](../05-command/personas/) — stell dir
  vor, wie jede Persona als Skill gespeichert aussähe. Das Muster
  fällt einem auf.
