# Step 5 · Command (Terminal / Chat / Apply)

<p align="center">
  <a href="README.md">English</a> | <a href="README.ko.md">한국어</a> | <b>日本語</b> | <a href="README.de.md">Deutsch</a> | <a href="README.fr.md">Français</a> | <a href="README.es.md">Español</a> | <a href="README.pt.md">Português</a> | <a href="README.it.md">Italiano</a>
</p>

> Step 4 で *どこ* を指すかを覚えたなら、このステップはそれを *コマンド*
> に変える方法。cite + apply_edit サイクル。
> 約 10 分。

このステップはキャンパスの最深部 — 26 ペルソナのウォークスルーが
ここにあります ([`personas/`](personas/))。最初はご自分の領域のものを
1 本だけ追えば十分です。

## 5.1 · 4 つのコマンドパターン

| パターン | 場所 | 入力の形 |
|---|---|---|
| **Chat (BYOM チャット)** | 右側の AI パネル | 自然言語 + cite anchor が自動添付 |
| **Terminal CLI** | ⌘J でトグル、その中で `claude` / `codex` / `gemini` | shell prompt |
| **外部 MCP クライアント** | Claude Code / Cursor / Windsurf / Zed | そのクライアントのチャット欄 |
| **Inline cite link** | 応答内の `[B14](xlsx://q3.xlsx#B14)` | クリック → その位置へジャンプ |

## 5.2 · Cite + apply_edit サイクル

```
[Step 4 で領域を指す]
   → cite anchor が AI パネルに添付
   → 自然言語プロンプト
   → LLM が htmlook_apply_edit を呼び出す
   → ファイルが変更される
   → file watcher が右ペインを自動リロード
```

コア動画 4 本 (各 30 秒):

| # | 動画 | パターン |
|---|---|---|
| 7 | [Cite the cell. Get the narrative.](../videos/features/07-advanced-01-xlsx-cite.mp4) | xlsx セル cite |
| 8 | [14:14 → paragraph.](../videos/features/08-advanced-02-live-cue-cite.mp4) | 動画タイムスタンプ cite |
| 9 | [One cite. Three files.](../videos/features/09-advanced-03-multi-target.mp4) | 1 つの cite → 複数ファイルにパッチ |
| 17 | [Cross-file anchors. Recorded.](../videos/features/17-advanced-11-cross-link.mp4) | `.htmlook/links.json` サイドカー |

## 5.3 · ペルソナウォークスルー (26 本)

自分の職種 / 領域の *1 日* ワークフロー。60-70 秒の mp4 + フォローアロー
可能な sample workspace + ステップバイステップの `WALKTHROUGH.md`。

詳細カタログ: [`personas/INDEX.md`](personas/INDEX.md)。おすすめの順番は
職種別にグループ化されています:

- **開発**: [`personas/01-hf-claude/`](personas/01-hf-claude/) →
  [`02-hf-llama/`](personas/02-hf-llama/) →
  [`03-dev-pr-docs/`](personas/03-dev-pr-docs/)
- **コンテンツ**: [`personas/04-creator-podcast/`](personas/04-creator-podcast/) →
  [`12-press-editor/`](personas/12-press-editor/) →
  [`15-picture-book/`](personas/15-picture-book/) →
  [`22-hobby-fiction/`](personas/22-hobby-fiction/)
- **分析**: [`personas/09-data-analyst/`](personas/09-data-analyst/) →
  [`11-finance-report/`](personas/11-finance-report/) →
  [`10-research-notes/`](personas/10-research-notes/) →
  [`06-economy-analyst/`](personas/06-economy-analyst/)
- **法務 / 翻訳**: [`personas/08-legal-redline/`](personas/08-legal-redline/) →
  [`07-translator-book/`](personas/07-translator-book/) →
  [`05-domain-battery/`](personas/05-domain-battery/)
- **教育 (先生)**: [`personas/17-teacher-quiz/`](personas/17-teacher-quiz/) →
  [`18-teacher-newsletter/`](personas/18-teacher-newsletter/) →
  [`19-teacher-record/`](personas/19-teacher-record/)
- **教育 (学生)**: [`personas/20-student-notes/`](personas/20-student-notes/) →
  [`24-student-flashcard/`](personas/24-student-flashcard/) →
  [`23-homework-helper/`](personas/23-homework-helper/) →
  [`21-kid-coding/`](personas/21-kid-coding/) →
  [`14-kids-science-mag/`](personas/14-kids-science-mag/)
- **ビジネス**: [`personas/16-corp-deck/`](personas/16-corp-deck/) →
  [`13-product-prd/`](personas/13-product-prd/)
- **日常**: [`personas/25-recipe-card/`](personas/25-recipe-card/) →
  [`26-mobile-news/`](personas/26-mobile-news/)

## 5.4 · フォローアローのパターン

各ペルソナフォルダの中:

- `WALKTHROUGH.md` — ステップバイステップ (`[VIEW]` / `[AI]` マーク)
- `before/` — 編集前の状態 (視覚比較用)
- `after/` — 編集後の状態 (AI なしのユーザーも結果確認可)
- ドメインコンテンツファイル (md / html / pdf / xlsx / svg / py / mp3 など)

## 5.5 · LLM 非依存 — ベンダースワップ

同じ cite + apply_edit ワークフローが 9 ベンダーのどこでも同じように
動きます。[Step 3](../03-byom-setup/) で別のベンダーを追加してスワップ
すれば同じ結果。

## ✅ Step 5 チェックポイント

- 自分の職種に近いペルソナの動画 (60-70 秒) を 1 本視聴した。
- そのペルソナフォルダの `WALKTHROUGH.md` の `[VIEW]` ステップまで
  追った。
- (AI セットアップ済みなら) `[AI]` ステップを実行 → 右ペインがリロード
  されることを確認。
- (AI なしなら) `before/` と `after/` を分割ビューで比較。

3 つ揃ったら → [Step 6 · save-as-skill](../06-save-as-skill/) — よく使う
ワークフローをアプリに永久登録。

## 詳しくは

- [`personas/INDEX.md`](personas/INDEX.md) — 26 ペルソナのカタログ +
  動画 ↔ フォルダのマッピング。
- [`personas/README.md`](personas/README.md) — sample workspace の
  使い方。
- [`../03-byom-setup/AI_GUIDE.md`](../03-byom-setup/AI_GUIDE.md) — 約
  22 種の MCP ツール + AI エージェントの出力トーンガイド。
