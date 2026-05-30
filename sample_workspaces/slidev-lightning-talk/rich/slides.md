---
theme: default
title: Stop typing grep
class: text-center
---

# ⚡ Lightning · 5 min

# Stop typing <span style="color:#dc2626">grep</span>.<br>Start typing <span style="color:#16a34a">rg</span>.

Tess Moreau · Driftwood Eng brown-bag · 2026-05-08

---
layout: center
class: text-center
---

# 11.4×

faster on our monorepo · same query · zero config

---

## The query I run 40 times a day

```bash
# find every call site of a function, across the repo
grep -rn "chargeCustomer" . \
  --include="*.ts" \
  --exclude-dir=node_modules \
  --exclude-dir=dist
```

Four flags I have to remember every single time.

---

## Same thing, ripgrep

```bash
rg "chargeCustomer" -t ts
```

That's it. `rg`:

- **skips `.gitignore`'d paths by default** — no more `--exclude-dir`
- **recurses by default** — no `-r`
- **picks file types by name** — `-t ts`, `-t py`, `-t rust`
- **searches in parallel** across CPU cores

---

## Why it's actually faster

| | grep | ripgrep |
|---|------|---------|
| Honors `.gitignore` | no | yes (skips `node_modules`) |
| Parallelism | single thread | all cores |
| Regex engine | backtracking | finite automata (linear) |
| Unicode | patchy | first-class |

Most of the win isn't the engine — it's **not reading 400 MB of `node_modules`**.

---
layout: two-cols
---

## Things grep can't do

```bash
# search only Python, show 2 lines of context
rg "TODO" -t py -C 2

# every file that does NOT match
rg --files-without-match "license"
```

::right::

## ...and one more

```bash
# search-and-replace preview across the repo
rg "oldName" --replace "newName" \
  --passthru | less
```

Multiline, PCRE2, JSON output — all built in.

---

## "But it's not installed everywhere"

Fair. One line fixes it:

```bash
brew install ripgrep      # macOS
apt install ripgrep       # Debian/Ubuntu
cargo install ripgrep     # anywhere with Rust
```

And it's already bundled inside VS Code, Helix, and most editor search bars —
you've been using it without knowing.

---
layout: center
class: text-center
---

# Try it today

```bash
alias grep='echo "use rg 🙂"'
```

(Okay, maybe not that. But `rg pattern` and never look back.)

github.com/.../ripgrep-cheatsheet · @tess
