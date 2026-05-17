# Step 4 · Editing (Paint / Region / Element Pick)

<p align="center">
  <a href="README.md">English</a> | <a href="README.ko.md">한국어</a> | <a href="README.ja.md">日本語</a> | <a href="README.de.md">Deutsch</a> | <a href="README.fr.md">Français</a> | <b>Español</b> | <a href="README.pt.md">Português</a> | <a href="README.it.md">Italiano</a>
</p>

> Cuatro formas de decir al LLM *qué zona de la pantalla* quieres.
> ~ 5 min.

La parte más distintiva de HTMLook. Cuando dices a la AI *"arregla
aquí"*, puedes señalar *aquí* directamente — como un pintor.

Al terminar este paso habrás recorrido el ciclo principal una vez tú
mismo: drag de region → cite anchor → prompt AI.

## 4.1 · Las cuatro formas de selección

| Método | Cómo | Para qué |
|---|---|---|
| **element pick** | clic en la preview | un solo nodo DOM (botón / titular / párrafo) |
| **range select** | drag en la preview | un rango de texto (frase / fragmento) |
| **region paint** ⭐ | ⌘Shift+R y luego drag de rectángulo | una zona visual (chart / área de ilustración) |
| **outline pick** | clic en el panel Outline a la derecha | una sección por encabezado |

Vídeo: [BASIC #6 · Pick what you see.](../videos/features/06-basic-06-html-4mode.mp4) (30 s)

## 4.2 · ⭐ Region cite — la pieza clave

El movimiento más importante del Step 4. Tu primer *lenguaje común* con
la AI.

1. Abre un HTML o PDF (p. ej. [`../05-command/personas/01-hf-claude/landing.html`](../05-command/personas/01-hf-claude/landing.html)).
2. ⌘Shift+R entra en modo region paint.
3. Traza un rectángulo sobre la preview → la zona se ilumina en acento
   magenta.
4. Un cite anchor se adjunta solo al panel AI a la derecha.
5. Dile a la AI *"arregla esto — el valor de Apex (edge compute) en
   una línea"*.

Si MCP está conectado, el LLM:
- saca un PNG de la zona vía `htmlook_region_current_png` (modelos
  vision),
- asegura el anchor de texto correspondiente con `htmlook_active_file`
  + `htmlook_cite`,
- aplica el parche con `htmlook_apply_edit`.

> Vídeo: [BASIC #5 ⭐ · Drag. Tell the LLM.](../videos/features/05-basic-05-region-cite.mp4)
> (30 s · el punto de entrada AI)

## 4.3 · Element pick

Hover sobre un elemento en la preview → contorno → clic → seleccionado.
⌘E conmuta el modo.

El outerHTML del elemento elegido lo lee el LLM vía
`htmlook_selection_html`, lo parchea y lo commitea con
`htmlook_apply_edit`.

## 4.4 · Sentence-id (a nivel frase en texto / vídeo largo)

Cita la frase #N directamente en un transcript o paper largo:

1. Abre un vídeo o una md larga.
2. Activa *Sentence Map* en el panel derecho → las frases reciben
   número N.
3. Clic → el cite anchor `sentence:5` se adjunta al panel AI.

> Vídeo: [ADV · Click sentence 5. Clip ships.](../videos/features/14-advanced-08-sentence-id.mp4)
> (30 s)

## 4.5 · Range select — solo drag

Lo más habitual. Drag de texto en la preview → `selection_text` y
`selection_html` ya están disponibles.

## ✅ Checkpoint Step 4

- Entraste en region paint con ⌘Shift+R y dibujaste un rectángulo.
- La región dibujada se enganchó como cite anchor al panel AI.
- Mandaste una frase a la AI y te llegó un patch (la respuesta lleva
  un cite anchor *en algún sitio*).

¿Los tres? → [Step 5 · command (terminal / chat / apply)](../05-command/)

## Más a fondo

- [`../03-byom-setup/AI_GUIDE.md`](../03-byom-setup/AI_GUIDE.md) — las
  herramientas MCP (selection / region / element / cite).
- [`../05-command/personas/`](../05-command/personas/) — 26 walkthroughs
  de persona (cada persona prefiere un patrón
  region/element/sentence-cite distinto).
