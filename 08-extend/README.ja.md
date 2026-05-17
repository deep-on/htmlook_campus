# Step 8 · Extend (自分の Profile を書く + カタログ)

<p align="center">
  <a href="README.md">English</a> | <a href="README.ko.md">한국어</a> | <b>日本語</b> | <a href="README.de.md">Deutsch</a> | <a href="README.fr.md">Français</a> | <a href="README.es.md">Español</a> | <a href="README.pt.md">Português</a> | <a href="README.it.md">Italiano</a>
</p>

> 8 ステップの最後。自分の profile を書いてカタログに登録する方法。
> 所要時間は無制限 (書く道具の複雑さ次第)。

このステップは *learner* が *contributor* に変わる場所です。v1.0 GA
以後、外部 profile をカタログに PR で受け入れる予定です。

## 8.1 · Profile とは

```
profiles/<id>/
├─ profile.json   ← manifest (id, name, category, description, tags, license)
├─ SKILL.md       ← Skill v0.3 バンドル (この profile が登録するツール群)
├─ README.md      ← 人間向け説明
└─ seed/          ← シードコンテンツ (install 時にユーザーへコピー)
```

サンプル: [`../profiles/hyperframes/`](../profiles/hyperframes/) (もっとも
シンプル)。

## 8.2 · クイックスタート — 空の profile を作る

```bash
cd /Users/vincent/Works/htmlook_campus/profiles
mkdir my-tool
cat > my-tool/profile.json <<'EOF'
{
  "id": "my-tool",
  "name": "My Tool",
  "category": "misc",
  "description": "一行の説明",
  "tags": ["mytool"],
  "license": "MIT"
}
EOF
mkdir my-tool/seed
echo "# seed example" > my-tool/seed/example.md
echo "# My Tool Profile" > my-tool/README.md
```

## 8.3 · SKILL.md — Skill v0.3 バンドル

```markdown
# My Tool Skills

## render

- prompt: 現在のワークスペースを my-tool でレンダーして
- needs: [active_file, workspace_files]
- produces: [apply_edit]
```

詳しい spec: HTMLook 本リポの `docs/skills/v0.3.md`。

## 8.4 · カタログのビルド

```bash
node scripts/build-catalog.mjs > catalog.json
```

CI が push のたびに自動実行 (`.github/workflows/catalog.yml`)。新しい
profile フォルダが追加されると `catalog.json` の `entries[]` が自動で
更新されます。

ビルダーのソース: [`../scripts/build-catalog.mjs`](../scripts/build-catalog.mjs)。

## 8.5 · sample_workspaces/ にシードを追加

profile 本体に加えて、ドメイン固有の追加シードを
[`../sample_workspaces/`](../sample_workspaces/) に入れられます。例:
`my-tool-marketing-page/`、`my-tool-api-docs/`。

各シードフォルダに `.htmlook/workspace.json` を置くと、カタログビルダー
が `uses_profiles` / `category` / `description` を自動で抽出します:

```json
{
  "profiles": { "my-tool": { "active": true } },
  "category": "marketing",
  "description": "My Tool で作るマーケティングページのシード"
}
```

## 8.6 · 動画を追加 (任意)

自分の profile に 60-70 秒のウォークスルー、または 30 秒の機能スポット
ライトを作りたい場合:

- 動画標準 + 逆検証手順: [`PRODUCTION.md`](PRODUCTION.md)
- 17 機能の動画カタログ (参考): [`FEATURES.md`](FEATURES.md)
- 動画ビルドツール: [`../profiles/hyperframes/`](../profiles/hyperframes/)
  (キャンパス自体がこの道具で制作)

## 8.7 · PR ワークフロー

1. fork → 自分の profile フォルダを add
2. `node scripts/build-catalog.mjs > catalog.json`
3. PR を開く → CI の `build catalog` ワークフローが catalog を自動検証
4. v1.0 GA 以後にレビューしてマージ

## ✅ Step 8 チェックポイント

- profile を 1 つ [`../profiles/`](../profiles/) に mkdir した。
- 最小構成の `profile.json` + `seed/` が揃っている。
- `node scripts/build-catalog.mjs` が catalog.json に新エントリを
  追加することを確認。

ここまで来たらキャンパス 8 ステップ完走。ドメイン特化の profile を
ぜひ追加してください — v1.0 GA のカタログが
[`htmlook.app/catalog`](https://htmlook.app/catalog) から fresh-fetch
します。

## Reference

- [`PRODUCTION.md`](PRODUCTION.md) — 動画制作標準 + 逆検証手順 + 字幕
  mux レシピ。
- [`FEATURES.md`](FEATURES.md) — 17 機能の動画カタログ (hooks + accents)。
- [`../scripts/build-catalog.mjs`](../scripts/build-catalog.mjs) —
  カタログビルダーのソース。
- [`../catalog.json`](../catalog.json) — 現在のカタログ (8 profile +
  75 seed)。
