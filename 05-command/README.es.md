# Step 5 · Command (Terminal / Chat / Apply)

<p align="center">
  <a href="README.md">English</a> | <a href="README.ko.md">한국어</a> | <a href="README.ja.md">日本語</a> | <a href="README.de.md">Deutsch</a> | <a href="README.fr.md">Français</a> | <b>Español</b> | <a href="README.pt.md">Português</a> | <a href="README.it.md">Italiano</a>
</p>

> El Step 4 te enseñó a señalar *dónde*. Este paso lo convierte en
> *comandos*. El ciclo cite + apply_edit.
> ~ 10 min.

La parte más profunda del campus — los 26 walkthroughs de personas
viven aquí ([`personas/`](personas/)). Al principio sigue solo el de
tu dominio.

## 5.1 · Cuatro patrones de comando

| Patrón | Dónde | Forma de entrada |
|---|---|---|
| **Chat (BYOM)** | Panel AI a la derecha | lenguaje natural + cite anchor adjuntado solo |
| **Terminal CLI** | Conmuta ⌘J, ejecuta `claude` / `codex` / `gemini` | prompt de shell |
| **Cliente MCP externo** | Claude Code / Cursor / Windsurf / Zed | el chat de ese cliente |
| **Inline cite link** | un `[B14](xlsx://q3.xlsx#B14)` en la respuesta | clic → salta a ese anchor |

## 5.2 · El ciclo cite + apply_edit

```
[elige una zona del Step 4]
   → el cite anchor se adjunta al panel AI
   → prompt en lenguaje natural
   → el LLM llama a htmlook_apply_edit
   → el archivo cambia
   → el file watcher recarga el pane derecho solo
```

Cuatro vídeos ancla (30 s cada uno):

| # | Vídeo | Patrón |
|---|---|---|
| 7 | [Cite the cell. Get the narrative.](../videos/features/07-advanced-01-xlsx-cite.mp4) | cite a celda xlsx |
| 8 | [14:14 → paragraph.](../videos/features/08-advanced-02-live-cue-cite.mp4) | cite a timestamp de vídeo |
| 9 | [One cite. Three files.](../videos/features/09-advanced-03-multi-target.mp4) | un cite → parches en varios archivos |
| 17 | [Cross-file anchors. Recorded.](../videos/features/17-advanced-11-cross-link.mp4) | sidecar `.htmlook/links.json` |

## 5.3 · Walkthroughs de persona (26)

Un workflow *day-in-the-life* por rol / dominio. mp4 de 60–70 s + un
sample workspace follow-along + un `WALKTHROUGH.md` paso a paso.

Catálogo completo: [`personas/INDEX.md`](personas/INDEX.md). El orden
recomendado está agrupado por rol:

- **Dev**: [`personas/01-hf-claude/`](personas/01-hf-claude/) →
  [`02-hf-llama/`](personas/02-hf-llama/) →
  [`03-dev-pr-docs/`](personas/03-dev-pr-docs/)
- **Contenido**: [`personas/04-creator-podcast/`](personas/04-creator-podcast/) →
  [`12-press-editor/`](personas/12-press-editor/) →
  [`15-picture-book/`](personas/15-picture-book/) →
  [`22-hobby-fiction/`](personas/22-hobby-fiction/)
- **Análisis**: [`personas/09-data-analyst/`](personas/09-data-analyst/) →
  [`11-finance-report/`](personas/11-finance-report/) →
  [`10-research-notes/`](personas/10-research-notes/) →
  [`06-economy-analyst/`](personas/06-economy-analyst/)
- **Legal / traducción**: [`personas/08-legal-redline/`](personas/08-legal-redline/) →
  [`07-translator-book/`](personas/07-translator-book/) →
  [`05-domain-battery/`](personas/05-domain-battery/)
- **Educación (profes)**: [`personas/17-teacher-quiz/`](personas/17-teacher-quiz/) →
  [`18-teacher-newsletter/`](personas/18-teacher-newsletter/) →
  [`19-teacher-record/`](personas/19-teacher-record/)
- **Educación (alumnos)**: [`personas/20-student-notes/`](personas/20-student-notes/) →
  [`24-student-flashcard/`](personas/24-student-flashcard/) →
  [`23-homework-helper/`](personas/23-homework-helper/) →
  [`21-kid-coding/`](personas/21-kid-coding/) →
  [`14-kids-science-mag/`](personas/14-kids-science-mag/)
- **Negocio**: [`personas/16-corp-deck/`](personas/16-corp-deck/) →
  [`13-product-prd/`](personas/13-product-prd/)
- **Diario**: [`personas/25-recipe-card/`](personas/25-recipe-card/) →
  [`26-mobile-news/`](personas/26-mobile-news/)

## 5.4 · El patrón follow-along

Dentro de cada carpeta de persona:

- `WALKTHROUGH.md` — paso a paso (marcas `[VIEW]` / `[AI]`)
- `before/` — estado antes del edit (comparación visual)
- `after/` — estado después del edit (para que usuarios sin AI vean el
  resultado igual)
- los archivos de contenido del dominio (md / html / pdf / xlsx / svg /
  py / mp3, …)

## 5.5 · LLM-agnóstico — swap de proveedor

El mismo workflow cite + apply_edit corre idéntico en los 9
proveedores. Añade otro en [Step 3](../03-byom-setup/) y haz swap —
mismo resultado.

## ✅ Checkpoint Step 5

- Has visto un vídeo de persona (60–70 s) cercano a tu rol.
- Has seguido los pasos `[VIEW]` del `WALKTHROUGH.md` de esa persona.
- (Con AI lista) Has corrido los pasos `[AI]` → el pane derecho se
  recargó.
- (Sin AI) Has comparado `before/` vs `after/` en split view.

¿Todo? → [Step 6 · save-as-skill](../06-save-as-skill/) — registra un
workflow recurrente en la app de forma permanente.

## Más a fondo

- [`personas/INDEX.md`](personas/INDEX.md) — catálogo de 26 personas +
  mapeo vídeo ↔ carpeta.
- [`personas/README.md`](personas/README.md) — cómo usar los sample
  workspaces.
- [`../03-byom-setup/AI_GUIDE.md`](../03-byom-setup/AI_GUIDE.md) — las
  ~22 herramientas MCP + la guía de tono de los agentes AI.
