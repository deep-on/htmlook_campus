import { defineConfig } from "astro/config";
import starlight from "@astrojs/starlight";

export default defineConfig({
  integrations: [
    starlight({
      title: "Bramble Help",
      description: "FAQ and getting-started for Bramble, the notes app.",
      sidebar: [
        { label: "FAQ", link: "/" },
        { label: "Getting started", link: "/getting-started/" },
      ],
    }),
  ],
});
