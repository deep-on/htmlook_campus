"""manim -p -qm scene.py DerivativeIntuition"""
from manim import *
import numpy as np

class DerivativeIntuition(Scene):
    def construct(self):
        title = Text("미분 · 접선의 기울기 = 순간 변화율", font_size=32)
        self.play(FadeIn(title)); self.wait(1); self.play(title.animate.to_edge(UP))

        ax = Axes(x_range=[-3, 3, 1], y_range=[-1, 9, 1], x_length=8, y_length=5, tips=False)
        graph = ax.plot(lambda x: x**2, color=BLUE)
        graph_label = MathTex(r"y = x^2", color=BLUE).next_to(ax, RIGHT)
        self.play(Create(ax), FadeIn(graph), Write(graph_label))
        self.wait(0.5)

        x = ValueTracker(1.5)
        dot = always_redraw(lambda: Dot(ax.c2p(x.get_value(), x.get_value()**2), color=RED))
        tangent = always_redraw(lambda: ax.plot(
            lambda t: 2*x.get_value()*(t - x.get_value()) + x.get_value()**2,
            x_range=[x.get_value()-1.5, x.get_value()+1.5], color=GREEN,
        ))
        self.play(Create(dot), Create(tangent))
        self.play(x.animate.set_value(2.5), run_time=2)
        self.play(x.animate.set_value(-1.5), run_time=2.5)
        self.wait(0.5)

        formula = MathTex(r"\frac{d}{dx} x^2 = 2x", color=GREEN, font_size=44).to_edge(DOWN)
        self.play(Write(formula)); self.wait(2)
