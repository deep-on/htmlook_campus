---
theme: default
title: Acme Q3 Review
class: text-center
transition: slide-left
mdc: true
---

# Acme Q3 Review

Vincent · 2026-Q3

<div class="text-sm opacity-60 mt-12">
  ⌘ + → 다음 슬라이드
</div>

---
layout: section
---

# 핵심 지표

---

## 매출 / 가입자 / NPS

| 지표         | Q2     | Q3     | Δ      |
|--------------|--------|--------|--------|
| 매출 (M)     | 4.20   | 5.10   | +21%   |
| 신규 가입자  | 8,400  | 11,200 | +33%   |
| NPS          | 42     | 48     | +6     |

<v-click>

> Q3 최대 동력: 모바일 onboarding 단축 (5단계 → 2단계).

</v-click>

---
layout: two-cols
---

# 다음 분기 우선순위

::default::

- 모바일 retention 개선
- API 엔터프라이즈 티어
- DACH 지역 진출

::right::

```ts {1,3-5}{at:'click'}
const goals = {
  retention: '+15%',
  enterprise_arr: '$2.4M',
  dach_signups: 1500,
};
```

---
layout: center
class: text-center
---

# 질문 / 토론

slidev → `pnpm dev` → http://localhost:3030
