# Extensions

> Things HTMLook can do beyond opening files — diagrams, slide decks, smart exports — and how to ask for them.

HTMLook ships with a small set of *extensions* and lets you add more later. Most of them just *happen* — you never install or configure anything; you just type and they take effect. A few unlock new export formats or new code-block renderers.

## Built-in (already on, just type)

### Mermaid diagrams

Type a fenced code block tagged `mermaid` and the editor renders it live:

````markdown
```mermaid
flowchart LR
  Browse --> Read
  Read --> Annotate
  Annotate --> Save
```
````

You can also use `mmd` as the tag — both work.

### D2 diagrams

Same idea, different syntax:

````markdown
```d2
direction: right
a -> b -> c
```
````

### Smart Markdown (export)

When you Export → **Markdown (Smart)**, HTMLook runs a polish pass that restores footnotes, tidies tables, and removes stray whitespace. Useful when bouncing the file out to another tool.

### Slide deck (export)

Heading 1's in your Markdown become slide titles. Export → **Slide deck** produces a `.pptx`.

## Discovering more

The **Extensions** panel in the sidebar shows every extension currently enabled, with a coloured dot:

- Solid colour — extension is installed and detected
- Dim ring — extension is installed in HTMLook but the external tool it relies on (e.g. LibreOffice for `.pptx`) isn't on your computer yet. Click the dot to install it (Homebrew handles the install with a progress modal)

Extensions live alongside the rest of your Settings under **Settings → Tools**. The same panel has an **+ Add** button if you want to drop in your own.

## Adding your own

You can drop a markdown file into the workspace's `.claude/skills/` folder describing what you want, and HTMLook treats it as a callable extension during AI conversations. This is an advanced workflow — most users never need it. Existing collections you can copy in (and the wizard to author your own) live under **Settings → Tools → + Add**.

## Next

- [Export →](Export.md)
- [Settings →](Settings.md)
