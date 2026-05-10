# 21 · kid-coding — star.py + turtle 결과

> 영상: `demo/persona_units/kid-coding/renders/kid-coding_voiced_bgm.en+ko.mp4`

어린이가 좌측에 `star.py` 코드를, 우측에 turtle 그림 결과 (정적 SVG) 를
띄우고 각도 한 줄을 바꿔서 별의 모양을 변형. 친근한 한국어 튜터 모드.

## 사전 준비

- HTMLook Pro
- (선택) LLM (한국어 친근체 가능 모델)
- HTMLook 은 Python 을 *실행* 하지 않습니다. turtle 결과는 정적 SVG 로
  미리 그려져 있습니다. 실제 코드 실행은 외부 IDE 가 담당.

## 단계

### 1. [VIEW] 좌측 star.py, 우측 star.svg

- 좌측: `21-kid-coding/star.py` (5각 별, 144도)
- 우측: `21-kid-coding/star.svg` (5각 별 그림)

### 2. [AI] for 반복문 설명

좌측에서 `for i in range(5):` 줄 드래그-선택.

LLM 에 (친근 한국어 톤):

> *"이 for 반복문이 무슨 뜻인지 4학년 친구한테 설명해 주는 것처럼 말해줘.
> 그리고 우측 journal.md 의 *오늘 배운 것* 칸에 한 줄 적어 줘."*

LLM 이 `htmlook_apply_edit` 으로 journal.md 의 *오늘 배운 것* 영역 patch.

### 3. [AI] 144 → 72 변경, 별 모양 변형

좌측 star.py 에서 `144` 숫자 드래그-선택. LLM 에:

> *"이 각도를 72 로 바꾸면 별이 어떻게 바뀌는지 설명해 줘. 그리고 코드 +
> 결과 svg 둘 다 patch."*

LLM 이:
1. `htmlook_apply_edit` 으로 star.py 의 `range(5)` → `range(10)`, `t.right(144)` → `t.right(72)`
2. star.svg 도 10각 별 도형으로 교체
3. journal.md 에 *"144 → 72 로 바꿨더니 ..."* 한 줄 추가

### 4. [VIEW] 우측 reload

- star.svg 가 10각 별 (`🌟`) 로 보임
- journal 에 5 단계 학습 정리 + *다음 도전* 2 개 (무지개 별 / 별 안의 별)

### 5. [AI 없는 사용자] before/after 비교

- 좌측 셋: `21-kid-coding/before/{star.py,star.svg,journal.md}`
- 우측 셋: `21-kid-coding/after/{star.py,star.svg,journal.md}`

## 검증 포인트

- ✅ `htmlook_pane_pair` (py + svg)
- ✅ `htmlook_selection_text` (코드 한 줄 / 숫자)
- ✅ `htmlook_apply_edit` (py + svg + journal 동시)
- ⚠️ HTMLook 은 Python 인터프리터가 *없습니다*. turtle 결과 svg 는 외부 도구
  결과물을 갈아 끼우는 흐름입니다.
- ⚠️ Kokoro 친근 한국어 음성 / Whisper align 은 외부 CLI

## 다음 페르소나

`22-hobby-fiction/` — SF 소설 outline → scene 작성
