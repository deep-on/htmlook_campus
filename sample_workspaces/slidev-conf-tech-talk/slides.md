---
theme: seriph
title: Reactivity in Vue 4
info: |
  ## VueConf 2026 · 30 min talk
  by @your-handle
class: text-center
transition: slide-left
mdc: true
---

# Reactivity in Vue 4

Anthony Fu  ·  VueConf 2026  ·  30 min

<div class="text-sm opacity-60 mt-12">⌘ + → to advance</div>

---
layout: section
---

# Why this matters

---

## The cost of reactivity

Every framework pays for change detection somehow:

| Framework | Strategy | Cost |
|-----------|----------|------|
| React | Re-render + diff | O(tree) per update |
| Vue 3 | Proxy + dep graph | O(deps) per update |
| Solid | Compile-time tracking | ~O(1) per signal |
| Svelte 5 | Runes + compiler | ~O(deps) compile-time |
| **Vue 4** | **$state runes + Proxy** | **~O(1) hot path** |

<v-click>

> Vue 4's runes give us Solid-like signal granularity AND backwards compat.

</v-click>

---
layout: two-cols
---

# Before · Vue 3

::default::

```ts {1-6}{at:0}
import { ref, computed } from 'vue'

const x = ref(0)
const y = computed(() => x.value * 2)

x.value++
```

::right::

- ✓ Familiar
- ✗ Wrapper objects
- ✗ `.value` everywhere
- ✗ Boilerplate

---
layout: two-cols
---

# After · Vue 4

::default::

```ts {1-5}{at:'click+1'}
const x = $state(0)
const y = $derived(x * 2)

x++  // just a number
```

::right::

- ✓ Plain numbers
- ✓ No `.value`
- ✓ Auto-tracked
- ✓ Compiler unwraps

---

## Live demo

<iframe src="https://stackblitz.com/edit/vue4-reactivity-demo" class="w-full h-96"></iframe>

---
layout: section
---

# How it works under the hood

---

## Proxy + auto-tracking

```ts {1-9|11-13|15-17|all}{lines:true}
function $state<T>(initial: T): T {
  const dep = new Set<Effect>()
  return new Proxy(box(initial), {
    get(t, k) {
      track(dep)
      return Reflect.get(t, k)
    },
    set(t, k, v) {
      Reflect.set(t, k, v)
      trigger(dep)
      return true
    },
  })
}

// $derived auto-collects deps via track()
function $derived<T>(fn: () => T): T { return memo(fn) }
```

---

## Performance numbers

```
Benchmark: 100k updates of `count++` in tight loop
                Vue 3 ref     Vue 4 $state
ms              312           87
allocations     200k          0
GC pauses       4             0
```

---
layout: center
class: text-center
---

# Try it

```bash
npm create vue@4
```

[github.com/vuejs/core/discussions](https://github.com/vuejs/core/discussions)

---
layout: end
---

# Thanks!

@your-handle  ·  vueconf2026.dev/reactivity
