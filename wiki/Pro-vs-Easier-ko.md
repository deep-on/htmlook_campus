# Pro vs Easier 차이점

> 두 청중을 위한 두 빌드. 누가 쓰느냐로 고르세요.

| | **HTMLook Pro** | **HTMLook Easier** |
|---|---|---|
| **타겟 사용자** | 파워 유저 · 개발자 · 본인 AI 키 보유 prosumer | 비전문가 · 일반 reader |
| **AI** | Bring Your Own Model — OpenAI / DeepSeek / Mistral / Together / Groq / Cerebras / Ollama / Custom 직접 키 | 내장 구독형 AI |
| **터미널** | 셸 + AI preset (Claude / Codex / Gemini / Shell) 풀 터미널. AI 에이전트가 워크스페이스 파일을 보고 작업 가능. | (없음) |
| **Paint** | 어떤 파일 위에든 스케치 캔버스. 7 도구, undo / redo, PNG export, 채팅에 드래그. | (없음) |
| **음성 메모** | 워크스페이스에 AAC 메모 녹음, transcript 는 본인이 관리. | (없음) |
| **확장 (Extensions)** | 직접 작성한 명령과 렌더러를 markdown 파일로 워크스페이스에 떨어뜨리기. | (없음) |
| **마크다운 에디터** | Full WYSIWYG — autocorrect · ⌘K 링크 · 코드블록 언어 picker · paste sanitizer · 인쇄 머리/꼬리말 사용자 정의. | read-only 렌더 |
| **Export** | PDF · Print · DOCX · Markdown · Markdown (Smart) · HTML · 확장이 추가하는 동적 포맷. | PDF · Print · HTML |
| **자동 업데이트** | 백그라운드 다운로드 + 재시작 prompt. 서명/검증. | 동일. |
| **라이선스** | Pro Solo $7/mo · 14일 무료 트라이얼 · 영구. | 구독 (내장 AI 비용 포함). |
| **프라이버시** | 직접 호출한 AI 외에는 디바이스를 떠나는 것 없음. | 구독 AI 콜은 우리 백엔드 경유. |

## Pro 를 골라야 할 때

다음 중 하나라도 해당:

- 이미 쓰는 AI 키가 있음 (Anthropic · OpenAI · Together · 로컬 Ollama …)
- 터미널 익숙. Claude / Codex / Gemini 가 *앱 안* 에 있길 원함
- 어떤 파일이 디바이스를 떠나는지 세밀하게 통제하고 싶음
- 디자이너 / 작가 / 엔지니어 / 리서처 / 변호사 / PM — annotate 많이 하고 Paint · 음성 메모 빌트인 원함

## Easier 가 맞는 경우

- API 키 · 월 LLM 비용 · 모델 선택을 고민하기 싫음
- 쓰기보다 읽기가 훨씬 많음
- "그냥 AI 있는 거" 가 좋고 매월 구독 OK
- 도구 메뉴 안 좋아하는 가족 / 동료에게 추천

## 솔직한 trade-off

Pro 는 더 강력하고 비용 면에서 솔직 — LLM 청구서가 본인 앞으로 가고, 모델 직접 고르고, 앱이 지갑에 손 안 댐. Easier 는 첫날부터 들어가기 편하고 AI 품질이 사용자 간 일관 — 좋은 답 얻으려고 8 개 provider 비교 안 해도 됨.

둘 다 같은 렌더러 · 파일 watcher · Markdown 엔진 위에서 동작. 워크스페이스 fidelity 동일. 갈아탈 때 다른 빌드 깔고 같은 폴더 가리키면 파일과 메모가 그대로 따라옴.

## 다음

- [설치 →](Installation-ko.md)
- [워크스페이스 →](Workspace-ko.md)
