"""Fourier series & transform — a five-scene visual explainer.

Build a square wave from sinusoids, trace a path with rotating epicycles,
move between time and frequency domains, and work a harmonic-amplitude
example by hand.

Render a single scene:
    manim -pql scene.py Intro
    manim -pql scene.py SquareWaveBuildup
    manim -pql scene.py Epicycles
    manim -pql scene.py TimeAndFrequency
    manim -pql scene.py HarmonicAmplitudes
"""

from manim import *
import numpy as np

# Odd harmonics 1, 3, 5, ... reconstruct a square wave:
#     f(t) = (4/pi) * sum_{k odd} sin(k t) / k
ODD_HARMONICS = [1, 3, 5, 7, 9, 11]


def square_partial_sum(t, n_terms):
    """Sum of the first n odd-harmonic sine terms of a unit square wave."""
    total = 0.0
    for k in ODD_HARMONICS[:n_terms]:
        total += np.sin(k * t) / k
    return (4 / np.pi) * total


class Intro(Scene):
    def construct(self):
        title = Text("Fourier Series", weight=BOLD).scale(1.1)
        subtitle = Text("every signal is a sum of pure sine waves").scale(0.5)
        subtitle.next_to(title, DOWN)

        self.play(Write(title))
        self.play(FadeIn(subtitle, shift=UP * 0.3))
        self.wait(1.2)

        eq = MathTex(
            r"f(t) = \frac{a_0}{2} + \sum_{n=1}^{\infty}"
            r"\left[a_n \cos(n t) + b_n \sin(n t)\right]"
        ).scale(0.9)
        self.play(ReplacementTransform(VGroup(title, subtitle), eq))
        self.wait(2)


class SquareWaveBuildup(Scene):
    def construct(self):
        axes = Axes(
            x_range=[0, 2 * PI, PI / 2],
            y_range=[-1.4, 1.4, 0.5],
            x_length=11,
            y_length=4.5,
        )
        target = axes.plot(
            lambda t: square_partial_sum(t, len(ODD_HARMONICS)),
            color=GREY_B,
        )
        self.play(Create(axes))
        self.play(Create(target))

        label = MathTex(r"\text{1 term}").to_corner(UR)
        approx = axes.plot(lambda t: square_partial_sum(t, 1), color=YELLOW)
        self.play(Write(label), Create(approx))
        self.wait(0.6)

        for n in range(2, len(ODD_HARMONICS) + 1):
            new_approx = axes.plot(
                lambda t, n=n: square_partial_sum(t, n), color=YELLOW
            )
            new_label = MathTex(rf"\text{{{n} terms}}").to_corner(UR)
            self.play(
                Transform(approx, new_approx),
                Transform(label, new_label),
                run_time=0.7,
            )
            self.wait(0.3)

        caption = MathTex(
            r"f(t) = \frac{4}{\pi}\sum_{k\,\text{odd}}\frac{\sin(k t)}{k}"
        ).scale(0.8).to_edge(DOWN)
        self.play(FadeIn(caption, shift=UP * 0.3))
        self.wait(2)


class Epicycles(Scene):
    def construct(self):
        # Three rotating arrows (odd harmonics) chained tip-to-tail; the
        # final tip traces a square-wave-like path over time.
        title = Text("Rotating epicycles", weight=BOLD).scale(0.6).to_edge(UP)
        self.play(FadeIn(title))

        center = LEFT * 3
        freqs = [1, 3, 5]
        radii = [(4 / np.pi) / k for k in freqs]
        t = ValueTracker(0)

        def tip_positions():
            pts = [center]
            theta = t.get_value()
            for k, r in zip(freqs, radii):
                prev = pts[-1]
                pts.append(prev + r * np.array([np.cos(k * theta), np.sin(k * theta), 0]))
            return pts

        arrows = VGroup()
        for i in range(len(freqs)):
            arrows.add(always_redraw(
                lambda i=i: Arrow(
                    tip_positions()[i],
                    tip_positions()[i + 1],
                    buff=0,
                    color=[BLUE, GREEN, YELLOW][i],
                    stroke_width=4,
                    max_tip_length_to_length_ratio=0.25,
                )
            ))
        circles = VGroup(*[
            always_redraw(
                lambda i=i: Circle(radius=radii[i], color=GREY_D, stroke_width=1)
                .move_to(tip_positions()[i])
            )
            for i in range(len(freqs))
        ])

        trace = TracedPath(
            lambda: tip_positions()[-1], stroke_color=RED, stroke_width=3
        )
        dot = always_redraw(lambda: Dot(tip_positions()[-1], color=RED, radius=0.05))

        self.add(circles, arrows, trace, dot)
        self.play(t.animate.set_value(2 * PI), run_time=6, rate_func=linear)
        self.wait(1)


class TimeAndFrequency(Scene):
    def construct(self):
        # Top: time-domain signal. Bottom: its discrete frequency spectrum.
        ax_t = Axes(
            x_range=[0, 4 * PI, PI],
            y_range=[-2, 2, 1],
            x_length=11,
            y_length=2.6,
        ).to_edge(UP, buff=0.6)
        sig = ax_t.plot(
            lambda t: np.sin(3 * t) + 0.5 * np.sin(7 * t), color=BLUE
        )
        eq_t = MathTex(
            r"f(t) = \sin(3t) + 0.5\,\sin(7t)", color=BLUE
        ).scale(0.7).next_to(ax_t, DOWN, buff=0.1)

        self.play(Create(ax_t), Create(sig), Write(eq_t))
        self.wait(0.8)

        ax_f = Axes(
            x_range=[0, 10, 1],
            y_range=[0, 1.2, 0.5],
            x_length=11,
            y_length=2.6,
        ).to_edge(DOWN, buff=0.6)
        ax_f_label = MathTex(r"|F(\omega)|", color=GREEN).scale(0.7).next_to(
            ax_f, UP, buff=0.1
        )

        bars = VGroup(*[
            Rectangle(
                height=h * 2.0,
                width=0.35,
                fill_color=GREEN,
                fill_opacity=0.85,
                stroke_width=0,
            ).move_to(ax_f.c2p(x, 0), DOWN)
            for x, h in [(3, 1.0), (7, 0.5)]
        ])

        self.play(Create(ax_f), Write(ax_f_label))
        self.play(LaggedStart(*[GrowFromEdge(b, DOWN) for b in bars], lag_ratio=0.4))

        arrow = Arrow(ax_t.get_bottom(), ax_f.get_top(), color=YELLOW, buff=0.2)
        arrow_label = Text("FFT", font_size=24, color=YELLOW).next_to(arrow, RIGHT)
        self.play(GrowArrow(arrow), FadeIn(arrow_label))
        self.wait(2)


class HarmonicAmplitudes(Scene):
    def construct(self):
        title = Text("Worked example: b_n of a square wave", weight=BOLD)
        title.scale(0.55).to_edge(UP)
        self.play(FadeIn(title))

        integral = MathTex(
            r"b_n = \frac{1}{\pi}\int_{-\pi}^{\pi} f(t)\,\sin(n t)\,dt"
        )
        self.play(Write(integral))
        self.play(integral.animate.next_to(title, DOWN, buff=0.5))

        steps = VGroup(
            MathTex(r"f(t) = +1 \text{ on } (0,\pi),\; -1 \text{ on } (-\pi,0)"),
            MathTex(r"b_n = \frac{2}{\pi}\int_{0}^{\pi}\sin(n t)\,dt"),
            MathTex(r"b_n = \frac{2}{\pi}\cdot\frac{1 - \cos(n\pi)}{n}"),
            MathTex(r"b_n = \frac{4}{n\pi}\ \text{(n odd)},\quad 0\ \text{(n even)}"),
        ).arrange(DOWN, buff=0.45).next_to(integral, DOWN, buff=0.5)

        for step in steps:
            self.play(FadeIn(step, shift=RIGHT * 0.3))
            self.wait(0.7)

        box = SurroundingRectangle(steps[-1], color=GREEN)
        self.play(Create(box))
        self.wait(2)
