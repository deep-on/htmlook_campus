# manim · Sorting Algorithms (rich)

Animated bar charts for three sorting algorithms over the same input
`[3, 7, 1, 5, 9, 2, 6, 4]`:

1. **BubbleSort** — adjacent compares and swaps; the largest value bubbles
   to the end each pass, turning green when locked in.
2. **SelectionSort** — scan the unsorted suffix for its minimum, then swap
   it into place.
3. **MergeSort** — split into two halves, then merge them back into a
   single sorted array.
4. **ComplexityRecap** — `O(n²)` vs `O(n log n)` side by side.

```bash
pip install -r requirements.txt
manim -pql scene.py BubbleSort   # or SelectionSort / MergeSort / ComplexityRecap
```

Educational sample — no fictional company. Edit `ARR` to sort your own
input.
