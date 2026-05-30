# astro-starlight · Product Changelog (rich)

A Starlight changelog site for the fictional **Tideline** product analytics
platform. The landing page explains how to read the changelog and links to the
three most recent releases (v3.0.0, v2.8.0, v2.7.1), each with its own page.
All internal links between the index and the release pages resolve.

```bash
npm install
npm run dev      # http://localhost:4321
```

Add a release by creating a new file under `src/content/docs/releases/` and
adding it to the sidebar in `astro.config.mjs`. Entries use a simple legend:
`+` added, `~` changed, `!` breaking, and `fix` for bug fixes.
