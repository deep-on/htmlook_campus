# Step 6 · Save-as-Skill (ワークフローのキャプチャ)

<p align="center">
  <a href="README.md">English</a> | <a href="README.ko.md">한국어</a> | <b>日本語</b> | <a href="README.de.md">Deutsch</a> | <a href="README.fr.md">Français</a> | <a href="README.es.md">Español</a> | <a href="README.pt.md">Português</a> | <a href="README.it.md">Italiano</a>
</p>

> Step 5 で覚えた cite + apply_edit サイクルを *アプリが覚える*。次回は
> ワンクリックで再実行。
> 約 5 分。

このステップが終わると、ワークスペースに自分のツールが 1 つ登録され、
サイドバーの *Tools* セクションや ⌘K の Add wizard に出てきます。

## 6.1 · *Save as Skill* — 入り口

直前の LLM とのやり取り / apply_edit サイクルがうまくいったら、右側の
AI パネル上部の *⋯* → **Save as Skill** をクリック。

ダイアログで 3 行だけ埋めれば OK:

| フィールド | 例 |
|---|---|
| Name | *Tighten subtitle* |
| When to use | *副題が短すぎるとき、1 行に拡張* |
| Default prompt | *現在の cite 領域の副題を Apex の価値 (edge compute, 高速デプロイ) に 1 行で広げて apply_edit* |

> 動画: [ADV · Add a tool. Three fields.](../videos/features/12-advanced-06-tool-wizard.mp4) (30 秒)

## 6.2 · どこに保存される?

`.htmlook/skills/<name>.skill.json` (ワークスペース内、v0.3 spec)。ワーク
スペースを共有すれば同僚もそのまま使えます。

すべてのワークスペースで使うには **Settings → Skills → Promote to
global**。

## 6.3 · Add wizard から呼ぶ

⌘K またはサイドバーの *+* ボタン → カタログと自分の skill がカードと
して表示。カードクリック → 現在の selection コンテキストで自動実行。

## 6.4 · Skill v0.3 spec — 中身

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

`needs` / `produces` は MCP ツール名。詳しい spec は HTMLook 本リポの
`docs/skills/v0.3.md` を参照 (v1.0 GA 時点で公開)。

## 6.5 · Skill と Profile の違い

- **Skill** = *動作* のキャプチャ (1 つの prompt + ツールの組み合わせ)。
  ワークスペース単位またはユーザーグローバル。
- **Profile** = *ツール + シードコンテンツ + Skill 群* をひとまとめにした
  パッケージ。v1.0 で 8 種類 bundled ([Step 7](../07-bundled-profiles/))。

自分の Profile を書く方法は [Step 8 · extend](../08-extend/) で。

## ✅ Step 6 チェックポイント

- 右側 AI パネルの *Save as Skill* ダイアログを 1 度開いた。
- 3 行埋めて skill を 1 個保存。
- ⌘K のカードにその skill が表示される — クリックで再実行。

3 つ揃ったら → [Step 7 · bundled profiles](../07-bundled-profiles/)

## 詳しくは

- [`../05-command/personas/`](../05-command/personas/) — 各ペルソナが
  どんな skill として保存されるか想像してみてください。パターンが
  掴めます。
