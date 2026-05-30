import { defineConfig } from 'astro/config';
import starlight from '@astrojs/starlight';
export default defineConfig({ integrations: [starlight({ title: 'Pylon Developers', sidebar: [
  { label: 'Get Started', autogenerate: { directory: 'guides' } },
  { label: 'SDKs',        autogenerate: { directory: 'sdk' } },
  { label: 'Reference',   autogenerate: { directory: 'reference' } },
] })] });
