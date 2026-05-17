# Step 8 · Extend (eigenes Profile schreiben + Katalog)

<p align="center">
  <a href="README.md">English</a> | <a href="README.ko.md">한국어</a> | <a href="README.ja.md">日本語</a> | <b>Deutsch</b> | <a href="README.fr.md">Français</a> | <a href="README.es.md">Español</a> | <a href="README.pt.md">Português</a> | <a href="README.it.md">Italiano</a>
</p>

> Der letzte der 8 Schritte. Wie du dein eigenes Profile schreibst und
> im Katalog einreichst.
> Open-ended (hängt davon ab, wie komplex das Tool ist).

Hier wechselt ein *Lernender* die Rolle zum *Contributor*. Nach v1.0
GA nehmen wir externe Profiles per PR in den Katalog auf.

## 8.1 · Was ist ein Profile

```
profiles/<id>/
├─ profile.json   ← manifest (id, name, category, description, tags, license)
├─ SKILL.md       ← Skill-v0.3-Bundle (die Tools, die das Profile registriert)
├─ README.md      ← Beschreibung für Menschen
└─ seed/          ← Seed-Content (wird beim Install zu den Nutzer:innen kopiert)
```

Beispiel: [`../profiles/hyperframes/`](../profiles/hyperframes/) (das
einfachste).

## 8.2 · Quick-Start — leeres Profile aufsetzen

```bash
cd /Users/vincent/Works/htmlook_campus/profiles
mkdir my-tool
cat > my-tool/profile.json <<'EOF'
{
  "id": "my-tool",
  "name": "My Tool",
  "category": "misc",
  "description": "Beschreibung in einer Zeile",
  "tags": ["mytool"],
  "license": "MIT"
}
EOF
mkdir my-tool/seed
echo "# seed example" > my-tool/seed/example.md
echo "# My Tool Profile" > my-tool/README.md
```

## 8.3 · SKILL.md — das Skill-v0.3-Bundle

```markdown
# My Tool Skills

## render

- prompt: Render den aktuellen Workspace mit my-tool
- needs: [active_file, workspace_files]
- produces: [apply_edit]
```

Volle Spec: `docs/skills/v0.3.md` im HTMLook-Haupt-Repo.

## 8.4 · Den Katalog bauen

```bash
node scripts/build-catalog.mjs > catalog.json
```

CI macht das bei jedem Push automatisch
(`.github/workflows/catalog.yml`). Wenn ein neuer Profile-Ordner
auftaucht, aktualisiert sich `entries[]` in `catalog.json` von selbst.

Builder-Quelle: [`../scripts/build-catalog.mjs`](../scripts/build-catalog.mjs).

## 8.5 · Seeds zu sample_workspaces/ hinzufügen

Zusätzlich zum Profile selbst kannst du domain-spezifische Seeds in
[`../sample_workspaces/`](../sample_workspaces/) ablegen, z. B.
`my-tool-marketing-page/`, `my-tool-api-docs/`.

Pack eine `.htmlook/workspace.json` in jeden Seed-Ordner und der
Katalog-Builder zieht `uses_profiles` / `category` / `description`
automatisch:

```json
{
  "profiles": { "my-tool": { "active": true } },
  "category": "marketing",
  "description": "Marketing-Page-Seed, gebaut mit My Tool"
}
```

## 8.6 · Video hinzufügen (optional)

Wenn du einen 60–70 s Walkthrough oder einen 30 s Feature-Spotlight
für dein Profile machen willst:

- Video-Standard + Reverse-Verification-Verfahren: [`PRODUCTION.md`](PRODUCTION.md)
- 17-Feature-Video-Katalog (Referenz): [`FEATURES.md`](FEATURES.md)
- Video-Build-Tool: [`../profiles/hyperframes/`](../profiles/hyperframes/)
  (der Campus selbst wird damit produziert)

## 8.7 · PR-Workflow

1. fork → eigenen Profile-Ordner hinzufügen.
2. `node scripts/build-catalog.mjs > catalog.json`.
3. PR aufmachen → der CI-Workflow `build catalog` validiert den
   Katalog automatisch.
4. Nach v1.0 GA reviewen und mergen wir.

## ✅ Step 8 Checkpoint

- Du hast ein Profile mit mkdir unter
  [`../profiles/`](../profiles/) angelegt.
- Minimum `profile.json` + `seed/` ist da.
- `node scripts/build-catalog.mjs` fügt einen neuen Eintrag in
  catalog.json hinzu — verifiziert.

Wenn du hier ankommst, hast du den 8-Step-Campus absolviert. Füg gerne
ein domain-spezifisches Profile dazu — der v1.0-GA-Katalog unter
[`htmlook.app/catalog`](https://htmlook.app/catalog) holt es sich
frisch.

## Reference

- [`PRODUCTION.md`](PRODUCTION.md) — Video-Produktionsstandard +
  Reverse-Verification-Verfahren + Untertitel-Mux-Rezept.
- [`FEATURES.md`](FEATURES.md) — 17-Feature-Video-Katalog (Hooks +
  Akzente).
- [`../scripts/build-catalog.mjs`](../scripts/build-catalog.mjs) —
  Quelle des Katalog-Builders.
- [`../catalog.json`](../catalog.json) — aktueller Katalog (8 Profile
  + 75 Seeds).
