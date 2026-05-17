# Step 6 · Save-as-Skill (capturar un workflow)

<p align="center">
  <a href="README.md">English</a> | <a href="README.ko.md">한국어</a> | <a href="README.ja.md">日本語</a> | <a href="README.de.md">Deutsch</a> | <a href="README.fr.md">Français</a> | <b>Español</b> | <a href="README.pt.md">Português</a> | <a href="README.it.md">Italiano</a>
</p>

> El ciclo cite + apply_edit que aprendiste en Step 5 — *la app lo
> recuerda*. La próxima vez, un clic lo vuelve a ejecutar.
> ~ 5 min.

Al terminar este paso tendrás una herramienta tuya registrada en el
workspace y visible en la sección *Tools* de la sidebar (o en el
lanzador ⌘K · Add wizard).

## 6.1 · *Save as Skill* — entrada

Si tu última conversación LLM / ciclo apply_edit fue bien, clic en el
*⋯* arriba del panel AI a la derecha → **Save as Skill**.

El diálogo pide tres líneas:

| Campo | Ejemplo |
|---|---|
| Name | *Tighten subtitle* |
| When to use | *cuando un subtítulo es demasiado corto, expandirlo a una línea* |
| Default prompt | *Expande el subtítulo de la región cite actual con el valor de Apex (edge compute, despliegue rápido) y apply_edit* |

> Vídeo: [ADV · Add a tool. Three fields.](../videos/features/12-advanced-06-tool-wizard.mp4) (30 s)

## 6.2 · Dónde vive

`.htmlook/skills/<name>.skill.json` (dentro del workspace, spec v0.3).
Si compartes el workspace, tus compañeros también lo tienen.

Para usarlo en cualquier workspace — **Settings → Skills → Promote to
global**.

## 6.3 · Llamarlo desde el Add wizard

⌘K o el *+* de la sidebar → el catálogo más tus skills aparecen como
tarjetas. Clic en una tarjeta → se ejecuta solo con el contexto de
selección actual.

## 6.4 · Spec Skill v0.3 — qué hay dentro

```json
{
  "name": "tighten-subtitle",
  "version": "0.3",
  "description": "...",
  "default_prompt": "...",
  "needs": ["selection_html", "active_file"],
  "produces": ["apply_edit"]
}
```

`needs` / `produces` son nombres de herramientas MCP. Spec completa
en el repo principal de HTMLook en `docs/skills/v0.3.md` (público en
v1.0 GA).

## 6.5 · Skill vs Profile

- **Skill** = captura de una *acción* (un prompt + combinación de
  herramientas). Local al workspace o user-global.
- **Profile** = bundle de *herramientas + contenido seed + Skills*.
  v1.0 trae 8 profiles ([Step 7](../07-bundled-profiles/)).

Cómo escribir tu propio Profile está en [Step 8 · extend](../08-extend/).

## ✅ Checkpoint Step 6

- Has abierto el diálogo *Save as Skill* en el panel AI a la derecha.
- Has rellenado las tres líneas y guardado un skill.
- El skill aparece como tarjeta en ⌘K — clic lo vuelve a ejecutar.

¿Los tres? → [Step 7 · bundled profiles](../07-bundled-profiles/)

## Más a fondo

- [`../05-command/personas/`](../05-command/personas/) — imagina cada
  persona guardada como skill. El patrón se ve enseguida.
