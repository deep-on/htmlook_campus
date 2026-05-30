import { defineConfig } from 'astro/config';
import starlight from '@astrojs/starlight';
export default defineConfig({ integrations: [starlight({ title: 'Tideline Changelog', sidebar: [
  { label: 'Releases', autogenerate: { directory: 'releases' } },
] })] });
