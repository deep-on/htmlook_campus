# Step 2 · Primer archivo (HTML / Markdown / PDF / vídeo)

<p align="center">
  <a href="README.md">English</a> | <a href="README.ko.md">한국어</a> | <a href="README.ja.md">日本語</a> | <a href="README.de.md">Deutsch</a> | <a href="README.fr.md">Français</a> | <b>Español</b> | <a href="README.pt.md">Português</a> | <a href="README.it.md">Italiano</a>
</p>

> Aprende el corazón del *viewer* de HTMLook. La parte que ya tiene valor
> sin AI / MCP.
> ~ 5 min.

Al terminar este paso: sabes cómo leer cada uno de los cuatro tipos de
archivo (md / html / pdf / vídeo) y cómo navegarlos con split view,
preview y outline.

## 2.1 · Markdown — edición en vivo

1. Doble clic en cualquier `.md` de la sidebar (p. ej.
   [`../05-command/personas/03-dev-pr-docs/docs.md`](../05-command/personas/03-dev-pr-docs/docs.md)).
2. ⌘\\ o menú *View → Split* conmuta la split view.
3. Source a la izquierda, preview a la derecha. Tecleas a la izquierda y
   la derecha se refresca en vivo.

> Vídeo: [BASIC #3 · Type left. See right. Live.](../videos/features/03-basic-03-md-live-edit.mp4) (30 s)

## 2.2 · HTML — clic en un elemento para editarlo

1. Doble clic en un `.html` (p. ej.
   [`../05-command/personas/01-hf-claude/landing.html`](../05-command/personas/01-hf-claude/landing.html)).
2. Modo por defecto: preview. En split view, clic directo en un elemento
   → aparece un editor de texto.
3. Sync bidireccional — los cambios en preview llegan a source al instante.

> Vídeo: [BASIC #4 · Click anything. Edit it.](../videos/features/04-basic-04-html-split.mp4) (30 s)

## 2.3 · HTML — cuatro modos de selección

En el mismo archivo HTML, ⌘E rota entre los cuatro modos de selección:

| Modo | Lo que coge |
|---|---|
| element | un solo nodo DOM |
| range | un rango de texto |
| region | un rectángulo pintado |
| outline | el árbol de encabezados |

Vídeo: [BASIC #6 · Pick what you see.](../videos/features/06-basic-06-html-4mode.mp4) (30 s)

Lo que cada modo capta se convierte en el punto de entrada de cite-anchor
en [Step 4 · editing](../04-editing/).

## 2.4 · PDF — páginas + capa de texto

1. Doble clic en un `.pdf` (p. ej.
   [`../05-command/personas/05-domain-battery/vendor.pdf`](../05-command/personas/05-domain-battery/vendor.pdf)).
2. Navegador de miniaturas a la izquierda + canvas de página a la derecha
   + capa de texto seleccionable.
3. Drag-select sobre una región → region cite (se usa en Step 4).

## 2.5 · Vídeo — miniaturas de frame + outline

1. Doble clic en cualquier mp4 (p. ej.
   [`../videos/features/01-basic-01-drop-open.mp4`](../videos/features/01-basic-01-drop-open.mp4)).
2. El viewer de vídeo muestra una timeline con previsualizaciones en
   miniatura.
3. ⌘Shift+T o hover te da una preview de 1 s sobre el frame (sin
   scrubbing).

> Vídeo: [ADV · Frame check. No scrub.](../videos/features/15-advanced-09-thumbnail.mp4) (30 s, categoría advanced)

## 2.6 · Outline — navegar un documento largo

La estructura de encabezados de cualquier md / html / PDF largo →
pestaña Outline del panel derecho. Clic en un encabezado y saltas allí.

> Vídeo: [ADV · Click §3.2. You're there.](../videos/features/16-advanced-10-outline.mp4) (30 s)

## 2.7 · Split view / multi-pane (⌘1 / ⌘2 / ⌘3 / ⌘J)

| Atajo | Efecto |
|---|---|
| ⌘1 | Solo preview |
| ⌘2 | Solo source |
| ⌘3 | Split (preview + source) |
| ⌘J | Conmuta el panel terminal |

Vídeo: [ADV · Two keys. Three views.](../videos/features/10-advanced-04-multi-pane.mp4)
(30 s — el *"Two keys"* de la narración era ⌘D + ⌘J en el corte
original; se corrigió a ⌘1/⌘2/⌘3 + ⌘J para la v1.0. Lineaje completo
en [`../08-extend/PRODUCTION.md`](../08-extend/PRODUCTION.md), tabla
*fixed false claims*.)

## ✅ Checkpoint Step 2

- Has abierto una md / html / pdf / vídeo, cada una en split view.
- Has notado la diferencia entre los cuatro modos HTML (element / range /
  region / outline) haciendo clic directo.
- ⌘1 / ⌘2 / ⌘3 / ⌘J para conmutar el layout es ya reflejo.

¿Los tres? → [Step 3 · BYOM setup](../03-byom-setup/) — elige un
proveedor y registra una clave.
