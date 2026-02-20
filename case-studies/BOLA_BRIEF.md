# Bola Brief: Case Studies Gallery Page

## Overview
Build a Case Studies gallery page that showcases Aremu Consulting's completed projects. Match the retro-futuristic terminal aesthetic of the homepage.

**Location:** `/data/.openclaw/workspace/projects/aremu-website/case-studies/index.html`

---

## Content Strategy: Two Sections

### SECTION 1: n8n Automations (Group Page)
**Theme:** Quick, elegant automation workflows — the bread and butter work
**Tone:** Efficient, reliable, "this-could-be-you"

**Projects to Include (n8n-based):**
1. **LedgerLens** — AI accounting gateway (2 images)
2. **Connex-One Data Bridge** — CRM to Sheets pipeline (1 image)
3. **ACIA** — Claims automator (8 images)
4. **CAS Tracker** — Claims group tracking (6 images)
5. **DocketLeads** — Legal OCR intake (2 images)
6. **Email Leads to Sheets** — AI-assisted form parsing (1 image)

**Source Material:**
- `/case-studies/assets/ledgerlens/` → mealprep.exe (if related) OR create ledgerlens folder with images
- `/case-studies/assets/connex-one/`
- `/case-studies/assets/acia/`
- `/case-studies/assets/cas-tracker/`
- `/case-studies/assets/docketleads/`
- `/case-studies/assets/email-leads/`

**For descriptions:** Read the original .md files:
- Look for files with "ledgerlens", "connex", "acia", "cas", "docketleads" in the name
- `/case-studies/assets/` may have .txt/.md description files

---

### SECTION 2: Full Systems (Individual Project Pages)
**Theme:** Comprehensive, production-grade applications
**Tone:** Robust, enterprise-ready, "this-changed-their-business"

**Projects with dedicated sub-pages:**

#### 2.1 MealPrep.exe
**Stack:** Google Sheets + Apps Script + APIs  
**Images:** 11 (`/case-studies/assets/mealprep/`)
**Link:** `case-studies/mealprep/index.html`

#### 2.2 Marketing Performance Dashboard
**Stack:** React + Google Sheets overlay  
**Images:** 10 (`/case-studies/assets/marketing-dashboard/` + root assets)
**Link:** `case-studies/marketing-dashboard/index.html`

---

## Design Requirements

### Aesthetic (Match Homepage)
- **Background:** Void black (#0a0a0f) with noise/scanline overlay
- **Typography:** Space Grotesk (display), IBM Plex Mono (body)
- **Colors:** Electric indigo (#6366f1), Cyan (#22d3ee), Hot pink (#f472b6)
- **Cards:** Terminal-style borders, hover effects with glow
- **Animations:** CSS-only scroll reveals, staggered grid loading

### Layout
- **Grid:** 3-column on desktop (n8n automations), 2-column for full systems
- **Hero:** "Systems in Production" with terminal typing animation
- **Filter:** Toggle between "All", "n8n Automations", "Full Systems"

### Card Contents
Each card displays:
- **Project image/thumbnail** (from assets folder)
- **Project name** (Bola can rename as she sees fit)
- **One-line summary** (extract from .md descriptions)
- **Tech stack** (Sheets, n8n, React, etc.)
- **Hours saved per week** (feature prominently)
- **"View Details"** link

### Individual Project Pages (for Full Systems)
Each dedicated page includes:
- Hero with large image
- Problem section (before state)
- Solution section (after state)
- Technical architecture diagram
- Results/ROI stats
- Image gallery (if multiple screenshots)
- CTA: "Book Free 30-Min Call"

---

## Assests Available

```
case-studies/assets/
├── acia/
│   ├── acia_automator_1.png
│   ├── acia_automator_2.png
│   └── [use root assets: ACIA_Details.png, ACIA_Extended.jpg, etc.]
├── cas-tracker/
│   └── tracker_1.jpg through tracker_6.jpg
├── connex-one/
│   └── connex_one_1.png
├── docketleads/
│   ├── docketleads_1.png
│   └── docketleads_2.png
├── email-leads/
│   └── email_leads_1.png
├── ledgerlens/
│   ├── ledgerlens_1.png
│   └── ledgerlens_2.png
├── marketing-dashboard/
│   └── dashboard_1.jpg through dashboard_7.jpg
├── mealprep/
│   └── mealprep_1.png through mealprep_11.jpg
└── [root level assets]
    ├── ACIA_Details.png
    ├── ACIA_Extended.jpg
    ├── Claims_AI_Project.png
    ├── Claims_AI_System.jpg
    ├── Claims_Classification.png
    ├── Claims_Document_AI.jpg
    ├── Connex_One_Updated.jpg
    ├── Invoice_Automation.png
    ├── Invoice_Extraction.jpg
    ├── Luminary_AI_Law_Firm.jpg
    ├── Marketing_Dashboard.jpg
    ├── Marketing_Performance_Dashboard.jpg
    ├── and more...
```

---

## Key Messaging

### For n8n Automations:
- "Fast, reliable automation in weeks"
- "Connect your tools, reclaim your time"
- Starting from £2,000

### For Full Systems:
- "Production-grade applications"
- "Built to run your business"
- Starting from £5,000

---

## CTA Strategy
Throughout the page:
1. **Hero CTA:** "Book Free 30-Min Call" (discuss your automation needs)
2. **n8n Section CTA:** "See What's Automatable"  
3. **Full Systems CTA:** "Discuss Your System Build"
4. **Individual project CTAs:** "Start Similar Project"

---

## Technical Requirements
- HTML5 + Tailwind CSS + Vanilla JS (same as homepage/services)
- Responsive: 1-col mobile, 2-col tablet, 3-col desktop
- Smooth scroll for anchor links
- Image lazy loading for gallery
- SEO-friendly URLs: `/case-studies/`

---

## Navigation
Update navbar links:
- Homepage → `../index.html`
- Services → `../services/index.html`
- Case Studies → `./index.html` (current)
- The Lab → `#` (placeholder)
- Contact → `../index.html#contact-form`

---

## Deliverables
1. `/case-studies/index.html` — Gallery main page
2. `/case-studies/mealprep/index.html` — MealPrep full page
3. `/case-studies/marketing-dashboard/index.html` — Dashboard full page

---

## BEFORE You Start

1. **Read project descriptions** — Look for .md or .txt files in assets folders for detailed writeups
2. **Map images** — Note which image is best suited for hero vs thumbnails
3. **Declare your design choices:**
   - Tone for this page (suggest: "Production Terminal" — more technical, results-focused)
   - Unforgettable Element (suggest: "Before/After slider" or "Living grid of systems")
   - Typography & Color (inherit from homepage)

---

*Ready to build. Make it clickable, make it memorable, make them want to book that call.*
