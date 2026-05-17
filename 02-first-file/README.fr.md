# Step 2 · Premier fichier (HTML / Markdown / PDF / vidéo)

<p align="center">
  <a href="README.md">English</a> | <a href="README.ko.md">한국어</a> | <a href="README.ja.md">日本語</a> | <a href="README.de.md">Deutsch</a> | <b>Français</b> | <a href="README.es.md">Español</a> | <a href="README.pt.md">Português</a> | <a href="README.it.md">Italiano</a>
</p>

> Apprenez l'essentiel du *viewer* de HTMLook. La partie qui a déjà de la
> valeur sans AI / MCP.
> ~ 5 min.

À la fin de cette étape : vous savez comment lire chacun des quatre types
de fichier (md / html / pdf / vidéo) et comment naviguer avec split view,
preview et outline.

## 2.1 · Markdown — édition live

1. Double-clic sur n'importe quel `.md` dans la sidebar (par ex.
   [`../05-command/personas/03-dev-pr-docs/docs.md`](../05-command/personas/03-dev-pr-docs/docs.md)).
2. Basculez la split view avec ⌘\\ ou *View → Split*.
3. Source à gauche, preview à droite. Vous tapez à gauche, le côté droit
   se rafraîchit en direct.

> Vidéo : [BASIC #3 · Type left. See right. Live.](../videos/features/03-basic-03-md-live-edit.mp4) (30 s)

## 2.2 · HTML — cliquer un élément pour l'éditer

1. Double-clic sur un `.html` (par ex.
   [`../05-command/personas/01-hf-claude/landing.html`](../05-command/personas/01-hf-claude/landing.html)).
2. Mode par défaut : preview. En split view, cliquez un élément
   directement → un éditeur de texte apparaît.
3. Sync bidirectionnel — les changements en preview arrivent dans la
   source instantanément.

> Vidéo : [BASIC #4 · Click anything. Edit it.](../videos/features/04-basic-04-html-split.mp4) (30 s)

## 2.3 · HTML — quatre modes de sélection

Dans le même fichier HTML, ⌘E fait tourner les quatre modes de sélection :

| Mode | Ce qu'il prend |
|---|---|
| element | un seul nœud DOM |
| range | une plage de texte |
| region | un rectangle peint |
| outline | l'arbre des titres |

Vidéo : [BASIC #6 · Pick what you see.](../videos/features/06-basic-06-html-4mode.mp4) (30 s)

Ce que chaque mode capture devient le point d'entrée de cite-anchor à
[Step 4 · editing](../04-editing/).

## 2.4 · PDF — pages + couche texte

1. Double-clic sur un `.pdf` (par ex.
   [`../05-command/personas/05-domain-battery/vendor.pdf`](../05-command/personas/05-domain-battery/vendor.pdf)).
2. Navigateur de miniatures à gauche + canvas de page à droite + couche
   texte sélectionnable.
3. Drag-select sur une région → region cite (utilisé en Step 4).

## 2.5 · Vidéo — miniatures de frame + outline

1. Double-clic sur n'importe quel mp4 (par ex.
   [`../videos/features/01-basic-01-drop-open.mp4`](../videos/features/01-basic-01-drop-open.mp4)).
2. Le viewer vidéo affiche une timeline avec aperçus en miniature.
3. ⌘Shift+T ou hover vous donne un aperçu de 1 s sur la frame (sans
   scrubbing).

> Vidéo : [ADV · Frame check. No scrub.](../videos/features/15-advanced-09-thumbnail.mp4) (30 s, catégorie advanced)

## 2.6 · Outline — naviguer dans un long document

La structure des titres d'un long md / html / PDF → onglet Outline dans le
panneau droit. Cliquez un titre pour y sauter.

> Vidéo : [ADV · Click §3.2. You're there.](../videos/features/16-advanced-10-outline.mp4) (30 s)

## 2.7 · Split view / multi-pane (⌘1 / ⌘2 / ⌘3 / ⌘J)

| Raccourci | Effet |
|---|---|
| ⌘1 | Preview seulement |
| ⌘2 | Source seulement |
| ⌘3 | Split (preview + source) |
| ⌘J | Bascule du panneau terminal |

Vidéo : [ADV · Two keys. Three views.](../videos/features/10-advanced-04-multi-pane.mp4)
(30 s — le *"Two keys"* de la narration était ⌘D + ⌘J dans la coupe
originale, corrigé en ⌘1/⌘2/⌘3 + ⌘J pour la v1.0. Historique complet
dans [`../08-extend/PRODUCTION.md`](../08-extend/PRODUCTION.md), tableau
*fixed false claims*.)

## ✅ Checkpoint Step 2

- Vous avez ouvert une md / html / pdf / vidéo, chacune en split view.
- Vous avez senti la différence entre les quatre modes HTML (element /
  range / region / outline) en cliquant directement.
- ⌘1 / ⌘2 / ⌘3 / ⌘J pour basculer la mise en page est devenu un réflexe.

Les trois ? → [Step 3 · BYOM setup](../03-byom-setup/) — choisissez un
fournisseur et enregistrez une clé.
