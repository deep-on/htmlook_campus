import { defineConfig } from 'astro/config';
import starlight from '@astrojs/starlight';
export default defineConfig({
  integrations: [starlight({
    title: 'Acme API',
    description: 'REST API reference for the Acme platform',
    sidebar: [
      { label: 'Get Started', items: [{ slug: 'index' }, { slug: 'auth/api-keys' }] },
      { label: 'Auth',     autogenerate: { directory: 'auth' } },
      { label: 'Orders',   autogenerate: { directory: 'orders' } },
      { label: 'Customers',autogenerate: { directory: 'customers' } },
      { label: 'Webhooks', autogenerate: { directory: 'webhooks' } },
    ],
  })],
});
