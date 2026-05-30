---
title: Typography
description: The Lattice type families, scale, and line-height rules.
sidebar:
  order: 2
---

Typography in Lattice is deliberately small: two families and one scale. The
goal is legibility and rhythm, not variety. Pair these rules with the
[color tokens](/foundations/color/) when building a component.

## Families

- **Sans (UI and body):** Inter. Used for everything except code.
- **Mono (code and data):** JetBrains Mono. Used in code blocks, IDs, and
  tabular numerals.

Both ship as variable fonts, so weights between the named steps are available
when needed.

## Type scale

| Role     | Size / line-height | Weight | Notes                       |
|----------|--------------------|--------|-----------------------------|
| Display  | 32px / 1.15        | 800    | `-0.025em` letter-spacing   |
| Heading  | 20px / 1.25        | 700    | section titles              |
| Body     | 14px / 1.55        | 400    | default text                |
| Label    | 13px / 1.4         | 600    | form labels, buttons        |
| Caption  | 12px / 1.4         | 400    | helper and meta text        |

Sizes are a fixed scale rather than fluid — components are dense, and a fixed
scale keeps alignment predictable.

## Rules

- **One display per view.** A screen has a single most-important title; further
  headings step down to Heading.
- **Body line-height is generous (1.55)** because most product copy is read, not
  scanned. Tighten only for single-line labels.
- **Labels are 600 weight, not bold display weight.** They should be findable
  without shouting. This is the weight used by the
  [input label](/components/input/) and [button text](/components/button/).

Next, see how these roles appear in real components: [Button](/components/button/)
and [Input](/components/input/).
