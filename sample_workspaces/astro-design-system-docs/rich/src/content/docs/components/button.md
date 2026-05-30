---
title: Button
description: Lattice button variants, states, and usage guidance.
sidebar:
  order: 1
---

The button triggers an action. Its variant communicates how important or
risky that action is. Buttons draw their fill from the
[color tokens](/foundations/color/) and their text from the
[label type role](/foundations/typography/).

## Variants

```html
<button class="btn btn-primary">Save</button>
<button class="btn btn-secondary">Cancel</button>
<button class="btn btn-ghost">Learn more</button>
<button class="btn btn-danger">Delete account</button>
```

| Variant     | Fill token   | When to use                                   |
|-------------|--------------|-----------------------------------------------|
| `primary`   | `--accent`   | the main action on a view — one per screen.   |
| `secondary` | `--surface`  | supporting actions like Cancel.               |
| `ghost`     | transparent  | low-emphasis or repeated inline actions.      |
| `danger`    | `--danger`   | destructive actions only.                     |

There should be at most **one primary button per view**. If two actions feel
equally important, the layout needs rethinking, not two accents.

## States

Every variant supports four interactive states:

- **hover** — lighten the fill one perceptual step (easy because tokens are
  [OKLCH](/foundations/color/)).
- **active** — darken one step.
- **disabled** — reduce opacity and remove pointer events; never just grey the
  text, which reads as an error.
- **loading** — show an inline spinner and keep the button width fixed so the
  layout doesn't jump.

## Accessibility

- Use a real `<button>` element so keyboard and screen-reader behavior come for
  free.
- A button with only an icon needs an `aria-label`.
- Never disable the submit button as the *only* validation feedback — pair it
  with inline messages, as described in the [forms pattern](/patterns/forms/).

Buttons are most often used inside a [form](/patterns/forms/) alongside the
[input](/components/input/) component.
