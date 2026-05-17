# Step 5 · Command (Terminal / Chat / Apply)

<p align="center">
  <a href="README.md">English</a> | <a href="README.ko.md">한국어</a> | <a href="README.ja.md">日本語</a> | <a href="README.de.md">Deutsch</a> | <a href="README.fr.md">Français</a> | <a href="README.es.md">Español</a> | <b>Português</b> | <a href="README.it.md">Italiano</a>
</p>

> O Step 4 te ensinou a apontar *onde*. Este passo transforma isso em
> *comandos*. O ciclo cite + apply_edit.
> ~ 10 min.

A parte mais profunda do campus — os 26 walkthroughs de persona moram
aqui ([`personas/`](personas/)). No começo, siga só o do seu domínio.

## 5.1 · Quatro padrões de comando

| Padrão | Onde | Formato de entrada |
|---|---|---|
| **Chat (BYOM)** | Painel AI à direita | linguagem natural + cite anchor anexado sozinho |
| **Terminal CLI** | Alterne ⌘J, rode `claude` / `codex` / `gemini` | prompt de shell |
| **Cliente MCP externo** | Claude Code / Cursor / Windsurf / Zed | o chat desse cliente |
| **Inline cite link** | um `[B14](xlsx://q3.xlsx#B14)` na resposta | clique → pula pra esse anchor |

## 5.2 · O ciclo cite + apply_edit

```
[escolha uma área no Step 4]
   → o cite anchor anexa ao painel AI
   → prompt em linguagem natural
   → o LLM chama htmlook_apply_edit
   → o arquivo muda
   → o file watcher recarrega o pane direito sozinho
```

Quatro vídeos âncora (30 s cada):

| # | Vídeo | Padrão |
|---|---|---|
| 7 | [Cite the cell. Get the narrative.](../videos/features/07-advanced-01-xlsx-cite.mp4) | cite numa célula xlsx |
| 8 | [14:14 → paragraph.](../videos/features/08-advanced-02-live-cue-cite.mp4) | cite num timestamp de vídeo |
| 9 | [One cite. Three files.](../videos/features/09-advanced-03-multi-target.mp4) | um cite → patches em vários arquivos |
| 17 | [Cross-file anchors. Recorded.](../videos/features/17-advanced-11-cross-link.mp4) | sidecar `.htmlook/links.json` |

## 5.3 · Walkthroughs de persona (26)

Um workflow *day-in-the-life* por papel / domínio. mp4 de 60–70 s +
sample workspace pra acompanhar + `WALKTHROUGH.md` passo a passo.

Catálogo completo: [`personas/INDEX.md`](personas/INDEX.md). A ordem
recomendada é agrupada por papel:

- **Dev**: [`personas/01-hf-claude/`](personas/01-hf-claude/) →
  [`02-hf-llama/`](personas/02-hf-llama/) →
  [`03-dev-pr-docs/`](personas/03-dev-pr-docs/)
- **Conteúdo**: [`personas/04-creator-podcast/`](personas/04-creator-podcast/) →
  [`12-press-editor/`](personas/12-press-editor/) →
  [`15-picture-book/`](personas/15-picture-book/) →
  [`22-hobby-fiction/`](personas/22-hobby-fiction/)
- **Análise**: [`personas/09-data-analyst/`](personas/09-data-analyst/) →
  [`11-finance-report/`](personas/11-finance-report/) →
  [`10-research-notes/`](personas/10-research-notes/) →
  [`06-economy-analyst/`](personas/06-economy-analyst/)
- **Jurídico / tradução**: [`personas/08-legal-redline/`](personas/08-legal-redline/) →
  [`07-translator-book/`](personas/07-translator-book/) →
  [`05-domain-battery/`](personas/05-domain-battery/)
- **Educação (professores)**: [`personas/17-teacher-quiz/`](personas/17-teacher-quiz/) →
  [`18-teacher-newsletter/`](personas/18-teacher-newsletter/) →
  [`19-teacher-record/`](personas/19-teacher-record/)
- **Educação (alunos)**: [`personas/20-student-notes/`](personas/20-student-notes/) →
  [`24-student-flashcard/`](personas/24-student-flashcard/) →
  [`23-homework-helper/`](personas/23-homework-helper/) →
  [`21-kid-coding/`](personas/21-kid-coding/) →
  [`14-kids-science-mag/`](personas/14-kids-science-mag/)
- **Negócios**: [`personas/16-corp-deck/`](personas/16-corp-deck/) →
  [`13-product-prd/`](personas/13-product-prd/)
- **Cotidiano**: [`personas/25-recipe-card/`](personas/25-recipe-card/) →
  [`26-mobile-news/`](personas/26-mobile-news/)

## 5.4 · O padrão follow-along

Dentro de cada pasta de persona:

- `WALKTHROUGH.md` — passo a passo (marcas `[VIEW]` / `[AI]`)
- `before/` — estado antes do edit (comparação visual)
- `after/` — estado depois do edit (pra quem não tem AI ver o resultado
  mesmo assim)
- os arquivos de conteúdo do domínio (md / html / pdf / xlsx / svg /
  py / mp3, …)

## 5.5 · LLM-agnóstico — swap de fornecedor

O mesmo workflow cite + apply_edit roda idêntico nos 9 fornecedores.
Adicione outro no [Step 3](../03-byom-setup/) e troque — mesmo
resultado.

## ✅ Checkpoint Step 5

- Você assistiu a um vídeo de persona (60–70 s) próximo do seu papel.
- Você seguiu os passos `[VIEW]` do `WALKTHROUGH.md` dessa persona.
- (Com AI configurada) Rodou os passos `[AI]` → o pane direito
  recarregou.
- (Sem AI) Comparou `before/` vs `after/` em split view.

Tudo? → [Step 6 · save-as-skill](../06-save-as-skill/) — registre um
workflow recorrente no app de forma permanente.

## Mais a fundo

- [`personas/INDEX.md`](personas/INDEX.md) — catálogo das 26 personas
  + mapeamento vídeo ↔ pasta.
- [`personas/README.md`](personas/README.md) — como usar os sample
  workspaces.
- [`../03-byom-setup/AI_GUIDE.md`](../03-byom-setup/AI_GUIDE.md) — as
  ~22 ferramentas MCP + o guia de tom dos agentes AI.
