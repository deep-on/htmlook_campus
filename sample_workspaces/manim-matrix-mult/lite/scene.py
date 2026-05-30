from manim import *
class MatrixMult(Scene):
    def construct(self):
        m = Matrix([[2, 1], [1, 3]])
        self.play(Write(m)); self.wait(1)
        self.play(m.animate.shift(LEFT*2)); self.wait(1)
