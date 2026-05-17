# Step 7 · Bundled Profiles (HyperFrames / Slidev + 6 altri)

<p align="center">
  <a href="README.md">English</a> | <a href="README.ko.md">한국어</a> | <a href="README.ja.md">日本語</a> | <a href="README.de.md">Deutsch</a> | <a href="README.fr.md">Français</a> | <a href="README.es.md">Español</a> | <a href="README.pt.md">Português</a> | <b>Italiano</b>
</p>

> La v1.0 porta 8 *Heavyweight Profiles* embeddati nell'app. Al primo
> avvio vengono auto-decompressi in `~/.htmlook/profiles/_bundled-*`.
> ~ 5 min (solo un giro — l'uso effettivo dipende dalla curva di
> apprendimento di ogni strumento).

Un Profile = strumento esterno + bundle Skill v0.3 + contenuto seed,
tutto in un pacchetto. Installazione con un clic dal New Workspace
Wizard (⌘⇧N) o da una card dell'Add wizard.

> I manifest dei profile (profile.json + SKILL.md + seed/) stanno nella
> root del campus in [`../profiles/`](../profiles/) — il builder di
> catalog.json li legge da lì. Questo step è il giro guidato attorno.

## 7.1 · Le 8 card profile

| Profile | Categoria | Output | Licenza dello strumento | Inizio |
|---------|-----------|--------|-------------------------|--------|
| HyperFrames | motion-graphics | mp4 (kinetic typography) | MIT | [`../profiles/hyperframes/`](../profiles/hyperframes/) |
| Slidev | presentation | HTML/PDF slides | MIT | [`../profiles/slidev/`](../profiles/slidev/) |
| Quarto | publishing | PDF/HTML/PPT/book | GPL-2.0 | [`../profiles/quarto/`](../profiles/quarto/) |
| D2 | diagram | SVG | MPL-2.0 | [`../profiles/d2/`](../profiles/d2/) |
| Astro Starlight | documentation | docs site | MIT | [`../profiles/astro-starlight/`](../profiles/astro-starlight/) |
| Marimo | notebook | reactive HTML | Apache-2.0 | [`../profiles/marimo/`](../profiles/marimo/) |
| Excalidraw | diagram | JSON/SVG/PNG | MIT | [`../profiles/excalidraw/`](../profiles/excalidraw/) |
| Manim | educational-animation | mp4 | BSD-3-Clause | [`../profiles/manim/`](../profiles/manim/) |

> **HTMLook non bundle gli strumenti in sé.** L'app fornisce le guide
> d'uso e l'integrazione con il Wizard. Ogni strumento esterno si
> installa a parte (le README di ciascun profile elencano le
> dipendenze).

## 7.2 · Sceglierne uno e partire

Prima volta? Vai sul leggero:

- **Slidev** — `npx slidev` per installare. Un file md → slide HTML.
- **D2** — installa un binario Go. txt → diagramma SVG.
- **Excalidraw** — nessuna installazione (HTMLook ha un viewer
  integrato).

I più pesanti:

- **HyperFrames** — Node + ffmpeg + Kokoro TTS (Python). Lo stesso
  strumento con cui sono fatti i video del campus.
- **Manim** — Python + LaTeX. Animazione matematica.
- **Quarto** — R / Python / Pandoc. Publishing accademico.

## 7.3 · Installare dall'Add wizard

1. ⌘⇧N (New Workspace Wizard) o *+* nella sidebar (Add wizard).
2. Scegli la card del profile che vuoi dal catalogo.
3. *Install* — la cartella seed viene copiata nella tua home.
4. *Open* — HTMLook apre quella cartella come workspace e gli Skill
   del profile finiscono nel catalogo ⌘K.

## 7.4 · Seed di dominio extra (opzionale)

Sopra agli 8 profile ci sono 75 seed di workspace in
[`../sample_workspaces/`](../sample_workspaces/) — tutti con prefix
così vedi al volo a quale profile appartengono:

- `hf-*/` (26 — HyperFrames, il lineup completo di persona usato per
  produrre i video del campus)
- `slidev-*/` (7) · `quarto-*/` (7) · `marimo-*/` (7) · `manim-*/` (7)
- `d2-*/` (7) · `excalidraw-*/` (7) · `astro-*/` (7)

`hf-claude/` e `hf-llama/` sono i riferimenti BYOM (Anthropic Claude
/ Llama locale). Gli altri 24 (`hf-corp-deck/`, `hf-teacher-quiz/`,
`hf-kid-coding/` …) sono scenari di dominio. Ogni seed porta il set
completo `index.html + hyperframes.json + brand.txt + prompts.txt +
AGENTS.md + meta.json + README.md`, così un agente AI può replicare
fedelmente il workflow con il BYOM dell'utente.

Catalogo completo: [`../catalog.json`](../catalog.json) — attualmente
**83 voci** (8 profile + 75 workspace seed). Il CI lo ricostruisce
da solo ([`../scripts/build-catalog.mjs`](../scripts/build-catalog.mjs)).

## ✅ Checkpoint Step 7

- Hai letto una delle 8 README di profile.
- (Opzionale) Hai installato uno strumento esterno → dall'Add wizard,
  installato il seed di quel profile.
- (Opzionale) Hai dato un'occhiata a un seed di `sample_workspaces/`
  vicino al tuo dominio.

Tutto? → [Step 8 · extend (scrivere il proprio Profile)](../08-extend/)

## Per approfondire

- Il `SKILL.md` in ogni cartella di profile — il manifest Skill v0.3
  che il profile registra.
- [`../08-extend/PRODUCTION.md`](../08-extend/PRODUCTION.md) — lo
  standard di produzione dei video del campus con HyperFrames (i
  17 + 26 video sono tutti fatti con questo strumento).
