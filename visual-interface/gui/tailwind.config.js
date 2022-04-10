const production = !process.env.ROLLUP_WATCH;
const colors = require('./node_modules/tailwindcss/colors');

module.exports = {
  mode: "jit",
  purge: {
    content: [
      "./src/**/*.svelte",
    ],
    enabled: production // disable purge in dev
  },
  darkMode: false, // or 'media' or 'class'
  theme: {
    extend: {
      colors: {
        orange: colors.orange
      },
      fontFamily: {
        jetbrains: ["JetBrains Mono", "monospace"]
      }
    },
  },
  variants: {
    extend: {},
  },
  plugins: [],
  future: {
    purgeLayersByDefault: true,
    removeDeprecatedGapUtilities: true,
  }
}
