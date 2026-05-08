---
name: manim
description: ManimCommunity 수학/과학 애니메이션 — Scene 클래스 .py → mp4.
---

# Manim 워크플로우

3Blue1Brown 의 수학 영상 도구 — ManimCommunity 포크가 더 활발히 유지됨 (`pip install manim`).

## 발견 신호

- `manim` 또는 `from manim import *` import
- `class XxxScene(Scene):` 패턴
- `media/` 출력 폴더 (자동 생성)
- `manim.cfg` (설정 파일 — 선택)

## 작업 패턴

```bash
manim -p -qm scene.py SquareToCircle
#       │  │  │       │
#       │  │  │       └── Scene 클래스 이름
#       │  │  └────────── scene.py 파일
#       │  └────────────  quality: -ql / -qm / -qh / -qk
#       └─────────────── -p preview (렌더 후 재생)
```

## 핵심 개념

```python
from manim import *

class SquareToCircle(Scene):
    def construct(self):
        square = Square()
        circle = Circle()
        self.play(Create(square))
        self.wait()
        self.play(Transform(square, circle))
        self.wait()
```

- **Scene** = 한 클립.
- **Mobject** (mathematical object) = 화면 위 모든 객체 (Square, Circle, Tex, Graph, ...).
- **animation** = `Create / Transform / FadeIn / Write` 등.
- **self.play()** + **self.wait()** = 시퀀스 단위.

## HTMLook 시그니처 활용

- **Pane pair**: 좌 `.py` Scene 코드 ↔ 우 viewer 가 렌더된 mp4 (`media/videos/<scene>/720p30/SquareToCircle.mp4`).
- **Region cite**: 영상의 한 frame / region 캡처 → AI 에게 "이 부분 색 더 차분하게" / "이 텍스트 더 천천히".
- **Live-cue**: 영상 timestamp ↔ Scene 코드의 `self.play(...)` 라인 양방향.

## 자주 쓰는 패턴

```python
# 그래프
ax = Axes(x_range=[-3, 3], y_range=[-1, 9])
graph = ax.plot(lambda x: x**2, color=BLUE)
self.play(Create(ax), Create(graph))

# LaTeX
formula = MathTex(r"\frac{d}{dx} x^2 = 2x")
self.play(Write(formula))

# 텍스트
title = Text("미분 직관", font="Pretendard")
self.play(FadeIn(title))
```

## 주의

- LaTeX 렌더링 = TeX 설치 필요 (TeX Live / MiKTeX). Pretendard 등 한글 폰트 = 시스템 폰트 fallback.
- `ManimCommunity` 와 3Blue1Brown 원본 (`manimgl`) 은 syntax 일부 다름 — 본 Profile 은 Community 버전 기준.
- ffmpeg 필요 (mp4 인코딩).
- 4k (-qk) 렌더는 시간 길음 — 작업 중엔 -qm 권장.

## 참조

- 공식: https://www.manim.community
- GitHub (Community): https://github.com/ManimCommunity/manim (BSD-3-Clause)
- GitHub (3b1b 원본): https://github.com/3b1b/manim (MIT)
- 라이선스: 본 Profile = MIT, Manim Community = BSD-3-Clause
