import { defineConfig } from "astro/config";
import starlight from "@astrojs/starlight";
export default defineConfig({ integrations: [starlight({ title: "Acme RFCs", sidebar: [{ label: "RFCs", autogenerate: { directory: "rfcs" } }] })] });
