# HTMLook Campus

<p align="center">
  <a href="README.md">English</a> | <a href="README.ko.md">한국어</a> | <a href="README.ja.md">日本語</a> | <a href="README.de.md">Deutsch</a> | <a href="README.fr.md">Français</a> | <a href="README.es.md">Español</a> | <a href="README.pt.md">Português</a> | <b>Italiano</b>
</p>

> Un **tutorial in 8 step** per chi si avvicina a HTMLook Pro. Seguendo gli
> step uno alla volta, in 30–40 minuti vai da installazione → primo file →
> BYOM → editing → comandi → save-as-skill → profili inclusi → scrivere il
> tuo profilo personale.

Questa repo segue il **HTMLook Pro v1.0 release-candidate** (GA prevista
per metà 2026). L'app desktop è su [htmlook.app](https://htmlook.app), con
14 giorni di prova gratuita. BYOM (Bring-Your-Own-Model) significa margine
zero sui token — Claude · GPT · Gemini · DeepSeek · Mistral · Together ·
Groq · Cerebras · Ollama, chiami il modello che preferisci direttamente con
la tua chiave.

## Percorso del tutorial

Dall'alto in basso. Ogni step si appoggia su quello precedente.

| Step | Cartella | Cosa fai | Tempo |
|---|---|---|---|
| 1 | [`01-getting-started/`](01-getting-started/) | installazione · primo avvio · drag-drop · apertura cartella | 3 min |
| 2 | [`02-first-file/`](02-first-file/) | md / html / pdf / video — 4 tipi, split view, outline | 5 min |
| 3 | [`03-byom-setup/`](03-byom-setup/) | scegli un fornitore e registra la chiave (oppure Ollama) | 5 min |
| 4 | [`04-editing/`](04-editing/) | element pick · region paint · sentence-id · cite anchor | 5 min |
| 5 | [`05-command/`](05-command/) | chat · terminale CLI · apply_edit · 26 walkthrough di persona | 10 min |
| 6 | [`06-save-as-skill/`](06-save-as-skill/) | catturare un workflow → scheda catalogo ⌘K | 5 min |
| 7 | [`07-bundled-profiles/`](07-bundled-profiles/) | HyperFrames · Slidev · Quarto · D2 · Astro Starlight · Marimo · Excalidraw · Manim | 5 min |
| 8 | [`08-extend/`](08-extend/) | scrivere il proprio profilo + PR sul catalogo | facoltativo |

> Per una panoramica veloce, la mappa step → video sta in
> [`01-getting-started/LEARNING_PATH.md`](01-getting-started/LEARNING_PATH.md).
> Ogni video dura 30–70 secondi.

## Manuale di riferimento (Wiki)

Il tutorial in 8 step ti mostra il flusso *dall'inizio alla fine, una
volta*. Il [`wiki/`](wiki/) è il **manuale di riferimento funzione per
funzione** a cui torni dopo: Sidebar · Tab · Viewer · Editor Markdown · PDF ·
Player video/audio · Terminale · Assistente IA · Paint · Note vocali · Skill ·
Export · Impostazioni · scorciatoie. Due piste parallele — una per utenti
umani, una per assistenti IA (MCP / schemi).

| Pista | Ingresso | Lingue |
|---|---|---|
| Manuale per utenti umani | [`wiki/Home.md`](wiki/Home.md) · [Coreano](wiki/Home-ko.md) | EN / KO |
| Guida per assistenti IA | [`wiki/AI-Overview.md`](wiki/AI-Overview.md) · [Coreano](wiki/AI-Overview-ko.md) | EN / KO |

Il tutorial lo percorri una volta; il wiki resta a portata di mano ogni
giorno (lo apri dall'app via *Help → Documentation*).

## Edizioni

- **HTMLook Pro** (v1.0) — per power user. Chat BYOM + terminale PTY
  integrato + adattatori CLI (claude / codex / gemini) + ponte MCP + canvas
  Paint + cattura regione + selezione elemento + save-as-skill + 8 profili
  inclusi + 49 seed.
- **HTMLook Easier** *(soon)* — edizione entry-level, in ridefinizione.

## Step 1 — Installazione + primo avvio

Parti da [`01-getting-started/README.md`](01-getting-started/README.md).

Scarica il .dmg da [htmlook.app](https://htmlook.app), trascinalo in
Applications, e fai drag-and-drop del tuo primo file.

## Step 2 — Primo file (HTML / MD / PDF / video)

[`02-first-file/README.md`](02-first-file/README.md). Naviga quattro tipi
di file con split view + outline + miniature.

Video: BASIC #3 #4 #6 + ADV multi-pane / thumbnail / outline. Gli mp4 stanno
in [`videos/features/`](videos/features/).

## Step 3 — Setup BYOM (un solo fornitore)

[`03-byom-setup/README.md`](03-byom-setup/README.md). Per la guida IA
completa: [`03-byom-setup/AI_GUIDE.md`](03-byom-setup/AI_GUIDE.md); un
esempio di configurazione per client MCP esterno in
[`03-byom-setup/.htmlook/mcp-config.example.json`](03-byom-setup/.htmlook/mcp-config.example.json).

## Step 4 — Puntare *a qualcosa* sullo schermo

[`04-editing/README.md`](04-editing/README.md). Quattro modi: element pick ·
region paint · sentence-id · range select. Video chiave: BASIC #5 ⭐ region-cite
(il punto d'ingresso per l'IA).

## Step 5 — Modificare con un comando (cite + apply_edit)

[`05-command/README.md`](05-command/README.md). La parte più profonda del
campus — 26 walkthrough di persona in
[`05-command/personas/`](05-command/personas/) (raggruppati per ruolo, ogni
cartella con un WALKTHROUGH.md da seguire + before/after).

Catalogo persona: [`05-command/personas/INDEX.md`](05-command/personas/INDEX.md).

## Step 6 — Workflow ricorrenti → Skill

[`06-save-as-skill/README.md`](06-save-as-skill/README.md). Pannello IA a
destra, dialog *Save as Skill*. Tre righe ed è fatto.

## Step 7 — Gli 8 profili inclusi

[`07-bundled-profiles/README.md`](07-bundled-profiles/README.md). HyperFrames /
Slidev / Quarto / D2 / Astro Starlight / Marimo / Excalidraw / Manim. I seed
di profilo stanno in [`profiles/`](profiles/) (il builder catalog.json li
legge direttamente da lì).

## Step 8 — Scrivi il tuo profilo + standard video

[`08-extend/README.md`](08-extend/README.md). Costruisci un profilo per il
tuo dominio e aggiungilo al catalogo. Lo standard video + la procedura di
reverse-verification stanno in
[`08-extend/PRODUCTION.md`](08-extend/PRODUCTION.md); il catalogo dei 17
video di feature in [`08-extend/FEATURES.md`](08-extend/FEATURES.md).

## Posizione degli asset (riferimento)

Accanto alle cartelle di step (01~08), nella root del campus ci sono questi
*directory di asset condivisi* (catalog.json + l'app li referenziano per
percorso, quindi non si spostano nelle singole cartelle di step):

| Cartella | Contenuto |
|---|---|
| [`videos/`](videos/) | 17 mp4 feature + 26 mp4 persona (~340 MB in totale) |
| [`profiles/`](profiles/) | 8 seed di profilo (`profile.json` + `SKILL.md` + `seed/`) |
| [`sample_workspaces/`](sample_workspaces/) | 75 seed di dominio (`hf-*` 26 persona + 49 seed di profilo) |
| [`catalog.json`](catalog.json) | 83 voci (8 profili + 75 seed di workspace) — fresh-fetch dal Wizard dell'app (cache 24 h) |
| [`scripts/`](scripts/) | `build-catalog.mjs` |
| [`infra/`](infra/) | worker delle licenze (servizio separato) |
| [`docs/`](docs/) | spazio di lavoro per artefatti generati (gitignored) |

## Due strati di apprendimento — video + interattivo

I video del campus mostrano il *cosa (cosa è possibile)*. Il walkthrough
interattivo integrato in HTMLook Pro (*Help → Interactive Tutorials…*)
mostra il *come (come si fa)*. Ognuna delle 17 funzionalità nei video ha
una guida interattiva corrispondente, una per una.

| Strato | Dove | Durata | Ruolo |
|---|---|---|---|
| Video (campus) | `videos/features/`, `videos/` | 30 s / 60–70 s | mostra il risultato |
| Interattivo (app) | HTMLook Pro · Help → Interactive Tutorials… | 4 step | pratica dal vivo |

## Promessa di reverse-verification

Ogni video di questo campus **afferma solo cose che HTMLook fa davvero**.
Funzionalità che non esistono non vengono pubblicizzate. Procedura di
verifica + elenco dei claim falsi corretti:
[`08-extend/PRODUCTION.md`](08-extend/PRODUCTION.md).

## Stato

Questa repo segue il **HTMLook Pro v1.0 release-candidate** (GA prevista
per metà 2026) come materiale didattico vivo. Diventa pubblica insieme al
v1.0 GA, momento in cui l'endpoint del catalogo (`htmlook.app/catalog`)
inizia a fresh-fetch degli URL raw di questa repo (cache 24 h).

## Licenza

- Codice / testi dei walkthrough: MIT
- Video mp4: CC BY 4.0 (attribuire *"HTMLook Campus"*)
- Contenuto d'esempio (PDF / xlsx / md / html): CC0 / pubblico dominio — tutti placeholder fittizi
