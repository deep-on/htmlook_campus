# 18 · teacher-newsletter — 학구 정책 → 학부모 친화 newsletter

> 영상: `demo/persona_units/teacher-newsletter/renders/teacher-newsletter_voiced_bgm.en+ko.mp4`

학구 공문의 딱딱한 정책 본문을 cite 해서 4학년 학급 학부모 안내문 (헤드라인
1 + 친근 bullet 3 + 회신 슬립) 으로 변환.

## 사전 준비

- HTMLook Pro
- (선택) LLM

## 단계

### 1. [VIEW] 좌측 memo.md (정책), 우측 newsletter.html (학급 안내문)

- 좌측: `18-teacher-newsletter/memo.md` — 학구 공문 발췌
- 우측: `18-teacher-newsletter/newsletter.html` — 헤드라인 / 본문 / 회신 슬립 자리

### 2. [AI] 정책 본문 cite + 학부모 paraphrase

좌측 *## 정책 본문 (발췌)* 단락 드래그-선택.

LLM 에:

> *"학부모 친화 톤으로 paraphrase. 헤드라인 1 + 부드러운 bullet 3 + 회신 슬립
> 안내. 가능하면 이모지 한두 개로 친근함."*

LLM 이:
1. `htmlook_selection_text` 로 본문 anchor
2. `htmlook_apply_edit` 으로 newsletter.html 의 `<h1>`, `<ul>`, body paragraph 영역 동시 patch

### 3. [AI] 일정 라인 추가 + 회신 슬립 boxes

좌측 *## 핵심 일정* 섹션 cite.

LLM 에:

> *"일정 두 줄 (5/7 설명회, 5/13 시행) 을 본문 위에 한 줄 강조. 회신 슬립의
> 체크박스도 ✔ 확인 / ✘ 문의 / 참석 / 불참 으로 톤 다듬어."*

`htmlook_apply_edit` → 일정 단락 + `.reply` 영역 patch.

### 4. [VIEW] 우측 reload

- 헤드라인이 *"5월 13일부터, 수업 시간엔 휴대전화는 잠시 안녕!"*
- 친근한 bullet 3 줄
- 일정 단락
- 회신 슬립의 체크박스 4 종

### 5. [AI 없는 사용자] before/after 비교

- 좌측: `18-teacher-newsletter/before/newsletter.html`
- 우측: `18-teacher-newsletter/after/newsletter.html`

## 검증 포인트

- ✅ `htmlook_pane_pair` (정책 + newsletter)
- ✅ `htmlook_selection_text` (정책 본문 단락)
- ✅ `htmlook_apply_edit` (헤드라인 + 본문 + bullets + reply 동시)
- ⚠️ Kokoro recap / Whisper align 은 외부 CLI

## 다음 페르소나

`19-teacher-record/` — 일일 노트 → 학생별 종합 의견
