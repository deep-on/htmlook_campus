---
title: RFC 0000 · Template
description: Copy this file to start a new RFC.
---

Copy this file to `rfcs/NNNN-short-title.md`, where `NNNN` is the next unused
number. Fill in every section. For background on the workflow, see the
[RFC process](/). For a completed example, see
[RFC 0001](/rfcs/0001-event-schema-versioning/).

- **Status:** Draft
- **Author:** Your Name
- **Created:** YYYY-MM-DD
- **Tracking issue:** (added on acceptance)

## Summary

One paragraph. If a reader stops here, what is being proposed and why?

## Motivation

What problem does this solve? What can't we do today, or what is painful? Use
concrete examples or incidents rather than abstractions. A reviewer should
finish this section agreeing the problem is worth solving.

## Detailed design

The bulk of the RFC. Describe the proposal in enough detail that someone other
than the author could implement it. Include data shapes, API signatures,
migration steps, and how the change behaves at the boundaries (errors, empty
input, rollback).

## Drawbacks

Why might we *not* do this? Cost, added complexity, maintenance burden, and risk
all belong here. An RFC with an empty Drawbacks section is not finished.

## Alternatives

What other designs were considered, and why were they set aside? "Do nothing"
is always a valid alternative to weigh.

## Open questions

Things deliberately left unresolved, to be settled during review or
implementation. Move each one to the design or drawbacks section as it's
answered.
