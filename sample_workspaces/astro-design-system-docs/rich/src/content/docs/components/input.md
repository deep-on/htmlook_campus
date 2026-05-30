---
title: Input
description: The Lattice text input, with label, helper, and error states.
sidebar:
  order: 2
---

The input collects a single line of text. In Lattice an input is never just a
box — it always travels with a **label**, and optionally a **helper** or an
**error** message. Colors come from the [color tokens](/foundations/color/) and
text from the [type scale](/foundations/typography/).

## Anatomy

```html
<div class="field">
  <label class="field-label" for="email">Email</label>
  <input class="input" id="email" type="email" />
  <p class="field-helper">We'll only use this for receipts.</p>
</div>
```

- **Label** uses the [label type role](/foundations/typography/) and is always
  visible — placeholder text is not a substitute for a label.
- **Helper** uses caption text in `--muted` and explains the field before the
  user makes a mistake.

## Error state

```html
<div class="field field-error">
  <label class="field-label" for="email">Email</label>
  <input class="input" id="email" type="email" aria-invalid="true" />
  <p class="field-error-message">Enter a valid email address.</p>
</div>
```

The error message replaces the helper, uses `--danger` from the
[color tokens](/foundations/color/), and the input border picks up the same
token. Set `aria-invalid="true"` so assistive tech announces the error.

## Rules

- **One message slot.** Helper and error share the same space — show the helper
  until there's an error, then swap. Never stack both.
- **Validate on blur, not on every keystroke**, so the field doesn't flash red
  while the user is still typing. The [forms pattern](/patterns/forms/) covers
  when to validate in more detail.
- **Keep the label clickable** via `for`/`id` so tapping the label focuses the
  input — important on touch.

Inputs are almost always grouped into a [form](/patterns/forms/) and submitted
with a [button](/components/button/).
