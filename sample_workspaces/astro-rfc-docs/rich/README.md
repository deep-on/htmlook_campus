# astro-starlight · RFC Documentation Site (rich)

A Starlight site documenting the RFC (Request for Comments) process at the
fictional **Northwind Labs** engineering org. It has a process landing page
explaining how a proposal moves from draft to accepted, a copy-ready RFC
template (0000), and one worked example RFC (0001 · Event schema versioning).
Internal links between the process page, template, and example all resolve.

```bash
npm install
npm run dev      # http://localhost:4321
```

Edit the markdown under `src/content/docs/`; the sidebar is configured in
`astro.config.mjs`. To open a new RFC, copy `rfcs/0000-template.md` to the
next number and fill in the sections.
