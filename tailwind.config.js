/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./*.html",
    "./**/*.html",
  ],
  theme: {
    extend: {
      colors: {
        void: '#0a0a0f',
        surface: '#141419',
        electric: '#6366f1',
        cyan: '#22d3ee',
        accent: '#f472b6',
        soft: '#e2e2e2',
        steel: '#6b7280',
      },
      fontFamily: {
        display: ['Space Grotesk', 'sans-serif'],
        mono: ['IBM Plex Mono', 'monospace'],
      },
    },
  },
  plugins: [],
}
