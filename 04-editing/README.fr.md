# Step 4 · Editing (Paint / Region / Element Pick)

<p align="center">
  <a href="README.md">English</a> | <a href="README.ko.md">한국어</a> | <a href="README.ja.md">日本語</a> | <a href="README.de.md">Deutsch</a> | <b>Français</b> | <a href="README.es.md">Español</a> | <a href="README.pt.md">Português</a> | <a href="README.it.md">Italiano</a>
</p>

> Quatre façons de dire au LLM *quelle zone à l'écran* vous voulez.
> ~ 5 min.

La partie la plus distinctive de HTMLook. Quand vous dites à l'AI
*« corrige ici »*, vous pouvez pointer *ici* directement — comme un
peintre.

À la fin de cette étape, vous aurez parcouru le cycle clé une fois
vous-même : drag de region → cite anchor → prompt AI.

## 4.1 · Les quatre méthodes de sélection

| Méthode | Comment | Pour quoi |
|---|---|---|
| **element pick** | clic dans la preview | un seul nœud DOM (bouton / titre / paragraphe) |
| **range select** | drag dans la preview | une plage de texte (phrase / morceau) |
| **region paint** ⭐ | ⌘Shift+R puis drag d'un rectangle | une zone visuelle (chart / zone d'illustration) |
| **outline pick** | clic dans le panneau Outline à droite | une section centrée sur un titre |

Vidéo : [BASIC #6 · Pick what you see.](../videos/features/06-basic-06-html-4mode.mp4) (30 s)

## 4.2 · ⭐ Region cite — la clé de voûte

Le mouvement le plus important du Step 4. Votre premier *langage
commun* avec l'AI.

1. Ouvrez un HTML ou un PDF (par ex. [`../05-command/personas/01-hf-claude/landing.html`](../05-command/personas/01-hf-claude/landing.html)).
2. ⌘Shift+R entre dans le mode region paint.
3. Tracez un rectangle sur la preview → la zone s'éclaire en accent
   magenta.
4. Un cite anchor s'attache automatiquement au panneau AI à droite.
5. Dites à l'AI *« corrige ici — la valeur d'Apex (edge compute) en une
   ligne »*.

Si MCP est connecté, le LLM :
- récupère un PNG de la zone via `htmlook_region_current_png` (modèles
  vision),
- sécurise l'anchor texte correspondant avec `htmlook_active_file` +
  `htmlook_cite`,
- applique le patch via `htmlook_apply_edit`.

> Vidéo : [BASIC #5 ⭐ · Drag. Tell the LLM.](../videos/features/05-basic-05-region-cite.mp4)
> (30 s · le point d'entrée AI)

## 4.3 · Element pick

Hover sur un élément dans la preview → contour → clic → sélectionné.
⌘E bascule le mode.

L'outerHTML de l'élément sélectionné est lu par le LLM via
`htmlook_selection_html`, patché, puis commité avec
`htmlook_apply_edit`.

## 4.4 · Sentence-id (au niveau phrase dans un texte / vidéo long)

Citer la phrase #N directement dans un transcript ou un papier long :

1. Ouvrez une vidéo ou une longue md.
2. Activez *Sentence Map* dans le panneau droit → les phrases reçoivent
   un numéro N.
3. Clic → le cite anchor `sentence:5` s'attache au panneau AI.

> Vidéo : [ADV · Click sentence 5. Clip ships.](../videos/features/14-advanced-08-sentence-id.mp4)
> (30 s)

## 4.5 · Range select — juste un drag

Le plus courant. Drag de texte dans la preview → `selection_text` et
`selection_html` deviennent tous deux disponibles.

## ✅ Checkpoint Step 4

- Vous êtes entré en region paint avec ⌘Shift+R et avez dessiné un
  rectangle.
- La région dessinée s'est attachée comme cite anchor au panneau AI.
- Vous avez envoyé une phrase à l'AI et reçu un patch en retour (la
  réponse a un cite anchor *quelque part*).

Les trois ? → [Step 5 · command (terminal / chat / apply)](../05-command/)

## Pour aller plus loin

- [`../03-byom-setup/AI_GUIDE.md`](../03-byom-setup/AI_GUIDE.md) — les
  outils MCP (selection / region / element / cite).
- [`../05-command/personas/`](../05-command/personas/) — 26 walkthroughs
  de persona (chaque persona privilégie un pattern
  region/element/sentence-cite différent).
