# Step 3 · BYOM セットアップ (ベンダー 1 つを選択)

<p align="center">
  <a href="README.md">English</a> | <a href="README.ko.md">한국어</a> | <b>日本語</b> | <a href="README.de.md">Deutsch</a> | <a href="README.fr.md">Français</a> | <a href="README.es.md">Español</a> | <a href="README.pt.md">Português</a> | <a href="README.it.md">Italiano</a>
</p>

> Bring-Your-Own-Model — ベンダーキーをご自身で登録します。トークンの
> マージン 0。
> 約 5 分。

HTMLook は LLM をバンドルせず、*アダプタ* だけを提供します。v1.0 では
9 ベンダー対応: Claude / GPT / Gemini / DeepSeek / Mistral / Together /
Groq / Cerebras / Ollama (ローカル)。このステップでは **1 つだけ** 選んで
動作を確認します — 後で [Step 5](../05-command/) でスワップできます。

## 3.1 · 3 つのエントリーパス

HTMLook から LLM を呼ぶ経路は 3 つ。いずれも同じ MCP ツール
(`htmlook_*`) を公開します:

| 経路 | 場所 | おすすめの人 |
|---|---|---|
| **内蔵 BYOM チャット** ⭐ | Settings → Models → キー登録後、右側の AI パネル | はじめて使う人 |
| **内蔵 Terminal + CLI** | ⌘J でトグル後、`claude` / `codex` / `gemini` を実行 | CLI に慣れた人 |
| **外部 MCP クライアント** | Claude Code / Cursor / Windsurf / Zed の mcp.json にマージ | すでに別のクライアントを使用中 |

詳しい使い方ガイドと MCP ツール一覧: [`AI_GUIDE.md`](AI_GUIDE.md)。

## 3.2 · おすすめ: 内蔵 BYOM チャット

1. HTMLook 右上の歯車 → **Settings → Models** タブ
2. ベンダーを 1 つ選んで *Add Provider*
   - Anthropic Claude (最も安定) または
   - OpenAI GPT または
   - Google Gemini (フリーティアが最も大きい)
3. API キーを貼り付けて *Test* — 200 OK を確認
4. *Save* — 右側の AI パネルが有効化

> 動画: [ADV · Swap the LLM. Keep the workflow.](../videos/features/13-advanced-07-mcp-swap.mp4)
> (30 秒 · MCP 経由で LLM 非依存)

## 3.3 · Ollama (ローカル、キー不要)

キーを外部サービスに送りたくない場合:

1. [ollama.com](https://ollama.com) から Ollama をインストール
2. `ollama pull llama3.2` (お好きなモデルで)
3. HTMLook Settings → Models → *Add Provider* → Ollama → host
   `http://localhost:11434` (デフォルト)

## 3.4 · 外部 MCP クライアントを使う場合

すでに Claude Code / Cursor / Windsurf / Zed をお使いなら、
[`./.htmlook/mcp-config.example.json`](./.htmlook/mcp-config.example.json)
の内容を各クライアントの mcp.json にマージ。HTMLook MCP サーバーは
約 22 個の `htmlook_*` ツール (cite, apply_edit, selection,
region_current_png, outline, link, video_*, …) を公開します。

## 3.5 · 最初の hello

AI パネルが有効になったら、チャット欄に入力:

> *現在のワークスペースの最初のファイルを 1 行で要約してください。*

LLM が `htmlook_active_file` MCP ツールでワークスペースのコンテキストを
取得してから応答するか確認。応答がワークスペースを認識していなければ、
もう一度 **Settings → AI → Connect** を押すか、外部 MCP クライアント
使用時は mcp.json のマージ状態を再点検。

## 3.6 · auto-reload — モデルが応答したあと

`apply_edit` がファイルに書き込むと、ファイルウォッチャーが検知して
分割ビューの右ペインが自動でリロード。

> 動画: [ADV · It just reloaded.](../videos/features/11-advanced-05-auto-reload.mp4)
> (30 秒)

## ✅ Step 3 チェックポイント

- 1 つのベンダー (または Ollama) のキーが Settings → Models に保存された。
- チャット欄に hello を送って応答が返ってきた。
- 応答がワークスペースのコンテキストを認識していた。

問題があれば [`AI_GUIDE.md`](AI_GUIDE.md) の *デバッグ* セクションを
参照。

3 つ揃ったら → [Step 4 · editing (paint / region / element pick)](../04-editing/)

## 詳しくは

- [`AI_GUIDE.md`](AI_GUIDE.md) — 約 22 種の MCP ツール + ペルソナ
  follow-along パターン + AI エージェントの出力トーン。
- [`./.htmlook/mcp-config.example.json`](./.htmlook/mcp-config.example.json)
  — 外部 MCP クライアント用サンプル設定。
