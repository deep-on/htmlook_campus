# AWS 3-tier Architecture Walkthrough · 30-min Walkthrough

> 🌟 **Wave A · High Quality** — 마케팅 / 데모 자산. 직접 demo recording 가능.

## 1. 다이어그램 렌더
```bash
brew install d2
d2 --watch architecture.d2 architecture.svg
```

## 2. Pane pair
- 좌: architecture.d2 편집
- 우: HTMLook viewer 가 architecture.svg auto-reload

## 3. Region cite 시그니처
1. Web tier 영역 캡처
2. AI: "이 영역의 비용 추정 + 대안 제시"
3. AI 가 cost-estimate 섹션 + alternative pattern 제안

## 4. Multi-target
- internal app 으로 적응 시: ALB → NLB / 도메인 변경 일괄
