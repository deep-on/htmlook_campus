# Step 8 · Extend (scrivere il proprio Profile + catalogo)

<p align="center">
  <a href="README.md">English</a> | <a href="README.ko.md">한국어</a> | <a href="README.ja.md">日本語</a> | <a href="README.de.md">Deutsch</a> | <a href="README.fr.md">Français</a> | <a href="README.es.md">Español</a> | <a href="README.pt.md">Português</a> | <b>Italiano</b>
</p>

> L'ultimo degli 8 step. Come scrivere il proprio profile e
> registrarlo nel catalogo.
> Tempo libero (dipende dalla complessità dello strumento per cui
> scrivi).

Questo step è dove un *learner* diventa *contributor*. Dopo la v1.0
GA accetteremo profile di terze parti nel catalogo via PR.

## 8.1 · Cos'è un Profile

```
profiles/<id>/
├─ profile.json   ← manifest (id, name, category, description, tags, license)
├─ SKILL.md       ← bundle Skill v0.3 (gli strumenti che il profile registra)
├─ README.md      ← descrizione leggibile
└─ seed/          ← contenuto seed (copiato all'utente in install)
```

Esempio: [`../profiles/hyperframes/`](../profiles/hyperframes/) (il
più semplice).

## 8.2 · Avvio rapido — scaffold di un profile vuoto

```bash
cd /Users/vincent/Works/htmlook_campus/profiles
mkdir my-tool
cat > my-tool/profile.json <<'EOF'
{
  "id": "my-tool",
  "name": "My Tool",
  "category": "misc",
  "description": "una riga di descrizione",
  "tags": ["mytool"],
  "license": "MIT"
}
EOF
mkdir my-tool/seed
echo "# seed example" > my-tool/seed/example.md
echo "# My Tool Profile" > my-tool/README.md
```

## 8.3 · SKILL.md — il bundle Skill v0.3

```markdown
# My Tool Skills

## render

- prompt: renderizza il workspace corrente con my-tool
- needs: [active_file, workspace_files]
- produces: [apply_edit]
```

Spec completa: `docs/skills/v0.3.md` nel repo principale di HTMLook.

## 8.4 · Costruire il catalogo

```bash
node scripts/build-catalog.mjs > catalog.json
```

Il CI lo lancia ad ogni push (`.github/workflows/catalog.yml`).
Quando spunta una cartella di profile nuova, `entries[]` in
`catalog.json` si aggiorna da solo.

Sorgente del builder: [`../scripts/build-catalog.mjs`](../scripts/build-catalog.mjs).

## 8.5 · Aggiungere seed a sample_workspaces/

Oltre al profile stesso, puoi mettere seed di dominio specifici sotto
[`../sample_workspaces/`](../sample_workspaces/), es.
`my-tool-marketing-page/`, `my-tool-api-docs/`.

Lascia un `.htmlook/workspace.json` in ogni cartella seed e il
builder del catalogo estrae `uses_profiles` / `category` /
`description` da solo:

```json
{
  "profiles": { "my-tool": { "active": true } },
  "category": "marketing",
  "description": "Seed di pagina marketing fatto con My Tool"
}
```

## 8.6 · Aggiungere un video (opzionale)

Se vuoi consegnare un walkthrough da 60–70 s o un feature spotlight
da 30 s per il tuo profile:

- Standard video + procedura di reverse-verification: [`PRODUCTION.md`](PRODUCTION.md)
- Catalogo dei 17 video di feature (riferimento): [`FEATURES.md`](FEATURES.md)
- Strumento di build video: [`../profiles/hyperframes/`](../profiles/hyperframes/)
  (il campus stesso è prodotto con questo strumento)

## 8.7 · Workflow di PR

1. fork → aggiungi la tua cartella di profile.
2. `node scripts/build-catalog.mjs > catalog.json`.
3. Apri una PR → il workflow CI `build catalog` valida il catalogo
   da solo.
4. Dopo la v1.0 GA facciamo review e merge.

## ✅ Checkpoint Step 8

- Hai fatto mkdir di un profile sotto [`../profiles/`](../profiles/).
- Minimo `profile.json` + `seed/` al loro posto.
- `node scripts/build-catalog.mjs` aggiunge una voce nuova in
  catalog.json — verificato.

Se sei arrivato qui, hai chiuso il campus 8-step. Aggiungi un profile
specifico per il tuo dominio — il catalogo v1.0-GA su
[`htmlook.app/catalog`](https://htmlook.app/catalog) lo ricarica
on-the-fly.

## Reference

- [`PRODUCTION.md`](PRODUCTION.md) — standard di produzione video +
  procedura di reverse-verification + ricetta di mux dei sottotitoli.
- [`FEATURES.md`](FEATURES.md) — catalogo dei 17 video di feature
  (hook + accenti).
- [`../scripts/build-catalog.mjs`](../scripts/build-catalog.mjs) —
  sorgente del builder del catalogo.
- [`../catalog.json`](../catalog.json) — catalogo attuale (8 profile
  + 75 seed).
