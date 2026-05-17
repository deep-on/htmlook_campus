# Step 4 · Editing (Paint / Region / Element Pick)

<p align="center">
  <a href="README.md">English</a> | <a href="README.ko.md">한국어</a> | <a href="README.ja.md">日本語</a> | <b>Deutsch</b> | <a href="README.fr.md">Français</a> | <a href="README.es.md">Español</a> | <a href="README.pt.md">Português</a> | <a href="README.it.md">Italiano</a>
</p>

> Vier Wege, dem LLM zu sagen, *welche Stelle auf dem Bildschirm* du
> meinst.
> ~ 5 min.

Der unverwechselbarste Teil von HTMLook. Wenn du der AI *"hier
ausbessern"* sagst, kannst du auf *hier* direkt zeigen — wie ein Maler.

Am Ende dieses Schritts hast du den Kernzyklus einmal selbst durchlaufen:
Region-Drag → cite anchor → AI-Prompt.

## 4.1 · Vier Auswahlmethoden auf einen Blick

| Methode | Einstieg | Wofür |
|---|---|---|
| **element pick** | Klick in der Preview | ein einzelner DOM-Knoten (Button / Heading / Absatz) |
| **range select** | Drag in der Preview | ein Textbereich (Satz / Phrase) |
| **region paint** ⭐ | ⌘Shift+R, dann Rechteck ziehen | eine visuelle Zone (Chart / Illustrationsbereich) |
| **outline pick** | Klick im rechten Outline-Panel | ein heading-skopierter Abschnitt |

Video: [BASIC #6 · Pick what you see.](../videos/features/06-basic-06-html-4mode.mp4) (30 s)

## 4.2 · ⭐ Region cite — der Dreh- und Angelpunkt

Die wichtigste Bewegung in Step 4. Deine erste *gemeinsame Sprache* mit
der AI.

1. Öffne eine HTML- oder PDF-Datei (z. B. [`../05-command/personas/01-hf-claude/landing.html`](../05-command/personas/01-hf-claude/landing.html)).
2. ⌘Shift+R schaltet in den Region-Paint-Modus.
3. Zieh ein Rechteck auf der Preview → die Fläche leuchtet in
   Magenta-Akzent.
4. Ein cite anchor heftet sich automatisch ans AI-Panel rechts.
5. Sag der AI *"hier ausbessern — Apex's Mehrwert (Edge Compute) in
   einer Zeile"*.

Wenn MCP verbunden ist, holt sich der LLM:
- per `htmlook_region_current_png` ein PNG der Region (Vision-Modelle),
- per `htmlook_active_file` + `htmlook_cite` den passenden Text-Anchor,
- per `htmlook_apply_edit` den Patch.

> Video: [BASIC #5 ⭐ · Drag. Tell the LLM.](../videos/features/05-basic-05-region-cite.mp4)
> (30 s · der AI-Einstiegspunkt)

## 4.3 · Element pick

In der Preview übers Element hovern → Umriss → Klick → ausgewählt.
⌘E schaltet den Modus.

Das outerHTML des gewählten Elements liest der LLM über
`htmlook_selection_html`, patcht, und committet via `htmlook_apply_edit`.

## 4.4 · Sentence-id (satzweise in langem Text / Video)

Satz #N direkt in einem langen Transcript oder Paper citen:

1. Ein Video oder eine lange md öffnen.
2. Im rechten Panel *Sentence Map* einschalten → Sätze bekommen
   N-Nummern.
3. Klick → cite anchor `sentence:5` heftet sich ans AI-Panel.

> Video: [ADV · Click sentence 5. Clip ships.](../videos/features/14-advanced-08-sentence-id.mp4)
> (30 s)

## 4.5 · Range select — einfach ziehen

Der häufigste Move. Text in der Preview ziehen → sowohl
`selection_text` als auch `selection_html` werden verfügbar.

## ✅ Step 4 Checkpoint

- Du hast Region-Paint mit ⌘Shift+R gestartet und ein Rechteck
  gezeichnet.
- Die gezeichnete Fläche hat sich als cite anchor ans AI-Panel
  geheftet.
- Du hast der AI einen Satz geschickt und einen Patch zurückbekommen
  (in der Antwort steckt *irgendwo* ein cite-Anchor).

Alle drei? → [Step 5 · command (terminal / chat / apply)](../05-command/)

## Weiterlesen

- [`../03-byom-setup/AI_GUIDE.md`](../03-byom-setup/AI_GUIDE.md) — die
  MCP-Tools (selection / region / element / cite).
- [`../05-command/personas/`](../05-command/personas/) — 26 Persona-
  Walkthroughs (jede Persona bevorzugt eine andere
  region/element/sentence-cite-Variante).
