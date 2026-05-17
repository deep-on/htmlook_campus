# Step 8 · Extend (escrever seu Profile + catálogo)

<p align="center">
  <a href="README.md">English</a> | <a href="README.ko.md">한국어</a> | <a href="README.ja.md">日本語</a> | <a href="README.de.md">Deutsch</a> | <a href="README.fr.md">Français</a> | <a href="README.es.md">Español</a> | <b>Português</b> | <a href="README.it.md">Italiano</a>
</p>

> O último dos 8 passos. Como escrever seu próprio profile e
> registrar no catálogo.
> Sem prazo (depende da complexidade da ferramenta sobre a qual você
> escreve).

Este passo é onde um *aprendiz* vira *contribuidor*. Depois da v1.0 GA
vamos aceitar profiles de terceiros no catálogo via PR.

## 8.1 · O que é um Profile

```
profiles/<id>/
├─ profile.json   ← manifest (id, name, category, description, tags, license)
├─ SKILL.md       ← bundle Skill v0.3 (as ferramentas que esse profile registra)
├─ README.md      ← descrição pra humanos
└─ seed/          ← conteúdo seed (copiado pro usuário no install)
```

Amostra: [`../profiles/hyperframes/`](../profiles/hyperframes/) (o
mais simples).

## 8.2 · Início rápido — scaffold de profile vazio

```bash
cd /Users/vincent/Works/htmlook_campus/profiles
mkdir my-tool
cat > my-tool/profile.json <<'EOF'
{
  "id": "my-tool",
  "name": "My Tool",
  "category": "misc",
  "description": "descrição de uma linha",
  "tags": ["mytool"],
  "license": "MIT"
}
EOF
mkdir my-tool/seed
echo "# seed example" > my-tool/seed/example.md
echo "# My Tool Profile" > my-tool/README.md
```

## 8.3 · SKILL.md — o bundle Skill v0.3

```markdown
# My Tool Skills

## render

- prompt: renderiza o workspace atual com my-tool
- needs: [active_file, workspace_files]
- produces: [apply_edit]
```

Spec completa: `docs/skills/v0.3.md` no repo principal do HTMLook.

## 8.4 · Construir o catálogo

```bash
node scripts/build-catalog.mjs > catalog.json
```

O CI roda isso sozinho a cada push (`.github/workflows/catalog.yml`).
Quando aparece uma pasta de profile nova, `entries[]` no
`catalog.json` atualiza solo.

Fonte do builder: [`../scripts/build-catalog.mjs`](../scripts/build-catalog.mjs).

## 8.5 · Adicionar seeds em sample_workspaces/

Além do profile em si, dá pra largar seeds específicos de domínio em
[`../sample_workspaces/`](../sample_workspaces/), ex.
`my-tool-marketing-page/`, `my-tool-api-docs/`.

Coloque um `.htmlook/workspace.json` em cada pasta seed e o builder do
catálogo extrai `uses_profiles` / `category` / `description` sozinho:

```json
{
  "profiles": { "my-tool": { "active": true } },
  "category": "marketing",
  "description": "Seed de página de marketing feita com My Tool"
}
```

## 8.6 · Adicionar vídeo (opcional)

Se quiser entregar um walkthrough de 60–70 s ou um feature spotlight
de 30 s pro seu profile:

- Padrão de vídeo + procedimento de reverse-verification: [`PRODUCTION.md`](PRODUCTION.md)
- Catálogo dos 17 vídeos de feature (referência): [`FEATURES.md`](FEATURES.md)
- Ferramenta de build de vídeo: [`../profiles/hyperframes/`](../profiles/hyperframes/)
  (o próprio campus é feito com essa ferramenta)

## 8.7 · Workflow de PR

1. fork → adicione sua pasta de profile.
2. `node scripts/build-catalog.mjs > catalog.json`.
3. Abra um PR → o workflow CI `build catalog` valida o catálogo
   sozinho.
4. Depois da v1.0 GA fazemos review e merge.

## ✅ Checkpoint Step 8

- Você fez mkdir de um profile em [`../profiles/`](../profiles/).
- Mínimo `profile.json` + `seed/` no lugar.
- `node scripts/build-catalog.mjs` adiciona uma entrada nova no
  catalog.json — verificado.

Chegando aqui, você completou o campus 8-step. Adiciona um profile
do seu domínio — o catálogo v1.0-GA em
[`htmlook.app/catalog`](https://htmlook.app/catalog) recarrega ele on
demand.

## Reference

- [`PRODUCTION.md`](PRODUCTION.md) — padrão de produção de vídeo +
  procedimento de reverse-verification + receita de mux de legendas.
- [`FEATURES.md`](FEATURES.md) — catálogo dos 17 vídeos de feature
  (hooks + acentos).
- [`../scripts/build-catalog.mjs`](../scripts/build-catalog.mjs) —
  fonte do builder de catálogo.
- [`../catalog.json`](../catalog.json) — catálogo atual (8 profile +
  75 seed).
