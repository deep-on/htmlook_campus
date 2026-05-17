# Step 8 · Extend (écrire son Profile + catalogue)

<p align="center">
  <a href="README.md">English</a> | <a href="README.ko.md">한국어</a> | <a href="README.ja.md">日本語</a> | <a href="README.de.md">Deutsch</a> | <b>Français</b> | <a href="README.es.md">Español</a> | <a href="README.pt.md">Português</a> | <a href="README.it.md">Italiano</a>
</p>

> La dernière des 8 étapes. Comment écrire votre propre profile et le
> faire enregistrer au catalogue.
> Durée libre (selon la complexité de l'outil que vous visez).

C'est ici qu'un *apprenant* devient *contributeur*. Après la v1.0 GA,
nous accepterons des profiles tiers dans le catalogue via PR.

## 8.1 · Qu'est-ce qu'un Profile

```
profiles/<id>/
├─ profile.json   ← manifest (id, name, category, description, tags, license)
├─ SKILL.md       ← bundle Skill v0.3 (les outils que ce profile enregistre)
├─ README.md      ← description pour les humains
└─ seed/          ← contenu seed (copié chez l'utilisateur à l'install)
```

Exemple : [`../profiles/hyperframes/`](../profiles/hyperframes/) (le
plus simple).

## 8.2 · Démarrage rapide — scaffold un profile vide

```bash
cd /Users/vincent/Works/htmlook_campus/profiles
mkdir my-tool
cat > my-tool/profile.json <<'EOF'
{
  "id": "my-tool",
  "name": "My Tool",
  "category": "misc",
  "description": "une ligne de description",
  "tags": ["mytool"],
  "license": "MIT"
}
EOF
mkdir my-tool/seed
echo "# seed example" > my-tool/seed/example.md
echo "# My Tool Profile" > my-tool/README.md
```

## 8.3 · SKILL.md — le bundle Skill v0.3

```markdown
# My Tool Skills

## render

- prompt: rends le workspace courant avec my-tool
- needs: [active_file, workspace_files]
- produces: [apply_edit]
```

Spec complète : `docs/skills/v0.3.md` dans le repo principal HTMLook.

## 8.4 · Construire le catalogue

```bash
node scripts/build-catalog.mjs > catalog.json
```

Le CI le lance à chaque push (`.github/workflows/catalog.yml`). Quand
un nouveau dossier de profile apparaît, `entries[]` dans
`catalog.json` se met à jour tout seul.

Source du builder : [`../scripts/build-catalog.mjs`](../scripts/build-catalog.mjs).

## 8.5 · Ajouter des seeds à sample_workspaces/

En plus du profile lui-même, vous pouvez déposer des seeds
spécifiques à votre domaine sous
[`../sample_workspaces/`](../sample_workspaces/), par ex.
`my-tool-marketing-page/`, `my-tool-api-docs/`.

Posez un `.htmlook/workspace.json` dans chaque dossier seed et le
builder du catalogue extrait `uses_profiles` / `category` /
`description` automatiquement :

```json
{
  "profiles": { "my-tool": { "active": true } },
  "category": "marketing",
  "description": "Un seed de page marketing fait avec My Tool"
}
```

## 8.6 · Ajouter une vidéo (optionnel)

Si vous voulez livrer un walkthrough de 60–70 s ou un feature
spotlight de 30 s pour votre profile :

- Standard vidéo + procédure de reverse-verification : [`PRODUCTION.md`](PRODUCTION.md)
- Catalogue des 17 vidéos de fonctionnalités (référence) : [`FEATURES.md`](FEATURES.md)
- Outil de build vidéo : [`../profiles/hyperframes/`](../profiles/hyperframes/)
  (le campus lui-même est produit avec cet outil)

## 8.7 · Workflow PR

1. fork → ajoutez votre dossier profile.
2. `node scripts/build-catalog.mjs > catalog.json`.
3. Ouvrez une PR → le workflow CI `build catalog` valide
   automatiquement le catalogue.
4. Après v1.0 GA, nous reviewons et mergeons.

## ✅ Checkpoint Step 8

- Vous avez mkdir un profile sous [`../profiles/`](../profiles/).
- Minimum `profile.json` + `seed/` en place.
- `node scripts/build-catalog.mjs` ajoute une entrée dans catalog.json
  — vérifié.

Arrivé là, vous avez bouclé le campus 8-step. Ajoutez un profile
spécifique à votre domaine — le catalogue v1.0-GA à
[`htmlook.app/catalog`](https://htmlook.app/catalog) le recharge à
chaud.

## Reference

- [`PRODUCTION.md`](PRODUCTION.md) — standard de production vidéo +
  procédure de reverse-verification + recette de mux des sous-titres.
- [`FEATURES.md`](FEATURES.md) — catalogue des 17 vidéos de
  fonctionnalités (hooks + accents).
- [`../scripts/build-catalog.mjs`](../scripts/build-catalog.mjs) —
  source du builder de catalogue.
- [`../catalog.json`](../catalog.json) — catalogue courant (8 profile
  + 75 seed).
