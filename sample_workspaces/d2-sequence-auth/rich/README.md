# d2 · OAuth 2.1 + OIDC Sequence (rich)

A full authorization-code-with-PKCE sign-in for the fictional **Larkspur ID**
identity platform. The diagram walks every hop: OIDC discovery, PKCE
challenge generation, the `/authorize` redirect with login + MFA + consent,
the `/token` exchange (verifier check), a Bearer-token resource call that
validates the JWT against a cached JWKS endpoint, and a silent
refresh-token rotation at the end.

Shapes: a `sequence_diagram` with a hexagon SPA actor, a JWKS cylinder, a
dashed key-fetch edge, and grouped sub-flows (`login_check`, `refresh`).

Preview the diagram with the D2 pane (`.d2` ↔ live SVG), or:

```bash
d2 --layout elk sequence.d2 sequence.svg
```
