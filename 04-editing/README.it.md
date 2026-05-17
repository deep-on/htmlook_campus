# Step 4 · Editing (Paint / Region / Element Pick)

<p align="center">
  <a href="README.md">English</a> | <a href="README.ko.md">한국어</a> | <a href="README.ja.md">日本語</a> | <a href="README.de.md">Deutsch</a> | <a href="README.fr.md">Français</a> | <a href="README.es.md">Español</a> | <a href="README.pt.md">Português</a> | <b>Italiano</b>
</p>

> Quattro modi per dire all'LLM *quale zona dello schermo* intendi.
> ~ 5 min.

La parte più distintiva di HTMLook. Quando dici all'AI *"sistema
qui"*, puoi puntare a *qui* direttamente — come un pittore.

Alla fine di questo step avrai percorso il ciclo chiave una volta da
solo: drag di region → cite anchor → prompt AI.

## 4.1 · I quattro modi di selezione

| Metodo | Come | Per cosa |
|---|---|---|
| **element pick** | clic nella preview | un singolo nodo DOM (bottone / heading / paragrafo) |
| **range select** | drag nella preview | un intervallo di testo (frase / spezzone) |
| **region paint** ⭐ | ⌘Shift+R poi drag di un rettangolo | un'area visiva (chart / zona di illustrazione) |
| **outline pick** | clic nel pannello Outline a destra | una sezione centrata su un heading |

Video: [BASIC #6 · Pick what you see.](../videos/features/06-basic-06-html-4mode.mp4) (30 s)

## 4.2 · ⭐ Region cite — il fulcro

La mossa più importante dello Step 4. La tua prima *lingua condivisa*
con l'AI.

1. Apri un HTML o un PDF (es. [`../05-command/personas/01-hf-claude/landing.html`](../05-command/personas/01-hf-claude/landing.html)).
2. ⌘Shift+R entra in modalità region paint.
3. Traccia un rettangolo sulla preview → la zona si illumina con
   accento magenta.
4. Un cite anchor si attacca da solo al pannello AI a destra.
5. Di' all'AI *"sistema qui — il valore di Apex (edge compute) in una
   riga"*.

Se MCP è collegato, l'LLM:
- recupera un PNG dell'area via `htmlook_region_current_png` (modelli
  vision),
- assicura l'anchor di testo corrispondente con `htmlook_active_file`
  + `htmlook_cite`,
- applica la patch con `htmlook_apply_edit`.

> Video: [BASIC #5 ⭐ · Drag. Tell the LLM.](../videos/features/05-basic-05-region-cite.mp4)
> (30 s · il punto di ingresso AI)

## 4.3 · Element pick

Hover su un elemento nella preview → contorno → clic → selezionato.
⌘E alterna la modalità.

L'outerHTML dell'elemento scelto viene letto dall'LLM via
`htmlook_selection_html`, patchato, e committato con
`htmlook_apply_edit`.

## 4.4 · Sentence-id (a livello frase in testi / video lunghi)

Cita la frase #N direttamente in un transcript o paper lungo:

1. Apri un video o un md lungo.
2. Attiva *Sentence Map* nel pannello destro → le frasi ricevono
   numero N.
3. Clic → il cite anchor `sentence:5` si attacca al pannello AI.

> Video: [ADV · Click sentence 5. Clip ships.](../videos/features/14-advanced-08-sentence-id.mp4)
> (30 s)

## 4.5 · Range select — basta un drag

Il più comune. Drag di testo nella preview → `selection_text` e
`selection_html` diventano entrambi disponibili.

## ✅ Checkpoint Step 4

- Sei entrato in region paint con ⌘Shift+R e hai disegnato un
  rettangolo.
- L'area disegnata si è attaccata come cite anchor al pannello AI.
- Hai mandato una frase all'AI e ti è tornata una patch (nella
  risposta c'è un cite anchor *da qualche parte*).

Tutti e tre? → [Step 5 · command (terminal / chat / apply)](../05-command/)

## Per approfondire

- [`../03-byom-setup/AI_GUIDE.md`](../03-byom-setup/AI_GUIDE.md) — gli
  strumenti MCP (selection / region / element / cite).
- [`../05-command/personas/`](../05-command/personas/) — 26 walkthrough
  per persona (ognuna predilige un pattern
  region/element/sentence-cite diverso).
