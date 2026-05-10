# Persona Catalog

26편 페르소나의 영상 + sample workspace + walkthrough cross-reference.
HTMLook Pro v1.0 release-candidate 기준. AI 단계는 내장 BYOM 채팅 / 내장
Terminal CLI / 외부 MCP 클라이언트 어느 것이나 사용 가능.

각 페르소나는 [Step 5 · command](../README.md) 의 cite + apply_edit 흐름을
자기 도메인에 적용한 1-day-in-the-life. 60-70 초 walkthrough 영상 +
sample workspace + step-by-step `WALKTHROUGH.md` 한 세트.

| # | 페르소나 | 영상 | 샘플 폴더 | Walkthrough | 한 줄 요약 |
|---|---|---|---|---|---|
| 1 | `hf-claude` | [01-hf-claude.mp4](../../videos/01-hf-claude.mp4) | [`01-hf-claude/`](01-hf-claude/) | [WALKTHROUGH](01-hf-claude/WALKTHROUGH.md) | Code on the left, result on the right — Claude through MCP cites + apply_edit |
| 2 | `hf-llama` | [02-hf-llama.mp4](../../videos/02-hf-llama.mp4) | [`02-hf-llama/`](02-hf-llama/) | [WALKTHROUGH](02-hf-llama/WALKTHROUGH.md) | Same workflow, local Llama swap — LLM-agnostic via MCP |
| 3 | `dev-pr-docs` | [03-dev-pr-docs.mp4](../../videos/03-dev-pr-docs.mp4) | [`03-dev-pr-docs/`](03-dev-pr-docs/) | [WALKTHROUGH](03-dev-pr-docs/WALKTHROUGH.md) | PR diff + docs file dual-pane — find drift, patch docs |
| 4 | `creator-podcast` | [04-creator-podcast.mp4](../../videos/04-creator-podcast.mp4) | [`04-creator-podcast/`](04-creator-podcast/) | [WALKTHROUGH](04-creator-podcast/WALKTHROUGH.md) | Transcript + kinetic-caption clip — find quotable moment, retime |
| 5 | `domain-battery` | [05-domain-battery.mp4](../../videos/05-domain-battery.mp4) | [`05-domain-battery/`](05-domain-battery/) | [WALKTHROUGH](05-domain-battery/WALKTHROUGH.md) | Vendor PDF + brief draft — cite cycle-life row, redo chart |
| 6 | `economy-analyst` | [06-economy-analyst.mp4](../../videos/06-economy-analyst.mp4) | [`06-economy-analyst/`](06-economy-analyst/) | [WALKTHROUGH](06-economy-analyst/WALKTHROUGH.md) | Mobile-first portrait report — bullets, citations, voice |
| 7 | `translator-book` | [07-translator-book.mp4](../../videos/07-translator-book.mp4) | [`07-translator-book/`](07-translator-book/) | [WALKTHROUGH](07-translator-book/WALKTHROUGH.md) | Source PDF + Korean draft — cite paragraph, iterate per pass |
| 8 | `legal-redline` | [08-legal-redline.mp4](../../videos/08-legal-redline.mp4) | [`08-legal-redline/`](08-legal-redline/) | [WALKTHROUGH](08-legal-redline/WALKTHROUGH.md) | Contract PDF + redline memo — clause grading, counter language |
| 9 | `data-analyst` | [09-data-analyst.mp4](../../videos/09-data-analyst.mp4) | [`09-data-analyst/`](09-data-analyst/) | [WALKTHROUGH](09-data-analyst/WALKTHROUGH.md) | SQL + chart svg — cite column, LLM rewrites the chart |
| 10 | `research-notes` | [10-research-notes.mp4](../../videos/10-research-notes.mp4) | [`10-research-notes/`](10-research-notes/) | [WALKTHROUGH](10-research-notes/WALKTHROUGH.md) | Paper PDF + notes — cite methods, anchor pages, bibliography |
| 11 | `finance-report` | [11-finance-report.mp4](../../videos/11-finance-report.mp4) | [`11-finance-report/`](11-finance-report/) | [WALKTHROUGH](11-finance-report/WALKTHROUGH.md) | Q3 xlsx + CFO brief — cite EBITDA!B14, narrative paragraph |
| 12 | `press-editor` | [12-press-editor.mp4](../../videos/12-press-editor.mp4) | [`12-press-editor/`](12-press-editor/) | [WALKTHROUGH](12-press-editor/WALKTHROUGH.md) | Transcript + article — cite quote at timestamp, polish |
| 13 | `product-prd` | [13-product-prd.mp4](../../videos/13-product-prd.mp4) | [`13-product-prd/`](13-product-prd/) | [WALKTHROUGH](13-product-prd/WALKTHROUGH.md) | PRD + wireframe + tickets — one cite syncs three files |
| 14 | `kids-science-mag` | [14-kids-science-mag.mp4](../../videos/14-kids-science-mag.mp4) | [`14-kids-science-mag/`](14-kids-science-mag/) | [WALKTHROUGH](14-kids-science-mag/WALKTHROUGH.md) | Adult science cite → kid-friendly paraphrase |
| 15 | `picture-book` | [15-picture-book.mp4](../../videos/15-picture-book.mp4) | [`15-picture-book/`](15-picture-book/) | [WALKTHROUGH](15-picture-book/WALKTHROUGH.md) | Verse manuscript + illustrated spread — line 2 rhythm tighten |
| 16 | `corp-deck` | [16-corp-deck.mp4](../../videos/16-corp-deck.mp4) | [`16-corp-deck/`](16-corp-deck/) | [WALKTHROUGH](16-corp-deck/WALKTHROUGH.md) | Outline → slides composition |
| 17 | `teacher-quiz` | [17-teacher-quiz.mp4](../../videos/17-teacher-quiz.mp4) | [`17-teacher-quiz/`](17-teacher-quiz/) | [WALKTHROUGH](17-teacher-quiz/WALKTHROUGH.md) | Source notes → quiz sheet (Korean) |
| 18 | `teacher-newsletter` | [18-teacher-newsletter.mp4](../../videos/18-teacher-newsletter.mp4) | [`18-teacher-newsletter/`](18-teacher-newsletter/) | [WALKTHROUGH](18-teacher-newsletter/WALKTHROUGH.md) | Class notes → printable parent newsletter (Korean) |
| 19 | `teacher-record` | [19-teacher-record.mp4](../../videos/19-teacher-record.mp4) | [`19-teacher-record/`](19-teacher-record/) | [WALKTHROUGH](19-teacher-record/WALKTHROUGH.md) | Observations → student record book (Korean) |
| 20 | `student-notes` | [20-student-notes.mp4](../../videos/20-student-notes.mp4) | [`20-student-notes/`](20-student-notes/) | [WALKTHROUGH](20-student-notes/WALKTHROUGH.md) | Lecture notes → flashcards in sync |
| 21 | `kid-coding` | [21-kid-coding.mp4](../../videos/21-kid-coding.mp4) | [`21-kid-coding/`](21-kid-coding/) | [WALKTHROUGH](21-kid-coding/WALKTHROUGH.md) | star.py + svg drawing — for-loop tutor, angle change reload |
| 22 | `hobby-fiction` | [22-hobby-fiction.mp4](../../videos/22-hobby-fiction.mp4) | [`22-hobby-fiction/`](22-hobby-fiction/) | [WALKTHROUGH](22-hobby-fiction/WALKTHROUGH.md) | Research notes → chapter draft (Korean SF) |
| 23 | `homework-helper` | [23-homework-helper.mp4](../../videos/23-homework-helper.mp4) | [`23-homework-helper/`](23-homework-helper/) | [WALKTHROUGH](23-homework-helper/WALKTHROUGH.md) | Math problem → step-by-step + concept reminder + practice set |
| 24 | `student-flashcard` | [24-student-flashcard.mp4](../../videos/24-student-flashcard.mp4) | [`24-student-flashcard/`](24-student-flashcard/) | [WALKTHROUGH](24-student-flashcard/WALKTHROUGH.md) | Notes → flashcard deck (Korean) |
| 25 | `recipe-card` | [25-recipe-card.mp4](../../videos/25-recipe-card.mp4) | [`25-recipe-card/`](25-recipe-card/) | [WALKTHROUGH](25-recipe-card/WALKTHROUGH.md) | Recipe text → card-format render (Korean tteokbokki) |
| 26 | `mobile-news` | [26-mobile-news.mp4](../../videos/26-mobile-news.mp4) | [`26-mobile-news/`](26-mobile-news/) | [WALKTHROUGH](26-mobile-news/WALKTHROUGH.md) | Article → mobile-first portrait card |

## 시청 + 따라하기 권장 순서

1. **개발자 첫 인상**: hf-claude → hf-llama → dev-pr-docs
2. **콘텐츠 제작**: creator-podcast → press-editor → picture-book → hobby-fiction
3. **분석/리포트**: data-analyst → finance-report → research-notes → economy-analyst
4. **PDF/xlsx 워크플로우**: domain-battery → translator-book → legal-redline
5. **교육 (선생님)**: teacher-quiz → teacher-newsletter → teacher-record
6. **교육 (학생)**: student-notes → student-flashcard → homework-helper → kid-coding → kids-science-mag
7. **비즈니스**: corp-deck → product-prd
8. **일상**: recipe-card → mobile-news

## 영상 주요 정보

- 길이: 각 60-70초
- 자막: 영문 (default) + 한글 — `.en+ko.mp4` 는 한글 default+forced, mov_text muxed
- 해상도: 1920×1080
- TTS: Kokoro-82M (af_nova) via `npx hyperframes tts`
- 자막 정렬: Whisper word-level via `npx hyperframes transcribe`
