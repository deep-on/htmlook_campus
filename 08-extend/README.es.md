# Step 8 · Extend (escribir tu Profile + catálogo)

<p align="center">
  <a href="README.md">English</a> | <a href="README.ko.md">한국어</a> | <a href="README.ja.md">日本語</a> | <a href="README.de.md">Deutsch</a> | <a href="README.fr.md">Français</a> | <b>Español</b> | <a href="README.pt.md">Português</a> | <a href="README.it.md">Italiano</a>
</p>

> El último de los 8 pasos. Cómo escribir tu propio profile y
> registrarlo en el catálogo.
> Sin límite de tiempo (depende de la complejidad de la herramienta
> sobre la que escribes).

Este paso es donde un *aprendiz* pasa a *contribuidor*. Tras v1.0 GA
aceptaremos profiles de terceros en el catálogo vía PR.

## 8.1 · Qué es un Profile

```
profiles/<id>/
├─ profile.json   ← manifest (id, name, category, description, tags, license)
├─ SKILL.md       ← bundle Skill v0.3 (las herramientas que registra el profile)
├─ README.md      ← descripción legible
└─ seed/          ← contenido seed (se copia al usuario al instalar)
```

Ejemplo: [`../profiles/hyperframes/`](../profiles/hyperframes/) (el
más simple).

## 8.2 · Inicio rápido — scaffold de un profile vacío

```bash
cd /Users/vincent/Works/htmlook_campus/profiles
mkdir my-tool
cat > my-tool/profile.json <<'EOF'
{
  "id": "my-tool",
  "name": "My Tool",
  "category": "misc",
  "description": "una línea de descripción",
  "tags": ["mytool"],
  "license": "MIT"
}
EOF
mkdir my-tool/seed
echo "# seed example" > my-tool/seed/example.md
echo "# My Tool Profile" > my-tool/README.md
```

## 8.3 · SKILL.md — el bundle Skill v0.3

```markdown
# My Tool Skills

## render

- prompt: renderiza el workspace actual con my-tool
- needs: [active_file, workspace_files]
- produces: [apply_edit]
```

Spec completa: `docs/skills/v0.3.md` en el repo principal de HTMLook.

## 8.4 · Construir el catálogo

```bash
node scripts/build-catalog.mjs > catalog.json
```

CI lo corre solo en cada push (`.github/workflows/catalog.yml`).
Cuando aparece una carpeta de profile nueva, `entries[]` en
`catalog.json` se actualiza solo.

Fuente del builder: [`../scripts/build-catalog.mjs`](../scripts/build-catalog.mjs).

## 8.5 · Añadir seeds a sample_workspaces/

Encima del profile en sí, puedes meter seeds específicos de dominio
bajo [`../sample_workspaces/`](../sample_workspaces/), p. ej.
`my-tool-marketing-page/`, `my-tool-api-docs/`.

Pon un `.htmlook/workspace.json` en cada carpeta seed y el builder del
catálogo extrae `uses_profiles` / `category` / `description`
automáticamente:

```json
{
  "profiles": { "my-tool": { "active": true } },
  "category": "marketing",
  "description": "Seed de marketing page hecha con My Tool"
}
```

## 8.6 · Añadir vídeo (opcional)

Si quieres entregar un walkthrough de 60–70 s o un feature spotlight
de 30 s para tu profile:

- Estándar de vídeo + procedimiento de reverse-verification: [`PRODUCTION.md`](PRODUCTION.md)
- Catálogo de los 17 vídeos de funciones (referencia): [`FEATURES.md`](FEATURES.md)
- Herramienta de build de vídeo: [`../profiles/hyperframes/`](../profiles/hyperframes/)
  (el propio campus se produce con esta herramienta)

## 8.7 · Workflow de PR

1. fork → añade tu carpeta de profile.
2. `node scripts/build-catalog.mjs > catalog.json`.
3. Abre un PR → el workflow CI `build catalog` valida el catálogo
   solo.
4. Tras v1.0 GA hacemos review y merge.

## ✅ Checkpoint Step 8

- Has hecho mkdir de un profile en [`../profiles/`](../profiles/).
- Mínimo `profile.json` + `seed/` en su sitio.
- `node scripts/build-catalog.mjs` añade una entrada nueva al
  catalog.json — verificado.

Si has llegado aquí, has completado el campus 8-step. Añade un profile
de tu dominio — el catálogo v1.0-GA en
[`htmlook.app/catalog`](https://htmlook.app/catalog) lo recarga al
vuelo.

## Reference

- [`PRODUCTION.md`](PRODUCTION.md) — estándar de producción de vídeo +
  procedimiento de reverse-verification + receta de mux de subtítulos.
- [`FEATURES.md`](FEATURES.md) — catálogo de los 17 vídeos de
  funciones (hooks + acentos).
- [`../scripts/build-catalog.mjs`](../scripts/build-catalog.mjs) —
  fuente del builder de catálogo.
- [`../catalog.json`](../catalog.json) — catálogo actual (8 profile +
  75 seed).
