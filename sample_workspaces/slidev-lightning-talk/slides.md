---
theme: default
title: One trick that 8x'd our test suite
class: text-center
---

# ⚡ Lightning · 5 min

# One trick that 8× <span style="color:#16a34a">faster</span> our test suite

@vincent · TIL meetup · 2026-05-08

---
layout: center
class: text-center
---

# 8.4×

faster · same coverage

---

## What

```ts
// before · vitest.config.ts
export default {
  test: { pool: 'forks' }
}

// after
export default {
  test: { pool: 'threads', poolOptions: { threads: { singleThread: false } } }
}
```

---

## Why

| | forks (default) | threads |
|---|----------------|---------|
| Process startup | ~80 ms × N | ~5 ms × N |
| Memory | shared none | shared OK |
| Best for | E2E / IO-heavy | Pure unit tests |

Our suite is 92% pure unit · 8% IO (mocked).
**threads** = right tool.

---
layout: center
class: text-center
---

# Try it

```bash
# vitest.config.ts
export default { test: { pool: 'threads' } }
```

If your tests share state through globals, threads break things — fork-pool first to find dependencies.

github.com/.../parallel-vitest · @vincent
