# MFB Assets — Style Guide

**Handoff document 2 of 2** · The five-tier visual asset system
**Source project:** MFB Assets · **Ratified:** August 2026 · **Transcribed:** 21 August 2026
**Prepared for:** Bitcoin Diploma asset production

> **How to use this document.** Document 1 (*My First Bitcoin — Design System*) is the style
> authority: colour, type, voice, motif, components. **This document is the asset authority:**
> what may be drawn, how it is constructed, and what is already built.
>
> Read Document 1 first. Then read §0 of this document, which lists the four places the two
> disagree and which one wins.
>
> **Nothing in this document is a preference.** Every value was ratified against shipped
> artwork or a stated production constraint, and every exclusion was a decision with a reason.

---

## Table of contents

- [§0 · Where this document overrides Document 1](#0--where-this-document-overrides-document-1)
- [§1 · The one rule](#1--the-one-rule)
- [§2 · The eight constants](#2--the-eight-constants)
- [§3 · The slant, definitively](#3--the-slant-definitively)
- [§4 · Tier 1 — Icons](#4--tier-1--icons)
- [§5 · Tier 2 — Elements](#5--tier-2--elements)
- [§6 · Tier 3 — Graphics](#6--tier-3--graphics)
- [§7 · Tier 4 — Layouts](#7--tier-4--layouts)
- [§8 · Tier 5 — Templates](#8--tier-5--templates)
- [§9 · Surface constraints](#9--surface-constraints)
- [§10 · The print pipeline — non-negotiable](#10--the-print-pipeline--non-negotiable)
- [§11 · Exclusions](#11--exclusions)
- [§12 · Known defects and debts](#12--known-defects-and-debts)
- [§13 · Producing a new asset](#13--producing-a-new-asset)
- [§14 · File inventory](#14--file-inventory)
- [§15 · Governance](#15--governance)

---

## §0 · Where this document overrides Document 1

Four disagreements. Each is named in both documents.

| Topic | Document 1 says | This document says | Which wins |
|---|---|---|---|
| **Icons** | No first-party set; use Lucide from CDN | 153 first-party icons, committed | **This document.** The set exists. Do not use Lucide. |
| **Slant angle** | `--skew-angle: -19deg` | 13°, measured from the logo | **Unresolved.** See §3 — do not assume either silently. |
| **Body black** | `--text-strong: #000000` | `#1A1A24` | **This document**, provisionally. Also disputed — see §12. |
| **Slide system** | 5 templates in `slides/` | 12 slide types, 18-slide deck | **This document.** Superset of Document 1's five. |

And one correction that goes the other way:

| Topic | This project had | Correct value | Note |
|---|---|---|---|
| `--orange-400` | `#D97B06` | **`#EF7B00`** | Document 1 is right. This project documented a wrong hex. Rendered artwork is unaffected — the token resolved correctly at runtime — but do not carry `#D97B06` forward. |

---

## §1 · The one rule

> **A tier may only use what the tiers below it define.**

A template cannot invent a diagram. A diagram cannot invent an arrow. An arrow cannot invent a
stroke weight. Everything traces to Tier 1.

**The practical consequence:** producing an asset means **filling a template**, never designing
from scratch. That is what keeps assets made months apart consistent, and it is the whole
reason the hierarchy exists.

**The diagnostic:** if a requested asset has no home in the stack, that is the signal. It is
either a variant of an existing template — duplicate and adjust — or it is genuinely a new
template, and it belongs in Tier 5 first. Producing it directly means it inherits nothing and
drift starts on the first file.

### The stack

| Tier | Name | Count | Builds on |
|---|---|---|---|
| **1** | Icons | 153 files | Nothing. This is the floor. |
| **2** | Elements | 16 named parts | Tier 1 stroke, caps, joins, angle |
| **3** | Graphics | 12 patterns | Tiers 1–2 only. No new primitives. |
| **4** | Layouts | 11 skeletons | Tier 3 blocks on a shared grid |
| **5** | Templates | 5 artefacts | Tier 4 skeletons filled with Tier 3 blocks |

---

## §2 · The eight constants

Ratified August 2026 against shipped artwork. Every tier inherits these. **Reproduce these
eight values and the system is recoverable even if every file is lost.**

| Value | Constant | Detail |
|---|---|---|
| **24u** | Icon canvas | 20×20u live area, 2u padding every side |
| **2u** | Stroke | One weight. 2.5u exists only for Diploma print. |
| **0u** | Corners | Hard in every glyph. Radius belongs to surfaces. |
| **butt** | Caps | No round, no square projection, no exceptions |
| **6** | Miter limit | Only bites below roughly 30° |
| **13°** | Slant | From the logo icon. Frames lean; glyphs never do. |
| **12pt** | Print floor | Any line a learner reads. Labels/folios 8–10pt. |
| **44px** | Touch target | App minimum, whatever the icon size inside it |

### As tokens

Not yet in the design system. Recommended addition:

```css
:root {
  --icon-canvas:       24;    /* units — the drawing grid */
  --icon-live-area:    20;    /* units — 2u padding every side */
  --icon-stroke:        2;    /* units — the one weight */
  --icon-stroke-print:  2.5;  /* Diploma print cut only */
  --icon-cap:          butt;
  --icon-join:         miter;
  --icon-miterlimit:    6;
  --icon-radius:        0;    /* hard corners in every glyph */
  --icon-accent:       var(--orange-300);

  --icon-size-sm: 20px;   --icon-size-md: 24px;
  --icon-size-lg: 32px;   --icon-size-xl: 48px;

  --touch-target-min: 44px;
  --print-type-floor: 12pt;
}
```

> **Do not name a `:root` token `--mfb-icon-stroke`.** That exact name is read *inside* the
> sprite symbols and must stay settable per-element, or the print cut stops working. See §4.

---

## §3 · The slant, definitively

**One angle, everywhere: 13°.**

Measured from the logo icon. It replaced two earlier figures:

| Value | Source | Status |
|---|---|---|
| 19° | Brand Book, stated in words | Superseded — but still written in Document 1 |
| 13.3° | Briefly ratified by this project | Superseded — measured against artwork |
| **13°** | The logo icon itself | **Current** |

> **⚠ This is the one open question in the whole stack.** The Brand Book says 19° in words; the
> artwork measures 13°. The entire asset stack is cut to 13°. Amending the design system to 13°
> writes a value the Brand Book contradicts. Ratifying 19° means re-cutting everything.
>
> **This is the November discovery call's decision (question 02), not a designer's.** Until it
> is settled, use 13° for consistency with the built stack, and flag any new artwork as
> angle-dependent.

### The rules

1. **Frames lean. Glyphs never do.** An icon is never skewed.
2. **A glyph inside a leaning frame counter-skews +13°** so its verticals stay true.
3. **Never two slant angles in one composition.**
4. **The highlighter's 1.4° tilt is a different value** for a different purpose. Do not collapse them.

### Where the slant is permitted

Currently permitted on frames at **48px and above only** — below that the frame closes the
counters of the glyph inside it. This is a provisional rule pending the same November call
(question 03).

---

## §4 · Tier 1 — Icons

The atomic vocabulary, and **the only tier that exists as consumable files.**

### What is in the set

| Tier | Count | What |
|---|---|---|
| Workhorses | 137 | Converted and re-terminated from a base set |
| Brand carriers | 16 | Drawn fresh, prefixed `brand-` |
| Curriculum marks | 3 | `callout`, `definition`, `key-takeaways` |
| **Total** | **153** | |

`brand-bitcoin` is **deliberately excluded** — it places the existing B-tag asset rather than
drawing a glyph. **The logo is never redrawn.**

### Specification

| Property | Value | Note |
|---|---|---|
| Canvas | `viewBox="0 0 24 24"` | No `width`/`height` on the file |
| Live area | 20×20u | 2u padding every side, nothing crosses it |
| Stroke | 2u | 2.5u on a `-print` cut only |
| Caps | `butt` | No round, no square projection |
| Joins | `miter`, limit `6` | Corrected from `4` in the first spec draft |
| Corners | 0u | Converter strips every `rx` and every corner arc |
| Colour | `currentColor` | Tier 2 accents read `--mfb-icon-accent` |
| Sizes | 20 / 24 / 32 / 48 | **No 16px cut** — see §11 |

### The fourteen groups

`Bitcoin & money` · `Keys & custody` · `Network & nodes` · `Learning & diploma` ·
`People & community` · `Content & media` · `App chrome` · `Actions` · `Arrows & direction` ·
`Status & feedback` · `Comms` · `Place` · `brand` · `curriculum`

### Naming

**Concept first, kebab-case, singular, ASCII.**

| ✅ | ❌ | Why |
|---|---|---|
| `key-cold-storage` | `cold-storage-key` | Concept leads |
| `wallet` | `wallets` | Singular |
| `wallet` | `sidebar-icon` | Never named for where it is used |

Modifiers are **suffixes**: `-print`, `-filled`, `-alt`. Brand carriers are **prefixed**
`brand-`.

### The nine checks

Eight are machine-testable **on purpose**, so review time goes on the ninth — the only one a
script cannot judge.

1. `viewBox="0 0 24 24"`, with no `width` or `height` attributes on the file.
2. `stroke-width="2"` — or exactly `2.5` on a `-print` cut, and nothing else.
3. `stroke-linecap="butt"`. No round caps, no square projection.
4. `stroke-linejoin="miter"` with `stroke-miterlimit="6"`.
5. No corner radius anywhere — no `rx`, no `ry`, no arc standing in for a corner.
6. `stroke="currentColor"`. No hard-coded hex on a Tier 1 icon.
7. Nothing crosses the 20×20u live area; 2u padding on every side.
8. Concept-first kebab-case name, singular, no reference to where it is used.
9. **(Human)** Reads at 20px on white **and** on purple, and does not stand out in a row of ten.

### Two implementation details that will bite you

Both of these are real bugs that shipped and were fixed. Both are **invisible in source review**
because the markup looks correct.

**1. Stroke must ride a custom property *inside* the symbol.**

```xml
<!-- CORRECT -->
<symbol id="mfb-wallet" viewBox="0 0 24 24" fill="none" stroke="currentColor"
        style="stroke-width:var(--mfb-icon-stroke, 2)"
        stroke-linecap="butt" stroke-linejoin="miter" stroke-miterlimit="6">
```

A `stroke-width` *attribute* on the symbol beats one set on the outer `<svg>`, so a `print`
flag set outside silently fails to reach inside a `<use>`. The custom property is what makes
the 2.5u print cut actually work.

**2. `currentColor` does not cross the sprite host boundary.**

A sprite loaded into an out-of-flow host div resolves `currentColor` against **the host's**
inherited colour, not the `<use>` site. Every icon in the teaching deck once rendered
white-on-white because of this.

Two safe patterns:
- **Set colour explicitly at the `<use>` site** — for themed or runtime-coloured UI
- **Inline the geometry** — for fixed-palette documents like a deck or a print page

For a single document with a fixed palette, inline geometry is correct. The sprite's value is
runtime theming, which a deck does not need.

### The React component

`icons/Icon.jsx` — renders from the sprite by name.

```jsx
<Icon name="brand-wallet" size={24} />
<Icon name="brand-wallet" active />              {/* orange colour change */}
<Icon name="definition" print />                 {/* 2.5u stroke */}
<Icon name="map" label="Community map" />        {/* labelled = role="img" */}
```

Props: `name`, `size` (default 24), `color`, `active`, `print`, `label`, plus passthrough.
Exports `MFB_ICON_NAMES` so a bad name fails at build rather than rendering nothing.

**Load the sprite once per document before any `Icon` renders.** This is the one component with
a document-level prerequisite.

### The active state

**An orange colour change. Nothing else.**

No bar, no underline, no mark. The highlighter is the brand's only bar (Document 1 §7), and a
second bar under an icon or a nav item competes with it. This is a direct corollary of the
highlighter rule, not a separate preference.

---

## §5 · Tier 2 — Elements

Sixteen named parts that join, separate and frame **without carrying meaning themselves.** All
inherit the Tier 1 stroke, caps, joins and angle.

Two already exist as design-system components (`Highlight`, `ParallelogramFrame`) and are
correct — use those, do not rebuild them.

### Arrows and connectors — four

| Element | What | Spec |
|---|---|---|
| `arrow-straight` | The default direction mark. **Open chevron head, never filled** — a solid triangle reads heavier than the 2u line it terminates. | head 7u per side, 90° included |
| `connector-elbow` | Right-angle turns only, mitred sharp. **No curves** — the brand's geometry is hard cuts. | 90° turns, miter 6, no radius |
| `connector-dashed` | Optional or inferred relationships — the step that may not happen. | `dasharray 6 5`, gray-500 |
| `node-dot` | A junction, a stop, a point on a timeline. **Filled**, because hollow reads as an error on a 2u line. | ⌀12u filled, 6× stroke |

### Rules and dividers — three

| Element | What | Spec |
|---|---|---|
| `rule-hairline` | The default separator — table rows, list separators, card edges. | 1px, `--border` |
| `rule-strong` | Section boundaries and heading underlines. **Matches icon stroke exactly**, so rule and icon agree. | 2px, purple-300 |
| `rule-slanted` | A major divider at the brand angle. Segments may carry the palette. The one place the slant is not frame-exclusive. | 10u tall, `skewX(-13deg)`, 5u gaps |

### Frames and cuts — four

| Element | What | Spec |
|---|---|---|
| `parallelogram-frame` | The signature frame. One subject, content counter-skewed. *(= `ParallelogramFrame`)* | 6:7 aspect, `skewX(-13deg)` |
| `parallelogram-stack` | Layered frames for depth at **one shared angle.** Depth from offset, never a second angle. | 34u offsets, 4u rise per layer |
| `bracket` | Marks a region without boxing it — a pull-quote, a grouped set, a term under discussion. **Upright, never slanted.** | 2u stroke, arms 26u |
| `diagonal-cut` | The full-bleed edge where a purple section meets paper. Angle-exact at any viewport width. | `skewY(-13deg)` |

### Emphasis — three

| Element | What | Spec |
|---|---|---|
| `highlighter` | The brand's only bar. Under one word, never restyled. *(= `Highlight`)* | `-0.12em`, `0.14em`, `skewY(-1.4deg)` |
| `stat-tick` | A slanted tick beside a big number — does an underline's work **without becoming a second bar.** | 5u wide, 0.65em tall, `skewX(-13deg)` |
| `list-marker` | Replaces the bullet. Orange on the active item, gray otherwise. | 3u × 16u, `skewX(-13deg)` |

### Textures — four

| Element | What | Spec |
|---|---|---|
| `screen-dots` | An even dot screen over a brand surface. Print texture on a flat field, **no gradient.** | 1.6u dot, 11u pitch |
| `screen-fade` | The screen thinning across the field, on the brand axis. Section backgrounds, cover art. | 13° axis, 2.2u dot, 13u pitch |
| `hatch-slant` | Parallel 2u lines on the brand angle. Fills a shape that must read structural, not photographic — **and separates in greyscale.** | 2u line, 9u pitch, 77° |
| `halftone-portrait` | The Brand Book halftone, and the only thing entitled to the name. An **image treatment**, not a CSS pattern. | photographic input required |

The first three are `repeating-linear-gradient` patterns and are print-safe. `hatch-slant` is
what makes multi-series graphics survive greyscale, which is a Diploma requirement — see §6.

---

## §6 · Tier 3 — Graphics

Twelve patterns assembled **only** from Tiers 1 and 2. The aesthetic is fixed; **data and
purpose are customisable** — building blocks for users of all abilities.

> **The governing constraint:** the Bitcoin Diploma is printed, photocopied, and taught from in
> rooms with no projector. Every graphic must survive that.

### The five authoring rules

1. **Label every value on the mark**, not in a legend three inches away. Legends fail first
   when a graphic is photocopied.
2. **Separate series by hatch, not hue.** Every multi-series graphic must survive greyscale.
   Colour carries meaning second, never first.
3. **No pie charts.** They cannot be labelled reliably in print. `proportion-bar` replaces them.
4. **Data is editable, look is not.** A value and its label are neighbours in the markup, so a
   non-designer can change one without breaking the other.
5. **Every text node carries `data-t`.** Untagged text is never translated. See §10.

### The twelve patterns

| Group | Patterns | Note |
|---|---|---|
| **A · Teaching diagrams** | `comparison-pair`, `layer-stack`, `timeline`, `process-flow` | The Diploma's working set. Four, because a fifth would go unused. |
| **B · Data charts** | `bar-chart`, `proportion-bar`, `big-stat`, `trend-line` | Every value labelled on the mark. Greyscale-proof by construction. |
| **C · Micrographics** | `callout`, `definition`, `key-takeaways` | The three curriculum marks, matching the icons of the same names. |
| **D · Screen only** | `map` | One — and it must **never** reach the Diploma. Maps date faster than the print revision cycle. |

Group C matches the design system's existing micrographics library concept exactly and should
land there as three library entries.

> **⚠ DEFECT:** the built Tier 3 specimens use CSS grid and `px`, and carry no `data-t`. They
> **cannot render in the print pipeline** and would ship English-only. See §12 for the
> remediation. Rewrite as flexbox with `pt` before using any of them in the Diploma.

---

## §7 · Tier 4 — Layouts

Eleven skeletons deciding where a graphic sits, plus shared chrome. Grid, rhythm and hierarchy
with **no content assumptions baked in.**

| Group | Skeletons | Frame |
|---|---|---|
| **Print** | `chapter-opener`, `teaching-page`, `exercise-page` | A4 and Legal, flexible |
| **Web** | `landing-hero`, `content-page`, `directory-index` | Max 1280px content width |
| **App** | `app-home`, `app-lesson`, `app-progress` | 390px, mobile first |
| **Shared chrome** | `web-header`, `doc-sidebar`, `app-tab-bar` | Cross-surface |

**Paper size is deliberately unpinned.** A4 for Europe, Legal for North America, nothing fixed
to one. If a single global size is chosen later, the layouts absorb it without redrawing.

---

## §8 · Tier 5 — Templates

Finished, fillable surfaces. **Drop in content and they hold** — type longer and nothing breaks,
add a section and the pagination follows.

**This is what production actually uses.** An asset is a template plus content, never a fresh
design.

| # | Surface | Template | What it is | Constraint |
|---|---|---|---|---|
| 01 | Print | **Diploma chapter** | Opener, three sections, comparison figure, definition, callout, takeaways. Paginates itself. | 12pt floor, greyscale passes. **⚠ needs flexbox rewrite — see §12** |
| 02 | Print | **Community flier** | One page, one side, any office printer. What a local educator hands out to fill a room — date, place, what you will learn. | Smallest template, most copies printed |
| 03 | Web | **Landing page** | Hero, the argument, proof, one call to action. From `landing-hero` + `content-page`, with `big-stat` and `process-flow` carrying the middle. | Needs real photography to finish |
| 04 | App | **Lesson flow** | Four connected screens at 390px — home, lesson, exercise, complete. The only template with **behaviour** rather than pages. | 44px targets, working prototype |
| 05 | Slides | **Teaching deck** | 18 slides covering 12 slide types, with six deliberate repeats. Both a worked example and a template. | 1920×1080, 26px minimum type |

### The teaching deck's twelve slide types

`Cover` · `Section divider` · `Big statement` · `One-number stat` · `Definition` ·
`Diagram (three-part)` · `Diagram (sequence)` · `Comparison` · `Photo + caption` ·
`Photo full-bleed` · `Discussion prompt` · `Exercise` · `Key takeaways` · `Closing`

**Six repeats are deliberate** — two dividers, two statements, two definitions, two stats, two
diagram variants, two photo treatments. The repetition shows an educator which slides are meant
to be identical and which are variants.

**Swap notes live in each slide's speaker notes**, so they travel with the slide when it is
reordered or duplicated. Each says what goes in the slot *and the constraint* — five words max
on the cover, three takeaways not five, four rows max in the comparison.

---

## §9 · Surface constraints

The three build targets **do not each get their own kit.** They take different slices of the
same one. That is the only reason a learner recognises the app as the same organisation as the
Diploma.

| Surface | Frame | Uses | Excludes |
|---|---|---|---|
| **Website** | Max 1280px content width | All 153 icons, frames + textures, maps, hero layouts, social cards | — |
| **Programs (print)** | A4 and Legal, flexible | Curriculum marks, callouts, definitions, chapter template, certificate | **No maps.** 12pt floor. 2.5u stroke cut. |
| **App** | Mobile first, 44px targets | App chrome, status + feedback, stat blocks, screen skeletons, maps | — |

**The exclusions are the important part**, not the frames. "No maps in print" and "12pt on any
line a learner reads" are decisions someone will otherwise reverse in good faith.

---

## §10 · The print pipeline — non-negotiable

**Read this before authoring anything that will reach the Diploma.**

The publishing pipeline renders through **WeasyPrint**, whose CSS support is narrower than a
browser's. This is documented in the design system's `micrographics/README.md` but **not** in
its main style guide — which is exactly how two templates in this project ended up violating it.

### The envelope

| ✅ Allowed | ❌ Forbidden |
|---|---|
| flexbox with **explicit** `pt`/`mm`/`%`/`em` sizing | **CSS grid** |
| floats | `vh` / `vw` / `vmin` / `vmax` |
| absolute positioning | `rem` |
| inline SVG | `position: fixed` / `sticky` |
| | `@import` |
| | JavaScript |

### Scoping

Every CSS selector must sit under `.mg-<slug>`. The renderer wraps output in
`<figure class="micrographic mg-<slug>">` and there is **no runtime scoping** — WeasyPrint has
no `@scope`. Unscoped rules leak into the entire book.

### Translation tagging

Tag translatable text with `data-t="key"`. **Only the innerHTML of a `data-t` element is
translated. Untagged visible text is never translated**, and the linter warns about it.

- Keys match `^[A-Za-z0-9_-]+$`, unique per micrographic, never nested
- **Numerals and symbols stay outside `data-t`** — only prose is tagged
- Inline markup inside a tagged element travels with the text

### Units

Author in `pt`. House conventions from the existing `the-halving` micrographic: `10pt 12pt`
padding, `14pt` titles, `9pt` body, `8pt` labels, `1pt` borders, `3pt` radii, and
`flex: 1 1 0` rather than grid.

### The token vocabulary is different in print

The print pipeline uses a **parallel set of token names** for the same brand colours:

| Concept | Design system | Print pipeline |
|---|---|---|
| Primary purple | `--purple-300` | `--color-purple` |
| Deep purple | `--purple-400` | `--color-purple-dark` |
| Light purple | `--purple-200` | `--color-purple-light` |
| Definition-card purple | *(none)* | `--color-purple-deep: #673C95` |
| Accent orange | `--orange-300` | `--color-orange` |
| Amber | `--orange-200` | `--color-amber` |
| Caption gray | `--gray-700` | `--color-caption` |
| Body text | `--text-strong` | `--color-text: #1a1a1a` |
| Font family | `--font-sans` | `--ts-font-family` |

Always write token references **with hex fallbacks** in print CSS:
`var(--color-purple, #422C70)`.

> **Note `--color-purple-deep: #673C95` exists only in print** and has no design-system
> equivalent. It is a production colour the design system does not know about. This is the
> highest-priority structural finding in the audit — two declared sources of truth, synced by
> hand.

### Output shape

Each micrographic is a folder:

```
<slug>/
  micrographic.html    # exact fragment for the Sanity HTML field
  micrographic.css     # exact CSS for the Sanity CSS field, scoped to .mg-<slug>
  meta.json            # { bundleVersion, title, slug, altText, caption }
  preview.html         # self-contained Claude Design card
```

Run `pnpm lint:micrographics` before syncing — the linter enforces the whole contract.

---

## §11 · Exclusions

**The exclusions are as load-bearing as the rules.** Each was a decision with a reason, and
each is something a future contributor will attempt in good faith. A guide that records only
what to do gets quietly undone.

### 1 · No badge system

Badges were treated as graphics, not as a separate achievement taxonomy. Node badges are
retired; the community badge is an example only; a Certified Educator badge is expected. **If a
badge system is wanted, it is new work — not a gap in this stack.**

### 2 · No 16px icon cut

Dropped on evidence: **no MFB surface places icons inline in body text or in dense tables.** It
was solving a problem that does not exist. If one appears, draw a thinner cut for that icon
alone and name it `<concept>-16.svg`.

*That is the right reason to drop something — not that it was hard, but that it solved nothing.*

### 3 · No second bar, anywhere

The active state is an orange colour change. A bar under an icon or a nav item competes with
the highlighter, which is the only bar the brand owns. Direct corollary of Document 1 §7.

### 4 · No Lucide at runtime

The CDN reference comes out of the design system. Leaving it in means both sets get used side
by side and the family test was for nothing.

### 5 · No maps in print

Maps are **online only** — website and app. On a printed Diploma they date faster than the
revision cycle that could fix them.

### 6 · No pie charts

They cannot be labelled reliably in print. `proportion-bar` replaces them.

---

## §12 · Known defects and debts

Written down rather than tidied away, each dated to a real trigger so it surfaces when it
matters. **A new project inheriting this system inherits these too — they must travel in the
brief or they get rediscovered the hard way.**

### Defects — wrong now, fix before use

| # | Defect | Detail | Action |
|---|---|---|---|
| D1 | **Tier 3 graphics use CSS grid** | Five specimens in `3 Graphics`; unrenderable in WeasyPrint | Rewrite as flexbox with `pt` |
| D2 | **Diploma chapter template uses CSS grid** | The comparison figure. Its `mm` sizing and `12pt` type are correct; the grid is not. | Rewrite as flexbox with explicit `%`/`mm` |
| D3 | **No graphic carries `data-t`** | Every Tier 3 graphic would ship English-only into a multilingual book | Tag every text node; leave numerals untagged |
| D4 | **`--orange-400` documented as `#D97B06`** | Correct value is `#EF7B00`. Rendered artwork unaffected — the token resolved correctly — but the reference documents a false hex. | Correct to `#EF7B00` |
| D5 | **Graphics are not pipeline-shaped** | Inline styles, no `.mg-<slug>` scoping, `px` not `pt`. Cannot be pasted into the Sanity block's separate HTML/CSS fields. | Produce `micrographic.html` + `.css` + `meta.json` per slug |

### Debts — correct now, will need work later

| # | Debt | Trigger |
|---|---|---|
| T1 | **Three curriculum icons wrong in print** — `callout`, `definition`, `key-takeaways` ship in the current Diploma with round caps, a 6px radius and a 3px stroke on a 48 grid. Re-cut versions are committed. | Next curriculum revision |
| T2 | **Figma holds no icon set** (read 19 Aug 2026). Every value here is a *promotion candidate* into the source, not a replication of it. Nothing contradicts Figma; nothing has been accepted into it. | November discovery call |
| T3 | **Slant stated as 19° in words** — the artwork measures 13°. Confirm or amend with a cost attached. | November discovery call |
| T4 | **Paper size unconfirmed** — built flexible (A4 Europe, Legal North America). | If a global size is chosen |
| T5 | **Tiers 2–5 are specified, not packaged** — Tier 1 is the only tier that exists as consumable files. | On a developer request |
| T6 | **Two token vocabularies** — needs a build-time generation or aliasing decision, not a design decision. | November call, then Benoit |
| T7 | **Three competing blacks** — `#000000` (design system), `#1a1a1a` (print), `#1A1A24` (asset stack). Recommend `#1A1A24` for consistency with the cool ramp. | Cheap, but touches every component |

---

## §13 · Producing a new asset

### The workflow

1. **Map the request to a template.** Every asset resolves to one template plus content. If it
   does not resolve to one, stop — decide whether it is a variant or a new template *before*
   producing it.
2. **Check the surface constraints** (§9). Print excludes maps and enforces the 12pt floor.
3. **If print-bound, read §10 first.** Flexbox, `pt`, scoped, `data-t` tagged. Not optional.
4. **Fill the template.** Do not restyle it. If the template is wrong, fix the template — a
   one-off override is drift with a deadline.
5. **Run the checks.** Icons: the nine (§4). Graphics: the five rules (§6) plus the linter.

### Setting up a new project

| Move | What | Why |
|---|---|---|
| **Required** | `icons/` — sprite, manifest, 152 SVGs, `Icon.jsx` | The floor. Nothing works without it. |
| **Required** | The five Tier 5 templates | This is what production fills. |
| **Required** | Bind the MFB design system | A pick, not a copy — it lives at the system level. |
| **Required** | `assets/` — logos and the B-tag mark | Never redrawn, always placed. |
| **If amending** | Tier 2–4 specification pages | Their rules are already baked into the templates. |
| **Archive** | Tier 1 audit/spec/conversion pages | Provenance, not production. |

### Then, in order

1. **Bind the design system first** — before any file is written. Tokens resolving to nothing
   is the most common cause of a page that looks *almost* right.
2. **Copy `icons/` and confirm the sprite loads.** Render one icon on white and one on purple.
   If either is invisible, see §4 — you are relying on inherited `currentColor` across a host
   boundary.
3. **Map every requested asset to a template.** Anything with no home is either a variant to
   duplicate or a new template. Decide which before producing it.
4. **Carry the debts into the brief** (§12). A new project does not know about the pending
   curriculum re-cut or the unconfirmed paper size. Unwritten, they get rediscovered expensively.
5. **Produce by filling, never by designing.** The moment an asset is drawn outside a template
   it inherits nothing, and drift starts on the first file.

---

## §14 · File inventory

### Committed and consumable

```
icons/
  mfb-icons.svg        # 153 symbols, 65KB, one <symbol> per icon
  mfb-icons.json       # manifest: version, spec, name/group/tier per icon
  Icon.jsx             # React component + MFB_ICON_NAMES
  svg/                 # 152 individual SVG files
```

### Specification pages (this project)

```
0    Asset Ecosystem            # the index across all five tiers
1.1  Icons - Audit              # 541 → 150 essentials
1.2  Icons - Specification      # the eight clauses
1.3  Icons - Brand Carriers     # the 16 drawn fresh
1.4  Icons - Conversion         # re-termination of the 137
1.5  Icons - Family Test        # all icons at 20px on purple
1.6  Icons - Packaging          # sprite, component, contribution rules
2    Elements                   # the 16 named parts
3    Graphics                   # the 12 patterns  ⚠ see D1
4    Layouts                    # the 11 skeletons
5    Templates                  # what a template promises
5.1  Template - Diploma Chapter # ⚠ see D2
5.2  Template - Community Flier
5.3  Template - Landing Page
5.4  Template - Lesson Flow
5.5  Template - Teaching Deck
```

### Governance (post-publication)

```
A  Discovery Call - November        # the harmonisation brief
A  Harmonisation - Scope of Work
   MFB Assets Reference Sheet       # the single-page keystone
   MFB Design System - Correction List.md
```

---

## §15 · Governance

### Ownership

| Role | Who | Scope |
|---|---|---|
| **Harmonisation owner** | Patrick | The Figma, the promotion register, ratifying open questions |
| **Asset work** | Pablo | Producing and maintaining the five tiers |
| **App and publishing** | Benoit | Pipeline, tokens, the app |
| **Websites** | Alexandre | Main site and impact hub |

### The chain — one direction only

```
Figma  →  GitHub  →  brand.md + /build /design skills  →  Products
source    mirror     generated brief                      audited, never defining
```

**Truth flows one way.** A change enters at the top and is pushed down; it never enters halfway
and works backwards. Anything arriving out of order is an audit finding, not a new source.

### The four rules

1. **Figma is the source.** It is where a brand value is true. Everything else reports it.
2. **Amend, never overwrite.** A value changes by adding a dated entry that supersedes the old
   one. The previous entry stays visible.
3. **GitHub is downstream and exact.** A faithful copy plus the things Figma cannot hold — the
   sprite, the tokens, the component code. It never originates a value.
4. **One `brand.md` for every AI tool**, generated from the repo rather than written per tool.

### Status of everything in this document

Every value here is a **Tier 3 decision the Figma is silent on** — which makes all of them
promotion candidates rather than replications. Nothing contradicts the source, so nothing needs
escalating. But it does need a custodian to accept it.

**Ratified August 2026. Harmonisation is post-publication. Until then, this project is the
working source.**

---

*Document 2 of 2. See **My First Bitcoin — Design System** for colour, type, voice, motif and
components.*
