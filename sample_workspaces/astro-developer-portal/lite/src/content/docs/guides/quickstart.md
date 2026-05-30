---
title: Quickstart
sidebar: { order: 1 }
---

```bash
npm install @pylon/sdk
```

```js
import { Pylon } from '@pylon/sdk';
const c = new Pylon({ apiKey: process.env.PYLON_KEY });
await c.ping();
```
