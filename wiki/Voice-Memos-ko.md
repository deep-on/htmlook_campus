# 음성 메모

> 상태바의 마이크 버튼. AAC 파일이 워크스페이스 옆에. 선택적 transcript.

## 녹음

상태바 우측: 마이크 글리프. 클릭 → 녹음 시작, 글리프가 빨갛게 변하고 옆에 음량 미터 막대. 다시 클릭 → 정지. 파일은 `<workspace>/.htmlook-voice/voice_<YYYYMMDD-HHMMSS>.m4a` 로 떨어집니다.

첫 사용 시 macOS 가 마이크 권한 요청. 다이얼로그가 "녹음은 디바이스에 머문다" 설명.

> M3 + MacBook Pro 의 lid 닫음 (클램쉘) 시 내부 마이크가 디지털 무음 — 알려진 macOS 버그. lid 열거나 외부 마이크 페어링. HTMLook 이 zero-amplitude 스트림 감지 시 1회 경고.

## 재생 플레이어

![welcome.md 뷰어 내 인라인 음성 플레이어](images/08-voice.png)

음성 메모는 **문서에 부속된 메타데이터** — 플레이어는 문서에 묶임, 오디오 파일에 묶이지 않음. 활성 문서에 메모 (그 문서 열린 상태에서 녹음된 것) 가 하나 이상 있으면, 뷰어 내 렌더된 콘텐츠 사이에 플레이어 strip 이 인라인으로 등장.

- ◀ ▶▶ 활성 문서에 attach 된 메모 순환; 배지 = `n / total`
- 메모 파일명 + 경과 / 총 시간 (예: `0:00 / 0:06`)
- 우측 볼륨 슬라이더

**사이드바에서 `.m4a` 직접 클릭은 플레이어를 띄우지 않음** — 뷰어가 인식 안 되는 파일로 보고 "Preview not available" 카드를 띄움. 들으려면 그 메모가 녹음된 원래 문서를 여세요.

## Transcript

transcript 는 메모 옆 형제 파일 — `<memo>.m4a.transcript.json`. 있으면 플레이어가 timecode 와 함께 인라인 표시. 문장 클릭 시 그 위치로 seek.

만들려면 AI 어시스턴트에게 부탁하세요 ("이 메모 transcribe 해줘") — 어시스턴트가 파일을 만들어 둡니다. 앱 자체엔 speech-to-text 엔진 없음; 신뢰하는 것 가져다 쓰면 됨.

## Drag-out

사이드바 메모를 Finder · Mail · Slack · Notion 으로 드래그. .m4a 경로가 실림 — Mail 에 drop 하면 첨부.

## 메모 전체 검색

⌘⇧F (워크스페이스 검색) 가 음성 transcript 도 포함. 매치는 메모 이름과 hit 의 timecode 로 표시.

## 프라이버시

음성 파일은 자체로 워크스페이스 폴더를 떠나지 않습니다. transcribe · chat 전송 같은 액션은 모두 명시적. 녹음 중에는 마이크 글리프가 빨갛게 — 상태가 항상 가시.

## 다음

- [확장 (Extensions) →](Skills-ko.md)
- [Settings →](Settings-ko.md)
