# AI 어시스턴트

> Bring Your Own Model. 우측 패널은 *내* AI provider 를 호출하는 채팅 — 우리 서버를 거치지 않음.

## 열기 / 닫기

⌘I 로 우측 AI 어시스턴트 토글. 첫 실행 시 5-카드 가이드 setup. 이후 ⌘I 는 단순 토글.

## Provider preset

원클릭 preset 8 종:

| Provider | 어울리는 용도 |
|---|---|
| OpenAI | 가장 강력, 다양한 모델 |
| DeepSeek | 저렴, 빠름, 강한 reasoning |
| Mistral | EU 호스팅, 프랑스어 + 영어 강함 |
| Together | 다양한 오픈 모델 호스팅 |
| Groq | 최저 latency, Llama 계열 |
| Cerebras | 빠른 Llama / Qwen 추론 |
| Ollama | 로컬, 키 불필요 |
| Custom | OpenAI-호환 URL 무엇이든 |

하나 선택 → API 키 paste → 기본 모델 선택 → 끝.

## 패널 구성

- 상단 — 설정 톱니 + 히스토리 drawer
- 대화 위 — HTMLook 이 현재 워크스페이스 + 파일에 관련된다고 판단한 확장의 chip
- 대화 본체 — 내 메시지, 어시스턴트의 응답, 어시스턴트가 워크스페이스에 취한 액션이 인라인
- 하단 — 입력 박스 + 첨부용 📎 버튼

## 일 시키기

평소 채팅처럼 타이핑. 어시스턴트가 워크스페이스 읽기 권한을 갖고 다음을 할 수 있음:

- 현재 파일 읽기
- 다른 파일을 새 탭에 열기
- 파일을 제자리에서 편집 (첫 시도 시 확인)
- 새 파일 만들기
- 화면에 보이는 것 캡처
- 활성화된 확장 사용

어시스턴트가 워크스페이스를 *변경* 하려는 첫 시도에 HTMLook 이 4-버튼 동의 모달:

- **이번만** — 1회 허용
- **이 워크스페이스에서** — 워크스페이스 기억
- **모든 워크스페이스** — 글로벌 허용
- **거부**

언제든 *Settings → AI* 에서 해제.

## 첨부

📎 (또는 입력 박스에 drag):

- 이미지 (`.png`, `.jpg`, …)
- 현재 Paint 캔버스
- PDF 페이지 (PDF 뷰어의 *AI 에 페이지 보내기*)
- 워크스페이스 파일 (텍스트류)

입력 위 배지가 메시지당 첨부 수.

## 채팅 히스토리

워크스페이스별 `.htmlook/` 에 저장. 히스토리 drawer 에서 스레드 재오픈 · 핀 · 삭제. 스레드는 markdown 으로 export.

## 취소 + 재시도

⌘. 로 스트리밍 응답 취소. 마지막 user turn 에 *Retry* affordance.

## 프라이버시

outbound 는 설정한 provider 로만. system prompt + 메시지 + 명시적으로 참조한 파일 발췌가 호출 내용. HTMLook 은 Deep-On 서버를 통해 프록시 안 함.

## 다음

- [확장 (Extensions) →](Skills-ko.md)
- [Settings →](Settings-ko.md)
