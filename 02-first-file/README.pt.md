# Step 2 · Primeiro arquivo (HTML / Markdown / PDF / vídeo)

<p align="center">
  <a href="README.md">English</a> | <a href="README.ko.md">한국어</a> | <a href="README.ja.md">日本語</a> | <a href="README.de.md">Deutsch</a> | <a href="README.fr.md">Français</a> | <a href="README.es.md">Español</a> | <b>Português</b> | <a href="README.it.md">Italiano</a>
</p>

> Aprenda o coração do *viewer* do HTMLook. A parte que já vale a pena
> sem AI / MCP.
> ~ 5 min.

No fim deste passo: você sabe ler cada um dos quatro tipos de arquivo
(md / html / pdf / vídeo) e navegar por eles com split view, preview e
outline.

## 2.1 · Markdown — edição ao vivo

1. Duplo clique em qualquer `.md` na sidebar (ex.
   [`../05-command/personas/03-dev-pr-docs/docs.md`](../05-command/personas/03-dev-pr-docs/docs.md)).
2. ⌘\\ ou menu *View → Split* alterna a split view.
3. Source à esquerda, preview à direita. Você digita à esquerda e a
   direita atualiza ao vivo.

> Vídeo: [BASIC #3 · Type left. See right. Live.](../videos/features/03-basic-03-md-live-edit.mp4) (30 s)

## 2.2 · HTML — clique no elemento para editar

1. Duplo clique em um `.html` (ex.
   [`../05-command/personas/01-hf-claude/landing.html`](../05-command/personas/01-hf-claude/landing.html)).
2. Modo padrão é preview. Em split view, clique direto em um elemento →
   um editor de texto aparece.
3. Sync bidirecional — mudanças no preview pousam no source na hora.

> Vídeo: [BASIC #4 · Click anything. Edit it.](../videos/features/04-basic-04-html-split.mp4) (30 s)

## 2.3 · HTML — quatro modos de seleção

No mesmo arquivo HTML, ⌘E roda pelos quatro modos de seleção:

| Modo | O que pega |
|---|---|
| element | um único nó DOM |
| range | uma faixa de texto |
| region | um retângulo pintado |
| outline | a árvore de cabeçalhos |

Vídeo: [BASIC #6 · Pick what you see.](../videos/features/06-basic-06-html-4mode.mp4) (30 s)

O que cada modo captura vira o ponto de entrada de cite-anchor em
[Step 4 · editing](../04-editing/).

## 2.4 · PDF — páginas + camada de texto

1. Duplo clique em qualquer `.pdf` (ex.
   [`../05-command/personas/05-domain-battery/vendor.pdf`](../05-command/personas/05-domain-battery/vendor.pdf)).
2. Navegador de miniaturas à esquerda + canvas de página à direita +
   camada de texto selecionável.
3. Drag-select numa região → region cite (usado em Step 4).

## 2.5 · Vídeo — miniaturas de frame + outline

1. Duplo clique em qualquer mp4 (ex.
   [`../videos/features/01-basic-01-drop-open.mp4`](../videos/features/01-basic-01-drop-open.mp4)).
2. O viewer de vídeo mostra timeline com previews em miniatura.
3. ⌘Shift+T ou hover te dá um preview de 1 s no frame (sem scrubbing).

> Vídeo: [ADV · Frame check. No scrub.](../videos/features/15-advanced-09-thumbnail.mp4) (30 s, categoria advanced)

## 2.6 · Outline — navegando um documento longo

A estrutura de cabeçalhos de qualquer md / html / PDF longo → aba
Outline no painel direito. Clique num cabeçalho e pula pra lá.

> Vídeo: [ADV · Click §3.2. You're there.](../videos/features/16-advanced-10-outline.mp4) (30 s)

## 2.7 · Split view / multi-pane (⌘1 / ⌘2 / ⌘3 / ⌘J)

| Atalho | Efeito |
|---|---|
| ⌘1 | Só preview |
| ⌘2 | Só source |
| ⌘3 | Split (preview + source) |
| ⌘J | Alterna o painel terminal |

Vídeo: [ADV · Two keys. Three views.](../videos/features/10-advanced-04-multi-pane.mp4)
(30 s — o *"Two keys"* da narração era ⌘D + ⌘J no corte original e foi
corrigido para ⌘1/⌘2/⌘3 + ⌘J na v1.0. Histórico completo em
[`../08-extend/PRODUCTION.md`](../08-extend/PRODUCTION.md), tabela
*fixed false claims*.)

## ✅ Checkpoint Step 2

- Você abriu uma md / html / pdf / vídeo, cada uma em split view.
- Sentiu a diferença entre os quatro modos HTML (element / range /
  region / outline) clicando direto.
- ⌘1 / ⌘2 / ⌘3 / ⌘J pra alternar o layout virou reflexo.

Os três? → [Step 3 · BYOM setup](../03-byom-setup/) — escolha um
fornecedor e registre uma chave.
