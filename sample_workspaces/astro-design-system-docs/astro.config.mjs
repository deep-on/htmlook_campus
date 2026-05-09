import { defineConfig } from 'astro/config';
import starlight from '@astrojs/starlight';
export default defineConfig({ integrations: [starlight({ title: 'Acme Design System', sidebar: [
  { label: 'Foundations', autogenerate: { directory: 'foundations' } },
  { label: 'Components',  autogenerate: { directory: 'components' } },
  { label: 'Patterns',    autogenerate: { directory: 'patterns' } },
] })] });
