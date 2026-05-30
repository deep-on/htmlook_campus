# manim · Fourier series & transform (rich)

A five-scene visual explainer that builds Fourier intuition from the ground
up, centered on the square wave and its odd-harmonic series
`f(t) = (4/π) Σ_{k odd} sin(k t) / k`:

1. **Intro** — the general Fourier-series formula `f(t) = a₀/2 + Σ[aₙ cos + bₙ sin]`.
2. **SquareWaveBuildup** — partial sums of 1, 2, … 6 sine terms converging
   toward a square wave (watch the Gibbs overshoot at the edges).
3. **Epicycles** — three chained rotating arrows (harmonics 1, 3, 5) whose
   final tip traces the reconstructed path with a `TracedPath`.
4. **TimeAndFrequency** — a time-domain signal `sin(3t) + 0.5 sin(7t)` on top,
   its discrete amplitude spectrum `|F(ω)|` below, joined by an FFT arrow.
5. **HarmonicAmplitudes** — deriving the coefficients `bₙ` of the square wave
   by hand, ending at `bₙ = 4/(nπ)` for odd `n`.

```bash
pip install -r requirements.txt

manim -pql scene.py Intro
manim -pql scene.py SquareWaveBuildup
manim -pql scene.py Epicycles
manim -pql scene.py TimeAndFrequency
manim -pql scene.py HarmonicAmplitudes
```

Use `-qm` or `-qk` instead of `-ql` for medium / 4K renders.

Educational sample — no fictional company. Change `ODD_HARMONICS` or the
`freqs` list in **Epicycles** to reconstruct other waveforms.
