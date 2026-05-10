# Step 8 · Extend (자기 Profile 작성 + 카탈로그)

> 8 step 의 마지막. 자기만의 profile 을 만들어 카탈로그에 등록하는 법.
> 시간 무제한 (작성하는 도구의 복잡도에 따름).

이 step 은 *learner* 가 *contributor* 로 전환되는 곳. v1.0 GA 이후 외부
profile 을 카탈로그에 PR 받을 예정.

## 8.1 · Profile = 무엇

```
profiles/<id>/
├─ profile.json   ← manifest (id, name, category, description, tags, license)
├─ SKILL.md       ← Skill v0.3 묶음 (이 profile 이 등록하는 도구들)
├─ README.md      ← human-readable 설명
└─ seed/          ← 시드 콘텐츠 (사용자가 install 시 복사받는 파일)
```

샘플: [`../profiles/hyperframes/`](../profiles/hyperframes/) (가장 단순).

## 8.2 · 빠른 시작 — 빈 profile 생성

```bash
cd /Users/vincent/Works/htmlook_campus/profiles
mkdir my-tool
cat > my-tool/profile.json <<'EOF'
{
  "id": "my-tool",
  "name": "My Tool",
  "category": "misc",
  "description": "한 줄 설명",
  "tags": ["mytool"],
  "license": "MIT"
}
EOF
mkdir my-tool/seed
echo "# seed example" > my-tool/seed/example.md
echo "# My Tool Profile" > my-tool/README.md
```

## 8.3 · SKILL.md — Skill v0.3 묶음

```markdown
# My Tool Skills

## render

- prompt: 현재 워크스페이스를 my-tool 로 렌더해 줘
- needs: [active_file, workspace_files]
- produces: [apply_edit]
```

자세한 spec: HTMLook 본 레포의 `docs/skills/v0.3.md`.

## 8.4 · 카탈로그 빌드

```bash
node scripts/build-catalog.mjs > catalog.json
```

CI 가 매 push 마다 자동으로 실행 (`.github/workflows/catalog.yml`). 신규 profile
폴더가 추가되면 `catalog.json` 의 `entries[]` 가 자동 업데이트.

빌더 소스: [`../scripts/build-catalog.mjs`](../scripts/build-catalog.mjs).

## 8.5 · sample_workspaces/ 시드 추가

profile 본체 외에 도메인-별 추가 시드를 [`../sample_workspaces/`](../sample_workspaces/)
에 넣을 수 있음. 예: `my-tool-marketing-page/`, `my-tool-api-docs/`.

각 시드 폴더에 `.htmlook/workspace.json` 을 두면 카탈로그 빌더가 자동으로
`uses_profiles` / `category` / `description` 을 추출:

```json
{
  "profiles": { "my-tool": { "active": true } },
  "category": "marketing",
  "description": "My Tool 으로 만드는 마케팅 페이지 시드"
}
```

## 8.6 · 영상 추가 (선택)

자기 profile 의 60-70 초 walkthrough 또는 30 초 feature spotlight 를 만들고
싶다면:

- 영상 표준 + 역검증 절차: [`PRODUCTION.md`](PRODUCTION.md)
- 17 feature 영상 카탈로그 (참고 대상): [`FEATURES.md`](FEATURES.md)
- 영상 빌드 도구: [`../profiles/hyperframes/`](../profiles/hyperframes/) (캠퍼스
  자체가 이 도구로 제작)

## 8.7 · PR 워크플로우

1. fork → 자기 profile 폴더 add
2. `node scripts/build-catalog.mjs > catalog.json`
3. PR open → CI 의 `build catalog` workflow 가 catalog 자동 검증
4. v1.0 GA 이후 review 후 merge

## ✅ Step 8 체크포인트

- profile 1 개를 [`../profiles/`](../profiles/) 에 mkdir.
- `profile.json` + `seed/` 최소 구성.
- `node scripts/build-catalog.mjs` 가 새 entry 를 catalog.json 에 추가하는 것 확인.

여기까지 오면 캠퍼스 8 step 완주. 도메인-specific profile 을 추가해
주세요 — v1.0 GA 의 카탈로그가 [`htmlook.app/catalog`](https://htmlook.app/catalog)
에서 fresh-fetch.

## Reference

- [`PRODUCTION.md`](PRODUCTION.md) — 영상 제작 표준 + 역검증 절차 + 자막
  mux 레시피.
- [`FEATURES.md`](FEATURES.md) — 17 feature 영상 카탈로그 (hooks + accents).
- [`../scripts/build-catalog.mjs`](../scripts/build-catalog.mjs) — 카탈로그 빌더 소스.
- [`../catalog.json`](../catalog.json) — 현재 카탈로그 (8 profile + 49 seed).
