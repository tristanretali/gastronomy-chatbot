/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./src/**/*.{js,jsx,ts,tsx}"],
  theme: {
    container: {
      center: true,
    },
    extend: {
      minHeight: {
        desktop: "90vh",
      },
      spacing: {
        header: "17rem",
      },
    },
  },
  plugins: [],
};
