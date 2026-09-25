# My First Bitcoin Diploma — Illustration Style Guide

**Purpose:** the complete production brief for illustrations, diagrams, data graphics and tables in the Bitcoin Diploma.

## 1. Visual direction

**Working name: MFB Angular Editorial Illustration.**

Create flat, print-safe vector education artwork with hard geometric structure, warm simplified people, purple-led composition, controlled orange emphasis and a consistent 13° parallelogram language.

The work should feel clear, calm, practical, human, professional, independent and grassroots-but-polished. It should feel like a well-made open-source textbook, not a fintech campaign.

### Never make it look like

- A crypto trading advertisement: gold coin piles, rockets, moons, laser eyes, price hype or generic blockchain cubes.
- Corporate Memphis: noodle arms, giant hands, tiny heads, blob bodies, floating UI screens or fake-startup cheerfulness.
- Glossy 3D, gradients, glassmorphism, glow, soft shadows, airbrush rendering or generic AI stock art.
- A children’s cartoon, mascot system or image with no learning purpose.

## 2. Decision order

1. `CHARACTERS.md` controls the identity and reuse of the recurring cast.
2. The MFB Assets Style Guide controls icons, graphic patterns and print constraints.
3. The MFB Design System and `brand-spec.md` control colour, typography and voice.
4. This file translates those source systems into illustration-production rules.

Fill an existing visual pattern/template before inventing a new one. If a request does not fit, propose a reusable variant—not a one-off visual treatment.

### Asset hierarchy

An asset may use only what the tiers below it define. Build by filling a template, not by designing a one-off treatment.

| Tier | Defines | Diploma use |
|---|---|---|
| 1. Icons | Atomic marks and stroke language | First-party MFB icons only |
| 2. Elements | Connectors, frames, rules, emphasis and textures | Diagram primitives |
| 3. Graphics (aka Micrographics) | Reusable teaching-diagram and chart patterns | One clear learning point |
| 4. Layouts | Content placement, rhythm and shared chrome | Page or screen skeleton |
| 5. Templates | Finished, fillable surfaces | A specific learner-facing asset |

If a request has no home in this stack, decide whether it is a variant of an existing template or a new reusable template before producing it.

## 3. Palette

| Role | Hex | Use |
|---|---:|---|
| Primary purple | `#422C70` | Main structure, headings, frames/shapes |
| Deep purple | `#2B1C58` | Contrast, deep fields, strong detail |
| Light purple | `#5E378E` | Secondary structure |
| Orange | `#F7941F` | One focal point, highlighter, ₿ symbol |
| Strong orange | `#EF7B00` | Active/strong emphasis only |
| Paper | `#F6F6F8` | Preferred quiet surface |
| Cool divider | `#D8D8E7` | Hairlines/separators |
| Body neutral | `#25252B` | Light-surface text and neutral structure |

### Complete brand tokens and implementation

`brand.css` is generated from `tokens.json`; do not edit it by hand. Its variables are the canonical implementation names. Use the values below when a production asset, template or CSS micrographic needs a token that is not in the abbreviated working palette above.

| CSS variable | Hex/value | Brand use |
|---|---|---|
| `--mfb-purple-300` | `#422C70` | Primary purple; hero colour, backgrounds and headers |
| `--mfb-purple-400` | `#2B1C58` | Dark-purple contrast and footer backgrounds |
| `--mfb-purple-200` | `#5E378E` | Light-purple accent, secondary headings and gradient endpoint |
| `--mfb-orange-300` | `#F7941F` | Primary orange; CTAs, links, highlights and the ₿ symbol |
| `--mfb-orange-400` | `#EF7B00` | Dark-orange hover/active state and strong emphasis |
| `--mfb-orange-200` | `#FBB040` | Soft highlight and secondary orange accent |
| `--mfb-black` | `#000000` | Primary black for high-contrast text and bold headlines where required |
| `--mfb-white` | `#FFFFFF` | Primary white background and text on dark surfaces |
| `--mfb-gray-900` | `#25252B` | Near-black body text on light surfaces |
| `--mfb-gray-800` | `#4F4F5D` | Secondary text and subtle headings |
| `--mfb-gray-700` | `#6C6C7D` | Muted text and placeholders |
| `--mfb-gray-600` | `#88889C` | Disabled text and borders |
| `--mfb-gray-500` | `#ADADBE` | Subtle borders and dividers |
| `--mfb-gray-400` | `#C0C0D0` | Light borders and inactive elements |
| `--mfb-gray-300` | `#D8D8E7` | Card borders and separators |
| `--mfb-gray-200` | `#EAEAF4` | Light backgrounds and alternating rows |
| `--mfb-gray-100` | `#F3F3FA` | Page background and subtle tint |

The canonical brand gradient is `--mfb-gradient-brand`: `linear-gradient(135deg, #2B1C58 0%, #5E378E 100%)`. Its direction is always 135° (top-left to bottom-right). It is the signature brand treatment for heroes, headers and slides. It is not permitted inside flat, print-safe Diploma illustrations or graphics, where the no-gradients rule above takes precedence.

Use `--mfb-font-heading` and `--mfb-font-body` for `"IBM Plex Sans", Arial, sans-serif`; `--mfb-font-sans` is the same alias. Use `--mfb-font-mono` (`"IBM Plex Mono", monospace`) only for code, data and technical content. The supporting supergraphic tokens are `--sg-angle-base: 13deg`, `--sg-angle-alt: 24deg`, `--sg-aspect: 1.5`, `--sg-logo-icon-h: 40px` and `--sg-base-h-ratio: 2`.

### Colour rules

- Purple carries identity. Orange is emphasis, never a large background or dominant fill.
- At the broader brand level, full backgrounds are purple gradient or white only; use no other colour as a full background.
- Use two brand background colours maximum per asset—normally purple plus white/paper.
- Use cool grays only. Colour may not be the sole way to distinguish data.
- Use a controlled, stylised brand-tone skin palette: pale lilac, muted orange-tan, deep purple-brown and cool gray. Do not render people photorealistically.
- Keep Diploma illustrations and graphics flat; do not use gradients.
- On dark or purple-gradient surfaces, text is always white. On white or gray-100 surfaces, use gray-900 rather than pure black for ordinary text; purple headings and orange CTAs provide the standard contrast pair.
- Links are orange and receive an underline on hover. Orange is not a background fill.

## 4. Type and copy inside assets

- **IBM Plex Sans only.** 400 body, 500 headings/big numerals, 600 controlled emphasis.
- Use short, literal labels and strong left alignment.
- Display headings use Title Case; explanatory copy uses sentence case.
- Light surfaces use cool near-black; purple surfaces use white.
- Learner-facing type is at least **12pt**. Labels/folios only may be 8–10pt.
- The orange highlighter underlines one word in a heading. It sits below the glyphs and is the brand’s only bar; do not add decorative underlines elsewhere.

### Brand type scale

The following print/large-format scale is available through the matching `--mfb-size-<level>` CSS variables. Scale it proportionally for screen.

| Level / variable | Size | Treatment |
|---|---:|---|
| h1 / `--mfb-size-h1` | 70px | IBM Plex Sans Medium; line-height 1 |
| h2 / `--mfb-size-h2` | 58px | IBM Plex Sans Medium; line-height 1 |
| h3 / `--mfb-size-h3` | 48px | IBM Plex Sans Medium; line-height 1 |
| h4 / `--mfb-size-h4` | 40px | IBM Plex Sans Medium; line-height 1 |
| h5 / `--mfb-size-h5` | 36px | IBM Plex Sans Medium; line-height 1.1 |
| h6 / `--mfb-size-h6` | 32px | IBM Plex Sans Medium; line-height 1.1 |
| body / `--mfb-size-body` | 18px | IBM Plex Sans Regular; line-height 1.2 |
| label / `--mfb-size-label` | 22px | IBM Plex Sans Regular; line-height 1.2 |
| quote / `--mfb-size-quote` | 40px | IBM Plex Sans Medium; line-height 1 |

Use 400 for body text and labels, 500 for headings, H1–H6 and quotes, and 600 for strong emphasis and CTAs. Do not use more than two font weights in one content piece.

### Brand supergraphics

- The highlighter applies to one key word—not a full phrase—per heading, on purple or white. Its CSS treatment is `background-image: linear-gradient(transparent 60%, var(--mfb-orange-300) 60%)`.
- Parallelogram containers are sparing decorative accents behind statistics or section labels: `transform: skewX(-10deg)`, with child content counter-skewed using `transform: skewX(10deg)`.
- When used in wider brand communications, halftone portraits are a photo-editing effect, not CSS: duotone purple shadows `#45265B` with `#F7E6FF` highlights for cutouts, or an orange background. Reserve them for speaker/team sections.
- Use official logo files only. Maintain clear space equal to the height of the ₿ symbol; use the white variant on dark or gradient backgrounds and the dark variant on light backgrounds. The ₿ itself is Unicode `₿` in `#F7941F`, never generic coin imagery.
- Brand photography shows real people in real educational settings, with warm natural lighting and diverse representation. It remains separate from the flat Diploma illustration system unless a photography asset is explicitly requested.

## 5. Geometry, line and texture

### The 13° rule

- Use **13°** for parallelogram frames, diagonal cuts, slanted rules and hatch axes.
- Use one structural slant angle per composition. Never add arbitrary rotation.
- Frames lean; their contents counter-skew and stay upright. Faces, icons and text do not lean.

### Construction

- Prefer rectangles, parallelograms, brackets, diagonal cuts, straight connectors, right-angle elbows and filled node dots.
- Maintain an even monoline feel. Follow the icon family’s hard corners, butt caps and miter joins proportionally in illustrations.
- Use cool-gray hairlines for quiet separation; use a purple strong rule only for a meaningful section break.
- Curves are permitted only for legible human/object anatomy, never as decoration.
- Preserve generous negative space and remove non-teaching detail.

### Icon and connector construction

- Use the first-party MFB icon set; do not mix in Lucide or redraw the logo/B-tag.
- Icons use a `24 × 24u` canvas with a `20 × 20u` live area and `2u` clear padding on every side. Their standard stroke is `2u`; use the dedicated `2.5u` print cut for Diploma print.
- Icon strokes use butt caps, miter joins with a miter limit of `6`, and hard corners. Use `currentColor`, not a hard-coded icon colour.
- An arrow uses an open chevron head, never a filled triangle: `7u` per head side and a `90°` included angle. Connector elbows turn only at `90°`; optional/inferred relationships use a `6 5` dash in gray-500.
- Node dots are filled `12u` circles. A hollow dot reads as an error at this stroke weight.

### Texture/depth

Permitted: screen dots, screen fade, 13° hatch and approved halftone portrait treatment. Use hatch to distinguish multi-series data in greyscale.

Avoid: blur, glow, noise, watercolour, glass, airbrush shading, photoreal lighting and heavy shadows.

## 6. People and props

Use the approved recurring cast in `CHARACTERS.md` whenever people appear.

- They are fixed people, not interchangeable demographic symbols.
- Use realistic, slightly simplified proportions and minimal calm faces.
- Preserve the same face construction, hands, outline weight, clothing-detail level and flat colour treatment in every asset.
- Clothing is built from simple angular planes, not detailed fashion illustration.
- The older learner is active and capable, never a stereotype.
- Only show people needed to teach the point; avoid decorative background crowds.

Preferred props: notebooks, printed guides, pencils, whiteboards, desks, payment devices, wallets, hardware wallets, keys, seed-phrase cards, simple network marks and classroom materials.

Use official MFB logo/B-tag assets if a mark is needed. Never redraw the logo.

## 7. Illustration recipes

### Human educational scene

1. State one learning point.
2. Select one to four named characters and a purposeful action.
3. Use white/paper as default; add one or two restrained purple structural shapes.
4. Use orange only for the key teaching cue.
5. Remove irrelevant props and background detail.

Good subjects: workshop discussion, custody practice, merchant payment, learner comparison and simple network explanation.

### Object/metaphor illustration

Use one direct relationship—key + wallet, checklist + seed phrase, guide + learner or lock + storage. Keep the same flat fills, outline logic and 13° structure as scenes.

### Chapter opener

May use a bolder purple field and one major subject with large negative space. It remains flat, direct and print-safe: no orange full bleed or dense text embedded in artwork.

## 8. Diagrams, data and tables

Use the existing graphic patterns first:

| Learning need | Pattern |
|---|---|
| Compare two concepts | Comparison pair |
| Explain components/levels | Layer stack |
| Explain chronology | Timeline |
| Explain sequence | Process flow |
| Compare quantities | Bar chart |
| Explain a share | Proportion bar |
| Make one numeric point | Big stat |
| Show change | Trend line |
| Flag/define/conclude | Callout, definition, key takeaways |

### Diagram rules

- Direct-label values on or beside the mark; never depend on a distant legend.
- Use open chevron arrowheads, straight paths and right-angle connectors.
- Use filled node dots for stops, junctions and timeline points.
- Pair hatch with colour for multiple series so the graphic survives photocopying.
- No pie charts; use a proportion bar.
- No maps in the printed Diploma.
- One chart communicates one point; avoid dashboard density.

At the layout level, use the appropriate skeleton in [`layouts/README.md`](layouts/README.md); do not make a print page imitate an app screen or a slide imitate a textbook page.

### Table rules

- White/paper ground, purple heading/section label, cool-gray hairline dividers.
- Left-align prose; right-align comparable numeric columns.
- Keep cells short and translation-safe.
- Orange marks one active value, warning or key takeaway only.
- No rainbow cells, heavy borders, pill overload or decorative icons in each row.

## 9. AI reference-image language

AI output is only a visual reference. Final diagrams need editable, live labels.

```text
Create a flat vector educational illustration for My First Bitcoin.

MFB Angular Editorial Illustration: hard geometric structure, 13-degree parallelogram accents, flat fills, restrained monoline outlines, realistic simplified proportions, minimal calm faces, angular clothing, clear negative space, mostly white or paper background, purple-led palette, cool-gray neutrals and small controlled orange emphasis. Professional, friendly, practical, independent and human, but not corporate.

Avoid gold Bitcoin coins, rockets, moons, laser eyes, trading hype, generic blockchain cubes, glossy 3D, gradients, glassmorphism, soft blob backgrounds, childish cartooning, Corporate Memphis proportions, heavy shadows and baked-in text.
```

For people, append: `Use the approved MFB Character Bible exactly. Preserve each named character’s face construction, hairstyle, clothing identity, hand style, outline weight, simplified realistic proportions and stylised brand-tone skin treatment.`

For a diagram, append: `Use direct placeholder labels, purple structure, cool-gray dividers, one orange emphasis point, straight/right-angle connectors, open arrowheads and hatch for greyscale. Rebuild labels as live translated text in production.`

## 10. Final-production requirements

Every asset requires editable source layers/groups, an appropriate export, a review PNG/PDF, alt text and a one-sentence educational purpose.

For a final Diploma HTML/CSS micrographic:

- Scope every CSS selector under `.mg-<slug>`.
- Use flexbox with explicit `pt`, `mm`, `%` or `em` sizing.
- Do not use CSS grid, JavaScript, `rem`, viewport units, sticky/fixed positioning or `@import`.
- Tag each translatable visible text node with `data-t="key"`; leave bare numerals/symbols outside the tag.
- Use editable values and live labels, with token references and hex fallbacks.

### Pre-flight checklist

- [ ] Asset teaches one clear thing and fits an existing pattern/template.
- [ ] Purple/white/paper lead; orange remains emphasis.
- [ ] Structural slant is exactly 13° and content stays upright.
- [ ] Characters match `CHARACTERS.md`.
- [ ] First-party MFB icons are used.
- [ ] Diagram works in greyscale and learner-facing type reaches 12pt.
- [ ] Final labels are live, editable and translatable.
- [ ] No crypto-hype, corporate-cartoon or glossy visual cliché remains.

## Source basis

Consolidated from the supplied `brand-spec.md`, `HANDOFF 1 - MFB Design System.md`, `HANDOFF 2 - MFB Assets Style Guide.md`, and the agreed direction for the six-person recurring Diploma cast.
