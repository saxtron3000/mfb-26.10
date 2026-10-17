Build a My First Bitcoin Diploma micrographic.

This prompt does not apply to an asset of type `EXTERNAL`. An EXTERNAL asset has its approved .jpg added directly through Sanity; do not create a micrographic, editable source, or package for it.

What it should show: [describe the content, the pieces, and any exact numbers or labels]

Use the supplied asset brief as the binding content contract. Preserve its
required elements, reading order, exact strings, exclusions, safety guidance,
localization needs, caption, and alt-text requirements. If an essential fact,
label, number, URL, or requirement is missing or conflicts with another
supplied source, identify the gap rather than inventing it.

Make every essential visual element editable HTML, CSS, or inline SVG; do not
use raster images as diagram content. Do not rely on colour alone—also use
shape, position, line style, pattern, or text—and allow translated text to
grow. Never include a real seed phrase, private key, payable address, private
learner data, balance, or transaction. Do not imply investment returns,
guaranteed outcomes, risk-free self-custody, or universal legal conclusions.

Before returning, verify the required elements and relationships, factual
accuracy, readable 458px layout, print safety, and grayscale legibility.

First, choose two things for me and state them at the top of your reply:
- a short, descriptive title (a few words, e.g. "The Bitcoin Halving")
- a slug derived from the title — lowercase, words joined by single hyphens,
  letters and digits only (e.g. the-halving). Use it everywhere <slug> appears.

Then produce four files: micrographic.html, micrographic.css, a meta.json
({"bundleVersion":1, "title":"…", "slug":"<slug>", "altText":"one plain
sentence describing the visual", "caption":"", "editableText":true}), and a
self-contained preview.html.

Follow these rules exactly:
1. Wrap everything in a single root element <div class="mg-<slug>">, and
   prefix EVERY CSS selector with .mg-<slug> so the styles can't leak
   into the rest of the book.
2. Tag every piece of translatable text with a data-t="key" attribute on the
   element that directly contains it. Keys are short, lowercase, letters /
   numbers / hyphens only, unique, and never nested inside each other. Do NOT
   tag pure numbers or symbols that are the same in every language.
3. Print-safe CSS only: use pt, mm, em, or % sizes; flexbox is fine with
   explicit sizes. No CSS grid, no vh/vw, no rem, no position: fixed/sticky,
   no @import, no JavaScript, no external images or fonts.
4. Use the My First Bitcoin brand tokens with fallbacks: var(--color-purple, #422C70),
   var(--color-orange, #F7941F), var(--color-text, #1a1a1a),
   var(--color-caption, #6C6C7D), and
   font-family: var(--ts-font-family, "IBM Plex Sans"), sans-serif.
5. Design for a narrow book page: the root should be width: 100% and look
   good around 458px wide (A5 book content width).
6. Inline SVG is allowed, but keep SVG attribute names correctly capitalized
   (viewBox, not viewbox).
7. Also generate a self-contained preview.html whose first line is
   <!-- @dsCard group="Micrographics" --> that inlines the brand tokens, the
   CSS, and the HTML fragment inside a 458px frame. Inline the IBM Plex Sans font
   as a @font-face data URI (copy the block from an existing preview.html) so the
   card shows the brand font in Claude Design, where font CDNs are blocked.
8. Return the four files as separate fenced code blocks, each preceded by
   its filename (e.g. micrographic.html), in this order: html, css, json, preview.html.
9. Do not tag brand-specific terms that are the same across languages —
   "BTC", "sat", "bitcoin", and pure symbols (→, %, ×) stay untagged.
10. Design principles: use --color-orange only as an accent or to highlight
    the single most important element. Use --color-purple for primary structure.
    Keep text minimal — a micrographic should be scannable in under 10 seconds.
    Aim for no more than 7 translatable text elements total.
11. Leave the caption field empty ("caption":"") unless the content
    specifically requires a clarifying note below the visual.
