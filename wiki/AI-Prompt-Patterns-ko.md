# 프롬프트 패턴

> 재사용 프롬프트 골격. 13-페르소나 시나리오 셋에서 검증된 루프들.

## 1. "사용자 무엇을 보고 있나?" (저렴한 오리엔테이션)

명시적 상태가 없으면 모든 대화는 이걸로 시작.

```
1. workspace_info     → root, 탭 수
2. active_file        → 경로 + 크기
3. (HTML / .md)  layout_map  → 구조
   (.pdf)        outline     → heading tree + 페이지 수
   (video)       video_info  → 길이 + 코덱
```

3회 호출, max ~50 KB 반환. 이후 방을 안다. 편집 계획 전까지 무거운 capture 도구 피하기.

## 2. 왕복 편집 (워크호스)

```
capture_selector(target)      ← before.png
apply_edit(find, replace)     ← 변경
capture_selector(target)      ← after.png
capture_diff(before, after)   ← 검증
```

메모:
- 대기 불필요 — 뷰어 리로드가 `htmlook:apply-edit-reload` 이벤트로 구동, apply_edit 응답 반환 전에 발화.
- target bbox 바깥 변경이 diff 에 보이면 CSS cascade 가 의도보다 넓음 — 성공 선언 전 조사.

## 3. "보여줘, 그 다음 변경" (사용자 주도)

사용자가 "이거 더 명확히" 라고만 할 때:

```
selection_text  /  selection_html  /  element_active   ← 초점 읽기
region_current_png                                     ← 영역 캡처가 있을 때
… 이 입력들로부터 추론 …
apply_edit(...) or insert_at_selection(...)
```

이 wiki 의 현재 상태 컨텍스트 ("Workspace root", "Active file") 가 시작점 — 단 항상 선택 도구로 재확인, 사용자가 움직였을 수 있음.

## 4. 다중 후보 탐색

```
for variant in candidates:
    apply_edit(find, variant)
    capture_selector(target)
    sketch_save  / annotation_add  ← 결과 보존
    (variant=원래값 으로 다시 apply_edit 해서 undo)
```

각 후보 작게. 파일을 5번 실제 mutate 하지 말고 — 캡처, undo, 다시 캡처.

## 5. 오디오 / 비디오 리뷰

```
video_info                              ← 길이, fps
video_scene_detect(threshold=0.3)       ← cut 리스트
for cut in cuts[:N]:
    capture_video_frame_region(time=cut.start, rect=center)
    → 챕터 제목 제안
video_chapter_create(...)
```

## 6. PDF 인용 chain

```
pdf_text_spans(page)                  ← 문장 찾기
pdf_citation_anchor(page)             ← htmlook:// URL
pdf_highlight_add(rects, label)       ← 영구 마커
agent_message_post(body: "<인용> — <링크>")   ← 사용자 보게
```

## 7. 다중 에이전트 핸드오프

알려진 contentious 편집 적용 전:

```
audit_log_query(tool=apply_edit, path=현재파일, since=now-300s)
  → 최근 다른 에이전트 편집? yes 면 메시지 post:
agent_message_post(to=any, subject="claim: hero.html for 5min")
sleep ~3s ← 사용자/다른 에이전트가 chatpanel 로 반응 가능
apply_edit(...)
```

## 8. "멈춤, 사람에게 묻기" surface

확인 없이 진행하면 안 된다고 판단 시:

- `confirm({ title, message })` → 사용자 클릭까지 block, boolean 반환
- `request_user_input({ prompt })` → 문자열 반환
- `wait_for_user_action({ hint })` → 설명한 hint 버튼 클릭까지 block
- `show_toast({ message, level })` → fire-and-forget 알림
- `chatpanel_post({ text })` → ChatPanel 에 메시지 push (사용자 입력 박스가 아닌 대화 스트림)

기본: "되돌릴 수 없는 액션" 에 `confirm`, "추정 어려운 값 필요" 에 `request_user_input`.

## 9. 장기 plan

다단계 plan (예: "오디오 transcript 에서 슬라이드 덱 재구성") 은 명시적으로 audit log 에 체크포인트:

```
agent_message_post(subject="plan",
                   body="1) transcript 추출 2) outline 3) draft 4) 리뷰")
… 1 단계 …
agent_message_post(subject="plan", body="step 1 done")
…
```

사용자가 audit log 안 읽고도 언제든 plan 확인 가능. future-you (다음 세션) 가 메시지 읽고 resume.

## 안티 패턴

- **캡처 스팸**: 20× `capture_viewport`. 항상 가장 타이트한 scope.
- **모호한 find 의 `apply_edit`**: 긴 자연어 find 가 `MULTIPLE_MATCHES` 초래. selector / selection 대신.
- **rate limit 무시**: `RATE_LIMITED` 받으면 back off — retry-loop 하지 말 것. limiter 가 사용자 CPU + 뷰어 인터랙티브성 보호.
- **메시지 폴**: 2 s 보다 빠르면 drop. 사용자가 ping 하도록 요청.
- **조용한 실패**: tool 이 `ok: false` 반환 시 사용자에게 surface (`show_toast` 또는 chat). 삼키지 말 것.

## 다음

- [에러 & 복구 →](AI-Errors-Recovery-ko.md)
- [개요](AI-Overview-ko.md) 로
