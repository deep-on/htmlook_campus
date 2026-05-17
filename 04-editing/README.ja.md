# Step 4 · Editing (Paint / Region / Element Pick)

<p align="center">
  <a href="README.md">English</a> | <a href="README.ko.md">한국어</a> | <b>日本語</b> | <a href="README.de.md">Deutsch</a> | <a href="README.fr.md">Français</a> | <a href="README.es.md">Español</a> | <a href="README.pt.md">Português</a> | <a href="README.it.md">Italiano</a>
</p>

> 画面上で *どの領域か* を LLM に伝える 4 つの方法。
> 約 5 分。

HTMLook の最も差別化された部分。AI に *「ここを直して」* と言うとき、
*ここ* を painter のような道具で直接指せます。

このステップが終わると、region ドラッグ → cite anchor → AI プロンプトと
いうコアサイクルを一度自分の手で回したことになります。

## 4.1 · 4 つの選択方法サマリー

| 方法 | 入り方 | 用途 |
|---|---|---|
| **element pick** | preview をクリック | 単一 DOM ノード (button / heading / paragraph) |
| **range select** | preview でドラッグ | テキスト範囲 (sentence / phrase) |
| **region paint** ⭐ | ⌘Shift+R のあと矩形をドラッグ | 視覚的な領域 (chart / イラスト領域) |
| **outline pick** | 右側の Outline パネルをクリック | 見出し単位 |

動画: [BASIC #6 · Pick what you see.](../videos/features/06-basic-06-html-4mode.mp4) (30 秒)

## 4.2 · ⭐ Region cite — もっとも核となる動作

Step 4 で一番重要な動作。AI との最初の *共通言語* です。

1. HTML または PDF を 1 つ開く (例: [`../05-command/personas/01-hf-claude/landing.html`](../05-command/personas/01-hf-claude/landing.html))
2. ⌘Shift+R で region paint モードに入る
3. preview 上で矩形ドラッグ → 領域がマゼンタアクセントでハイライト
4. 右側の AI パネルに自動で cite anchor が添付される
5. AI に *「ここを直して — Apex の価値 (edge compute) を一行で」*

MCP が繋がっていれば LLM は:
- `htmlook_region_current_png` で領域の PNG を取得 (vision モデル)
- `htmlook_active_file` + `htmlook_cite` でマッチするテキスト anchor を
  確保
- `htmlook_apply_edit` でパッチ適用

> 動画: [BASIC #5 ⭐ · Drag. Tell the LLM.](../videos/features/05-basic-05-region-cite.mp4)
> (30 秒 · AI のエントリーポイント)

## 4.3 · Element pick

preview で要素にホバー → 輪郭線 → クリック → 選択。⌘E でモード切り替え。

選択された要素の outerHTML は `htmlook_selection_html` で LLM が読み、
パッチ後 `htmlook_apply_edit`。

## 4.4 · Sentence-id (動画 / テキスト内の文単位)

長い transcript や paper の中で文 #N を直接 cite:

1. 動画または長い md を開く。
2. 右パネルの *Sentence Map* をトグル → 文に N 番号が付く。
3. クリック → cite anchor `sentence:5` が AI パネルに添付。

> 動画: [ADV · Click sentence 5. Clip ships.](../videos/features/14-advanced-08-sentence-id.mp4)
> (30 秒)

## 4.5 · Range select — ただドラッグ

最も一般的。preview でテキストをドラッグ → `selection_text` /
`selection_html` の両方が使えるようになります。

## ✅ Step 4 チェックポイント

- region paint モードを ⌘Shift+R で開いて矩形を 1 度描いた。
- 描いた領域が AI パネルに cite anchor として添付されることを確認。
- AI に一言送ってパッチを受け取った (応答の *どこか* に cite が
  あるはず)。

3 つ揃ったら → [Step 5 · command (terminal / chat / apply)](../05-command/)

## 詳しくは

- [`../03-byom-setup/AI_GUIDE.md`](../03-byom-setup/AI_GUIDE.md) — MCP
  ツール一覧 (selection / region / element / cite)。
- [`../05-command/personas/`](../05-command/personas/) — 26 ペルソナ
  ウォークスルー (各ペルソナが region/element/sentence cite のどの
  パターンを使うかは様々)。
