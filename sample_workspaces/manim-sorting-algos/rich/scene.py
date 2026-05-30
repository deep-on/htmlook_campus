"""Sorting algorithms — animated bars for bubble, selection, and merge sort.

Render a single scene:
    manim -pql scene.py BubbleSort
    manim -pql scene.py SelectionSort
    manim -pql scene.py MergeSort
    manim -pql scene.py ComplexityRecap
"""

from manim import *
import numpy as np

ARR = [3, 7, 1, 5, 9, 2, 6, 4]
UNIT = 0.5


def make_bars(arr, scale=0.5):
    bars = VGroup()
    for i, v in enumerate(arr):
        b = Rectangle(
            width=UNIT, height=v * scale,
            fill_color=BLUE, fill_opacity=0.85, stroke_width=1,
        )
        b.move_to(np.array([(i - len(arr) / 2) * 0.6, v * scale / 2 - 1.5, 0]))
        bars.add(b)
    return bars


class BubbleSort(Scene):
    """Adjacent compares and swaps; the largest bubbles to the end."""

    def construct(self):
        title = Text("Bubble Sort · O(n^2)", font_size=30).to_edge(UP)
        self.play(FadeIn(title))
        bars = make_bars(ARR)
        self.play(*[GrowFromEdge(b, DOWN) for b in bars])

        a = ARR.copy()
        n = len(a)
        for i in range(n):
            for j in range(n - 1 - i):
                self.play(
                    bars[j].animate.set_fill(YELLOW),
                    bars[j + 1].animate.set_fill(YELLOW),
                    run_time=0.12,
                )
                if a[j] > a[j + 1]:
                    a[j], a[j + 1] = a[j + 1], a[j]
                    self.play(Swap(bars[j], bars[j + 1]), run_time=0.18)
                    bars[j], bars[j + 1] = bars[j + 1], bars[j]
                self.play(
                    bars[j].animate.set_fill(BLUE),
                    bars[j + 1].animate.set_fill(BLUE),
                    run_time=0.08,
                )
            self.play(bars[n - 1 - i].animate.set_fill(GREEN), run_time=0.15)
        self.wait(1.5)


class SelectionSort(Scene):
    """Pick the minimum of the unsorted suffix and place it at the front."""

    def construct(self):
        title = Text("Selection Sort · O(n^2)", font_size=30).to_edge(UP)
        self.play(FadeIn(title))
        bars = make_bars(ARR)
        self.play(*[GrowFromEdge(b, DOWN) for b in bars])

        a = ARR.copy()
        n = len(a)
        for i in range(n):
            m = i
            self.play(bars[i].animate.set_fill(YELLOW), run_time=0.12)
            for j in range(i + 1, n):
                self.play(bars[j].animate.set_fill(ORANGE), run_time=0.06)
                if a[j] < a[m]:
                    if m != i:
                        self.play(bars[m].animate.set_fill(BLUE), run_time=0.04)
                    m = j
                    self.play(bars[m].animate.set_fill(YELLOW), run_time=0.06)
                else:
                    self.play(bars[j].animate.set_fill(BLUE), run_time=0.04)
            if m != i:
                a[i], a[m] = a[m], a[i]
                self.play(Swap(bars[i], bars[m]), run_time=0.25)
                bars[i], bars[m] = bars[m], bars[i]
            self.play(bars[i].animate.set_fill(GREEN), run_time=0.12)
        self.wait(1.5)


class MergeSort(Scene):
    """Show the divide step, then merge sorted halves back together."""

    def construct(self):
        title = Text("Merge Sort · O(n log n)", font_size=30).to_edge(UP)
        self.play(FadeIn(title))
        bars = make_bars(ARR)
        self.play(*[GrowFromEdge(b, DOWN) for b in bars])

        half = len(ARR) // 2
        left = VGroup(*bars[:half])
        right = VGroup(*bars[half:])
        self.play(
            left.animate.shift(LEFT * 0.8).set_fill(TEAL),
            right.animate.shift(RIGHT * 0.8).set_fill(MAROON),
            run_time=0.8,
        )
        self.wait(0.4)

        merged = sorted(ARR)
        target = make_bars(merged)
        self.play(
            *[Transform(bars[i], target[i]) for i in range(len(ARR))],
            run_time=1.5,
        )
        self.play(*[b.animate.set_fill(GREEN) for b in bars], run_time=0.5)
        self.wait(1.5)


class ComplexityRecap(Scene):
    """Side-by-side complexity summary for the three algorithms."""

    def construct(self):
        title = Text("Complexity recap", weight=BOLD).scale(0.7).to_edge(UP)
        self.play(Write(title))

        rows = VGroup(
            MathTex(r"\text{Bubble} \quad O(n^2)"),
            MathTex(r"\text{Selection} \quad O(n^2)"),
            MathTex(r"\text{Merge} \quad O(n \log n)"),
        ).arrange(DOWN, buff=0.6).scale(1.1)

        for r in rows:
            self.play(FadeIn(r, shift=RIGHT * 0.3), run_time=0.6)
        win = SurroundingRectangle(rows[2], color=GREEN)
        self.play(Create(win))
        self.wait(2)
