# Aremu Consulting Website - Changelog

## 2026-04-20: Performance, SEO, and UX Improvements

### Performance
- **Compiled Tailwind CSS**: Switched from CDN (350KB) to locally compiled CSS (35KB) - ~10x reduction
  - Added `npm run build:css` script
  - Added `@tailwindcss/cli` and `@tailwindcss/postcss` dependencies
  - All pages now reference local `assets/styles.css`

### SEO
- **JSON-LD Structured Data**: Added schema markup
  - Homepage: `ProfessionalService` schema with service catalog
  - Services page: `Service` schema with all offerings
  - Solopreneur page: `Service` + `FAQPage` schemas
  - Improves SERP visibility and rich snippets

### Conversion Optimization
- **Sticky Mobile CTA**: Fixed bottom "Book Free Audit" button
  - Appears after scrolling past 60% of hero
  - Auto-hides when contact form is visible
  - Added to homepage, services, solopreneur pages

- **Testimonials Section**: Added social proof section
  - Positioned between trust signals and CTA
  - 2 placeholder testimonials (replace with real quotes)
  - Star ratings with name and title

- **FAQ Section**: Added expandable FAQ on homepage
  - Reduces friction by answering common questions
  - 4 questions covering tools, timeline, technical skills, post-build support

### UX Improvements
- **Font Preloading**: Added async font loading for faster initial render
- **Breadcrumb Navigation**: Added to inner pages (services, case-studies, lab)

### Accessibility
- **Skip-to-Content Link**: Added keyboard navigation link
- **sr-only CSS Class**: Added screen reader utility styles

### Bug Fixes
- Fixed corrupted Google Fonts URLs in services.html and solopreneur.html
- Fixed missing font preconnect on inner pages

---

## Development Commands

```bash
# Install dependencies
npm install

# Build CSS (after changes to assets/main.css)
npm run build:css

# Watch CSS for development
npm run watch:css
```

---

## Files Modified

| File | Changes |
|------|---------|
| `assets/main.css` | Added sr-only styles |
| `assets/styles.css` | Compiled Tailwind CSS |
| `index.html` | All improvements (preload, FAQ, testimonials, sticky CTA, skip link) |
| `services.html` | Font preload, JSON-LD schema |
| `services/index.html` | Breadcrumbs |
| `solopreneur.html` | Font preload, JSON-LD schema |
| `case-studies/index.html` | Breadcrumbs |
| `lab/index.html` | Breadcrumbs |
| `package.json` | Added build scripts |
| `postcss.config.js` | PostCSS configuration |
| `tailwind.config.js` | Tailwind v4 configuration |

---

## TODO

- [ ] Replace placeholder testimonials with real client quotes
- [ ] Add client logos (with permission) for social proof
- [ ] Consider adding "years in business" trust signal
- [ ] Add urgency elements (e.g., "Limited availability")
- [ ] Monitor Core Web Vitals for performance
- [ ] Set up analytics conversion tracking
