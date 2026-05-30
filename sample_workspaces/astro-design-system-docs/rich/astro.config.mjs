import { defineConfig } from "astro/config";
import starlight from "@astrojs/starlight";

export default defineConfig({
  integrations: [
    starlight({
      title: "Lattice Design System",
      description: "Foundations, components, and patterns for the Lattice design system.",
      sidebar: [
        { label: "Overview", link: "/" },
        {
          label: "Foundations",
          items: [
            { label: "Color", link: "/foundations/color/" },
            { label: "Typography", link: "/foundations/typography/" },
          ],
        },
        {
          label: "Components",
          items: [
            { label: "Button", link: "/components/button/" },
            { label: "Input", link: "/components/input/" },
          ],
        },
        {
          label: "Patterns",
          items: [{ label: "Forms", link: "/patterns/forms/" }],
        },
      ],
    }),
  ],
});
