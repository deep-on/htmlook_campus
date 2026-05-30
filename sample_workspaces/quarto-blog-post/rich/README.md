# quarto · Engineering Blog Post (rich)

A complete technical blog post — YAML front matter, table of contents,
a decision matrix, two executable Python chunks (a table + a latency plot),
and a lessons section. The story: Lumen Commerce moving its order pipeline
from self-hosted Kafka to SQS.

Preview / render:

```bash
quarto preview index.qmd   # live
quarto render  index.qmd   # → index.html
```

Code chunks are foldable. Swap in your own data and narrative; the structure
(TL;DR → background → decision table → migration → lessons) is the template.
