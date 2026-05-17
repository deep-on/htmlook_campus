# Step 2 · Primo file (HTML / Markdown / PDF / video)

<p align="center">
  <a href="README.md">English</a> | <a href="README.ko.md">한국어</a> | <a href="README.ja.md">日本語</a> | <a href="README.de.md">Deutsch</a> | <a href="README.fr.md">Français</a> | <a href="README.es.md">Español</a> | <a href="README.pt.md">Português</a> | <b>Italiano</b>
</p>

> Impara il cuore del *viewer* di HTMLook. La parte che ha già valore
> senza AI / MCP.
> ~ 5 min.

Alla fine di questo step: sai leggere ciascuno dei quattro tipi di file
(md / html / pdf / video) e navigarli con split view, preview e outline.

## 2.1 · Markdown — modifica live

1. Doppio clic su un qualunque `.md` nella sidebar (es.
   [`../05-command/personas/03-dev-pr-docs/docs.md`](../05-command/personas/03-dev-pr-docs/docs.md)).
2. ⌘\\ o menu *View → Split* attiva la split view.
3. Source a sinistra, preview a destra. Tu scrivi a sinistra, la destra
   si aggiorna live.

> Video: [BASIC #3 · Type left. See right. Live.](../videos/features/03-basic-03-md-live-edit.mp4) (30 s)

## 2.2 · HTML — clic su un elemento per modificarlo

1. Doppio clic su un `.html` (es.
   [`../05-command/personas/01-hf-claude/landing.html`](../05-command/personas/01-hf-claude/landing.html)).
2. Modalità di default: preview. In split view, clic diretto su un
   elemento → compare un editor di testo.
3. Sync bidirezionale — le modifiche in preview atterrano in source
   all'istante.

> Video: [BASIC #4 · Click anything. Edit it.](../videos/features/04-basic-04-html-split.mp4) (30 s)

## 2.3 · HTML — quattro modalità di selezione

Nello stesso file HTML, ⌘E ruota tra le quattro modalità di selezione:

| Modalità | Cosa prende |
|---|---|
| element | un singolo nodo DOM |
| range | un intervallo di testo |
| region | un rettangolo dipinto |
| outline | l'albero degli heading |

Video: [BASIC #6 · Pick what you see.](../videos/features/06-basic-06-html-4mode.mp4) (30 s)

Ciò che ogni modalità cattura diventa il punto d'ingresso di cite-anchor
in [Step 4 · editing](../04-editing/).

## 2.4 · PDF — pagine + livello testo

1. Doppio clic su un qualunque `.pdf` (es.
   [`../05-command/personas/05-domain-battery/vendor.pdf`](../05-command/personas/05-domain-battery/vendor.pdf)).
2. Navigatore di miniature a sinistra + canvas della pagina a destra +
   livello testo selezionabile.
3. Drag-select su una regione → region cite (usato in Step 4).

## 2.5 · Video — miniature di frame + outline

1. Doppio clic su un qualunque mp4 (es.
   [`../videos/features/01-basic-01-drop-open.mp4`](../videos/features/01-basic-01-drop-open.mp4)).
2. Il viewer video mostra una timeline con anteprime in miniatura.
3. ⌘Shift+T o hover ti dà un'anteprima di 1 s sul frame (senza
   scrubbing).

> Video: [ADV · Frame check. No scrub.](../videos/features/15-advanced-09-thumbnail.mp4) (30 s, categoria advanced)

## 2.6 · Outline — navigare un documento lungo

La struttura degli heading di qualsiasi md / html / PDF lungo → tab
Outline nel pannello destro. Clic su un heading e salti lì.

> Video: [ADV · Click §3.2. You're there.](../videos/features/16-advanced-10-outline.mp4) (30 s)

## 2.7 · Split view / multi-pane (⌘1 / ⌘2 / ⌘3 / ⌘J)

| Scorciatoia | Effetto |
|---|---|
| ⌘1 | Solo preview |
| ⌘2 | Solo source |
| ⌘3 | Split (preview + source) |
| ⌘J | Alterna il pannello terminale |

Video: [ADV · Two keys. Three views.](../videos/features/10-advanced-04-multi-pane.mp4)
(30 s — il *"Two keys"* della narrazione era ⌘D + ⌘J nel taglio
originale ed è stato corretto in ⌘1/⌘2/⌘3 + ⌘J per la v1.0. Storia
completa in [`../08-extend/PRODUCTION.md`](../08-extend/PRODUCTION.md),
tabella *fixed false claims*.)

## ✅ Checkpoint Step 2

- Hai aperto una md / html / pdf / video, ciascuna in split view.
- Hai sentito la differenza tra le quattro modalità HTML (element /
  range / region / outline) cliccando direttamente.
- ⌘1 / ⌘2 / ⌘3 / ⌘J per alternare il layout è un riflesso.

Tutti e tre? → [Step 3 · BYOM setup](../03-byom-setup/) — scegli un
fornitore e registra una chiave.
