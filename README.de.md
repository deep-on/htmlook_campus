# HTMLook Campus

<p align="center">
  <a href="README.md">English</a> | <a href="README.ko.md">한국어</a> | <a href="README.ja.md">日本語</a> | <b>Deutsch</b> | <a href="README.fr.md">Français</a> | <a href="README.es.md">Español</a> | <a href="README.pt.md">Português</a> | <a href="README.it.md">Italiano</a>
</p>

> Ein **8-Schritt-Tutorial** für alle, die HTMLook Pro neu kennenlernen.
> Schritt für Schritt durchgearbeitet kommst du in 30–40 Minuten von
> Installation → erste Datei → BYOM → Bearbeiten → Befehle → save-as-skill
> → mitgelieferte Profile → eigenem Profil.

Dieses Repository entspricht dem **HTMLook Pro v1.0 Release Candidate**
(GA für Mitte 2026 geplant). Die Desktop-App findest du unter
[htmlook.app](https://htmlook.app) — 14 Tage kostenlos testen. BYOM
(Bring-Your-Own-Model) heißt: kein Token-Aufschlag — Claude · GPT · Gemini ·
DeepSeek · Mistral · Together · Groq · Cerebras · Ollama, ruf jedes Modell
direkt mit deinem eigenen Key auf.

## Tutorial-Pfad

Von oben nach unten. Jeder Schritt baut auf dem vorherigen auf.

| Schritt | Ordner | Was du tust | Dauer |
|---|---|---|---|
| 1 | [`01-getting-started/`](01-getting-started/) | Installation · erster Start · Drag & Drop · Ordner öffnen | 3 min |
| 2 | [`02-first-file/`](02-first-file/) | md / html / pdf / Video — 4 Dateitypen, Split-View, Outline | 5 min |
| 3 | [`03-byom-setup/`](03-byom-setup/) | einen Anbieter wählen und Key hinterlegen (oder Ollama) | 5 min |
| 4 | [`04-editing/`](04-editing/) | Element-Pick · Region-Paint · Sentence-ID · Cite-Anchor | 5 min |
| 5 | [`05-command/`](05-command/) | Chat · Terminal-CLI · apply_edit · 26 Persona-Walkthroughs | 10 min |
| 6 | [`06-save-as-skill/`](06-save-as-skill/) | Workflow festhalten → ⌘K-Katalogkarte | 5 min |
| 7 | [`07-bundled-profiles/`](07-bundled-profiles/) | HyperFrames · Slidev · Quarto · D2 · Astro Starlight · Marimo · Excalidraw · Manim | 5 min |
| 8 | [`08-extend/`](08-extend/) | eigenes Profil schreiben + Katalog-PR einreichen | optional |

> Wenn du nur einen schnellen Überblick willst, schau dir das Schritt → Video
> Mapping in [`01-getting-started/LEARNING_PATH.md`](01-getting-started/LEARNING_PATH.md)
> an. Jedes Video dauert 30–70 Sekunden.

## Referenzhandbuch (Wiki)

Das 8-Schritt-Tutorial zeigt dir den Ablauf *einmal von Anfang bis Ende*.
Das [`wiki/`](wiki/) ist das **Feature-für-Feature-Referenzhandbuch**, zu
dem du danach immer wieder greifst: Sidebar · Tabs · Viewer · Markdown-Editor ·
PDF · Video/Audio-Player · Terminal · KI-Assistent · Paint · Sprachnotizen ·
Skill · Export · Einstellungen · Tastenkürzel. Zwei parallele Spuren — eine
für menschliche Nutzer, eine für KI-Assistenten (MCP / Schema).

| Spur | Einstieg | Sprachen |
|---|---|---|
| Handbuch für Menschen | [`wiki/Home.md`](wiki/Home.md) · [Koreanisch](wiki/Home-ko.md) | EN / KO |
| Anleitung für KI-Assistenten | [`wiki/AI-Overview.md`](wiki/AI-Overview.md) · [Koreanisch](wiki/AI-Overview-ko.md) | EN / KO |

Das Tutorial läufst du einmal durch; das Wiki liegt dauerhaft in Reichweite
(öffnen in der App über *Help → Documentation*).

## Editionen

- **HTMLook Pro** (v1.0) — für Power-User. BYOM-Chat + integriertes PTY-Terminal
  + CLI-Adapter (claude / codex / gemini) + MCP-Brücke + Paint-Canvas +
  Region-Capture + Element-Pick + Save-as-Skill + 8 Bundle-Profile + 49 Seeds.
- **HTMLook Easier** *(soon)* — Einsteiger-Edition, wird gerade neu definiert.

## Schritt 1 — Installation + erster Start

Beginne bei [`01-getting-started/README.md`](01-getting-started/README.md).

Lade das .dmg unter [htmlook.app](https://htmlook.app), zieh es in Applications,
und Drag-and-Drop deine erste Datei hinein.

## Schritt 2 — Erste Datei (HTML / MD / PDF / Video)

[`02-first-file/README.md`](02-first-file/README.md). Vier Dateitypen mit
Split-View + Outline + Thumbnails durchblättern.

Videos: BASIC #3 #4 #6 + ADV multi-pane / thumbnail / outline. Die mp4s
liegen unter [`videos/features/`](videos/features/).

## Schritt 3 — BYOM einrichten (nur ein Anbieter)

[`03-byom-setup/README.md`](03-byom-setup/README.md). Den ausführlichen
KI-Leitfaden findest du in [`03-byom-setup/AI_GUIDE.md`](03-byom-setup/AI_GUIDE.md);
eine Beispielkonfiguration für externe MCP-Clients liegt unter
[`03-byom-setup/.htmlook/mcp-config.example.json`](03-byom-setup/.htmlook/mcp-config.example.json).

## Schritt 4 — Auf dem Bildschirm *auf etwas zeigen*

[`04-editing/README.md`](04-editing/README.md). Vier Möglichkeiten: Element-Pick ·
Region-Paint · Sentence-ID · Range-Select. Kernvideo: BASIC #5 ⭐ region-cite
(der Einstiegspunkt für die KI).

## Schritt 5 — Per Befehl ändern (cite + apply_edit)

[`05-command/README.md`](05-command/README.md). Der tiefste Teil des Campus —
26 Persona-Walkthroughs unter [`05-command/personas/`](05-command/personas/)
(nach Rolle gruppiert, jeweils mit Follow-Along WALKTHROUGH.md + before/after).

Persona-Katalog: [`05-command/personas/INDEX.md`](05-command/personas/INDEX.md).

## Schritt 6 — Wiederkehrende Workflows → Skills

[`06-save-as-skill/README.md`](06-save-as-skill/README.md). Im rechten KI-Panel
der Dialog *Save as Skill*. Drei Zeilen, fertig.

## Schritt 7 — Die 8 mitgelieferten Profile

[`07-bundled-profiles/README.md`](07-bundled-profiles/README.md). HyperFrames /
Slidev / Quarto / D2 / Astro Starlight / Marimo / Excalidraw / Manim. Die
Profile-Seeds selbst liegen unter [`profiles/`](profiles/) (der catalog.json-
Builder liest direkt von dort).

## Schritt 8 — Eigenes Profil + Video-Standard

[`08-extend/README.md`](08-extend/README.md). Bau ein Profil für deine eigene
Domain und reich es im Katalog ein. Der Video-Standard und das
Reverse-Verification-Verfahren stehen in
[`08-extend/PRODUCTION.md`](08-extend/PRODUCTION.md); der Katalog der 17
Feature-Videos in [`08-extend/FEATURES.md`](08-extend/FEATURES.md).

## Asset-Lokationen (Referenz)

Neben den Schritt-Ordnern (01~08) liegen im Campus-Root diese *gemeinsamen
Asset-Verzeichnisse* (catalog.json + die App referenzieren sie per Pfad, sie
wandern also nicht in einzelne Schritt-Ordner):

| Ordner | Inhalt |
|---|---|
| [`videos/`](videos/) | 17 Feature-mp4 + 26 Persona-mp4 (insgesamt ~340 MB) |
| [`profiles/`](profiles/) | 8 Profile-Seeds (`profile.json` + `SKILL.md` + `seed/`) |
| [`sample_workspaces/`](sample_workspaces/) | 75 Domain-Seeds (`hf-*` 26 Personas + 49 Profil-Seeds) |
| [`catalog.json`](catalog.json) | 83 Einträge (8 Profile + 75 Workspace-Seeds) — vom Wizard der App fresh-gefetcht (24 h Cache) |
| [`scripts/`](scripts/) | `build-catalog.mjs` |
| [`infra/`](infra/) | Lizenz-Worker (eigenständiger Dienst) |
| [`docs/`](docs/) | Arbeitsbereich für generierte Artefakte (gitignored) |

## Zwei Lernebenen — Video + interaktiv

Die Campus-Videos zeigen das *was (was möglich ist)*. Der eingebaute
interaktive Walkthrough in HTMLook Pro (*Help → Interactive Tutorials…*) ist
das *wie (wie es geht)*. Zu jedem der 17 Features in den Videos gibt es einen
passenden interaktiven Guide, eins zu eins.

| Ebene | Wo | Länge | Rolle |
|---|---|---|---|
| Video (Campus) | `videos/features/`, `videos/` | 30 s / 60–70 s | zeigt das Ergebnis |
| Interaktiv (App) | HTMLook Pro · Help → Interactive Tutorials… | 4 Schritte | Hands-on-Übung |

## Reverse-Verification-Versprechen

Jedes Video in diesem Campus **behauptet nur Dinge, die HTMLook auch
wirklich tut**. Features, die es nicht gibt, werden nicht beworben. Der
Verifikationsprozess und die Liste korrigierter False Claims stehen in
[`08-extend/PRODUCTION.md`](08-extend/PRODUCTION.md).

## Status

Dieses Repo synchronisiert mit dem **HTMLook Pro v1.0 Release Candidate** (GA
für Mitte 2026 geplant) als lebendiges Lernmaterial. Mit v1.0 GA wechselt es
gleichzeitig öffentlich + der Katalog-Endpoint (`htmlook.app/catalog`)
fresh-fetcht ab dann die raw-URLs dieses Repos (24 h Cache).

## Lizenz

- Code / Walkthrough-Texte: MIT
- Video-mp4: CC BY 4.0 (mit Quellangabe *"HTMLook Campus"*)
- Beispiel-Content (PDF / xlsx / md / html): CC0 / Public Domain — alles fiktive Platzhalter
