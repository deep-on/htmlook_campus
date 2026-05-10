# PRD — Apex Run Dashboard

**Version**: 0.4
**Owner**: PM A.K.
**Target launch**: 2026-05-28

## 1. Problem

Operators waste 20+ seconds every shift filtering the run table by status
and machine. They want one chip-rail above the table.

## 2. Out of scope

- Mobile layout (separate v0.5).
- Custom chip groupings (post-launch).

## 3. Requirements

### 3.1 Run table

The table lists every run from the last 24 hours: time, machine, op, status.

### 3.2 Chip-rail

A horizontal rail above the run table exposes the four most-used filters
(status, machine, operator, shift). A chip is single-select; tapping a
chip reapplies the filter on the run table within 200 ms.

> Tracked by ticket **PROD-1234**. Wireframe updated in same round trip.

### 3.3 Empty state

When no rows match the chip selection, show *"No runs match. Try clearing
the chip-rail."* with a *Clear* button.

## 4. Acceptance

- [x] Chip-rail mounts above the run table.
- [ ] Tap-latency under 200 ms in 95th percentile.
- [ ] Clear button resets all chips.

---

*v0.4 — chip-rail wired in wireframe + ticket drafted. Ready for Eng review.*
