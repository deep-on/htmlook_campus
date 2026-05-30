"""Derivatives & limits — the secant-to-tangent story in four scenes.

Render a single scene:
    manim -pql scene.py SecantToTangent
    manim -pql scene.py LimitDefinition
    manim -pql scene.py SlopeReadout
    manim -pql scene.py FiveFunctions
"""

from manim import *
import numpy as np


def f(x):
    return 0.5 * x**2


class SecantToTangent(Scene):
    """A secant line through (a, f(a)) and (a+h, f(a+h)) as h -> 0."""

    def construct(self):
        ax = Axes(
            x_range=[-1, 4, 1], y_range=[-1, 8, 1],
            x_length=8, y_length=5, tips=False,
        )
        graph = ax.plot(f, color=BLUE)
        label = MathTex(r"f(x) = \tfrac{1}{2}x^2", color=BLUE).to_corner(UR)
        self.play(Create(ax), Create(graph), Write(label))

        a = 2.0
        h = ValueTracker(1.8)
        pa = Dot(ax.c2p(a, f(a)), color=YELLOW)
        pb = always_redraw(
            lambda: Dot(ax.c2p(a + h.get_value(), f(a + h.get_value())), color=RED)
        )

        def secant():
            hv = h.get_value()
            slope = (f(a + hv) - f(a)) / hv
            return ax.plot(
                lambda t: slope * (t - a) + f(a),
                x_range=[a - 1.5, a + 2], color=GREEN,
            )

        line = always_redraw(secant)
        self.play(Create(pa), Create(pb), Create(line))
        self.wait(0.5)

        self.play(h.animate.set_value(0.05), run_time=4, rate_func=smooth)
        self.wait(0.5)

        note = Text("secant -> tangent as h -> 0", font_size=26, color=GREEN).to_edge(DOWN)
        self.play(FadeIn(note))
        self.wait(2)


class LimitDefinition(Scene):
    """The formal definition, derived term by term."""

    def construct(self):
        title = Text("Definition of the derivative", weight=BOLD).scale(0.7).to_edge(UP)
        self.play(Write(title))

        steps = VGroup(
            MathTex(r"f'(a) = \lim_{h \to 0} \frac{f(a+h) - f(a)}{h}"),
            MathTex(r"= \lim_{h \to 0} \frac{\tfrac12(a+h)^2 - \tfrac12 a^2}{h}"),
            MathTex(r"= \lim_{h \to 0} \frac{a h + \tfrac12 h^2}{h}"),
            MathTex(r"= \lim_{h \to 0} \left(a + \tfrac12 h\right) = a"),
        ).arrange(DOWN, buff=0.45)

        for s in steps:
            self.play(FadeIn(s, shift=RIGHT * 0.3))
            self.wait(0.7)

        box = SurroundingRectangle(steps[-1], color=GREEN)
        self.play(Create(box))
        self.wait(2)


class SlopeReadout(Scene):
    """Live slope value of the tangent as the point slides along the curve."""

    def construct(self):
        ax = Axes(
            x_range=[-3, 3, 1], y_range=[-1, 9, 1],
            x_length=8, y_length=5, tips=False,
        )
        graph = ax.plot(lambda x: x**2, color=BLUE)
        self.play(Create(ax), Create(graph))

        x = ValueTracker(-2.0)
        dot = always_redraw(lambda: Dot(ax.c2p(x.get_value(), x.get_value()**2), color=RED))
        tangent = always_redraw(
            lambda: ax.plot(
                lambda t: 2 * x.get_value() * (t - x.get_value()) + x.get_value()**2,
                x_range=[x.get_value() - 1.4, x.get_value() + 1.4], color=GREEN,
            )
        )
        readout = always_redraw(
            lambda: MathTex(
                r"\text{slope} = 2x = %.2f" % (2 * x.get_value())
            ).to_edge(DOWN)
        )
        self.play(Create(dot), Create(tangent), Write(readout))
        self.play(x.animate.set_value(2.0), run_time=4, rate_func=there_and_back)
        self.wait(1)


class FiveFunctions(Scene):
    """Known derivatives of five staple functions."""

    def construct(self):
        title = Text("Five derivatives to know", weight=BOLD).scale(0.6).to_edge(UP)
        self.play(Write(title))

        rules = VGroup(
            MathTex(r"\frac{d}{dx} x^2 = 2x"),
            MathTex(r"\frac{d}{dx} \sin x = \cos x"),
            MathTex(r"\frac{d}{dx} e^x = e^x"),
            MathTex(r"\frac{d}{dx} \tfrac{1}{x} = -\tfrac{1}{x^2}"),
            MathTex(r"\frac{d}{dx} \ln x = \tfrac{1}{x}"),
        ).arrange(DOWN, buff=0.4).scale(0.9)

        for r in rules:
            self.play(Write(r), run_time=0.6)
        self.wait(2)
