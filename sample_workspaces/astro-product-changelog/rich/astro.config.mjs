import { defineConfig } from "astro/config";
import starlight from "@astrojs/starlight";

export default defineConfig({
  integrations: [
    starlight({
      title: "Tideline Changelog",
      description: "New features, changes, and fixes for Tideline analytics.",
      sidebar: [
        { label: "What's new", link: "/" },
        {
          label: "Releases",
          items: [
            { label: "v3.0.0", link: "/releases/v3-0-0/" },
            { label: "v2.8.0", link: "/releases/v2-8-0/" },
            { label: "v2.7.1", link: "/releases/v2-7-1/" },
          ],
        },
      ],
    }),
  ],
});
