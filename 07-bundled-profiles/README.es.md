# Step 7 · Bundled Profiles (HyperFrames / Slidev + 6 más)

<p align="center">
  <a href="README.md">English</a> | <a href="README.ko.md">한국어</a> | <a href="README.ja.md">日本語</a> | <a href="README.de.md">Deutsch</a> | <a href="README.fr.md">Français</a> | <b>Español</b> | <a href="README.pt.md">Português</a> | <a href="README.it.md">Italiano</a>
</p>

> v1.0 trae 8 *Heavyweight Profiles* embebidos en la app. En el primer
> arranque se auto-descomprimen en `~/.htmlook/profiles/_bundled-*`.
> ~ 5 min (solo un tour — el uso real depende de la curva de cada
> herramienta).

Un Profile = herramienta externa + bundle de Skill v0.3 + contenido
seed, empaquetado todo junto. Instala con un clic desde el New
Workspace Wizard (⌘⇧N) o una tarjeta del Add wizard.

> Los manifests de profile (profile.json + SKILL.md + seed/) viven en
> la raíz del campus en [`../profiles/`](../profiles/) — el builder de
> catalog.json los lee directamente. Este paso es el tour guiado
> alrededor.

## 7.1 · Las 8 tarjetas de profile

| Profile | Categoría | Salida | Licencia de la herramienta | Empezar |
|---------|-----------|--------|---------------------------|---------|
| HyperFrames | motion-graphics | mp4 (kinetic typography) | MIT | [`../profiles/hyperframes/`](../profiles/hyperframes/) |
| Slidev | presentation | HTML/PDF slides | MIT | [`../profiles/slidev/`](../profiles/slidev/) |
| Quarto | publishing | PDF/HTML/PPT/book | GPL-2.0 | [`../profiles/quarto/`](../profiles/quarto/) |
| D2 | diagram | SVG | MPL-2.0 | [`../profiles/d2/`](../profiles/d2/) |
| Astro Starlight | documentation | docs site | MIT | [`../profiles/astro-starlight/`](../profiles/astro-starlight/) |
| Marimo | notebook | reactive HTML | Apache-2.0 | [`../profiles/marimo/`](../profiles/marimo/) |
| Excalidraw | diagram | JSON/SVG/PNG | MIT | [`../profiles/excalidraw/`](../profiles/excalidraw/) |
| Manim | educational-animation | mp4 | BSD-3-Clause | [`../profiles/manim/`](../profiles/manim/) |

> **HTMLook no embarca las herramientas en sí.** La app trae las guías
> de uso e integración con el Wizard. Cada herramienta externa se
> instala aparte (los README de cada profile listan las dependencias).

## 7.2 · Elige una y arranca

Si es tu primera vez, ve a lo ligero:

- **Slidev** — `npx slidev` para instalar. Un md → slides HTML.
- **D2** — instala un binario Go. txt → diagrama SVG.
- **Excalidraw** — sin instalación (HTMLook trae un viewer).

Las más pesadas:

- **HyperFrames** — Node + ffmpeg + Kokoro TTS (Python). La misma
  herramienta con la que se hicieron los vídeos del campus.
- **Manim** — Python + LaTeX. Animación matemática.
- **Quarto** — R / Python / Pandoc. Publicación académica.

## 7.3 · Instalar desde el Add wizard

1. ⌘⇧N (New Workspace Wizard) o *+* en la sidebar (Add wizard).
2. Elige la tarjeta de profile que quieras del catálogo.
3. *Install* — la carpeta seed se copia a tu home.
4. *Open* — HTMLook abre esa carpeta como workspace y los Skills del
   profile aterrizan en el catálogo ⌘K.

## 7.4 · Seeds extra de dominio (opcional)

Encima de los 8 profiles hay 75 seeds de workspace en
[`../sample_workspaces/`](../sample_workspaces/) — todos con prefijo
para ver de un vistazo a qué profile pertenecen:

- `hf-*/` (26 — HyperFrames, el lineup completo de personas usado para
  producir los vídeos del campus)
- `slidev-*/` (7) · `quarto-*/` (7) · `marimo-*/` (7) · `manim-*/` (7)
- `d2-*/` (7) · `excalidraw-*/` (7) · `astro-*/` (7)

`hf-claude/` y `hf-llama/` son las referencias BYOM (Anthropic Claude
/ Llama local). Las otras 24 (`hf-corp-deck/`, `hf-teacher-quiz/`,
`hf-kid-coding/` …) son escenarios de dominio. Cada seed trae el set
completo `index.html + hyperframes.json + brand.txt + prompts.txt +
AGENTS.md + meta.json + README.md`, para que un agente AI replique
fielmente el workflow con el BYOM del usuario.

Catálogo completo: [`../catalog.json`](../catalog.json) — actualmente
**83 entradas** (8 profile + 75 workspace seed). CI lo reconstruye
solo ([`../scripts/build-catalog.mjs`](../scripts/build-catalog.mjs)).

## ✅ Checkpoint Step 7

- Has leído uno de los 8 README de profile.
- (Opcional) Has instalado una herramienta externa → desde el Add
  wizard, instalado el seed de ese profile.
- (Opcional) Has ojeado un seed de `sample_workspaces/` cercano a tu
  dominio.

¿Todo? → [Step 8 · extend (escribir tu propio Profile)](../08-extend/)

## Más a fondo

- El `SKILL.md` en cada carpeta de profile — el manifest Skill v0.3
  que registra ese profile.
- [`../08-extend/PRODUCTION.md`](../08-extend/PRODUCTION.md) — el
  estándar de producción de vídeos del campus con HyperFrames (los
  17 + 26 vídeos están hechos con esta herramienta).
