"""Graph traversal — BFS and DFS over a small graph, with queue/stack.

Render a single scene:
    manim -pql scene.py BfsTraversal
    manim -pql scene.py DfsTraversal
    manim -pql scene.py QueueVsStack
"""

from manim import *
import numpy as np
from collections import deque

POSITIONS = {
    "A": np.array([0, 2, 0]),
    "B": np.array([-2, 0.5, 0]), "C": np.array([2, 0.5, 0]),
    "D": np.array([-3, -1, 0]), "E": np.array([-1, -1, 0]),
    "F": np.array([1, -1, 0]), "G": np.array([3, -1, 0]),
}
EDGES = [("A", "B"), ("A", "C"), ("B", "D"), ("B", "E"), ("C", "F"), ("C", "G")]
ADJ = {k: [] for k in POSITIONS}
for u, v in EDGES:
    ADJ[u].append(v)
    ADJ[v].append(u)


def build_graph():
    lines = VGroup(*[
        Line(POSITIONS[a], POSITIONS[b], stroke_width=2, color=GRAY)
        for a, b in EDGES
    ])
    nodes = {
        k: Circle(radius=0.32, color=GRAY, fill_opacity=0.6).move_to(p)
        for k, p in POSITIONS.items()
    }
    labels = {k: Text(k, font_size=20).move_to(p) for k, p in POSITIONS.items()}
    return lines, nodes, labels


class BfsTraversal(Scene):
    """Breadth-first: explore level by level using a queue."""

    def construct(self):
        title = Text("BFS · queue, level by level", font_size=28).to_edge(UP)
        self.play(FadeIn(title))
        lines, nodes, labels = build_graph()
        self.play(Create(lines))
        self.play(*[Create(n) for n in nodes.values()],
                  *[FadeIn(l) for l in labels.values()])
        self.wait(0.4)

        order = []
        seen = {"A"}
        q = deque(["A"])
        while q:
            cur = q.popleft()
            order.append(cur)
            self.play(
                nodes[cur].animate.set_color(GREEN).set_fill(GREEN, opacity=0.9),
                run_time=0.4,
            )
            for nb in ADJ[cur]:
                if nb not in seen:
                    seen.add(nb)
                    q.append(nb)

        path = Text(" → ".join(order), font_size=24, color=GREEN).to_edge(DOWN)
        self.play(Write(path))
        self.wait(2)


class DfsTraversal(Scene):
    """Depth-first: dive deep using a stack before backtracking."""

    def construct(self):
        title = Text("DFS · stack, dive deep", font_size=28).to_edge(UP)
        self.play(FadeIn(title))
        lines, nodes, labels = build_graph()
        self.play(Create(lines))
        self.play(*[Create(n) for n in nodes.values()],
                  *[FadeIn(l) for l in labels.values()])
        self.wait(0.4)

        order = []
        seen = set()

        def dfs(u):
            seen.add(u)
            order.append(u)
            self.play(
                nodes[u].animate.set_color(ORANGE).set_fill(ORANGE, opacity=0.9),
                run_time=0.4,
            )
            for nb in ADJ[u]:
                if nb not in seen:
                    self.play(
                        Line(POSITIONS[u], POSITIONS[nb], color=ORANGE,
                             stroke_width=4).animate.set_opacity(1),
                        run_time=0.001,
                    )
                    dfs(nb)

        dfs("A")
        path = Text(" → ".join(order), font_size=24, color=ORANGE).to_edge(DOWN)
        self.play(Write(path))
        self.wait(2)


class QueueVsStack(Scene):
    """The one-line difference that turns BFS into DFS."""

    def construct(self):
        title = Text("BFS vs DFS = queue vs stack", weight=BOLD).scale(0.6).to_edge(UP)
        self.play(Write(title))

        bfs = VGroup(
            Text("BFS", color=GREEN, weight=BOLD).scale(0.7),
            MathTex(r"\text{next} = \text{queue.popleft()}"),
            Text("explores nearest first", font_size=24),
        ).arrange(DOWN, buff=0.3).shift(LEFT * 3)

        dfs = VGroup(
            Text("DFS", color=ORANGE, weight=BOLD).scale(0.7),
            MathTex(r"\text{next} = \text{stack.pop()}"),
            Text("explores deepest first", font_size=24),
        ).arrange(DOWN, buff=0.3).shift(RIGHT * 3)

        self.play(FadeIn(bfs, shift=RIGHT * 0.3))
        self.play(FadeIn(dfs, shift=LEFT * 0.3))
        divider = DashedLine(UP * 2, DOWN * 2, color=GRAY)
        self.play(Create(divider))
        self.wait(2)
