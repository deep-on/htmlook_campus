import { defineConfig } from "astro/config";
import starlight from "@astrojs/starlight";

export default defineConfig({
  integrations: [
    starlight({
      title: "Pylon Developers",
      description: "Guides, SDKs, and API reference for the Pylon delivery platform.",
      sidebar: [
        { label: "Overview", link: "/" },
        {
          label: "Get started",
          items: [{ label: "Quickstart", link: "/guides/quickstart/" }],
        },
        {
          label: "SDKs",
          items: [
            { label: "JavaScript / TypeScript", link: "/sdk/javascript/" },
            { label: "Python", link: "/sdk/python/" },
          ],
        },
        {
          label: "Reference",
          items: [{ label: "REST API", link: "/reference/api/" }],
        },
      ],
    }),
  ],
});
