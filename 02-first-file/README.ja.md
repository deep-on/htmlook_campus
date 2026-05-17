# Step 2 · 最初のファイル (HTML / Markdown / PDF / 動画)

<p align="center">
  <a href="README.md">English</a> | <a href="README.ko.md">한국어</a> | <b>日本語</b> | <a href="README.de.md">Deutsch</a> | <a href="README.fr.md">Français</a> | <a href="README.es.md">Español</a> | <a href="README.pt.md">Português</a> | <a href="README.it.md">Italiano</a>
</p>

> HTMLook の *ビューワー* の本質を体得します。AI / MCP なしでも価値のある
> パートです。
> 約 5 分。

このステップが終わると、4 種類のファイル (md / html / pdf / 動画) それぞれの
読み方と、分割ビュー / プレビュー / アウトラインでのナビゲート方法が
分かります。

## 2.1 · Markdown ライブ編集

1. サイドバーで任意の `.md` ファイル (例: [`../05-command/personas/03-dev-pr-docs/docs.md`](../05-command/personas/03-dev-pr-docs/docs.md)) をダブルクリック。
2. ⌘\\ またはメニュー *View → Split* で分割ビューをトグル。
3. 左にソース、右にプレビュー。左で打つと右がライブで更新されます。

> 動画: [BASIC #3 · Type left. See right. Live.](../videos/features/03-basic-03-md-live-edit.mp4) (30 秒)

## 2.2 · HTML — 要素をクリックして直接編集

1. `.html` ファイル (例: [`../05-command/personas/01-hf-claude/landing.html`](../05-command/personas/01-hf-claude/landing.html)) をダブルクリック。
2. 既定モードはプレビュー。分割ビューで要素を直接クリック → テキスト
   エディタが出現。
3. 双方向同期 — プレビューでの変更がソースに即座に反映。

> 動画: [BASIC #4 · Click anything. Edit it.](../videos/features/04-basic-04-html-split.mp4) (30 秒)

## 2.3 · HTML — 4 つの選択モード

同じ HTML ファイルで ⌘E が選択モードを巡回します:

| モード | 拾うもの |
|---|---|
| element | 単一 DOM ノード |
| range | テキスト範囲 |
| region | 矩形ペイント |
| outline | 見出しツリー |

動画: [BASIC #6 · Pick what you see.](../videos/features/06-basic-06-html-4mode.mp4) (30 秒)

各モードが拾ったものが [Step 4 · editing](../04-editing/) の cite anchor
入口になります。

## 2.4 · PDF — ページ + テキストレイヤー

1. 任意の `.pdf` ファイル (例: [`../05-command/personas/05-domain-battery/vendor.pdf`](../05-command/personas/05-domain-battery/vendor.pdf)) をダブルクリック。
2. 左にサムネイルナビゲーター、右にページキャンバス、テキスト選択可能。
3. 領域ドラッグ → region cite (Step 4 で使います)。

## 2.5 · 動画 — フレームサムネイル + アウトライン

1. 任意の mp4 (例: [`../videos/features/01-basic-01-drop-open.mp4`](../videos/features/01-basic-01-drop-open.mp4)) をダブルクリック。
2. 動画ビューワーが timeline とサムネイルプレビューを表示。
3. ⌘Shift+T またはホバーで、フレーム上で 1 秒のプレビュー (スクラブなし)。

> 動画: [ADV · Frame check. No scrub.](../videos/features/15-advanced-09-thumbnail.mp4) (30 秒、advanced カテゴリ)

## 2.6 · アウトライン — 長い文書をナビゲート

長い md / html / PDF の見出し構造 → 右パネルの Outline タブ。見出しを
クリックするとその位置にジャンプ。

> 動画: [ADV · Click §3.2. You're there.](../videos/features/16-advanced-10-outline.mp4) (30 秒)

## 2.7 · 分割ビュー / マルチペイン (⌘1 / ⌘2 / ⌘3 / ⌘J)

| ショートカット | 効果 |
|---|---|
| ⌘1 | プレビューのみ |
| ⌘2 | ソースのみ |
| ⌘3 | 分割 (preview + source) |
| ⌘J | ターミナルパネルのトグル |

動画: [ADV · Two keys. Three views.](../videos/features/10-advanced-04-multi-pane.mp4)
(30 秒 — ナレーションの *"Two keys"* は元のカットでは ⌘D + ⌘J で、v1.0
で ⌘1/⌘2/⌘3 + ⌘J に訂正されました。詳しい経緯は
[`../08-extend/PRODUCTION.md`](../08-extend/PRODUCTION.md) の *修正された
false claims* 表をご参照ください。)

## ✅ Step 2 チェックポイント

- md / html / pdf / 動画 4 種を分割ビューで開いた。
- HTML 4 モード (element / range / region / outline) の違いを直接クリック
  で体感した。
- ⌘1 / ⌘2 / ⌘3 / ⌘J でレイアウト切り替えが手に馴染んだ。

3 つ揃ったら → [Step 3 · BYOM setup](../03-byom-setup/) — ベンダーを 1 つ
選んでキー登録。
