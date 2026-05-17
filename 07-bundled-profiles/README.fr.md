# Step 7 · Bundled Profiles (HyperFrames / Slidev + 6 autres)

<p align="center">
  <a href="README.md">English</a> | <a href="README.ko.md">한국어</a> | <a href="README.ja.md">日本語</a> | <a href="README.de.md">Deutsch</a> | <b>Français</b> | <a href="README.es.md">Español</a> | <a href="README.pt.md">Português</a> | <a href="README.it.md">Italiano</a>
</p>

> v1.0 livre 8 *Heavyweight Profiles* embarqués dans l'app. Au premier
> lancement, ils sont auto-décompressés sous
> `~/.htmlook/profiles/_bundled-*`.
> ~ 5 min (juste un tour — l'usage réel dépend de la courbe
> d'apprentissage de chaque outil).

Un Profile = outil externe + bundle Skill v0.3 + contenu seed, le
tout packagé. Installation en un clic depuis le New Workspace Wizard
(⌘⇧N) ou une carte de l'Add wizard.

> Les manifests des profiles eux-mêmes (profile.json + SKILL.md +
> seed/) vivent à la racine du campus dans
> [`../profiles/`](../profiles/) — le builder catalog.json y lit
> directement. Ce step est la visite guidée autour.

## 7.1 · Les 8 cartes profile

| Profile | Catégorie | Sortie | Licence de l'outil | Démarrer |
|---------|-----------|--------|-------------------|---------|
| HyperFrames | motion-graphics | mp4 (kinetic typography) | MIT | [`../profiles/hyperframes/`](../profiles/hyperframes/) |
| Slidev | presentation | HTML/PDF slides | MIT | [`../profiles/slidev/`](../profiles/slidev/) |
| Quarto | publishing | PDF/HTML/PPT/book | GPL-2.0 | [`../profiles/quarto/`](../profiles/quarto/) |
| D2 | diagram | SVG | MPL-2.0 | [`../profiles/d2/`](../profiles/d2/) |
| Astro Starlight | documentation | docs site | MIT | [`../profiles/astro-starlight/`](../profiles/astro-starlight/) |
| Marimo | notebook | reactive HTML | Apache-2.0 | [`../profiles/marimo/`](../profiles/marimo/) |
| Excalidraw | diagram | JSON/SVG/PNG | MIT | [`../profiles/excalidraw/`](../profiles/excalidraw/) |
| Manim | educational-animation | mp4 | BSD-3-Clause | [`../profiles/manim/`](../profiles/manim/) |

> **HTMLook ne bundle pas les outils eux-mêmes.** L'app livre les
> guides d'usage et l'intégration au Wizard. Chaque outil externe
> s'installe à part (les READMEs de profile listent les dépendances).

## 7.2 · En choisir un et démarrer

Pour une première fois, partez léger :

- **Slidev** — `npx slidev` pour installer. Un fichier md → slides HTML.
- **D2** — installez un binaire Go. txt → diagramme SVG.
- **Excalidraw** — pas d'installation nécessaire (HTMLook embarque un
  viewer).

Les plus lourds :

- **HyperFrames** — Node + ffmpeg + Kokoro TTS (Python). L'outil même
  avec lequel les vidéos du campus ont été faites.
- **Manim** — Python + LaTeX. Animation mathématique.
- **Quarto** — R / Python / Pandoc. Publication académique.

## 7.3 · Installer depuis l'Add wizard

1. ⌘⇧N (New Workspace Wizard) ou *+* dans la sidebar (Add wizard).
2. Choisissez la carte profile voulue dans le catalogue.
3. *Install* — le dossier seed est copié dans votre home.
4. *Open* — HTMLook ouvre ce dossier comme workspace et les Skills du
   profile atterrissent dans le catalogue ⌘K.

## 7.4 · Seeds de domaine supplémentaires (optionnel)

Au-delà des 8 profiles, 75 seeds de workspace vivent dans
[`../sample_workspaces/`](../sample_workspaces/) — tous préfixés pour
qu'on voie au coup d'œil de quel profile vient chacun :

- `hf-*/` (26 — HyperFrames, le lineup complet de personas utilisé pour
  produire les vidéos du campus)
- `slidev-*/` (7) · `quarto-*/` (7) · `marimo-*/` (7) · `manim-*/` (7)
- `d2-*/` (7) · `excalidraw-*/` (7) · `astro-*/` (7)

`hf-claude/` et `hf-llama/` sont les références BYOM (Anthropic Claude
/ Llama local). Les 24 autres (`hf-corp-deck/`, `hf-teacher-quiz/`,
`hf-kid-coding/` …) sont des scénarios de domaine. Chaque seed livre
le set complet `index.html + hyperframes.json + brand.txt +
prompts.txt + AGENTS.md + meta.json + README.md`, pour qu'un agent AI
puisse rejouer fidèlement le workflow avec le BYOM de l'utilisateur.

Catalogue complet : [`../catalog.json`](../catalog.json) — actuellement
**83 entrées** (8 profile + 75 workspace seed). Le CI le reconstruit
automatiquement ([`../scripts/build-catalog.mjs`](../scripts/build-catalog.mjs)).

## ✅ Checkpoint Step 7

- Vous avez lu une des 8 READMEs de profile.
- (Optionnel) Vous avez installé un outil externe → via l'Add wizard,
  installé le seed de ce profile.
- (Optionnel) Vous avez parcouru un seed de `sample_workspaces/`
  proche de votre domaine.

Tout ? → [Step 8 · extend (écrire votre propre Profile)](../08-extend/)

## Pour aller plus loin

- Le `SKILL.md` dans chaque dossier profile — le manifest Skill v0.3
  que ce profile enregistre.
- [`../08-extend/PRODUCTION.md`](../08-extend/PRODUCTION.md) — le
  standard de production des vidéos du campus avec HyperFrames (les
  17 + 26 vidéos sont toutes faites avec cet outil).
