# MFB Brand Specification

## Colors

| Token | Hex | Usage |
|-------|-----|-------|
| purple-300 | #422C70 | Primary purple — brand hero color, backgrounds, headers |
| purple-400 | #2B1C58 | Accent dark purple — deep contrast, footer backgrounds |
| purple-200 | #5E378E | Accent light purple — secondary headings, gradient endpoint |
| orange-300 | #F7941F | Primary orange — CTAs, highlights, Bitcoin symbol color |
| orange-400 | #EF7B00 | Accent dark orange — hover/active states, strong emphasis |
| orange-200 | #FBB040 | Accent light orange — soft highlights, secondary accents |
| black | #000000 | Primary black — high-contrast text, bold headlines |
| white | #FFFFFF | Primary white — backgrounds, text on dark surfaces |
| gray-900 | #25252B | Neutral — near-black, body text on light backgrounds |
| gray-800 | #4F4F5D | Neutral — secondary text, subtle headings |
| gray-700 | #6C6C7D | Neutral — muted text, placeholders |
| gray-600 | #88889C | Neutral — disabled text, borders |
| gray-500 | #ADADBE | Neutral — subtle borders, dividers |
| gray-400 | #C0C0D0 | Neutral — light borders, inactive elements |
| gray-300 | #D8D8E7 | Neutral — card borders, separators |
| gray-200 | #EAEAF4 | Neutral — light backgrounds, alternating rows |
| gray-100 | #F3F3FA | Neutral — page background, subtle tint |

## Gradients

* **brand**: `linear-gradient(135deg, #2B1C58 0%, #5E378E 100%)` — Brand gradient (purple-400 → purple-200)

## Typography

| Role | Family | Weights |
|------|--------|---------|
| heading | IBM Plex Sans, Arial, sans-serif | Headings, titles, display text — Medium weight |
| body | IBM Plex Sans, Arial, sans-serif | Body text, paragraphs — Regular weight |
| mono | IBM Plex Mono, monospace | Code, data, technical content |

## Font Weights

* **regular**: 400 — Body text, labels
* **medium**: 500 — Headings H1-H6, quotes
* **semibold**: 600 — Strong emphasis, CTAs

## Font Sizes

| Level | Size | Notes |
|-------|------|-------|
| h1    | 70px | Heading 1 — IBM Plex Sans Medium, line-height: 1 |
| h2    | 58px | Heading 2 — IBM Plex Sans Medium, line-height: 1 |
| h3    | 48px | Heading 3 — IBM Plex Sans Medium, line-height: 1 |
| h4    | 40px | Heading 4 — IBM Plex Sans Medium, line-height: 1 |
| h5    | 36px | Heading 5 — IBM Plex Sans Medium, line-height: 1.1 |
| h6    | 32px | Heading 6 — IBM Plex Sans Medium, line-height: 1.1 |
| body  | 18px | Body text — IBM Plex Sans Regular, line-height: 1.2 |
| label | 22px | Labels — IBM Plex Sans Regular, line-height: 1.2 |
| quote | 40px | Block quotes — IBM Plex Sans Medium, line-height: 1 |

## CSS Variables

All colors available as `var(--mfb-<name>)` in brand.css. Font sizes available as `var(--mfb-size-<level>)` in brand.css.

## Usage Rules

### Color Application

* **Backgrounds:** Purple gradient or white — never other colors as full backgrounds
* **Accent:** Orange is for CTAs, links, highlights, and the ₿ symbol only — never as a background fill
* **Text on dark backgrounds:** Always white
* **Text on light backgrounds:** gray-900 (#25252B) — never pure black
* **Links:** Orange (#F7941F), with underline on hover
* **Gradient direction:** Always 135deg (top-left to bottom-right)

### Contrast Pairs

| Background | Text | Accent |
|------------|------|--------|
| Purple gradient | White | Orange for CTAs/highlights |
| White / gray-100 | gray-900 | Purple headings, orange CTAs |
| purple-300 | White | Orange accents |

### Typography Rules

* Use IBM Plex Sans for all general content. Use IBM Plex Mono for code, data, and technical content.
* Headings: Medium weight (500), line-height 1.0
* Body text: Regular weight (400), line-height 1.2
* Strong emphasis / CTAs: SemiBold (600)
* Never use more than 2 font weights in a single piece of content
* Heading sizes are for print/large-format — scale proportionally for screen

### Visual Elements

* **Purple gradient background** is the signature MFB look — use on hero sections, headers, slides
* **₿ symbol:** Always render in orange (#F7941F), use Unicode ₿ — never generic coin imagery
* **Logo:** Use official files only. Minimum clear space = height of the ₿ symbol
* Logo on dark/gradient backgrounds: white variant. On light backgrounds: dark variant.
* **Photography:** Real people in real educational settings, warm natural lighting, diverse representation

### Supergraphic Elements

* **Highlighter:** Orange underline mark on ONE key word per heading. CSS: `background-image: linear-gradient(transparent 60%, var(--mfb-orange-300) 60%)`. Apply on purple or white backgrounds. Only one per heading — never highlight full phrases.
* **Halftone portraits:** Duotone effect on portrait photos — purple (#45265B shadows, #F7E6FF highlights for cutouts) or orange background. Use for speaker/team sections. This is a photo editing effect (Recraft/image generation), not CSS.
* **Parallelogram shapes:** Skewed rectangular containers as decorative accents. CSS: `transform: skewX(-10deg)` with child content counter-skewed (`transform: skewX(10deg)`). Use sparingly as accent frames behind stat numbers or section labels.
