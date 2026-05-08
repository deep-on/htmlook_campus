"""
Manim Community 스타터 — 미분 직관.

실행:
    manim -p -qm scene.py DerivativeIntuition
"""

from manim import (
    Axes,
    BLUE,
    Create,
    DOWN,
    FadeIn,
    GREEN,
    LEFT,
    MathTex,
    RIGHT,
    Scene,
    Text,
    Transform,
    UP,
    WHITE,
    Write,
)


class DerivativeIntuition(Scene):
    def construct(self):
        title = Text("미분 직관: 접선의 기울기", font_size=40)
        self.play(FadeIn(title))
        self.wait(0.8)
        self.play(title.animate.to_edge(UP))

        ax = Axes(
            x_range=[-3, 3, 1],
            y_range=[-1, 9, 1],
            x_length=8,
            y_length=5,
            tips=False,
        )
        labels = ax.get_axis_labels(x_label="x", y_label="y")

        graph = ax.plot(lambda x: x**2, color=BLUE)
        graph_label = MathTex("y = x^2", color=BLUE).next_to(ax, RIGHT)

        self.play(Create(ax), FadeIn(labels))
        self.play(Create(graph), Write(graph_label))
        self.wait(0.5)

        formula = MathTex(r"\frac{d}{dx} x^2 = 2x", color=GREEN, font_size=44)
        formula.to_edge(DOWN)
        self.play(Write(formula))
        self.wait(1.2)

        narration = Text(
            "기울기는 접점에서의 순간 변화율",
            font_size=28,
            color=WHITE,
        )
        narration.next_to(formula, UP, buff=0.4)
        self.play(FadeIn(narration))
        self.wait(2)
