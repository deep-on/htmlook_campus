"""
Fourier Transform · 시간 영역 신호를 winding 으로 spectrum 추출.

Run:
    manim -p -qm scene.py FourierIntuition
"""
from manim import *
import numpy as np


class FourierIntuition(Scene):
    def construct(self):
        title = Text("Fourier Transform · 직관", font_size=36)
        sub = Text("시간 ↔ 주파수", font_size=22, color=GRAY).next_to(title, DOWN)
        self.play(Write(title), FadeIn(sub))
        self.wait(0.8)
        self.play(FadeOut(VGroup(title, sub)))

        # Scene 1 — time domain signal
        ax_t = Axes(x_range=[0, 4*PI, PI], y_range=[-2, 2, 1], x_length=10, y_length=3)
        sig = ax_t.plot(lambda t: np.sin(3*t) + 0.5*np.sin(7*t), color=BLUE)
        eq_t = MathTex(r"f(t) = \sin(3t) + 0.5 \sin(7t)", color=BLUE).next_to(ax_t, UP)
        self.play(Create(ax_t), Write(eq_t))
        self.play(Create(sig))
        self.wait(1.5)

        # Scene 2 — winding around a circle at varying freq
        self.play(*[FadeOut(m) for m in [ax_t, sig, eq_t]])
        circle = Circle(radius=1.5, color=PURPLE).move_to(LEFT*3)
        self.play(Create(circle))
        winding_freq = ValueTracker(1)
        # Visualization placeholder — actual winding is a Mobject built from sig × e^{-2πift}
        freq_label = MathTex(r"\text{winding freq}=", "{:.1f}").set_color(GREEN).move_to(RIGHT*2)
        self.play(Write(freq_label))
        self.play(winding_freq.animate.set_value(3), run_time=2.5)
        self.wait(0.8)

        # Scene 3 — spectrum
        self.play(*[FadeOut(m) for m in [circle, freq_label]])
        ax_f = Axes(x_range=[0, 10, 1], y_range=[0, 1.2, 0.5], x_length=10, y_length=3)
        bars = VGroup(*[
            Rectangle(height=h, width=0.4, fill_color=GREEN, fill_opacity=0.85, stroke_width=0).move_to(ax_f.c2p(x, h/2))
            for x, h in [(3, 1.0), (7, 0.5)]
        ])
        eq_f = MathTex(r"F(\omega)", color=GREEN).next_to(ax_f, UP)
        self.play(Create(ax_f), Write(eq_f))
        self.play(*[GrowFromEdge(b, DOWN) for b in bars])
        self.wait(1.0)

        narration = Text(
            "두 주파수 (3, 7) 의 강도를 정확히 추출함",
            font_size=24,
            color=WHITE,
        ).next_to(ax_f, DOWN, buff=0.6)
        self.play(FadeIn(narration))
        self.wait(2)
