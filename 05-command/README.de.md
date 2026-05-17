# Step 5 · Command (Terminal / Chat / Apply)

<p align="center">
  <a href="README.md">English</a> | <a href="README.ko.md">한국어</a> | <a href="README.ja.md">日本語</a> | <b>Deutsch</b> | <a href="README.fr.md">Français</a> | <a href="README.es.md">Español</a> | <a href="README.pt.md">Português</a> | <a href="README.it.md">Italiano</a>
</p>

> Step 4 hat dir gezeigt, *wo* du zeigen sollst. Dieser Schritt macht
> daraus *Kommandos*. Der cite + apply_edit-Zyklus.
> ~ 10 min.

Der tiefste Teil des Campus — die 26 Persona-Walkthroughs leben hier
([`personas/`](personas/)). Am Anfang reicht es, dem aus deiner Domäne
zu folgen.

## 5.1 · Vier Kommando-Patterns

| Pattern | Wo | Eingabeform |
|---|---|---|
| **Chat (BYOM-Chat)** | AI-Panel rechts | natürliche Sprache + automatisch angeheftetem cite anchor |
| **Terminal-CLI** | ⌘J umschalten, `claude` / `codex` / `gemini` starten | Shell-Prompt |
| **Externer MCP-Client** | Claude Code / Cursor / Windsurf / Zed | das Chat-Feld dieses Clients |
| **Inline cite link** | ein `[B14](xlsx://q3.xlsx#B14)` in der Antwort | Klick → springt zu diesem Anchor |

## 5.2 · Der cite + apply_edit-Zyklus

```
[Bereich aus Step 4 markieren]
   → cite anchor heftet sich ans AI-Panel
   → natürlichsprachlicher Prompt
   → LLM ruft htmlook_apply_edit auf
   → Datei ändert sich
   → File-Watcher lädt das rechte Pane neu
```

Vier Anker-Videos (je 30 s):

| # | Video | Pattern |
|---|---|---|
| 7 | [Cite the cell. Get the narrative.](../videos/features/07-advanced-01-xlsx-cite.mp4) | xlsx-Zelle citen |
| 8 | [14:14 → paragraph.](../videos/features/08-advanced-02-live-cue-cite.mp4) | Video-Timestamp citen |
| 9 | [One cite. Three files.](../videos/features/09-advanced-03-multi-target.mp4) | ein Cite → Patches in mehreren Dateien |
| 17 | [Cross-file anchors. Recorded.](../videos/features/17-advanced-11-cross-link.mp4) | `.htmlook/links.json`-Sidecar |

## 5.3 · Persona-Walkthroughs (26)

Ein *Tag-im-Leben*-Workflow pro Rolle / Domäne. 60–70 s mp4 + ein
follow-along Sample-Workspace + eine schrittweise `WALKTHROUGH.md`.

Voller Katalog: [`personas/INDEX.md`](personas/INDEX.md). Die empfohlene
Reihenfolge ist nach Rolle gruppiert:

- **Dev**: [`personas/01-hf-claude/`](personas/01-hf-claude/) →
  [`02-hf-llama/`](personas/02-hf-llama/) →
  [`03-dev-pr-docs/`](personas/03-dev-pr-docs/)
- **Content**: [`personas/04-creator-podcast/`](personas/04-creator-podcast/) →
  [`12-press-editor/`](personas/12-press-editor/) →
  [`15-picture-book/`](personas/15-picture-book/) →
  [`22-hobby-fiction/`](personas/22-hobby-fiction/)
- **Analyse**: [`personas/09-data-analyst/`](personas/09-data-analyst/) →
  [`11-finance-report/`](personas/11-finance-report/) →
  [`10-research-notes/`](personas/10-research-notes/) →
  [`06-economy-analyst/`](personas/06-economy-analyst/)
- **Recht / Übersetzung**: [`personas/08-legal-redline/`](personas/08-legal-redline/) →
  [`07-translator-book/`](personas/07-translator-book/) →
  [`05-domain-battery/`](personas/05-domain-battery/)
- **Bildung (Lehrkräfte)**: [`personas/17-teacher-quiz/`](personas/17-teacher-quiz/) →
  [`18-teacher-newsletter/`](personas/18-teacher-newsletter/) →
  [`19-teacher-record/`](personas/19-teacher-record/)
- **Bildung (Lernende)**: [`personas/20-student-notes/`](personas/20-student-notes/) →
  [`24-student-flashcard/`](personas/24-student-flashcard/) →
  [`23-homework-helper/`](personas/23-homework-helper/) →
  [`21-kid-coding/`](personas/21-kid-coding/) →
  [`14-kids-science-mag/`](personas/14-kids-science-mag/)
- **Business**: [`personas/16-corp-deck/`](personas/16-corp-deck/) →
  [`13-product-prd/`](personas/13-product-prd/)
- **Alltag**: [`personas/25-recipe-card/`](personas/25-recipe-card/) →
  [`26-mobile-news/`](personas/26-mobile-news/)

## 5.4 · Das Follow-along-Pattern

In jedem Persona-Ordner:

- `WALKTHROUGH.md` — Schritt für Schritt (`[VIEW]` / `[AI]`-Marker)
- `before/` — Zustand vor dem Edit (für visuellen Vergleich)
- `after/` — Zustand nach dem Edit (damit auch Nutzer ohne AI das
  Ergebnis sehen)
- die Domain-Content-Dateien (md / html / pdf / xlsx / svg / py / mp3 …)

## 5.5 · LLM-agnostisch — Vendor-Swap

Derselbe cite + apply_edit-Workflow läuft auf allen 9 Vendors identisch.
Füg in [Step 3](../03-byom-setup/) einen anderen Vendor hinzu und swap
— gleiches Ergebnis.

## ✅ Step 5 Checkpoint

- Du hast ein Persona-Video (60–70 s) nahe deiner Rolle geschaut.
- Du bist den `[VIEW]`-Schritten in dessen `WALKTHROUGH.md` gefolgt.
- (Falls AI eingerichtet) Du hast die `[AI]`-Schritte ausgeführt → das
  rechte Pane hat sich neu geladen.
- (Falls nicht) Du hast `before/` und `after/` in Split-View verglichen.

Alle erledigt? → [Step 6 · save-as-skill](../06-save-as-skill/) — einen
wiederkehrenden Workflow dauerhaft in der App registrieren.

## Weiterlesen

- [`personas/INDEX.md`](personas/INDEX.md) — 26-Persona-Katalog + Video
  ↔ Ordner-Mapping.
- [`personas/README.md`](personas/README.md) — Verwendung der
  Sample-Workspaces.
- [`../03-byom-setup/AI_GUIDE.md`](../03-byom-setup/AI_GUIDE.md) — die
  ~22 MCP-Tools + Output-Ton-Guide der AI-Agenten.
