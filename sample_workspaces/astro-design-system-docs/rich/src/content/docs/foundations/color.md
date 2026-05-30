---
title: Color tokens
description: The Lattice color palette, expressed as OKLCH design tokens.
sidebar:
  order: 1
---

Lattice colors are exposed as CSS custom properties — design **tokens** — so
components never hard-code a hex value. Change a token and every component that
uses it updates. See how components consume these in [Button](/components/button/)
and [Input](/components/input/).

## Core tokens

| Token         | Value                  | Use                       |
|---------------|------------------------|---------------------------|
| `--accent`    | `oklch(0.74 0.16 195)` | primary action            |
| `--accent-2`  | `oklch(0.70 0.16 280)` | secondary / highlight     |
| `--surface`   | `oklch(0.18 0.016 245)`| card and panel background |
| `--text`      | `oklch(0.95 0.012 240)`| body text                 |
| `--muted`     | `oklch(0.68 0.012 240)`| secondary text, helper    |
| `--danger`    | `oklch(0.62 0.20 25)`  | errors, destructive action|
| `--success`   | `oklch(0.70 0.15 150)` | confirmations             |

## Why OKLCH

We author colors in OKLCH rather than hex or HSL for two reasons:

- **Perceptual uniformity.** Equal numeric steps in lightness look like equal
  visual steps, which makes generating accessible hover and disabled states
  predictable instead of trial-and-error.
- **Wide gamut.** OKLCH maps cleanly onto the P3 displays most of our users have,
  so accents stay vivid without clipping.

## Usage rules

- Use `--accent` for the single most important action on a screen. Reserve it —
  if everything is accented, nothing is. See the
  [button variants](/components/button/) for which variant maps to which intent.
- Never put `--text` on `--accent`; the contrast is too low. Accent surfaces use
  a dedicated on-accent foreground.
- `--danger` is for genuinely destructive or error states only, as used in the
  [input error state](/components/input/).

Pair these tokens with the [type scale](/foundations/typography/) to build a
complete component.
