import { defineConfig } from "astro/config";
import starlight from "@astrojs/starlight";
export default defineConfig({ integrations: [starlight({ title: "Northwind RFCs", sidebar: [{ label: "RFCs", autogenerate: { directory: "rfcs" } }] })] });
