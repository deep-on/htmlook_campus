# manim · Eigenvectors (rich)

A three-scene visual explainer for eigenvectors and eigenvalues, built
around the matrix `[[2, 1], [1, 2]]`:

1. **Intro** — the defining equation `A v = λ v`.
2. **EigenTransform** — a `LinearTransformationScene` showing an eigenvector
   keeping its direction while a generic vector rotates.
3. **ComputeExample** — solving `det(A − λI) = 0` step by step.

```bash
pip install -r requirements.txt
manim -pql scene.py Intro            # or EigenTransform / ComputeExample
```

Educational sample — no fictional company. Swap the matrix `A` to explore
other transformations.
