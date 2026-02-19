# Aremu Consulting Website - Design Brief
## For Bola: Lead Conversion & Web Architect

---

## Project Overview

**Client:** Aremu Consulting LTD  
**Current Site:** https://www.aremuconsulting.com/ (basic landing page)  
**Goal:** Full website with lead conversion focus  

**Hero Value Proposition:**
> "We give you 10 hours of your week back."

---

## Sitemap

### 1. Homepage
- **Hero Section:** Bold value prop + CTA
- **Services Preview:** 3-4 pillar services with icons
- **Social Proof:** Logos of verticals served (Insurance, Legal, Marketing, Logistics, Food Service)
- **Case Study Teaser:** 2-3 featured projects
- **Trust Signals:** Owner-operated, fast turnaround, unusual availability
- **Primary CTA:** "Start Your Audit" or "Book Consultation"

### 2. Services
**Individual pages for each pillar:**
- **CRM Automation** — HubSpot/Salesforce sync, data cleanup, automated reporting
- **Workflow Streamlining** — Process mapping, Zapier/n8n automation, Google Sheets systems
- **Lead Qualification Systems** — AI triage, scoring, automated outreach
- **Document Processing** — OCR, extraction, automated filing
- **Dashboard & Reporting** — Real-time BI, custom visualizations

### 3. Case Studies
- **ACIA** — Accident Claims Intelligent Automator (Insurance)
- **Connex-One Data Bridge** — Contact center reporting
- **DocketLeads AI** — OCR extraction for law firms
- **MealPrep.exe** — ERP for meal prep businesses
- **LedgerLens** — AI expense capture
- **Marketing Performance Dashboard** — Campaign tracking

*Source material: See `/workspace/projects/aremu-website/case-studies/`*

### 4. The Lab (Blog)
- Automation tips
- Case study breakdowns
- Tool reviews (n8n vs Zapier, etc.)
- Industry insights

### 5. Consultation / Enquiry Page
- **Landing page for ads/campaigns**
- Simple form: Name, Email, Company, Problem, Budget, Timeline
- Trust signals near form
- Clear value proposition

---

## Brand Identity

**What Aremu Consulting IS:**
- Technical consultancy specializing in business automation
- Self-taught generalist who builds fast
- Owner-operated (talk to the builder, not account managers)
- Works nights = unusual availability
- No-code + code hybrid approach

**What Aremu Consulting IS NOT:**
- A development agency with teams
- A SaaS consultant pushing platforms
- Cheap offshore labor
- Corporate/consulting firm

**Tone:**
- Professional but direct
- Technical credibility without arrogance
- Builder-first, not theorist
- "Systems that save you hours of manual work every week"

---

## Target Audience

| Profile | Description |
|---------|-------------|
| **Size** | 5-50 employees |
| **Pain** | 10+ hours/week of manual work |
| **Stack** | Google Workspace or Microsoft 365 |
| **Budget** | £2,000–£15,000 |
| **Timeline** | 4-8 weeks to solution |
| **Tech Maturity** | Spreadsheets-fluent, not developers |

**Best Fit Verticals:**
1. Insurance/Claims firms
2. Law firms
3. Marketing agencies
4. Logistics/Delivery
5. Food/Meal prep

---

## Technical Stack

| Layer | Tool |
|-------|------|
| **Data** | Google Sheets |
| **Orchestration** | n8n |
| **Intelligence** | OpenAI/LLM APIs |
| **Frontend** | Google Apps Script / React |
| **Deployment** | Docker + VPS |
| **Extras** | Python scripts |

---

## Success Metrics (For This Website)

| Metric | Target |
|--------|--------|
| **Load Speed** | < 2s first paint |
| **Lighthouse Score** | 90+ |
| **Lead Form Conversion** | > 3% |
| **Mobile Responsive** | Flawless |
| **Accessibility** | WCAG 2.1 AA |

---

## Deliverables

1. **Multi-page static site** (HTML5 + Tailwind + Vanilla JS)
2. **Vercel deployment** (GitHub → Vercel auto-deploy)
3. **Mobile-first responsive** design
4. **Lead capture forms** on Consultation page
5. **Case study pages** with project details
6. **SEO-optimized** metadata, semantic HTML

---

## Creative Direction (Your Call, Bola)

### Tone Options (Choose One):
- **Brutalist Raw** — Exposed structure, industrial
- **Luxury Refined** — Restrained elegance, whitespace
- **Retro-Futuristic** — 80s sci-fi meets modern tech
- **Editorial** — Magazine-quality, dramatic typography

### Must Avoid:
- ❌ Inter or Roboto fonts
- ❌ Generic corporate layouts
- ❌ Stock photo aesthetics
- ❌ "Digital transformation" jargon

### Must Include:
- ✅ Distinctive typography (8vw+ hero text)
- ✅ High-contrast color system (CSS variables)
- ✅ One "Unforgettable Element"
- ✅ CSS-only animations (scroll reveals, hover states)
- ✅ Lead conversion focus (clear CTAs, trust signals)

---

## Design Thinking Protocol (Bola Must Declare Before Code)

### 1. Tone
*State clearly: This project adopts a [TONE] aesthetic...*

### 2. Unforgettable Element  
*State clearly: The Unforgettable Element is...*

### 3. Typography & Color
*Provide CSS variables:*
```css
:root {
  --color-bg: #...;
  --color-primary: #...;
  --color-secondary: #...;
  --color-text: #...;
  --color-muted: #...;
  --font-display: '...', sans-serif;
  --font-body: '...', sans-serif;
}
```

---

## Project Folder

`/data/.openclaw/workspace/projects/aremu-website/`

**Structure:**
```
aremu-website/
├── index.html              # Homepage
├── services/
│   ├── index.html          # Services overview
│   ├── crm-automation.html
│   ├── workflow-streamlining.html
│   ├── lead-qualification.html
│   ├── document-processing.html
│   └── dashboard-reporting.html
├── case-studies/
│   ├── index.html          # Case studies overview
│   ├── acia.html
│   ├── connex-one.html
│   ├── docketleads.html
│   ├── mealprep.html
│   ├── ledgerlens.html
│   └── marketing-dashboard.html
├── lab/                    # Blog posts
├── consultation.html       # Enquiry/landing page
├── assets/
│   ├── fonts/
│   ├── images/
│   └── icons/
├── styles.css              # Tailwind-compiled or custom
├── script.js
└── .gitignore
```

---

## Phase 1: Homepage MVP

**Scope:** Complete homepage with:
- Hero section (10 hours value prop)
- Services preview (4 pillars)
- 2 featured case studies
- Trust signals
- Consultation CTA
- Footer with contact

**Then:** Deploy to Vercel, get live URL

**Then:** Build remaining pages

---

## Constraints

- **No templates** — Every page unique
- **No Inter/Roboto** — Distinctive fonts only
- **Tailwind CSS** — Utility-first
- **Vanilla JS** — No frameworks
- **CSS animations** — No scroll libraries
- **Production-ready** — Clean code, accessible, fast

---

**Ready for Bola's creative declaration. What is the Tone? What is the Unforgettable Element?**
