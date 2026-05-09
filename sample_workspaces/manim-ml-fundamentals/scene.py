"""manim -p -qm scene.py BackpropIntro"""
from manim import *
import numpy as np

class BackpropIntro(Scene):
    def construct(self):
        title = Text("Backpropagation · 경사 하강의 핵심", font_size=30).to_edge(UP)
        self.play(FadeIn(title))

        # 2-layer NN graph
        layers = [3, 4, 2]
        positions = []
        for li, n in enumerate(layers):
            xs = np.full(n, li * 2 - 2)
            ys = np.linspace(1.5, -1.5, n)
            positions.append([np.array([x, y, 0]) for x, y in zip(xs, ys)])

        nodes = VGroup()
        for layer in positions:
            for p in layer:
                nodes.add(Dot(p, radius=0.16, color=BLUE))

        edges = VGroup()
        for li in range(len(layers) - 1):
            for a in positions[li]:
                for b in positions[li+1]:
                    edges.add(Line(a, b, stroke_width=1, color=GRAY))

        self.play(Create(edges), FadeIn(nodes))
        self.wait(0.5)

        # forward arrow
        fwd = Arrow(LEFT*3, RIGHT*3, color=GREEN, buff=0.3).shift(UP*2)
        fwd_label = Text("forward · loss", font_size=20, color=GREEN).next_to(fwd, UP)
        self.play(Create(fwd), Write(fwd_label))
        self.wait(0.6)

        # backward arrow
        bwd = Arrow(RIGHT*3, LEFT*3, color=RED, buff=0.3).shift(DOWN*2)
        bwd_label = Text(r"backward · ∇L", font_size=20, color=RED).next_to(bwd, DOWN)
        self.play(Create(bwd), Write(bwd_label))
        self.wait(2)
