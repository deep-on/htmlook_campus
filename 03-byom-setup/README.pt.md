# Step 3 · Setup BYOM (escolha um fornecedor)

<p align="center">
  <a href="README.md">English</a> | <a href="README.ko.md">한국어</a> | <a href="README.ja.md">日本語</a> | <a href="README.de.md">Deutsch</a> | <a href="README.fr.md">Français</a> | <a href="README.es.md">Español</a> | <b>Português</b> | <a href="README.it.md">Italiano</a>
</p>

> Bring-Your-Own-Model — você mesmo registra a chave do fornecedor.
> Margem zero sobre tokens.
> ~ 5 min.

O HTMLook não embarca um LLM; só entrega *adaptadores*. A v1.0 suporta
9 fornecedores: Claude / GPT / Gemini / DeepSeek / Mistral / Together /
Groq / Cerebras / Ollama (local). Neste passo você **escolhe um** e
confirma que está rodando — depois você troca no
[Step 5](../05-command/).

## 3.1 · Três caminhos de entrada

Três jeitos de chamar um LLM a partir do HTMLook. Os três expõem as
mesmas ferramentas MCP (`htmlook_*`):

| Caminho | Onde | Para quem |
|---|---|---|
| **Chat BYOM embutido** ⭐ | Settings → Models → registre a chave, depois o painel AI à direita | Recém-chegados |
| **Terminal + CLI embutidos** | Alterne com ⌘J, rode `claude` / `codex` / `gemini` | Quem é confortável com CLI |
| **Cliente MCP externo** | Mescle no mcp.json de Claude Code / Cursor / Windsurf / Zed | Já usa outro cliente |

Guia completo + lista das ferramentas MCP: [`AI_GUIDE.md`](AI_GUIDE.md).

## 3.2 · Recomendado: chat BYOM embutido

1. Engrenagem no canto superior direito do HTMLook → aba **Settings →
   Models**.
2. Escolha um fornecedor → *Add Provider*:
   - Anthropic Claude (mais estável), ou
   - OpenAI GPT, ou
   - Google Gemini (free tier maior).
3. Cole a chave API → *Test* — procure um 200 OK.
4. *Save* — o painel AI à direita liga.

> Vídeo: [ADV · Swap the LLM. Keep the workflow.](../videos/features/13-advanced-07-mcp-swap.mp4)
> (30 s · LLM-agnóstico via MCP)

## 3.3 · Ollama (local, sem chave)

Se você não quer mandar chave para serviço externo:

1. Instale o Ollama de [ollama.com](https://ollama.com).
2. `ollama pull llama3.2` (ou qualquer modelo).
3. HTMLook Settings → Models → *Add Provider* → Ollama → host
   `http://localhost:11434` (padrão).

## 3.4 · Com cliente MCP externo

Se você já está no Claude Code / Cursor / Windsurf / Zed, mescle o
conteúdo de [`./.htmlook/mcp-config.example.json`](./.htmlook/mcp-config.example.json)
no mcp.json do seu cliente. O servidor MCP do HTMLook expõe cerca de
22 ferramentas `htmlook_*` (cite, apply_edit, selection,
region_current_png, outline, link, video_*, …).

## 3.5 · Primeiro hello

Com o painel AI ligado, digite no chat:

> *Resuma em uma linha o primeiro arquivo do workspace atual.*

Confirme que o LLM busca o contexto do workspace pela ferramenta MCP
`htmlook_active_file` antes de responder. Se a resposta ignorar o
workspace, aperte de novo **Settings → AI → Connect**, ou — com
cliente MCP externo — confira de novo o merge do mcp.json.

## 3.6 · Auto-reload — depois que o modelo responde

Quando `apply_edit` grava num arquivo, o file watcher detecta e o pane
direito do split view recarrega sozinho.

> Vídeo: [ADV · It just reloaded.](../videos/features/11-advanced-05-auto-reload.mp4)
> (30 s)

## ✅ Checkpoint Step 3

- A chave de um fornecedor (ou Ollama) está em Settings → Models.
- Você mandou um hello no chat e recebeu resposta.
- A resposta enxerga o contexto do workspace.

Problemas? Seção *debugging* em [`AI_GUIDE.md`](AI_GUIDE.md).

Os três? → [Step 4 · editing (paint / region / element pick)](../04-editing/)

## Mais a fundo

- [`AI_GUIDE.md`](AI_GUIDE.md) — as ~22 ferramentas MCP + o padrão de
  follow-along de personas + o tom de saída do agente AI.
- [`./.htmlook/mcp-config.example.json`](./.htmlook/mcp-config.example.json)
  — config exemplo para cliente MCP externo.
