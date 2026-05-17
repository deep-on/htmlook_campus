# Step 8 · Extend (write your own Profile + catalog)

<p align="center">
  <b>English</b> | <a href="README.ko.md">한국어</a> | <a href="README.ja.md">日本語</a> | <a href="README.de.md">Deutsch</a> | <a href="README.fr.md">Français</a> | <a href="README.es.md">Español</a> | <a href="README.pt.md">Português</a> | <a href="README.it.md">Italiano</a>
</p>

> The last of the 8 steps. How to write your own Profile and register
> it in the catalog.
> Open-ended (depends on the complexity of the tool you're writing for).

This step is where a *learner* turns into a *contributor*. After v1.0
GA we'll accept third-party profiles into the catalog via PR.

## 8.1 · What is a Profile

```
profiles/<id>/
├─ profile.json   ← manifest (id, name, category, description, tags, license)
├─ SKILL.md       ← Skill v0.3 bundle (the tools this profile registers)
├─ README.md      ← human-readable description
└─ seed/          ← seed content (copied to the user on install)
```

Sample: [`../profiles/hyperframes/`](../profiles/hyperframes/) (the
simplest).

## 8.2 · Quick start — scaffold an empty profile

```bash
cd /Users/vincent/Works/htmlook_campus/profiles
mkdir my-tool
cat > my-tool/profile.json <<'EOF'
{
  "id": "my-tool",
  "name": "My Tool",
  "category": "misc",
  "description": "one-line description",
  "tags": ["mytool"],
  "license": "MIT"
}
EOF
mkdir my-tool/seed
echo "# seed example" > my-tool/seed/example.md
echo "# My Tool Profile" > my-tool/README.md
```

## 8.3 · SKILL.md — the Skill v0.3 bundle

```markdown
# My Tool Skills

## render

- prompt: render the current workspace with my-tool
- needs: [active_file, workspace_files]
- produces: [apply_edit]
```

Full spec: `docs/skills/v0.3.md` in the HTMLook main repo.

## 8.4 · Building the catalog

```bash
node scripts/build-catalog.mjs > catalog.json
```

CI runs this automatically on every push
(`.github/workflows/catalog.yml`). When a new profile folder is added,
`entries[]` in `catalog.json` updates by itself.

Builder source: [`../scripts/build-catalog.mjs`](../scripts/build-catalog.mjs).

## 8.5 · Adding seeds to sample_workspaces/

On top of the profile itself, you can add domain-specific extra seeds
under [`../sample_workspaces/`](../sample_workspaces/), e.g.
`my-tool-marketing-page/`, `my-tool-api-docs/`.

Drop a `.htmlook/workspace.json` in each seed folder and the catalog
builder pulls `uses_profiles` / `category` / `description` from it
automatically:

```json
{
  "profiles": { "my-tool": { "active": true } },
  "category": "marketing",
  "description": "A marketing-page seed produced with My Tool"
}
```

## 8.6 · Adding a video (optional)

If you want to ship a 60–70 s walkthrough or a 30 s feature spotlight
for your profile:

- Video standard + reverse-verification procedure: [`PRODUCTION.md`](PRODUCTION.md)
- 17-feature video catalog (reference): [`FEATURES.md`](FEATURES.md)
- Video build tool: [`../profiles/hyperframes/`](../profiles/hyperframes/)
  (the campus itself is produced with this tool)

## 8.7 · PR workflow

1. fork → add your profile folder.
2. `node scripts/build-catalog.mjs > catalog.json`.
3. Open a PR → CI's `build catalog` workflow validates the catalog
   automatically.
4. After v1.0 GA we review and merge.

## ✅ Step 8 checkpoint

- You've mkdir'd a profile under [`../profiles/`](../profiles/).
- Minimum `profile.json` + `seed/` in place.
- `node scripts/build-catalog.mjs` adds a new entry to catalog.json —
  verified.

If you got here, you've finished the 8-step campus. Please add a
domain-specific profile — the v1.0-GA catalog at
[`htmlook.app/catalog`](https://htmlook.app/catalog) fresh-fetches it.

## Reference

- [`PRODUCTION.md`](PRODUCTION.md) — video production standard +
  reverse-verification procedure + subtitle-mux recipe.
- [`FEATURES.md`](FEATURES.md) — 17-feature video catalog (hooks +
  accents).
- [`../scripts/build-catalog.mjs`](../scripts/build-catalog.mjs) —
  catalog builder source.
- [`../catalog.json`](../catalog.json) — current catalog (8 profile +
  75 seed).
