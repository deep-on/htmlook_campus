# Step 6 · Save-as-Skill (capturar um workflow)

<p align="center">
  <a href="README.md">English</a> | <a href="README.ko.md">한국어</a> | <a href="README.ja.md">日本語</a> | <a href="README.de.md">Deutsch</a> | <a href="README.fr.md">Français</a> | <a href="README.es.md">Español</a> | <b>Português</b> | <a href="README.it.md">Italiano</a>
</p>

> O ciclo cite + apply_edit que você aprendeu no Step 5 — *o app
> guarda ele*. Da próxima vez, um clique e ele roda de novo.
> ~ 5 min.

No fim deste passo você terá uma ferramenta sua registrada no
workspace, aparecendo na seção *Tools* da sidebar (ou no quick
launcher ⌘K · Add wizard).

## 6.1 · *Save as Skill* — entrada

Quando sua última conversa LLM / ciclo apply_edit foi bom, clique no
*⋯* no topo do painel AI à direita → **Save as Skill**.

O diálogo pede três linhas:

| Campo | Exemplo |
|---|---|
| Name | *Tighten subtitle* |
| When to use | *quando o subtítulo está curto demais, esticar pra uma linha* |
| Default prompt | *Estica o subtítulo na região cite atual com o valor do Apex (edge compute, deploy rápido) e apply_edit* |

> Vídeo: [ADV · Add a tool. Three fields.](../videos/features/12-advanced-06-tool-wizard.mp4) (30 s)

## 6.2 · Onde fica

`.htmlook/skills/<name>.skill.json` (dentro do workspace, spec v0.3).
Compartilhe o workspace e seus colegas têm o skill também.

Pra usar em qualquer workspace — **Settings → Skills → Promote to
global**.

## 6.3 · Chamando pelo Add wizard

⌘K ou o *+* na sidebar → o catálogo mais seus skills aparecem como
cards. Clique num card → roda sozinho com o contexto de seleção
atual.

## 6.4 · Spec Skill v0.3 — o que tem dentro

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

`needs` / `produces` são nomes de ferramentas MCP. Spec completa no
repo principal do HTMLook em `docs/skills/v0.3.md` (público no v1.0
GA).

## 6.5 · Skill vs Profile

- **Skill** = captura de uma *ação* (um prompt + combinação de
  ferramentas). Local ao workspace ou user-global.
- **Profile** = bundle de *ferramentas + conteúdo seed + Skills*. v1.0
  traz 8 profiles ([Step 7](../07-bundled-profiles/)).

Como escrever seu próprio Profile está em [Step 8 · extend](../08-extend/).

## ✅ Checkpoint Step 6

- Você abriu o diálogo *Save as Skill* no painel AI à direita.
- Preencheu as três linhas e salvou um skill.
- O skill aparece como card no ⌘K — clique roda de novo.

Os três? → [Step 7 · bundled profiles](../07-bundled-profiles/)

## Mais a fundo

- [`../05-command/personas/`](../05-command/personas/) — imagine cada
  persona salva como skill. O padrão fica claro.
