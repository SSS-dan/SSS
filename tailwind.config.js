const colors = require('tailwindcss/colors')

/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./**/*.{html,js}"],
  theme: {
    extend: {
      colors: {
        teal: colors.teal,
        mint: {
          light: "#e9f9fd",
          DEFAULT: "#17a8c9",
          dark: "#128aa6",
        },
        sogang: "#b30000",
        sogang_bold: "#7d0000",
        sogang_blue: "#523CD8",
        sogang_light: "#7785FF",
      },
    },
  },
  plugins: [],

}

