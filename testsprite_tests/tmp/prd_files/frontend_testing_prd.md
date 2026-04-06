# Frontend Testing PRD — Purbanchal Synergies Pvt. Ltd. Website

> **Document Version:** 1.0  
> **Date:** April 1, 2026  
> **Author:** QA Engineering  
> **Website:** Purbanchal Synergies Pvt. Ltd. — Corporate Portfolio  
> **Tech Stack:** HTML5, CSS3 (Vanilla), JavaScript (Vanilla), Swiper.js, Chart.js, FontAwesome  
> **Pages Under Test:** `index.html`, `about.html`, `projects.html`, `services.html`, `contact.html`

---

## 1. Executive Summary

This PRD defines all frontend testing requirements for the Purbanchal Synergies Pvt. Ltd. corporate website. The website is a premium, multi-page static corporate portfolio with interactive components including hero sliders, tabbed service panels, filterable team directories, a dynamic project dashboard with charts and modals, and a contact form. This document covers functional, visual, responsive, accessibility, performance, and cross-browser test scopes.

---

## 2. Objectives

| # | Objective | Priority |
|---|-----------|----------|
| 1 | Verify all navigation links across all pages resolve correctly | 🔴 Critical |
| 2 | Ensure all interactive components function as designed | 🔴 Critical |
| 3 | Validate responsive design across breakpoints (320px – 2560px) | 🔴 Critical |
| 4 | Confirm visual fidelity and brand consistency (typography, colors, spacing) | 🟠 High |
| 5 | Verify all images, logos, and assets load without errors | 🔴 Critical |
| 6 | Validate SEO meta tags, heading hierarchy, and semantic HTML | 🟡 Medium |
| 7 | Confirm cross-browser compatibility (Chrome, Firefox, Safari, Edge) | 🟠 High |
| 8 | Validate animations, transitions, and scroll-triggered effects | 🟡 Medium |
| 9 | Test performance metrics (LCP, FID, CLS) | 🟡 Medium |
| 10 | Ensure basic accessibility compliance (WCAG 2.1 Level A) | 🟠 High |

---

## 3. Scope & Architecture Overview

### 3.1 Site Map

```
index.html (Home)
├── about.html (Who We Are)
├── projects.html (Projects — Data Dashboard)
├── services.html (Services / Our Expertise)
└── contact.html (Contact Us)
```

### 3.2 Shared Components (All Pages)

| Component | Description |
|-----------|-------------|
| **Navbar** | Fixed position, transparent-to-solid on scroll, mobile hamburger toggle |
| **Footer** | 4-column grid: Brand, Quick Links, Services, Contact Info |
| **CTA Button ("Work With Us")** | Header gradient button linking to `contact.html` |
| **Logo** | PSPL logo with company name, linking to `index.html` |
| **Active Link** | Orange underline indicator for current page |

### 3.3 External Dependencies

| Library | Version | Purpose |
|---------|---------|---------|
| Google Fonts | — | Poppins, Inter, Orbitron (projects page) |
| FontAwesome | 6.4.0 | Icons |
| Swiper.js | 11.x | Hero slider, 3-card slider |
| Chart.js | Latest | Project analytics (doughnut + bar) |

### 3.4 CSS Design Tokens

```
--primary-color: #051424 (Deep Blue)
--accent-color: #FF6600 (Electric Orange)
--bg-main: #f8fafc
--bg-white: #ffffff
--text-dark: #1e293b
--text-muted: #64748b
```

---

## 4. Test Suites

### 4.1 Global Navigation & Routing

#### TC-NAV-001: Navbar Link Integrity
| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Click "Home" link from any page | Navigates to `index.html` |
| 2 | Click "Who We Are" link | Navigates to `about.html` |
| 3 | Click "Projects" link | Navigates to `projects.html` |
| 4 | Click "Services" link | Navigates to `services.html` |
| 5 | Click "Contact Us" link | Navigates to `contact.html` |
| 6 | Click "Work With Us" CTA button | Navigates to `contact.html` |
| 7 | Click PSPL Logo from any page | Navigates to `index.html` |

#### TC-NAV-002: Active Link State
| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Navigate to `index.html` | "Home" link has `active-link` class with orange underline |
| 2 | Navigate to `about.html` | "Who We Are" link has `active-link` class |
| 3 | Navigate to `projects.html` | "Projects" link has `active-link` class |
| 4 | Navigate to `services.html` | "Services" link has `active-link` class |
| 5 | Navigate to `contact.html` | "Contact Us" link has `active-link` class |

#### TC-NAV-003: Navbar Scroll Behavior
| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Load page (scroll at top) | Navbar is transparent with gradient background |
| 2 | Scroll down past 50px | Navbar gains `.scrolled` class — white background, blur, box-shadow |
| 3 | Scroll back to top | Navbar returns to transparent state |
| 4 | Verify logo color transition | White when transparent → Dark Blue when scrolled |
| 5 | Verify nav link color transition | White when transparent → Dark Blue when scrolled |

#### TC-NAV-004: Mobile Menu Toggle
| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Set viewport to ≤1024px | Hamburger menu icon (`.menu-toggle`) is visible |
| 2 | Verify nav links are hidden | `.nav-links` has `display: none` |
| 3 | Tap hamburger icon | Nav links appear in vertical column |
| 4 | Tap any nav link | Menu closes and page navigates |
| 5 | Tap hamburger icon again | Menu closes |

#### TC-NAV-005: Footer Link Verification
| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Click each "Quick Links" footer link | Navigates to correct page |
| 2 | Click each "Services" footer link | Navigates to `services.html` |
| 3 | Verify footer contact details match | Address: B.K Enclave, Panbazar, Guwahati-781001 |
| 4 | Verify phone number | +91-3614081063 |
| 5 | Verify email | pspl@purbanchalenterprise.com |
| 6 | Verify copyright text | © 2026 Purbanchal Synergies Pvt. Ltd. |

---

### 4.2 Home Page (`index.html`)

#### TC-HOME-001: Hero Banner Swiper
| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Page loads | First slide visible with zoom-out animation on background image |
| 2 | Wait 6 seconds | Auto-advances to next slide with fade crossfade |
| 3 | Verify progress bar | Progress bar fills to 100% over 6 seconds, resets on slide change |
| 4 | Click next arrow | Advances to next slide |
| 5 | Click prev arrow | Returns to previous slide |
| 6 | Verify loop behavior | After last slide, loops back to first |
| 7 | Verify slide text animation | Title, paragraph, and CTA animate in with translateY on active slide |
| 8 | Click "Learn About PSPL" CTA | Navigates to `about.html` |
| 9 | Click "Explore Services" CTA | Navigates to `services.html` |
| 10 | Click "View Projects" CTA | Navigates to `projects.html` |

#### TC-HOME-002: Company Stats Section
| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Scroll to stats section | Section becomes visible with scroll animation |
| 2 | Verify stat values display | 20+ Years, 70 Cr+ Turnover, 5,00,000+ Meters, 10,00,000+ Pipeline |
| 3 | Verify counter animation | Numbers count up from 0 with Indian number formatting |
| 4 | Hover over stat card | Card elevates with `translateY(-10px)` and background change |

#### TC-HOME-003: Growth / About Split Section
| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Scroll into view | Section fades in via `animate-on-scroll` |
| 2 | Verify MD photo loads | `logo/Ravi_Sir.jpeg` loads correctly, covers full height |
| 3 | Verify blockquote text | Contains "leading", "20 years of experience", "Smart Grid" in bold |
| 4 | Click "Read Full Story" button | Navigates to `about.html` |

#### TC-HOME-004: Core Services Vertical Tabs
| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Verify default active tab | "Smart Metering & AMI" tab is active with orange border |
| 2 | Hover over "Power Distribution & Grid" tab | Tab activates, right panel swaps to power distribution image |
| 3 | Hover over "Solar EPC Solutions" tab | Tab activates, right panel shows solar content |
| 4 | Hover over "Civil & Water Infrastructure" tab | Tab activates, right panel shows JJM content |
| 5 | Verify active tab shows arrow icon | Right arrow icon animates in on active tab |
| 6 | Click service links in right panel | All links navigate to `services.html` |
| 7 | Click "Explore Service" CTA | Navigates to `services.html` (JJM tab → `services.html#jjm-work`) |

#### TC-HOME-005: Featured Projects Slider (3-Card)
| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Section loads | 3 project cards visible on desktop |
| 2 | Verify card images load | Malda, Smart Meter, Solar Working images render |
| 3 | Hover over card | Card elevates, image zooms in |
| 4 | Click card or text | Navigates to `projects.html` |
| 5 | Click "View All" button | Navigates to `projects.html` |
| 6 | Swipe on mobile | Cards slide horizontally |

#### TC-HOME-006: Sister Companies Section
| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Verify 4 cards visible | Rhino Moulders (active), Rhino Electricals, Sach The Reality, Shremad Industries |
| 2 | Hover over "Rhino Electricals" | Card expands (`flex: 2`), info overlay slides up |
| 3 | Verify overlay content | Shows establishment year, description, CTA button |
| 4 | Click "Visit Store" (Rhino Electricals) | Opens `https://www.rhinoelectricals.com` in new tab |
| 5 | Click "View Channel" (Sach Reality) | Opens `https://sachthereality.com/` in new tab |
| 6 | Verify responsive stacking | Cards stack vertically at ≤1024px with visible overlay |

#### TC-HOME-007: Clients & Partners Logo Carousel
| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Verify continuous scroll animation | Logos scroll left infinitely |
| 2 | Verify client logos load | APDCL, AEGCL, Eastern Railway, MES, Indian Air Force |
| 3 | Verify partner logos load | Kimbal, Schneider, Esyasoft, Landis+Gyr, Jio, Airtel |
| 4 | Hover over carousel | Animation pauses |
| 5 | Verify grayscale filter | Logos are grayscale by default, full color on hover |
| 6 | Verify duplicate logos exist | For seamless infinite scroll |
| 7 | Verify gradient fade masks | Left and right edges have gradient fade overlay |

---

### 4.3 Who We Are Page (`about.html`)

#### TC-ABOUT-001: Hero Section
| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Page loads | Hero visible with background image + dark overlay |
| 2 | Verify heading text | "Driven by People. Powered by Innovation." |
| 3 | Verify subtitle | "Building the future of smart energy and electrical infrastructure" |
| 4 | Verify hero height | `60vh` minimum `500px` |

#### TC-ABOUT-002: Core Identity
| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Scroll to section | "Who We Are" heading visible, content centered |
| 2 | Verify text content | Mentions "Assam", "government utilities", "corporate clients" |

#### TC-ABOUT-003: Core Values Cards
| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Verify 4 value cards render | Excellence, Reliability, Transparency, Innovation |
| 2 | Verify each has background image and dark overlay | Images from Unsplash load correctly |
| 3 | Hover over card | Card lifts `translateY(-10px)`, orange bottom border appears |
| 4 | Verify icon scale | Icons scale up `1.1x` on hover |

#### TC-ABOUT-004: Team Directory Filter System
| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Default state | "All" filter button active, all 10 team cards visible |
| 2 | Click "Board of Directors" | Only 4 board member cards shown (Ravi, Amit, Manisha, Aditya) |
| 3 | Click "Project Management" | 4 project management cards shown (Sunil, Krishna, Arun, Surajit) |
| 4 | Click "HR & Accounts" | 2 cards shown (Niraj, Geerish) |
| 5 | Click "All" again | All 10 cards visible again |
| 6 | Verify card structure | Photo → Name → Designation |
| 7 | Verify all photos load | Each team member photo loads from `logo/` directory |
| 8 | Hover over team card | Card lifts, image zooms slightly, grayscale removed |

#### TC-ABOUT-005: Team Photo Slider
| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Slider animates continuously | Images scroll horizontally via CSS animation |
| 2 | Hover over slider | Animation pauses |
| 3 | Hover over individual box | Box scales to `1.15x`, orange border appears, z-index increases |
| 4 | Verify team images load | 7 team work photographs render correctly |

#### TC-ABOUT-006: Trust Indicators
| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Verify 3 trust items | "20+ Years Experience", "ISO Certified", "Trusted by Government Utilities" |
| 2 | Each has icon in circle | Orange icon inside light background circle |

#### TC-ABOUT-007: Vision Section
| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Section has dark blue background | `var(--primary-color)` background |
| 2 | Verify quote text | "To build smarter, sustainable, and future-ready energy infrastructure." |
| 3 | Keywords in orange | "smarter", "sustainable", "future-ready" highlighted in orange |

---

### 4.4 Projects Page (`projects.html`)

#### TC-PROJ-001: Hero Section
| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Page loads | Animated grid background visible with perspective transform |
| 2 | Verify heading | "Powering Infrastructure Across Assam" with gradient text |
| 3 | Click "Explore Deployments" button | Smooth scrolls to `#grid` section |

#### TC-PROJ-002: Stats Banner
| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Stats display on glass panel | 32+ Projects, ₹498+ CR Value, ₹70 Cr+ Turnover, 34+ Districts |
| 2 | Hover over stat box | Lifts with neon glow shadow |

#### TC-PROJ-003: Search & Filter
| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Type "Metering" in search | Only projects with "Metering" in title/location shown |
| 2 | Type "Jorhat" in search | Only projects from Jorhat displayed |
| 3 | Select "Ongoing" status filter | Only ongoing projects shown |
| 4 | Select "Completed" status filter | Only completed projects shown |
| 5 | Select "Smart Metering" category | Only Smart Metering projects shown |
| 6 | Combine search + filter | Results match both criteria |
| 7 | Clear all filters | All 24 projects displayed again |
| 8 | Search with no results | "No projects found matching the criteria" message displayed |

#### TC-PROJ-004: Project Cards
| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Verify 24 project cards render | All `projectsData` entries rendered |
| 2 | Cards sorted by value (high→low) | AMI Smart Metering (₹113.90 Cr) first |
| 3 | Verify card structure | Status badge, title, category icon, location, value, progress bar |
| 4 | Status badges correct | Green "Completed" or Orange "Ongoing" |
| 5 | Hover over card | Lifts, scales, neon glow shadow, shimmer sweep animation |
| 6 | Progress bar animates | Bars fill to target width on render |

#### TC-PROJ-005: Project Modal
| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Click any project card | Modal overlay opens with backdrop blur |
| 2 | Modal populates with project data | Title, description, client, value, LOA, completion date |
| 3 | Status badge matches card | Same style (ongoing/completed) |
| 4 | Click ✕ close button | Modal closes |
| 5 | Click modal overlay (outside content) | Modal closes |
| 6 | Close button rotates 90° on hover | Visual feedback confirmed |

#### TC-PROJ-006: Data Analytics Charts
| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Verify doughnut chart | Shows Ongoing vs Completed counts with correct data |
| 2 | Verify bar chart | Shows portfolio value grouped by category, sorted descending |
| 3 | Charts are responsive | Resize with container, `maintainAspectRatio: false` |
| 4 | Hover over chart segments | Tooltips appear with data values |

#### TC-PROJ-007: Growth Trajectory Timeline
| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Verify 4 timeline items | 2015, 2019, 2022, 2025 |
| 2 | Scroll into view | Items animate in from left (`translateX(-50px)` → `0`) |
| 3 | Verify neon line on left | Gradient orange-to-transparent vertical line |
| 4 | Each item has glowing node | Circular node with orange border and glow |

#### TC-PROJ-008: Active Deployments (Coverage Section)
| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Dark background section renders | `#020617` background with radial glow |
| 2 | Hub pill (Guwahati) | Green style with pulsing icon animation |
| 3 | Assam location pills | Cyan styled with breathing icon animation |
| 4 | Interstate pills | Purple styled (Malda, Bhagalpur, Sahibganj) |
| 5 | Hover over pill | Background fills, glow shadow, lifts `translateY(-3px)` |

#### TC-PROJ-009: Credibility Section
| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Verify 3 items | "Trusted by APDCL", "UDAY Scheme Alignment", "DDUGJY/IPDS Executions" |
| 2 | Each has orange icon | FontAwesome icons in accent color |

#### TC-PROJ-010: CTA Section
| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Heading visible | "Build the Future Grid with Us" |
| 2 | Click "Initiate Protocol" button | Navigates to `contact.html` |
| 3 | Button hover effect | Fills with orange, text color inverts, glow shadow |

---

### 4.5 Services Page (`services.html`)

#### TC-SVC-001: Hero Header
| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Page loads | "Our Expertise" heading with dark overlay on grid link image |
| 2 | Subtext renders | Describes sustainable infrastructure and energy solutions |

#### TC-SVC-002: Service Blocks (Alternating Layout)
| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Smart Metering block | Image left, text right; 3 checkmarks; "5,00,000+" stat |
| 2 | Power Distribution block | Image RIGHT (reversed), text left; 3 checkmarks |
| 3 | Solar EPC block | Image left, text right; "6000+" stat |
| 4 | Click "View Grid Projects" | Navigates to `projects.html` |
| 5 | All images load correctly | Local and Unsplash images render |


#### TC-SVC-003: JJM Section
| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Section has `id="jjm-work"` | Accessible via `services.html#jjm-work` |
| 2 | Verify 3 JJM cards | Pipeline & Distribution, Water Reservoirs, Treatment Plants |
| 3 | Each card has image, title, description | Images load from `Logo/` directory |
| 4 | Grid collapses on mobile | 1 column on ≤768px |

#### TC-SVC-004: Logistics Section
| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Layout is reversed | Image right, text left |
| 2 | Click "Inquire for Supply" | Navigates to `contact.html` |

---

### 4.6 Contact Page (`contact.html`)

#### TC-CONTACT-001: Page Header
| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | "Contact Us" heading visible | White text on dark gradient with background image |
| 2 | Subtext renders | Mentions "inquiries, collaborations, and project consultations" |

#### TC-CONTACT-002: Contact Information Card
| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Verify corporate office | B.K Enclave, Panbazar, Guwahati-781001, Assam, India |
| 2 | Verify phone | +91-3614081063 |
| 3 | Verify email link | `mailto:pspl@purbanchalenterprise.com` |
| 4 | Hover over icon | Icon fills orange, scales up, rotates 5deg |
| 5 | Card hover effect | Card lifts with shadow change |

#### TC-CONTACT-003: Contact Form
| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Verify form fields | First Name, Last Name, Email, Phone, Subject, Message |
| 2 | First Name/Last Name required | Form does not submit without them |
| 3 | Email validation | Requires valid email format |
| 4 | Phone field is optional | Form submits without phone |
| 5 | Subject field is required | Shows validation message |
| 6 | Message textarea is required | Must have content |
| 7 | Focus on input field | Orange border `var(--accent-color)` + orange glow shadow |
| 8 | Click "Send Message" with valid data | Form submits (note: no backend endpoint currently) |
| 9 | Verify form layout | 2-column grid rows for name/email pairs, single for subject/message |

#### TC-CONTACT-004: Google Maps Embed
| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Map iframe loads | Shows Pan Bazar, Guwahati area |
| 2 | Map is interactive | Can zoom, pan, view full screen |
| 3 | Hover over map container | Map scales slightly (`1.02x`) |
| 4 | Container has rounded borders | `20px` radius with white border |

---

## 5. Responsive Design Test Matrix

### 5.1 Breakpoints

| Breakpoint | Width | Targets |
|------------|-------|---------|
| Mobile S | 320px | Small phones |
| Mobile M | 375px | iPhone SE / Standard Android |
| Mobile L | 425px | Large phones |
| Tablet | 768px | iPad / Tablets |
| Laptop | 1024px | Small laptops (hamburger menu threshold) |
| Desktop | 1440px | Standard desktop |
| Wide | 2560px | Ultra-wide / 4K |

### 5.2 Critical Responsive Behaviors

| Component | ≤768px | 769px–1024px | ≥1025px |
|-----------|--------|--------------|---------|
| **Navbar** | Hamburger menu, links hidden | Hamburger menu, links hidden | Full nav visible |
| **Hero text** | `font-size: 2.5rem` | Standard | `font-size: 4.5rem` |
| **Growth wrapper** | Stacked vertically | Stacked vertically | Side-by-side |
| **Core Services tabs** | Stacked vertically | Stacked vertically | Side-by-side |
| **Sister Companies** | Stacked, `height: 300px`, overlays always visible | Stacked | Horizontal flex row |
| **Footer grid** | Single column | Standard | 4-column grid |
| **Contact form** | Single column inputs | Standard | 2-column rows |
| **JJM gallery** | Single column | 3-column grid | 3-column grid |
| **Team cards (About)** | Single column | 2 columns | Auto-fill grid |

---

## 6. Visual & Brand Consistency Tests

#### TC-VIS-001: Typography
| Check | Expected |
|-------|----------|
| Headings (h1–h6) | `font-family: 'Poppins'`, `font-weight: 700`, `color: #051424` |
| Body text | `font-family: 'Inter'`, `color: #1e293b` |
| Muted text | `color: #64748b` |
| Projects page headings | Use `Poppins` (Orbitron removed in favor of consistency) |

#### TC-VIS-002: Color Palette
| Token | Value | Usage |
|-------|-------|-------|
| Primary Color | `#051424` | Headings, navbar scrolled, footer background |
| Accent Color | `#FF6600` | CTAs, highlights, progress bars, borders |
| Background Main | `#f8fafc` | Odd sections |
| Background White | `#ffffff` | Even sections |

#### TC-VIS-003: Gradient Buttons
| Check | Expected |
|-------|----------|
| Background | `linear-gradient(90deg, #FF6600, #ff8c3a)` |
| Border radius | `50px` (pill shape) |
| Hover effect | `translateY(-3px)` + enhanced box shadow |
| Text color | White (`#fff`) |

#### TC-VIS-004: Scroll Animations
| Check | Expected |
|-------|----------|
| Initial state | `opacity: 0; transform: translateY(30px)` |
| Visible state | `opacity: 1; transform: translateY(0)` |
| Trigger | Intersection Observer at `threshold: 0.1` |

---

## 7. Cross-Browser Compatibility

| Browser | Version | Status |
|---------|---------|--------|
| Google Chrome | Latest 2 versions | 🔴 Must Pass |
| Mozilla Firefox | Latest 2 versions | 🔴 Must Pass |
| Microsoft Edge | Latest 2 versions | 🔴 Must Pass |
| Apple Safari | Latest 2 versions | 🟠 Should Pass |
| Samsung Internet | Latest | 🟡 Nice to Have |

### Key Areas for Cross-Browser Testing

| Feature | Risk Area |
|---------|-----------|
| `backdrop-filter: blur()` | Safari / older browsers |
| CSS Grid with `auto-fit` / `auto-fill` | IE 11 (excluded) |
| `object-fit: cover` on images | Universally supported |
| CSS Custom Properties (`var()`) | IE 11 (excluded) |
| `IntersectionObserver` | Older Safari |
| Swiper.js fade effect | Browser rendering differences |
| Chart.js canvas rendering | High DPI screens |

---

## 8. Performance Test Criteria

| Metric | Target | Tool |
|--------|--------|------|
| **Largest Contentful Paint (LCP)** | < 2.5s | Lighthouse |
| **First Input Delay (FID)** | < 100ms | Lighthouse |
| **Cumulative Layout Shift (CLS)** | < 0.1 | Lighthouse |
| **Total Blocking Time (TBT)** | < 300ms | Lighthouse |
| **Page Weight** | < 5MB per page | DevTools Network |
| **Image Optimization** | All images < 300KB each | Manual audit |
| **Font Loading** | FOUT/FOIT resolved within 1s | Visual check |

### Performance Risks to Monitor

| Risk | Affected Page | Mitigation |
|------|---------------|------------|
| Large hero images | `index.html` | Optimize, lazy-load below-fold |
| Unsplash external images | `index.html`, `services.html` | Consider caching or local copies |
| Chart.js bundle | `projects.html` | Only loaded on projects page ✅ |
| Multiple font families | All | `display=swap` already used ✅ |
| Duplicate logos for carousel | `index.html` | Expected behavior for infinite scroll |

---

## 9. Accessibility Testing (WCAG 2.1 Level A)

| Check | Category | Expected |
|-------|----------|----------|
| **Alt text on images** | Perceivable | All `<img>` tags have descriptive `alt` attributes |
| **Color contrast** | Perceivable | White text on `#051424` meets 4.5:1 ratio ✅ |
| **Keyboard navigation** | Operable | Tab through nav, form, buttons without mouse |
| **Focus indicators** | Operable | Visible focus ring on all interactive elements |
| **Form labels** | Perceivable | Inputs have `placeholder` (note: explicit `<label>` missing — flag) |
| **Heading hierarchy** | Perceivable | Single `<h1>` per page, logical `h2`→`h3` flow |
| **Skip navigation link** | Operable | Not present — flag as improvement |
| **Language attribute** | Perceivable | `<html lang="en">` present ✅ |
| **ARIA labels** | Perceivable | Swiper nav buttons may need `aria-label` — flag |

### Known Accessibility Issues

> [!WARNING]
> 1. **No `<label>` elements on contact form** — Inputs use `placeholder` only. Screen readers cannot properly identify fields.
> 2. **No skip-to-content link** — Keyboard users must tab through entire nav on every page.
> 3. **Sister company cards lack role** — Expandable cards may need `role="button"` or similar.
> 4. **Project modal lacks focus trap** — When modal opens, focus is not trapped inside.

---

## 10. SEO & Meta Tag Validation

| Page | Title | Expected |
|------|-------|----------|
| `index.html` | `Purbanchal Synergies Pvt. Ltd. \| Infrastructure & Energy` | ✅ Descriptive |
| `about.html` | `Who We Are \| Purbanchal Synergies Pvt. Ltd.` | ✅ |
| `projects.html` | `Projects \| Futuristic Grid Infra` | ⚠️ Missing company name |
| `services.html` | `Services \| Purbanchal Synergies Pvt. Ltd.` | ✅ |
| `contact.html` | `Contact Us \| Purbanchal Synergies Pvt. Ltd.` | ✅ |

### SEO Checks

| Check | Status |
|-------|--------|
| `<meta name="description">` present | ❌ Missing on all pages |
| `<meta name="viewport">` present | ✅ All pages |
| Single `<h1>` per page | ✅ All pages |
| Open Graph tags | ❌ Not implemented |
| Canonical URL | ❌ Not implemented |
| Favicon | ❌ Not implemented |

---

## 11. Image & Asset Audit

### 11.1 Local Assets to Verify

| Image | Used On | Path |
|-------|---------|------|
| PSPL Logo | All pages | `logo/pspl logo.png` |
| Ravi Sir | `index.html`, `about.html` | `logo/Ravi_Sir.jpeg` |
| Smart Meter Installation | `index.html`, `services.html` | `Logo/smart_meter_installation.jpeg` |
| Urbanization | `index.html` | `Logo/urbanization.jpeg` |
| Grid Link | `index.html`, `services.html` | `Logo/grid_link.jpeg` |
| Malda | `index.html` | `Logo/malda.jpeg` |
| Solar Working | `index.html` | `Logo/solar_working.jpeg` |
| JJM Photos (3) | `services.html` | `Logo/jjm work 1-3.jpeg`, `Logo/jjm.jpeg` |
| Team Photos (10) | `about.html` | Various in `logo/` |
| Team Work Photos (7) | `about.html` | `Logo/men_working_*.jpeg` |
| Sister Company Logos (4) | `index.html` | `logo/Rhino_moulders.jpeg`, etc. |
| Client Logos (5) | `index.html` | APDCL, AEGCL, Eastern Railway, MES, IAF |
| Partner Logos (6) | `index.html` | Kimbal, Schneider, Esyasoft, Landis+Gyr, Jio, Airtel |

### 11.2 External Assets to Verify

| Source | Images | Risk |
|--------|--------|------|
| Unsplash | Solar panels, power lines, office photos, logistics | May fail if Unsplash is down or URL changes |

> [!IMPORTANT]
> **Case Sensitivity Warning:** The project uses inconsistent casing for the image directory (`Logo/` vs `logo/`). This works on Windows but **will break on Linux/macOS hosting** (case-sensitive filesystems). All image paths should be audited and normalized.

---

## 12. JavaScript Functional Tests

#### TC-JS-001: Swiper Initialization
| Check | Expected |
|-------|----------|
| Hero slider initializes | Only if Swiper library loaded AND `.HeroSlider` exists |
| 3-card slider initializes | Only if Swiper loaded AND `.three-imgSlideWrapper` exists |
| No JS errors on pages without Swiper | `about.html`, `contact.html` load cleanly |

#### TC-JS-002: IntersectionObserver
| Check | Expected |
|-------|----------|
| `.animate-on-scroll` elements | Start invisible, gain `.visible` class at `threshold: 0.1` |
| `.scroll-anim` elements (projects) | Separate observer for timeline items |

#### TC-JS-003: Counter Animation
| Check | Expected |
|-------|----------|
| Triggers once | Counter runs only first time stats section is intersected |
| Indian number formatting | Uses `toLocaleString('en-IN')` — e.g., `5,00,000` |
| Suffix handling | "+" and "Cr" suffixes appended correctly |

#### TC-JS-004: Projects Page Dynamic Rendering
| Check | Expected |
|-------|----------|
| `projectsData` defines 24 projects | Rendered from JavaScript array |
| Sort order | Highest value first |
| Filter combination | Search + status + category work together |
| Category dropdown | Dynamically populated from unique categories |
| Empty state | "No projects found" displayed when no matches |

---

## 13. Edge Cases & Error Handling

| Scenario | Expected Behavior |
|----------|-------------------|
| JavaScript disabled | Navbar, hero images still visible (no animations) |
| CDN failure (FontAwesome) | Icons missing but layout intact |
| CDN failure (Swiper) | Hero shows static first slide image |
| CDN failure (Chart.js) | Charts section shows blank canvas |
| Slow network (3G) | Images lazy-load, text readable first |
| Very long project title | Card layout doesn't break |
| Window resize during interaction | Layout recalculates without errors |
| Double-click on filter button | No duplicate renders |
| Rapid tab switching (Core Services) | No flickering or overlapping panels |
| External link target="_blank" | Opens in new tab, existing page preserved |

---

## 14. Test Execution Plan

### Phase 1: Smoke Testing (Day 1)
- [ ] All 5 pages load without console errors
- [ ] All navigation links work
- [ ] All images load (no broken images)
- [ ] Mobile hamburger menu works

### Phase 2: Functional Testing (Days 2–3)
- [ ] Execute all TC-HOME tests
- [ ] Execute all TC-ABOUT tests
- [ ] Execute all TC-PROJ tests
- [ ] Execute all TC-SVC tests
- [ ] Execute all TC-CONTACT tests

### Phase 3: Cross-Browser Testing (Day 4)
- [ ] Chrome, Firefox, Edge, Safari
- [ ] Desktop and mobile viewports

### Phase 4: Visual & Responsive Testing (Day 5)
- [ ] All 7 breakpoints verified
- [ ] Screenshot comparison across browsers
- [ ] Animation smoothness validated

### Phase 5: Performance & Accessibility (Day 6)
- [ ] Lighthouse audit (all 5 pages)
- [ ] Accessibility audit (axe DevTools)
- [ ] Performance bottleneck identification

---

## 15. Defect Severity Classification

| Severity | Definition | Example |
|----------|------------|---------|
| 🔴 **P0 — Blocker** | Feature completely broken, no workaround | Navigation link 404, page won't load |
| 🟠 **P1 — Critical** | Major feature broken, affects user flow | Contact form doesn't submit, modal won't close |
| 🟡 **P2 — Major** | Feature partially broken, workaround exists | Filter doesn't reset, animation choppy |
| 🟢 **P3 — Minor** | Cosmetic issue, doesn't affect functionality | Alignment off by 2px, wrong shade of orange |
| ⚪ **P4 — Enhancement** | Improvement suggestion | Add meta descriptions, improve alt text |

---

## 16. Sign-Off Criteria

| Criteria | Threshold |
|----------|-----------|
| **P0 Defects** | 0 open |
| **P1 Defects** | 0 open |
| **P2 Defects** | ≤ 3 open with planned fix dates |
| **P3/P4 Defects** | Documented and tracked |
| **Lighthouse Performance Score** | ≥ 75 |
| **Lighthouse Accessibility Score** | ≥ 80 |
| **Cross-Browser Pass Rate** | 100% on Chrome, Firefox, Edge |

---

*End of Document*
