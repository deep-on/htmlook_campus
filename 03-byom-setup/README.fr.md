# Step 3 · Setup BYOM (choisir un seul fournisseur)

<p align="center">
  <a href="README.md">English</a> | <a href="README.ko.md">한국어</a> | <a href="README.ja.md">日本語</a> | <a href="README.de.md">Deutsch</a> | <b>Français</b> | <a href="README.es.md">Español</a> | <a href="README.pt.md">Português</a> | <a href="README.it.md">Italiano</a>
</p>

> Bring-Your-Own-Model — vous enregistrez vous-même la clé fournisseur.
> Zéro marge sur les tokens.
> ~ 5 min.

HTMLook ne livre pas de LLM ; il fournit juste des *adaptateurs*. v1.0
supporte 9 fournisseurs : Claude / GPT / Gemini / DeepSeek / Mistral /
Together / Groq / Cerebras / Ollama (local). À cette étape vous **en
choisissez un** et confirmez qu'il fonctionne — vous changerez plus tard
au [Step 5](../05-command/).

## 3.1 · Trois points d'entrée

Trois façons d'appeler un LLM depuis HTMLook. Toutes les trois exposent
les mêmes outils MCP (`htmlook_*`) :

| Voie | Où | Pour qui |
|---|---|---|
| **Chat BYOM intégré** ⭐ | Settings → Models → enregistrez la clé, puis le panneau AI à droite | Nouveaux venus |
| **Terminal + CLI intégrés** | Bascule ⌘J, lancez `claude` / `codex` / `gemini` | Utilisateurs à l'aise en CLI |
| **Client MCP externe** | Merger dans le mcp.json de Claude Code / Cursor / Windsurf / Zed | Déjà sur un autre client |

Guide complet + liste des outils MCP : [`AI_GUIDE.md`](AI_GUIDE.md).

## 3.2 · Recommandé : chat BYOM intégré

1. Engrenage en haut à droite de HTMLook → onglet **Settings → Models**.
2. Choisissez un fournisseur → *Add Provider* :
   - Anthropic Claude (le plus stable), ou
   - OpenAI GPT, ou
   - Google Gemini (free tier le plus large).
3. Collez la clé API → *Test* — cherchez un 200 OK.
4. *Save* — le panneau AI à droite s'active.

> Vidéo : [ADV · Swap the LLM. Keep the workflow.](../videos/features/13-advanced-07-mcp-swap.mp4)
> (30 s · LLM-agnostique via MCP)

## 3.3 · Ollama (local, sans clé)

Si vous ne voulez pas envoyer de clé à un service externe :

1. Installez Ollama depuis [ollama.com](https://ollama.com).
2. `ollama pull llama3.2` (ou n'importe quel modèle).
3. HTMLook Settings → Models → *Add Provider* → Ollama → host
   `http://localhost:11434` (défaut).

## 3.4 · Avec un client MCP externe

Si vous êtes déjà sur Claude Code / Cursor / Windsurf / Zed, fusionnez le
contenu de [`./.htmlook/mcp-config.example.json`](./.htmlook/mcp-config.example.json)
dans le mcp.json de votre client. Le serveur MCP HTMLook expose ~22
outils `htmlook_*` (cite, apply_edit, selection, region_current_png,
outline, link, video_*, …).

## 3.5 · Premier hello

Une fois le panneau AI activé, tapez dans le chat :

> *Résume en une ligne le premier fichier du workspace actuel.*

Vérifiez que le LLM va chercher le contexte du workspace via l'outil MCP
`htmlook_active_file` avant de répondre. Si la réponse ignore le
workspace, cliquez à nouveau **Settings → AI → Connect**, ou — avec un
client MCP externe — revérifiez la fusion de mcp.json.

## 3.6 · Auto-reload — après la réponse du modèle

Quand `apply_edit` écrit dans un fichier, le file watcher détecte et le
pane droit de la split view se recharge automatiquement.

> Vidéo : [ADV · It just reloaded.](../videos/features/11-advanced-05-auto-reload.mp4)
> (30 s)

## ✅ Checkpoint Step 3

- La clé d'un fournisseur (ou Ollama) est enregistrée sous Settings →
  Models.
- Vous avez envoyé un hello dans le chat et reçu une réponse.
- La réponse connaît le contexte du workspace.

Souci ? Section *debugging* de [`AI_GUIDE.md`](AI_GUIDE.md).

Les trois ? → [Step 4 · editing (paint / region / element pick)](../04-editing/)

## Pour aller plus loin

- [`AI_GUIDE.md`](AI_GUIDE.md) — les ~22 outils MCP + le pattern de
  follow-along persona + le ton de sortie de l'agent AI.
- [`./.htmlook/mcp-config.example.json`](./.htmlook/mcp-config.example.json)
  — config d'exemple pour un client MCP externe.
