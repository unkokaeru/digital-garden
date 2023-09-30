import { QuartzConfig } from "./quartz/cfg"
import * as Plugin from "./quartz/plugins"

const config: QuartzConfig = {
  configuration: {
    pageTitle: "The Knowledge Cottage",
    enableSPA: true,
    enablePopovers: true,
    analytics: {
      provider: "plausible",
    },
    baseUrl: "mydigitalgarden.space",
    ignorePatterns: ["private", "templates"],
    defaultDateType: "created",
    theme: {
      typography: {
        header: "Spectral",
        body: "Spectral",
        code: "JetBrains Mono",
      },
      colors: {
        lightMode: {
          light: "#f3f3eb", // background
          lightgray: "#e5e5e5", // search bar
          gray: "#b8b8b8", // date
          darkgray: "#4e4e4e", // body text
          dark: "#2b2b2b", // headings
          secondary: "#284b63", // hyperlinks and title
          tertiary: "#84a59d", // highlighted hyperlink
          highlight: "rgba(143, 159, 169, 0.15)",
        },
        darkMode: {
          light: "#201c14", // background
          lightgray: "#393639", // search bar
          gray: "#646464", // date
          darkgray: "#d4d4d4", // body text
          dark: "#ebebec", // headings
          secondary: "#7b97aa", // hyperlinks and title
          tertiary: "#84a59d", // highlighted hyperlink
          highlight: "rgba(143, 159, 169, 0.15)",
        },
      },
    },
  },
  plugins: {
    transformers: [
      Plugin.FrontMatter(),
      Plugin.TableOfContents(),
      Plugin.CreatedModifiedDate({
        priority: ["frontmatter", "filesystem"], // you can add 'git' here for last modified from Git but this makes the build slower
      }),
      Plugin.SyntaxHighlighting(),
      Plugin.ObsidianFlavoredMarkdown({ enableInHtmlEmbed: false }),
      Plugin.GitHubFlavoredMarkdown(),
      Plugin.CrawlLinks({ markdownLinkResolution: "shortest" }),
      Plugin.Latex({ renderEngine: "katex" }),
      Plugin.Description(),
    ],
    filters: [Plugin.RemoveDrafts()],
    emitters: [
      Plugin.AliasRedirects(),
      Plugin.ComponentResources({ fontOrigin: "googleFonts" }),
      Plugin.ContentPage(),
      Plugin.FolderPage(),
      Plugin.TagPage(),
      Plugin.ContentIndex({
        enableSiteMap: true,
        enableRSS: true,
      }),
      Plugin.Assets(),
      Plugin.Static(),
    ],
  },
}

export default config
