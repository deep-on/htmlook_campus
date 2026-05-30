# manim · Calculus Intro (rich)

A four-scene explainer for the secant-to-tangent idea behind derivatives:

1. **SecantToTangent** — a secant line through two points on `f(x)=½x²`
   collapses to the tangent as `h → 0`.
2. **LimitDefinition** — the formal limit definition derived term by term.
3. **SlopeReadout** — a live `slope = 2x` readout as the tangent point
   slides along `y = x²`.
4. **FiveFunctions** — the derivatives of `x²`, `sin x`, `eˣ`, `1/x`, `ln x`.

```bash
pip install -r requirements.txt
manim -pql scene.py SecantToTangent   # or LimitDefinition / SlopeReadout / FiveFunctions
```

Educational sample — no fictional company. Change `f` to explore other
curves and their tangents.
