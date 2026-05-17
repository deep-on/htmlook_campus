# Step 3 · BYOM-Setup (einen Anbieter wählen)

<p align="center">
  <a href="README.md">English</a> | <a href="README.ko.md">한국어</a> | <a href="README.ja.md">日本語</a> | <b>Deutsch</b> | <a href="README.fr.md">Français</a> | <a href="README.es.md">Español</a> | <a href="README.pt.md">Português</a> | <a href="README.it.md">Italiano</a>
</p>

> Bring-Your-Own-Model — du registrierst den Vendor-Key selbst. Null
> Aufschlag auf Tokens.
> ~ 5 min.

HTMLook bundelt keinen LLM, sondern liefert nur *Adapter*. v1.0
unterstützt 9 Anbieter: Claude / GPT / Gemini / DeepSeek / Mistral /
Together / Groq / Cerebras / Ollama (lokal). In diesem Schritt **wählst
du einen** und bestätigst, dass er läuft — gewechselt wird später in
[Step 5](../05-command/).

## 3.1 · Drei Einstiegswege

Drei Wege, um einen LLM aus HTMLook aufzurufen. Alle drei stellen
dieselben MCP-Tools (`htmlook_*`) bereit:

| Weg | Wo | Für wen |
|---|---|---|
| **Eingebauter BYOM-Chat** ⭐ | Settings → Models → Key hinterlegen, dann das AI-Panel rechts | Einsteiger |
| **Eingebautes Terminal + CLI** | ⌘J umschalten, `claude` / `codex` / `gemini` starten | CLI-erfahrene Nutzer |
| **Externer MCP-Client** | In die mcp.json von Claude Code / Cursor / Windsurf / Zed mergen | Bereits anderer Client im Einsatz |

Volle Anleitung + Liste der MCP-Tools: [`AI_GUIDE.md`](AI_GUIDE.md).

## 3.2 · Empfohlen: eingebauter BYOM-Chat

1. Zahnrad oben rechts in HTMLook → Tab **Settings → Models**.
2. Einen Anbieter wählen → *Add Provider*:
   - Anthropic Claude (am stabilsten), oder
   - OpenAI GPT, oder
   - Google Gemini (größter Free-Tier).
3. API-Key einfügen → *Test* — auf 200 OK achten.
4. *Save* — das AI-Panel rechts aktiviert sich.

> Video: [ADV · Swap the LLM. Keep the workflow.](../videos/features/13-advanced-07-mcp-swap.mp4)
> (30 s · LLM-agnostisch über MCP)

## 3.3 · Ollama (lokal, kein Key)

Wenn du keinen Key an einen externen Dienst schicken willst:

1. Ollama von [ollama.com](https://ollama.com) installieren.
2. `ollama pull llama3.2` (oder ein beliebiges Modell).
3. HTMLook Settings → Models → *Add Provider* → Ollama → Host
   `http://localhost:11434` (Default).

## 3.4 · Bei einem externen MCP-Client

Wenn du schon Claude Code / Cursor / Windsurf / Zed nutzt, merge den
Inhalt von [`./.htmlook/mcp-config.example.json`](./.htmlook/mcp-config.example.json)
in die mcp.json deines Clients. Der HTMLook-MCP-Server stellt rund 22
`htmlook_*`-Tools bereit (cite, apply_edit, selection,
region_current_png, outline, link, video_*, …).

## 3.5 · Das erste hello

Sobald das AI-Panel an ist, tipp ins Chat-Feld:

> *Fass die erste Datei im aktuellen Workspace in einer Zeile zusammen.*

Schau, ob der LLM den Workspace-Kontext über das MCP-Tool
`htmlook_active_file` zieht, bevor er antwortet. Sieht die Antwort den
Workspace nicht, drück nochmal **Settings → AI → Connect**, oder — bei
externem MCP-Client — den Merge-Stand der mcp.json prüfen.

## 3.6 · Auto-Reload — nachdem das Modell geantwortet hat

Sobald `apply_edit` in eine Datei schreibt, erkennt es der File-Watcher
und das rechte Pane der Split-View lädt sich automatisch neu.

> Video: [ADV · It just reloaded.](../videos/features/11-advanced-05-auto-reload.mp4)
> (30 s)

## ✅ Step 3 Checkpoint

- Der Key eines Anbieters (oder Ollama) ist unter Settings → Models
  hinterlegt.
- Du hast ein hello in den Chat geschickt und eine Antwort bekommen.
- Die Antwort kennt den Workspace-Kontext.

Probleme? Siehe Abschnitt *Debugging* in [`AI_GUIDE.md`](AI_GUIDE.md).

Alle drei? → [Step 4 · editing (paint / region / element pick)](../04-editing/)

## Weiterlesen

- [`AI_GUIDE.md`](AI_GUIDE.md) — die rund 22 MCP-Tools + Persona-
  Follow-along-Muster + Output-Ton der AI-Agenten.
- [`./.htmlook/mcp-config.example.json`](./.htmlook/mcp-config.example.json)
  — Beispielkonfig für einen externen MCP-Client.
