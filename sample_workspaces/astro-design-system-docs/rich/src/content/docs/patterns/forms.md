---
title: Form patterns
description: How to compose Lattice inputs and buttons into a usable, accessible form.
---

A form is the most common place Lattice components meet. This pattern shows how
to lay out, validate, and save a form using the [input](/components/input/) and
[button](/components/button/) components. For the underlying styling, see the
[color tokens](/foundations/color/) and [typography](/foundations/typography/).

## Layout

- **One column.** Stack fields vertically. Multi-column forms slow scanning and
  break on narrow screens.
- **Group related fields** under a heading using the
  [heading type role](/foundations/typography/) — e.g. "Billing address".
- **Primary action bottom-right, secondary to its left.** Use a single
  [primary button](/components/button/) to submit and a `secondary` button to
  cancel.

## Validation

- **Validate on blur, then on submit.** Flagging errors on every keystroke is
  hostile while the user is still typing — let the [input](/components/input/)
  show its error state only after the field loses focus.
- **Inline first, summary second.** Each invalid field shows its own message;
  for long forms, also render an **error summary** at the top that links to the
  first invalid field. This is the single most impactful accessibility move for
  forms.
- **Use real semantics.** `aria-invalid` on the field and `aria-describedby`
  pointing at the message, as shown in the
  [input error state](/components/input/).

## Save state

Long or auto-saving forms should make their state visible so users trust their
work is kept:

- **saved** — quiet confirmation in `--success` (see
  [color tokens](/foundations/color/)).
- **saving** — the submit [button](/components/button/) enters its `loading`
  state; keep its width fixed so nothing jumps.
- **error** — surface a retry affordance, not a dead end.

## Putting it together

A complete Lattice form is just these pieces composed:
[inputs](/components/input/) with labels and helpers, a primary and secondary
[button](/components/button/), validation on blur, and a visible save state —
all themed by the [foundations](/foundations/color/). Start from the
[overview](/) if you need the full map.
