# manim · Matrix Multiplication (rich)

A four-scene visual explainer for matrix multiplication, built around
`A = [[2, 1], [0, 3]]` and `B = [[1, 4], [2, 1]]`:

1. **DotProductRow** — one output entry is a row dotted with a column.
2. **BuildProduct** — fill the product matrix entry by entry, highlighting
   the row/column pair behind each value.
3. **DimensionRule** — why the inner dimensions `(m×n)·(n×p)` must match.
4. **ComposeTransforms** — a `LinearTransformationScene` showing the product
   as the composition of two linear maps (apply `B`, then `A`).

```bash
pip install -r requirements.txt
manim -pql scene.py DotProductRow   # or BuildProduct / DimensionRule / ComposeTransforms
```

Educational sample — no fictional company. Swap `A` and `B` to explore
other products.
