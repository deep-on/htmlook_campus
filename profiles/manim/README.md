# Manim Profile

수학 / 과학 애니메이션 [Manim Community](https://www.manim.community) HTMLook Profile.

## 시작

```bash
pip install manim
manim -p -qm scene.py DerivativeIntuition
# media/videos/scene/720p30/DerivativeIntuition.mp4 생성 + 자동 재생
```

## HTMLook 활용

- **Pane pair**: 좌 `.py` Scene ↔ 우 렌더된 mp4 (Sidebar viewer).
- **Region cite**: frame 의 한 영역 캡처 → AI 에게 색/타이밍 수정 지시.
- **Live-cue ⭐**: timestamp ↔ Scene 코드 라인 양방향.

## 외부 의존

- Python 3.10+
- ffmpeg (mp4 인코딩)
- TeX Live / MiKTeX (LaTeX 수식 렌더링)
- 한글 폰트 (Pretendard 등)

## 라이선스

본 Profile = MIT (deep-on). Manim Community = BSD-3-Clause.
