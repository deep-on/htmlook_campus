# Step 7 · Bundled Profiles (HyperFrames / Slidev + 6 outros)

<p align="center">
  <a href="README.md">English</a> | <a href="README.ko.md">한국어</a> | <a href="README.ja.md">日本語</a> | <a href="README.de.md">Deutsch</a> | <a href="README.fr.md">Français</a> | <a href="README.es.md">Español</a> | <b>Português</b> | <a href="README.it.md">Italiano</a>
</p>

> A v1.0 traz 8 *Heavyweight Profiles* embutidos no app. No primeiro
> launch, eles são auto-descompactados em `~/.htmlook/profiles/_bundled-*`.
> ~ 5 min (só uma volta — uso real depende da curva de cada
> ferramenta).

Um Profile = ferramenta externa + bundle de Skill v0.3 + conteúdo
seed, empacotado tudo junto. Instale com um clique pelo New Workspace
Wizard (⌘⇧N) ou um card no Add wizard.

> Os manifests de profile (profile.json + SKILL.md + seed/) ficam na
> raiz do campus em [`../profiles/`](../profiles/) — o builder do
> catalog.json lê direto de lá. Este passo é o tour guiado em volta.

## 7.1 · Os 8 cards de profile

| Profile | Categoria | Saída | Licença da ferramenta | Começar |
|---------|-----------|-------|----------------------|---------|
| HyperFrames | motion-graphics | mp4 (kinetic typography) | MIT | [`../profiles/hyperframes/`](../profiles/hyperframes/) |
| Slidev | presentation | HTML/PDF slides | MIT | [`../profiles/slidev/`](../profiles/slidev/) |
| Quarto | publishing | PDF/HTML/PPT/book | GPL-2.0 | [`../profiles/quarto/`](../profiles/quarto/) |
| D2 | diagram | SVG | MPL-2.0 | [`../profiles/d2/`](../profiles/d2/) |
| Astro Starlight | documentation | docs site | MIT | [`../profiles/astro-starlight/`](../profiles/astro-starlight/) |
| Marimo | notebook | reactive HTML | Apache-2.0 | [`../profiles/marimo/`](../profiles/marimo/) |
| Excalidraw | diagram | JSON/SVG/PNG | MIT | [`../profiles/excalidraw/`](../profiles/excalidraw/) |
| Manim | educational-animation | mp4 | BSD-3-Clause | [`../profiles/manim/`](../profiles/manim/) |

> **O HTMLook não embarca as ferramentas em si.** O app entrega os
> guias de uso e a integração com o Wizard. Cada ferramenta externa é
> instalada à parte (os READMEs de cada profile listam as
> dependências).

## 7.2 · Escolha um e comece

Primeira vez? Vai no leve:

- **Slidev** — `npx slidev` pra instalar. Um md → slides HTML.
- **D2** — instale um binário Go. txt → diagrama SVG.
- **Excalidraw** — sem instalação (HTMLook já tem viewer embutido).

Os mais pesados:

- **HyperFrames** — Node + ffmpeg + Kokoro TTS (Python). A própria
  ferramenta que produziu os vídeos do campus.
- **Manim** — Python + LaTeX. Animação matemática.
- **Quarto** — R / Python / Pandoc. Publicação acadêmica.

## 7.3 · Instalar pelo Add wizard

1. ⌘⇧N (New Workspace Wizard) ou *+* na sidebar (Add wizard).
2. Escolha o card de profile que quer no catálogo.
3. *Install* — a pasta seed é copiada pro seu home.
4. *Open* — o HTMLook abre essa pasta como workspace e os Skills do
   profile aparecem no catálogo ⌘K.

## 7.4 · Seeds extras de domínio (opcional)

Além dos 8 profiles, 75 seeds de workspace ficam em
[`../sample_workspaces/`](../sample_workspaces/) — todos com prefixo
pra ver na hora a qual profile cada um pertence:

- `hf-*/` (26 — HyperFrames, o lineup completo de personas usado pra
  produzir os vídeos do campus)
- `slidev-*/` (7) · `quarto-*/` (7) · `marimo-*/` (7) · `manim-*/` (7)
- `d2-*/` (7) · `excalidraw-*/` (7) · `astro-*/` (7)

`hf-claude/` e `hf-llama/` são as referências BYOM (Anthropic Claude
/ Llama local). Os outros 24 (`hf-corp-deck/`, `hf-teacher-quiz/`,
`hf-kid-coding/` …) são cenários de domínio. Cada seed traz o set
completo `index.html + hyperframes.json + brand.txt + prompts.txt +
AGENTS.md + meta.json + README.md`, pra que um agente AI replique
fielmente o workflow com o BYOM do usuário.

Catálogo completo: [`../catalog.json`](../catalog.json) — atualmente
**83 entradas** (8 profile + 75 workspace seed). O CI reconstrói
sozinho ([`../scripts/build-catalog.mjs`](../scripts/build-catalog.mjs)).

## ✅ Checkpoint Step 7

- Você leu um dos 8 READMEs de profile.
- (Opcional) Instalou uma ferramenta externa → pelo Add wizard,
  instalou o seed daquele profile.
- (Opcional) Deu uma olhada num seed de `sample_workspaces/` próximo
  do seu domínio.

Tudo? → [Step 8 · extend (escrever seu próprio Profile)](../08-extend/)

## Mais a fundo

- O `SKILL.md` em cada pasta de profile — o manifest Skill v0.3 que
  o profile registra.
- [`../08-extend/PRODUCTION.md`](../08-extend/PRODUCTION.md) — o padrão
  de produção dos vídeos do campus com HyperFrames (os 17 + 26
  vídeos foram todos feitos com essa ferramenta).
