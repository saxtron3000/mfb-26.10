# My First Bitcoin Design System — Correction List

**Audit date:** 21 August 2026
**Auditor:** Pablo (asset work) · owner for harmonisation: Patrick
**Design system audited:** `MyFirstBitcoinDesignSystem_b26ab8` (`b26ab809-b968-4c9e-bbc6-ff90715695a2`)
**Audited against:** MFB Assets project — five-tier asset hierarchy, ratified August 2026

---

## How to read this document

This is a list of **corrections to the design system**, derived from building a complete
five-tier visual asset stack against it. It is not a wishlist. Every entry is a place where
the design system and the asset stack currently disagree, or where the design system is
silent on something the stack had to decide.

Three kinds of entry appear, and the distinction matters:

| Kind | Meaning | Action |
|---|---|---|
| **STALE** | The design system says something that was true and no longer is. | Amend the design system. |
| **GAP** | The design system is silent; the asset stack had to decide. | Promote the decision into the design system. |
| **MY ERROR** | The asset stack is wrong and the design system is right. | Fix the asset stack, not the design system. |

**Read the MY ERROR entries first.** There are four, and two of them are serious. A
correction list that only travels in one direction is a wishlist wearing a lab coat.

Every entry carries a **severity** and a **difficulty**, scored the same way as the November
discovery-call audit, because those two together — not severity alone — decide the order of work.

**Severity:** `breaks` (wrong logo, wrong colour, retired terminology, unrenderable output) ·
`visible` (wrong stroke, wrong angle, off-palette accent) · `cosmetic` (spacing, radius, a
caption a few points small)

**Difficulty:** `one-file` · `one-product` · `across-products`

---

## Executive summary

The design system is **structurally sound and factually stale**. Its foundations (colour ramp,
type tokens, spacing, the highlighter geometry, the component primitives) are correct and were
used unchanged throughout the asset stack. Nothing in the foundations needs rebuilding.

Four things are wrong, in descending order of cost:

1. **A second token vocabulary exists** (`--color-purple`, `--ts-font-family`) in the
   micrographics pipeline, parallel to the design system's own (`--purple-300`, `--font-sans`),
   with the same hex values under different names. This is the four-sources drift pattern
   reproduced inside a single project. *(§2)*

2. **The publishing pipeline's real constraints are not in the design system.** The
   micrographics library documents a WeasyPrint CSS envelope — no CSS grid, no `vh`/`vw`, no
   `rem`, `pt` units, `.mg-<slug>` scoping, `data-t` translation tagging. The design system's
   guide does not mention any of it, so anything authored from the guide alone is unrenderable
   in print. **Two of my own templates violate it.** *(§3, §11)*

3. **The slant is documented as 19° in four places and is 13° in the artwork.** *(§4)*

4. **The iconography section is obsolete.** It tells readers to pull Lucide from a CDN because
   no first-party set exists. 153 first-party icons now exist. *(§5)*

Beyond those, Tiers 2–4 (elements, graphics, layouts) have no representation in the design
system at all, and Tier 5 has partial representation (slides and a website kit, not the five
production templates).

---

# PART I — CORRECTIONS TO THE ASSET STACK (my errors)

These come first because they are cheapest to fix now and most expensive to propagate.

## §1 — MY ERROR: `--orange-400` hex is wrong throughout the asset stack

**Severity:** `visible` · **Difficulty:** `across-products`

- **Design system says:** `--orange-400: #EF7B00` (`tokens/colors.css`, line 15)
- **Asset stack says:** `--orange-400 #D97B06` (`MFB Assets Reference Sheet`, palette section)

`#EF7B00` is the design system's value and therefore the correct one. `#D97B06` appears to be
a value I derived rather than read, and it has been propagated into the reference sheet as
though it were canonical. Every eyebrow label and hover state in the asset stack that names
`--orange-400` resolves correctly at runtime (the token wins), so **no rendered artwork is
wrong** — but the reference sheet documents a false hex, and the reference sheet is the
document intended to survive into other projects.

**Action:** correct the reference sheet palette to `#EF7B00`. Audit the five templates for any
hard-coded `#D97B06`.

**Why this matters more than it looks:** the reference sheet was written to be the document
you can rebuild from if every file is lost. A wrong hex in it is a latent error that only
surfaces once the files are gone.

---

## §2 — MY ERROR: two of my templates use CSS grid and cannot render in the print pipeline

**Severity:** `breaks` · **Difficulty:** `one-product`

The micrographics pipeline (`micrographics/README.md`, authoring contract clause 3) states the
WeasyPrint envelope explicitly:

> ✅ flexbox with **explicit** `pt`/`mm`/`%`/`em` sizing, floats, absolute positioning, inline SVG.
> ❌ CSS grid, `vh`/`vw`/`vmin`/`vmax`, `rem`, `position: fixed`/`sticky`, `@import`, JavaScript.

Confirmed violations in the asset stack:

| File | Violation | Lines |
|---|---|---|
| `5.1 Template - Diploma Chapter` | `display:grid` on the comparison figure | 67 |
| `3 Graphics` | `display:grid` in five graphic specimens | 61, 86, 115, 191, 283, 344 |

The Diploma chapter template is the most affected: it is the template most likely to reach the
actual publishing pipeline, and it will not render there. The `mm` sizing and `12pt` type in
that file are correct; the grid is not.

**Action:**
1. Rewrite the Diploma chapter comparison figure as flexbox with explicit `%`/`mm` widths.
2. Rewrite the Tier 3 print-bound graphics (`comparison-pair`, `layer-stack`, `timeline`,
   `process-flow`, `bar-chart`, `proportion-bar`, `big-stat`, `trend-line`) as flexbox.
3. Screen-only graphics (`map`) may keep grid — it never reaches print by decision.

**Note on the Tier 3 spec page itself:** the page's own *layout* using grid is fine — it is a
screen document. Only the graphic *specimens*, which are meant to be copied into print, must
be envelope-safe. That distinction needs stating on the page, or the next person copies a
specimen and it silently fails.

---

## §3 — MY ERROR: no graphic carries `data-t` translation tagging

**Severity:** `breaks` · **Difficulty:** `one-product`

The pipeline translates micrographics automatically, but only the `innerHTML` of elements
carrying `data-t="key"` is translated (`micrographics/README.md`, clause 1). Untagged visible
text is **never translated** and the linter warns about it.

No graphic in Tier 3 carries `data-t`. Every one of them would ship English-only into a
multilingual Diploma.

Key rules I did not know and did not follow:
- Keys match `^[A-Za-z0-9_-]+$`, unique within one micrographic, never nested.
- Numbers and symbols stay outside `data-t` — only prose is tagged.
- Inline markup inside a tagged element travels with the text.

**Action:** add `data-t` to every text node in every Tier 3 graphic. Add the rule to the Tier 3
page as a stated constraint, and to the reference sheet's graphic rules (currently four rules;
this is a fifth and arguably the most consequential).

**Worth noting:** the existing `the-halving` micrographic tags prose (`title`, `intro`, `unit1`,
`year1`, `note`) but leaves the numerals (`50`, `25`, `12.5`) untagged. That is the correct
pattern and should be the documented example.

---

## §4 — MY ERROR: Tier 3 graphics do not use the pipeline's CSS scoping or units

**Severity:** `visible` · **Difficulty:** `one-product`

Two further pipeline requirements the asset stack ignores:

- **Scoping:** every selector must sit under `.mg-<slug>` because the renderer wraps output in
  `<figure class="micrographic mg-<slug>">` and there is no runtime scoping (WeasyPrint has no
  `@scope`). Unscoped rules leak into the whole book.
- **Units:** the pipeline authors in `pt` (`10pt 12pt` padding, `14pt` titles, `9pt` body,
  `1pt` borders, `3pt` radii). The asset stack authors in `px` throughout.

The asset stack uses inline styles, which sidesteps scoping but produces markup that cannot be
pasted into the Sanity `micrographic` block's separate HTML and CSS fields.

**Action:** Tier 3 print-bound graphics need a second, pipeline-shaped output: `micrographic.html`
+ `micrographic.css` + `meta.json` per slug, scoped and in `pt`. This is real work, not a
reformat — it should be scoped explicitly rather than absorbed silently.

---

# PART II — STALE: THE DESIGN SYSTEM SAYS SOMETHING NO LONGER TRUE

## §5 — STALE: the slant is documented as 19°, measured at 13°

**Severity:** `visible` · **Difficulty:** `across-products`

The 19° figure appears in **four** places:

| File | Location | Current text |
|---|---|---|
| `tokens/spacing.css` | line 40 | `--skew-angle: -19deg;` |
| `readme.md` | Visual Foundations | "The signature motif — the slant (~`-19deg`)" |
| `guidelines/brand-slant.html` | `@dsCard` subtitle | "The signature ~-19° lean" |
| `SKILL.md` | Quick orientation | "the ~-19° parallelogram lean" |

The asset stack is cut to **13°**, measured from the logo icon. That value replaced both the
19° stated here and a 13.3° figure the project itself briefly ratified before measuring the
shipped artwork.

**This is the one correction on this list that should not be made unilaterally.** The Brand
Book states 19° in words; the artwork measures 13°. Amending the design system to 13° writes a
value the Brand Book contradicts, and propagates instantly to everything bound to the system.

**Action:** hold for the November discovery call (question 02). Then either:
- **Ratify 13°:** change all four locations, and log the amendment as superseding the 19°
  entry rather than editing it away. Note that `--skew-angle` currently carries a
  `@kind other` annotation which should be preserved.
- **Ratify 19°:** the entire asset stack needs re-cutting. Cost is high and should be stated
  before the decision, not after.

**Detail worth carrying either way:** the asset stack distinguishes the *frame* angle (13°,
`skewX`) from the *highlighter* tilt (1.4°, `skewY`). These are different values for different
purposes and the design system correctly documents the highlighter separately. Do not
collapse them.

---

## §6 — STALE: the iconography section recommends Lucide from a CDN

**Severity:** `breaks` · **Difficulty:** `across-products`

Current text, `readme.md` ICONOGRAPHY:

> The brand has **no bespoke UI icon font.** For interface icons (arrows, menu, checks, etc.)
> use **[Lucide](https://lucide.dev)** — … *(Substitution flagged: no first-party UI icon set
> exists in the brand assets; Lucide is the recommended match.)* Load from CDN; keep stroke
> width ~2 and color from the palette.

And in Notes / caveats:

> UI icons use Lucide (CDN) as a flagged substitute — the brand has no first-party UI icon set.

And `SKILL.md` implies the same by omission.

A first-party set now exists: **153 icons**, committed as individual SVGs, a sprite, a manifest
and a React component. Leaving the Lucide line in place means both sets get used side by side,
which makes the entire family test pointless.

**Action:** replace the Iconography bullet with the first-party set and its spec. Remove the
CDN reference and the caveat. Add `assets/icons/` to the Assets index.

Also: `components/core/IconButton.jsx` line 4 docstring reads *"Pairs a Lucide icon with brand
tones."* — change to reference the MFB set.

---

## §7 — STALE: `--text-strong` resolves to pure black

**Severity:** `cosmetic` · **Difficulty:** `across-products`

`tokens/colors.css` line 55: `--text-strong: var(--black);` → `#000000`

The design system's own guide says *"Black and white provide balance and legibility"* but the
asset stack and the print pipeline both use an off-black:

| Source | Value |
|---|---|
| Design system `--text-strong` | `#000000` |
| Micrographics `--color-text` | `#1a1a1a` |
| Asset stack body copy | `#1A1A24` |

Three different "blacks" for the same job. The asset stack's `#1A1A24` is the cool-toned one
that matches the slightly-blue gray ramp; `#1a1a1a` is neutral; `#000000` is neither.

**Action:** pick one. Recommend `#1A1A24` — it is consistent with the deliberately cool ramp,
and pure black against `--paper #F6F6F8` is harsher than the brand's "corporate-clean" register
wants. Then align the micrographics token and the asset stack to it.

**Difficulty is `across-products` because** `--text-strong` is referenced by every component
in `components/core/`.

---

## §8 — STALE: the type scale does not match how display type is actually set

**Severity:** `cosmetic` · **Difficulty:** `one-product`

`tokens/typography.css` defines a scale taken from the Brand Book specimen:

```
--text-display: 147px   --text-h1: 70px    --text-h2: 58px
--text-section: 46px    --text-lead: 29px  --text-base: 22px
```

The asset stack's five templates and the teaching deck use a different, denser scale:

| Role | Design system | Asset stack |
|---|---|---|
| Cover heading | 147px | 120–132px |
| Section divider | — | up to 200px |
| Display heading | 70px | 60–104px |
| Section heading | 46px | 32–36px |
| Body | 22px | 15–20px |
| Eyebrow | — | 12.5–26px, 600 weight, 0.09–0.16em tracking |

Neither is wrong — the design system's scale is a Brand Book print specimen, the asset stack's
is screen-and-deck. But there is no token for the eyebrow (used on nearly every page in the
stack), no token for the 200px divider numeral, and `--text-base: 22px` is not the body size
any template actually uses.

**Action:** either add a second named scale (`--text-screen-*`) or add the missing tokens
(`--text-eyebrow`, `--text-numeral`) and annotate `--text-base` as print-specimen. Do not
delete the existing scale — it is the Brand Book's and correct for print.

---

## §9 — STALE: `slides/` templates predate the deck system

**Severity:** `cosmetic` · **Difficulty:** `one-product`

`slides/` holds five templates: cover, divider, quote, stat, why-how-what. The asset stack's
teaching deck defines **twelve** slide types and ships 18 slides covering all of them with six
deliberate repeats.

Overlap: cover, divider, stat, and (loosely) quote ↔ big statement. Missing from the design
system: definition, diagram (two variants), comparison, photo + caption, photo full-bleed,
discussion prompt, exercise, key takeaways, closing.

**Action:** either extend `slides/` to the twelve types, or replace it with the teaching deck
template and note that the deck is the canonical slide system. Recommend the latter —
maintaining two slide systems is how the type scale ended up with two answers.

---

# PART III — GAP: THE DESIGN SYSTEM IS SILENT

## §10 — GAP: no icon tokens exist

**Severity:** `visible` · **Difficulty:** `one-file`

The eight ratified icon constants have no token representation. Every consumer currently has
to remember them, which is exactly the condition that produced the original drift.

**Action:** add to `tokens/spacing.css` or a new `tokens/icons.css`:

```css
:root {
  --icon-canvas: 24;             /* units, the drawing grid */
  --icon-live-area: 20;          /* units, 2u padding every side */
  --icon-stroke: 2;              /* units — the one weight */
  --icon-stroke-print: 2.5;      /* Diploma print cut only */
  --icon-cap: butt;
  --icon-join: miter;
  --icon-miterlimit: 6;
  --icon-radius: 0;              /* hard corners in every glyph */
  --icon-accent: var(--orange-300);
  --icon-size-sm: 20px;
  --icon-size-md: 24px;
  --icon-size-lg: 32px;
  --icon-size-xl: 48px;
  --touch-target-min: 44px;
  --print-type-floor: 12pt;
}
```

**One caveat on `--icon-stroke`:** in the shipped sprite this rides a *separate* custom property
`--mfb-icon-stroke` set at the `<svg>` element, not at `:root`. That is deliberate — see §14.
If the token is added at `:root`, it must not be the property the sprite reads, or the print
cut stops working.

---

## §11 — GAP: no `Icon` component

**Severity:** `visible` · **Difficulty:** `one-file`

`components/core/` holds eight components (Avatar, Badge, Button, Card, Highlight, IconButton,
ParallelogramFrame, StatBlock). There is no `Icon`.

The asset stack ships `icons/Icon.jsx` with `name`, `size`, `color`, `active`, `print` and
`label` props, plus an exported `MFB_ICON_NAMES` array so a bad name fails at build rather
than rendering nothing.

**Action:** add `components/core/Icon.jsx`, `Icon.d.ts`, `Icon.prompt.md` following the
existing convention. Register it in `_ds_manifest.json` under `components`. Add
`assets/icons/mfb-icons.svg` and `mfb-icons.json`.

**Load-order note for the prompt.md:** the sprite must be present in the document before any
`Icon` renders. This is the one component with a document-level prerequisite, and it should say so.

---

## §12 — GAP: the two token vocabularies are not reconciled

**Severity:** `breaks` · **Difficulty:** `across-products`

This is the most structurally significant finding in the audit.

Two complete token vocabularies exist for the same brand, with the same hex values:

| Concept | Design system | Micrographics / print |
|---|---|---|
| Primary purple | `--purple-300` | `--color-purple` |
| Deep purple | `--purple-400` | `--color-purple-dark` |
| Light purple | `--purple-200` | `--color-purple-light` |
| — | *(none)* | `--color-purple-deep: #673C95` |
| Accent orange | `--orange-300` | `--color-orange` |
| Amber | `--orange-200` | `--color-amber` |
| Lilac | `--gray-300` | `--color-lilac` |
| Caption gray | `--gray-700` | `--color-caption` |
| Body text | `--text-strong` / `--text-body` | `--color-text` |
| Font family | `--font-sans` | `--ts-font-family` |

Note `--color-purple-deep: #673C95` exists **only** in the print vocabulary and has no design
system equivalent. It is used for definition-card backgrounds. That is a colour in production
that the design system does not know about.

`micrographics/tokens.css` states its own provenance:

> Mirrors the brand section of `apps/web/public/styles/print.css` §1 (DESIGN TOKENS). Keep in
> sync with that file — it is the source of truth for the PDFs.

So there are **two declared sources of truth**: `print.css` for PDFs, and the design system for
everything else. "Keep in sync" is a manual instruction, which is what "drift" means before it
happens.

**Action:** this is a discovery-call decision, not a unilateral fix. Options:
1. **Alias:** print tokens become `var()` references to the design system tokens. One source,
   two names, no drift possible. Requires `print.css` to load the design system tokens.
2. **Generate:** `print.css` §1 is generated from the design system tokens at build time.
   Cleanest, requires pipeline work from Benoit.
3. **Document the mapping** and accept two names. Cheapest, and leaves the drift risk in place.

Recommend 2, fall back to 1. Add `#673C95` to the design system's purple ramp either way.

---

## §13 — GAP: the WeasyPrint envelope is not in the design system guide

**Severity:** `breaks` · **Difficulty:** `one-file`

The constraints in §2–§4 are documented in `micrographics/README.md` — a file a designer
reading the design system guide has no reason to open. The guide's Visual Foundations section
discusses backgrounds, corners, borders and motion, and says nothing about what CSS survives
the print renderer.

Consequence: anything authored from the guide alone is unrenderable in the Diploma. I did
exactly this, twice (§2).

**Action:** add a **Print & publishing** section to `readme.md` carrying the envelope, the
scoping rule, the `data-t` contract, the `pt` convention, and a pointer to
`micrographics/README.md` for the full authoring contract. Add the same to `SKILL.md`'s Quick
orientation — it is as load-bearing as the colour and type lines already there.

---

## §14 — GAP: nothing documents how the sprite's stroke override works

**Severity:** `visible` · **Difficulty:** `one-file`

Two hard-won implementation details exist nowhere in the design system:

**1. Stroke must ride a custom property inside the symbol.**
The sprite sets `style="stroke-width:var(--mfb-icon-stroke, 2)"` on each `<symbol>`, not a
`stroke-width` attribute. An attribute on the symbol beats one set on the outer `<svg>`, so the
`print` flag silently fails to reach inside a `<use>` — which is precisely the bug the asset
stack shipped and then fixed.

**2. `currentColor` does not cross the sprite host boundary.**
A sprite loaded into an out-of-flow host div resolves `currentColor` against *the host's*
inherited colour, not the `<use>` site. Every icon in the teaching deck rendered white-on-white
because of this. Two safe patterns: set colour explicitly at the `<use>` site, or inline the
geometry for fixed-palette documents.

**Action:** put both in `Icon.prompt.md` and in the Print & publishing section. These are not
trivia — they are the two failure modes that actually occurred, and both are invisible in
source review because the markup looks correct.

---

## §15 — GAP: Tier 2 elements have no representation

**Severity:** `visible` · **Difficulty:** `one-product`

Sixteen named elements exist in the asset stack across five families. The design system has
two of them as components (`Highlight`, `ParallelogramFrame` — both correct and used unchanged)
and is silent on the other fourteen.

| Family | Elements | In design system |
|---|---|---|
| Arrows & connectors | `arrow-straight`, `connector-elbow`, `connector-dashed`, `node-dot` | ✗ |
| Rules & dividers | `rule-hairline`, `rule-strong`, `rule-slanted` | ✗ |
| Frames & cuts | `parallelogram-frame`, `parallelogram-stack`, `bracket`, `diagonal-cut` | 1 of 4 |
| Emphasis | `highlighter`, `stat-tick`, `list-marker` | 1 of 3 |
| Textures | `screen-dots`, `screen-fade`, `hatch-slant`, `halftone-portrait` | ✗ |

Notes on specific items:
- `ParallelogramFrame.jsx` takes `angle = "var(--skew-angle)"`, so it inherits whatever §5
  resolves to. Correct by construction.
- `Highlight.jsx` hard-codes the canonical geometry (`-0.12em`, `0.14em`, `skewY(-1.4deg)`) and
  matches the asset stack exactly. **No change needed.**
- `parallelogram-stack` is a composition of `ParallelogramFrame`, not a new component — it may
  be a documented pattern rather than code.
- `halftone-portrait` requires photographic input and is an image treatment, not CSS. It
  belongs in the guide, not in `components/`.
- The textures (`screen-dots`, `screen-fade`, `hatch-slant`) are `repeating-linear-gradient`
  patterns and are print-safe. They are also what makes multi-series graphics survive
  greyscale, which is a Diploma requirement.

**Action:** add the arrow/connector set and the three rules as components; document the
textures as CSS recipes in `guidelines/`; document `parallelogram-stack` as a pattern.

---

## §16 — GAP: Tier 3 graphics have no representation beyond micrographics

**Severity:** `visible` · **Difficulty:** `one-product`

The design system's `micrographics/` folder is a **pipeline**, holding one worked example
(`the-halving`). It is not a graphics library.

The asset stack defines twelve patterns in four groups:

| Group | Patterns |
|---|---|
| A · Teaching diagrams | `comparison-pair`, `layer-stack`, `timeline`, `process-flow` |
| B · Data charts | `bar-chart`, `proportion-bar`, `big-stat`, `trend-line` |
| C · Micrographics | `callout`, `definition`, `key-takeaways` |
| D · Screen only | `map` |

Group C matches the design system's micrographics concept exactly and should land there as
three library entries. Groups A and B are the Diploma's working diagram set. Group D must
never reach print (maps date faster than the revision cycle).

Four authoring rules go with them, and none are currently in the design system:
1. Label every value **on the mark**, not in a legend — legends fail first when photocopied.
2. Separate series by **hatch, not hue** — every multi-series graphic must survive greyscale.
3. **No pie charts** — they cannot be labelled reliably in print; `proportion-bar` replaces them.
4. **Data is editable, look is not** — a value and its label are neighbours in the markup so a
   non-designer can change one without breaking the other.

A fifth rule follows from §3: **every text node carries `data-t`.**

**Action:** create `micrographics/<slug>/` entries for group C first (they match the existing
convention and are needed by the curriculum). Groups A and B need the flexbox rewrite from §2
before they can land. Add the five rules to the guide.

---

## §17 — GAP: Tier 4 layouts have no representation

**Severity:** `cosmetic` · **Difficulty:** `one-product`

Eleven skeletons exist in the asset stack; the design system has `ui_kits/website/` (a site
recreation, not a layout skeleton) and `slides/`.

| Group | Skeletons | Frame |
|---|---|---|
| Print | `chapter-opener`, `teaching-page`, `exercise-page` | A4 and Legal, flexible |
| Web | `landing-hero`, `content-page`, `directory-index` | Max 1280px content width |
| App | `app-home`, `app-lesson`, `app-progress` | 390px, mobile first |
| Shared chrome | `web-header`, `doc-sidebar`, `app-tab-bar` | Cross-surface |

**Action:** add a `layouts/` directory following the `slides/` convention (`@dsCard` markers so
they surface as cards). Lower priority than §10–§16 — layouts are the tier most likely to be
regenerated per project anyway.

---

## §18 — GAP: no Tier 5 production templates

**Severity:** `visible` · **Difficulty:** `one-product`

The design system ships `slides/` and `ui_kits/website/`. The asset stack's five production
templates are absent:

| Template | Surface | Constraint |
|---|---|---|
| Diploma chapter | Print | 12pt floor, greyscale passes, **needs flexbox rewrite (§2)** |
| Community flier | Print | One page one side, any office printer |
| Landing page | Web | Needs real photography |
| Lesson flow | App | 390px, 44px targets, has behaviour not pages |
| Teaching deck | Slides | 1920×1080, 26px minimum, 18 slides / 12 types |

**Action:** add a `templates/` directory. Rewrite the Diploma chapter for the print envelope
first — it is the one most likely to be used and currently the one most likely to fail.

---

## §19 — GAP: surface constraints are undocumented

**Severity:** `cosmetic` · **Difficulty:** `one-file`

The design system does not state what each build target may and may not use. The asset stack does:

| Surface | Frame | Notable exclusions |
|---|---|---|
| Website | Max 1280px content width | — |
| Programs (print) | A4 and Legal, flexible | No maps; 12pt floor; 2.5u stroke cut |
| App | Mobile first, 44px targets | — |

The important content here is the *exclusions*, not the frames. "No maps in print" and "12pt
on any line a learner reads" are decisions someone will otherwise reverse without knowing they
were made.

**Action:** add a Surfaces section to `readme.md`.

---

## §20 — GAP: the exclusions are not recorded anywhere

**Severity:** `visible` · **Difficulty:** `one-file`

Five things the asset stack deliberately does **not** do. Each was a decision with a reason,
and each is something a future contributor will attempt in good faith:

1. **No badge system.** Badges were treated as graphics, not as a separate achievement
   taxonomy. *(The design system already correctly documents that node badges are retired, the
   community badge is an example only, and a Certified Educator badge is pending — that section
   needs no change. It should simply also say that no badge work is in the asset stack.)*
2. **No 16px icon cut.** Dropped on evidence: no MFB surface places icons inline in body text
   or dense tables. If one appears, draw a thinner cut for that icon alone as `<concept>-16.svg`.
3. **No second bar, anywhere.** The active state is an orange colour change. A bar under an
   icon or nav item competes with the highlighter, which is the only bar the brand owns. This
   follows directly from the guide's existing highlighter rule and should be stated as its
   corollary.
4. **No Lucide at runtime.** See §6.
5. **No maps in print.** Online only — they date faster than the print revision cycle.

**Action:** add an Exclusions section to `readme.md`, immediately after Iconography. The
exclusions are as load-bearing as the rules; a guide that records only what to do gets quietly
undone.

---

## §21 — GAP: no icon contribution checklist

**Severity:** `cosmetic` · **Difficulty:** `one-file`

The asset stack ships nine checks, eight machine-testable by design so review time goes on the
ninth. The design system has no contribution criteria for any asset type.

1. `viewBox="0 0 24 24"`, no `width`/`height` attributes on the file.
2. `stroke-width="2"` — or exactly `2.5` on a `-print` cut, nothing else.
3. `stroke-linecap="butt"`. No round caps, no square projection.
4. `stroke-linejoin="miter"` with `stroke-miterlimit="6"`.
5. No corner radius anywhere — no `rx`, no `ry`, no arc standing in for a corner.
6. `stroke="currentColor"`. No hard-coded hex on a Tier 1 icon.
7. Nothing crosses the 20×20u live area; 2u padding on every side.
8. Concept-first kebab-case name, singular, no reference to where it is used.
9. **(Human)** Reads at 20px on white and on purple, and does not stand out in a row of ten.

Plus the naming rule: concept first, kebab-case, singular, ASCII. `key-cold-storage`, not
`cold-storage-key`, not `wallets`, never `sidebar-icon`. Modifiers are suffixes (`-print`,
`-filled`, `-alt`); brand carriers are prefixed `brand-`.

**Action:** add `CONTRIBUTING.md` to the design system root, or a `guidelines/contributing.html`
card.

---

## §22 — GAP: the tier rule itself is not stated

**Severity:** `visible` · **Difficulty:** `one-file`

The single most useful sentence in the asset stack has no equivalent in the design system:

> **A tier may only use what the tiers below it define.**

A template cannot invent a diagram. A diagram cannot invent an arrow. An arrow cannot invent a
stroke weight. Everything traces to Tier 1.

The practical consequence — **producing an asset means filling a template, never designing from
scratch** — is what keeps assets made months apart consistent. And its corollary is the useful
diagnostic: if something has no home in the stack, it is either a variant of an existing
template or a new template, and deciding which is the work.

**Action:** add a Hierarchy section to `readme.md` near the top, and the one-line rule to
`SKILL.md`'s Quick orientation. Of everything on this list, this is the cheapest entry and
plausibly the highest-value.

---

# PART IV — CONFIRMED CORRECT (no action)

Recorded so a future audit does not re-derive them.

| Item | Status |
|---|---|
| `Highlight.jsx` geometry | `-0.12em` / `0.14em` / `skewY(-1.4deg)` — matches the asset stack exactly |
| Highlighter usage rule | "under one word, never above or beside, never restyled" — correct and load-bearing |
| Purple ramp | `#2B1C58` / `#422C70` / `#5E378E` — used unchanged throughout |
| `--orange-300 #F7941F` | Correct |
| Cool gray ramp | `gray-100`→`gray-800`, slightly blue — correct and deliberate |
| `--paper #F6F6F8` | Correct |
| `--radius-lg: 12px` | Correct for surfaces. The asset stack's 0u rule applies to *glyphs* only — no conflict |
| Two-background-colours-max rule | Followed by every template |
| "Orange never a large background fill" | Followed throughout |
| IBM Plex Sans, max two weights | Followed |
| Retired Node terminology | Correctly documented; asset stack follows it |
| `ParallelogramFrame.jsx` | Takes `angle` from `--skew-angle`, so it self-corrects on §5 |
| No gradients, no noise, flat surfaces | Followed |
| Logo never redrawn | Followed — `brand-bitcoin` places the B-tag asset rather than drawing a glyph |
| `the-halving` micrographic | A correct worked example; the `data-t` pattern in it is the one to document |

---

# PART V — ORDER OF WORK

Derived from severity × difficulty. Each row's action is already decided by its cell.

## Immediate — before anything else consumes the stack

| # | Item | Why first |
|---|---|---|
| §1 | Fix `--orange-400` in the reference sheet | Wrong value in the document meant to survive file loss |
| §2 | Rewrite Diploma chapter as flexbox | Currently unrenderable in the real pipeline |
| §3 | Add `data-t` to Tier 3 graphics | Currently ships English-only into a multilingual book |
| §22 | Add the tier rule to the guide | One line, highest value on the list |

## Next — the design system's own staleness

| # | Item | Note |
|---|---|---|
| §6 | Replace the Lucide section | Blocks nothing, but every day it stays both sets get used |
| §13 | Add Print & publishing to the guide | Prevents the §2 error recurring |
| §14 | Document the sprite failure modes | Two real bugs, both invisible in source review |
| §10 | Add icon tokens | One file |
| §11 | Add the `Icon` component | One file plus manifest registration |
| §20 | Add the Exclusions section | One file |
| §21 | Add the contribution checklist | One file |

## Hold for the November discovery call

| # | Item | Question |
|---|---|---|
| §5 | The slant: 13° or 19° | Discovery Q02. Propagates instantly; do not fix unilaterally |
| §12 | Reconcile the two token vocabularies | Needs Benoit — pipeline work, not a design decision |
| §7 | Pick one black | Cheap but touches every component |

## Scoped work, after the above

| # | Item | Size |
|---|---|---|
| §4 | Pipeline-shaped output for Tier 3 | Real work — new files per slug, not a reformat |
| §15 | Tier 2 elements as components | 14 items, some are patterns not code |
| §16 | Tier 3 graphics into the library | Group C first; A and B need §2 done |
| §18 | Tier 5 templates | Diploma chapter needs §2 first |
| §8 | Reconcile the type scales | Add tokens rather than replacing |
| §9 | Extend or replace `slides/` | Recommend replace — two slide systems is how §8 happened |
| §17 | Tier 4 layouts | Lowest priority; regenerated per project anyway |

---

# PART VI — WHAT THIS AUDIT COULD NOT CHECK

Stated so the gaps are known rather than assumed closed.

1. **Figma was read on 19 August 2026 and holds no UI icon set.** Every icon value in the asset
   stack is therefore a *promotion candidate* into the source, not a replication of it. Nothing
   contradicts Figma, but nothing has been accepted into it either.

2. **`print.css` §1 was not read** — it is in the product repo, not the design system. It is
   declared the source of truth for PDFs (`micrographics/tokens.css` header), so §12 cannot be
   fully specified without it.

3. **`docs/TECHNICAL.md` §2–§4 and `docs/education-micrographics-guide.md` were not read** —
   same repo. They govern how the micrographic block is stored, rendered and translated.

4. **The live products were not audited** — slides, websites, app, Diploma print, social,
   educator materials. That is the November call's scope, and it needs the three departmental
   inventories in the room.

5. **`ui_kits/website/` was not compared** against the current live site.

6. **Paper size is unconfirmed.** Templates are built flexible (A4 for Europe, Legal for North
   America). A single global size can be absorbed later without redrawing.

7. **Three curriculum icons remain wrong in print** — `callout`, `definition`,
   `key-takeaways` ship in the current Diploma with round caps, a 6px radius and a 3px stroke
   on a 48 grid. Re-cut versions are committed. They land at the next curriculum revision.

---

*End of correction list. 22 findings: 4 asset-stack errors, 5 stale design-system entries,
13 gaps. Harmonisation owned by Patrick; asset work by Pablo; implementation requires Benoit
(app, publishing) and Alexandre (websites).*
