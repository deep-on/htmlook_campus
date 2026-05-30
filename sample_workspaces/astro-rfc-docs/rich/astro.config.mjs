import { defineConfig } from "astro/config";
import starlight from "@astrojs/starlight";

export default defineConfig({
  integrations: [
    starlight({
      title: "Northwind RFCs",
      description: "The RFC process and accepted proposals for Northwind Labs engineering.",
      sidebar: [
        { label: "Process", link: "/" },
        {
          label: "RFCs",
          items: [
            { label: "0000 · Template", link: "/rfcs/0000-template/" },
            { label: "0001 · Event schema versioning", link: "/rfcs/0001-event-schema-versioning/" },
          ],
        },
      ],
    }),
  ],
});
