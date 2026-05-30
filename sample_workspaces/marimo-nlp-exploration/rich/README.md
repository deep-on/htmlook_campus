# marimo · NLP Text Exploration (rich)

A reactive marimo notebook exploring a small inline corpus of customer
reviews. Twelve cells: imports → corpus → summary → tokenization →
word-frequency table + bar chart → tiny lexicon sentiment → sentiment
chart → takeaway. Self-contained — no model or corpus downloads.

```bash
pip install marimo numpy pandas matplotlib
marimo edit notebook.py     # reactive editor
marimo run  notebook.py     # app mode
```

Replace the inline `reviews` list with your own strings to analyze, and
extend the `POSITIVE` / `NEGATIVE` lexicons to sharpen the sentiment score.
