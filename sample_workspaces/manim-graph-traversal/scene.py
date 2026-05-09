"""manim -p -qm scene.py BfsVsDfs"""
from manim import *
import numpy as np

class BfsVsDfs(Scene):
    def construct(self):
        title = Text("BFS vs DFS · O(V+E)", font_size=30).to_edge(UP)
        self.play(FadeIn(title))

        # binary tree-like graph
        positions = {
            "A": np.array([0, 2, 0]),
            "B": np.array([-2, 0.5, 0]), "C": np.array([2, 0.5, 0]),
            "D": np.array([-3, -1, 0]), "E": np.array([-1, -1, 0]),
            "F": np.array([1, -1, 0]),  "G": np.array([3, -1, 0]),
        }
        edges = [("A","B"),("A","C"),("B","D"),("B","E"),("C","F"),("C","G")]

        nodes = {k: Circle(radius=0.3, color=GRAY, fill_opacity=0.6).move_to(p) for k, p in positions.items()}
        labels = {k: Text(k, font_size=18).move_to(p) for k, p in positions.items()}
        edge_lines = VGroup(*[Line(positions[a], positions[b], stroke_width=2, color=GRAY) for a, b in edges])

        self.play(Create(edge_lines))
        self.play(*[Create(n) for n in nodes.values()], *[FadeIn(l) for l in labels.values()])
        self.wait(0.5)

        # BFS visit order: A, B, C, D, E, F, G
        bfs_order = ["A", "B", "C", "D", "E", "F", "G"]
        narration = Text("BFS · level-by-level", font_size=22, color=GREEN).to_edge(DOWN)
        self.play(FadeIn(narration))
        for k in bfs_order:
            self.play(nodes[k].animate.set_color(GREEN).set_fill(GREEN, opacity=0.9), run_time=0.4)
        self.wait(1)
