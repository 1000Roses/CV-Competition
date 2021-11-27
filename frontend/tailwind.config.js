module.exports = {
  purge: ['./index.html', './src/**/*.{vue,js,ts,jsx,tsx}'],
  darkMode: false, // or 'media' or 'class'
  theme: {
    extend: {},
    backgroundColor: theme => ({
      ...theme('colors'),
      'header': '#13EC44',
      "cv"    : "#f8fff0",
      "body"  : "#18e7a9"
     })
  },
  variants: {
    extend: {},
  },
  plugins: [],
}
