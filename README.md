# HTMLook Campus

> HTMLook Pro 의 26 페르소나 워크플로우를 영상 + 따라하기 워크스페이스 + 튜토리얼로
> 학습할 수 있는 캠퍼스.

## 무엇이 들어 있나

| 폴더 | 내용 |
|---|---|
| [`videos/`](videos/) | 26 페르소나 walkthrough 영상 (각 ~60초, mp4 + en/ko subtitle muxed) |
| [`videos/features/`](videos/features/) | 17 feature spotlight 영상 (각 30초, 단일 magic moment) — BASIC 6 + ADVANCED 11 |
| [`samples/`](samples/) | 영상의 모든 워크플로우를 직접 따라할 수 있는 sample workspace |
| [`docs/INDEX.md`](docs/INDEX.md) | 페르소나 카탈로그 (영상 ↔ 샘플 ↔ 워크스루 cross-link) |
| [`docs/FEATURES.md`](docs/FEATURES.md) | 17 feature spotlight 카탈로그 |

## 빠르게 시작

1. **HTMLook Pro 설치** — [htmlook.app](https://htmlook.app) (혹은 자체 빌드)
2. 이 레포 clone:
   ```bash
   git clone git@github.com:deep-on/htmlook_campus.git
   cd htmlook_campus
   ```
3. `samples/` 폴더를 HTMLook Pro 에서 *Open Folder* 로 열기
4. 좌측 사이드바에 26 페르소나 폴더 보임 — 각 폴더의 `WALKTHROUGH.md` 따라하기

## 페르소나 (26편)

영상 카탈로그 + sample 링크는 [`docs/INDEX.md`](docs/INDEX.md) 참고.

분류:

- **개발** (3): hf-claude, hf-llama, dev-pr-docs
- **콘텐츠** (4): creator-podcast, press-editor, hobby-fiction, picture-book
- **분석** (4): data-analyst, finance-report, research-notes, economy-analyst
- **법무/번역** (3): legal-redline, translator-book, domain-battery
- **교육 (선생님)** (3): teacher-quiz, teacher-newsletter, teacher-record
- **교육 (학생)** (5): student-notes, student-flashcard, kid-coding, homework-helper, kids-science-mag
- **비즈니스** (2): corp-deck, product-prd
- **일상** (2): recipe-card, mobile-news

## AI 협업 (선택)

`samples/CLAUDE.md` 가 AI agent 용 가이드. MCP 호환 LLM 클라이언트 (Claude Code,
Cursor, Windsurf, Ollama 등) 에 `samples/.htmlook/mcp-config.example.json` 의
설정을 병합하면 영상의 *cite + apply_edit* 워크플로우를 직접 실행할 수 있음.

LLM 없는 사용자도 각 페르소나의 `before/` `after/` 디렉토리로 결과를 시각 비교 가능.

## 라이선스

- 코드 / 워크스루 텍스트: MIT
- 영상 mp4: CC BY 4.0 (사용 시 *"HTMLook Campus"* 출처 표기)
- 샘플 콘텐츠 (PDF / xlsx / md / html): CC0 / public domain — 모두 fictional placeholder

## 상태

이 레포는 *private preview*. HTMLook Pro 정식 출시 시점에 public 전환 예정.

## 관련 프로젝트

- HTMLook Pro 본 레포: 비공개 (정식 출시 시 공개)
- 페르소나 영상 raw composition: HTMLook 본 레포의 `demo/persona_units/`
