# Tutorial Path Reference

> 본 캠퍼스는 8 step 으로 설계된 step-by-step 튜토리얼. 각 step 폴더에
> `README.md` (해당 step 가이드) 가 있고, 영상 / 샘플 / 워크스루는 step 안에
> 들어 있습니다. v1.0 release-candidate 기준.

## Step 개요

| Step | 폴더 | 핵심 약속 | 시간 |
|---|---|---|---|
| 1 | [`01-getting-started/`](../01-getting-started/) | 설치 + 첫 launch | 3 min |
| 2 | [`02-first-file/`](../02-first-file/) | HTML / MD / PDF / 영상 열기 | 5 min |
| 3 | [`03-byom-setup/`](../03-byom-setup/) | BYOM provider 1개 키 등록 | 5 min |
| 4 | [`04-editing/`](../04-editing/) | paint / region / element pick | 5 min |
| 5 | [`05-command/`](../05-command/) | terminal / chat / apply_edit | 10 min |
| 6 | [`06-save-as-skill/`](../06-save-as-skill/) | 워크플로우 캡처 → tool 등록 | 5 min |
| 7 | [`07-bundled-profiles/`](../07-bundled-profiles/) | HyperFrames / Slidev / Quarto / D2 / Astro / Marimo / Excalidraw / Manim | 5 min |
| 8 | [`08-extend/`](../08-extend/) | 자기 Profile 작성 + 카탈로그 | 선택 |

처음 onboarding **30-40 분 이내** 에 핵심 기능을 모두 학습 완료.

## Step → 영상 mapping

각 step 에서 시청할 영상 (mp4 본체는 [`../videos/features/`](../videos/features/)
공용 디렉토리에 보관):

### Step 1 · install & first launch

- BASIC #1 [Drop. Open. Done.](../videos/features/01-basic-01-drop-open.mp4)
- BASIC #2 [Folder ready.](../videos/features/02-basic-02-workspace.mp4)

### Step 2 · open a file

- BASIC #3 [Type left. See right. Live.](../videos/features/03-basic-03-md-live-edit.mp4) (md live edit)
- BASIC #4 [Click anything. Edit it.](../videos/features/04-basic-04-html-split.mp4) (html split)
- BASIC #6 [Pick what you see.](../videos/features/06-basic-06-html-4mode.mp4) (4-mode)
- ADV [Two keys. Three views.](../videos/features/10-advanced-04-multi-pane.mp4) (multi-pane)
- ADV [Frame check. No scrub.](../videos/features/15-advanced-09-thumbnail.mp4) (thumbnail)
- ADV [Click §3.2. You're there.](../videos/features/16-advanced-10-outline.mp4) (outline)

### Step 3 · BYOM setup

- ADV [Swap the LLM. Keep the workflow.](../videos/features/13-advanced-07-mcp-swap.mp4) (mcp-swap)
- ADV [It just reloaded.](../videos/features/11-advanced-05-auto-reload.mp4) (auto-reload — 모델 응답 후)

### Step 4 · editing (paint / region / element pick)

- BASIC #5 ⭐ [Drag. Tell the LLM.](../videos/features/05-basic-05-region-cite.mp4) (region cite — AI 진입점)
- ADV [Click sentence 5. Clip ships.](../videos/features/14-advanced-08-sentence-id.mp4) (sentence id)

### Step 5 · command (terminal / chat / apply)

- ADV [Cite the cell. Get the narrative.](../videos/features/07-advanced-01-xlsx-cite.mp4) (xlsx-cite)
- ADV [14:14 → paragraph.](../videos/features/08-advanced-02-live-cue-cite.mp4) (live-cue-cite)
- ADV [One cite. Three files.](../videos/features/09-advanced-03-multi-target.mp4) (multi-target)
- ADV [Cross-file anchors. Recorded.](../videos/features/17-advanced-11-cross-link.mp4) (cross-link)
- 26 페르소나 영상 ([`05-command/personas/INDEX.md`](../05-command/personas/INDEX.md))

### Step 6 · save-as-skill

- ADV [Add a tool. Three fields.](../videos/features/12-advanced-06-tool-wizard.mp4) (tool-wizard)

### Step 7 · bundled profiles

- 영상 별도 없음. [`../profiles/`](../profiles/) 시드 폴더 + Add wizard 카드로 학습.

### Step 8 · extend

- 영상 별도 없음. [`../08-extend/PRODUCTION.md`](../08-extend/PRODUCTION.md) +
  [`../scripts/build-catalog.mjs`](../scripts/build-catalog.mjs) 참고.

## 자료 위치

- **영상 mp4**: [`../videos/features/`](../videos/features/) (17 feature) +
  [`../videos/`](../videos/) (26 페르소나)
- **페르소나 walkthroughs**: [`../05-command/personas/`](../05-command/personas/)
  (NN-name/WALKTHROUGH.md + before/after/)
- **Profile 시드**: [`../profiles/`](../profiles/) (8 종)
- **워크스페이스 시드**: [`../sample_workspaces/`](../sample_workspaces/)
  (75 폴더 — 추가 도메인)
- **카탈로그 manifest**: [`../catalog.json`](../catalog.json) (앱 Wizard fresh-fetch)

## 두 layer 의 학습 — 영상 + 인터랙티브

캠퍼스 영상은 *what (무엇이 되는지)*. HTMLook Pro 내장 인터랙티브 walkthrough
(Settings → Tutorials) 는 *how (어떻게 하는지)*. 영상에 등장하는 17 feature
모두 인터랙티브 가이드가 1:1 매칭.

| Layer | 어디서 | 길이 | 역할 |
|---|---|---|---|
| 영상 (캠퍼스) | `videos/features/`, `videos/` | 30 s / 60-70 s | 결과 보여주기 |
| 인터랙티브 (앱) | HTMLook Pro · Settings → Tutorials | 4 step | 직접 따라하기 |

## 다음 단계

- [`../08-extend/PRODUCTION.md`](../08-extend/PRODUCTION.md) — 영상 제작 표준 + 역검증 절차
- [`../08-extend/FEATURES.md`](../08-extend/FEATURES.md) — 17 feature 영상 카탈로그
- [`../05-command/personas/INDEX.md`](../05-command/personas/INDEX.md) — 26 페르소나 카탈로그
- Deep-dive 데모: [htmlook.app/demos/lv1.html](https://htmlook.app/demos/lv1.html) ·
  [lv2](https://htmlook.app/demos/lv2.html) · [lv3](https://htmlook.app/demos/lv3.html)
