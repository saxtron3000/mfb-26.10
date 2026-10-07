# My First Bitcoin — Design System

**Handoff document 1 of 2** · Complete brand and design system reference
**Source:** `MyFirstBitcoinDesignSystem_b26ab8` (Claude Design system project `b26ab809-b968-4c9e-bbc6-ff90715695a2`)
**Transcribed:** 21 August 2026

> **How to use this document.** This is the design system as it exists — the brand's
> foundations, tokens, components and assets. It is the *style* authority: colour, type,
> voice, motif, components.
>
> It is **not** complete on its own. Five things in it are stale or missing, and they are
> flagged inline as `⚠ SEE DOC 2`. Document 2 (*MFB Assets — Style Guide*) carries the
> asset hierarchy, the icon set, the print pipeline constraints and the corrections.
>
> **Read both. Where they conflict, the conflicts are named explicitly in both documents.**

---

## Table of contents

1. [The organisation](#1-the-organisation)
2. [Voice and content](#2-voice-and-content)
3. [Colour](#3-colour)
4. [Typography](#4-typography)
5. [Spacing, radius, shadow, motion](#5-spacing-radius-shadow-motion)
6. [The slant — the signature motif](#6-the-slant--the-signature-motif)
7. [The highlighter](#7-the-highlighter)
8. [Backgrounds, cards, borders](#8-backgrounds-cards-borders)
9. [Layout](#9-layout)
10. [Logos and brand assets](#10-logos-and-brand-assets)
11. [Iconography](#11-iconography)
12. [Badges](#12-badges)
13. [Components](#13-components)
14. [Slide templates](#14-slide-templates)
15. [The micrographics publishing pipeline](#15-the-micrographics-publishing-pipeline)
16. [What is stale in this system](#16-what-is-stale-in-this-system)
17. [Provenance](#17-provenance)

---

## 1 · The organisation

**My First Bitcoin (MFB)** is a global, non-profit, open-source Bitcoin education movement.
It builds a decentralised network of local educators who teach the **Bitcoin Diploma** in their
own communities using free, open materials. It began in El Salvador and is expanding worldwide.

> **Mission:** Provide independent, unbiased Bitcoin education — as quickly as possible and
> with the greatest possible impact. *"Empower those who empower others."*

**The model matters to the design.** MFB scales by empowering local educators, not by growing a
central organisation. Materials are printed, photocopied, translated and taught from in rooms
that may have no projector. Every design decision that looks conservative — flat colour, no
gradients, hard geometry, greyscale-proof figures — traces back to that.

**Vocabulary.** *Educators* (local educators / communities), *Educator Network*, *Bitcoin
Diploma*, *Unconference*, *Bitcoin Educators*, *open-source*, *independent*, *non-profit*.

**Retired terminology — do not use.** "Node" and "Node Network" are no longer used for
communities. It is **Educator** / **Educator Network**. The Light Node / Full Node tiers are
replaced by a **single community badge**. All old badge artwork has been removed because the
retired lettering is baked into the images.

---

## 2 · Voice and content

**Voice.** Plain, confident, mission-driven. MFB speaks like an educator who respects the
reader: clear over clever, direct over salesy. No hype, no crypto jargon, no price talk. The
brand is *fiercely independent* and says so — it does not endorse products or take political
sides.

**Person.** Collective **"we"** for the organisation and its mission. **"You"** addresses the
learner or partner directly. Avoid "I".

**Casing.** Display headings use **Title Case**. Body copy uses **sentence case**.

**Headlines** are short, declarative statements, often provocative framings of a problem:

- *"Money Was Weaponized Against The People"*
- *"This Is Who We Work For"*
- *"Open Source Education"*

**Sentences** are short and concrete. Big ideas, few words.

**Numbers and stats.** Used sparingly but boldly — a single huge figure carries a slide. The
canonical example: **`$0`** government funding → *"No political or commercial influence."*
Let one number make one point. Do not pile on stats.

**Real brand copy, for tone calibration:**

- *"Open-Source Bitcoin Education for the world"* (tagline)
- *"MyFirstBitcoin is a global, open-source education movement, building a decentralized network of Bitcoin educators around the world."*
- *"We scale not by growing a large central organization, but by empowering local educators who teach in their own communities using open-source materials."*
- *"We are a non-profit organization and remain fiercely independent."*
- *"Empower those who empower others."*

**Emoji.** Essentially not part of the formal brand system. A 💜 appears only in casual social
captions. **Default to no emoji** in product, slides, print and marketing surfaces.

**The vibe:** grassroots but polished. Idealistic, anti-establishment in substance, but visually
disciplined and corporate-clean. Educational, global, human.

---

## 3 · Colour

**Purple is the hero. Orange is a supporting accent only.**

### Purple — primary

| Token | Hex | Use |
|---|---|---|
| `--purple-400` | `#2B1C58` | Deep contrast, footer backgrounds |
| `--purple-300` | `#422C70` | **PRIMARY** — brand hero, backgrounds, headers |
| `--purple-200` | `#5E378E` | Secondary headings, accents |

### Orange — supporting accent

| Token | Hex | Use |
|---|---|---|
| `--orange-400` | `#EF7B00` | Hover / active, strong emphasis |
| `--orange-300` | `#F7941F` | **PRIMARY accent** — CTAs, highlighter, Bitcoin symbol |
| `--orange-200` | `#FBB040` | Soft highlights, secondary accents |

> **Orange is never used as a large background or surface fill.** Backgrounds are purple,
> white, paper or neutral gray. This is a hard rule, not a preference.

### Base and neutrals

| Token | Hex |
|---|---|
| `--black` | `#000000` |
| `--white` | `#FFFFFF` |
| `--paper` | `#F6F6F8` |

The gray ramp is **cool — every step is slightly blue.** This is deliberate; a neutral or warm
gray reads wrong against the purple.

| Token | Hex |
|---|---|
| `--gray-100` | `#F3F3FA` |
| `--gray-200` | `#EAEAF4` |
| `--gray-300` | `#D8D8E7` |
| `--gray-400` | `#C0C0D0` |
| `--gray-500` | `#ADADBE` |
| `--gray-600` | `#88889C` |
| `--gray-700` | `#6C6C7D` |
| `--gray-800` | `#4F4F5D` |

### Semantic aliases — prefer these in components and layouts

```css
/* Brand */
--brand:            var(--purple-300);
--brand-deep:       var(--purple-400);
--brand-soft:       var(--purple-200);
--accent:           var(--orange-300);   /* accent ONLY — never a large background fill */
--accent-strong:    var(--orange-400);
--accent-soft:      var(--orange-200);

/* Surfaces */
--surface-page:        var(--paper);
--surface-card:        var(--white);
--surface-brand:       var(--purple-300);
--surface-brand-deep:  var(--purple-400);
--surface-accent:      var(--orange-300);
--surface-muted:       var(--gray-100);

/* Text */
--text-strong:          var(--black);              /* ⚠ SEE DOC 2 — three competing blacks */
--text-body:            var(--gray-700);           /* #6C6C7D — body copy on light */
--text-muted:           var(--gray-600);
--text-on-brand:        var(--white);
--text-on-brand-muted:  rgba(246, 246, 248, 0.75); /* body copy on purple */
--text-on-accent:       var(--black);

/* Lines & borders */
--border:           var(--gray-300);
--border-strong:    var(--gray-400);
--border-on-brand:  rgba(255, 255, 255, 0.18);

/* Focus ring */
--focus-ring:       var(--orange-300);
```

### The two-colour rule

**Two brand background colours maximum per piece** — typically purple plus white or paper.
A third brand background is the fastest way to make MFB work look unbranded.

---

## 4 · Typography

**IBM Plex Sans only.** It is the sole brand typeface. No secondary family, no display face,
no mono for brand surfaces.

### Weights — never more than two in one piece

| Weight | Token | Use |
|---|---|---|
| 400 Regular | `--weight-regular` | Body copy |
| 500 Medium | `--weight-medium` | All headings, display type, big numerals |
| 600 SemiBold | `--weight-semibold` | CTAs, strong emphasis, eyebrows |

### The setting is the look

Headings are **Medium 500 at line-height 1.0 with tight negative tracking**
(`-0.03em` to `-0.04em` at display sizes). This tight, confident setting is core to the brand.
Loosening it makes the work look like a different organisation.

```css
--leading-display: 1;      /* huge display + headings */
--leading-heading: 1.1;    /* smaller headings */
--leading-body: 1.2;       /* body copy */
--leading-prose: 1.25;     /* long-form paragraphs */

--tracking-display: -0.04em;
--tracking-heading: -0.03em;
--tracking-snug:    -0.02em;
--tracking-normal:  0;
```

### Type scale — from the Brand Book specimen

| Token | Size | Role |
|---|---|---|
| `--text-display` | 147px | Cover / hero display |
| `--text-h1` | 70px | |
| `--text-h2` | 58px | |
| `--text-h3` | 48px | |
| `--text-h4` | 40px | |
| `--text-h5` | 36px | |
| `--text-h6` | 32px | |
| `--text-section` | 46px | Section title, used across the Brand Book |
| `--text-lead` | 29px | Large intro paragraph |
| `--text-body-lg` | 24px | |
| `--text-base` | 22px | Default body across the brand |
| `--text-sm` | 18px | |
| `--text-xs` | 13px | |

> **⚠ SEE DOC 2 §8.** This is a print specimen scale. The asset stack's screen and deck work
> uses a denser scale and adds an eyebrow style with no token here. Both are legitimate; the
> reconciliation is documented in Document 2.

**Display type is enormous.** Cover headings run ~147px; section dividers go up to 200px.
That scale is intentional confidence, not an error.

### Fonts are loaded from CDN

Genuine IBM Plex Sans from the Fontsource CDN via jsDelivr, weights 400 / 500 / 600, latin
subset, `font-display: swap`:

```
https://cdn.jsdelivr.net/fontsource/fonts/ibm-plex-sans@latest/latin-{400,500,600}-normal.woff2
```

For fully offline use, self-host the woff2 files and update `tokens/fonts.css`.

---

## 5 · Spacing, radius, shadow, motion

### Spacing — 4px base

```css
--space-1:  4px;    --space-2:  8px;    --space-3:  12px;
--space-4:  16px;   --space-5:  20px;   --space-6:  24px;
--space-8:  32px;   --space-10: 40px;   --space-12: 48px;
--space-16: 64px;   --space-20: 80px;

--margin-page:  40px;   /* Brand Book page margin */
--margin-slide: 60px;   /* slide margin */
```

### Radius

```css
--radius-sm:   6px;
--radius-md:  10px;
--radius-lg:  12px;   /* the standard brand card / surface radius */
--radius-xl:  20px;
--radius-pill: 999px;
```

`--radius-lg: 12px` is the one to reach for. **Note:** this governs *surfaces*. Glyph geometry
is hard-cornered — see Document 2.

### Border widths

```css
--border-width:        1px;
--border-width-strong: 2px;
```

### Shadows — the brand is flat

```css
--shadow-sm: 0 1px 2px   rgba(43, 28, 88, 0.06);
--shadow-md: 0 6px 20px  rgba(43, 28, 88, 0.10);
--shadow-lg: 0 18px 48px rgba(43, 28, 88, 0.16);
```

All purple-tinted, all restrained. **Avoid heavy drop shadows.** Reach for a border or a
surface change before elevation.

### Motion — restrained and purposeful

```css
--ease-standard: cubic-bezier(0.2, 0, 0, 1);
--ease-out:      cubic-bezier(0.16, 1, 0.3, 1);
--duration-fast: 120ms;
--duration-base: 200ms;
--duration-slow: 320ms;
```

Fades and short slides. **No bounces, no infinite decorative loops.**

- **Hover:** shift to the darker step (`--orange-400`, `--purple-400`) or a subtle lift
- **Press:** slightly darker plus a touch of scale-down (~0.98)
- **Focus:** an orange ring (`--focus-ring`)

---

## 6 · The slant — the signature motif

**A leaning parallelogram is *the* brand element.**

```css
--skew-angle: -19deg;
```

> **⚠ SEE DOC 2 §5 — THIS VALUE IS DISPUTED.**
> The design system states 19° in four places. The shipped logo artwork measures **13°**, and
> the entire MFB Assets stack is cut to 13°. This is unresolved pending the November discovery
> call. Do not assume either value silently — read Document 2 before drawing anything that leans.

### Where the slant appears

- **Parallelogram frames** — skewed image and content windows. Can be layered for depth. Best
  framing a single subject: a speaker, a landmark, the Bitcoin Diploma book.
- **The highlighter** — see §7. This is its most important and most abused appearance.
- **Spotlights and books** — angled cut shapes and the tilted Bitcoin Diploma book.
- **Halftones** — dotted and screened texture treatments.

### The rules of the slant

1. **All slanted shapes share the same lean.** Never two slant angles in one composition.
2. **Shapes stay inside their frame.** Don't let them wander.
3. **Never rotate arbitrarily** — this is a skew on a fixed angle, not free rotation.
4. **Content inside a frame counter-skews** so it stays upright. Faces must not lean.

---

## 7 · The highlighter

**This is the brand's only bar.** It deserves its own section because it is the single most
misused element in the system.

A slightly-tilted orange bar that sits **under** a word in a heading, spanning the full width
of the wrapped text, **below the glyphs and never over them**.

### Canonical geometry

```css
position: absolute;
left: 0;
right: 0;
bottom: -0.12em;
height: 0.14em;
background: var(--accent);
transform: skewY(-1.4deg);
transform-origin: left center;
z-index: 0;
```

**Em-relative, so it scales with the type.** Hard-coding pixels here is the most common way it
breaks.

### The rules

1. **It always underlines a word.** It is never placed above or beside text as a decorative rule.
2. **One word per heading**, at most. Two highlighted words in one heading emphasises nothing.
3. **Never restyled.** Not a different colour, not a different height, not a different tilt.
4. **Nothing else is a bar.** No underline under a nav item, no bar under an icon, no
   decorative rule that could be mistaken for it. Anything bar-like near it competes with it.

> Rule 4 has a direct consequence for interface work: **the active state of a UI element is a
> colour change, never a bar.** See Document 2 §Active state.

### Note the tilt is not the slant

The highlighter tilts **1.4°** (`skewY`). The parallelogram slant is 13°/19° (`skewX`). These
are different values for different purposes. Do not collapse them.

---

## 8 · Backgrounds, cards, borders

**Backgrounds are mostly flat solid colour** — full-bleed purple, orange, white or paper.

- **No gradients.** Anywhere.
- **No noise.**
- Photography appears inside **parallelogram frames** or as full-bleed images with a clean
  diagonal cut.
- Imagery skews **warm and human** — people, classrooms, events. Not abstract, not stock-crypto.

**Cards** use `--radius-lg` (12px) and are typically **flat** — solid fill or white, with no
border or a hairline `--border`.

**Avoid:**
- Heavy drop shadows
- The "rounded card with a coloured left-border accent" cliché
- Glassmorphism and heavy blur

**Borders** are hairline 1px cool-gray on light surfaces, and subtle white-alpha
(`--border-on-brand`) on purple. Strong emphasis uses 2px.

**Transparency** is used lightly. Body copy on purple sits at ~75% white
(`--text-on-brand-muted`). That is the main legitimate use.

---

## 9 · Layout

- **Generous margins** — 40px on a Brand Book page, 60px on a slide.
- **Strong left alignment.**
- **Big type anchored top-left**, supporting content lower or to the right.
- **Confident negative space** — let surfaces breathe. Under-filling a layout is on-brand
  over-filling is not.

---

## 10 · Logos and brand assets

**Never redraw the logo.** Use the real SVG files. Never hand-roll brand artwork as inline SVG
paths.

### Available files (`assets/logos/`)

| File | What |
|---|---|
| `mfb_logo_purple.svg` | Full wordmark, purple |
| `mfb_logo_white.svg` | Full wordmark, white |
| `mfb_logo_black.svg` | Full wordmark, black |
| `mfb_logo_tagline_purple.svg` | Wordmark with tagline, purple |
| `mfb_logo_tagline_white.svg` | Wordmark with tagline, white |
| `mfb_logo_cobranding_purple.svg` | Co-branding lockup |
| `mfb_icon_purple.svg` / `.png` | Standalone "B" Bitcoin-tag icon, purple |
| `mfb_icon_white.svg` / `.png` | B-tag icon, white |
| `mfb_icon_black.svg` | B-tag icon, black |

### Profile pictures (`assets/profile/`)

Pre-made square avatars for social platforms: `purple.png`, `deep_purple.png`, `orange.png`.

---

## 11 · Iconography

> **⚠ SEE DOC 2 §6 — THIS SECTION IS OBSOLETE.**
>
> **What this design system currently says:** the brand has no bespoke UI icon set, so use
> [Lucide](https://lucide.dev) from CDN at stroke width ~2, coloured from the palette.
>
> **What is now true:** a first-party set of **153 icons** exists, specified, cut and committed.
> Document 2 carries the full specification. **Do not use Lucide.** Using both sets side by side
> is exactly the drift the icon project was run to eliminate.

What remains true in this section:

- **The brand ships its own logo and B-tag icon as SVG** — use the real files, never redraw.
- **Emoji / unicode as icons:** avoid in product and formal materials.
- **Never hand-roll brand artwork as inline SVG paths** — copy the real asset.

---

## 12 · Badges

**No final badge artwork exists.**

- The old "Node Network — Full Node / Light Node" and "Certified Instructor" badges are
  **retired** along with the Node terminology, and have been removed. Do not reuse them.
- `assets/badges/community_badge_example.png` is an **example only** of the direction for the
  new single community badge ("Official Bitcoin Education Community", Education Network,
  replacing the Light/Full Node tiers): a circular purple-and-white seal with laurels, the
  B-tag mark and a banner lockup. **Treat it as direction, not as approved artwork.**
- A **"Certified Educator"** badge is expected but does not exist yet.

> **Note from Document 2:** the MFB Assets stack deliberately excludes badge work. Badges were
> treated as graphics, not as a separate achievement taxonomy. If a badge system is wanted, it
> is new work rather than a gap in the asset stack.

---

## 13 · Components

Eight React primitives in `components/core/`. Each ships `.jsx`, `.d.ts` and `.prompt.md`.

Namespace when mounting from the bundle: `MyFirstBitcoinDesignSystem_b26ab8.<Name>`

| Component | Purpose |
|---|---|
| `Button` | Primary action control |
| `IconButton` | Square-cornered icon button |
| `Badge` | Status / label pill |
| `Tag` | Metadata tag |
| `Card` | Surface container |
| `StatBlock` | The big-number motif |
| `Highlight` | The highlighter — see §7 |
| `ParallelogramFrame` | The signature skewed frame |
| `Avatar` | User / educator image |

### Button

Variants: `primary` (purple), `accent` (orange), `secondary` (purple outline, 2px),
`ghost` (transparent), `on-brand` (white on purple).

Sizes: `sm` 36px / 14px type · `md` 46px / 16px · `lg` 56px / 18px.

Always SemiBold 600, `letterSpacing: -0.01em`, `lineHeight: 1`, `whiteSpace: nowrap`.
Hover shifts to the darker step; press scales to 0.98. Disabled drops to 0.4 opacity.

### IconButton

Same variant set. Default 46px square, `--radius-md`. Press scales to 0.95.

> **Note:** its docstring currently reads *"Pairs a Lucide icon with brand tones"* — stale,
> see §11.

### StatBlock

One huge figure carrying one point. Value at Medium 500, `clamp(64px, 12vw, 180px)`,
line-height 0.9, tracking `-0.04em`. Label at 28px Medium, max-width 360px.

Tones: `light` (strong / body) and `brand` (white / 75% white).

> Its own docstring carries the rule: *"No decorative rule — the brand's only bar is the
> highlighter, which underlines a word. Never place a bar above the value."*

### ParallelogramFrame

Takes `width`, `height`, `fill`, `angle` (defaults to `var(--skew-angle)`). Skews the outer
element and **counter-skews the inner content** so it stays upright.

Because it reads `--skew-angle`, it self-corrects if the 13°/19° question is resolved in the
token. Correct by construction.

### Highlight

Wraps one word. Hard-codes the canonical geometry from §7. **Verified correct** against the
asset stack — no change needed.

---

## 14 · Slide templates

Five branded 16:9 templates in `slides/`:

| File | Type |
|---|---|
| `cover.html` | Cover |
| `divider.html` | Section divider |
| `quote.html` | Big quote |
| `stat.html` | Stat / number |
| `why-how-what.html` | Three-column argument |

> **⚠ SEE DOC 2 §9.** The MFB Assets stack defines **twelve** slide types and ships an 18-slide
> teaching deck covering all of them. These five overlap partially (cover, divider, stat, and
> loosely quote ↔ big statement). Maintaining two slide systems is not recommended.

---

## 15 · The micrographics publishing pipeline

**This section is load-bearing and easy to miss.** It governs how graphics reach the Bitcoin
Diploma, and its constraints are stricter than ordinary web CSS.

The `micrographics/` directory is the **source of truth for English-language HTML/CSS**
micrographics in the publishing pipeline. Each is authored in a Claude Design project, then
pasted into a Sanity `micrographic` block. Translations happen automatically downstream.

### Structure

```
micrographics/
  README.md              # the full authoring contract
  tokens.css             # brand tokens mirrored from print.css §1
  <slug>/
    micrographic.html    # exact fragment for the block's HTML field
    micrographic.css     # exact CSS for the block's CSS field
    meta.json            # { bundleVersion, title, slug, altText, caption }
    preview.html         # self-contained Claude Design card
```

`<slug>` is the Sanity Slug field value and doubles as the CSS scope class (`mg-<slug>`).

### The authoring contract — three hard rules

**1. Tag translatable text with `data-t="key"`.**
Only the *innerHTML* of a `data-t` element is translated. Everything else — numbers, symbols,
markup — is left as-is. **Any visible text not inside a `data-t` element will never be
translated.**
- Keys match `^[A-Za-z0-9_-]+$`, unique within one micrographic, never nested.
- Inline markup inside a tagged element travels with the text.
- Numerals stay *outside* `data-t` — see the worked example below.

**2. Scope every CSS selector under `.mg-<slug>`.**
The renderer wraps the HTML in `<figure class="micrographic mg-<slug>">` and there is **no
runtime CSS scoping** — WeasyPrint has no `@scope`. Unscoped rules leak into the whole book.

**3. Stay inside the WeasyPrint CSS envelope.**

| ✅ Allowed | ❌ Forbidden |
|---|---|
| flexbox with **explicit** `pt`/`mm`/`%`/`em` sizing | CSS grid |
| floats | `vh` / `vw` / `vmin` / `vmax` |
| absolute positioning | `rem` |
| inline SVG | `position: fixed` / `sticky` |
| | `@import` |
| | JavaScript |

> **This is the constraint most likely to catch you out.** It is documented here and in
> `micrographics/README.md` — and it is **not** mentioned in the design system's main style
> guide. Two templates in the MFB Assets stack violate it. See Document 2 §2.

### The print token vocabulary — different names, same brand

`micrographics/tokens.css` mirrors `apps/web/public/styles/print.css` §1, which it declares
**the source of truth for the PDFs**:

```css
--ts-font-family:     "IBM Plex Sans";
--color-purple:       #422C70;   /* primary brand purple (Student edition) */
--color-purple-dark:  #2B1C58;   /* Educator edition / strong accents */
--color-purple-light: #5E378E;   /* light card background */
--color-purple-deep:  #673C95;   /* definition card background */
--color-orange:       #F7941F;   /* links and accent */
--color-amber:        #FBB040;   /* card emphasis text */
--color-lilac:        #D8D8E7;   /* blockquote attribution */
--color-caption:      #6C6C7D;   /* figure / video captions */
--color-text:         #1a1a1a;   /* default body text */
--color-white:        #fff;
--color-black:        #000;
```

> **⚠ SEE DOC 2 §12 — this is a second complete token vocabulary for the same brand.** Same hex
> values under different names, kept in sync manually. Note `--color-purple-deep: #673C95` exists
> **only** here and has no design-system equivalent. This is the highest-priority structural
> finding in the audit.

### Worked example — `the-halving`

The existing micrographic demonstrates the correct patterns. Note that **prose is tagged and
numerals are not**:

```html
<div class="mg-the-halving">
    <h3 class="mg-the-halving__title" data-t="title">The Bitcoin Halving</h3>
    <p class="mg-the-halving__intro" data-t="intro">
        Every 210,000 blocks — roughly every four years — the reward paid to miners
        is cut in half…
    </p>
    <ol class="mg-the-halving__track">
        <li class="mg-the-halving__era">
            <span class="mg-the-halving__reward">50</span>
            <span class="mg-the-halving__unit" data-t="unit1">BTC / block</span>
            <span class="mg-the-halving__year" data-t="year1">2009</span>
        </li>
        …
        <li class="mg-the-halving__era mg-the-halving__era--current">
            <span class="mg-the-halving__reward">3.125</span>
            …
        </li>
    </ol>
    <p class="mg-the-halving__note" data-t="note">…</p>
</div>
```

Its CSS shows the house conventions: BEM-ish naming under the scope class, `pt` units
throughout, `1pt` borders, `3pt` radii, token references with hex fallbacks, and flexbox with
`flex: 1 1 0` rather than grid.

### Library model

Micrographics are a **reusable library** — each is one shared Sanity document that content
*references*. Edit once, and every place that uses it updates, in every language.

1. **Author** in Claude Design → sync to the design-system project
2. **Import** via Project Archive `.zip` → Sanity Micrographic library → publish
3. **Reference** from sections, slides, brochures, one-pagers
4. **Translate** via `pnpm mfb translate --micrographics`

Run `pnpm lint:micrographics` before syncing — the linter enforces the whole contract.

---

## 16 · What is stale in this system

Five things, flagged inline above and detailed in Document 2. Listed here so nothing is missed:

| # | What | Doc 2 ref |
|---|---|---|
| 1 | **Iconography recommends Lucide** — a first-party 153-icon set now exists | §6 |
| 2 | **The slant is stated as 19°** — the artwork measures 13°; disputed, pending November | §5 |
| 3 | **`--text-strong` is pure black** — three competing blacks exist across the system | §7 |
| 4 | **Two token vocabularies** — `--purple-300` vs `--color-purple`, synced by hand | §12 |
| 5 | **The print envelope is not in the main guide** — only in `micrographics/README.md` | §13 |

Also missing rather than stale: the five-tier asset hierarchy, icon tokens, an `Icon`
component, Tier 2 elements, the Tier 3 graphics library, Tier 4 layouts, and the Tier 5
production templates. All are in Document 2.

**Everything else in this document is verified correct** against the MFB Assets audit of
21 August 2026 — the purple ramp, the orange accent, the cool gray ramp, `--paper`,
`--radius-lg`, the highlighter geometry, the two-colour rule, the flat-surface rule, the
no-gradient rule, the type weights, the retired Node terminology, and `ParallelogramFrame`.

---

## 17 · Provenance

**Sources used to build this design system:**

- **Figma:** "My First Bitcoin.fig" — Brand Book, Slide Deck, Landing Page, Social Media,
  fliers and collateral. *Read 19 August 2026: contains **no UI icon set**.*
- **GitHub — brand assets:** [`MyFirstBitcoin/mfb-brand`](https://github.com/MyFirstBitcoin/mfb-brand)
  — logos, icons, banners, badges, profile pictures, Brand Book PDF
- **GitHub — org and products:** [`MyFirstBitcoin`](https://github.com/MyFirstBitcoin) —
  `Education-Network`, `mfb-curriculum`, `myfirstbitcoin.org`, `mfb-impact`
- **Website:** myfirstbitcoin.org · **Impact hub:** impact.myfirstbitcoin.org

**Files in the design system:**

```
styles.css                  # global entry point — link this
tokens/colors.css · typography.css · spacing.css · fonts.css
guidelines/                 # 13 foundation specimen cards
assets/logos/ · profile/ · badges/
components/core/            # 8 React primitives + .d.ts + .prompt.md each
ui_kits/website/            # myfirstbitcoin.org recreation
slides/                     # 5 slide templates
micrographics/              # publishing pipeline + tokens + 1 worked example
SKILL.md                    # Claude Agent Skill entry point
readme.md                   # the full guide this document transcribes
```

---

*Document 1 of 2. Continue to **MFB Assets — Style Guide** for the asset hierarchy, the icon
set, the elements, graphics, layouts and templates.*
