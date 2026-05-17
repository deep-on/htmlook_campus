# Step 5 · Command (Terminal / Chat / Apply)

<p align="center">
  <a href="README.md">English</a> | <a href="README.ko.md">한국어</a> | <a href="README.ja.md">日本語</a> | <a href="README.de.md">Deutsch</a> | <a href="README.fr.md">Français</a> | <a href="README.es.md">Español</a> | <a href="README.pt.md">Português</a> | <b>Italiano</b>
</p>

> Lo Step 4 ti ha insegnato a puntare *dove*. Questo step lo trasforma
> in *comandi*. Il ciclo cite + apply_edit.
> ~ 10 min.

La parte più profonda del campus — i 26 walkthrough per persona stanno
qui ([`personas/`](personas/)). All'inizio, segui solo quello del tuo
dominio.

## 5.1 · Quattro pattern di comando

| Pattern | Dove | Forma di input |
|---|---|---|
| **Chat (BYOM)** | Pannello AI a destra | linguaggio naturale + cite anchor allegato in automatico |
| **Terminale CLI** | Alterna con ⌘J, lancia `claude` / `codex` / `gemini` | prompt shell |
| **Client MCP esterno** | Claude Code / Cursor / Windsurf / Zed | la chat di quel client |
| **Inline cite link** | un `[B14](xlsx://q3.xlsx#B14)` nella risposta | clic → salta a quell'anchor |

## 5.2 · Il ciclo cite + apply_edit

```
[scegli un'area dallo Step 4]
   → il cite anchor si attacca al pannello AI
   → prompt in linguaggio naturale
   → l'LLM chiama htmlook_apply_edit
   → il file cambia
   → il file watcher ricarica da solo il pane destro
```

Quattro video di riferimento (30 s ciascuno):

| # | Video | Pattern |
|---|---|---|
| 7 | [Cite the cell. Get the narrative.](../videos/features/07-advanced-01-xlsx-cite.mp4) | cite di una cella xlsx |
| 8 | [14:14 → paragraph.](../videos/features/08-advanced-02-live-cue-cite.mp4) | cite di un timestamp video |
| 9 | [One cite. Three files.](../videos/features/09-advanced-03-multi-target.mp4) | un cite → patch in più file |
| 17 | [Cross-file anchors. Recorded.](../videos/features/17-advanced-11-cross-link.mp4) | sidecar `.htmlook/links.json` |

## 5.3 · Walkthrough per persona (26)

Un workflow *day-in-the-life* per ruolo / dominio. mp4 da 60–70 s +
sample workspace follow-along + `WALKTHROUGH.md` passo passo.

Catalogo completo: [`personas/INDEX.md`](personas/INDEX.md). L'ordine
consigliato è raggruppato per ruolo:

- **Dev**: [`personas/01-hf-claude/`](personas/01-hf-claude/) →
  [`02-hf-llama/`](personas/02-hf-llama/) →
  [`03-dev-pr-docs/`](personas/03-dev-pr-docs/)
- **Contenuti**: [`personas/04-creator-podcast/`](personas/04-creator-podcast/) →
  [`12-press-editor/`](personas/12-press-editor/) →
  [`15-picture-book/`](personas/15-picture-book/) →
  [`22-hobby-fiction/`](personas/22-hobby-fiction/)
- **Analisi**: [`personas/09-data-analyst/`](personas/09-data-analyst/) →
  [`11-finance-report/`](personas/11-finance-report/) →
  [`10-research-notes/`](personas/10-research-notes/) →
  [`06-economy-analyst/`](personas/06-economy-analyst/)
- **Legale / traduzione**: [`personas/08-legal-redline/`](personas/08-legal-redline/) →
  [`07-translator-book/`](personas/07-translator-book/) →
  [`05-domain-battery/`](personas/05-domain-battery/)
- **Educazione (insegnanti)**: [`personas/17-teacher-quiz/`](personas/17-teacher-quiz/) →
  [`18-teacher-newsletter/`](personas/18-teacher-newsletter/) →
  [`19-teacher-record/`](personas/19-teacher-record/)
- **Educazione (studenti)**: [`personas/20-student-notes/`](personas/20-student-notes/) →
  [`24-student-flashcard/`](personas/24-student-flashcard/) →
  [`23-homework-helper/`](personas/23-homework-helper/) →
  [`21-kid-coding/`](personas/21-kid-coding/) →
  [`14-kids-science-mag/`](personas/14-kids-science-mag/)
- **Business**: [`personas/16-corp-deck/`](personas/16-corp-deck/) →
  [`13-product-prd/`](personas/13-product-prd/)
- **Vita quotidiana**: [`personas/25-recipe-card/`](personas/25-recipe-card/) →
  [`26-mobile-news/`](personas/26-mobile-news/)

## 5.4 · Il pattern follow-along

In ogni cartella persona:

- `WALKTHROUGH.md` — passo passo (marker `[VIEW]` / `[AI]`)
- `before/` — stato prima dell'edit (confronto visivo)
- `after/` — stato dopo l'edit (così anche chi non ha AI vede il
  risultato)
- i file di contenuto del dominio (md / html / pdf / xlsx / svg / py /
  mp3, …)

## 5.5 · LLM-agnostico — swap di fornitore

Lo stesso workflow cite + apply_edit gira identico sui 9 fornitori.
Aggiungine un altro in [Step 3](../03-byom-setup/) e fai swap — stesso
risultato.

## ✅ Checkpoint Step 5

- Hai visto un video persona (60–70 s) vicino al tuo ruolo.
- Hai seguito gli step `[VIEW]` del relativo `WALKTHROUGH.md`.
- (Se hai AI pronto) hai eseguito gli step `[AI]` → il pane destro
  si è ricaricato.
- (Altrimenti) hai confrontato `before/` vs `after/` in split view.

Tutto? → [Step 6 · save-as-skill](../06-save-as-skill/) — registra un
workflow ricorrente nell'app in modo permanente.

## Per approfondire

- [`personas/INDEX.md`](personas/INDEX.md) — catalogo delle 26 persona
  + mapping video ↔ cartella.
- [`personas/README.md`](personas/README.md) — come usare i sample
  workspace.
- [`../03-byom-setup/AI_GUIDE.md`](../03-byom-setup/AI_GUIDE.md) — i
  ~22 strumenti MCP + la guida al tono di output degli agent AI.
