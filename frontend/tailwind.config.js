module.exports = {
  purge: ['./index.html', './src/**/*.{vue,js,ts,jsx,tsx}'],
  darkMode: false, // or 'media' or 'class'
  theme: {
    extend: {},
    backgroundColor: theme => ({
      ...theme('colors'),
      "body"  : "#f6f6f6"
     })
  },
  variants: {
    extend: {},
  },
  plugins: [],
}
