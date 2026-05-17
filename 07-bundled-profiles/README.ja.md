# Step 7 · Bundled Profiles (HyperFrames / Slidev ほか 6 種)

<p align="center">
  <a href="README.md">English</a> | <a href="README.ko.md">한국어</a> | <b>日本語</b> | <a href="README.de.md">Deutsch</a> | <a href="README.fr.md">Français</a> | <a href="README.es.md">Español</a> | <a href="README.pt.md">Português</a> | <a href="README.it.md">Italiano</a>
</p>

> v1.0 から 8 種の *Heavyweight Profile* がアプリに同梱されています。
> 初回起動時に `~/.htmlook/profiles/_bundled-*` へ自動 unpack。
> 約 5 分 (見て回るだけ — 本格的な利用は各ツールの習熟度次第)。

Profile = 外部ツール + Skill v0.3 バンドル + シードコンテンツのパッケージ。
New Workspace Wizard (⌘⇧N) または Add wizard のカードからワンクリックで
インストール。

> Profile manifest (profile.json + SKILL.md + seed/) の本体はキャンパスの
> ルート [`../profiles/`](../profiles/) にあります — catalog.json ビルダーは
> このパスを直接読みます。本ステップはそれらを見て回るためのガイド。

## 7.1 · 8 種の profile カード

| Profile | カテゴリ | 出力 | ツールライセンス | 開始地点 |
|---------|---------|------|---------------|---------|
| HyperFrames | motion-graphics | mp4 (kinetic typography) | MIT | [`../profiles/hyperframes/`](../profiles/hyperframes/) |
| Slidev | presentation | HTML/PDF slides | MIT | [`../profiles/slidev/`](../profiles/slidev/) |
| Quarto | publishing | PDF/HTML/PPT/book | GPL-2.0 | [`../profiles/quarto/`](../profiles/quarto/) |
| D2 | diagram | SVG | MPL-2.0 | [`../profiles/d2/`](../profiles/d2/) |
| Astro Starlight | documentation | docs site | MIT | [`../profiles/astro-starlight/`](../profiles/astro-starlight/) |
| Marimo | notebook | reactive HTML | Apache-2.0 | [`../profiles/marimo/`](../profiles/marimo/) |
| Excalidraw | diagram | JSON/SVG/PNG | MIT | [`../profiles/excalidraw/`](../profiles/excalidraw/) |
| Manim | educational-animation | mp4 | BSD-3-Clause | [`../profiles/manim/`](../profiles/manim/) |

> **HTMLook はツール本体をバンドルしません。** 利用ガイドと Wizard 統合のみ
> 提供。外部ツールは別途インストールしてください (依存関係は各 profile の
> README に明記)。

## 7.2 · 1 つ選んでスタート

はじめてなら軽いものから:

- **Slidev** — `npx slidev` でインストール。md 1 ファイル → HTML スライド。
- **D2** — Go バイナリをインストール。txt → SVG 図。
- **Excalidraw** — インストール不要 (HTMLook 内蔵ビューワー)。

重めのもの:

- **HyperFrames** — Node + ffmpeg + Kokoro TTS (Python)。キャンパス動画を
  作った道具そのもの。
- **Manim** — Python + LaTeX。数学アニメーション。
- **Quarto** — R / Python / Pandoc。学術出版。

## 7.3 · Add wizard からインストール

1. ⌘⇧N (New Workspace Wizard) またはサイドバーの *+* (Add wizard)
2. カタログから欲しい profile カードを選択
3. *Install* — シードフォルダがユーザーの home にコピーされる
4. *Open* — HTMLook がそのフォルダをワークスペースとして開き、profile の
   Skill が ⌘K カタログに追加されます

## 7.4 · 追加のドメインシード (任意)

8 profile に加えて 75 のワークスペースシードが
[`../sample_workspaces/`](../sample_workspaces/) にあり、すべて prefix で
どの profile のシードか一目で分かります:

- `hf-*/` (26 種 — HyperFrames、キャンパス動画制作のフルペルソナラインナップ)
- `slidev-*/` (7 種) · `quarto-*/` (7 種) · `marimo-*/` (7 種) · `manim-*/` (7 種)
- `d2-*/` (7 種) · `excalidraw-*/` (7 種) · `astro-*/` (7 種)

`hf-claude/` と `hf-llama/` は BYOM のリファレンス経路 (Anthropic Claude
/ ローカル Llama)。残りの 24 種 (`hf-corp-deck/`, `hf-teacher-quiz/`,
`hf-kid-coding/` …) はドメインシナリオ。各シードは `index.html +
hyperframes.json + brand.txt + prompts.txt + AGENTS.md + meta.json +
README.md` のフルセットなので、AI エージェントがユーザーの BYOM モデル
でそのままワークフローを再現できます。

カタログ全体: [`../catalog.json`](../catalog.json) — 現在 **83 entries**
(8 profile + 75 workspace seed)。CI が自動更新
([`../scripts/build-catalog.mjs`](../scripts/build-catalog.mjs))。

## ✅ Step 7 チェックポイント

- 8 profile の README のうち 1 つを読んだ。
- (任意) ツールを 1 つ外部インストール → Add wizard からその profile の
  シードをインストール。
- (任意) `sample_workspaces/` から自分のドメインに近いシードを 1 つ
  眺めた。

3 つ揃ったら → [Step 8 · extend (自分の Profile を書く)](../08-extend/)

## 詳しくは

- 各 profile フォルダの `SKILL.md` — その profile が登録する Skill v0.3
  manifest。
- [`../08-extend/PRODUCTION.md`](../08-extend/PRODUCTION.md) — HyperFrames
  でキャンパス動画を作る標準 (17 + 26 本すべてこの道具で制作)。
