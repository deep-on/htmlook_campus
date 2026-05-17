# Step 7 · Bundled Profiles (HyperFrames / Slidev + 6 weitere)

<p align="center">
  <a href="README.md">English</a> | <a href="README.ko.md">한국어</a> | <a href="README.ja.md">日本語</a> | <b>Deutsch</b> | <a href="README.fr.md">Français</a> | <a href="README.es.md">Español</a> | <a href="README.pt.md">Português</a> | <a href="README.it.md">Italiano</a>
</p>

> v1.0 liefert 8 *Heavyweight Profiles* mit der App aus. Beim ersten
> Start werden sie automatisch nach `~/.htmlook/profiles/_bundled-*`
> entpackt.
> ~ 5 min (nur als Rundgang — der echte Einsatz ist eine tool-spezifische
> Lernkurve).

Ein Profile = externes Tool + Skill-v0.3-Bundle + Seed-Content,
zusammen verpackt. Installation per Klick aus dem New-Workspace-Wizard
(⌘⇧N) oder einer Karte im Add-Wizard.

> Die Profile-Manifests selbst (profile.json + SKILL.md + seed/) liegen
> im Campus-Root [`../profiles/`](../profiles/) — der catalog.json-
> Builder liest direkt von dort. Dieser Schritt ist die geführte Tour
> drumherum.

## 7.1 · Die 8 Profile-Karten

| Profile | Kategorie | Output | Tool-Lizenz | Einstieg |
|---------|-----------|--------|-------------|---------|
| HyperFrames | motion-graphics | mp4 (kinetic typography) | MIT | [`../profiles/hyperframes/`](../profiles/hyperframes/) |
| Slidev | presentation | HTML/PDF slides | MIT | [`../profiles/slidev/`](../profiles/slidev/) |
| Quarto | publishing | PDF/HTML/PPT/book | GPL-2.0 | [`../profiles/quarto/`](../profiles/quarto/) |
| D2 | diagram | SVG | MPL-2.0 | [`../profiles/d2/`](../profiles/d2/) |
| Astro Starlight | documentation | docs site | MIT | [`../profiles/astro-starlight/`](../profiles/astro-starlight/) |
| Marimo | notebook | reactive HTML | Apache-2.0 | [`../profiles/marimo/`](../profiles/marimo/) |
| Excalidraw | diagram | JSON/SVG/PNG | MIT | [`../profiles/excalidraw/`](../profiles/excalidraw/) |
| Manim | educational-animation | mp4 | BSD-3-Clause | [`../profiles/manim/`](../profiles/manim/) |

> **HTMLook bundelt die Tools selbst nicht.** Es liefert
> Nutzungsanleitungen und die Wizard-Integration. Jedes externe Tool
> wird separat installiert (jede Profile-README listet die
> Dependencies).

## 7.2 · Eines aussuchen und loslegen

Beim ersten Mal nimm was Leichtes:

- **Slidev** — `npx slidev` zum Installieren. Eine md-Datei → HTML-Slides.
- **D2** — Go-Binary installieren. txt → SVG-Diagramm.
- **Excalidraw** — keine Installation nötig (HTMLook bringt einen
  Viewer mit).

Die schwereren:

- **HyperFrames** — Node + ffmpeg + Kokoro-TTS (Python). Genau das
  Werkzeug, mit dem die Campus-Videos gemacht wurden.
- **Manim** — Python + LaTeX. Mathematische Animation.
- **Quarto** — R / Python / Pandoc. Akademisches Publishing.

## 7.3 · Aus dem Add-Wizard installieren

1. ⌘⇧N (New-Workspace-Wizard) oder *+* in der Sidebar (Add-Wizard).
2. Im Katalog die gewünschte Profile-Karte wählen.
3. *Install* — der Seed-Ordner wird in dein Home kopiert.
4. *Open* — HTMLook öffnet den Ordner als Workspace und die Skills des
   Profile landen im ⌘K-Katalog.

## 7.4 · Zusätzliche Domain-Seeds (optional)

Zusätzlich zu den 8 Profiles gibt's 75 Workspace-Seeds in
[`../sample_workspaces/`](../sample_workspaces/) — jeder mit Präfix, so
dass auf einen Blick klar ist, zu welchem Profile er gehört:

- `hf-*/` (26 — HyperFrames, das volle Persona-Lineup für die
  Campus-Videos)
- `slidev-*/` (7) · `quarto-*/` (7) · `marimo-*/` (7) · `manim-*/` (7)
- `d2-*/` (7) · `excalidraw-*/` (7) · `astro-*/` (7)

`hf-claude/` und `hf-llama/` sind die BYOM-Referenzpfade (Anthropic
Claude / lokales Llama). Die anderen 24 (`hf-corp-deck/`,
`hf-teacher-quiz/`, `hf-kid-coding/` …) sind Domain-Szenarien. Jeder
Seed kommt mit dem vollen Set `index.html + hyperframes.json +
brand.txt + prompts.txt + AGENTS.md + meta.json + README.md`, sodass
ein AI-Agent den Workflow mit dem eigenen BYOM-Modell verlässlich
nachstellen kann.

Voller Katalog: [`../catalog.json`](../catalog.json) — aktuell **83
Einträge** (8 Profile + 75 Workspace-Seeds). CI baut ihn automatisch
([`../scripts/build-catalog.mjs`](../scripts/build-catalog.mjs)).

## ✅ Step 7 Checkpoint

- Du hast eine der 8 Profile-READMEs gelesen.
- (Optional) Du hast ein externes Tool installiert → mit dem
  Add-Wizard den Seed des Profile installiert.
- (Optional) Du hast in `sample_workspaces/` einen Seed nah an deiner
  Domain angeschaut.

Alles erledigt? → [Step 8 · extend (eigenes Profile schreiben)](../08-extend/)

## Weiterlesen

- Die `SKILL.md` in jedem Profile-Ordner — das Skill-v0.3-Manifest,
  das das Profile registriert.
- [`../08-extend/PRODUCTION.md`](../08-extend/PRODUCTION.md) — der
  Standard, mit dem die Campus-Videos via HyperFrames produziert
  werden (alle 17 + 26 mit diesem Tool).
