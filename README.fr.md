# HTMLook Campus

<p align="center">
  <a href="README.md">English</a> | <a href="README.ko.md">한국어</a> | <a href="README.ja.md">日本語</a> | <a href="README.de.md">Deutsch</a> | <b>Français</b> | <a href="README.es.md">Español</a> | <a href="README.pt.md">Português</a> | <a href="README.it.md">Italiano</a>
</p>

> Un **tutoriel en 8 étapes** pour les personnes qui découvrent HTMLook Pro.
> En suivant les étapes une à une, vous passez en 30–40 minutes de
> l'installation → premier fichier → BYOM → édition → commande → save-as-skill
> → profils livrés → écriture de votre propre profil.

Ce dépôt suit le **HTMLook Pro v1.0 release-candidate** (GA prévu mi-2026).
L'application desktop est sur [htmlook.app](https://htmlook.app), avec 14
jours d'essai gratuit. BYOM (Bring-Your-Own-Model) signifie zéro marge sur
les tokens — Claude · GPT · Gemini · DeepSeek · Mistral · Together · Groq ·
Cerebras · Ollama, vous appelez n'importe quel modèle directement avec
votre propre clé.

## Parcours du tutoriel

De haut en bas. Chaque étape s'appuie sur la précédente.

| Étape | Dossier | Ce que vous faites | Durée |
|---|---|---|---|
| 1 | [`01-getting-started/`](01-getting-started/) | installation · premier lancement · drag-drop · ouvrir un dossier | 3 min |
| 2 | [`02-first-file/`](02-first-file/) | md / html / pdf / vidéo — 4 types, split view, outline | 5 min |
| 3 | [`03-byom-setup/`](03-byom-setup/) | choisir un fournisseur et enregistrer la clé (ou Ollama) | 5 min |
| 4 | [`04-editing/`](04-editing/) | element pick · region paint · sentence-id · cite anchor | 5 min |
| 5 | [`05-command/`](05-command/) | chat · CLI terminal · apply_edit · 26 walkthroughs de personas | 10 min |
| 6 | [`06-save-as-skill/`](06-save-as-skill/) | capturer un workflow → fiche catalogue ⌘K | 5 min |
| 7 | [`07-bundled-profiles/`](07-bundled-profiles/) | HyperFrames · Slidev · Quarto · D2 · Astro Starlight · Marimo · Excalidraw · Manim | 5 min |
| 8 | [`08-extend/`](08-extend/) | écrire votre propre profil + PR sur le catalogue | facultatif |

> Pour un tour rapide, le mapping étape → vidéo se trouve dans
> [`01-getting-started/LEARNING_PATH.md`](01-getting-started/LEARNING_PATH.md).
> Chaque vidéo dure 30–70 secondes.

## Manuel de référence (Wiki)

Le tutoriel en 8 étapes vous montre le flux *de bout en bout, une fois*. Le
[`wiki/`](wiki/) est le **manuel de référence fonctionnalité par
fonctionnalité** vers lequel vous revenez ensuite : Sidebar · Onglets ·
Viewer · Éditeur Markdown · PDF · Lecteur vidéo/audio · Terminal · Assistant
IA · Paint · Notes vocales · Skill · Export · Réglages · raccourcis. Deux
pistes parallèles — l'une pour les utilisateurs humains, l'autre pour les
assistants IA (MCP / schémas).

| Piste | Entrée | Langues |
|---|---|---|
| Manuel utilisateur humain | [`wiki/Home.md`](wiki/Home.md) · [Coréen](wiki/Home-ko.md) | EN / KO |
| Guide pour assistant IA | [`wiki/AI-Overview.md`](wiki/AI-Overview.md) · [Coréen](wiki/AI-Overview-ko.md) | EN / KO |

Le tutoriel ne se parcourt qu'une fois ; le wiki reste à portée de main tous
les jours (l'ouvrir depuis l'app via *Help → Documentation*).

## Éditions

- **HTMLook Pro** (v1.0) — pour les utilisateurs avancés. Chat BYOM +
  terminal PTY intégré + adaptateurs CLI (claude / codex / gemini) + pont MCP
  + canvas Paint + capture de région + sélection d'élément + save-as-skill +
  8 profils livrés + 49 seeds.
- **HTMLook Easier** *(bientôt)* — édition d'entrée de gamme, en cours de
  redéfinition.

## Étape 1 — Installation + premier lancement

Commencez par [`01-getting-started/README.md`](01-getting-started/README.md).

Téléchargez le .dmg depuis [htmlook.app](https://htmlook.app), glissez-le
dans Applications, et drag-and-drop votre premier fichier.

## Étape 2 — Premier fichier (HTML / MD / PDF / vidéo)

[`02-first-file/README.md`](02-first-file/README.md). Naviguez à travers
quatre types de fichier en split view + outline + miniatures.

Vidéos : BASIC #3 #4 #6 + ADV multi-pane / thumbnail / outline. Les mp4
eux-mêmes sont sous [`videos/features/`](videos/features/).

## Étape 3 — Configurer BYOM (un seul fournisseur)

[`03-byom-setup/README.md`](03-byom-setup/README.md). Pour le guide IA
détaillé, voir [`03-byom-setup/AI_GUIDE.md`](03-byom-setup/AI_GUIDE.md) ; un
exemple de configuration pour un client MCP externe se trouve dans
[`03-byom-setup/.htmlook/mcp-config.example.json`](03-byom-setup/.htmlook/mcp-config.example.json).

## Étape 4 — Pointer *quelque part* à l'écran

[`04-editing/README.md`](04-editing/README.md). Quatre façons : element pick ·
region paint · sentence-id · range select. Vidéo clé : BASIC #5 ⭐ region-cite
(point d'entrée IA).

## Étape 5 — Modifier par commande (cite + apply_edit)

[`05-command/README.md`](05-command/README.md). La partie la plus profonde du
campus — 26 walkthroughs de personas dans
[`05-command/personas/`](05-command/personas/) (groupés par rôle, chaque
dossier avec un WALKTHROUGH.md à suivre + before/after).

Catalogue des personas : [`05-command/personas/INDEX.md`](05-command/personas/INDEX.md).

## Étape 6 — Workflows récurrents → Skills

[`06-save-as-skill/README.md`](06-save-as-skill/README.md). Panneau IA à
droite, dialogue *Save as Skill*. Trois lignes, et c'est terminé.

## Étape 7 — Les 8 profils livrés

[`07-bundled-profiles/README.md`](07-bundled-profiles/README.md). HyperFrames /
Slidev / Quarto / D2 / Astro Starlight / Marimo / Excalidraw / Manim. Les
seeds de profil eux-mêmes sont sous [`profiles/`](profiles/) (le builder
catalog.json les lit directement de là).

## Étape 8 — Écrire son profil + standard vidéo

[`08-extend/README.md`](08-extend/README.md). Construisez un profil pour
votre propre domaine et ajoutez-le au catalogue. Le standard vidéo + le
processus de reverse-verification sont dans
[`08-extend/PRODUCTION.md`](08-extend/PRODUCTION.md) ; le catalogue des 17
vidéos de fonctionnalités dans
[`08-extend/FEATURES.md`](08-extend/FEATURES.md).

## Emplacements des assets (référence)

À côté des dossiers d'étape (01~08), la racine du campus contient ces
*répertoires d'assets partagés* (catalog.json + l'app y référencent par
chemin, donc ils ne migrent pas dans un dossier d'étape) :

| Dossier | Contenu |
|---|---|
| [`videos/`](videos/) | 17 mp4 de fonctionnalités + 26 mp4 de personas (~340 Mo au total) |
| [`profiles/`](profiles/) | 8 seeds de profil (`profile.json` + `SKILL.md` + `seed/`) |
| [`sample_workspaces/`](sample_workspaces/) | 75 seeds de domaine (`hf-*` 26 personas + 49 seeds de profil) |
| [`catalog.json`](catalog.json) | 83 entrées (8 profils + 75 seeds de workspace) — rechargé à chaud par l'assistant de l'app (cache 24 h) |
| [`scripts/`](scripts/) | `build-catalog.mjs` |
| [`infra/`](infra/) | worker de licences (service séparé) |
| [`docs/`](docs/) | espace de travail pour les artefacts générés (gitignored) |

## Deux couches d'apprentissage — vidéo + interactif

Les vidéos du campus montrent le *quoi (ce qui est possible)*. Le walkthrough
interactif intégré à HTMLook Pro (*Help → Interactive Tutorials…*) montre le
*comment (comment le faire)*. Chacune des 17 fonctionnalités vues dans les
vidéos a un guide interactif correspondant, un pour un.

| Couche | Où | Durée | Rôle |
|---|---|---|---|
| Vidéo (campus) | `videos/features/`, `videos/` | 30 s / 60–70 s | montre le résultat |
| Interactif (app) | HTMLook Pro · Help → Interactive Tutorials… | 4 étapes | pratique en direct |

## Promesse de reverse-verification

Chaque vidéo de ce campus **ne promet que ce que HTMLook fait
vraiment**. Les fonctionnalités qui n'existent pas ne sont pas annoncées.
Procédure de vérification + liste des fausses affirmations corrigées :
[`08-extend/PRODUCTION.md`](08-extend/PRODUCTION.md).

## État

Ce dépôt suit le **HTMLook Pro v1.0 release-candidate** (GA prévu mi-2026)
en tant que matériel pédagogique vivant. Il bascule en public en même temps
que la v1.0 GA, moment où l'endpoint catalogue (`htmlook.app/catalog`)
commencera à recharger à chaud les URLs raw de ce dépôt (cache 24 h).

## Licence

- Code / textes des walkthroughs : MIT
- Vidéos mp4 : CC BY 4.0 (attribuer *"HTMLook Campus"*)
- Contenu d'exemple (PDF / xlsx / md / html) : CC0 / domaine public — tous des placeholders fictifs
