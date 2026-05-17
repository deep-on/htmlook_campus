# HTMLook Campus

<p align="center">
  <a href="README.md">English</a> | <a href="README.ko.md">한국어</a> | <b>日本語</b> | <a href="README.de.md">Deutsch</a> | <a href="README.fr.md">Français</a> | <a href="README.es.md">Español</a> | <a href="README.pt.md">Português</a> | <a href="README.it.md">Italiano</a>
</p>

> HTMLook Pro をはじめて使う方のための **8 ステップチュートリアル**。
> 一段ずつ進めれば、30〜40 分でインストール → 最初のファイル → BYOM →
> 編集 → コマンド → save-as-skill → バンドルプロファイル →
> 自分のプロファイル作成までひと通り体験できます。

このリポジトリは **HTMLook Pro v1.0 リリース候補**（正式リリースは 2026 年
中頃予定）と同期しています。デスクトップアプリは
[htmlook.app](https://htmlook.app) で 14 日間の無料トライアル。BYOM
(Bring-Your-Own-Model) なのでトークンマージンはゼロ — Claude · GPT ·
Gemini · DeepSeek · Mistral · Together · Groq · Cerebras · Ollama、
お好きなモデルをご自身のキーで直接呼び出せます。

## チュートリアルパス

上から下へ順番に。各ステップは前のステップの動きの上に積み上がります。

| Step | フォルダ | 内容 | 所要時間 |
|---|---|---|---|
| 1 | [`01-getting-started/`](01-getting-started/) | インストール · 初回起動 · ドラッグ&ドロップ · フォルダを開く | 3 分 |
| 2 | [`02-first-file/`](02-first-file/) | md / html / pdf / 動画 4 種 + 分割ビュー + アウトライン | 5 分 |
| 3 | [`03-byom-setup/`](03-byom-setup/) | ベンダーを 1 つ選んでキー登録（または Ollama） | 5 分 |
| 4 | [`04-editing/`](04-editing/) | 要素ピック · 領域ペイント · sentence-id · cite アンカー | 5 分 |
| 5 | [`05-command/`](05-command/) | チャット · ターミナル CLI · apply_edit · 26 ペルソナのウォークスルー | 10 分 |
| 6 | [`06-save-as-skill/`](06-save-as-skill/) | ワークフローをキャプチャ → ⌘K カタログカード | 5 分 |
| 7 | [`07-bundled-profiles/`](07-bundled-profiles/) | HyperFrames · Slidev · Quarto · D2 · Astro Starlight · Marimo · Excalidraw · Manim を一覧 | 5 分 |
| 8 | [`08-extend/`](08-extend/) | 自分のプロファイル作成 + カタログ PR | 任意 |

> ざっと眺めるだけなら、ステップと動画のマッピングを
> [`01-getting-started/LEARNING_PATH.md`](01-getting-started/LEARNING_PATH.md)
> でご確認ください。各動画 30〜70 秒です。

## リファレンスマニュアル (Wiki)

8 ステップチュートリアルが *最初から最後まで一度通す* 流れだとすれば、
[`wiki/`](wiki/) は *機能ごとに引く* リファレンスマニュアルです。サイドバー ·
タブ · ビューワー · Markdown エディタ · PDF · 動画/音声プレイヤー · ターミナル ·
AI アシスタント · Paint · 音声メモ · Skill · Export · 設定 · ショートカット。
人間ユーザー向けと AI アシスタント (MCP/スキーマ) 向けの 2 系統。

| 系統 | 入口 | 言語 |
|---|---|---|
| 人間ユーザー向けマニュアル | [`wiki/Home.md`](wiki/Home.md) · [韓国語](wiki/Home-ko.md) | EN / KO |
| AI アシスタントガイド | [`wiki/AI-Overview.md`](wiki/AI-Overview.md) · [韓国語](wiki/AI-Overview-ko.md) | EN / KO |

チュートリアルは一度通せば充分、wiki はアプリを使っている間ずっと手元に。
アプリ内では *Help → Documentation* から直接開けます。

## エディション

- **HTMLook Pro** (v1.0) — パワーユーザー向け。BYOM チャット + 内蔵 PTY
  ターミナル + CLI アダプタ (claude / codex / gemini) + MCP ブリッジ + Paint
  キャンバス + 領域キャプチャ + 要素ピック + save-as-skill + 8 バンドル
  プロファイル + 49 シード。
- **HTMLook Easier** *(近日公開)* — はじめての方向けエディション、再定義中。

## Step 1 — インストール + 初回起動

[`01-getting-started/README.md`](01-getting-started/README.md) から開始。

[htmlook.app](https://htmlook.app) で .dmg を取得して Applications に
ドラッグし、最初のファイルをドラッグ&ドロップしてみてください。

## Step 2 — 最初のファイル (HTML / MD / PDF / 動画)

[`02-first-file/README.md`](02-first-file/README.md)。4 種類のファイルを
分割ビュー + アウトライン + サムネイルでナビゲート。

動画: BASIC #3 #4 #6 + ADV multi-pane / thumbnail / outline。mp4 本体は
[`videos/features/`](videos/features/) にあります。

## Step 3 — BYOM 設定 (ベンダー 1 つだけ)

[`03-byom-setup/README.md`](03-byom-setup/README.md)。詳しい AI ガイドは
[`03-byom-setup/AI_GUIDE.md`](03-byom-setup/AI_GUIDE.md)、外部 MCP クライアントの
サンプル設定は
[`03-byom-setup/.htmlook/mcp-config.example.json`](03-byom-setup/.htmlook/mcp-config.example.json)。

## Step 4 — 画面上で *どこか* を指し示す

[`04-editing/README.md`](04-editing/README.md)。要素ピック · 領域ペイント ·
sentence-id · 範囲選択の 4 通り。キーになる動画は BASIC #5 ⭐ region-cite
(AI のエントリーポイント)。

## Step 5 — コマンドで書き換える (cite + apply_edit)

[`05-command/README.md`](05-command/README.md)。キャンパスの最深部 — 26 の
ペルソナウォークスルーが [`05-command/personas/`](05-command/personas/) に
あります (職種別、各フォルダに follow-along WALKTHROUGH.md + before/after)。

ペルソナカタログ: [`05-command/personas/INDEX.md`](05-command/personas/INDEX.md)。

## Step 6 — 繰り返すワークフロー → Skill

[`06-save-as-skill/README.md`](06-save-as-skill/README.md)。右側の AI パネル、
*Save as Skill* ダイアログ。3 行で完了。

## Step 7 — バンドルされた 8 プロファイル

[`07-bundled-profiles/README.md`](07-bundled-profiles/README.md)。HyperFrames /
Slidev / Quarto / D2 / Astro Starlight / Marimo / Excalidraw / Manim。
プロファイルシード本体は [`profiles/`](profiles/) (catalog.json ビルダーが
直接参照)。

## Step 8 — 自分のプロファイル作成 + 動画スタンダード

[`08-extend/README.md`](08-extend/README.md)。自分のドメイン用プロファイルを
作ってカタログに追加。動画スタンダード + 逆検証プロセスは
[`08-extend/PRODUCTION.md`](08-extend/PRODUCTION.md)、17 機能の動画カタログは
[`08-extend/FEATURES.md`](08-extend/FEATURES.md)。

## 素材の場所 (リファレンス)

キャンパスのルートにはステップフォルダ (01〜08) と並んで、次の *共有 asset
ディレクトリ* があります (catalog.json + アプリがこのパスを直接参照するため、
ステップフォルダ内には移動しません):

| フォルダ | 内容 |
|---|---|
| [`videos/`](videos/) | 17 機能 mp4 + 26 ペルソナ mp4 (合計 ~340 MB) |
| [`profiles/`](profiles/) | 8 プロファイルシード (`profile.json` + `SKILL.md` + `seed/`) |
| [`sample_workspaces/`](sample_workspaces/) | 75 ドメインシード (`hf-*` ペルソナ 26 + プロファイルシード 49) |
| [`catalog.json`](catalog.json) | 83 エントリ (8 プロファイル + 75 ワークスペースシード) — アプリの Wizard が fresh-fetch (24 h キャッシュ) |
| [`scripts/`](scripts/) | `build-catalog.mjs` |
| [`infra/`](infra/) | ライセンスワーカー (別サービス) |
| [`docs/`](docs/) | 生成物の作業領域 (gitignored) |

## 2 つの学習レイヤー — 動画 + インタラクティブ

キャンパスの動画は *what (何ができるか)*。HTMLook Pro 内蔵のインタラクティブ
ウォークスルー (*Help → Interactive Tutorials…*) は *how (どうやるか)*。
動画に登場する 17 機能すべてにインタラクティブガイドが 1:1 で対応します。

| レイヤー | 場所 | 長さ | 役割 |
|---|---|---|---|
| 動画 (キャンパス) | `videos/features/`, `videos/` | 30 s / 60-70 s | 結果を見せる |
| インタラクティブ (アプリ) | HTMLook Pro · Help → Interactive Tutorials… | 4 ステップ | 自分の手で再現 |

## 逆検証の約束 (Reverse Verification)

このキャンパスの動画は **実際の HTMLook の動作と一致する主張のみ** を
行います。存在しない機能は宣伝しません。詳細な検証プロセスと修正済みの
誤った主張の一覧: [`08-extend/PRODUCTION.md`](08-extend/PRODUCTION.md)。

## ステータス

このリポジトリは **HTMLook Pro v1.0 リリース候補** (正式リリース 2026 年中頃
予定) と同期した学習素材です。v1.0 GA のタイミングで公開に切り替わり、
カタログエンドポイント (`htmlook.app/catalog`) がこのリポジトリの raw URL を
fresh-fetch するようになります (24 h キャッシュ)。

## ライセンス

- コード / ウォークスルーのテキスト: MIT
- 動画 mp4: CC BY 4.0 (利用時は *"HTMLook Campus"* と出典を表記)
- サンプルコンテンツ (PDF / xlsx / md / html): CC0 / パブリックドメイン — すべて架空のプレースホルダー
