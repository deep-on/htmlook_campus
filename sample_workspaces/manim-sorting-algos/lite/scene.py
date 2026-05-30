"""manim -p -qm scene.py BubbleSort QuickSort MergeSort"""
from manim import *
import numpy as np
import random

random.seed(42)
ARR = [3, 7, 1, 5, 9, 2, 6, 4]

def make_bars(arr, scale=0.5):
    bars = VGroup()
    for i, v in enumerate(arr):
        b = Rectangle(width=0.5, height=v*scale, fill_color=BLUE, fill_opacity=0.85, stroke_width=1)
        b.move_to(np.array([(i - len(arr)/2)*0.6, v*scale/2 - 1.5, 0]))
        bars.add(b)
    return bars

class BubbleSort(Scene):
    def construct(self):
        title = Text("Bubble Sort · O(n²)", font_size=30).to_edge(UP)
        self.play(FadeIn(title))
        bars = make_bars(ARR.copy())
        self.play(*[GrowFromEdge(b, DOWN) for b in bars])
        a = ARR.copy()
        n = len(a)
        for i in range(n):
            for j in range(n-1-i):
                if a[j] > a[j+1]:
                    a[j], a[j+1] = a[j+1], a[j]
                    self.play(Swap(bars[j], bars[j+1]), run_time=0.18)
        self.wait(1)
