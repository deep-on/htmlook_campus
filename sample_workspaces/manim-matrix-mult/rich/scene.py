"""Matrix multiplication — a visual explainer in four scenes.

Render a single scene:
    manim -pql scene.py DotProductRow
    manim -pql scene.py BuildProduct
    manim -pql scene.py DimensionRule
    manim -pql scene.py ComposeTransforms
"""

from manim import *
import numpy as np

# The running example: C = A @ B for 2x2 matrices.
A = [[2, 1], [0, 3]]
B = [[1, 4], [2, 1]]
C = (np.array(A) @ np.array(B)).tolist()  # [[4, 9], [6, 3]]


class DotProductRow(Scene):
    """One output entry is a row dotted with a column."""

    def construct(self):
        title = Text("Each entry = row · column", weight=BOLD).scale(0.7).to_edge(UP)
        self.play(Write(title))

        mat_a = Matrix(A).shift(LEFT * 3)
        mat_b = Matrix(B).shift(RIGHT * 0.2)
        times = MathTex(r"\times").move_to((mat_a.get_right() + mat_b.get_left()) / 2)
        self.play(Write(mat_a), Write(mat_b), Write(times))
        self.wait(0.5)

        row = SurroundingRectangle(mat_a.get_rows()[0], color=YELLOW)
        col = SurroundingRectangle(mat_b.get_columns()[0], color=GREEN)
        self.play(Create(row), Create(col))

        calc = MathTex(r"2\cdot 1 + 1\cdot 2 = 4").scale(0.9).to_edge(DOWN)
        self.play(Write(calc))
        self.wait(1.5)

        result = MathTex(r"C_{11} = 4", color=BLUE).next_to(calc, UP)
        self.play(FadeIn(result, shift=UP * 0.3))
        self.wait(2)


class BuildProduct(Scene):
    """Fill the product matrix entry by entry."""

    def construct(self):
        mat_a = Matrix(A).scale(0.9).shift(LEFT * 4)
        mat_b = Matrix(B).scale(0.9).shift(LEFT * 1)
        eq = MathTex("=").next_to(mat_b, RIGHT)
        self.play(Write(mat_a), Write(mat_b), Write(eq))

        entries = VGroup()
        for i in range(2):
            for j in range(2):
                entries.add(MathTex(str(C[i][j])))
        result = Matrix([["a", "b"], ["c", "d"]]).scale(0.9).next_to(eq, RIGHT)
        self.play(Create(result.get_brackets()))

        slots = result.get_entries()
        for k, (i, j) in enumerate([(0, 0), (0, 1), (1, 0), (1, 1)]):
            target = entries[k].move_to(slots[k].get_center())
            row = SurroundingRectangle(mat_a.get_rows()[i], color=YELLOW)
            col = SurroundingRectangle(mat_b.get_columns()[j], color=GREEN)
            self.play(Create(row), Create(col), run_time=0.4)
            self.play(Write(target), run_time=0.4)
            self.play(FadeOut(row), FadeOut(col), run_time=0.3)

        self.wait(2)


class DimensionRule(Scene):
    """Why inner dimensions must match."""

    def construct(self):
        title = Text("Inner dimensions must match", weight=BOLD).scale(0.6).to_edge(UP)
        self.play(Write(title))

        shape = MathTex(
            r"(m \times", r"n", r")", r"\cdot", r"(", r"n", r"\times p)", r"= (m \times p)"
        ).scale(1.1)
        self.play(Write(shape))
        self.wait(0.5)

        inner = VGroup(shape[1], shape[5])
        self.play(inner.animate.set_color(GREEN))
        link = DoubleArrow(
            shape[1].get_bottom(), shape[5].get_bottom(), color=GREEN, buff=0.2
        ).shift(DOWN * 0.3)
        match = Text("these must be equal", font_size=24, color=GREEN).next_to(link, DOWN)
        self.play(Create(link), FadeIn(match))
        self.wait(2)


class ComposeTransforms(LinearTransformationScene):
    """Matrix product = composition of two linear maps."""

    def __init__(self, **kwargs):
        super().__init__(show_coordinates=True, **kwargs)

    def construct(self):
        v = self.add_vector([1, 1], color=YELLOW)
        self.add_transformable_label(v, "v", color=YELLOW)
        self.wait()

        caption = Text("apply B, then A", font_size=28).to_edge(UP)
        self.add_fixed_in_frame_mobjects(caption)
        self.play(Write(caption))

        self.apply_matrix(B)
        self.wait()
        self.apply_matrix(A)
        self.wait(2)
