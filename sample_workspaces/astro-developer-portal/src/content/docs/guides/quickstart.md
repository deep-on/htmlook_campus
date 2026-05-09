---
title: Quickstart
sidebar: { order: 1 }
---
```bash
npm install @acme/sdk
```
```js
import { Acme } from '@acme/sdk';
const c = new Acme({ apiKey: process.env.ACME_KEY });
await c.ping();
```
