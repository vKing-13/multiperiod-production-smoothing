/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './main/templates/*.{html,js}',
    './node_modules/flowbite/**/*.{html,js}'
  ],
  theme: {
    extend: {},
  },
  plugins: [
    require('flowbite/plugin')
  ],
}
