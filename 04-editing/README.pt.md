# Step 4 · Editing (Paint / Region / Element Pick)

<p align="center">
  <a href="README.md">English</a> | <a href="README.ko.md">한국어</a> | <a href="README.ja.md">日本語</a> | <a href="README.de.md">Deutsch</a> | <a href="README.fr.md">Français</a> | <a href="README.es.md">Español</a> | <b>Português</b> | <a href="README.it.md">Italiano</a>
</p>

> Quatro jeitos de dizer ao LLM *qual área da tela* você quer.
> ~ 5 min.

A parte mais distintiva do HTMLook. Quando você diz à AI *"corrige
aqui"*, dá pra apontar *aqui* direto — como um pintor.

No fim deste passo você terá rodado o ciclo principal uma vez sozinho:
drag de region → cite anchor → prompt AI.

## 4.1 · As quatro formas de seleção

| Método | Como | Pra que |
|---|---|---|
| **element pick** | clique no preview | um único nó DOM (botão / título / parágrafo) |
| **range select** | drag no preview | uma faixa de texto (frase / trecho) |
| **region paint** ⭐ | ⌘Shift+R e drag de retângulo | uma zona visual (chart / área de ilustração) |
| **outline pick** | clique no painel Outline à direita | uma seção a partir de um cabeçalho |

Vídeo: [BASIC #6 · Pick what you see.](../videos/features/06-basic-06-html-4mode.mp4) (30 s)

## 4.2 · ⭐ Region cite — a peça-chave

A jogada mais importante do Step 4. Sua primeira *língua comum* com a
AI.

1. Abra um HTML ou PDF (ex. [`../05-command/personas/01-hf-claude/landing.html`](../05-command/personas/01-hf-claude/landing.html)).
2. ⌘Shift+R entra no modo region paint.
3. Trace um retângulo no preview → a área acende em acento magenta.
4. Um cite anchor anexa sozinho ao painel AI à direita.
5. Diga à AI *"corrige aqui — o valor do Apex (edge compute) em uma
   linha"*.

Se o MCP estiver conectado, o LLM:
- puxa um PNG da região via `htmlook_region_current_png` (modelos
  vision),
- garante o anchor de texto correspondente com `htmlook_active_file` +
  `htmlook_cite`,
- aplica o patch com `htmlook_apply_edit`.

> Vídeo: [BASIC #5 ⭐ · Drag. Tell the LLM.](../videos/features/05-basic-05-region-cite.mp4)
> (30 s · o ponto de entrada AI)

## 4.3 · Element pick

Hover sobre um elemento no preview → contorno → clique →
selecionado. ⌘E alterna o modo.

O outerHTML do elemento escolhido é lido pelo LLM via
`htmlook_selection_html`, recebe o patch, e vai com `htmlook_apply_edit`.

## 4.4 · Sentence-id (frase a frase em texto / vídeo longo)

Cite a frase #N direto num transcript ou paper longo:

1. Abra um vídeo ou uma md longa.
2. Ative *Sentence Map* no painel direito → as frases ganham número N.
3. Clique → o cite anchor `sentence:5` anexa ao painel AI.

> Vídeo: [ADV · Click sentence 5. Clip ships.](../videos/features/14-advanced-08-sentence-id.mp4)
> (30 s)

## 4.5 · Range select — só arrastar

O mais comum. Drag de texto no preview → `selection_text` e
`selection_html` ficam ambos disponíveis.

## ✅ Checkpoint Step 4

- Você entrou no region paint com ⌘Shift+R e desenhou um retângulo.
- A região desenhada anexou como cite anchor no painel AI.
- Você mandou uma frase pra AI e recebeu um patch (a resposta tem um
  cite anchor *em algum lugar*).

Os três? → [Step 5 · command (terminal / chat / apply)](../05-command/)

## Mais a fundo

- [`../03-byom-setup/AI_GUIDE.md`](../03-byom-setup/AI_GUIDE.md) — as
  ferramentas MCP (selection / region / element / cite).
- [`../05-command/personas/`](../05-command/personas/) — 26 walkthroughs
  de persona (cada persona prefere um padrão
  region/element/sentence-cite diferente).
