"""Eigenvectors & eigenvalues — a three-scene visual explainer.

Render a single scene:
    manim -pql scene.py Intro
    manim -pql scene.py EigenTransform
    manim -pql scene.py ComputeExample
"""

from manim import *

# The matrix we explore throughout: [[2, 1], [1, 2]].
# Eigenvalues 3 (along [1, 1]) and 1 (along [1, -1]).
A = [[2, 1], [1, 2]]


class Intro(Scene):
    def construct(self):
        title = Text("Eigenvectors", weight=BOLD).scale(1.1)
        subtitle = Text("vectors a matrix stretches but never rotates").scale(0.5)
        subtitle.next_to(title, DOWN)

        self.play(Write(title))
        self.play(FadeIn(subtitle, shift=UP * 0.3))
        self.wait(1.5)

        eq = MathTex(r"A\,\vec{v} = \lambda\,\vec{v}").scale(1.4)
        self.play(ReplacementTransform(VGroup(title, subtitle), eq))
        self.wait(2)


class EigenTransform(LinearTransformationScene):
    def __init__(self, **kwargs):
        super().__init__(
            show_coordinates=True,
            leave_ghost_vectors=True,
            **kwargs,
        )

    def construct(self):
        # An eigenvector (green, along [1, 1]) keeps its direction;
        # a generic vector (yellow) gets rotated.
        eigen = self.add_vector([1, 1], color=GREEN)
        generic = self.add_vector([1, -0.2], color=YELLOW)

        self.add_transformable_label(eigen, "v", color=GREEN)
        self.add_transformable_label(generic, "u", color=YELLOW)

        self.wait()
        self.apply_matrix(A)
        self.wait(2)


class ComputeExample(Scene):
    def construct(self):
        matrix = MathTex(r"A = \begin{bmatrix} 2 & 1 \\ 1 & 2 \end{bmatrix}")
        self.play(Write(matrix))
        self.play(matrix.animate.to_edge(UP))

        steps = VGroup(
            MathTex(r"\det(A - \lambda I) = 0"),
            MathTex(r"(2-\lambda)^2 - 1 = 0"),
            MathTex(r"\lambda^2 - 4\lambda + 3 = 0"),
            MathTex(r"\lambda = 3 \quad \text{or} \quad \lambda = 1"),
        ).arrange(DOWN, buff=0.5)

        for step in steps:
            self.play(FadeIn(step, shift=RIGHT * 0.3))
            self.wait(0.8)

        box = SurroundingRectangle(steps[-1], color=GREEN)
        self.play(Create(box))
        self.wait(2)
