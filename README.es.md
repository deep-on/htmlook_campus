# HTMLook Campus

<p align="center">
  <a href="README.md">English</a> | <a href="README.ko.md">한국어</a> | <a href="README.ja.md">日本語</a> | <a href="README.de.md">Deutsch</a> | <a href="README.fr.md">Français</a> | <b>Español</b> | <a href="README.pt.md">Português</a> | <a href="README.it.md">Italiano</a>
</p>

> Un **tutorial de 8 pasos** para quienes empiezan con HTMLook Pro. Siguiendo
> los pasos uno a uno, en 30–40 minutos vas de instalación → primer archivo
> → BYOM → edición → comandos → save-as-skill → perfiles incluidos →
> escribir tu propio perfil.

Este repo sigue el **HTMLook Pro v1.0 release-candidate** (GA prevista para
mediados de 2026). La app de escritorio está en [htmlook.app](https://htmlook.app)
— 14 días de prueba gratuita. BYOM (Bring-Your-Own-Model) significa cero
margen sobre tokens — Claude · GPT · Gemini · DeepSeek · Mistral · Together ·
Groq · Cerebras · Ollama, llama al modelo que prefieras directamente con tu
propia clave.

## Ruta del tutorial

De arriba abajo. Cada paso se apoya en el anterior.

| Paso | Carpeta | Qué haces | Tiempo |
|---|---|---|---|
| 1 | [`01-getting-started/`](01-getting-started/) | instalación · primer arranque · drag-drop · abrir carpeta | 3 min |
| 2 | [`02-first-file/`](02-first-file/) | md / html / pdf / vídeo — 4 tipos, split view, outline | 5 min |
| 3 | [`03-byom-setup/`](03-byom-setup/) | elegir un proveedor y registrar la clave (u Ollama) | 5 min |
| 4 | [`04-editing/`](04-editing/) | element pick · region paint · sentence-id · cite anchor | 5 min |
| 5 | [`05-command/`](05-command/) | chat · terminal CLI · apply_edit · 26 walkthroughs de personas | 10 min |
| 6 | [`06-save-as-skill/`](06-save-as-skill/) | capturar un workflow → tarjeta de catálogo ⌘K | 5 min |
| 7 | [`07-bundled-profiles/`](07-bundled-profiles/) | HyperFrames · Slidev · Quarto · D2 · Astro Starlight · Marimo · Excalidraw · Manim | 5 min |
| 8 | [`08-extend/`](08-extend/) | escribir tu propio perfil + PR al catálogo | opcional |

> Si solo quieres un vistazo rápido, el mapeo paso → vídeo está en
> [`01-getting-started/LEARNING_PATH.md`](01-getting-started/LEARNING_PATH.md).
> Cada vídeo dura 30–70 segundos.

## Manual de referencia (Wiki)

El tutorial de 8 pasos te enseña el flujo *de principio a fin, una vez*. El
[`wiki/`](wiki/) es el **manual de referencia función por función** al que
recurres después: Sidebar · Pestañas · Visor · Editor Markdown · PDF · Reproductor
vídeo/audio · Terminal · Asistente de IA · Paint · Notas de voz · Skill ·
Export · Ajustes · atajos. Dos vías paralelas — una para usuarios humanos,
otra para asistentes de IA (MCP / esquemas).

| Vía | Entrada | Idiomas |
|---|---|---|
| Manual para personas | [`wiki/Home.md`](wiki/Home.md) · [Coreano](wiki/Home-ko.md) | EN / KO |
| Guía para asistentes IA | [`wiki/AI-Overview.md`](wiki/AI-Overview.md) · [Coreano](wiki/AI-Overview-ko.md) | EN / KO |

El tutorial lo recorres una vez; el wiki se queda al alcance de la mano
todos los días (ábrelo desde la app con *Help → Documentation*).

## Ediciones

- **HTMLook Pro** (v1.0) — para usuarios avanzados. Chat BYOM + terminal PTY
  integrado + adaptadores CLI (claude / codex / gemini) + puente MCP + canvas
  Paint + captura de región + selección de elemento + save-as-skill + 8 perfiles
  incluidos + 49 seeds.
- **HTMLook Easier** *(próximamente)* — edición de entrada, en proceso de
  redefinición.

## Paso 1 — Instalación + primer arranque

Empieza por [`01-getting-started/README.md`](01-getting-started/README.md).

Descarga el .dmg desde [htmlook.app](https://htmlook.app), arrástralo a
Aplicaciones y haz drag-and-drop con tu primer archivo.

## Paso 2 — Primer archivo (HTML / MD / PDF / vídeo)

[`02-first-file/README.md`](02-first-file/README.md). Navega por cuatro
tipos de archivo con split view + outline + miniaturas.

Vídeos: BASIC #3 #4 #6 + ADV multi-pane / thumbnail / outline. Los mp4 están
en [`videos/features/`](videos/features/).

## Paso 3 — Configurar BYOM (un solo proveedor)

[`03-byom-setup/README.md`](03-byom-setup/README.md). Para la guía de IA
completa: [`03-byom-setup/AI_GUIDE.md`](03-byom-setup/AI_GUIDE.md); un
ejemplo de configuración para cliente MCP externo en
[`03-byom-setup/.htmlook/mcp-config.example.json`](03-byom-setup/.htmlook/mcp-config.example.json).

## Paso 4 — Señalar *algo* en pantalla

[`04-editing/README.md`](04-editing/README.md). Cuatro modos: element pick ·
region paint · sentence-id · range select. Vídeo clave: BASIC #5 ⭐ region-cite
(el punto de entrada de la IA).

## Paso 5 — Modificar por comando (cite + apply_edit)

[`05-command/README.md`](05-command/README.md). La parte más profunda del
campus — 26 walkthroughs de personas en
[`05-command/personas/`](05-command/personas/) (agrupados por rol, cada
carpeta con WALKTHROUGH.md a seguir + before/after).

Catálogo de personas: [`05-command/personas/INDEX.md`](05-command/personas/INDEX.md).

## Paso 6 — Workflows habituales → Skills

[`06-save-as-skill/README.md`](06-save-as-skill/README.md). Panel de IA a la
derecha, diálogo *Save as Skill*. Tres líneas y listo.

## Paso 7 — Los 8 perfiles incluidos

[`07-bundled-profiles/README.md`](07-bundled-profiles/README.md). HyperFrames /
Slidev / Quarto / D2 / Astro Starlight / Marimo / Excalidraw / Manim. Los
seeds de perfil están en [`profiles/`](profiles/) (el builder catalog.json los
lee directamente).

## Paso 8 — Escribir tu propio perfil + estándar de vídeo

[`08-extend/README.md`](08-extend/README.md). Construye un perfil para tu
propio dominio y añádelo al catálogo. El estándar de vídeo + procedimiento
de reverse-verification: [`08-extend/PRODUCTION.md`](08-extend/PRODUCTION.md);
el catálogo de los 17 vídeos: [`08-extend/FEATURES.md`](08-extend/FEATURES.md).

## Ubicaciones de assets (referencia)

Junto a las carpetas de paso (01~08), la raíz del campus contiene estos
*directorios de assets compartidos* (catalog.json + la app los referencian
por ruta, por lo que no se mueven a carpetas de paso individuales):

| Carpeta | Contenido |
|---|---|
| [`videos/`](videos/) | 17 mp4 de funciones + 26 mp4 de personas (~340 MB total) |
| [`profiles/`](profiles/) | 8 seeds de perfil (`profile.json` + `SKILL.md` + `seed/`) |
| [`sample_workspaces/`](sample_workspaces/) | 75 seeds de dominio (`hf-*` 26 personas + 49 seeds de perfil) |
| [`catalog.json`](catalog.json) | 83 entradas (8 perfiles + 75 seeds de workspace) — recargado al vuelo por el Wizard de la app (caché 24 h) |
| [`scripts/`](scripts/) | `build-catalog.mjs` |
| [`infra/`](infra/) | worker de licencias (servicio aparte) |
| [`docs/`](docs/) | espacio de trabajo para artefactos generados (gitignored) |

## Dos capas de aprendizaje — vídeo + interactivo

Los vídeos del campus muestran el *qué (qué es posible)*. El walkthrough
interactivo incorporado en HTMLook Pro (*Help → Interactive Tutorials…*)
muestra el *cómo (cómo hacerlo)*. Cada una de las 17 funciones de los vídeos
tiene una guía interactiva equivalente, uno a uno.

| Capa | Dónde | Duración | Rol |
|---|---|---|---|
| Vídeo (campus) | `videos/features/`, `videos/` | 30 s / 60–70 s | muestra el resultado |
| Interactivo (app) | HTMLook Pro · Help → Interactive Tutorials… | 4 pasos | práctica en vivo |

## Promesa de reverse-verification

Cada vídeo de este campus **solo afirma cosas que HTMLook hace de
verdad**. Las funciones que no existen no se anuncian. Procedimiento de
verificación + lista de afirmaciones falsas corregidas:
[`08-extend/PRODUCTION.md`](08-extend/PRODUCTION.md).

## Estado

Este repo sigue el **HTMLook Pro v1.0 release-candidate** (GA prevista para
mediados de 2026) como material de aprendizaje vivo. Se hará público a la
vez que la v1.0 GA, momento en que el endpoint de catálogo
(`htmlook.app/catalog`) empezará a recargar al vuelo las URLs raw de este
repo (caché 24 h).

## Licencia

- Código / textos de walkthroughs: MIT
- Vídeos mp4: CC BY 4.0 (atribuir *"HTMLook Campus"*)
- Contenido de ejemplo (PDF / xlsx / md / html): CC0 / dominio público — todos placeholders ficticios
