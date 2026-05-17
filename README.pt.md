# HTMLook Campus

<p align="center">
  <a href="README.md">English</a> | <a href="README.ko.md">한국어</a> | <a href="README.ja.md">日本語</a> | <a href="README.de.md">Deutsch</a> | <a href="README.fr.md">Français</a> | <a href="README.es.md">Español</a> | <b>Português</b> | <a href="README.it.md">Italiano</a>
</p>

> Um **tutorial em 8 passos** para quem está começando com o HTMLook Pro.
> Seguindo os passos um a um, em 30–40 minutos você vai de instalação →
> primeiro arquivo → BYOM → edição → comandos → save-as-skill → perfis
> incluídos → escrever o seu próprio perfil.

Este repositório acompanha o **HTMLook Pro v1.0 release-candidate** (GA
previsto para meados de 2026). O app desktop está em
[htmlook.app](https://htmlook.app) — 14 dias de teste gratuito. BYOM
(Bring-Your-Own-Model) significa margem zero sobre tokens — Claude · GPT ·
Gemini · DeepSeek · Mistral · Together · Groq · Cerebras · Ollama, chame
qualquer modelo direto com a sua própria chave.

## Trilha do tutorial

De cima para baixo. Cada passo se apoia no anterior.

| Passo | Pasta | O que você faz | Tempo |
|---|---|---|---|
| 1 | [`01-getting-started/`](01-getting-started/) | instalação · primeira execução · drag-drop · abrir pasta | 3 min |
| 2 | [`02-first-file/`](02-first-file/) | md / html / pdf / vídeo — 4 tipos, split view, outline | 5 min |
| 3 | [`03-byom-setup/`](03-byom-setup/) | escolher um fornecedor e cadastrar a chave (ou Ollama) | 5 min |
| 4 | [`04-editing/`](04-editing/) | element pick · region paint · sentence-id · cite anchor | 5 min |
| 5 | [`05-command/`](05-command/) | chat · terminal CLI · apply_edit · 26 walkthroughs de personas | 10 min |
| 6 | [`06-save-as-skill/`](06-save-as-skill/) | capturar workflow → cartão de catálogo ⌘K | 5 min |
| 7 | [`07-bundled-profiles/`](07-bundled-profiles/) | HyperFrames · Slidev · Quarto · D2 · Astro Starlight · Marimo · Excalidraw · Manim | 5 min |
| 8 | [`08-extend/`](08-extend/) | escrever seu próprio perfil + PR no catálogo | opcional |

> Se quiser só uma visão rápida, o mapeamento passo → vídeo está em
> [`01-getting-started/LEARNING_PATH.md`](01-getting-started/LEARNING_PATH.md).
> Cada vídeo dura 30–70 segundos.

## Manual de referência (Wiki)

O tutorial de 8 passos mostra o fluxo *de ponta a ponta, uma vez*. O
[`wiki/`](wiki/) é o **manual de referência funcionalidade por
funcionalidade** ao qual você volta depois: Sidebar · Abas · Visualizador ·
Editor Markdown · PDF · Player de vídeo/áudio · Terminal · Assistente de IA ·
Paint · Notas de voz · Skill · Export · Ajustes · atalhos. Duas trilhas
paralelas — uma para usuários humanos, outra para assistentes de IA (MCP /
esquemas).

| Trilha | Entrada | Idiomas |
|---|---|---|
| Manual para humanos | [`wiki/Home.md`](wiki/Home.md) · [Coreano](wiki/Home-ko.md) | EN / KO |
| Guia para assistentes IA | [`wiki/AI-Overview.md`](wiki/AI-Overview.md) · [Coreano](wiki/AI-Overview-ko.md) | EN / KO |

O tutorial você percorre uma vez; o wiki fica ao alcance da mão todo dia
(abra no app via *Help → Documentation*).

## Edições

- **HTMLook Pro** (v1.0) — para power users. Chat BYOM + terminal PTY
  embutido + adaptadores CLI (claude / codex / gemini) + ponte MCP + canvas
  Paint + captura de região + seleção de elemento + save-as-skill + 8 perfis
  incluídos + 49 seeds.
- **HTMLook Easier** *(em breve)* — edição de entrada, em redefinição.

## Passo 1 — Instalação + primeira execução

Comece em [`01-getting-started/README.md`](01-getting-started/README.md).

Baixe o .dmg em [htmlook.app](https://htmlook.app), arraste para Applications
e faça drag-and-drop do seu primeiro arquivo.

## Passo 2 — Primeiro arquivo (HTML / MD / PDF / vídeo)

[`02-first-file/README.md`](02-first-file/README.md). Navegue quatro tipos
de arquivo com split view + outline + miniaturas.

Vídeos: BASIC #3 #4 #6 + ADV multi-pane / thumbnail / outline. Os mp4 estão
em [`videos/features/`](videos/features/).

## Passo 3 — Configurar BYOM (um único fornecedor)

[`03-byom-setup/README.md`](03-byom-setup/README.md). Para o guia de IA
detalhado: [`03-byom-setup/AI_GUIDE.md`](03-byom-setup/AI_GUIDE.md); um
exemplo de configuração para cliente MCP externo em
[`03-byom-setup/.htmlook/mcp-config.example.json`](03-byom-setup/.htmlook/mcp-config.example.json).

## Passo 4 — Apontar *para algo* na tela

[`04-editing/README.md`](04-editing/README.md). Quatro modos: element pick ·
region paint · sentence-id · range select. Vídeo-chave: BASIC #5 ⭐ region-cite
(o ponto de entrada da IA).

## Passo 5 — Modificar por comando (cite + apply_edit)

[`05-command/README.md`](05-command/README.md). A parte mais profunda do
campus — 26 walkthroughs de personas em
[`05-command/personas/`](05-command/personas/) (agrupados por papel, cada
pasta com um WALKTHROUGH.md de acompanhamento + before/after).

Catálogo de personas: [`05-command/personas/INDEX.md`](05-command/personas/INDEX.md).

## Passo 6 — Workflows recorrentes → Skills

[`06-save-as-skill/README.md`](06-save-as-skill/README.md). Painel de IA à
direita, diálogo *Save as Skill*. Três linhas e está pronto.

## Passo 7 — Os 8 perfis incluídos

[`07-bundled-profiles/README.md`](07-bundled-profiles/README.md). HyperFrames /
Slidev / Quarto / D2 / Astro Starlight / Marimo / Excalidraw / Manim. Os
seeds de perfil estão em [`profiles/`](profiles/) (o builder catalog.json lê
direto dali).

## Passo 8 — Escrever seu perfil + padrão de vídeo

[`08-extend/README.md`](08-extend/README.md). Monte um perfil para o seu
domínio e adicione no catálogo. O padrão de vídeo + procedimento de
reverse-verification estão em
[`08-extend/PRODUCTION.md`](08-extend/PRODUCTION.md); o catálogo dos 17
vídeos em [`08-extend/FEATURES.md`](08-extend/FEATURES.md).

## Localização dos assets (referência)

Ao lado das pastas de passo (01~08), a raiz do campus contém estes
*diretórios de assets compartilhados* (catalog.json + o app referenciam
por caminho, então não migram para pastas de passo):

| Pasta | Conteúdo |
|---|---|
| [`videos/`](videos/) | 17 mp4 de features + 26 mp4 de personas (~340 MB no total) |
| [`profiles/`](profiles/) | 8 seeds de perfil (`profile.json` + `SKILL.md` + `seed/`) |
| [`sample_workspaces/`](sample_workspaces/) | 75 seeds de domínio (`hf-*` 26 personas + 49 seeds de perfil) |
| [`catalog.json`](catalog.json) | 83 entradas (8 perfis + 75 seeds de workspace) — recarregado on-demand pelo Wizard do app (cache 24 h) |
| [`scripts/`](scripts/) | `build-catalog.mjs` |
| [`infra/`](infra/) | worker de licenças (serviço separado) |
| [`docs/`](docs/) | área de trabalho para artefatos gerados (gitignored) |

## Duas camadas de aprendizado — vídeo + interativo

Os vídeos do campus mostram o *o quê (o que é possível)*. O walkthrough
interativo embutido no HTMLook Pro (*Help → Interactive Tutorials…*) mostra
o *como (como fazer)*. Cada uma das 17 funcionalidades dos vídeos tem um
guia interativo correspondente, um para um.

| Camada | Onde | Duração | Papel |
|---|---|---|---|
| Vídeo (campus) | `videos/features/`, `videos/` | 30 s / 60–70 s | mostra o resultado |
| Interativo (app) | HTMLook Pro · Help → Interactive Tutorials… | 4 passos | prática ao vivo |

## Promessa de reverse-verification

Cada vídeo deste campus **só afirma coisas que o HTMLook realmente faz**.
Funcionalidades que não existem não são anunciadas. Procedimento de
verificação + lista de afirmações falsas corrigidas:
[`08-extend/PRODUCTION.md`](08-extend/PRODUCTION.md).

## Status

Este repositório acompanha o **HTMLook Pro v1.0 release-candidate** (GA
prevista para meados de 2026) como material didático vivo. Vira público
junto com o v1.0 GA, quando o endpoint de catálogo
(`htmlook.app/catalog`) passa a recarregar as URLs raw deste repo (cache
24 h).

## Licença

- Código / textos dos walkthroughs: MIT
- Vídeos mp4: CC BY 4.0 (atribuir *"HTMLook Campus"*)
- Conteúdo de exemplo (PDF / xlsx / md / html): CC0 / domínio público — todos placeholders fictícios
