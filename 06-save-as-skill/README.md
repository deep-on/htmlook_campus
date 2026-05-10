# Step 6 · Save-as-Skill (워크플로우 캡처)

> Step 5 에서 익힌 cite + apply_edit 사이클을 *앱이 외운다*. 다음에 한 번
> 클릭으로 재실행.
> ~ 5 분.

이번 step 끝나면: 워크스페이스에 자기 도구가 1 개 등록되어 사이드바의
*Tools* 섹션 또는 ⌘K 의 빠른 실행 (Add wizard) 에 노출됩니다.

## 6.1 · *Save as Skill* — 진입

방금 LLM 과 한 대화 / apply_edit 사이클이 좋았다면 우측 AI 패널 상단 *⋯* →
**Save as Skill** 클릭.

다이얼로그가 뜨면 3 줄만 채우면 됩니다:

| 필드 | 예시 |
|---|---|
| Name | *Tighten subtitle* |
| When to use | *부제가 너무 짧을 때 한 줄 확장* |
| Default prompt | *현재 cite 영역의 부제를 Apex 가치 (edge compute, 빠른 배포) 로 한 줄 늘려서 apply_edit* |

> 영상: [ADV · Add a tool. Three fields.](../videos/features/12-advanced-06-tool-wizard.mp4)
> (30 s)

## 6.2 · 어디에 저장됨?

`.htmlook/skills/<name>.skill.json` (워크스페이스 내부, v0.3 spec). 워크스페이스를
공유하면 동료도 그대로 쓸 수 있습니다.

전역 (모든 워크스페이스에서) 사용하려면 **Settings → Skills → Promote to global**.

## 6.3 · Add wizard 에서 부르기

⌘K 또는 사이드바 *+* 버튼 → 카탈로그 + 자기 skill 들이 카드로 표시. 카드
클릭 → 자동 실행 (현재 selection 컨텍스트 사용).

## 6.4 · Skill v0.3 spec — 무엇이 들어 있는지

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

`needs` / `produces` 는 MCP 도구 이름. 자세한 spec 은 HTMLook 본 레포의
`docs/skills/v0.3.md` 참고 (v1.0 GA 시점에 공개).

## 6.5 · Skill ↔ Profile 차이

- **Skill** = *행동* 의 캡처 (단일 prompt + 도구 조합). 워크스페이스 또는 user 글로벌.
- **Profile** = *툴 + 시드 콘텐츠 + Skill 묶음* 패키지. v1.0 에 8 종 bundled
  ([Step 7](../07-bundled-profiles/)).

자기만의 Profile 을 만드는 방법은 [Step 8 · extend](../08-extend/) 에 있음.

## ✅ Step 6 체크포인트

- 우측 AI 패널 *Save as Skill* 다이얼로그를 한번 열어봤다.
- 3 줄 채워서 skill 1 개 저장.
- ⌘K 의 카드에 그 skill 이 보임 — 클릭으로 재실행.

다 맞으면 → [Step 7 · bundled profiles](../07-bundled-profiles/)

## 더 자세히

- [`../05-command/personas/`](../05-command/personas/) — 각 페르소나가 어떤 skill
  으로 저장될지 상상해 보세요. 패턴 잡힘.
