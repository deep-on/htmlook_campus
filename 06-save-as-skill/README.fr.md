# Step 6 · Save-as-Skill (capturer un workflow)

<p align="center">
  <a href="README.md">English</a> | <a href="README.ko.md">한국어</a> | <a href="README.ja.md">日本語</a> | <a href="README.de.md">Deutsch</a> | <b>Français</b> | <a href="README.es.md">Español</a> | <a href="README.pt.md">Português</a> | <a href="README.it.md">Italiano</a>
</p>

> Le cycle cite + apply_edit appris au Step 5 — *l'app le retient*. La
> prochaine fois, un clic le relance.
> ~ 5 min.

À la fin de cette étape vous aurez un outil bien à vous, enregistré
dans le workspace et visible dans la section *Tools* de la sidebar (ou
dans le quick launcher ⌘K · Add wizard).

## 6.1 · *Save as Skill* — entrée

Si votre dernier échange LLM / cycle apply_edit s'est bien passé,
cliquez sur le *⋯* en haut du panneau AI à droite → **Save as Skill**.

Le dialogue demande trois lignes :

| Champ | Exemple |
|---|---|
| Name | *Tighten subtitle* |
| When to use | *quand un sous-titre est trop court, l'étendre à une ligne* |
| Default prompt | *Étendre le sous-titre de la région cite courante avec la valeur d'Apex (edge compute, déploiement rapide) et apply_edit* |

> Vidéo : [ADV · Add a tool. Three fields.](../videos/features/12-advanced-06-tool-wizard.mp4) (30 s)

## 6.2 · Où ça vit

`.htmlook/skills/<name>.skill.json` (dans le workspace, spec v0.3).
Partagez le workspace et vos collègues l'ont aussi.

Pour l'utiliser partout (tous les workspaces) — **Settings → Skills →
Promote to global**.

## 6.3 · L'appeler depuis l'Add wizard

⌘K ou le *+* dans la sidebar → le catalogue plus vos skills
apparaissent en cartes. Clic sur une carte → exécution automatique
avec le contexte de sélection en cours.

## 6.4 · Spec Skill v0.3 — ce qu'il y a dedans

```json
{
  "name": "tighten-subtitle",
  "version": "0.3",
  "description": "...",
  "default_prompt": "...",
  "needs": ["selection_html", "active_file"],
  "produces": ["apply_edit"]
}
```

`needs` / `produces` sont des noms d'outils MCP. Spec complète dans le
repo principal HTMLook à `docs/skills/v0.3.md` (publié à v1.0 GA).

## 6.5 · Skill vs Profile

- **Skill** = capture d'une *action* (un prompt + une combinaison
  d'outils). Workspace-local ou user-global.
- **Profile** = un bundle d'*outils + contenu seed + Skills*. v1.0
  livre 8 profiles ([Step 7](../07-bundled-profiles/)).

Pour écrire votre propre Profile, voir
[Step 8 · extend](../08-extend/).

## ✅ Checkpoint Step 6

- Vous avez ouvert le dialogue *Save as Skill* dans le panneau AI à
  droite.
- Vous avez rempli les trois lignes et sauvegardé un skill.
- Le skill apparaît en carte dans ⌘K — clic le relance.

Les trois ? → [Step 7 · bundled profiles](../07-bundled-profiles/)

## Pour aller plus loin

- [`../05-command/personas/`](../05-command/personas/) — imaginez
  chaque persona sauvée en skill. Le pattern devient évident.
