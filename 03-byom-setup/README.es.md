# Step 3 · Setup BYOM (elige un proveedor)

<p align="center">
  <a href="README.md">English</a> | <a href="README.ko.md">한국어</a> | <a href="README.ja.md">日本語</a> | <a href="README.de.md">Deutsch</a> | <a href="README.fr.md">Français</a> | <b>Español</b> | <a href="README.pt.md">Português</a> | <a href="README.it.md">Italiano</a>
</p>

> Bring-Your-Own-Model — registras la clave del proveedor tú mismo.
> Margen cero sobre los tokens.
> ~ 5 min.

HTMLook no incluye un LLM; solo trae *adaptadores*. v1.0 soporta 9
proveedores: Claude / GPT / Gemini / DeepSeek / Mistral / Together /
Groq / Cerebras / Ollama (local). En este paso **eliges uno** y
compruebas que funciona — luego cambias en [Step 5](../05-command/).

## 3.1 · Tres vías de entrada

Tres formas de llamar a un LLM desde HTMLook. Las tres exponen las
mismas herramientas MCP (`htmlook_*`):

| Vía | Dónde | Para quién |
|---|---|---|
| **Chat BYOM integrado** ⭐ | Settings → Models → registra la clave, luego el panel AI a la derecha | Recién llegados |
| **Terminal + CLI integrados** | Conmuta con ⌘J, ejecuta `claude` / `codex` / `gemini` | Quien va cómodo en CLI |
| **Cliente MCP externo** | Fusiona en el mcp.json de Claude Code / Cursor / Windsurf / Zed | Ya usa otro cliente |

Guía completa + lista de herramientas MCP: [`AI_GUIDE.md`](AI_GUIDE.md).

## 3.2 · Recomendado: chat BYOM integrado

1. Rueda dentada arriba a la derecha de HTMLook → pestaña **Settings →
   Models**.
2. Elige un proveedor → *Add Provider*:
   - Anthropic Claude (lo más estable), o
   - OpenAI GPT, o
   - Google Gemini (free tier más grande).
3. Pega la clave API → *Test* — busca un 200 OK.
4. *Save* — el panel AI de la derecha se enciende.

> Vídeo: [ADV · Swap the LLM. Keep the workflow.](../videos/features/13-advanced-07-mcp-swap.mp4)
> (30 s · LLM-agnóstico vía MCP)

## 3.3 · Ollama (local, sin clave)

Si no quieres mandar una clave a un servicio externo:

1. Instala Ollama desde [ollama.com](https://ollama.com).
2. `ollama pull llama3.2` (o cualquier modelo).
3. HTMLook Settings → Models → *Add Provider* → Ollama → host
   `http://localhost:11434` (por defecto).

## 3.4 · Con un cliente MCP externo

Si ya estás en Claude Code / Cursor / Windsurf / Zed, fusiona el
contenido de [`./.htmlook/mcp-config.example.json`](./.htmlook/mcp-config.example.json)
en el mcp.json de tu cliente. El servidor MCP de HTMLook expone unas 22
herramientas `htmlook_*` (cite, apply_edit, selection,
region_current_png, outline, link, video_*, …).

## 3.5 · Primer hello

Cuando el panel AI esté activo, escribe en el chat:

> *Resume en una línea el primer archivo del workspace actual.*

Comprueba que el LLM trae el contexto del workspace vía la herramienta
MCP `htmlook_active_file` antes de responder. Si la respuesta no ve el
workspace, vuelve a pulsar **Settings → AI → Connect**, o — con un
cliente MCP externo — revisa otra vez el merge de mcp.json.

## 3.6 · Auto-reload — después de que el modelo responda

Cuando `apply_edit` escribe en un archivo, el file watcher lo detecta y
el pane derecho del split view recarga solo.

> Vídeo: [ADV · It just reloaded.](../videos/features/11-advanced-05-auto-reload.mp4)
> (30 s)

## ✅ Checkpoint Step 3

- La clave de un proveedor (u Ollama) está guardada en Settings →
  Models.
- Has mandado un hello en el chat y has recibido respuesta.
- La respuesta es consciente del contexto del workspace.

¿Problemas? Sección *debugging* en [`AI_GUIDE.md`](AI_GUIDE.md).

¿Los tres? → [Step 4 · editing (paint / region / element pick)](../04-editing/)

## Más a fondo

- [`AI_GUIDE.md`](AI_GUIDE.md) — las ~22 herramientas MCP + el patrón
  de follow-along de personas + el tono de salida del agente AI.
- [`./.htmlook/mcp-config.example.json`](./.htmlook/mcp-config.example.json)
  — config de ejemplo para un cliente MCP externo.
