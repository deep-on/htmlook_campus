# manim · ML Fundamentals (rich)

Four scenes covering gradient descent and linear regression:

1. **LossCurve** — the loss `L(w) = 0.4(w−2)² + 0.5` with its global
   minimum marked.
2. **GradientDescent** — a point steps downhill along the loss curve, the
   yellow tangent showing the gradient at each step until it converges.
3. **LinearRegression** — a least-squares line replaces a bad guess to fit
   scattered points.
4. **UpdateRule** — the annotated rule `w ← w − η ∇L(w)` (learning rate and
   gradient labeled).

```bash
pip install -r requirements.txt
manim -pql scene.py LossCurve   # or GradientDescent / LinearRegression / UpdateRule
```

Educational sample — no fictional company. Change `loss` / `grad` or the
learning rate to explore convergence.
