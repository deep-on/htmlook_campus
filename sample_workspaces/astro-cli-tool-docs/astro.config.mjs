import { defineConfig } from 'astro/config';
import starlight from '@astrojs/starlight';
export default defineConfig({
  integrations: [starlight({
    title: 'Skiff CLI',
    sidebar: [
      { label: 'Commands', autogenerate: { directory: 'commands' } },
      { label: 'Flags',    autogenerate: { directory: 'flags' } },
    ],
  })],
});
