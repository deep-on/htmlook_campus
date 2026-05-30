"""ML fundamentals — gradient descent and linear regression in four scenes.

Render a single scene:
    manim -pql scene.py LossCurve
    manim -pql scene.py GradientDescent
    manim -pql scene.py LinearRegression
    manim -pql scene.py UpdateRule
"""

from manim import *
import numpy as np


def loss(w):
    return 0.4 * (w - 2) ** 2 + 0.5


def grad(w):
    return 0.8 * (w - 2)


class LossCurve(Scene):
    """The loss as a function of one weight, with its minimum marked."""

    def construct(self):
        ax = Axes(
            x_range=[-2, 6, 1], y_range=[0, 6, 1],
            x_length=8, y_length=5, tips=False,
        ).add_coordinates()
        curve = ax.plot(loss, color=BLUE)
        labels = ax.get_axis_labels(Tex("w"), Tex("L(w)"))
        self.play(Create(ax), Create(curve), Write(labels))

        minimum = Dot(ax.c2p(2, loss(2)), color=GREEN)
        tag = Text("global minimum", font_size=24, color=GREEN).next_to(minimum, DOWN)
        self.play(Create(minimum), FadeIn(tag))
        self.wait(2)


class GradientDescent(Scene):
    """Step downhill along the loss curve using the gradient."""

    def construct(self):
        ax = Axes(
            x_range=[-2, 6, 1], y_range=[0, 6, 1],
            x_length=8, y_length=5, tips=False,
        )
        curve = ax.plot(loss, color=BLUE)
        self.play(Create(ax), Create(curve))

        lr = 0.6
        w = 5.5
        dot = Dot(ax.c2p(w, loss(w)), color=RED)
        readout = always_redraw(
            lambda: MathTex(r"w = %.2f" % w).to_corner(UR)
        )
        self.play(Create(dot), Write(readout))

        for _ in range(8):
            g = grad(w)
            slope_line = ax.plot(
                lambda t: g * (t - w) + loss(w),
                x_range=[w - 1, w + 1], color=YELLOW,
            )
            self.play(Create(slope_line), run_time=0.3)
            w = w - lr * g
            new_dot = Dot(ax.c2p(w, loss(w)), color=RED)
            self.play(
                Transform(dot, new_dot),
                FadeOut(slope_line),
                run_time=0.4,
            )

        done = Text("converged near the minimum", font_size=24, color=GREEN).to_edge(DOWN)
        self.play(FadeIn(done))
        self.wait(2)


class LinearRegression(Scene):
    """Fit a line to scattered points by lowering the residuals."""

    def construct(self):
        rng = np.random.default_rng(7)
        xs = np.linspace(-2.5, 2.5, 9)
        ys = 1.3 * xs + 0.4 + rng.normal(0, 0.6, size=xs.size)

        ax = Axes(
            x_range=[-3, 3, 1], y_range=[-4, 4, 1],
            x_length=8, y_length=5, tips=False,
        )
        self.play(Create(ax))
        dots = VGroup(*[Dot(ax.c2p(x, y), color=BLUE, radius=0.06)
                        for x, y in zip(xs, ys)])
        self.play(LaggedStartMap(FadeIn, dots, lag_ratio=0.1))

        # closed-form least-squares fit
        slope = np.cov(xs, ys, bias=True)[0, 1] / np.var(xs)
        intercept = ys.mean() - slope * xs.mean()

        bad = ax.plot(lambda x: -0.5 * x + 1.5, color=RED)
        self.play(Create(bad))
        good = ax.plot(lambda x: slope * x + intercept, color=GREEN)
        self.play(Transform(bad, good), run_time=1.5)

        eq = MathTex(r"\hat{y} = %.2f x + %.2f" % (slope, intercept),
                     color=GREEN).to_edge(DOWN)
        self.play(Write(eq))
        self.wait(2)


class UpdateRule(Scene):
    """The gradient-descent update rule, annotated."""

    def construct(self):
        title = Text("The update rule", weight=BOLD).scale(0.7).to_edge(UP)
        self.play(Write(title))

        rule = MathTex(
            r"w", r"\leftarrow", r"w", r"-", r"\eta", r"\nabla L(w)"
        ).scale(1.5)
        self.play(Write(rule))
        self.wait(0.5)

        lr_brace = Brace(rule[4], DOWN)
        lr_text = lr_brace.get_text("learning rate")
        grad_brace = Brace(rule[5], UP)
        grad_text = grad_brace.get_text("gradient")
        self.play(GrowFromCenter(lr_brace), FadeIn(lr_text))
        self.play(GrowFromCenter(grad_brace), FadeIn(grad_text))
        self.wait(2)
