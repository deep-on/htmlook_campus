# Step 5 · Command (Terminal / Chat / Apply)

<p align="center">
  <a href="README.md">English</a> | <a href="README.ko.md">한국어</a> | <a href="README.ja.md">日本語</a> | <a href="README.de.md">Deutsch</a> | <b>Français</b> | <a href="README.es.md">Español</a> | <a href="README.pt.md">Português</a> | <a href="README.it.md">Italiano</a>
</p>

> Le Step 4 vous a appris à pointer *où*. Cette étape transforme ça en
> *commandes*. Le cycle cite + apply_edit.
> ~ 10 min.

C'est la partie la plus profonde du campus — les 26 walkthroughs de
persona vivent ici ([`personas/`](personas/)). Au début, ne suivez que
celui de votre domaine.

## 5.1 · Quatre patterns de commande

| Pattern | Où | Forme d'entrée |
|---|---|---|
| **Chat (BYOM)** | Panneau AI à droite | langage naturel + cite anchor attaché automatiquement |
| **Terminal CLI** | Bascule ⌘J, lancez `claude` / `codex` / `gemini` | prompt shell |
| **Client MCP externe** | Claude Code / Cursor / Windsurf / Zed | la zone de chat de ce client |
| **Inline cite link** | un `[B14](xlsx://q3.xlsx#B14)` dans la réponse | clic → saut vers cet anchor |

## 5.2 · Le cycle cite + apply_edit

```
[choisir une zone via Step 4]
   → cite anchor s'attache au panneau AI
   → prompt en langage naturel
   → le LLM appelle htmlook_apply_edit
   → le fichier change
   → le file watcher recharge le pane droit automatiquement
```

Quatre vidéos d'ancrage (30 s chacune) :

| # | Vidéo | Pattern |
|---|---|---|
| 7 | [Cite the cell. Get the narrative.](../videos/features/07-advanced-01-xlsx-cite.mp4) | cite d'une cellule xlsx |
| 8 | [14:14 → paragraph.](../videos/features/08-advanced-02-live-cue-cite.mp4) | cite d'un timestamp vidéo |
| 9 | [One cite. Three files.](../videos/features/09-advanced-03-multi-target.mp4) | un cite → patches dans plusieurs fichiers |
| 17 | [Cross-file anchors. Recorded.](../videos/features/17-advanced-11-cross-link.mp4) | sidecar `.htmlook/links.json` |

## 5.3 · Walkthroughs de persona (26)

Un workflow *day-in-the-life* par rôle / domaine. mp4 de 60–70 s + un
sample workspace follow-along + un `WALKTHROUGH.md` pas à pas.

Catalogue complet : [`personas/INDEX.md`](personas/INDEX.md). L'ordre
recommandé est groupé par rôle :

- **Dev** : [`personas/01-hf-claude/`](personas/01-hf-claude/) →
  [`02-hf-llama/`](personas/02-hf-llama/) →
  [`03-dev-pr-docs/`](personas/03-dev-pr-docs/)
- **Contenu** : [`personas/04-creator-podcast/`](personas/04-creator-podcast/) →
  [`12-press-editor/`](personas/12-press-editor/) →
  [`15-picture-book/`](personas/15-picture-book/) →
  [`22-hobby-fiction/`](personas/22-hobby-fiction/)
- **Analyse** : [`personas/09-data-analyst/`](personas/09-data-analyst/) →
  [`11-finance-report/`](personas/11-finance-report/) →
  [`10-research-notes/`](personas/10-research-notes/) →
  [`06-economy-analyst/`](personas/06-economy-analyst/)
- **Juridique / traduction** : [`personas/08-legal-redline/`](personas/08-legal-redline/) →
  [`07-translator-book/`](personas/07-translator-book/) →
  [`05-domain-battery/`](personas/05-domain-battery/)
- **Éducation (enseignants)** : [`personas/17-teacher-quiz/`](personas/17-teacher-quiz/) →
  [`18-teacher-newsletter/`](personas/18-teacher-newsletter/) →
  [`19-teacher-record/`](personas/19-teacher-record/)
- **Éducation (élèves)** : [`personas/20-student-notes/`](personas/20-student-notes/) →
  [`24-student-flashcard/`](personas/24-student-flashcard/) →
  [`23-homework-helper/`](personas/23-homework-helper/) →
  [`21-kid-coding/`](personas/21-kid-coding/) →
  [`14-kids-science-mag/`](personas/14-kids-science-mag/)
- **Business** : [`personas/16-corp-deck/`](personas/16-corp-deck/) →
  [`13-product-prd/`](personas/13-product-prd/)
- **Quotidien** : [`personas/25-recipe-card/`](personas/25-recipe-card/) →
  [`26-mobile-news/`](personas/26-mobile-news/)

## 5.4 · Le pattern follow-along

Dans chaque dossier persona :

- `WALKTHROUGH.md` — pas à pas (marqueurs `[VIEW]` / `[AI]`)
- `before/` — état avant edit (comparaison visuelle)
- `after/` — état après edit (pour que les utilisateurs sans AI voient
  quand même le résultat)
- les fichiers de contenu de domaine (md / html / pdf / xlsx / svg / py
  / mp3 …)

## 5.5 · LLM-agnostique — vendor swap

Le même workflow cite + apply_edit tourne identique sur les 9
fournisseurs. Ajoutez-en un autre dans [Step 3](../03-byom-setup/) et
swappez — même résultat.

## ✅ Checkpoint Step 5

- Vous avez regardé une vidéo persona (60–70 s) proche de votre rôle.
- Vous avez suivi les étapes `[VIEW]` du `WALKTHROUGH.md`
  correspondant.
- (Si AI configurée) Vous avez exécuté les étapes `[AI]` → le pane
  droit s'est rechargé.
- (Sinon) Vous avez comparé `before/` vs `after/` en split view.

Tout ? → [Step 6 · save-as-skill](../06-save-as-skill/) — enregistrer
durablement un workflow récurrent dans l'app.

## Pour aller plus loin

- [`personas/INDEX.md`](personas/INDEX.md) — catalogue des 26 personas
  + mapping vidéo ↔ dossier.
- [`personas/README.md`](personas/README.md) — comment utiliser les
  sample workspaces.
- [`../03-byom-setup/AI_GUIDE.md`](../03-byom-setup/AI_GUIDE.md) — les
  ~22 outils MCP + le guide de ton des agents AI.
