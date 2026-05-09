from manim import *
class Eigen(Scene):
    def construct(self):
        title = Text("Eigenvectors · stretched but not rotated").scale(0.6)
        self.play(Write(title)); self.wait(2)
