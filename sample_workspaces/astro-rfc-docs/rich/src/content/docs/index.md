---
title: The Northwind RFC process
description: How engineering proposals move from draft to accepted at Northwind Labs.
---

Substantial changes to Northwind systems — new public APIs, data-format changes,
cross-team dependencies, or anything hard to reverse — go through an RFC. Small,
local changes do not; a normal pull request is enough. When in doubt, open an
RFC: the cost of writing one is far lower than the cost of an undiscussed
breaking change.

## Lifecycle

An RFC moves through five states:

1. **Draft** — you open a PR adding a file under `rfcs/`. Discussion happens in
   the PR thread.
2. **In review** — at least two reviewers from affected teams are assigned. The
   author addresses comments and updates the document in place.
3. **Final comment period (FCP)** — a 5-business-day window where the proposal
   is considered done pending objections. Announced in `#eng-rfcs`.
4. **Accepted** — FCP closes with no blocking objections; the PR merges and an
   implementation tracking issue is opened.
5. **Rejected / Withdrawn** — closed with a short rationale recorded in the
   document so future authors can find it.

## Writing an RFC

Copy the [RFC template (0000)](/rfcs/0000-template/) to the next available
number and fill in every section. Empty sections are a signal the proposal
isn't ready — write "N/A" with a reason rather than leaving a heading blank.

The single most important section is **Drawbacks**: a reviewer's first question
is always "what does this cost us?" Answer it before they ask.

## A worked example

[RFC 0001 · Event schema versioning](/rfcs/0001-event-schema-versioning/) is a
complete, accepted RFC. Read it alongside the template to see the expected
depth — concrete enough to implement from, short enough to review in one
sitting.

## Reviewer expectations

- Respond within two business days of being assigned.
- Distinguish **blocking** objections (this is wrong / unsafe) from
  **non-blocking** preferences (I'd do it differently). Only blocking
  objections stop an RFC.
- Approve the trade-off, not perfection. Every design has drawbacks; the
  question is whether they're acknowledged and acceptable.

---

Questions about the process? Ask in `#eng-rfcs` or read an accepted RFC like
[0001](/rfcs/0001-event-schema-versioning/) for a concrete model.
