# Claude Design and Sanity asset prompt

## Purpose

Attach this file to every Claude Design request that turns a Bitcoin Diploma contract into a production asset. Every asset receives an approved reference JPG and its conformance report. Claude must create the editable, accessible source and upload-ready deliverables; it must not publish a reference image.

The complete entry in [08_assets.md](08_assets.md) is the instructional source of truth. The Claude Design System and its local authoring contract are the source of truth for brand and design-system choices. Where they conflict, stop and report the specific conflict for resolution.

## Folder routing

Claude consumes the approved reference materials from the ignored `assets-work/` area, but must create its editable production bundle only in the tracked `assets/diploma/` tree. Choose the destination from the asset entry's placement(s):

```text
assets/diploma/
├── student-guide/bd-v-000/  # Student Guide only
├── educator-guide/bd-v-000/ # Educator Guide only
└── shared/bd-v-000/         # reused by both guides
```

Use `shared/` only when the same approved implementation serves both guides. Keep any JPG, its JSON conformance report, prompt, model settings, and rejected concepts in `assets-work/`; they are references, not production deliverables. Do not create a final source bundle at `assets/diploma/bd-v-000/`: flat paths are handoff examples for publication pipelines, not the canonical editable-project location.

## How to read the asset entry

Every request supplies one complete row from [08_assets.md](08_assets.md). Claude must read every field before coding and use them as follows:

| Asset-index field | How Claude must use it |
|---|---|
| `ID` | Stable asset identifier. Use its lowercase form for the project directory and metadata; do not rename it. |
| `Suggested by` | Provenance only. It is not a design instruction, factual source, or approval state. |
| `Priority` | Planning importance (`Essential`, `Supporting`, or `Conditional`), not authorization to publish or lower review standards. A `Conditional` asset waits for its stated decision or verification. |
| `Type` | Required visual family: a structured comparison/template (`Table`), relationship/process/map/timeline (`Diagram`), or illustration/source/interface representation (`Image`). |
| `Page` and `Note` | Historic annotated-draft provenance. Do not use them as a current page layout, placement, or factual source. |
| `Placement` | Authoritative intended insertion: the guide, exact heading, and before/after/replace instruction. Use it to choose `student-guide`, `educator-guide`, or `shared`; preserve all listed placements in metadata. |
| `Line` | A one-based location snapshot only. Re-find the anchor through the named heading and nearby described text if it has shifted. |
| `Text–visual link` | The single instructional relationship the finished visual must make easier to understand than prose alone. It governs hierarchy and reading order. |
| `Design brief` | Binding content contract: required elements, exclusions, factual constraints, safety rules, caption, alt text, master/export instructions, and localization requirements. Implement every applicable instruction as editable, reviewable source. |
| `Format` | Expected visual form and layout role. Meet it in responsive and print layouts, or flag a justified conflict before changing it. |

Treat the row as one integrated specification. Preserve every qualifier, negative instruction, related-asset distinction, accessibility requirement, and editable/localizable element, even if it appears inside a field that seems informational.

## Complete prompt

```text
Build one production-ready My First Bitcoin Bitcoin Diploma visual that can be
reviewed and uploaded to Sanity through the approved publishing workflow.

Read all supplied material before designing or coding:
- Asset ID: [BD-V-000]
- Complete asset entry from workspace/08_assets.md: [paste entry]
- Complete section 7 reference specification from workspace/08_assets.md (the classification record and complete incorporated asset entry): [paste specification]
- Relevant section 8 shared-register entries from workspace/08_assets.md: [paste entries, if any]
- Approved low-resolution reference JPG: [attach]
- Matching conformance report: [attach bd-v-000-ref.json]
- Optional adjacent guide text: [paste only when it clarifies the lesson]
- Sanity asset/schema requirements, if supplied: [attach]

Source-of-truth order
1. The complete asset entry and section 7 specification control teaching
   intent, required elements, counts, composition, relationships, reading
   order, strings, prohibitions, safety, localization needs, and placement.
2. The Claude Design System controls visual tokens, components, typography,
   iconography, layout conventions, and brand expression.
3. Relevant section 8 entries control reusable actor, prop, symbol, interface,
   and notation definitions. Do not merge roles that the register keeps
   distinct.
4. The approved reference JPG guides
   spatial arrangement and visual treatment. Its conformance report identifies
   placement and deviations, but self-reported conformance is not proof.
   Check it against the section 7 specification.
5. The adjacent guide text may clarify context but does not override the asset
   entry.
6. Sanity schema or publishing requirements control the final deliverable
   format and metadata fields.

If these sources conflict, a section 7 `open` item blocks the required
structure, or an essential factual detail is absent, identify the specific
conflict or gap before implementing it. Do not invent facts, labels,
numbers, providers, URLs, legal claims, or safety claims. Do not trace, embed,
or publish the reference JPG. Reject or revise
the reference before implementation when `textPresentInImage` is not empty or
when `elementsAdded` is not empty and not justified.

Interpret every asset-index field before implementation: `ID` is the stable
identifier; `Suggested by` is provenance only; `Priority` signals planning
importance but never reduces review; `Type` selects the visual family; `Page`
and `Note` are historical provenance only; `Placement` is the current guide,
heading, and insertion authority; `Line` is only a potentially stale locator;
`Text–visual link` defines the one relationship to make clear; `Design brief`
is the binding required-elements, guardrails, caption, alt-text, factual,
safety, and localization contract; and `Format` defines the intended visual
form and layout role. Preserve every qualifier, prohibition, and related-asset
boundary across the editable source, metadata, export, and handoff.

First inspect the local design-system authoring instructions required by the
project (including micrographics/README.md and micrographics/tokens.css when
they are supplied). Start from the closest approved micrographic bundle rather
than a blank implementation. Apply the design system faithfully; do not copy
the reference image's provisional colors, fonts, or logo-like treatment.

Rebuild the visual as editable HTML, CSS, and inline SVG. All essential
diagram geometry, arrows, icons, interface shapes, labels, warnings, and data
must be editable code or editable SVG text—not pixels in an image. Use the
reference to preserve the useful composition and visual grammar, but simplify
or change it whenever necessary for accessibility, factual accuracy,
localization, responsive layout, or the design system.

Build every section 7 element in its stated composition and preserve each
specified relationship, reading order, string, prohibition, and safety
requirement. Use one clear teaching idea, an obvious reading order, and the
asset brief's specified roles and trade-offs. Keep people and local details culturally
replaceable. Distinguish color with shape, line style, pattern, position, and
text. Support grayscale printing, narrow book pages (about 458px content
width), phone-width display, desktop display, and A4 or US Letter output.
Allow translated text to grow and support future right-to-left adaptation
without redrawing the visual.

Safety and accuracy rules
- Preserve every prohibition and qualification in the asset entry.
- Never include a real seed phrase, private key, payable address, private
  learner data, learner balance, or transaction.
- Mark fictional interfaces, sample QR codes, and non-payable examples as the
  asset brief requires.
- Do not imply investment returns, guaranteed outcomes, risk-free
  self-custody, inevitable adoption, or a universal legal or local conclusion.
- Do not turn a named wallet, exchange, service, or local resource into a
  global recommendation.
- Cross-check every visible fact, number, date, URL, QR code, or interface
  detail against the supplied source before including it.

Implementation rules
1. Choose and state a short title and a lowercase hyphenated slug at the top
   of the response.
2. Produce `micrographic.html` with one root `<div class="mg-<slug>">`.
3. Produce `micrographic.css` with every selector prefixed `.mg-<slug>`.
4. Produce `meta.json` containing at least `bundleVersion`, `title`, `slug`,
   `altText`, `caption`, `assetId`, `sourceGuide`, `editableText: true`, and
   any required Sanity fields supplied in the schema.
5. Produce `preview.html`, self-contained and using the design-system preview
   conventions. It must show the graphic in a 458px review frame.
6. Tag each translatable text element with a unique, non-nested
   `data-t="key"` attribute. Do not tag universal pure numbers or symbols.
7. Use print-safe CSS: pt, mm, em, or %, flexbox with explicit sizes where
   needed; no CSS grid, vh/vw, rem, fixed/sticky positioning, @import,
   JavaScript, external images, or external fonts.
8. Use inline SVG with correct attribute capitalization. Keep icons and
   geometric relationships editable.
9. Provide `alt-text.md` with final alt text, a concise text equivalent for
   any complex diagram, and the final caption where the asset brief requires
   one.
10. Provide `README.md` recording the asset ID, source-brief revision,
    section 7 specification revision, relevant section 8 entries, reference
    file paths when used, conformance-report deviations when used, factual
    sources, production date, responsive and grayscale checks, reviewer
    status, and any unresolved judgment calls.

Sanity-ready deliverables
Create the source bundle in the appropriate tracked project folder:
`assets/diploma/<student-guide|educator-guide|shared>/bd-v-000/`.

Read the supplied asset entry before choosing this folder. If it has placements in both guides, use `shared/`; otherwise use the guide named in its placement. Do not move or copy the working reference files into the production bundle.

Create a production export only in the file type, dimensions, and metadata
shape required by the supplied Sanity schema or publishing pipeline. Prefer an
approved SVG export when the pipeline supports it; otherwise create the
required raster derivative from the editable source. Never make a raster file
the only master. Include a `sanity-asset.json` handoff file with the asset ID,
title, alt text, caption, source guide, target placement, export filename,
mime type, pixel dimensions or viewBox, focal point if applicable, credit or
licence information if applicable, and review status. Do not upload or publish
to Sanity unless explicit access and authorization are supplied.

Before declaring completion, report the results of visual checks at 458px,
phone width, desktop, A4 or US Letter, and grayscale. Flag any design-system
constraint or unresolved decision rather than silently substituting one.
```

## Required handoff shape

Use the production bundle described in the prompt. A typical `sanity-asset.json` contains only verified, schema-compatible values:

```json
{
  "assetId": "BD-V-000",
  "title": "Short descriptive title",
  "altText": "One plain sentence describing the teaching relationship.",
  "caption": "",
  "sourceGuide": "student-guide | educator-guide | shared",
  "targetPlacement": "Exact heading and insertion position from 08_assets.md",
  "exportFile": "visual.svg",
  "mimeType": "image/svg+xml",
  "dimensions": {"viewBox": "0 0 1000 750"},
  "focalPoint": null,
  "credit": null,
  "licence": null,
  "reviewStatus": "draft | review | approved"
}
```

Do not invent a Sanity document type, field name, or upload endpoint. Adapt this handoff to the actual schema when it is available.
