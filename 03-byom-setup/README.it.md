# Step 3 · Setup BYOM (scegli un fornitore)

<p align="center">
  <a href="README.md">English</a> | <a href="README.ko.md">한국어</a> | <a href="README.ja.md">日本語</a> | <a href="README.de.md">Deutsch</a> | <a href="README.fr.md">Français</a> | <a href="README.es.md">Español</a> | <a href="README.pt.md">Português</a> | <b>Italiano</b>
</p>

> Bring-Your-Own-Model — registri tu stesso la chiave del fornitore.
> Margine zero sui token.
> ~ 5 min.

HTMLook non include un LLM; offre solo *adattatori*. La v1.0 supporta
9 fornitori: Claude / GPT / Gemini / DeepSeek / Mistral / Together /
Groq / Cerebras / Ollama (locale). In questo step ne **scegli uno** e
verifichi che funzioni — più tardi cambierai in [Step 5](../05-command/).

## 3.1 · Tre vie d'ingresso

Tre modi per chiamare un LLM da HTMLook. Tutti e tre espongono gli
stessi strumenti MCP (`htmlook_*`):

| Via | Dove | Per chi |
|---|---|---|
| **Chat BYOM integrato** ⭐ | Settings → Models → registra la chiave, poi il pannello AI a destra | Chi inizia |
| **Terminal + CLI integrati** | Attiva con ⌘J, lancia `claude` / `codex` / `gemini` | Chi è a suo agio in CLI |
| **Client MCP esterno** | Unisci nel mcp.json di Claude Code / Cursor / Windsurf / Zed | Già su un altro client |

Guida completa + elenco degli strumenti MCP: [`AI_GUIDE.md`](AI_GUIDE.md).

## 3.2 · Consigliato: chat BYOM integrato

1. Ingranaggio in alto a destra in HTMLook → tab **Settings → Models**.
2. Scegli un fornitore → *Add Provider*:
   - Anthropic Claude (il più stabile), oppure
   - OpenAI GPT, oppure
   - Google Gemini (free tier più ampio).
3. Incolla la chiave API → *Test* — cerca un 200 OK.
4. *Save* — il pannello AI a destra si attiva.

> Video: [ADV · Swap the LLM. Keep the workflow.](../videos/features/13-advanced-07-mcp-swap.mp4)
> (30 s · LLM-agnostico via MCP)

## 3.3 · Ollama (locale, senza chiave)

Se non vuoi mandare una chiave a un servizio esterno:

1. Installa Ollama da [ollama.com](https://ollama.com).
2. `ollama pull llama3.2` (o qualunque modello).
3. HTMLook Settings → Models → *Add Provider* → Ollama → host
   `http://localhost:11434` (default).

## 3.4 · Con un client MCP esterno

Se sei già su Claude Code / Cursor / Windsurf / Zed, unisci il
contenuto di [`./.htmlook/mcp-config.example.json`](./.htmlook/mcp-config.example.json)
nel mcp.json del tuo client. Il server MCP di HTMLook espone circa 22
strumenti `htmlook_*` (cite, apply_edit, selection,
region_current_png, outline, link, video_*, …).

## 3.5 · Primo hello

Con il pannello AI attivo, scrivi nella chat:

> *Riassumi in una riga il primo file del workspace attuale.*

Verifica che l'LLM prenda il contesto del workspace via lo strumento
MCP `htmlook_active_file` prima di rispondere. Se la risposta non
"vede" il workspace, premi di nuovo **Settings → AI → Connect**, o —
con un client MCP esterno — controlla di nuovo il merge del mcp.json.

## 3.6 · Auto-reload — dopo che il modello risponde

Quando `apply_edit` scrive su un file, il file watcher lo nota e il
pane destro della split view si ricarica da solo.

> Video: [ADV · It just reloaded.](../videos/features/11-advanced-05-auto-reload.mp4)
> (30 s)

## ✅ Checkpoint Step 3

- La chiave di un fornitore (o Ollama) è in Settings → Models.
- Hai mandato un hello in chat e hai ricevuto risposta.
- La risposta è consapevole del contesto del workspace.

Problemi? Sezione *debugging* in [`AI_GUIDE.md`](AI_GUIDE.md).

Tutti e tre? → [Step 4 · editing (paint / region / element pick)](../04-editing/)

## Per approfondire

- [`AI_GUIDE.md`](AI_GUIDE.md) — i ~22 strumenti MCP + il pattern di
  follow-along delle persona + il tono di output dell'agente AI.
- [`./.htmlook/mcp-config.example.json`](./.htmlook/mcp-config.example.json)
  — config di esempio per un client MCP esterno.
