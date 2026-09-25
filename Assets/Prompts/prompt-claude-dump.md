# Claude prompt dump

## Purpose



This is the consolidated, non-lossy prompt document for the Bitcoin Diploma visual-production workflow. It brings together the unique content from the requested prompt sources. Duplicate source files are recorded below rather than repeated verbatim:



- `Assets/Prompts/prompt-01-json.md` and `Assets/Prompts/prompt-02-jpg.md` are identical; their shared content appears once in “OpenAI reference-image prompt.”

- `Assets/Prompts/prompt-03-mg.md` and `workspace/23_claude-design-sanity-asset-prompt.md` are identical; their shared content appears once in “Claude Design and Sanity asset prompt.”



The complete production checklist is retained verbatim, including all 101 asset briefs. This document does not itself authorize production, upload, publication, or release of deferred items.



---



# OpenAI reference-image prompt




## Purpose

**Attach** this file to every OpenAI image-generation request for a Bitcoin Diploma asset. Every eligible asset requires a low-resolution transparent PNG reference, a white-background JPG preview of the same image, and a matching conformance report before coded production. The reference and preview are never publication assets.

The current batch contains 101 indexed assets: 98 eligible and three deferred (`BD-V-001`, `BD-V-070`, and `BD-V-075`). Do not generate references for deferred items. `BD-V-001` retains its official licence-mark brief for later production; an AI redraw or an empty reference would not meet that brief.

The section 7 specification is the contract. It settles element identity and count, composition, relationships, reading order, strings, prohibitions, safety, and localization before generation. The reference image contributes only spatial arrangement and visual treatment. It is not a final Diploma asset and does not authorize publication.

The curriculum text and [08_assets.md](08_assets.md) are the instructional source of truth. [27_assets-style.md](27_assets-style.md) is the binding reference-image style authority. If its visual treatment conflicts with an instructional, safety, or structural requirement, the asset brief wins; record the conflict in `unresolved`.

## Folder routing

ChatGPT creates working reference material only. It must never treat its PNG, JPG, or JSON as a production asset, place them in `assets/`, or propose a direct manuscript insertion. Store outputs in the ignored local-work area:

```text
Assets/
├── references/bd-v-000-ref.png
├── references/bd-v-000-ref.jpg
├── references/bd-v-000-ref.json
└── prompts/bd-v-000-ref.txt
```

Replace `bd-v-000` with the lowercase stable asset ID. The later Claude implementation belongs in the tracked `Assets/diploma/` tree. This separation keeps experiments out of version control and makes approved, editable source reviewable.

## Complete prompt

```text
Create one low-resolution transparent PNG reference image and a white-background
JPG preview of that same image for a My First Bitcoin Bitcoin Diploma visual.
Generate the composition once. Preserve real alpha transparency in the PNG;
composite that PNG over solid white (#FFFFFF) to export the JPG at the same
dimensions, without changing the composition. JPEG does not store transparency.
Do not substitute a checkerboard pattern for transparent pixels.
These are private working references for a later Claude
implementation in editable HTML, CSS, and inline SVG. It is not a publication
asset, brand asset, or asset to upload to Sanity.

Read all supplied material before generating:
- Asset ID: [BD-V-000]
- Complete section 7 reference specification from workspace/08_assets.md (the classification record and complete incorporated section 3 asset entry):
  [paste specification]
- Complete section 3 asset row from workspace/08_assets.md: [paste entry]
- Relevant section 8 shared-register entries from workspace/08_assets.md:
  [paste entries, if any]
- Optional adjacent guide text: [paste only when it clarifies the lesson]
- Binding reference-image style: workspace/27_assets-style.md [attach]

Contract
The section 7 specification is the complete structural contract. Build exactly
the elements in `elements`, in the stated `composition`, with the stated
`relationships`, and in the stated `reading_order`. Add nothing that is not
listed. Follow every `must_not` item and every safety requirement exactly. Stop
and report in `unresolved` rather than invent when the specification is missing
something the image needs. Carry every unresolved `open` item from the
specification into `unresolved`. If an open item prevents the required
structure, do not generate the image.

When relevant section 8 shared-register entries are supplied, reuse those
actor, prop, symbol, interface, and notation definitions exactly. Do not merge
roles that the register marks as distinct.

Render zero text, letters, or numerals anywhere in either image. Do not render
labels, placeholder bars, punctuation, logos, URLs, QR codes, captions,
warnings, data, or decorative characters. Every string belongs only in the
live, translatable coding stage.

Visual construction
Apply workspace/27_assets-style.md. Use flat vector-style artwork on a
transparent PNG canvas, with a white-background JPG preview. Draw front-on,
orthographic forms with no perspective or depth. Use one uniform outline
weight, rounded corners, soft joins, and solid flat fills.
Use no gradients, shading, shadows, texture, or grain. Restrict shapes to
rectangles, rounded rectangles, circles, ellipses, triangles, trapezoids, and simple arcs. Keep to
a hard budget of 24 closed shapes for each prop and 60 for each person.

Use the purple-led palette, soft violet, white, and restrained warm orange
accents specified in workspace/27_assets-style.md. Use orange sparingly.
Keep negative space transparent in the PNG; white/off-white fills may be used
inside specified objects. The JPG preview background is solid white.

Draw no arrows, connectors, bubbles, frames, borders, or scenery. The Claude
implementation adds those separate design-system elements in code.

Safety and factual boundaries
Never show a real seed phrase, private key, payable address, learner identity,
learner balance, or private personal data. Do not depict an unverified real
QR code, URL, address, interface, transaction, price, date, or factual datum.
Do not imply guaranteed returns, risk-free self-custody, inevitable adoption,
a universal local or legal conclusion, or a recommendation of a wallet,
exchange, service, or provider. Keep protocol, wallet, service, user, node,
miner, and educator roles distinct whenever relevant. Preserve every supplied
qualification and trade-off.

Return these outputs in this order:
1. One transparent PNG reference image.
2. One white-background JPG preview of the same composition and dimensions.
3. One JSON code block named [asset-id-lowercase]-ref.json. It is a
   conformance report, not a description of the image.

Use this schema:
{
  "assetId": "BD-V-000",
  "specVersion": 3,
  "canvas": {
    "aspectRatio": "",
    "orientation": "landscape | portrait | square",
    "suggestedWidthPx": 1024,
    "reference": {
      "fileName": "bd-v-000-ref.png",
      "format": "PNG",
      "background": "transparent"
    },
    "preview": {
      "fileName": "bd-v-000-ref.jpg",
      "format": "JPEG",
      "background": "#FFFFFF"
    }
  },
  "placement": [
    {
      "elementId": "must match an id from the specification",
      "boundsPercent": {"x": 0, "y": 0, "width": 0, "height": 0},
      "zIndex": 1,
      "treatmentNotes": "shape, posture, emphasis, hatch, orientation"
    }
  ],
  "conformance": {
    "elementsRendered": [],
    "elementsMissing": [],
    "elementsAdded": [{"description": "", "why": ""}],
    "compositionFollowed": true,
    "compositionDeviation": "",
    "countDeviations": [],
    "mustNotViolations": [],
    "textPresentInImage": [],
    "shapeBudgetEstimate": 0,
    "pngTransparencyVerified": true,
    "jpgWhiteBackgroundVerified": true,
    "exportsMatch": true
  },
  "unresolved": [
    "anything the specification did not settle that the image had to resolve arbitrarily"
  ]
}
```

## Save and review

Save the transparent PNG as `Assets/Reference/bd-v-000-ref.jpg`, the white-background JPG preview as `Assets/Reference/bd-v-000-ref.jpg`, their conformance report as `Assets/Reference/bd-v-000-ref.json`, and the completed prompt, model or tool, settings (including the JPG export), generation date, source-brief revision, and review note as `Assets/Prompts/prompt-codex.md Replace `bd-v-000` with the lowercase stable asset ID.

Review both images against the brief. Verify actual transparent background pixels in the PNG, a solid white background in the JPG, matching dimensions and composition, and no prohibited visible content in either file. Record actual formats and background treatments in `canvas`; set the three export-verification flags to true only after checking the files. An alpha channel containing only opaque pixels does not satisfy transparency. Change a checklist item to `[X]` only after all four files exist and pass review; deferred and blocked items remain unchecked.

The report is deliberately smaller than the earlier descriptive schema. Element identity, relationships, reading order, labels, and prohibitions live in the specification, so the report carries only placement, treatment, and deviations. At review, `textPresentInImage` must be empty. `elementsAdded` must be empty or justified.

Self-reported conformance is weak evidence. A model will tend to claim it complied. The report narrows what a human or Claude must check. It does not replace the check.


---

# Claude Design and Sanity asset prompt

---



---


## Purpose

Attach this file to every Claude Design request that turns a Bitcoin Diploma contract into a production asset. Each eligible asset receives an approved transparent PNG reference, its white-background JPG preview, and their conformance report. Claude must create the editable, accessible source and upload-ready deliverables; it must not publish a reference image. The current reference batch defers `BD-V-001`, `BD-V-070`, and `BD-V-075`; these prompts do not release deferred items. For later `BD-V-001` production, use the official licence mark under its existing brief, not an AI redraw.

The complete entry in [08_assets.md](08_assets.md) is the instructional source of truth. The Claude Design System and its local authoring contract are the source of truth for brand and design-system choices. Where they conflict, stop and report the specific conflict for resolution.

## Folder routing

Claude consumes the approved reference materials from the ignored `Assets/` area, but must create its editable production bundle only in the tracked `Assets/diploma/` tree. Choose the destination from the asset entry's placement(s):

```text
Assets/diploma/
├── student-guide/bd-v-000/  # Student Guide only
├── educator-guide/bd-v-000/ # Educator Guide only
└── shared/bd-v-000/         # reused by both guides
```

Use `shared/` only when the same approved implementation serves both guides. Keep reference PNGs, JPG previews, JSON conformance reports, prompts, model settings, and rejected concepts in `Assets/`; they are references, not production deliverables. Do not create a final source bundle at `Assets/diploma/bd-v-000/`: flat paths are handoff examples for publication pipelines, not the canonical editable-project location.

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
- Approved low-resolution transparent PNG reference: [attach bd-v-000-ref.png]
- Matching white-background JPG preview: [attach bd-v-000-ref.jpg]
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
4. The approved PNG reference and its JPG preview guide
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
or publish either reference image. Reject or revise
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
`Assets/diploma/<student-guide|educator-guide|shared>/bd-v-000/`.

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


---

# Claude production-asset prompt checklist

---



---


## Purpose

Use each item only after its matching transparent PNG reference, white-background JPG preview, and JSON conformance report have passed review. Copy the entire prompt, attach the three reference files, the section 7 classification registry, and the relevant Claude Design System/Sanity schema, and build the editable production bundle. These prompts do not authorize a Sanity upload or publication.

The checklist is generated from [08_assets.md](08_assets.md) and contains all 101 complete asset briefs. The section 7 classification registry incorporates each complete asset brief as its structural contract and requires approved references for each eligible ID. The current batch defers `BD-V-001`, `BD-V-070`, and `BD-V-075`; this production checklist does not release them. It complements [23_claude-design-sanity-asset-prompt.md](23_claude-design-sanity-asset-prompt.md): this file is the ready-to-paste production queue; document 23 is the deeper reusable implementation contract.

## Completion rules

- Change `[ ]` to `[X]` only when the editable bundle, preview, accessibility handoff, and documented visual checks exist and have passed review.
- Attach the matching `Assets/Reference/<asset-id-lowercase>-ref.png`, `.jpg`, and `.json` before using an eligible prompt. Confirm that both images, the conformance report, and the prompt record passed reference review. Do not treat reference files as production files.
- Keep deferred `BD-V-001`, `BD-V-070`, and `BD-V-075` unchecked. Later `BD-V-001` production must use the official licence mark under its existing brief, not an AI redraw.
- Keep adjoining and related assets separate. A shared asset may serve both listed placements only when the same implementation is genuinely appropriate.
- Conditional assets remain blocked until every verification or local/editorial decision named in the asset brief is resolved.

## 3.1 Welcome and learning setup

### [ ] BD-V-001 — Image

```text
DEFERRED — this prompt does not release the item for production. Leave its checklist item unchecked. Its required official Creative Commons BY-SA 4.0 logo and adjacent text are prohibited in reference images. Keep the official mark for later production under the complete brief; do not redraw it or invent a substitute.

Complete asset brief
- Asset ID: BD-V-001
- Suggested by: Pablo
- Priority: Supporting
- Type: Image
- Historical page/note: 1; add the Creative Commons Attribution-ShareAlike 4.0 licence logo in Sanity.
- Placement: At the Creative Commons Attribution-ShareAlike 4.0 licence statement near the front of `../publish/mfb-bd-26.10/mfb-bd-sg-26.10.md`, immediately after the licence paragraph and before the horizontal rule.
- Source locator: 11
- Text–visual link: Gives the open licence a recognisable visual marker while leaving the written licence terms primary.
- Design brief: Use the official Creative Commons BY-SA 4.0 mark at small but legible size. Keep the written licence statement, attribution requirement, and adaptation condition beside or immediately above it. Do not redraw, recolour, distort, or use the logo as a replacement for the licence text or link.
- Format: Official licence mark with short text lockup; small inline or corner placement.

Retain the complete brief for a later authorized production decision. Do not generate, upload, or publish an asset in the current batch.
```
### [ ] BD-V-002 — Diagram

```text
You are building one production-ready, accessible My First Bitcoin Bitcoin Diploma visual from a supplied approved transparent PNG reference, its white-background JPG preview, and their JSON conformance report. Read the complete brief below before acting. The asset brief is the source of truth for lesson intent, content, safety, caption, alt text, placement, and localization. The reference image guides composition only. If it conflicts with the brief, the brief wins; report any unresolved factual or design-system gap before implementing.

Rebuild—not trace or embed—the reference as editable HTML, CSS, and inline SVG. Apply the supplied Claude Design System rather than the reference's provisional styling. Keep all essential geometry, arrows, labels, warnings, icons, and data editable. Preserve one clear teaching relationship, a decisive reading order, cultural replaceability, grayscale meaning, narrow-page responsiveness, phone and desktop usability, A4/US-Letter printing, expandable translated text, and future RTL adaptation.

Never invent facts, labels, numbers, providers, URLs, legal claims, safety claims, or brand choices. Preserve every prohibition and qualification in the brief. Do not include real seed phrases, private keys, payable addresses, private learner data, balances, or transactions. Use a verified QR, address, URL, interface, date, or fact only when the brief explicitly authorizes it and it has been checked. Do not imply investment returns, guaranteed outcomes, risk-free self-custody, inevitable adoption, or universal local conclusions. Do not turn a named service into a recommendation.

Produce a bundle in the guide-specific `Assets/diploma/<student-guide|educator-guide|shared>/<asset-id-lowercase>/` folder selected from the placement. Include `micrographic.html`, `micrographic.css`, `meta.json`, `preview.html` in a 458px review frame, `alt-text.md`, `README.md`, and `sanity-asset.json`. Prefix CSS selectors with a unique `.mg-<slug>` root; tag all translatable text with non-nested `data-t` keys; use no JavaScript, external assets, external fonts, CSS grid, vh/vw, rem, fixed/sticky positioning, or `@import`. Do not upload or publish to Sanity. Before declaring completion, report visual checks at 458px, phone, desktop, A4/US Letter, and grayscale.

Required inputs to attach
- Approved transparent PNG reference: Assets/Reference/bd-v-002-ref.jpg
- Matching white-background JPG preview: Assets/Reference/bd-v-002-ref.jpg
- Matching conformance report: Assets/Reference/bd-v-002-ref.json
- Current Claude Design System authoring instructions and closest approved micrographic bundle
- Current Sanity schema/publishing requirements, if available

Complete asset brief
- Asset ID: BD-V-002
- Suggested by: Pablo
- Priority: Supporting
- Type: Diagram
- Historical page/note: 2; teach a critical-thinking process with scans, tips, or checkpoints.
- Placement: Under `### What we stand for: accessibility, critical thinking, community, and self-sovereignty`, after the paragraph on examining claims and trade-offs.
- Source locator: 41
- Text–visual link: Makes “teach how to think, not what to think” into a repeatable learner action.
- Design brief: Show a six-step loop: identify the claim; separate fact from preference; inspect evidence and source; compare alternatives; name a trade-off or uncertainty; form a provisional conclusion or question. The loop must allow revision rather than ending in certainty.
- Format: Horizontal process strip or circular loop; half page.

Use the exact heading and insertion direction in Placement as the target placement. Preserve all listed placements in metadata. Include source-brief revision, reference paths, factual sources, production date, reviewer status, checks, and unresolved judgments in README.md. Set `reviewStatus` to draft or review unless an authorized reviewer has approved it.
```
### [ ] BD-V-076 — Image

```text
You are building one production-ready, accessible My First Bitcoin Bitcoin Diploma visual from a supplied approved transparent PNG reference, its white-background JPG preview, and their JSON conformance report. Read the complete brief below before acting. The asset brief is the source of truth for lesson intent, content, safety, caption, alt text, placement, and localization. The reference image guides composition only. If it conflicts with the brief, the brief wins; report any unresolved factual or design-system gap before implementing.

Rebuild—not trace or embed—the reference as editable HTML, CSS, and inline SVG. Apply the supplied Claude Design System rather than the reference's provisional styling. Keep all essential geometry, arrows, labels, warnings, icons, and data editable. Preserve one clear teaching relationship, a decisive reading order, cultural replaceability, grayscale meaning, narrow-page responsiveness, phone and desktop usability, A4/US-Letter printing, expandable translated text, and future RTL adaptation.

Never invent facts, labels, numbers, providers, URLs, legal claims, safety claims, or brand choices. Preserve every prohibition and qualification in the brief. Do not include real seed phrases, private keys, payable addresses, private learner data, balances, or transactions. Use a verified QR, address, URL, interface, date, or fact only when the brief explicitly authorizes it and it has been checked. Do not imply investment returns, guaranteed outcomes, risk-free self-custody, inevitable adoption, or universal local conclusions. Do not turn a named service into a recommendation.

Produce a bundle in the guide-specific `Assets/diploma/<student-guide|educator-guide|shared>/<asset-id-lowercase>/` folder selected from the placement. Include `micrographic.html`, `micrographic.css`, `meta.json`, `preview.html` in a 458px review frame, `alt-text.md`, `README.md`, and `sanity-asset.json`. Prefix CSS selectors with a unique `.mg-<slug>` root; tag all translatable text with non-nested `data-t` keys; use no JavaScript, external assets, external fonts, CSS grid, vh/vw, rem, fixed/sticky positioning, or `@import`. Do not upload or publish to Sanity. Before declaring completion, report visual checks at 458px, phone, desktop, A4/US Letter, and grayscale.

Required inputs to attach
- Approved transparent PNG reference: Assets/Reference/bd-v-076-ref.jpg
- Matching white-background JPG preview: Assets/Reference/bd-v-076-ref.jpg
- Matching conformance report: Assets/Reference/bd-v-076-ref.json
- Current Claude Design System authoring instructions and closest approved micrographic bundle
- Current Sanity schema/publishing requirements, if available

Complete asset brief
- Asset ID: BD-V-076
- Suggested by: User
- Priority: Essential
- Type: Image
- Historical page/note: —; Provide an app-download call to action with a QR code at the introduction and end of both guides only.
- Placement: SG: after the download call to action under `### Learn more with the [My First Bitcoin App](https://myfirstbitcoin.app/)` and `## Continue learning`. EG: after the download calls under `## About this guide` and `## Continue learning`; replace the two matching markers. All four source lines are listed here.
- Source locator: SG: 51, 1514; EG: 9, 3619
- Text–visual link: Gives learners and educators an optional download route at the start and end of each guide.
- Design brief: Reuse one QR panel at exactly these four download calls to action: two per guide. Use `https://myfirstbitcoin.app/` for the QR destination, hyperlink, and readable printed URL. Label the panel Download the [My First Bitcoin App](https://myfirstbitcoin.app/) and state that use is optional. Do not place this app QR elsewhere in either guide or in other publications. Other app mentions remain text hyperlinks. Test the link and printed QR before publication.
- Format: Reusable compact download QR panel with a readable URL.

Use the exact heading and insertion direction in Placement as the target placement. Preserve all listed placements in metadata. Include source-brief revision, reference paths, factual sources, production date, reviewer status, checks, and unresolved judgments in README.md. Set `reviewStatus` to draft or review unless an authorized reviewer has approved it.
```
### [ ] BD-V-077 — Diagram

```text
You are building one production-ready, accessible My First Bitcoin Bitcoin Diploma visual from a supplied approved transparent PNG reference, its white-background JPG preview, and their JSON conformance report. Read the complete brief below before acting. The asset brief is the source of truth for lesson intent, content, safety, caption, alt text, placement, and localization. The reference image guides composition only. If it conflicts with the brief, the brief wins; report any unresolved factual or design-system gap before implementing.

Rebuild—not trace or embed—the reference as editable HTML, CSS, and inline SVG. Apply the supplied Claude Design System rather than the reference's provisional styling. Keep all essential geometry, arrows, labels, warnings, icons, and data editable. Preserve one clear teaching relationship, a decisive reading order, cultural replaceability, grayscale meaning, narrow-page responsiveness, phone and desktop usability, A4/US-Letter printing, expandable translated text, and future RTL adaptation.

Never invent facts, labels, numbers, providers, URLs, legal claims, safety claims, or brand choices. Preserve every prohibition and qualification in the brief. Do not include real seed phrases, private keys, payable addresses, private learner data, balances, or transactions. Use a verified QR, address, URL, interface, date, or fact only when the brief explicitly authorizes it and it has been checked. Do not imply investment returns, guaranteed outcomes, risk-free self-custody, inevitable adoption, or universal local conclusions. Do not turn a named service into a recommendation.

Produce a bundle in the guide-specific `Assets/diploma/<student-guide|educator-guide|shared>/<asset-id-lowercase>/` folder selected from the placement. Include `micrographic.html`, `micrographic.css`, `meta.json`, `preview.html` in a 458px review frame, `alt-text.md`, `README.md`, and `sanity-asset.json`. Prefix CSS selectors with a unique `.mg-<slug>` root; tag all translatable text with non-nested `data-t` keys; use no JavaScript, external assets, external fonts, CSS grid, vh/vw, rem, fixed/sticky positioning, or `@import`. Do not upload or publish to Sanity. Before declaring completion, report visual checks at 458px, phone, desktop, A4/US Letter, and grayscale.

Required inputs to attach
- Approved transparent PNG reference: Assets/Reference/bd-v-077-ref.jpg
- Matching white-background JPG preview: Assets/Reference/bd-v-077-ref.jpg
- Matching conformance report: Assets/Reference/bd-v-077-ref.json
- Current Claude Design System authoring instructions and closest approved micrographic bundle
- Current Sanity schema/publishing requirements, if available

Complete asset brief
- Asset ID: BD-V-077
- Suggested by: User
- Priority: Essential
- Type: Diagram
- Historical page/note: —; Add the learning-to-teaching pathway beside the Student Guide paragraph beginning “If you have limited time”.
- Placement: SG: Under `### How learners can use this course as a starting point`, immediately after the paragraph beginning “If you have limited time”. EG: under `### The pathway from learner to educator`, replace the matching marker after the source text at the listed EG line. See section 3.8 for the exact anchor.
- Source locator: SG: 85; EG: 408
- Text–visual link: Shows how the Diploma fits into a wider pathway from first learning to teaching and community participation.
- Design brief: Show [Introduction to Bitcoin](https://myfirstbitcoin.org/learn/programs#intro) → Bitcoin Diploma → [Educator Training Program](https://etp.myfirstbitcoin.org/) → Joining the Bitcoin Education Network. Link the final stage to the [Bitcoin Education Network](https://leaderboard.myfirstbitcoin.org) dashboard in digital versions. Add short labels: `Explore the basics`, `Build a beginner foundation`, `Develop teaching practice`, and `Connect and contribute`. Present this as an optional progression, with direct entry to the Diploma possible. Do not imply that Diploma completion automatically qualifies someone to teach or grants network membership. Align with `### The pathway from learner to educator` in the Educator Guide.
- Format: Four-stage pathway diagram with editable text; full width.

Use the exact heading and insertion direction in Placement as the target placement. Preserve all listed placements in metadata. Include source-brief revision, reference paths, factual sources, production date, reviewer status, checks, and unresolved judgments in README.md. Set `reviewStatus` to draft or review unless an authorized reviewer has approved it.
```
### [ ] BD-V-006 — Diagram

```text
You are building one production-ready, accessible My First Bitcoin Bitcoin Diploma visual from a supplied approved transparent PNG reference, its white-background JPG preview, and their JSON conformance report. Read the complete brief below before acting. The asset brief is the source of truth for lesson intent, content, safety, caption, alt text, placement, and localization. The reference image guides composition only. If it conflicts with the brief, the brief wins; report any unresolved factual or design-system gap before implementing.

Rebuild—not trace or embed—the reference as editable HTML, CSS, and inline SVG. Apply the supplied Claude Design System rather than the reference's provisional styling. Keep all essential geometry, arrows, labels, warnings, icons, and data editable. Preserve one clear teaching relationship, a decisive reading order, cultural replaceability, grayscale meaning, narrow-page responsiveness, phone and desktop usability, A4/US-Letter printing, expandable translated text, and future RTL adaptation.

Never invent facts, labels, numbers, providers, URLs, legal claims, safety claims, or brand choices. Preserve every prohibition and qualification in the brief. Do not include real seed phrases, private keys, payable addresses, private learner data, balances, or transactions. Use a verified QR, address, URL, interface, date, or fact only when the brief explicitly authorizes it and it has been checked. Do not imply investment returns, guaranteed outcomes, risk-free self-custody, inevitable adoption, or universal local conclusions. Do not turn a named service into a recommendation.

Produce a bundle in the guide-specific `Assets/diploma/<student-guide|educator-guide|shared>/<asset-id-lowercase>/` folder selected from the placement. Include `micrographic.html`, `micrographic.css`, `meta.json`, `preview.html` in a 458px review frame, `alt-text.md`, `README.md`, and `sanity-asset.json`. Prefix CSS selectors with a unique `.mg-<slug>` root; tag all translatable text with non-nested `data-t` keys; use no JavaScript, external assets, external fonts, CSS grid, vh/vw, rem, fixed/sticky positioning, or `@import`. Do not upload or publish to Sanity. Before declaring completion, report visual checks at 458px, phone, desktop, A4/US Letter, and grayscale.

Required inputs to attach
- Approved transparent PNG reference: Assets/Reference/bd-v-006-ref.jpg
- Matching white-background JPG preview: Assets/Reference/bd-v-006-ref.jpg
- Matching conformance report: Assets/Reference/bd-v-006-ref.json
- Current Claude Design System authoring instructions and closest approved micrographic bundle
- Current Sanity schema/publishing requirements, if available

Complete asset brief
- Asset ID: BD-V-006
- Suggested by: AI
- Priority: Supporting
- Type: Diagram
- Historical page/note: 4; apply the five-step learning rhythm consistently.
- Placement: Under `### Flexible learning: in person, online, or through low-tech delivery`, after the five-item list beginning “Learn a key idea”.
- Source locator: 124
- Text–visual link: Shows how a learner moves through a typical concept rather than only reading it.
- Design brief: Use the five stages in the current list: `Learn a key idea → Show what you can explain or apply → Apply the idea → Explain in your own words → Review the connection to the next module`. Keep discussion, safe practice, and offline participation available throughout. Do not turn this learning rhythm into an assessment score or imply that self-report proves competency.
- Format: Five-step rhythm strip; half to full width.

Use the exact heading and insertion direction in Placement as the target placement. Preserve all listed placements in metadata. Include source-brief revision, reference paths, factual sources, production date, reviewer status, checks, and unresolved judgments in README.md. Set `reviewStatus` to draft or review unless an authorized reviewer has approved it.
```
### [ ] BD-V-003 — Diagram

```text
You are building one production-ready, accessible My First Bitcoin Bitcoin Diploma visual from a supplied approved transparent PNG reference, its white-background JPG preview, and their JSON conformance report. Read the complete brief below before acting. The asset brief is the source of truth for lesson intent, content, safety, caption, alt text, placement, and localization. The reference image guides composition only. If it conflicts with the brief, the brief wins; report any unresolved factual or design-system gap before implementing.

Rebuild—not trace or embed—the reference as editable HTML, CSS, and inline SVG. Apply the supplied Claude Design System rather than the reference's provisional styling. Keep all essential geometry, arrows, labels, warnings, icons, and data editable. Preserve one clear teaching relationship, a decisive reading order, cultural replaceability, grayscale meaning, narrow-page responsiveness, phone and desktop usability, A4/US-Letter printing, expandable translated text, and future RTL adaptation.

Never invent facts, labels, numbers, providers, URLs, legal claims, safety claims, or brand choices. Preserve every prohibition and qualification in the brief. Do not include real seed phrases, private keys, payable addresses, private learner data, balances, or transactions. Use a verified QR, address, URL, interface, date, or fact only when the brief explicitly authorizes it and it has been checked. Do not imply investment returns, guaranteed outcomes, risk-free self-custody, inevitable adoption, or universal local conclusions. Do not turn a named service into a recommendation.

Produce a bundle in the guide-specific `Assets/diploma/<student-guide|educator-guide|shared>/<asset-id-lowercase>/` folder selected from the placement. Include `micrographic.html`, `micrographic.css`, `meta.json`, `preview.html` in a 458px review frame, `alt-text.md`, `README.md`, and `sanity-asset.json`. Prefix CSS selectors with a unique `.mg-<slug>` root; tag all translatable text with non-nested `data-t` keys; use no JavaScript, external assets, external fonts, CSS grid, vh/vw, rem, fixed/sticky positioning, or `@import`. Do not upload or publish to Sanity. Before declaring completion, report visual checks at 458px, phone, desktop, A4/US Letter, and grayscale.

Required inputs to attach
- Approved transparent PNG reference: Assets/Reference/bd-v-003-ref.jpg
- Matching white-background JPG preview: Assets/Reference/bd-v-003-ref.jpg
- Matching conformance report: Assets/Reference/bd-v-003-ref.json
- Current Claude Design System authoring instructions and closest approved micrographic bundle
- Current Sanity schema/publishing requirements, if available

Complete asset brief
- Asset ID: BD-V-003
- Suggested by: AI
- Priority: Essential
- Type: Diagram
- Historical page/note: 6; clarify the four-module Diploma, educator-curated Modules 3–4, and Advanced boundaries.
- Placement: SG: Under `### The four-module Diploma, educator-curated Module 4, and Advanced Learning`, after the paragraph beginning “Advanced Learning is outside the Diploma” and before “A topic is not unimportant”. EG: under `### Four-module Diploma and Advanced boundaries`, replace the matching marker after the source text at the listed EG line. See section 3.8 for the exact anchor.
- Source locator: SG: 205; EG: 466
- Text–visual link: Clarifies that all four modules are the Diploma, while educators adapt Module 3 practice and curate the required Connect Module 4.
- Design brief: Show all four modules inside a `Diploma: all learners` container, labeled Problem → Solution → Action → Connect. Mark Modules 1–2 as shared core learning, Module 3 as educator-adapted practical learning, and Module 4 as `Connect: educator-curated local learning; required`. Show that Connect applies the earlier learning to a local need and realistic alternative. Show Advanced as a separate onward path. Use arrows to show progression, not a hierarchy of importance.
- Format: Layered pathway diagram; full width.

Use the exact heading and insertion direction in Placement as the target placement. Preserve all listed placements in metadata. Include source-brief revision, reference paths, factual sources, production date, reviewer status, checks, and unresolved judgments in README.md. Set `reviewStatus` to draft or review unless an authorized reviewer has approved it.
```
### [ ] BD-V-004 — Diagram

```text
You are building one production-ready, accessible My First Bitcoin Bitcoin Diploma visual from a supplied approved transparent PNG reference, its white-background JPG preview, and their JSON conformance report. Read the complete brief below before acting. The asset brief is the source of truth for lesson intent, content, safety, caption, alt text, placement, and localization. The reference image guides composition only. If it conflicts with the brief, the brief wins; report any unresolved factual or design-system gap before implementing.

Rebuild—not trace or embed—the reference as editable HTML, CSS, and inline SVG. Apply the supplied Claude Design System rather than the reference's provisional styling. Keep all essential geometry, arrows, labels, warnings, icons, and data editable. Preserve one clear teaching relationship, a decisive reading order, cultural replaceability, grayscale meaning, narrow-page responsiveness, phone and desktop usability, A4/US-Letter printing, expandable translated text, and future RTL adaptation.

Never invent facts, labels, numbers, providers, URLs, legal claims, safety claims, or brand choices. Preserve every prohibition and qualification in the brief. Do not include real seed phrases, private keys, payable addresses, private learner data, balances, or transactions. Use a verified QR, address, URL, interface, date, or fact only when the brief explicitly authorizes it and it has been checked. Do not imply investment returns, guaranteed outcomes, risk-free self-custody, inevitable adoption, or universal local conclusions. Do not turn a named service into a recommendation.

Produce a bundle in the guide-specific `Assets/diploma/<student-guide|educator-guide|shared>/<asset-id-lowercase>/` folder selected from the placement. Include `micrographic.html`, `micrographic.css`, `meta.json`, `preview.html` in a 458px review frame, `alt-text.md`, `README.md`, and `sanity-asset.json`. Prefix CSS selectors with a unique `.mg-<slug>` root; tag all translatable text with non-nested `data-t` keys; use no JavaScript, external assets, external fonts, CSS grid, vh/vw, rem, fixed/sticky positioning, or `@import`. Do not upload or publish to Sanity. Before declaring completion, report visual checks at 458px, phone, desktop, A4/US Letter, and grayscale.

Required inputs to attach
- Approved transparent PNG reference: Assets/Reference/bd-v-004-ref.jpg
- Matching white-background JPG preview: Assets/Reference/bd-v-004-ref.jpg
- Matching conformance report: Assets/Reference/bd-v-004-ref.json
- Current Claude Design System authoring instructions and closest approved micrographic bundle
- Current Sanity schema/publishing requirements, if available

Complete asset brief
- Asset ID: BD-V-004
- Suggested by: AI
- Priority: Essential
- Type: Diagram
- Historical page/note: 6–7; clarify the Problem → Solution → Action → Connect module structure and show timing as adaptable.
- Placement: Under `### How the 4-module learning path is organized`, immediately before the existing four-row table.
- Source locator: 211
- Text–visual link: Gives learners a mental map of the Diploma before they enter Module 1.
- Design brief: Show one connected sequence: `1 Problem: Understanding Money → 2 Solution: How Bitcoin Works → 3 Action: Using Bitcoin Safely → 4 Connect: Bitcoin in Your Community`. Mark Modules 1–3 as shared learning and Module 4 as educator-curated, locally relevant, and required. Show that Connect links the first three stages to a local need, realistic alternative, safe task, and next step. Include each module's guiding question in short editable text. The final module must not be reduced to spending.
- Format: Four-stage roadmap; full width.

Use the exact heading and insertion direction in Placement as the target placement. Preserve all listed placements in metadata. Include source-brief revision, reference paths, factual sources, production date, reviewer status, checks, and unresolved judgments in README.md. Set `reviewStatus` to draft or review unless an authorized reviewer has approved it.
```
### [ ] BD-V-005 — Table

```text
You are building one production-ready, accessible My First Bitcoin Bitcoin Diploma visual from a supplied approved transparent PNG reference, its white-background JPG preview, and their JSON conformance report. Read the complete brief below before acting. The asset brief is the source of truth for lesson intent, content, safety, caption, alt text, placement, and localization. The reference image guides composition only. If it conflicts with the brief, the brief wins; report any unresolved factual or design-system gap before implementing.

Rebuild—not trace or embed—the reference as editable HTML, CSS, and inline SVG. Apply the supplied Claude Design System rather than the reference's provisional styling. Keep all essential geometry, arrows, labels, warnings, icons, and data editable. Preserve one clear teaching relationship, a decisive reading order, cultural replaceability, grayscale meaning, narrow-page responsiveness, phone and desktop usability, A4/US-Letter printing, expandable translated text, and future RTL adaptation.

Never invent facts, labels, numbers, providers, URLs, legal claims, safety claims, or brand choices. Preserve every prohibition and qualification in the brief. Do not include real seed phrases, private keys, payable addresses, private learner data, balances, or transactions. Use a verified QR, address, URL, interface, date, or fact only when the brief explicitly authorizes it and it has been checked. Do not imply investment returns, guaranteed outcomes, risk-free self-custody, inevitable adoption, or universal local conclusions. Do not turn a named service into a recommendation.

Produce a bundle in the guide-specific `Assets/diploma/<student-guide|educator-guide|shared>/<asset-id-lowercase>/` folder selected from the placement. Include `micrographic.html`, `micrographic.css`, `meta.json`, `preview.html` in a 458px review frame, `alt-text.md`, `README.md`, and `sanity-asset.json`. Prefix CSS selectors with a unique `.mg-<slug>` root; tag all translatable text with non-nested `data-t` keys; use no JavaScript, external assets, external fonts, CSS grid, vh/vw, rem, fixed/sticky positioning, or `@import`. Do not upload or publish to Sanity. Before declaring completion, report visual checks at 458px, phone, desktop, A4/US Letter, and grayscale.

Required inputs to attach
- Approved transparent PNG reference: Assets/Reference/bd-v-005-ref.jpg
- Matching white-background JPG preview: Assets/Reference/bd-v-005-ref.jpg
- Matching conformance report: Assets/Reference/bd-v-005-ref.json
- Current Claude Design System authoring instructions and closest approved micrographic bundle
- Current Sanity schema/publishing requirements, if available

Complete asset brief
- Asset ID: BD-V-005
- Suggested by: AI
- Priority: Supporting
- Type: Table
- Historical page/note: 6–7; turn the Problem → Solution → Action → Connect learning-path table into a clear visual reference.
- Placement: Under `### How the 4-module learning path is organized`, replace the existing four-row table visually while retaining an accessible text equivalent.
- Source locator: 211
- Text–visual link: Lets learners compare each Diploma module's role, guiding question, and promise at a glance.
- Design brief: Preserve the columns `Module`, `Role`, `Guiding question`, and `Learner promise`. Use four clearly separated, editable rows for Problem: Understanding Money, Solution: How Bitcoin Works, Action: Using Bitcoin Safely, and Connect: Bitcoin in Your Community. Mark Modules 1–3 as shared learning and Module 4 as educator-curated, locally relevant, and required for Diploma completion.
- Format: Four-module reference table; full width.

Use the exact heading and insertion direction in Placement as the target placement. Preserve all listed placements in metadata. Include source-brief revision, reference paths, factual sources, production date, reviewer status, checks, and unresolved judgments in README.md. Set `reviewStatus` to draft or review unless an authorized reviewer has approved it.
```

## 3.2 Module 1: Understanding Money

### [ ] BD-V-007 — Table

```text
You are building one production-ready, accessible My First Bitcoin Bitcoin Diploma visual from a supplied approved transparent PNG reference, its white-background JPG preview, and their JSON conformance report. Read the complete brief below before acting. The asset brief is the source of truth for lesson intent, content, safety, caption, alt text, placement, and localization. The reference image guides composition only. If it conflicts with the brief, the brief wins; report any unresolved factual or design-system gap before implementing.

Rebuild—not trace or embed—the reference as editable HTML, CSS, and inline SVG. Apply the supplied Claude Design System rather than the reference's provisional styling. Keep all essential geometry, arrows, labels, warnings, icons, and data editable. Preserve one clear teaching relationship, a decisive reading order, cultural replaceability, grayscale meaning, narrow-page responsiveness, phone and desktop usability, A4/US-Letter printing, expandable translated text, and future RTL adaptation.

Never invent facts, labels, numbers, providers, URLs, legal claims, safety claims, or brand choices. Preserve every prohibition and qualification in the brief. Do not include real seed phrases, private keys, payable addresses, private learner data, balances, or transactions. Use a verified QR, address, URL, interface, date, or fact only when the brief explicitly authorizes it and it has been checked. Do not imply investment returns, guaranteed outcomes, risk-free self-custody, inevitable adoption, or universal local conclusions. Do not turn a named service into a recommendation.

Produce a bundle in the guide-specific `Assets/diploma/<student-guide|educator-guide|shared>/<asset-id-lowercase>/` folder selected from the placement. Include `micrographic.html`, `micrographic.css`, `meta.json`, `preview.html` in a 458px review frame, `alt-text.md`, `README.md`, and `sanity-asset.json`. Prefix CSS selectors with a unique `.mg-<slug>` root; tag all translatable text with non-nested `data-t` keys; use no JavaScript, external assets, external fonts, CSS grid, vh/vw, rem, fixed/sticky positioning, or `@import`. Do not upload or publish to Sanity. Before declaring completion, report visual checks at 458px, phone, desktop, A4/US Letter, and grayscale.

Required inputs to attach
- Approved transparent PNG reference: Assets/Reference/bd-v-007-ref.jpg
- Matching white-background JPG preview: Assets/Reference/bd-v-007-ref.jpg
- Matching conformance report: Assets/Reference/bd-v-007-ref.json
- Current Claude Design System authoring instructions and closest approved micrographic bundle
- Current Sanity schema/publishing requirements, if available

Complete asset brief
- Asset ID: BD-V-007
- Suggested by: AI
- Priority: Supporting
- Type: Table
- Historical page/note: 8; make the money-properties table easy to scan and compare.
- Placement: Under `### Functions and properties of money`, replace the existing `Property / Question to ask` table visually while retaining an accessible text equivalent.
- Source locator: 267
- Text–visual link: Gives learners a reusable set of questions for assessing whether a form of money is useful.
- Design brief: Preserve durability, portability, divisibility, fungibility, scarcity, acceptability, and verifiability, each paired with its existing question. Add restrained, distinct icons only as supporting cues. Do not score currencies or name a universal winner.
- Format: Icon-supported property-question table; full width.

Use the exact heading and insertion direction in Placement as the target placement. Preserve all listed placements in metadata. Include source-brief revision, reference paths, factual sources, production date, reviewer status, checks, and unresolved judgments in README.md. Set `reviewStatus` to draft or review unless an authorized reviewer has approved it.
```
### [ ] BD-V-008 — Diagram

```text
You are building one production-ready, accessible My First Bitcoin Bitcoin Diploma visual from a supplied approved transparent PNG reference, its white-background JPG preview, and their JSON conformance report. Read the complete brief below before acting. The asset brief is the source of truth for lesson intent, content, safety, caption, alt text, placement, and localization. The reference image guides composition only. If it conflicts with the brief, the brief wins; report any unresolved factual or design-system gap before implementing.

Rebuild—not trace or embed—the reference as editable HTML, CSS, and inline SVG. Apply the supplied Claude Design System rather than the reference's provisional styling. Keep all essential geometry, arrows, labels, warnings, icons, and data editable. Preserve one clear teaching relationship, a decisive reading order, cultural replaceability, grayscale meaning, narrow-page responsiveness, phone and desktop usability, A4/US-Letter printing, expandable translated text, and future RTL adaptation.

Never invent facts, labels, numbers, providers, URLs, legal claims, safety claims, or brand choices. Preserve every prohibition and qualification in the brief. Do not include real seed phrases, private keys, payable addresses, private learner data, balances, or transactions. Use a verified QR, address, URL, interface, date, or fact only when the brief explicitly authorizes it and it has been checked. Do not imply investment returns, guaranteed outcomes, risk-free self-custody, inevitable adoption, or universal local conclusions. Do not turn a named service into a recommendation.

Produce a bundle in the guide-specific `Assets/diploma/<student-guide|educator-guide|shared>/<asset-id-lowercase>/` folder selected from the placement. Include `micrographic.html`, `micrographic.css`, `meta.json`, `preview.html` in a 458px review frame, `alt-text.md`, `README.md`, and `sanity-asset.json`. Prefix CSS selectors with a unique `.mg-<slug>` root; tag all translatable text with non-nested `data-t` keys; use no JavaScript, external assets, external fonts, CSS grid, vh/vw, rem, fixed/sticky positioning, or `@import`. Do not upload or publish to Sanity. Before declaring completion, report visual checks at 458px, phone, desktop, A4/US Letter, and grayscale.

Required inputs to attach
- Approved transparent PNG reference: Assets/Reference/bd-v-008-ref.jpg
- Matching white-background JPG preview: Assets/Reference/bd-v-008-ref.jpg
- Matching conformance report: Assets/Reference/bd-v-008-ref.json
- Current Claude Design System authoring instructions and closest approved micrographic bundle
- Current Sanity schema/publishing requirements, if available

Complete asset brief
- Asset ID: BD-V-008
- Suggested by: Pablo
- Priority: Essential
- Type: Diagram
- Historical page/note: 8; illustrate the functions and properties of money.
- Placement: SG: Under `### Functions and properties of money`, after the properties table and before “No form of money scores perfectly.” EG: under `### Functions and properties of money`, replace the matching marker after the source text at the listed EG line. See section 3.8 for the exact anchor.
- Source locator: SG: 275; EG: 1032
- Text–visual link: Separates what money does from the qualities that make it useful.
- Design brief: Use two linked layers. Layer 1 shows the three functions with small, simple icons: exchange arrows for medium of exchange; a price tag or measuring symbol for unit of account; and a clock with protected value for store of value. Layer 2 shows the seven properties: durability, portability, divisibility, fungibility, scarcity, acceptability, verifiability. Use cash, gold, and a generic digital monetary asset only as examples; do not assign a universal winner or a simplistic total score.
- Format: Icon-led two-layer diagram; full width.

Use the exact heading and insertion direction in Placement as the target placement. Preserve all listed placements in metadata. Include source-brief revision, reference paths, factual sources, production date, reviewer status, checks, and unresolved judgments in README.md. Set `reviewStatus` to draft or review unless an authorized reviewer has approved it.
```
### [ ] BD-V-009 — Image

```text
You are building one production-ready, accessible My First Bitcoin Bitcoin Diploma visual from a supplied approved transparent PNG reference, its white-background JPG preview, and their JSON conformance report. Read the complete brief below before acting. The asset brief is the source of truth for lesson intent, content, safety, caption, alt text, placement, and localization. The reference image guides composition only. If it conflicts with the brief, the brief wins; report any unresolved factual or design-system gap before implementing.

Rebuild—not trace or embed—the reference as editable HTML, CSS, and inline SVG. Apply the supplied Claude Design System rather than the reference's provisional styling. Keep all essential geometry, arrows, labels, warnings, icons, and data editable. Preserve one clear teaching relationship, a decisive reading order, cultural replaceability, grayscale meaning, narrow-page responsiveness, phone and desktop usability, A4/US-Letter printing, expandable translated text, and future RTL adaptation.

Never invent facts, labels, numbers, providers, URLs, legal claims, safety claims, or brand choices. Preserve every prohibition and qualification in the brief. Do not include real seed phrases, private keys, payable addresses, private learner data, balances, or transactions. Use a verified QR, address, URL, interface, date, or fact only when the brief explicitly authorizes it and it has been checked. Do not imply investment returns, guaranteed outcomes, risk-free self-custody, inevitable adoption, or universal local conclusions. Do not turn a named service into a recommendation.

Produce a bundle in the guide-specific `Assets/diploma/<student-guide|educator-guide|shared>/<asset-id-lowercase>/` folder selected from the placement. Include `micrographic.html`, `micrographic.css`, `meta.json`, `preview.html` in a 458px review frame, `alt-text.md`, `README.md`, and `sanity-asset.json`. Prefix CSS selectors with a unique `.mg-<slug>` root; tag all translatable text with non-nested `data-t` keys; use no JavaScript, external assets, external fonts, CSS grid, vh/vw, rem, fixed/sticky positioning, or `@import`. Do not upload or publish to Sanity. Before declaring completion, report visual checks at 458px, phone, desktop, A4/US Letter, and grayscale.

Required inputs to attach
- Approved transparent PNG reference: Assets/Reference/bd-v-009-ref.jpg
- Matching white-background JPG preview: Assets/Reference/bd-v-009-ref.jpg
- Matching conformance report: Assets/Reference/bd-v-009-ref.json
- Current Claude Design System authoring instructions and closest approved micrographic bundle
- Current Sanity schema/publishing requirements, if available

Complete asset brief
- Asset ID: BD-V-009
- Suggested by: Pablo
- Priority: Essential
- Type: Image
- Historical page/note: 8–9; add exchange-difficulty examples and a local three-role barter graphic.
- Placement: SG: Under `### Barter and the double coincidence of wants`, after the Amina, Luis, and Mei scenario and before the formal definition. EG: under `### Barter and the double coincidence of wants`, after the sentence beginning `First, let the group attempt direct exchange`. See section 3.8 for the exact anchor.
- Source locator: SG: 337; EG: 1076
- Text–visual link: Makes the failed direct-exchange relationships in the prose visible.
- Design brief: Show Amina with rice wanting shoes, Luis with shoes wanting cooking oil, and Mei with cooking oil wanting repair work. Use broken or unmatched arrows to show why no direct pair satisfies both wants. Keep names and objects editable for localization. Do not show money or a solution in this graphic. Keep this as a single failed-direct-exchange graphic; `BD-V-010` alone shows the money-mediated exchange.
- Format: Single three-role barter-mismatch illustration; full width.

Use the exact heading and insertion direction in Placement as the target placement. Preserve all listed placements in metadata. Include source-brief revision, reference paths, factual sources, production date, reviewer status, checks, and unresolved judgments in README.md. Set `reviewStatus` to draft or review unless an authorized reviewer has approved it.
```
### [ ] BD-V-010 — Diagram

```text
You are building one production-ready, accessible My First Bitcoin Bitcoin Diploma visual from a supplied approved transparent PNG reference, its white-background JPG preview, and their JSON conformance report. Read the complete brief below before acting. The asset brief is the source of truth for lesson intent, content, safety, caption, alt text, placement, and localization. The reference image guides composition only. If it conflicts with the brief, the brief wins; report any unresolved factual or design-system gap before implementing.

Rebuild—not trace or embed—the reference as editable HTML, CSS, and inline SVG. Apply the supplied Claude Design System rather than the reference's provisional styling. Keep all essential geometry, arrows, labels, warnings, icons, and data editable. Preserve one clear teaching relationship, a decisive reading order, cultural replaceability, grayscale meaning, narrow-page responsiveness, phone and desktop usability, A4/US-Letter printing, expandable translated text, and future RTL adaptation.

Never invent facts, labels, numbers, providers, URLs, legal claims, safety claims, or brand choices. Preserve every prohibition and qualification in the brief. Do not include real seed phrases, private keys, payable addresses, private learner data, balances, or transactions. Use a verified QR, address, URL, interface, date, or fact only when the brief explicitly authorizes it and it has been checked. Do not imply investment returns, guaranteed outcomes, risk-free self-custody, inevitable adoption, or universal local conclusions. Do not turn a named service into a recommendation.

Produce a bundle in the guide-specific `Assets/diploma/<student-guide|educator-guide|shared>/<asset-id-lowercase>/` folder selected from the placement. Include `micrographic.html`, `micrographic.css`, `meta.json`, `preview.html` in a 458px review frame, `alt-text.md`, `README.md`, and `sanity-asset.json`. Prefix CSS selectors with a unique `.mg-<slug>` root; tag all translatable text with non-nested `data-t` keys; use no JavaScript, external assets, external fonts, CSS grid, vh/vw, rem, fixed/sticky positioning, or `@import`. Do not upload or publish to Sanity. Before declaring completion, report visual checks at 458px, phone, desktop, A4/US Letter, and grayscale.

Required inputs to attach
- Approved transparent PNG reference: Assets/Reference/bd-v-010-ref.jpg
- Matching white-background JPG preview: Assets/Reference/bd-v-010-ref.jpg
- Matching conformance report: Assets/Reference/bd-v-010-ref.json
- Current Claude Design System authoring instructions and closest approved micrographic bundle
- Current Sanity schema/publishing requirements, if available

Complete asset brief
- Asset ID: BD-V-010
- Suggested by: User
- Priority: Essential
- Type: Diagram
- Historical page/note: 9; separate the money-mediated exchange explanation from the barter-mismatch graphic.
- Placement: SG: Under `### Barter and the double coincidence of wants`, after the paragraph beginning `A commonly accepted money separates selling from buying`. EG: under `### Barter and the double coincidence of wants`, after the sentence beginning `Then introduce a commonly accepted medium`. See section 3.8 for the exact anchor.
- Source locator: SG: 354; EG: 1084
- Text–visual link: Shows that a commonly accepted medium lets a person sell to one party and buy from another.
- Design brief: Show Amina selling rice to one person for a generic commonly accepted medium, then using that medium to buy shoes from another person. Use a simple two-step sequence with distinct arrows for selling and buying. Keep names, goods, and the generic medium editable for localization. Do not use a specific currency, price, brand, wallet, QR code, or claim that money removes every exchange problem.
- Format: Single money-mediated exchange flow; half to full width.

Use the exact heading and insertion direction in Placement as the target placement. Preserve all listed placements in metadata. Include source-brief revision, reference paths, factual sources, production date, reviewer status, checks, and unresolved judgments in README.md. Set `reviewStatus` to draft or review unless an authorized reviewer has approved it.
```
### [ ] BD-V-011 — Image

```text
You are building one production-ready, accessible My First Bitcoin Bitcoin Diploma visual from a supplied approved transparent PNG reference, its white-background JPG preview, and their JSON conformance report. Read the complete brief below before acting. The asset brief is the source of truth for lesson intent, content, safety, caption, alt text, placement, and localization. The reference image guides composition only. If it conflicts with the brief, the brief wins; report any unresolved factual or design-system gap before implementing.

Rebuild—not trace or embed—the reference as editable HTML, CSS, and inline SVG. Apply the supplied Claude Design System rather than the reference's provisional styling. Keep all essential geometry, arrows, labels, warnings, icons, and data editable. Preserve one clear teaching relationship, a decisive reading order, cultural replaceability, grayscale meaning, narrow-page responsiveness, phone and desktop usability, A4/US-Letter printing, expandable translated text, and future RTL adaptation.

Never invent facts, labels, numbers, providers, URLs, legal claims, safety claims, or brand choices. Preserve every prohibition and qualification in the brief. Do not include real seed phrases, private keys, payable addresses, private learner data, balances, or transactions. Use a verified QR, address, URL, interface, date, or fact only when the brief explicitly authorizes it and it has been checked. Do not imply investment returns, guaranteed outcomes, risk-free self-custody, inevitable adoption, or universal local conclusions. Do not turn a named service into a recommendation.

Produce a bundle in the guide-specific `Assets/diploma/<student-guide|educator-guide|shared>/<asset-id-lowercase>/` folder selected from the placement. Include `micrographic.html`, `micrographic.css`, `meta.json`, `preview.html` in a 458px review frame, `alt-text.md`, `README.md`, and `sanity-asset.json`. Prefix CSS selectors with a unique `.mg-<slug>` root; tag all translatable text with non-nested `data-t` keys; use no JavaScript, external assets, external fonts, CSS grid, vh/vw, rem, fixed/sticky positioning, or `@import`. Do not upload or publish to Sanity. Before declaring completion, report visual checks at 458px, phone, desktop, A4/US Letter, and grayscale.

Required inputs to attach
- Approved transparent PNG reference: Assets/Reference/bd-v-011-ref.jpg
- Matching white-background JPG preview: Assets/Reference/bd-v-011-ref.jpg
- Matching conformance report: Assets/Reference/bd-v-011-ref.json
- Current Claude Design System authoring instructions and closest approved micrographic bundle
- Current Sanity schema/publishing requirements, if available

Complete asset brief
- Asset ID: BD-V-011
- Suggested by: Pablo
- Priority: Essential
- Type: Image
- Historical page/note: 10; compare clean water in two contexts to show context-dependent value and price.
- Placement: Under `### Scarcity, value, and exchange`, immediately after the sentence “Clean water may be inexpensive near a safe public source and extremely valuable during a shortage.”
- Source locator: 303
- Text–visual link: Makes the same good's changing value and price clear through a concrete example.
- Design brief: Use two parallel images of the same quantity of clean water. Panel 1: near a safe public source, readily available, with an illustrative lower-price label. Panel 2: during a shortage, limited access and urgent need, with an illustrative higher-price label. State clearly that availability, need, and circumstances change value and price; do not imply that water scarcity or high prices are ethically acceptable. Keep people, setting, language, and price units editable for localization.
- Format: Two-panel contextual-value illustration; half to full width.

Use the exact heading and insertion direction in Placement as the target placement. Preserve all listed placements in metadata. Include source-brief revision, reference paths, factual sources, production date, reviewer status, checks, and unresolved judgments in README.md. Set `reviewStatus` to draft or review unless an authorized reviewer has approved it.
```
### [ ] BD-V-012 — Image

```text
You are building one production-ready, accessible My First Bitcoin Bitcoin Diploma visual from a supplied approved transparent PNG reference, its white-background JPG preview, and their JSON conformance report. Read the complete brief below before acting. The asset brief is the source of truth for lesson intent, content, safety, caption, alt text, placement, and localization. The reference image guides composition only. If it conflicts with the brief, the brief wins; report any unresolved factual or design-system gap before implementing.

Rebuild—not trace or embed—the reference as editable HTML, CSS, and inline SVG. Apply the supplied Claude Design System rather than the reference's provisional styling. Keep all essential geometry, arrows, labels, warnings, icons, and data editable. Preserve one clear teaching relationship, a decisive reading order, cultural replaceability, grayscale meaning, narrow-page responsiveness, phone and desktop usability, A4/US-Letter printing, expandable translated text, and future RTL adaptation.

Never invent facts, labels, numbers, providers, URLs, legal claims, safety claims, or brand choices. Preserve every prohibition and qualification in the brief. Do not include real seed phrases, private keys, payable addresses, private learner data, balances, or transactions. Use a verified QR, address, URL, interface, date, or fact only when the brief explicitly authorizes it and it has been checked. Do not imply investment returns, guaranteed outcomes, risk-free self-custody, inevitable adoption, or universal local conclusions. Do not turn a named service into a recommendation.

Produce a bundle in the guide-specific `Assets/diploma/<student-guide|educator-guide|shared>/<asset-id-lowercase>/` folder selected from the placement. Include `micrographic.html`, `micrographic.css`, `meta.json`, `preview.html` in a 458px review frame, `alt-text.md`, `README.md`, and `sanity-asset.json`. Prefix CSS selectors with a unique `.mg-<slug>` root; tag all translatable text with non-nested `data-t` keys; use no JavaScript, external assets, external fonts, CSS grid, vh/vw, rem, fixed/sticky positioning, or `@import`. Do not upload or publish to Sanity. Before declaring completion, report visual checks at 458px, phone, desktop, A4/US Letter, and grayscale.

Required inputs to attach
- Approved transparent PNG reference: Assets/Reference/bd-v-012-ref.jpg
- Matching white-background JPG preview: Assets/Reference/bd-v-012-ref.jpg
- Matching conformance report: Assets/Reference/bd-v-012-ref.json
- Current Claude Design System authoring instructions and closest approved micrographic bundle
- Current Sanity schema/publishing requirements, if available

Complete asset brief
- Asset ID: BD-V-012
- Suggested by: Pablo
- Priority: Supporting
- Type: Image
- Historical page/note: 10; expand opportunity cost, time preference, and trade-offs with examples and graphics.
- Placement: SG: Under `### Scarcity, value, and exchange`, after the definitions of opportunity cost, time preference, and trade-off. EG: under `### Scarcity, value, and exchange`, replace the matching marker after the source text at the listed EG line. See section 3.8 for the exact anchor.
- Source locator: SG: 311; EG: 1090
- Text–visual link: Connects three abstract choice concepts to one everyday decision.
- Design brief: Show one person choosing between two uses of limited money or time. Label the chosen benefit, the best alternative forgone, the present-versus-future preference, and the resulting trade-off. Do not moralize the learner's choice or imply one time preference is always correct.
- Format: Branching choice illustration; half page.

Use the exact heading and insertion direction in Placement as the target placement. Preserve all listed placements in metadata. Include source-brief revision, reference paths, factual sources, production date, reviewer status, checks, and unresolved judgments in README.md. Set `reviewStatus` to draft or review unless an authorized reviewer has approved it.
```
### [ ] BD-V-013 — Diagram

```text
You are building one production-ready, accessible My First Bitcoin Bitcoin Diploma visual from a supplied approved transparent PNG reference, its white-background JPG preview, and their JSON conformance report. Read the complete brief below before acting. The asset brief is the source of truth for lesson intent, content, safety, caption, alt text, placement, and localization. The reference image guides composition only. If it conflicts with the brief, the brief wins; report any unresolved factual or design-system gap before implementing.

Rebuild—not trace or embed—the reference as editable HTML, CSS, and inline SVG. Apply the supplied Claude Design System rather than the reference's provisional styling. Keep all essential geometry, arrows, labels, warnings, icons, and data editable. Preserve one clear teaching relationship, a decisive reading order, cultural replaceability, grayscale meaning, narrow-page responsiveness, phone and desktop usability, A4/US-Letter printing, expandable translated text, and future RTL adaptation.

Never invent facts, labels, numbers, providers, URLs, legal claims, safety claims, or brand choices. Preserve every prohibition and qualification in the brief. Do not include real seed phrases, private keys, payable addresses, private learner data, balances, or transactions. Use a verified QR, address, URL, interface, date, or fact only when the brief explicitly authorizes it and it has been checked. Do not imply investment returns, guaranteed outcomes, risk-free self-custody, inevitable adoption, or universal local conclusions. Do not turn a named service into a recommendation.

Produce a bundle in the guide-specific `Assets/diploma/<student-guide|educator-guide|shared>/<asset-id-lowercase>/` folder selected from the placement. Include `micrographic.html`, `micrographic.css`, `meta.json`, `preview.html` in a 458px review frame, `alt-text.md`, `README.md`, and `sanity-asset.json`. Prefix CSS selectors with a unique `.mg-<slug>` root; tag all translatable text with non-nested `data-t` keys; use no JavaScript, external assets, external fonts, CSS grid, vh/vw, rem, fixed/sticky positioning, or `@import`. Do not upload or publish to Sanity. Before declaring completion, report visual checks at 458px, phone, desktop, A4/US Letter, and grayscale.

Required inputs to attach
- Approved transparent PNG reference: Assets/Reference/bd-v-013-ref.jpg
- Matching white-background JPG preview: Assets/Reference/bd-v-013-ref.jpg
- Matching conformance report: Assets/Reference/bd-v-013-ref.json
- Current Claude Design System authoring instructions and closest approved micrographic bundle
- Current Sanity schema/publishing requirements, if available

Complete asset brief
- Asset ID: BD-V-013
- Suggested by: Pablo
- Priority: Essential
- Type: Diagram
- Historical page/note: 10–11; add a non-linear money timeline and historical context through modern fiat.
- Placement: SG: Under `### Beginner monetary history from barter to digital money`, after the `Digital money` paragraph. EG: under `### Beginner monetary history`, replace the matching marker after the source text at the listed EG line. See section 3.8 for the exact anchor.
- Source locator: SG: 332; EG: 1112
- Text–visual link: Prevents the history from appearing as one universal, inevitable sequence.
- Design brief: Create several overlapping tracks rather than one straight progress arrow: direct exchange and local records; commodity forms; standard coins; representative paper; bank and government money; modern fiat; digital fiat. Mark that different forms coexist and developed differently across places. Include 1971 only as a dated milestone in the modern-fiat track, not as the origin of all fiat money.
- Format: Braided or layered timeline; full-page width.

Use the exact heading and insertion direction in Placement as the target placement. Preserve all listed placements in metadata. Include source-brief revision, reference paths, factual sources, production date, reviewer status, checks, and unresolved judgments in README.md. Set `reviewStatus` to draft or review unless an authorized reviewer has approved it.
```
### [ ] BD-V-014 — Table

```text
You are building one production-ready, accessible My First Bitcoin Bitcoin Diploma visual from a supplied approved transparent PNG reference, its white-background JPG preview, and their JSON conformance report. Read the complete brief below before acting. The asset brief is the source of truth for lesson intent, content, safety, caption, alt text, placement, and localization. The reference image guides composition only. If it conflicts with the brief, the brief wins; report any unresolved factual or design-system gap before implementing.

Rebuild—not trace or embed—the reference as editable HTML, CSS, and inline SVG. Apply the supplied Claude Design System rather than the reference's provisional styling. Keep all essential geometry, arrows, labels, warnings, icons, and data editable. Preserve one clear teaching relationship, a decisive reading order, cultural replaceability, grayscale meaning, narrow-page responsiveness, phone and desktop usability, A4/US-Letter printing, expandable translated text, and future RTL adaptation.

Never invent facts, labels, numbers, providers, URLs, legal claims, safety claims, or brand choices. Preserve every prohibition and qualification in the brief. Do not include real seed phrases, private keys, payable addresses, private learner data, balances, or transactions. Use a verified QR, address, URL, interface, date, or fact only when the brief explicitly authorizes it and it has been checked. Do not imply investment returns, guaranteed outcomes, risk-free self-custody, inevitable adoption, or universal local conclusions. Do not turn a named service into a recommendation.

Produce a bundle in the guide-specific `Assets/diploma/<student-guide|educator-guide|shared>/<asset-id-lowercase>/` folder selected from the placement. Include `micrographic.html`, `micrographic.css`, `meta.json`, `preview.html` in a 458px review frame, `alt-text.md`, `README.md`, and `sanity-asset.json`. Prefix CSS selectors with a unique `.mg-<slug>` root; tag all translatable text with non-nested `data-t` keys; use no JavaScript, external assets, external fonts, CSS grid, vh/vw, rem, fixed/sticky positioning, or `@import`. Do not upload or publish to Sanity. Before declaring completion, report visual checks at 458px, phone, desktop, A4/US Letter, and grayscale.

Required inputs to attach
- Approved transparent PNG reference: Assets/Reference/bd-v-014-ref.jpg
- Matching white-background JPG preview: Assets/Reference/bd-v-014-ref.jpg
- Matching conformance report: Assets/Reference/bd-v-014-ref.json
- Current Claude Design System authoring instructions and closest approved micrographic bundle
- Current Sanity schema/publishing requirements, if available

Complete asset brief
- Asset ID: BD-V-014
- Suggested by: AI
- Priority: Supporting
- Type: Table
- Historical page/note: 12; make the fiat-system participant table clear and easy to compare.
- Placement: Under `### Fiat money`, replace the existing `Participant / Main role` table visually while retaining an accessible text equivalent.
- Source locator: 344
- Text–visual link: Clarifies the different roles of central banks, commercial banks, governments, and citizens or businesses.
- Design brief: Preserve the four participant rows and their main roles. Use neutral role icons and editable text. Do not imply that every country has the same institutions, powers, or rules.
- Format: Participant-and-role reference table; full width.

Use the exact heading and insertion direction in Placement as the target placement. Preserve all listed placements in metadata. Include source-brief revision, reference paths, factual sources, production date, reviewer status, checks, and unresolved judgments in README.md. Set `reviewStatus` to draft or review unless an authorized reviewer has approved it.
```
### [ ] BD-V-015 — Diagram

```text
You are building one production-ready, accessible My First Bitcoin Bitcoin Diploma visual from a supplied approved transparent PNG reference, its white-background JPG preview, and their JSON conformance report. Read the complete brief below before acting. The asset brief is the source of truth for lesson intent, content, safety, caption, alt text, placement, and localization. The reference image guides composition only. If it conflicts with the brief, the brief wins; report any unresolved factual or design-system gap before implementing.

Rebuild—not trace or embed—the reference as editable HTML, CSS, and inline SVG. Apply the supplied Claude Design System rather than the reference's provisional styling. Keep all essential geometry, arrows, labels, warnings, icons, and data editable. Preserve one clear teaching relationship, a decisive reading order, cultural replaceability, grayscale meaning, narrow-page responsiveness, phone and desktop usability, A4/US-Letter printing, expandable translated text, and future RTL adaptation.

Never invent facts, labels, numbers, providers, URLs, legal claims, safety claims, or brand choices. Preserve every prohibition and qualification in the brief. Do not include real seed phrases, private keys, payable addresses, private learner data, balances, or transactions. Use a verified QR, address, URL, interface, date, or fact only when the brief explicitly authorizes it and it has been checked. Do not imply investment returns, guaranteed outcomes, risk-free self-custody, inevitable adoption, or universal local conclusions. Do not turn a named service into a recommendation.

Produce a bundle in the guide-specific `Assets/diploma/<student-guide|educator-guide|shared>/<asset-id-lowercase>/` folder selected from the placement. Include `micrographic.html`, `micrographic.css`, `meta.json`, `preview.html` in a 458px review frame, `alt-text.md`, `README.md`, and `sanity-asset.json`. Prefix CSS selectors with a unique `.mg-<slug>` root; tag all translatable text with non-nested `data-t` keys; use no JavaScript, external assets, external fonts, CSS grid, vh/vw, rem, fixed/sticky positioning, or `@import`. Do not upload or publish to Sanity. Before declaring completion, report visual checks at 458px, phone, desktop, A4/US Letter, and grayscale.

Required inputs to attach
- Approved transparent PNG reference: Assets/Reference/bd-v-015-ref.jpg
- Matching white-background JPG preview: Assets/Reference/bd-v-015-ref.jpg
- Matching conformance report: Assets/Reference/bd-v-015-ref.json
- Current Claude Design System authoring instructions and closest approved micrographic bundle
- Current Sanity schema/publishing requirements, if available

Complete asset brief
- Asset ID: BD-V-015
- Suggested by: Pablo
- Priority: Supporting
- Type: Diagram
- Historical page/note: 12; turn the fiat-participant table into a guided explanation and clarify liabilities.
- Placement: SG: Under `### Fiat money`, after the participant table. EG: under `### Fiat money and the local system`, replace the matching marker after the source text at the listed EG line. See section 3.8 for the exact anchor.
- Source locator: SG: 349; EG: 1143
- Text–visual link: Shows where trust, claims, and control sit in a fiat payment system.
- Design brief: Map central bank, commercial bank, government, citizens and businesses, and payment services. Use distinct arrows for money or claims, policy or rules, taxes and spending, and payment instructions. Show that a bank deposit is the bank's liability to the customer. Avoid suggesting that every country has identical institutions or rules.
- Format: Actor-and-flow system map; full width.

Use the exact heading and insertion direction in Placement as the target placement. Preserve all listed placements in metadata. Include source-brief revision, reference paths, factual sources, production date, reviewer status, checks, and unresolved judgments in README.md. Set `reviewStatus` to draft or review unless an authorized reviewer has approved it.
```
### [ ] BD-V-016 — Diagram

```text
You are building one production-ready, accessible My First Bitcoin Bitcoin Diploma visual from a supplied approved transparent PNG reference, its white-background JPG preview, and their JSON conformance report. Read the complete brief below before acting. The asset brief is the source of truth for lesson intent, content, safety, caption, alt text, placement, and localization. The reference image guides composition only. If it conflicts with the brief, the brief wins; report any unresolved factual or design-system gap before implementing.

Rebuild—not trace or embed—the reference as editable HTML, CSS, and inline SVG. Apply the supplied Claude Design System rather than the reference's provisional styling. Keep all essential geometry, arrows, labels, warnings, icons, and data editable. Preserve one clear teaching relationship, a decisive reading order, cultural replaceability, grayscale meaning, narrow-page responsiveness, phone and desktop usability, A4/US-Letter printing, expandable translated text, and future RTL adaptation.

Never invent facts, labels, numbers, providers, URLs, legal claims, safety claims, or brand choices. Preserve every prohibition and qualification in the brief. Do not include real seed phrases, private keys, payable addresses, private learner data, balances, or transactions. Use a verified QR, address, URL, interface, date, or fact only when the brief explicitly authorizes it and it has been checked. Do not imply investment returns, guaranteed outcomes, risk-free self-custody, inevitable adoption, or universal local conclusions. Do not turn a named service into a recommendation.

Produce a bundle in the guide-specific `Assets/diploma/<student-guide|educator-guide|shared>/<asset-id-lowercase>/` folder selected from the placement. Include `micrographic.html`, `micrographic.css`, `meta.json`, `preview.html` in a 458px review frame, `alt-text.md`, `README.md`, and `sanity-asset.json`. Prefix CSS selectors with a unique `.mg-<slug>` root; tag all translatable text with non-nested `data-t` keys; use no JavaScript, external assets, external fonts, CSS grid, vh/vw, rem, fixed/sticky positioning, or `@import`. Do not upload or publish to Sanity. Before declaring completion, report visual checks at 458px, phone, desktop, A4/US Letter, and grayscale.

Required inputs to attach
- Approved transparent PNG reference: Assets/Reference/bd-v-016-ref.jpg
- Matching white-background JPG preview: Assets/Reference/bd-v-016-ref.jpg
- Matching conformance report: Assets/Reference/bd-v-016-ref.json
- Current Claude Design System authoring instructions and closest approved micrographic bundle
- Current Sanity schema/publishing requirements, if available

Complete asset brief
- Asset ID: BD-V-016
- Suggested by: Pablo
- Priority: Essential
- Type: Diagram
- Historical page/note: 12; explain deposit-money creation, define liability, and diagram fractional-reserve banking.
- Placement: SG: Under `### Fractional reserve banking`, after the paragraph beginning “When a commercial bank approves a loan” and before the definition of fractional reserve banking. EG: under `### Fractional-reserve banking, liquidity, and solvency`, replace the matching marker after the source text at the listed EG line. See section 3.8 for the exact anchor.
- Source locator: SG: 367; EG: 1168
- Text–visual link: Makes deposit creation and the bank balance sheet clear without relying on a misleading money-multiplier story.
- Design brief: Trace a simplified loan: bank approves loan; bank records a loan asset and a matching deposit liability; borrower can transfer the deposit; settlement and liquidity requirements remain. Label assets and liabilities on both sides. State `simplified example; exact rules vary`. Do not show banks lending out the same physical deposit repeatedly.
- Format: Numbered balance-sheet flow; full width.

Use the exact heading and insertion direction in Placement as the target placement. Preserve all listed placements in metadata. Include source-brief revision, reference paths, factual sources, production date, reviewer status, checks, and unresolved judgments in README.md. Set `reviewStatus` to draft or review unless an authorized reviewer has approved it.
```
### [ ] BD-V-017 — Table

```text
You are building one production-ready, accessible My First Bitcoin Bitcoin Diploma visual from a supplied approved transparent PNG reference, its white-background JPG preview, and their JSON conformance report. Read the complete brief below before acting. The asset brief is the source of truth for lesson intent, content, safety, caption, alt text, placement, and localization. The reference image guides composition only. If it conflicts with the brief, the brief wins; report any unresolved factual or design-system gap before implementing.

Rebuild—not trace or embed—the reference as editable HTML, CSS, and inline SVG. Apply the supplied Claude Design System rather than the reference's provisional styling. Keep all essential geometry, arrows, labels, warnings, icons, and data editable. Preserve one clear teaching relationship, a decisive reading order, cultural replaceability, grayscale meaning, narrow-page responsiveness, phone and desktop usability, A4/US-Letter printing, expandable translated text, and future RTL adaptation.

Never invent facts, labels, numbers, providers, URLs, legal claims, safety claims, or brand choices. Preserve every prohibition and qualification in the brief. Do not include real seed phrases, private keys, payable addresses, private learner data, balances, or transactions. Use a verified QR, address, URL, interface, date, or fact only when the brief explicitly authorizes it and it has been checked. Do not imply investment returns, guaranteed outcomes, risk-free self-custody, inevitable adoption, or universal local conclusions. Do not turn a named service into a recommendation.

Produce a bundle in the guide-specific `Assets/diploma/<student-guide|educator-guide|shared>/<asset-id-lowercase>/` folder selected from the placement. Include `micrographic.html`, `micrographic.css`, `meta.json`, `preview.html` in a 458px review frame, `alt-text.md`, `README.md`, and `sanity-asset.json`. Prefix CSS selectors with a unique `.mg-<slug>` root; tag all translatable text with non-nested `data-t` keys; use no JavaScript, external assets, external fonts, CSS grid, vh/vw, rem, fixed/sticky positioning, or `@import`. Do not upload or publish to Sanity. Before declaring completion, report visual checks at 458px, phone, desktop, A4/US Letter, and grayscale.

Required inputs to attach
- Approved transparent PNG reference: Assets/Reference/bd-v-017-ref.jpg
- Matching white-background JPG preview: Assets/Reference/bd-v-017-ref.jpg
- Matching conformance report: Assets/Reference/bd-v-017-ref.json
- Current Claude Design System authoring instructions and closest approved micrographic bundle
- Current Sanity schema/publishing requirements, if available

Complete asset brief
- Asset ID: BD-V-017
- Suggested by: Pablo
- Priority: Essential
- Type: Table
- Historical page/note: 12; add liquidity-versus-solvency examples.
- Placement: SG: Under `### Fractional reserve banking`, after the liquidity-risk and solvency-risk definitions. EG: under `### Fractional-reserve banking, liquidity, and solvency`, replace the matching marker after the source text at the listed EG line. See section 3.8 for the exact anchor.
- Source locator: SG: 376; EG: 1181
- Text–visual link: Prevents learners from treating liquidity and solvency as the same problem.
- Design brief: Show two parallel simplified bank snapshots. In the liquidity case, assets exceed liabilities but too little is immediately available. In the solvency case, asset value is below liabilities. Use small round example numbers and label them as fictional.
- Format: Side-by-side balance-sheet comparison; half to full width.

Use the exact heading and insertion direction in Placement as the target placement. Preserve all listed placements in metadata. Include source-brief revision, reference paths, factual sources, production date, reviewer status, checks, and unresolved judgments in README.md. Set `reviewStatus` to draft or review unless an authorized reviewer has approved it.
```
### [ ] BD-V-018 — Image

```text
You are building one production-ready, accessible My First Bitcoin Bitcoin Diploma visual from a supplied approved transparent PNG reference, its white-background JPG preview, and their JSON conformance report. Read the complete brief below before acting. The asset brief is the source of truth for lesson intent, content, safety, caption, alt text, placement, and localization. The reference image guides composition only. If it conflicts with the brief, the brief wins; report any unresolved factual or design-system gap before implementing.

Rebuild—not trace or embed—the reference as editable HTML, CSS, and inline SVG. Apply the supplied Claude Design System rather than the reference's provisional styling. Keep all essential geometry, arrows, labels, warnings, icons, and data editable. Preserve one clear teaching relationship, a decisive reading order, cultural replaceability, grayscale meaning, narrow-page responsiveness, phone and desktop usability, A4/US-Letter printing, expandable translated text, and future RTL adaptation.

Never invent facts, labels, numbers, providers, URLs, legal claims, safety claims, or brand choices. Preserve every prohibition and qualification in the brief. Do not include real seed phrases, private keys, payable addresses, private learner data, balances, or transactions. Use a verified QR, address, URL, interface, date, or fact only when the brief explicitly authorizes it and it has been checked. Do not imply investment returns, guaranteed outcomes, risk-free self-custody, inevitable adoption, or universal local conclusions. Do not turn a named service into a recommendation.

Produce a bundle in the guide-specific `Assets/diploma/<student-guide|educator-guide|shared>/<asset-id-lowercase>/` folder selected from the placement. Include `micrographic.html`, `micrographic.css`, `meta.json`, `preview.html` in a 458px review frame, `alt-text.md`, `README.md`, and `sanity-asset.json`. Prefix CSS selectors with a unique `.mg-<slug>` root; tag all translatable text with non-nested `data-t` keys; use no JavaScript, external assets, external fonts, CSS grid, vh/vw, rem, fixed/sticky positioning, or `@import`. Do not upload or publish to Sanity. Before declaring completion, report visual checks at 458px, phone, desktop, A4/US Letter, and grayscale.

Required inputs to attach
- Approved transparent PNG reference: Assets/Reference/bd-v-018-ref.jpg
- Matching white-background JPG preview: Assets/Reference/bd-v-018-ref.jpg
- Matching conformance report: Assets/Reference/bd-v-018-ref.json
- Current Claude Design System authoring instructions and closest approved micrographic bundle
- Current Sanity schema/publishing requirements, if available

Complete asset brief
- Asset ID: BD-V-018
- Suggested by: Pablo
- Priority: Essential
- Type: Image
- Historical page/note: 13; turn inflation and purchasing-power definitions into graphics and local examples.
- Placement: SG: Under `### Inflation and purchasing power`, after the basket example in the second paragraph. EG: under `### Inflation and purchasing power`, replace the matching marker after the source text at the listed EG line. See section 3.8 for the exact anchor.
- Source locator: SG: 388; EG: 1212
- Text–visual link: Shows the inverse relationship between a rising basket price and what a fixed amount of money can buy.
- Design brief: Use the same fixed amount of currency at two dates. At Date A it buys the full basket; at Date B the basket costs more and the fixed amount buys less. Distinguish `price level` from `purchasing power`. Use fictional or sourced-and-dated local values; never mix the two.
- Format: Before-and-after quantity illustration; full width.

Use the exact heading and insertion direction in Placement as the target placement. Preserve all listed placements in metadata. Include source-brief revision, reference paths, factual sources, production date, reviewer status, checks, and unresolved judgments in README.md. Set `reviewStatus` to draft or review unless an authorized reviewer has approved it.
```
### [ ] BD-V-020 — Table

```text
You are building one production-ready, accessible My First Bitcoin Bitcoin Diploma visual from a supplied approved transparent PNG reference, its white-background JPG preview, and their JSON conformance report. Read the complete brief below before acting. The asset brief is the source of truth for lesson intent, content, safety, caption, alt text, placement, and localization. The reference image guides composition only. If it conflicts with the brief, the brief wins; report any unresolved factual or design-system gap before implementing.

Rebuild—not trace or embed—the reference as editable HTML, CSS, and inline SVG. Apply the supplied Claude Design System rather than the reference's provisional styling. Keep all essential geometry, arrows, labels, warnings, icons, and data editable. Preserve one clear teaching relationship, a decisive reading order, cultural replaceability, grayscale meaning, narrow-page responsiveness, phone and desktop usability, A4/US-Letter printing, expandable translated text, and future RTL adaptation.

Never invent facts, labels, numbers, providers, URLs, legal claims, safety claims, or brand choices. Preserve every prohibition and qualification in the brief. Do not include real seed phrases, private keys, payable addresses, private learner data, balances, or transactions. Use a verified QR, address, URL, interface, date, or fact only when the brief explicitly authorizes it and it has been checked. Do not imply investment returns, guaranteed outcomes, risk-free self-custody, inevitable adoption, or universal local conclusions. Do not turn a named service into a recommendation.

Produce a bundle in the guide-specific `Assets/diploma/<student-guide|educator-guide|shared>/<asset-id-lowercase>/` folder selected from the placement. Include `micrographic.html`, `micrographic.css`, `meta.json`, `preview.html` in a 458px review frame, `alt-text.md`, `README.md`, and `sanity-asset.json`. Prefix CSS selectors with a unique `.mg-<slug>` root; tag all translatable text with non-nested `data-t` keys; use no JavaScript, external assets, external fonts, CSS grid, vh/vw, rem, fixed/sticky positioning, or `@import`. Do not upload or publish to Sanity. Before declaring completion, report visual checks at 458px, phone, desktop, A4/US Letter, and grayscale.

Required inputs to attach
- Approved transparent PNG reference: Assets/Reference/bd-v-020-ref.jpg
- Matching white-background JPG preview: Assets/Reference/bd-v-020-ref.jpg
- Matching conformance report: Assets/Reference/bd-v-020-ref.json
- Current Claude Design System authoring instructions and closest approved micrographic bundle
- Current Sanity schema/publishing requirements, if available

Complete asset brief
- Asset ID: BD-V-020
- Suggested by: AI
- Priority: Supporting
- Type: Table
- Historical page/note: 14–15; make the alternatives comparison table easy to evaluate without ranking assets.
- Placement: Under `### Why people look for alternatives`, replace the existing comparison table visually while retaining an accessible text equivalent.
- Source locator: 412
- Text–visual link: Helps learners compare why an asset may be chosen alongside its important trade-offs.
- Design brief: Preserve precious metals, real estate, and stocks with columns for `Why people may choose it` and `Important trade-offs`. Add simple, non-promotional icons. Do not add investment advice, price predictions, or a best-choice ranking.
- Format: Alternatives trade-off table; full width.

Use the exact heading and insertion direction in Placement as the target placement. Preserve all listed placements in metadata. Include source-brief revision, reference paths, factual sources, production date, reviewer status, checks, and unresolved judgments in README.md. Set `reviewStatus` to draft or review unless an authorized reviewer has approved it.
```
### [ ] BD-V-021 — Diagram

```text
You are building one production-ready, accessible My First Bitcoin Bitcoin Diploma visual from a supplied approved transparent PNG reference, its white-background JPG preview, and their JSON conformance report. Read the complete brief below before acting. The asset brief is the source of truth for lesson intent, content, safety, caption, alt text, placement, and localization. The reference image guides composition only. If it conflicts with the brief, the brief wins; report any unresolved factual or design-system gap before implementing.

Rebuild—not trace or embed—the reference as editable HTML, CSS, and inline SVG. Apply the supplied Claude Design System rather than the reference's provisional styling. Keep all essential geometry, arrows, labels, warnings, icons, and data editable. Preserve one clear teaching relationship, a decisive reading order, cultural replaceability, grayscale meaning, narrow-page responsiveness, phone and desktop usability, A4/US-Letter printing, expandable translated text, and future RTL adaptation.

Never invent facts, labels, numbers, providers, URLs, legal claims, safety claims, or brand choices. Preserve every prohibition and qualification in the brief. Do not include real seed phrases, private keys, payable addresses, private learner data, balances, or transactions. Use a verified QR, address, URL, interface, date, or fact only when the brief explicitly authorizes it and it has been checked. Do not imply investment returns, guaranteed outcomes, risk-free self-custody, inevitable adoption, or universal local conclusions. Do not turn a named service into a recommendation.

Produce a bundle in the guide-specific `Assets/diploma/<student-guide|educator-guide|shared>/<asset-id-lowercase>/` folder selected from the placement. Include `micrographic.html`, `micrographic.css`, `meta.json`, `preview.html` in a 458px review frame, `alt-text.md`, `README.md`, and `sanity-asset.json`. Prefix CSS selectors with a unique `.mg-<slug>` root; tag all translatable text with non-nested `data-t` keys; use no JavaScript, external assets, external fonts, CSS grid, vh/vw, rem, fixed/sticky positioning, or `@import`. Do not upload or publish to Sanity. Before declaring completion, report visual checks at 458px, phone, desktop, A4/US Letter, and grayscale.

Required inputs to attach
- Approved transparent PNG reference: Assets/Reference/bd-v-021-ref.jpg
- Matching white-background JPG preview: Assets/Reference/bd-v-021-ref.jpg
- Matching conformance report: Assets/Reference/bd-v-021-ref.json
- Current Claude Design System authoring instructions and closest approved micrographic bundle
- Current Sanity schema/publishing requirements, if available

Complete asset brief
- Asset ID: BD-V-021
- Suggested by: AI
- Priority: Supporting
- Type: Diagram
- Historical page/note: 14–15; add local real-estate context and clarify assets versus money.
- Placement: Under `### Why people look for alternatives`, after the existing comparison table.
- Source locator: 416
- Text–visual link: Reinforces that each alternative serves some purposes while introducing different constraints.
- Design brief: Place cash, precious metals, real estate, stocks, and Bitcoin around the needs `daily payment`, `long-term saving`, `portability`, `income or productive use`, and `direct control`. Use qualitative callouts, not a ranked score or investment recommendation.
- Format: Trade-off landscape; full width.

Use the exact heading and insertion direction in Placement as the target placement. Preserve all listed placements in metadata. Include source-brief revision, reference paths, factual sources, production date, reviewer status, checks, and unresolved judgments in README.md. Set `reviewStatus` to draft or review unless an authorized reviewer has approved it.
```
### [ ] BD-V-019 — Table

```text
You are building one production-ready, accessible My First Bitcoin Bitcoin Diploma visual from a supplied approved transparent PNG reference, its white-background JPG preview, and their JSON conformance report. Read the complete brief below before acting. The asset brief is the source of truth for lesson intent, content, safety, caption, alt text, placement, and localization. The reference image guides composition only. If it conflicts with the brief, the brief wins; report any unresolved factual or design-system gap before implementing.

Rebuild—not trace or embed—the reference as editable HTML, CSS, and inline SVG. Apply the supplied Claude Design System rather than the reference's provisional styling. Keep all essential geometry, arrows, labels, warnings, icons, and data editable. Preserve one clear teaching relationship, a decisive reading order, cultural replaceability, grayscale meaning, narrow-page responsiveness, phone and desktop usability, A4/US-Letter printing, expandable translated text, and future RTL adaptation.

Never invent facts, labels, numbers, providers, URLs, legal claims, safety claims, or brand choices. Preserve every prohibition and qualification in the brief. Do not include real seed phrases, private keys, payable addresses, private learner data, balances, or transactions. Use a verified QR, address, URL, interface, date, or fact only when the brief explicitly authorizes it and it has been checked. Do not imply investment returns, guaranteed outcomes, risk-free self-custody, inevitable adoption, or universal local conclusions. Do not turn a named service into a recommendation.

Produce a bundle in the guide-specific `Assets/diploma/<student-guide|educator-guide|shared>/<asset-id-lowercase>/` folder selected from the placement. Include `micrographic.html`, `micrographic.css`, `meta.json`, `preview.html` in a 458px review frame, `alt-text.md`, `README.md`, and `sanity-asset.json`. Prefix CSS selectors with a unique `.mg-<slug>` root; tag all translatable text with non-nested `data-t` keys; use no JavaScript, external assets, external fonts, CSS grid, vh/vw, rem, fixed/sticky positioning, or `@import`. Do not upload or publish to Sanity. Before declaring completion, report visual checks at 458px, phone, desktop, A4/US Letter, and grayscale.

Required inputs to attach
- Approved transparent PNG reference: Assets/Reference/bd-v-019-ref.jpg
- Matching white-background JPG preview: Assets/Reference/bd-v-019-ref.jpg
- Matching conformance report: Assets/Reference/bd-v-019-ref.json
- Current Claude Design System authoring instructions and closest approved micrographic bundle
- Current Sanity schema/publishing requirements, if available

Complete asset brief
- Asset ID: BD-V-019
- Suggested by: AI
- Priority: Supporting
- Type: Table
- Historical page/note: 14; add current CBDC examples and explain risks, benefits, privacy, and control.
- Placement: SG: Under `### Central Bank Digital Currencies (CBDCs)`, after the paragraph beginning “A CBDC does not create a fixed monetary supply” EG: under `### CBDCs as digital fiat`, replace the matching marker after the source text at the listed EG line. See section 3.8 for the exact anchor.
- Source locator: SG: 432; EG: 1280
- Text–visual link: Clarifies that digital, centralized, decentralized, private, and scarce are different attributes.
- Design brief: Compare physical cash, commercial-bank digital deposits, a generic retail CBDC, and Bitcoin across issuer or controller, form, access permission, visibility, supply-rule control, and independent verifiability. Mark CBDC features as design-dependent. Do not imply that all CBDCs have identical surveillance or control features.
- Format: Layered comparison matrix with icons; full width.

Use the exact heading and insertion direction in Placement as the target placement. Preserve all listed placements in metadata. Include source-brief revision, reference paths, factual sources, production date, reviewer status, checks, and unresolved judgments in README.md. Set `reviewStatus` to draft or review unless an authorized reviewer has approved it.
```

## 3.3 Module 2: How Bitcoin Works

### [ ] BD-V-022 — Diagram

```text
You are building one production-ready, accessible My First Bitcoin Bitcoin Diploma visual from a supplied approved transparent PNG reference, its white-background JPG preview, and their JSON conformance report. Read the complete brief below before acting. The asset brief is the source of truth for lesson intent, content, safety, caption, alt text, placement, and localization. The reference image guides composition only. If it conflicts with the brief, the brief wins; report any unresolved factual or design-system gap before implementing.

Rebuild—not trace or embed—the reference as editable HTML, CSS, and inline SVG. Apply the supplied Claude Design System rather than the reference's provisional styling. Keep all essential geometry, arrows, labels, warnings, icons, and data editable. Preserve one clear teaching relationship, a decisive reading order, cultural replaceability, grayscale meaning, narrow-page responsiveness, phone and desktop usability, A4/US-Letter printing, expandable translated text, and future RTL adaptation.

Never invent facts, labels, numbers, providers, URLs, legal claims, safety claims, or brand choices. Preserve every prohibition and qualification in the brief. Do not include real seed phrases, private keys, payable addresses, private learner data, balances, or transactions. Use a verified QR, address, URL, interface, date, or fact only when the brief explicitly authorizes it and it has been checked. Do not imply investment returns, guaranteed outcomes, risk-free self-custody, inevitable adoption, or universal local conclusions. Do not turn a named service into a recommendation.

Produce a bundle in the guide-specific `Assets/diploma/<student-guide|educator-guide|shared>/<asset-id-lowercase>/` folder selected from the placement. Include `micrographic.html`, `micrographic.css`, `meta.json`, `preview.html` in a 458px review frame, `alt-text.md`, `README.md`, and `sanity-asset.json`. Prefix CSS selectors with a unique `.mg-<slug>` root; tag all translatable text with non-nested `data-t` keys; use no JavaScript, external assets, external fonts, CSS grid, vh/vw, rem, fixed/sticky positioning, or `@import`. Do not upload or publish to Sanity. Before declaring completion, report visual checks at 458px, phone, desktop, A4/US Letter, and grayscale.

Required inputs to attach
- Approved transparent PNG reference: Assets/Reference/bd-v-022-ref.jpg
- Matching white-background JPG preview: Assets/Reference/bd-v-022-ref.jpg
- Matching conformance report: Assets/Reference/bd-v-022-ref.json
- Current Claude Design System authoring instructions and closest approved micrographic bundle
- Current Sanity schema/publishing requirements, if available

Complete asset brief
- Asset ID: BD-V-022
- Suggested by: AI
- Priority: Essential
- Type: Diagram
- Historical page/note: 16; make intermediary power and risk concrete and define digital signatures.
- Placement: SG: Under `### Why Bitcoin was created`, after the paragraph beginning “Bitcoin was created to solve this problem” EG: under `### Why Bitcoin was created`, replace the matching marker after the source text at the listed EG line. See section 3.8 for the exact anchor.
- Source locator: SG: 478; EG: 1412
- Text–visual link: Contrasts a central ledger keeper with Bitcoin's distributed verification model.
- Design brief: Left panel: sender and receiver depend on one intermediary that keeps and approves the ledger. Right panel: signed transactions propagate to independent nodes; miners propose blocks; nodes verify the same public rules. Emphasize reduced dependence on a central settlement authority, not removal of all trust.
- Format: Two-system comparison diagram; full width.

Use the exact heading and insertion direction in Placement as the target placement. Preserve all listed placements in metadata. Include source-brief revision, reference paths, factual sources, production date, reviewer status, checks, and unresolved judgments in README.md. Set `reviewStatus` to draft or review unless an authorized reviewer has approved it.
```
### [ ] BD-V-023 — Diagram

```text
You are building one production-ready, accessible My First Bitcoin Bitcoin Diploma visual from a supplied approved transparent PNG reference, its white-background JPG preview, and their JSON conformance report. Read the complete brief below before acting. The asset brief is the source of truth for lesson intent, content, safety, caption, alt text, placement, and localization. The reference image guides composition only. If it conflicts with the brief, the brief wins; report any unresolved factual or design-system gap before implementing.

Rebuild—not trace or embed—the reference as editable HTML, CSS, and inline SVG. Apply the supplied Claude Design System rather than the reference's provisional styling. Keep all essential geometry, arrows, labels, warnings, icons, and data editable. Preserve one clear teaching relationship, a decisive reading order, cultural replaceability, grayscale meaning, narrow-page responsiveness, phone and desktop usability, A4/US-Letter printing, expandable translated text, and future RTL adaptation.

Never invent facts, labels, numbers, providers, URLs, legal claims, safety claims, or brand choices. Preserve every prohibition and qualification in the brief. Do not include real seed phrases, private keys, payable addresses, private learner data, balances, or transactions. Use a verified QR, address, URL, interface, date, or fact only when the brief explicitly authorizes it and it has been checked. Do not imply investment returns, guaranteed outcomes, risk-free self-custody, inevitable adoption, or universal local conclusions. Do not turn a named service into a recommendation.

Produce a bundle in the guide-specific `Assets/diploma/<student-guide|educator-guide|shared>/<asset-id-lowercase>/` folder selected from the placement. Include `micrographic.html`, `micrographic.css`, `meta.json`, `preview.html` in a 458px review frame, `alt-text.md`, `README.md`, and `sanity-asset.json`. Prefix CSS selectors with a unique `.mg-<slug>` root; tag all translatable text with non-nested `data-t` keys; use no JavaScript, external assets, external fonts, CSS grid, vh/vw, rem, fixed/sticky positioning, or `@import`. Do not upload or publish to Sanity. Before declaring completion, report visual checks at 458px, phone, desktop, A4/US Letter, and grayscale.

Required inputs to attach
- Approved transparent PNG reference: Assets/Reference/bd-v-023-ref.jpg
- Matching white-background JPG preview: Assets/Reference/bd-v-023-ref.jpg
- Matching conformance report: Assets/Reference/bd-v-023-ref.json
- Current Claude Design System authoring instructions and closest approved micrographic bundle
- Current Sanity schema/publishing requirements, if available

Complete asset brief
- Asset ID: BD-V-023
- Suggested by: AI
- Priority: Supporting
- Type: Diagram
- Historical page/note: 17; attribute the earlier contributors and ideas on which Bitcoin was built.
- Placement: Under `### The search for digital and decentralized money`, after the paragraph beginning “Bitcoin was built upon decades of work by many people.”
- Source locator: 494
- Text–visual link: Shows that Bitcoin combined prior ideas rather than appearing without context.
- Design brief: Create an idea lineage with DigiCash, Hashcash, Bit Gold, B-money, reusable proof of work, and peer-to-peer file sharing feeding distinct contributions toward Bitcoin. Label contributions carefully; do not imply that every project directly supplied code or that Bitcoin has one intellectual predecessor.
- Format: Converging idea timeline; full width.

Use the exact heading and insertion direction in Placement as the target placement. Preserve all listed placements in metadata. Include source-brief revision, reference paths, factual sources, production date, reviewer status, checks, and unresolved judgments in README.md. Set `reviewStatus` to draft or review unless an authorized reviewer has approved it.
```
### [ ] BD-V-024 — Diagram

```text
You are building one production-ready, accessible My First Bitcoin Bitcoin Diploma visual from a supplied approved transparent PNG reference, its white-background JPG preview, and their JSON conformance report. Read the complete brief below before acting. The asset brief is the source of truth for lesson intent, content, safety, caption, alt text, placement, and localization. The reference image guides composition only. If it conflicts with the brief, the brief wins; report any unresolved factual or design-system gap before implementing.

Rebuild—not trace or embed—the reference as editable HTML, CSS, and inline SVG. Apply the supplied Claude Design System rather than the reference's provisional styling. Keep all essential geometry, arrows, labels, warnings, icons, and data editable. Preserve one clear teaching relationship, a decisive reading order, cultural replaceability, grayscale meaning, narrow-page responsiveness, phone and desktop usability, A4/US-Letter printing, expandable translated text, and future RTL adaptation.

Never invent facts, labels, numbers, providers, URLs, legal claims, safety claims, or brand choices. Preserve every prohibition and qualification in the brief. Do not include real seed phrases, private keys, payable addresses, private learner data, balances, or transactions. Use a verified QR, address, URL, interface, date, or fact only when the brief explicitly authorizes it and it has been checked. Do not imply investment returns, guaranteed outcomes, risk-free self-custody, inevitable adoption, or universal local conclusions. Do not turn a named service into a recommendation.

Produce a bundle in the guide-specific `Assets/diploma/<student-guide|educator-guide|shared>/<asset-id-lowercase>/` folder selected from the placement. Include `micrographic.html`, `micrographic.css`, `meta.json`, `preview.html` in a 458px review frame, `alt-text.md`, `README.md`, and `sanity-asset.json`. Prefix CSS selectors with a unique `.mg-<slug>` root; tag all translatable text with non-nested `data-t` keys; use no JavaScript, external assets, external fonts, CSS grid, vh/vw, rem, fixed/sticky positioning, or `@import`. Do not upload or publish to Sanity. Before declaring completion, report visual checks at 458px, phone, desktop, A4/US Letter, and grayscale.

Required inputs to attach
- Approved transparent PNG reference: Assets/Reference/bd-v-024-ref.jpg
- Matching white-background JPG preview: Assets/Reference/bd-v-024-ref.jpg
- Matching conformance report: Assets/Reference/bd-v-024-ref.json
- Current Claude Design System authoring instructions and closest approved micrographic bundle
- Current Sanity schema/publishing requirements, if available

Complete asset brief
- Asset ID: BD-V-024
- Suggested by: AI
- Priority: Essential
- Type: Diagram
- Historical page/note: 17; format, visually clarify, and fact-check the four-step transaction/miner/node process.
- Placement: SG: Under `### Early digital-money attempts and the double-spend problem`, after the five numbered features introduced by “The whitepaper brought together the features needed for that approach”. EG: under `### Explain the combined response`, replace the matching marker after the source text at the listed EG line. See section 3.8 for the exact anchor.
- Source locator: SG: 522; EG: 1446
- Text–visual link: Explains how a conflicting second spend is resolved without a central database.
- Design brief: Begin with one spendable output and two conflicting payment attempts. Show the five linked features from the text: peer-to-peer announcement; digital signatures; blocks and mining; independent verification; and a shared valid history with the most accumulated proof of work. Show the conflicting second spend rejected. Do not imply that one miner decides validity or that the longest chain is accepted regardless of its validity.
- Format: Five-feature conflict-resolution flow; full width.

Use the exact heading and insertion direction in Placement as the target placement. Preserve all listed placements in metadata. Include source-brief revision, reference paths, factual sources, production date, reviewer status, checks, and unresolved judgments in README.md. Set `reviewStatus` to draft or review unless an authorized reviewer has approved it.
```
### [ ] BD-V-027 — Diagram

```text
You are building one production-ready, accessible My First Bitcoin Bitcoin Diploma visual from a supplied approved transparent PNG reference, its white-background JPG preview, and their JSON conformance report. Read the complete brief below before acting. The asset brief is the source of truth for lesson intent, content, safety, caption, alt text, placement, and localization. The reference image guides composition only. If it conflicts with the brief, the brief wins; report any unresolved factual or design-system gap before implementing.

Rebuild—not trace or embed—the reference as editable HTML, CSS, and inline SVG. Apply the supplied Claude Design System rather than the reference's provisional styling. Keep all essential geometry, arrows, labels, warnings, icons, and data editable. Preserve one clear teaching relationship, a decisive reading order, cultural replaceability, grayscale meaning, narrow-page responsiveness, phone and desktop usability, A4/US-Letter printing, expandable translated text, and future RTL adaptation.

Never invent facts, labels, numbers, providers, URLs, legal claims, safety claims, or brand choices. Preserve every prohibition and qualification in the brief. Do not include real seed phrases, private keys, payable addresses, private learner data, balances, or transactions. Use a verified QR, address, URL, interface, date, or fact only when the brief explicitly authorizes it and it has been checked. Do not imply investment returns, guaranteed outcomes, risk-free self-custody, inevitable adoption, or universal local conclusions. Do not turn a named service into a recommendation.

Produce a bundle in the guide-specific `Assets/diploma/<student-guide|educator-guide|shared>/<asset-id-lowercase>/` folder selected from the placement. Include `micrographic.html`, `micrographic.css`, `meta.json`, `preview.html` in a 458px review frame, `alt-text.md`, `README.md`, and `sanity-asset.json`. Prefix CSS selectors with a unique `.mg-<slug>` root; tag all translatable text with non-nested `data-t` keys; use no JavaScript, external assets, external fonts, CSS grid, vh/vw, rem, fixed/sticky positioning, or `@import`. Do not upload or publish to Sanity. Before declaring completion, report visual checks at 458px, phone, desktop, A4/US Letter, and grayscale.

Required inputs to attach
- Approved transparent PNG reference: Assets/Reference/bd-v-027-ref.jpg
- Matching white-background JPG preview: Assets/Reference/bd-v-027-ref.jpg
- Matching conformance report: Assets/Reference/bd-v-027-ref.json
- Current Claude Design System authoring instructions and closest approved micrographic bundle
- Current Sanity schema/publishing requirements, if available

Complete asset brief
- Asset ID: BD-V-027
- Suggested by: AI
- Priority: Supporting
- Type: Diagram
- Historical page/note: 19; distinguish supply claims, subsidy, and node-enforced issuance facts.
- Placement: Under `### Digital scarcity and credible scarcity`, after the final paragraph beginning “Scarcity is more credible”.
- Source locator: 532
- Text–visual link: Distinguishes a written supply claim from a supply rule independently enforced in practice.
- Design brief: Compare `claim on a website or issuer database` with `public rule checked by many independent nodes`. Show that signatures, transaction history, proof of work, and node verification jointly prevent invalid creation or double spending. Avoid saying that scarcity alone creates value.
- Format: Credibility comparison diagram; half to full width.

Use the exact heading and insertion direction in Placement as the target placement. Preserve all listed placements in metadata. Include source-brief revision, reference paths, factual sources, production date, reviewer status, checks, and unresolved judgments in README.md. Set `reviewStatus` to draft or review unless an authorized reviewer has approved it.
```
### [ ] BD-V-026 — Diagram

```text
You are building one production-ready, accessible My First Bitcoin Bitcoin Diploma visual from a supplied approved transparent PNG reference, its white-background JPG preview, and their JSON conformance report. Read the complete brief below before acting. The asset brief is the source of truth for lesson intent, content, safety, caption, alt text, placement, and localization. The reference image guides composition only. If it conflicts with the brief, the brief wins; report any unresolved factual or design-system gap before implementing.

Rebuild—not trace or embed—the reference as editable HTML, CSS, and inline SVG. Apply the supplied Claude Design System rather than the reference's provisional styling. Keep all essential geometry, arrows, labels, warnings, icons, and data editable. Preserve one clear teaching relationship, a decisive reading order, cultural replaceability, grayscale meaning, narrow-page responsiveness, phone and desktop usability, A4/US-Letter printing, expandable translated text, and future RTL adaptation.

Never invent facts, labels, numbers, providers, URLs, legal claims, safety claims, or brand choices. Preserve every prohibition and qualification in the brief. Do not include real seed phrases, private keys, payable addresses, private learner data, balances, or transactions. Use a verified QR, address, URL, interface, date, or fact only when the brief explicitly authorizes it and it has been checked. Do not imply investment returns, guaranteed outcomes, risk-free self-custody, inevitable adoption, or universal local conclusions. Do not turn a named service into a recommendation.

Produce a bundle in the guide-specific `Assets/diploma/<student-guide|educator-guide|shared>/<asset-id-lowercase>/` folder selected from the placement. Include `micrographic.html`, `micrographic.css`, `meta.json`, `preview.html` in a 458px review frame, `alt-text.md`, `README.md`, and `sanity-asset.json`. Prefix CSS selectors with a unique `.mg-<slug>` root; tag all translatable text with non-nested `data-t` keys; use no JavaScript, external assets, external fonts, CSS grid, vh/vw, rem, fixed/sticky positioning, or `@import`. Do not upload or publish to Sanity. Before declaring completion, report visual checks at 458px, phone, desktop, A4/US Letter, and grayscale.

Required inputs to attach
- Approved transparent PNG reference: Assets/Reference/bd-v-026-ref.jpg
- Matching white-background JPG preview: Assets/Reference/bd-v-026-ref.jpg
- Matching conformance report: Assets/Reference/bd-v-026-ref.json
- Current Claude Design System authoring instructions and closest approved micrographic bundle
- Current Sanity schema/publishing requirements, if available

Complete asset brief
- Asset ID: BD-V-026
- Suggested by: AI
- Priority: Essential
- Type: Diagram
- Historical page/note: 19; clarify decentralization roles, unilateral limits, economic nodes, and trade-offs.
- Placement: SG: Under `### Decentralization`, after the list of decentralizing features and before the paragraph beginning “Decentralization is not the same as equal influence.” EG: under `### Decentralization and peer-to-peer transfer`, replace the matching marker after the source text at the listed EG line. See section 3.8 for the exact anchor.
- Source locator: SG: 556; EG: 1478
- Text–visual link: Makes the distribution and limits of participant power visible.
- Design brief: Place users, nodes, miners, developers, and services around the shared protocol and public ledger. For each, show `can do` and `cannot do unilaterally`. Services must sit outside the protocol boundary. Show unequal influence and points of dependence without adding a central controller.
- Format: Roles-and-rules network map; full width.

Use the exact heading and insertion direction in Placement as the target placement. Preserve all listed placements in metadata. Include source-brief revision, reference paths, factual sources, production date, reviewer status, checks, and unresolved judgments in README.md. Set `reviewStatus` to draft or review unless an authorized reviewer has approved it.
```
### [ ] BD-V-030 — Diagram

```text
You are building one production-ready, accessible My First Bitcoin Bitcoin Diploma visual from a supplied approved transparent PNG reference, its white-background JPG preview, and their JSON conformance report. Read the complete brief below before acting. The asset brief is the source of truth for lesson intent, content, safety, caption, alt text, placement, and localization. The reference image guides composition only. If it conflicts with the brief, the brief wins; report any unresolved factual or design-system gap before implementing.

Rebuild—not trace or embed—the reference as editable HTML, CSS, and inline SVG. Apply the supplied Claude Design System rather than the reference's provisional styling. Keep all essential geometry, arrows, labels, warnings, icons, and data editable. Preserve one clear teaching relationship, a decisive reading order, cultural replaceability, grayscale meaning, narrow-page responsiveness, phone and desktop usability, A4/US-Letter printing, expandable translated text, and future RTL adaptation.

Never invent facts, labels, numbers, providers, URLs, legal claims, safety claims, or brand choices. Preserve every prohibition and qualification in the brief. Do not include real seed phrases, private keys, payable addresses, private learner data, balances, or transactions. Use a verified QR, address, URL, interface, date, or fact only when the brief explicitly authorizes it and it has been checked. Do not imply investment returns, guaranteed outcomes, risk-free self-custody, inevitable adoption, or universal local conclusions. Do not turn a named service into a recommendation.

Produce a bundle in the guide-specific `Assets/diploma/<student-guide|educator-guide|shared>/<asset-id-lowercase>/` folder selected from the placement. Include `micrographic.html`, `micrographic.css`, `meta.json`, `preview.html` in a 458px review frame, `alt-text.md`, `README.md`, and `sanity-asset.json`. Prefix CSS selectors with a unique `.mg-<slug>` root; tag all translatable text with non-nested `data-t` keys; use no JavaScript, external assets, external fonts, CSS grid, vh/vw, rem, fixed/sticky positioning, or `@import`. Do not upload or publish to Sanity. Before declaring completion, report visual checks at 458px, phone, desktop, A4/US Letter, and grayscale.

Required inputs to attach
- Approved transparent PNG reference: Assets/Reference/bd-v-030-ref.jpg
- Matching white-background JPG preview: Assets/Reference/bd-v-030-ref.jpg
- Matching conformance report: Assets/Reference/bd-v-030-ref.json
- Current Claude Design System authoring instructions and closest approved micrographic bundle
- Current Sanity schema/publishing requirements, if available

Complete asset brief
- Asset ID: BD-V-030
- Suggested by: AI
- Priority: Supporting
- Type: Diagram
- Historical page/note: 21; distinguish the Bitcoin network from services and intermediaries.
- Placement: Under `### Peer-to-peer transfer`, after the paragraph explaining that peer-to-peer does not always mean only two computers communicate.
- Source locator: 572
- Text–visual link: Separates direct settlement rules from the communications and service infrastructure a transaction may pass through.
- Design brief: Show sender wallet → network peers → recipient wallet, with optional exchange, hosted wallet, payment service, and internet provider around the path. Use different line styles for transaction propagation, custody, and communications. The presence of network infrastructure must not be mistaken for central approval.
- Format: Layered transfer-path diagram; full width.

Use the exact heading and insertion direction in Placement as the target placement. Preserve all listed placements in metadata. Include source-brief revision, reference paths, factual sources, production date, reviewer status, checks, and unresolved judgments in README.md. Set `reviewStatus` to draft or review unless an authorized reviewer has approved it.
```
### [ ] BD-V-031 — Diagram

```text
You are building one production-ready, accessible My First Bitcoin Bitcoin Diploma visual from a supplied approved transparent PNG reference, its white-background JPG preview, and their JSON conformance report. Read the complete brief below before acting. The asset brief is the source of truth for lesson intent, content, safety, caption, alt text, placement, and localization. The reference image guides composition only. If it conflicts with the brief, the brief wins; report any unresolved factual or design-system gap before implementing.

Rebuild—not trace or embed—the reference as editable HTML, CSS, and inline SVG. Apply the supplied Claude Design System rather than the reference's provisional styling. Keep all essential geometry, arrows, labels, warnings, icons, and data editable. Preserve one clear teaching relationship, a decisive reading order, cultural replaceability, grayscale meaning, narrow-page responsiveness, phone and desktop usability, A4/US-Letter printing, expandable translated text, and future RTL adaptation.

Never invent facts, labels, numbers, providers, URLs, legal claims, safety claims, or brand choices. Preserve every prohibition and qualification in the brief. Do not include real seed phrases, private keys, payable addresses, private learner data, balances, or transactions. Use a verified QR, address, URL, interface, date, or fact only when the brief explicitly authorizes it and it has been checked. Do not imply investment returns, guaranteed outcomes, risk-free self-custody, inevitable adoption, or universal local conclusions. Do not turn a named service into a recommendation.

Produce a bundle in the guide-specific `Assets/diploma/<student-guide|educator-guide|shared>/<asset-id-lowercase>/` folder selected from the placement. Include `micrographic.html`, `micrographic.css`, `meta.json`, `preview.html` in a 458px review frame, `alt-text.md`, `README.md`, and `sanity-asset.json`. Prefix CSS selectors with a unique `.mg-<slug>` root; tag all translatable text with non-nested `data-t` keys; use no JavaScript, external assets, external fonts, CSS grid, vh/vw, rem, fixed/sticky positioning, or `@import`. Do not upload or publish to Sanity. Before declaring completion, report visual checks at 458px, phone, desktop, A4/US Letter, and grayscale.

Required inputs to attach
- Approved transparent PNG reference: Assets/Reference/bd-v-031-ref.jpg
- Matching white-background JPG preview: Assets/Reference/bd-v-031-ref.jpg
- Matching conformance report: Assets/Reference/bd-v-031-ref.json
- Current Claude Design System authoring instructions and closest approved micrographic bundle
- Current Sanity schema/publishing requirements, if available

Complete asset brief
- Asset ID: BD-V-031
- Suggested by: AI
- Priority: Essential
- Type: Diagram
- Historical page/note: 21; clarify users, wallet clients, full nodes, and developer proposals.
- Placement: SG: Under `### Users, nodes, and miners`, after the paragraph on developers and before “These roles limit one another.” EG: under `### Users, nodes, miners, developers, and services`, replace the matching marker after the source text at the listed EG line. See section 3.8 for the exact anchor.
- Source locator: SG: 590; EG: 1496
- Text–visual link: Gives beginners a durable model of who does what in Bitcoin.
- Design brief: Show users signing or accepting transactions; nodes validating and relaying; miners assembling candidate blocks and performing proof of work; developers proposing software; services serving customers. Then show the checks among roles. Do not label all wallet users as nodes or developers as rule-makers.
- Format: Participant role map; full width.

Use the exact heading and insertion direction in Placement as the target placement. Preserve all listed placements in metadata. Include source-brief revision, reference paths, factual sources, production date, reviewer status, checks, and unresolved judgments in README.md. Set `reviewStatus` to draft or review unless an authorized reviewer has approved it.
```
### [ ] BD-V-032 — Diagram

```text
You are building one production-ready, accessible My First Bitcoin Bitcoin Diploma visual from a supplied approved transparent PNG reference, its white-background JPG preview, and their JSON conformance report. Read the complete brief below before acting. The asset brief is the source of truth for lesson intent, content, safety, caption, alt text, placement, and localization. The reference image guides composition only. If it conflicts with the brief, the brief wins; report any unresolved factual or design-system gap before implementing.

Rebuild—not trace or embed—the reference as editable HTML, CSS, and inline SVG. Apply the supplied Claude Design System rather than the reference's provisional styling. Keep all essential geometry, arrows, labels, warnings, icons, and data editable. Preserve one clear teaching relationship, a decisive reading order, cultural replaceability, grayscale meaning, narrow-page responsiveness, phone and desktop usability, A4/US-Letter printing, expandable translated text, and future RTL adaptation.

Never invent facts, labels, numbers, providers, URLs, legal claims, safety claims, or brand choices. Preserve every prohibition and qualification in the brief. Do not include real seed phrases, private keys, payable addresses, private learner data, balances, or transactions. Use a verified QR, address, URL, interface, date, or fact only when the brief explicitly authorizes it and it has been checked. Do not imply investment returns, guaranteed outcomes, risk-free self-custody, inevitable adoption, or universal local conclusions. Do not turn a named service into a recommendation.

Produce a bundle in the guide-specific `Assets/diploma/<student-guide|educator-guide|shared>/<asset-id-lowercase>/` folder selected from the placement. Include `micrographic.html`, `micrographic.css`, `meta.json`, `preview.html` in a 458px review frame, `alt-text.md`, `README.md`, and `sanity-asset.json`. Prefix CSS selectors with a unique `.mg-<slug>` root; tag all translatable text with non-nested `data-t` keys; use no JavaScript, external assets, external fonts, CSS grid, vh/vw, rem, fixed/sticky positioning, or `@import`. Do not upload or publish to Sanity. Before declaring completion, report visual checks at 458px, phone, desktop, A4/US Letter, and grayscale.

Required inputs to attach
- Approved transparent PNG reference: Assets/Reference/bd-v-032-ref.jpg
- Matching white-background JPG preview: Assets/Reference/bd-v-032-ref.jpg
- Matching conformance report: Assets/Reference/bd-v-032-ref.json
- Current Claude Design System authoring instructions and closest approved micrographic bundle
- Current Sanity schema/publishing requirements, if available

Complete asset brief
- Asset ID: BD-V-032
- Suggested by: Pablo
- Priority: Essential
- Type: Diagram
- Historical page/note: 22; demonstrate proof of work and difficulty, and diagram proof of work's purposes.
- Placement: SG: Under `### Proof of work`, after the paragraph beginning “When a miner finds a valid result” EG: under `### Proof of work`, replace the matching marker after the source text at the listed EG line. See section 3.8 for the exact anchor.
- Source locator: SG: 609; EG: 1526
- Text–visual link: Makes costly-to-produce and easy-to-verify work visible.
- Design brief: Show candidate block data entering repeated hash attempts; many results miss the target; one result meets it; the miner broadcasts the block; nodes quickly verify proof and all other rules; accepted blocks add accumulated work. Include difficulty adjustment as a small feedback loop. Do not depict mining as solving an externally useful puzzle.
- Format: Sequential process diagram; full width.

Use the exact heading and insertion direction in Placement as the target placement. Preserve all listed placements in metadata. Include source-brief revision, reference paths, factual sources, production date, reviewer status, checks, and unresolved judgments in README.md. Set `reviewStatus` to draft or review unless an authorized reviewer has approved it.
```
### [ ] BD-V-028 — Diagram

```text
You are building one production-ready, accessible My First Bitcoin Bitcoin Diploma visual from a supplied approved transparent PNG reference, its white-background JPG preview, and their JSON conformance report. Read the complete brief below before acting. The asset brief is the source of truth for lesson intent, content, safety, caption, alt text, placement, and localization. The reference image guides composition only. If it conflicts with the brief, the brief wins; report any unresolved factual or design-system gap before implementing.

Rebuild—not trace or embed—the reference as editable HTML, CSS, and inline SVG. Apply the supplied Claude Design System rather than the reference's provisional styling. Keep all essential geometry, arrows, labels, warnings, icons, and data editable. Preserve one clear teaching relationship, a decisive reading order, cultural replaceability, grayscale meaning, narrow-page responsiveness, phone and desktop usability, A4/US-Letter printing, expandable translated text, and future RTL adaptation.

Never invent facts, labels, numbers, providers, URLs, legal claims, safety claims, or brand choices. Preserve every prohibition and qualification in the brief. Do not include real seed phrases, private keys, payable addresses, private learner data, balances, or transactions. Use a verified QR, address, URL, interface, date, or fact only when the brief explicitly authorizes it and it has been checked. Do not imply investment returns, guaranteed outcomes, risk-free self-custody, inevitable adoption, or universal local conclusions. Do not turn a named service into a recommendation.

Produce a bundle in the guide-specific `Assets/diploma/<student-guide|educator-guide|shared>/<asset-id-lowercase>/` folder selected from the placement. Include `micrographic.html`, `micrographic.css`, `meta.json`, `preview.html` in a 458px review frame, `alt-text.md`, `README.md`, and `sanity-asset.json`. Prefix CSS selectors with a unique `.mg-<slug>` root; tag all translatable text with non-nested `data-t` keys; use no JavaScript, external assets, external fonts, CSS grid, vh/vw, rem, fixed/sticky positioning, or `@import`. Do not upload or publish to Sanity. Before declaring completion, report visual checks at 458px, phone, desktop, A4/US Letter, and grayscale.

Required inputs to attach
- Approved transparent PNG reference: Assets/Reference/bd-v-028-ref.jpg
- Matching white-background JPG preview: Assets/Reference/bd-v-028-ref.jpg
- Matching conformance report: Assets/Reference/bd-v-028-ref.json
- Current Claude Design System authoring instructions and closest approved micrographic bundle
- Current Sanity schema/publishing requirements, if available

Complete asset brief
- Asset ID: BD-V-028
- Suggested by: Pablo
- Priority: Essential
- Type: Diagram
- Historical page/note: 19; add a finite-supply and halving graphic with block-based timing.
- Placement: SG: Under `### Finite supply`, after the paragraph beginning “The subsidy began at 50 BTC per block”, following the halving table. EG: under `### Finite supply and halving`, replace the matching marker after the source text at the listed EG line. See section 3.8 for the exact anchor.
- Source locator: SG: 635; EG: 1554
- Text–visual link: Separates maximum supply, issuance, block subsidy, halving, and miner fees.
- Design brief: Show a descending step chart for block subsidy by halving era and a rising cumulative issuance curve approaching 21 million. Mark halvings by block height or era and `roughly four years`, not guaranteed calendar dates. Show transaction fees separately from new issuance. Include no price curve or adoption prediction.
- Format: Paired issuance chart; full width.

Use the exact heading and insertion direction in Placement as the target placement. Preserve all listed placements in metadata. Include source-brief revision, reference paths, factual sources, production date, reviewer status, checks, and unresolved judgments in README.md. Set `reviewStatus` to draft or review unless an authorized reviewer has approved it.
```
### [ ] BD-V-029 — Table

```text
You are building one production-ready, accessible My First Bitcoin Bitcoin Diploma visual from a supplied approved transparent PNG reference, its white-background JPG preview, and their JSON conformance report. Read the complete brief below before acting. The asset brief is the source of truth for lesson intent, content, safety, caption, alt text, placement, and localization. The reference image guides composition only. If it conflicts with the brief, the brief wins; report any unresolved factual or design-system gap before implementing.

Rebuild—not trace or embed—the reference as editable HTML, CSS, and inline SVG. Apply the supplied Claude Design System rather than the reference's provisional styling. Keep all essential geometry, arrows, labels, warnings, icons, and data editable. Preserve one clear teaching relationship, a decisive reading order, cultural replaceability, grayscale meaning, narrow-page responsiveness, phone and desktop usability, A4/US-Letter printing, expandable translated text, and future RTL adaptation.

Never invent facts, labels, numbers, providers, URLs, legal claims, safety claims, or brand choices. Preserve every prohibition and qualification in the brief. Do not include real seed phrases, private keys, payable addresses, private learner data, balances, or transactions. Use a verified QR, address, URL, interface, date, or fact only when the brief explicitly authorizes it and it has been checked. Do not imply investment returns, guaranteed outcomes, risk-free self-custody, inevitable adoption, or universal local conclusions. Do not turn a named service into a recommendation.

Produce a bundle in the guide-specific `Assets/diploma/<student-guide|educator-guide|shared>/<asset-id-lowercase>/` folder selected from the placement. Include `micrographic.html`, `micrographic.css`, `meta.json`, `preview.html` in a 458px review frame, `alt-text.md`, `README.md`, and `sanity-asset.json`. Prefix CSS selectors with a unique `.mg-<slug>` root; tag all translatable text with non-nested `data-t` keys; use no JavaScript, external assets, external fonts, CSS grid, vh/vw, rem, fixed/sticky positioning, or `@import`. Do not upload or publish to Sanity. Before declaring completion, report visual checks at 458px, phone, desktop, A4/US Letter, and grayscale.

Required inputs to attach
- Approved transparent PNG reference: Assets/Reference/bd-v-029-ref.jpg
- Matching white-background JPG preview: Assets/Reference/bd-v-029-ref.jpg
- Matching conformance report: Assets/Reference/bd-v-029-ref.json
- Current Claude Design System authoring instructions and closest approved micrographic bundle
- Current Sanity schema/publishing requirements, if available

Complete asset brief
- Asset ID: BD-V-029
- Suggested by: Pablo
- Priority: Essential
- Type: Table
- Historical page/note: 20; turn the bitcoin-and-sats table into a graphic.
- Placement: SG: Under `### Satoshis and unit bias`, replace the unit table visually while retaining a text equivalent. EG: under `### Sats and unit bias`, replace the matching marker after the source text at the listed EG line. See section 3.8 for the exact anchor.
- Source locator: SG: 651; EG: 1583
- Text–visual link: Makes divisibility intuitive and counters the belief that a learner needs one whole bitcoin.
- Design brief: Start with `1 BTC = 100,000,000 sats`, then zoom into 0.1 BTC, 0.01 BTC, 0.001 BTC, and 1 sat. Show that differently displayed amounts can represent the same value, using `100,000 sats = 0.001 BTC`. Do not show a current fiat price.
- Format: Illustrated denomination reference table; half to full width.

Use the exact heading and insertion direction in Placement as the target placement. Preserve all listed placements in metadata. Include source-brief revision, reference paths, factual sources, production date, reviewer status, checks, and unresolved judgments in README.md. Set `reviewStatus` to draft or review unless an authorized reviewer has approved it.
```
### [ ] BD-V-033 — Table

```text
You are building one production-ready, accessible My First Bitcoin Bitcoin Diploma visual from a supplied approved transparent PNG reference, its white-background JPG preview, and their JSON conformance report. Read the complete brief below before acting. The asset brief is the source of truth for lesson intent, content, safety, caption, alt text, placement, and localization. The reference image guides composition only. If it conflicts with the brief, the brief wins; report any unresolved factual or design-system gap before implementing.

Rebuild—not trace or embed—the reference as editable HTML, CSS, and inline SVG. Apply the supplied Claude Design System rather than the reference's provisional styling. Keep all essential geometry, arrows, labels, warnings, icons, and data editable. Preserve one clear teaching relationship, a decisive reading order, cultural replaceability, grayscale meaning, narrow-page responsiveness, phone and desktop usability, A4/US-Letter printing, expandable translated text, and future RTL adaptation.

Never invent facts, labels, numbers, providers, URLs, legal claims, safety claims, or brand choices. Preserve every prohibition and qualification in the brief. Do not include real seed phrases, private keys, payable addresses, private learner data, balances, or transactions. Use a verified QR, address, URL, interface, date, or fact only when the brief explicitly authorizes it and it has been checked. Do not imply investment returns, guaranteed outcomes, risk-free self-custody, inevitable adoption, or universal local conclusions. Do not turn a named service into a recommendation.

Produce a bundle in the guide-specific `Assets/diploma/<student-guide|educator-guide|shared>/<asset-id-lowercase>/` folder selected from the placement. Include `micrographic.html`, `micrographic.css`, `meta.json`, `preview.html` in a 458px review frame, `alt-text.md`, `README.md`, and `sanity-asset.json`. Prefix CSS selectors with a unique `.mg-<slug>` root; tag all translatable text with non-nested `data-t` keys; use no JavaScript, external assets, external fonts, CSS grid, vh/vw, rem, fixed/sticky positioning, or `@import`. Do not upload or publish to Sanity. Before declaring completion, report visual checks at 458px, phone, desktop, A4/US Letter, and grayscale.

Required inputs to attach
- Approved transparent PNG reference: Assets/Reference/bd-v-033-ref.jpg
- Matching white-background JPG preview: Assets/Reference/bd-v-033-ref.jpg
- Matching conformance report: Assets/Reference/bd-v-033-ref.json
- Current Claude Design System authoring instructions and closest approved micrographic bundle
- Current Sanity schema/publishing requirements, if available

Complete asset brief
- Asset ID: BD-V-033
- Suggested by: Pablo
- Priority: Essential
- Type: Table
- Historical page/note: 23; add graphics to explain Bitcoin's properties in plain language.
- Placement: Under `### Bitcoin as sound digital money`, replace the existing property table visually while retaining an accessible text equivalent.
- Source locator: 673
- Text–visual link: Makes each monetary property concrete without treating Bitcoin as universally superior.
- Design brief: Retain a learner-friendly table with one small icon and concise plain-language explanation for each property: durability, portability, divisibility, fungibility, scarcity, verifiability, and acceptability. State the relevant qualification already in the text, especially that acceptance varies and public history can affect how services treat particular funds. Do not turn the properties into a total score or claim that Bitcoin performs every function equally well everywhere.
- Format: Icon-supported properties table; full width.

Use the exact heading and insertion direction in Placement as the target placement. Preserve all listed placements in metadata. Include source-brief revision, reference paths, factual sources, production date, reviewer status, checks, and unresolved judgments in README.md. Set `reviewStatus` to draft or review unless an authorized reviewer has approved it.
```
### [ ] BD-V-025 — Table

```text
You are building one production-ready, accessible My First Bitcoin Bitcoin Diploma visual from a supplied approved transparent PNG reference, its white-background JPG preview, and their JSON conformance report. Read the complete brief below before acting. The asset brief is the source of truth for lesson intent, content, safety, caption, alt text, placement, and localization. The reference image guides composition only. If it conflicts with the brief, the brief wins; report any unresolved factual or design-system gap before implementing.

Rebuild—not trace or embed—the reference as editable HTML, CSS, and inline SVG. Apply the supplied Claude Design System rather than the reference's provisional styling. Keep all essential geometry, arrows, labels, warnings, icons, and data editable. Preserve one clear teaching relationship, a decisive reading order, cultural replaceability, grayscale meaning, narrow-page responsiveness, phone and desktop usability, A4/US-Letter printing, expandable translated text, and future RTL adaptation.

Never invent facts, labels, numbers, providers, URLs, legal claims, safety claims, or brand choices. Preserve every prohibition and qualification in the brief. Do not include real seed phrases, private keys, payable addresses, private learner data, balances, or transactions. Use a verified QR, address, URL, interface, date, or fact only when the brief explicitly authorizes it and it has been checked. Do not imply investment returns, guaranteed outcomes, risk-free self-custody, inevitable adoption, or universal local conclusions. Do not turn a named service into a recommendation.

Produce a bundle in the guide-specific `Assets/diploma/<student-guide|educator-guide|shared>/<asset-id-lowercase>/` folder selected from the placement. Include `micrographic.html`, `micrographic.css`, `meta.json`, `preview.html` in a 458px review frame, `alt-text.md`, `README.md`, and `sanity-asset.json`. Prefix CSS selectors with a unique `.mg-<slug>` root; tag all translatable text with non-nested `data-t` keys; use no JavaScript, external assets, external fonts, CSS grid, vh/vw, rem, fixed/sticky positioning, or `@import`. Do not upload or publish to Sanity. Before declaring completion, report visual checks at 458px, phone, desktop, A4/US Letter, and grayscale.

Required inputs to attach
- Approved transparent PNG reference: Assets/Reference/bd-v-025-ref.jpg
- Matching white-background JPG preview: Assets/Reference/bd-v-025-ref.jpg
- Matching conformance report: Assets/Reference/bd-v-025-ref.json
- Current Claude Design System authoring instructions and closest approved micrographic bundle
- Current Sanity schema/publishing requirements, if available

Complete asset brief
- Asset ID: BD-V-025
- Suggested by: Pablo
- Priority: Essential
- Type: Table
- Historical page/note: 18; add images or links for the whitepaper, Genesis Block, first transaction, and Pizza Day.
- Placement: Under `### Bitcoin origin timeline`, replace the current date/event table visually while retaining an accessible text equivalent.
- Source locator: 731
- Text–visual link: Connects the four historical events to why each matters.
- Design brief: Show 31 Oct 2008 whitepaper; 3 Jan 2009 Genesis Block; 12 Jan 2009 first recorded person-to-person transaction; 22 May 2010 Pizza Day. Pair each event with a short significance line. Use document-style illustrations or rights-cleared source images only; avoid portraits or identity speculation for Satoshi.
- Format: Illustrated four-milestone reference table; full width.

Use the exact heading and insertion direction in Placement as the target placement. Preserve all listed placements in metadata. Include source-brief revision, reference paths, factual sources, production date, reviewer status, checks, and unresolved judgments in README.md. Set `reviewStatus` to draft or review unless an authorized reviewer has approved it.
```
### [ ] BD-V-034 — Table

```text
You are building one production-ready, accessible My First Bitcoin Bitcoin Diploma visual from a supplied approved transparent PNG reference, its white-background JPG preview, and their JSON conformance report. Read the complete brief below before acting. The asset brief is the source of truth for lesson intent, content, safety, caption, alt text, placement, and localization. The reference image guides composition only. If it conflicts with the brief, the brief wins; report any unresolved factual or design-system gap before implementing.

Rebuild—not trace or embed—the reference as editable HTML, CSS, and inline SVG. Apply the supplied Claude Design System rather than the reference's provisional styling. Keep all essential geometry, arrows, labels, warnings, icons, and data editable. Preserve one clear teaching relationship, a decisive reading order, cultural replaceability, grayscale meaning, narrow-page responsiveness, phone and desktop usability, A4/US-Letter printing, expandable translated text, and future RTL adaptation.

Never invent facts, labels, numbers, providers, URLs, legal claims, safety claims, or brand choices. Preserve every prohibition and qualification in the brief. Do not include real seed phrases, private keys, payable addresses, private learner data, balances, or transactions. Use a verified QR, address, URL, interface, date, or fact only when the brief explicitly authorizes it and it has been checked. Do not imply investment returns, guaranteed outcomes, risk-free self-custody, inevitable adoption, or universal local conclusions. Do not turn a named service into a recommendation.

Produce a bundle in the guide-specific `Assets/diploma/<student-guide|educator-guide|shared>/<asset-id-lowercase>/` folder selected from the placement. Include `micrographic.html`, `micrographic.css`, `meta.json`, `preview.html` in a 458px review frame, `alt-text.md`, `README.md`, and `sanity-asset.json`. Prefix CSS selectors with a unique `.mg-<slug>` root; tag all translatable text with non-nested `data-t` keys; use no JavaScript, external assets, external fonts, CSS grid, vh/vw, rem, fixed/sticky positioning, or `@import`. Do not upload or publish to Sanity. Before declaring completion, report visual checks at 458px, phone, desktop, A4/US Letter, and grayscale.

Required inputs to attach
- Approved transparent PNG reference: Assets/Reference/bd-v-034-ref.jpg
- Matching white-background JPG preview: Assets/Reference/bd-v-034-ref.jpg
- Matching conformance report: Assets/Reference/bd-v-034-ref.json
- Current Claude Design System authoring instructions and closest approved micrographic bundle
- Current Sanity schema/publishing requirements, if available

Complete asset brief
- Asset ID: BD-V-034
- Suggested by: Pablo
- Priority: Essential
- Type: Table
- Historical page/note: 24; add graphics to the Module 2 comparison and make the Module 3 transition explicit.
- Placement: Under `### Review: how does Bitcoin respond to fiat problems?`, replace the existing `Fiat-system issue / Bitcoin's response / New responsibility or trade-off` table visually while retaining an accessible text equivalent.
- Source locator: 764
- Text–visual link: Reconnects the entire Module 2 explanation to the Module 1 problems and the new responsibilities introduced by Bitcoin.
- Design brief: Preserve the three current columns and all five rows: supply policy; intermediary dependence; central ledger control; institutional access; and ordering digital payments. Retain the corresponding responsibilities for rule verification, irreversible errors, privacy, key protection, and mining equipment and energy. Do not label the middle column `perfect solution` or add unsupported promises.
- Format: Bridge diagram or visual table; full width.

Use the exact heading and insertion direction in Placement as the target placement. Preserve all listed placements in metadata. Include source-brief revision, reference paths, factual sources, production date, reviewer status, checks, and unresolved judgments in README.md. Set `reviewStatus` to draft or review unless an authorized reviewer has approved it.
```

## 3.4 Module 3: Using Bitcoin Safely

### [ ] BD-V-035 — Diagram

```text
You are building one production-ready, accessible My First Bitcoin Bitcoin Diploma visual from a supplied approved transparent PNG reference, its white-background JPG preview, and their JSON conformance report. Read the complete brief below before acting. The asset brief is the source of truth for lesson intent, content, safety, caption, alt text, placement, and localization. The reference image guides composition only. If it conflicts with the brief, the brief wins; report any unresolved factual or design-system gap before implementing.

Rebuild—not trace or embed—the reference as editable HTML, CSS, and inline SVG. Apply the supplied Claude Design System rather than the reference's provisional styling. Keep all essential geometry, arrows, labels, warnings, icons, and data editable. Preserve one clear teaching relationship, a decisive reading order, cultural replaceability, grayscale meaning, narrow-page responsiveness, phone and desktop usability, A4/US-Letter printing, expandable translated text, and future RTL adaptation.

Never invent facts, labels, numbers, providers, URLs, legal claims, safety claims, or brand choices. Preserve every prohibition and qualification in the brief. Do not include real seed phrases, private keys, payable addresses, private learner data, balances, or transactions. Use a verified QR, address, URL, interface, date, or fact only when the brief explicitly authorizes it and it has been checked. Do not imply investment returns, guaranteed outcomes, risk-free self-custody, inevitable adoption, or universal local conclusions. Do not turn a named service into a recommendation.

Produce a bundle in the guide-specific `Assets/diploma/<student-guide|educator-guide|shared>/<asset-id-lowercase>/` folder selected from the placement. Include `micrographic.html`, `micrographic.css`, `meta.json`, `preview.html` in a 458px review frame, `alt-text.md`, `README.md`, and `sanity-asset.json`. Prefix CSS selectors with a unique `.mg-<slug>` root; tag all translatable text with non-nested `data-t` keys; use no JavaScript, external assets, external fonts, CSS grid, vh/vw, rem, fixed/sticky positioning, or `@import`. Do not upload or publish to Sanity. Before declaring completion, report visual checks at 458px, phone, desktop, A4/US Letter, and grayscale.

Required inputs to attach
- Approved transparent PNG reference: Assets/Reference/bd-v-035-ref.jpg
- Matching white-background JPG preview: Assets/Reference/bd-v-035-ref.jpg
- Matching conformance report: Assets/Reference/bd-v-035-ref.json
- Current Claude Design System authoring instructions and closest approved micrographic bundle
- Current Sanity schema/publishing requirements, if available

Complete asset brief
- Asset ID: BD-V-035
- Suggested by: AI
- Priority: Essential
- Type: Diagram
- Historical page/note: 25; clarify that wallets coordinate keys and instructions while bitcoin remains on the ledger.
- Placement: SG: Under `### Wallets`, after the paragraph explaining that bitcoin is not stored inside the wallet. EG: under `### Wallets are interfaces`, replace the matching marker after the source text at the listed EG line. See section 3.8 for the exact anchor.
- Source locator: SG: 810; EG: 1837
- Text–visual link: Corrects the most important beginner wallet misconception.
- Design brief: Show the Bitcoin ledger as the record of spendable outputs; the wallet holding or managing keys and constructing instructions; the user authorizing an action; and the network verifying it. Do not draw coins sitting inside a phone or hardware device.
- Format: Conceptual layer diagram; full width.

Use the exact heading and insertion direction in Placement as the target placement. Preserve all listed placements in metadata. Include source-brief revision, reference paths, factual sources, production date, reviewer status, checks, and unresolved judgments in README.md. Set `reviewStatus` to draft or review unless an authorized reviewer has approved it.
```
### [ ] BD-V-036 — Diagram

```text
You are building one production-ready, accessible My First Bitcoin Bitcoin Diploma visual from a supplied approved transparent PNG reference, its white-background JPG preview, and their JSON conformance report. Read the complete brief below before acting. The asset brief is the source of truth for lesson intent, content, safety, caption, alt text, placement, and localization. The reference image guides composition only. If it conflicts with the brief, the brief wins; report any unresolved factual or design-system gap before implementing.

Rebuild—not trace or embed—the reference as editable HTML, CSS, and inline SVG. Apply the supplied Claude Design System rather than the reference's provisional styling. Keep all essential geometry, arrows, labels, warnings, icons, and data editable. Preserve one clear teaching relationship, a decisive reading order, cultural replaceability, grayscale meaning, narrow-page responsiveness, phone and desktop usability, A4/US-Letter printing, expandable translated text, and future RTL adaptation.

Never invent facts, labels, numbers, providers, URLs, legal claims, safety claims, or brand choices. Preserve every prohibition and qualification in the brief. Do not include real seed phrases, private keys, payable addresses, private learner data, balances, or transactions. Use a verified QR, address, URL, interface, date, or fact only when the brief explicitly authorizes it and it has been checked. Do not imply investment returns, guaranteed outcomes, risk-free self-custody, inevitable adoption, or universal local conclusions. Do not turn a named service into a recommendation.

Produce a bundle in the guide-specific `Assets/diploma/<student-guide|educator-guide|shared>/<asset-id-lowercase>/` folder selected from the placement. Include `micrographic.html`, `micrographic.css`, `meta.json`, `preview.html` in a 458px review frame, `alt-text.md`, `README.md`, and `sanity-asset.json`. Prefix CSS selectors with a unique `.mg-<slug>` root; tag all translatable text with non-nested `data-t` keys; use no JavaScript, external assets, external fonts, CSS grid, vh/vw, rem, fixed/sticky positioning, or `@import`. Do not upload or publish to Sanity. Before declaring completion, report visual checks at 458px, phone, desktop, A4/US Letter, and grayscale.

Required inputs to attach
- Approved transparent PNG reference: Assets/Reference/bd-v-036-ref.jpg
- Matching white-background JPG preview: Assets/Reference/bd-v-036-ref.jpg
- Matching conformance report: Assets/Reference/bd-v-036-ref.json
- Current Claude Design System authoring instructions and closest approved micrographic bundle
- Current Sanity schema/publishing requirements, if available

Complete asset brief
- Asset ID: BD-V-036
- Suggested by: Pablo; User
- Priority: Essential
- Type: Diagram
- Historical page/note: 26; Pablo: add an address/QR graphic, explain who creates addresses, and show address checks. User: show a My First Bitcoin test address as alphanumeric text and its matching QR code.
- Placement: Under `### Addresses` in the [Student Guide](../publish/mfb-bd-26.10/mfb-bd-sg-26.10.md#addresses), immediately after the opening paragraph beginning “A Bitcoin **address** is public receiving information” and before “If you want to receive an on-chain payment”.
- Source locator: 818
- Text–visual link: Shows that the alphanumeric address and QR code represent the same public receiving information; neither is a private key or a recovery phrase.
- Design brief: Show the full My First Bitcoin test address as readable, untruncated text beside a QR code encoding exactly that address, joined by the label `Same address, two formats`. Use [BLANK] for the official test address and [BLANK] for the exact test-network name until My First Bitcoin supplies and approves both values; do not generate a QR until TODO AST-001 is resolved. Do not invent an address or substitute a live donation address. Label `My First Bitcoin test address`, the confirmed test network, and `SAMPLE — DO NOT PAY`. Explain briefly that the wallet creates the receiving address and that the sender checks the decoded destination against the trusted receive screen. Encode only the address, without an amount, URL, or Lightning invoice. Generate the QR from the supplied text and verify that scanning the final print and screen exports returns the identical full address. Keep the QR unobstructed with a clear border. Caption: `Scan or copy: both give the same receiving address. Check the destination before sending.` Alt text: `A My First Bitcoin test address shown as alphanumeric text beside a QR code containing the same address, labelled with its test network and SAMPLE — DO NOT PAY.` Save the editable master as `Assets/Briefs/bd-v-036-brief.md`.
- Format: Side-by-side text-to-QR diagram with editable labels; half to full width.

Use the exact heading and insertion direction in Placement as the target placement. Preserve all listed placements in metadata. Include source-brief revision, reference paths, factual sources, production date, reviewer status, checks, and unresolved judgments in README.md. Set `reviewStatus` to draft or review unless an authorized reviewer has approved it.
```
### [ ] BD-V-078 — Diagram

```text
You are building one production-ready, accessible My First Bitcoin Bitcoin Diploma visual from a supplied approved transparent PNG reference, its white-background JPG preview, and their JSON conformance report. Read the complete brief below before acting. The asset brief is the source of truth for lesson intent, content, safety, caption, alt text, placement, and localization. The reference image guides composition only. If it conflicts with the brief, the brief wins; report any unresolved factual or design-system gap before implementing.

Rebuild—not trace or embed—the reference as editable HTML, CSS, and inline SVG. Apply the supplied Claude Design System rather than the reference's provisional styling. Keep all essential geometry, arrows, labels, warnings, icons, and data editable. Preserve one clear teaching relationship, a decisive reading order, cultural replaceability, grayscale meaning, narrow-page responsiveness, phone and desktop usability, A4/US-Letter printing, expandable translated text, and future RTL adaptation.

Never invent facts, labels, numbers, providers, URLs, legal claims, safety claims, or brand choices. Preserve every prohibition and qualification in the brief. Do not include real seed phrases, private keys, payable addresses, private learner data, balances, or transactions. Use a verified QR, address, URL, interface, date, or fact only when the brief explicitly authorizes it and it has been checked. Do not imply investment returns, guaranteed outcomes, risk-free self-custody, inevitable adoption, or universal local conclusions. Do not turn a named service into a recommendation.

Produce a bundle in the guide-specific `Assets/diploma/<student-guide|educator-guide|shared>/<asset-id-lowercase>/` folder selected from the placement. Include `micrographic.html`, `micrographic.css`, `meta.json`, `preview.html` in a 458px review frame, `alt-text.md`, `README.md`, and `sanity-asset.json`. Prefix CSS selectors with a unique `.mg-<slug>` root; tag all translatable text with non-nested `data-t` keys; use no JavaScript, external assets, external fonts, CSS grid, vh/vw, rem, fixed/sticky positioning, or `@import`. Do not upload or publish to Sanity. Before declaring completion, report visual checks at 458px, phone, desktop, A4/US Letter, and grayscale.

Required inputs to attach
- Approved transparent PNG reference: Assets/Reference/bd-v-078-ref.jpg
- Matching white-background JPG preview: Assets/Reference/bd-v-078-ref.jpg
- Matching conformance report: Assets/Reference/bd-v-078-ref.json
- Current Claude Design System authoring instructions and closest approved micrographic bundle
- Current Sanity schema/publishing requirements, if available

Complete asset brief
- Asset ID: BD-V-078
- Suggested by: User
- Priority: Essential
- Type: Diagram
- Historical page/note: —; Show an invoice with its amount, destination, and other payment details beside its matching QR code.
- Placement: Under `### Addresses` in the [Student Guide](../publish/mfb-bd-26.10/mfb-bd-sg-26.10.md#addresses), immediately after the paragraph beginning “For every payment request, confirm the intended payment method” and before “When a payment matters”.
- Source locator: 822
- Text–visual link: Shows how a Lightning invoice carries a payment request and how its readable details relate to the QR code; complements the on-chain address example in `BD-V-036`.
- Design brief: Show a My First Bitcoin test Lightning invoice as a readable payment-request panel on the left and its matching QR code on the right, joined by `Same payment request, two formats`. Include recipient `My First Bitcoin — test`, payment method `Lightning`, confirmed test network, amount with an explicit unit, description, expiry, and the invoice string labelled `Lightning payment request`. Use the invoice string as the destination to scan or copy; do not label it as an on-chain address or imply that a Lightning invoice requires one. Distinguish the recipient display label from the encoded invoice details; a familiar name alone does not verify the recipient. Use [BLANK] for the official test invoice, network, amount, description, and expiry until My First Bitcoin supplies and approves them; do not generate a QR until TODO AST-002 is resolved. Mark `SAMPLE — DO NOT PAY`; explain that this is a fixed teaching example and may be expired. Encode the complete supplied invoice in the QR, not an address or a summary of the displayed fields. Verify that scanning the final print and screen exports returns the identical invoice and that a compatible test wallet displays matching payment details. Keep the QR unobstructed with a clear border, and keep the complete invoice available as selectable text. Do not show private keys, recovery phrases, or a live donation request. Caption: `Check the payment method, recipient, amount, and expiry after scanning.` Alt text: `A My First Bitcoin test Lightning invoice with its recipient, network, amount, description, expiry, and payment-request text beside a QR code encoding the same invoice, marked SAMPLE — DO NOT PAY.` Save the editable master as `Assets/Briefs/bd-v-078-brief.md`.
- Format: Side-by-side invoice-and-QR diagram with editable labels; full width.

Use the exact heading and insertion direction in Placement as the target placement. Preserve all listed placements in metadata. Include source-brief revision, reference paths, factual sources, production date, reviewer status, checks, and unresolved judgments in README.md. Set `reviewStatus` to draft or review unless an authorized reviewer has approved it.
```
### [ ] BD-V-037 — Diagram

```text
You are building one production-ready, accessible My First Bitcoin Bitcoin Diploma visual from a supplied approved transparent PNG reference, its white-background JPG preview, and their JSON conformance report. Read the complete brief below before acting. The asset brief is the source of truth for lesson intent, content, safety, caption, alt text, placement, and localization. The reference image guides composition only. If it conflicts with the brief, the brief wins; report any unresolved factual or design-system gap before implementing.

Rebuild—not trace or embed—the reference as editable HTML, CSS, and inline SVG. Apply the supplied Claude Design System rather than the reference's provisional styling. Keep all essential geometry, arrows, labels, warnings, icons, and data editable. Preserve one clear teaching relationship, a decisive reading order, cultural replaceability, grayscale meaning, narrow-page responsiveness, phone and desktop usability, A4/US-Letter printing, expandable translated text, and future RTL adaptation.

Never invent facts, labels, numbers, providers, URLs, legal claims, safety claims, or brand choices. Preserve every prohibition and qualification in the brief. Do not include real seed phrases, private keys, payable addresses, private learner data, balances, or transactions. Use a verified QR, address, URL, interface, date, or fact only when the brief explicitly authorizes it and it has been checked. Do not imply investment returns, guaranteed outcomes, risk-free self-custody, inevitable adoption, or universal local conclusions. Do not turn a named service into a recommendation.

Produce a bundle in the guide-specific `Assets/diploma/<student-guide|educator-guide|shared>/<asset-id-lowercase>/` folder selected from the placement. Include `micrographic.html`, `micrographic.css`, `meta.json`, `preview.html` in a 458px review frame, `alt-text.md`, `README.md`, and `sanity-asset.json`. Prefix CSS selectors with a unique `.mg-<slug>` root; tag all translatable text with non-nested `data-t` keys; use no JavaScript, external assets, external fonts, CSS grid, vh/vw, rem, fixed/sticky positioning, or `@import`. Do not upload or publish to Sanity. Before declaring completion, report visual checks at 458px, phone, desktop, A4/US Letter, and grayscale.

Required inputs to attach
- Approved transparent PNG reference: Assets/Reference/bd-v-037-ref.jpg
- Matching white-background JPG preview: Assets/Reference/bd-v-037-ref.jpg
- Matching conformance report: Assets/Reference/bd-v-037-ref.json
- Current Claude Design System authoring instructions and closest approved micrographic bundle
- Current Sanity schema/publishing requirements, if available

Complete asset brief
- Asset ID: BD-V-037
- Suggested by: Pablo; User
- Priority: Essential
- Type: Diagram
- Historical page/note: 27; Pablo: add a public/private-key image and optional physical teaching tool. User: place a public/private-key relationship diagram after this section with an explicit warning never to share a private key.
- Placement: SG: At the end of `### Keys` in the [Student Guide](../publish/mfb-bd-26.10/mfb-bd-sg-26.10.md#keys), after the `Try it` sorting prompt and immediately before `### Seed phrases`. EG: under `### Keys and digital authorization`, replace the matching marker after the source text at the listed EG line. See section 3.8 for the exact anchor.
- Source locator: SG: 844; EG: 1954
- Text–visual link: Reinforces the rule “Public receiving information can be shared. Private spending information must remain secret” by showing how public information relates to a secret private key.
- Design brief: Show `Private key → Public key → Receiving address`, with the first arrow labelled `Derived from` and the address step labelled `Created from public-key information`. Place the private key inside a clearly marked secret boundary. Add a prominent warning beside it: `Never share your private key. Anyone with it can spend your bitcoin.` Use a warning symbol and readable text so the warning works in grayscale. Label the receiving address `Public receiving information`. Add a small signing branch: the private key creates a digital signature; nodes use the public key to verify it without seeing the private key. Keep the private key inside the secret boundary throughout. Do not imply that a public key or address can reveal the private key, that an address and public key are identical, or that a signature contains the private key. Use conceptual symbols only, never real or realistic private-key strings, recovery phrases, or scannable secrets. Caption: `Public information supports receiving and verification. The private key authorizes spending and must stay secret.` Alt text: `A private key kept inside a secret boundary derives a public key, from which receiving-address information is created. A separate branch shows signing and public verification without revealing the private key. Warning: never share your private key; anyone with it can spend your bitcoin.` Save the editable master as `Assets/Briefs/bd-v-037-brief.md`.
- Format: One-way key-relationship diagram with a prominent private-key warning and a supporting signing branch; full width.

Use the exact heading and insertion direction in Placement as the target placement. Preserve all listed placements in metadata. Include source-brief revision, reference paths, factual sources, production date, reviewer status, checks, and unresolved judgments in README.md. Set `reviewStatus` to draft or review unless an authorized reviewer has approved it.
```
### [ ] BD-V-038 — Diagram

```text
You are building one production-ready, accessible My First Bitcoin Bitcoin Diploma visual from a supplied approved transparent PNG reference, its white-background JPG preview, and their JSON conformance report. Read the complete brief below before acting. The asset brief is the source of truth for lesson intent, content, safety, caption, alt text, placement, and localization. The reference image guides composition only. If it conflicts with the brief, the brief wins; report any unresolved factual or design-system gap before implementing.

Rebuild—not trace or embed—the reference as editable HTML, CSS, and inline SVG. Apply the supplied Claude Design System rather than the reference's provisional styling. Keep all essential geometry, arrows, labels, warnings, icons, and data editable. Preserve one clear teaching relationship, a decisive reading order, cultural replaceability, grayscale meaning, narrow-page responsiveness, phone and desktop usability, A4/US-Letter printing, expandable translated text, and future RTL adaptation.

Never invent facts, labels, numbers, providers, URLs, legal claims, safety claims, or brand choices. Preserve every prohibition and qualification in the brief. Do not include real seed phrases, private keys, payable addresses, private learner data, balances, or transactions. Use a verified QR, address, URL, interface, date, or fact only when the brief explicitly authorizes it and it has been checked. Do not imply investment returns, guaranteed outcomes, risk-free self-custody, inevitable adoption, or universal local conclusions. Do not turn a named service into a recommendation.

Produce a bundle in the guide-specific `Assets/diploma/<student-guide|educator-guide|shared>/<asset-id-lowercase>/` folder selected from the placement. Include `micrographic.html`, `micrographic.css`, `meta.json`, `preview.html` in a 458px review frame, `alt-text.md`, `README.md`, and `sanity-asset.json`. Prefix CSS selectors with a unique `.mg-<slug>` root; tag all translatable text with non-nested `data-t` keys; use no JavaScript, external assets, external fonts, CSS grid, vh/vw, rem, fixed/sticky positioning, or `@import`. Do not upload or publish to Sanity. Before declaring completion, report visual checks at 458px, phone, desktop, A4/US Letter, and grayscale.

Required inputs to attach
- Approved transparent PNG reference: Assets/Reference/bd-v-038-ref.jpg
- Matching white-background JPG preview: Assets/Reference/bd-v-038-ref.jpg
- Matching conformance report: Assets/Reference/bd-v-038-ref.json
- Current Claude Design System authoring instructions and closest approved micrographic bundle
- Current Sanity schema/publishing requirements, if available

Complete asset brief
- Asset ID: BD-V-038
- Suggested by: AI
- Priority: Essential
- Type: Diagram
- Historical page/note: 27 and 30; show recovery language without implying every wallet uses an identical method.
- Placement: SG: Under `### Seed phrases`, after the explanation of what a seed phrase does. EG: under `### Seed phrases and recovery`, replace the matching marker after the source text at the listed EG line. See section 3.8 for the exact anchor.
- Source locator: SG: 850; EG: 1972
- Text–visual link: Places the seed phrase correctly in the recovery chain without teaching that every wallet uses an identical recovery method.
- Design brief: Show seed or wallet backup → wallet recreates keys → expected addresses and transaction access return. Mark the backup as secret and offline. Add `method and compatibility depend on the wallet`. Do not show actual words, screenshots of recovery entry, or educator access.
- Format: Recovery relationship diagram; half to full width.

Use the exact heading and insertion direction in Placement as the target placement. Preserve all listed placements in metadata. Include source-brief revision, reference paths, factual sources, production date, reviewer status, checks, and unresolved judgments in README.md. Set `reviewStatus` to draft or review unless an authorized reviewer has approved it.
```
### [ ] BD-V-079 — Image

```text
You are building one production-ready, accessible My First Bitcoin Bitcoin Diploma visual from a supplied approved transparent PNG reference, its white-background JPG preview, and their JSON conformance report. Read the complete brief below before acting. The asset brief is the source of truth for lesson intent, content, safety, caption, alt text, placement, and localization. The reference image guides composition only. If it conflicts with the brief, the brief wins; report any unresolved factual or design-system gap before implementing.

Rebuild—not trace or embed—the reference as editable HTML, CSS, and inline SVG. Apply the supplied Claude Design System rather than the reference's provisional styling. Keep all essential geometry, arrows, labels, warnings, icons, and data editable. Preserve one clear teaching relationship, a decisive reading order, cultural replaceability, grayscale meaning, narrow-page responsiveness, phone and desktop usability, A4/US-Letter printing, expandable translated text, and future RTL adaptation.

Never invent facts, labels, numbers, providers, URLs, legal claims, safety claims, or brand choices. Preserve every prohibition and qualification in the brief. Do not include real seed phrases, private keys, payable addresses, private learner data, balances, or transactions. Use a verified QR, address, URL, interface, date, or fact only when the brief explicitly authorizes it and it has been checked. Do not imply investment returns, guaranteed outcomes, risk-free self-custody, inevitable adoption, or universal local conclusions. Do not turn a named service into a recommendation.

Produce a bundle in the guide-specific `Assets/diploma/<student-guide|educator-guide|shared>/<asset-id-lowercase>/` folder selected from the placement. Include `micrographic.html`, `micrographic.css`, `meta.json`, `preview.html` in a 458px review frame, `alt-text.md`, `README.md`, and `sanity-asset.json`. Prefix CSS selectors with a unique `.mg-<slug>` root; tag all translatable text with non-nested `data-t` keys; use no JavaScript, external assets, external fonts, CSS grid, vh/vw, rem, fixed/sticky positioning, or `@import`. Do not upload or publish to Sanity. Before declaring completion, report visual checks at 458px, phone, desktop, A4/US Letter, and grayscale.

Required inputs to attach
- Approved transparent PNG reference: Assets/Reference/bd-v-079-ref.jpg
- Matching white-background JPG preview: Assets/Reference/bd-v-079-ref.jpg
- Matching conformance report: Assets/Reference/bd-v-079-ref.json
- Current Claude Design System authoring instructions and closest approved micrographic bundle
- Current Sanity schema/publishing requirements, if available

Complete asset brief
- Asset ID: BD-V-079
- Suggested by: User
- Priority: Essential
- Type: Image
- Historical page/note: —; Show a 12-word seed phrase being copied onto paper after the seed-phrase section.
- Placement: At the end of `### Seed phrases` in the [Student Guide](../publish/mfb-bd-26.10/mfb-bd-sg-26.10.md#seed-phrases), immediately after the paragraph beginning “Some wallets use additional passphrases” and before `### Custodial and non-custodial use`.
- Source locator: 861
- Text–visual link: Makes writing a private, offline backup concrete and reinforces preserving word order and spelling. Complements the recovery relationship in `BD-V-038`.
- Design brief: Show one person privately copying a 12-word seed phrase from a generic wallet backup screen onto paper with a pen. Show twelve clearly numbered positions on both screen and paper, in the same reading order, using matching placeholders `WORD 01` through `WORD 12` rather than an actual recovery phrase. Depict the hand completing the final entry; use a simple directional cue from screen to paper and a callout `Check every word and its number`. Label the illustration `EXAMPLE ONLY — NOT A VALID RECOVERY PHRASE`. Add a prominent warning: `Never share your seed phrase. Never photograph it or save it online.` Show no camera, cloud backup, messaging, website entry, or second person viewing the phrase. Use a generic interface without wallet branding. Note `12-word example; follow your wallet’s backup instructions` so the illustration does not imply that all wallets use twelve words. Caption: `Copy each word in order onto paper. Check it privately and store it securely offline.` Alt text: `A person uses a pen to copy twelve numbered placeholder words from a wallet backup screen onto paper in the same order. Labels remind the learner to check every word, keep the backup offline, and never share or photograph a seed phrase. The example is not a valid recovery phrase.` Save the editable master as `Assets/Briefs/bd-v-079-brief.md`.
- Format: Screen-to-paper illustration with numbered placeholders, editable labels, and a prominent safety warning; half to full width.

Use the exact heading and insertion direction in Placement as the target placement. Preserve all listed placements in metadata. Include source-brief revision, reference paths, factual sources, production date, reviewer status, checks, and unresolved judgments in README.md. Set `reviewStatus` to draft or review unless an authorized reviewer has approved it.
```
### [ ] BD-V-039 — Diagram

```text
You are building one production-ready, accessible My First Bitcoin Bitcoin Diploma visual from a supplied approved transparent PNG reference, its white-background JPG preview, and their JSON conformance report. Read the complete brief below before acting. The asset brief is the source of truth for lesson intent, content, safety, caption, alt text, placement, and localization. The reference image guides composition only. If it conflicts with the brief, the brief wins; report any unresolved factual or design-system gap before implementing.

Rebuild—not trace or embed—the reference as editable HTML, CSS, and inline SVG. Apply the supplied Claude Design System rather than the reference's provisional styling. Keep all essential geometry, arrows, labels, warnings, icons, and data editable. Preserve one clear teaching relationship, a decisive reading order, cultural replaceability, grayscale meaning, narrow-page responsiveness, phone and desktop usability, A4/US-Letter printing, expandable translated text, and future RTL adaptation.

Never invent facts, labels, numbers, providers, URLs, legal claims, safety claims, or brand choices. Preserve every prohibition and qualification in the brief. Do not include real seed phrases, private keys, payable addresses, private learner data, balances, or transactions. Use a verified QR, address, URL, interface, date, or fact only when the brief explicitly authorizes it and it has been checked. Do not imply investment returns, guaranteed outcomes, risk-free self-custody, inevitable adoption, or universal local conclusions. Do not turn a named service into a recommendation.

Produce a bundle in the guide-specific `Assets/diploma/<student-guide|educator-guide|shared>/<asset-id-lowercase>/` folder selected from the placement. Include `micrographic.html`, `micrographic.css`, `meta.json`, `preview.html` in a 458px review frame, `alt-text.md`, `README.md`, and `sanity-asset.json`. Prefix CSS selectors with a unique `.mg-<slug>` root; tag all translatable text with non-nested `data-t` keys; use no JavaScript, external assets, external fonts, CSS grid, vh/vw, rem, fixed/sticky positioning, or `@import`. Do not upload or publish to Sanity. Before declaring completion, report visual checks at 458px, phone, desktop, A4/US Letter, and grayscale.

Required inputs to attach
- Approved transparent PNG reference: Assets/Reference/bd-v-039-ref.jpg
- Matching white-background JPG preview: Assets/Reference/bd-v-039-ref.jpg
- Matching conformance report: Assets/Reference/bd-v-039-ref.json
- Current Claude Design System authoring instructions and closest approved micrographic bundle
- Current Sanity schema/publishing requirements, if available

Complete asset brief
- Asset ID: BD-V-039
- Suggested by: AI
- Priority: Essential
- Type: Diagram
- Historical page/note: 26 and 29; compare custody choices and custodial versus self-custodial wallet control.
- Placement: SG: Under `### Custodial and non-custodial use`, after the custody explanation. EG: under `### Custodial and self-custodial use`, replace the matching marker after the source text at the listed EG line. See section 3.8 for the exact anchor.
- Source locator: SG: 869; EG: 2031
- Text–visual link: Makes custody a question of key control rather than interface appearance.
- Design brief: Left: user logs into a service; service controls keys and authorizes withdrawal. Right: user controls keys; wallet signs under the user's authority; network checks the transaction. Show recovery responsibility and failure point in both paths. Avoid portraying self-custody as morally superior or risk free.
- Format: Side-by-side custody model; full width.

Use the exact heading and insertion direction in Placement as the target placement. Preserve all listed placements in metadata. Include source-brief revision, reference paths, factual sources, production date, reviewer status, checks, and unresolved judgments in README.md. Set `reviewStatus` to draft or review unless an authorized reviewer has approved it.
```
### [ ] BD-V-040 — Table

```text
You are building one production-ready, accessible My First Bitcoin Bitcoin Diploma visual from a supplied approved transparent PNG reference, its white-background JPG preview, and their JSON conformance report. Read the complete brief below before acting. The asset brief is the source of truth for lesson intent, content, safety, caption, alt text, placement, and localization. The reference image guides composition only. If it conflicts with the brief, the brief wins; report any unresolved factual or design-system gap before implementing.

Rebuild—not trace or embed—the reference as editable HTML, CSS, and inline SVG. Apply the supplied Claude Design System rather than the reference's provisional styling. Keep all essential geometry, arrows, labels, warnings, icons, and data editable. Preserve one clear teaching relationship, a decisive reading order, cultural replaceability, grayscale meaning, narrow-page responsiveness, phone and desktop usability, A4/US-Letter printing, expandable translated text, and future RTL adaptation.

Never invent facts, labels, numbers, providers, URLs, legal claims, safety claims, or brand choices. Preserve every prohibition and qualification in the brief. Do not include real seed phrases, private keys, payable addresses, private learner data, balances, or transactions. Use a verified QR, address, URL, interface, date, or fact only when the brief explicitly authorizes it and it has been checked. Do not imply investment returns, guaranteed outcomes, risk-free self-custody, inevitable adoption, or universal local conclusions. Do not turn a named service into a recommendation.

Produce a bundle in the guide-specific `Assets/diploma/<student-guide|educator-guide|shared>/<asset-id-lowercase>/` folder selected from the placement. Include `micrographic.html`, `micrographic.css`, `meta.json`, `preview.html` in a 458px review frame, `alt-text.md`, `README.md`, and `sanity-asset.json`. Prefix CSS selectors with a unique `.mg-<slug>` root; tag all translatable text with non-nested `data-t` keys; use no JavaScript, external assets, external fonts, CSS grid, vh/vw, rem, fixed/sticky positioning, or `@import`. Do not upload or publish to Sanity. Before declaring completion, report visual checks at 458px, phone, desktop, A4/US Letter, and grayscale.

Required inputs to attach
- Approved transparent PNG reference: Assets/Reference/bd-v-040-ref.jpg
- Matching white-background JPG preview: Assets/Reference/bd-v-040-ref.jpg
- Matching conformance report: Assets/Reference/bd-v-040-ref.json
- Current Claude Design System authoring instructions and closest approved micrographic bundle
- Current Sanity schema/publishing requirements, if available

Complete asset brief
- Asset ID: BD-V-040
- Suggested by: AI
- Priority: Supporting
- Type: Table
- Historical page/note: 29; provide a custodial-versus-self-custodial reference.
- Placement: Under `### Custodial and non-custodial use`, replace the existing `Question / Custodial use / Self-custodial use` table visually while retaining an accessible text equivalent.
- Source locator: 871
- Text–visual link: Makes key control, recovery, and failure points comparable without moralising either model.
- Design brief: Preserve the current rows `Who holds the keys?`, `Who handles recovery?`, and `Main trade-off`, with the custodial and self-custodial explanations. Use neutral icons and editable text. Do not add a recommendation badge or treat either model as risk free.
- Format: Custody comparison table; full width.

Use the exact heading and insertion direction in Placement as the target placement. Preserve all listed placements in metadata. Include source-brief revision, reference paths, factual sources, production date, reviewer status, checks, and unresolved judgments in README.md. Set `reviewStatus` to draft or review unless an authorized reviewer has approved it.
```
### [ ] BD-V-042 — Diagram

```text
You are building one production-ready, accessible My First Bitcoin Bitcoin Diploma visual from a supplied approved transparent PNG reference, its white-background JPG preview, and their JSON conformance report. Read the complete brief below before acting. The asset brief is the source of truth for lesson intent, content, safety, caption, alt text, placement, and localization. The reference image guides composition only. If it conflicts with the brief, the brief wins; report any unresolved factual or design-system gap before implementing.

Rebuild—not trace or embed—the reference as editable HTML, CSS, and inline SVG. Apply the supplied Claude Design System rather than the reference's provisional styling. Keep all essential geometry, arrows, labels, warnings, icons, and data editable. Preserve one clear teaching relationship, a decisive reading order, cultural replaceability, grayscale meaning, narrow-page responsiveness, phone and desktop usability, A4/US-Letter printing, expandable translated text, and future RTL adaptation.

Never invent facts, labels, numbers, providers, URLs, legal claims, safety claims, or brand choices. Preserve every prohibition and qualification in the brief. Do not include real seed phrases, private keys, payable addresses, private learner data, balances, or transactions. Use a verified QR, address, URL, interface, date, or fact only when the brief explicitly authorizes it and it has been checked. Do not imply investment returns, guaranteed outcomes, risk-free self-custody, inevitable adoption, or universal local conclusions. Do not turn a named service into a recommendation.

Produce a bundle in the guide-specific `Assets/diploma/<student-guide|educator-guide|shared>/<asset-id-lowercase>/` folder selected from the placement. Include `micrographic.html`, `micrographic.css`, `meta.json`, `preview.html` in a 458px review frame, `alt-text.md`, `README.md`, and `sanity-asset.json`. Prefix CSS selectors with a unique `.mg-<slug>` root; tag all translatable text with non-nested `data-t` keys; use no JavaScript, external assets, external fonts, CSS grid, vh/vw, rem, fixed/sticky positioning, or `@import`. Do not upload or publish to Sanity. Before declaring completion, report visual checks at 458px, phone, desktop, A4/US Letter, and grayscale.

Required inputs to attach
- Approved transparent PNG reference: Assets/Reference/bd-v-042-ref.jpg
- Matching white-background JPG preview: Assets/Reference/bd-v-042-ref.jpg
- Matching conformance report: Assets/Reference/bd-v-042-ref.json
- Current Claude Design System authoring instructions and closest approved micrographic bundle
- Current Sanity schema/publishing requirements, if available

Complete asset brief
- Asset ID: BD-V-042
- Suggested by: Pablo
- Priority: Supporting
- Type: Diagram
- Historical page/note: 29; add a graphic comparing hot, hardware/cold, and custodial wallets or accounts.
- Placement: SG: Under `### Hot and cold wallets`, after the introductory explanation. EG: under `### Hot, cold, hardware, and custodial are different dimensions`, replace the matching marker after the source text at the listed EG line. See section 3.8 for the exact anchor.
- Source locator: SG: 885; EG: 2048
- Text–visual link: Connects wallet type to exposure and use rather than treating `hot`, `cold`, and `custodial` as one scale.
- Design brief: Use two axes or layers: key control (`custodial` versus `self-custodial`) and connectivity or signing environment (`hot` versus `cold or hardware`). Place common use patterns and threat examples in the correct areas. Explicitly show that a custodial account is not a type of self-custodial wallet.
- Format: Two-axis classification graphic; full width.

Use the exact heading and insertion direction in Placement as the target placement. Preserve all listed placements in metadata. Include source-brief revision, reference paths, factual sources, production date, reviewer status, checks, and unresolved judgments in README.md. Set `reviewStatus` to draft or review unless an authorized reviewer has approved it.
```
### [ ] BD-V-041 — Table

```text
You are building one production-ready, accessible My First Bitcoin Bitcoin Diploma visual from a supplied approved transparent PNG reference, its white-background JPG preview, and their JSON conformance report. Read the complete brief below before acting. The asset brief is the source of truth for lesson intent, content, safety, caption, alt text, placement, and localization. The reference image guides composition only. If it conflicts with the brief, the brief wins; report any unresolved factual or design-system gap before implementing.

Rebuild—not trace or embed—the reference as editable HTML, CSS, and inline SVG. Apply the supplied Claude Design System rather than the reference's provisional styling. Keep all essential geometry, arrows, labels, warnings, icons, and data editable. Preserve one clear teaching relationship, a decisive reading order, cultural replaceability, grayscale meaning, narrow-page responsiveness, phone and desktop usability, A4/US-Letter printing, expandable translated text, and future RTL adaptation.

Never invent facts, labels, numbers, providers, URLs, legal claims, safety claims, or brand choices. Preserve every prohibition and qualification in the brief. Do not include real seed phrases, private keys, payable addresses, private learner data, balances, or transactions. Use a verified QR, address, URL, interface, date, or fact only when the brief explicitly authorizes it and it has been checked. Do not imply investment returns, guaranteed outcomes, risk-free self-custody, inevitable adoption, or universal local conclusions. Do not turn a named service into a recommendation.

Produce a bundle in the guide-specific `Assets/diploma/<student-guide|educator-guide|shared>/<asset-id-lowercase>/` folder selected from the placement. Include `micrographic.html`, `micrographic.css`, `meta.json`, `preview.html` in a 458px review frame, `alt-text.md`, `README.md`, and `sanity-asset.json`. Prefix CSS selectors with a unique `.mg-<slug>` root; tag all translatable text with non-nested `data-t` keys; use no JavaScript, external assets, external fonts, CSS grid, vh/vw, rem, fixed/sticky positioning, or `@import`. Do not upload or publish to Sanity. Before declaring completion, report visual checks at 458px, phone, desktop, A4/US Letter, and grayscale.

Required inputs to attach
- Approved transparent PNG reference: Assets/Reference/bd-v-041-ref.jpg
- Matching white-background JPG preview: Assets/Reference/bd-v-041-ref.jpg
- Matching conformance report: Assets/Reference/bd-v-041-ref.json
- Current Claude Design System authoring instructions and closest approved micrographic bundle
- Current Sanity schema/publishing requirements, if available

Complete asset brief
- Asset ID: BD-V-041
- Suggested by: AI
- Priority: Supporting
- Type: Table
- Historical page/note: 29; make hot, cold, hardware, and custody distinctions easy to scan.
- Placement: Under `### Hot and cold wallets`, replace the existing `Arrangement / Common strength / Responsibility to remember` table visually while retaining an accessible text equivalent.
- Source locator: 887
- Text–visual link: Prevents learners from treating custody and connectivity as one scale.
- Design brief: Preserve the current columns and the rows for hot wallet, hardware or cold wallet, and custodial account. Distinguish key control from signing environment; use the qualifications in `BD-V-042` to prevent treating custody and connectivity as one scale. Preserve one common strength and one responsibility for each arrangement.
- Format: Wallet-use comparison table; full width.

Use the exact heading and insertion direction in Placement as the target placement. Preserve all listed placements in metadata. Include source-brief revision, reference paths, factual sources, production date, reviewer status, checks, and unresolved judgments in README.md. Set `reviewStatus` to draft or review unless an authorized reviewer has approved it.
```
### [ ] BD-V-043 — Diagram

```text
You are building one production-ready, accessible My First Bitcoin Bitcoin Diploma visual from a supplied approved transparent PNG reference, its white-background JPG preview, and their JSON conformance report. Read the complete brief below before acting. The asset brief is the source of truth for lesson intent, content, safety, caption, alt text, placement, and localization. The reference image guides composition only. If it conflicts with the brief, the brief wins; report any unresolved factual or design-system gap before implementing.

Rebuild—not trace or embed—the reference as editable HTML, CSS, and inline SVG. Apply the supplied Claude Design System rather than the reference's provisional styling. Keep all essential geometry, arrows, labels, warnings, icons, and data editable. Preserve one clear teaching relationship, a decisive reading order, cultural replaceability, grayscale meaning, narrow-page responsiveness, phone and desktop usability, A4/US-Letter printing, expandable translated text, and future RTL adaptation.

Never invent facts, labels, numbers, providers, URLs, legal claims, safety claims, or brand choices. Preserve every prohibition and qualification in the brief. Do not include real seed phrases, private keys, payable addresses, private learner data, balances, or transactions. Use a verified QR, address, URL, interface, date, or fact only when the brief explicitly authorizes it and it has been checked. Do not imply investment returns, guaranteed outcomes, risk-free self-custody, inevitable adoption, or universal local conclusions. Do not turn a named service into a recommendation.

Produce a bundle in the guide-specific `Assets/diploma/<student-guide|educator-guide|shared>/<asset-id-lowercase>/` folder selected from the placement. Include `micrographic.html`, `micrographic.css`, `meta.json`, `preview.html` in a 458px review frame, `alt-text.md`, `README.md`, and `sanity-asset.json`. Prefix CSS selectors with a unique `.mg-<slug>` root; tag all translatable text with non-nested `data-t` keys; use no JavaScript, external assets, external fonts, CSS grid, vh/vw, rem, fixed/sticky positioning, or `@import`. Do not upload or publish to Sanity. Before declaring completion, report visual checks at 458px, phone, desktop, A4/US Letter, and grayscale.

Required inputs to attach
- Approved transparent PNG reference: Assets/Reference/bd-v-043-ref.jpg
- Matching white-background JPG preview: Assets/Reference/bd-v-043-ref.jpg
- Matching conformance report: Assets/Reference/bd-v-043-ref.json
- Current Claude Design System authoring instructions and closest approved micrographic bundle
- Current Sanity schema/publishing requirements, if available

Complete asset brief
- Asset ID: BD-V-043
- Suggested by: Pablo
- Priority: Essential
- Type: Diagram
- Historical page/note: 28–30; add a visual recovery-readiness activity and keep practice private and low risk.
- Placement: Under `### Wallet recovery and seed phrase testing`, after the six numbered recovery-readiness steps and before “The point is not to make recovery feel easy”.
- Source locator: 908
- Text–visual link: Turns the recovery text into a safe sequence a learner can rehearse.
- Design brief: Follow the six current steps: use official instructions for the exact training wallet; confirm compatibility; work privately; use the approved backup-check or recovery method; confirm expected receiving information or training history; reset or clear the temporary environment. Use only prepared, empty, or simulated materials. Put `educator never sees the secret` outside every step. Do not instruct learners to erase a wallet before verifying its backup or introduce real funds.
- Format: Safety-gated workflow; full width.

Use the exact heading and insertion direction in Placement as the target placement. Preserve all listed placements in metadata. Include source-brief revision, reference paths, factual sources, production date, reviewer status, checks, and unresolved judgments in README.md. Set `reviewStatus` to draft or review unless an authorized reviewer has approved it.
```
### [ ] BD-V-044 — Image

```text
You are building one production-ready, accessible My First Bitcoin Bitcoin Diploma visual from a supplied approved transparent PNG reference, its white-background JPG preview, and their JSON conformance report. Read the complete brief below before acting. The asset brief is the source of truth for lesson intent, content, safety, caption, alt text, placement, and localization. The reference image guides composition only. If it conflicts with the brief, the brief wins; report any unresolved factual or design-system gap before implementing.

Rebuild—not trace or embed—the reference as editable HTML, CSS, and inline SVG. Apply the supplied Claude Design System rather than the reference's provisional styling. Keep all essential geometry, arrows, labels, warnings, icons, and data editable. Preserve one clear teaching relationship, a decisive reading order, cultural replaceability, grayscale meaning, narrow-page responsiveness, phone and desktop usability, A4/US-Letter printing, expandable translated text, and future RTL adaptation.

Never invent facts, labels, numbers, providers, URLs, legal claims, safety claims, or brand choices. Preserve every prohibition and qualification in the brief. Do not include real seed phrases, private keys, payable addresses, private learner data, balances, or transactions. Use a verified QR, address, URL, interface, date, or fact only when the brief explicitly authorizes it and it has been checked. Do not imply investment returns, guaranteed outcomes, risk-free self-custody, inevitable adoption, or universal local conclusions. Do not turn a named service into a recommendation.

Produce a bundle in the guide-specific `Assets/diploma/<student-guide|educator-guide|shared>/<asset-id-lowercase>/` folder selected from the placement. Include `micrographic.html`, `micrographic.css`, `meta.json`, `preview.html` in a 458px review frame, `alt-text.md`, `README.md`, and `sanity-asset.json`. Prefix CSS selectors with a unique `.mg-<slug>` root; tag all translatable text with non-nested `data-t` keys; use no JavaScript, external assets, external fonts, CSS grid, vh/vw, rem, fixed/sticky positioning, or `@import`. Do not upload or publish to Sanity. Before declaring completion, report visual checks at 458px, phone, desktop, A4/US Letter, and grayscale.

Required inputs to attach
- Approved transparent PNG reference: Assets/Reference/bd-v-044-ref.jpg
- Matching white-background JPG preview: Assets/Reference/bd-v-044-ref.jpg
- Matching conformance report: Assets/Reference/bd-v-044-ref.json
- Current Claude Design System authoring instructions and closest approved micrographic bundle
- Current Sanity schema/publishing requirements, if available

Complete asset brief
- Asset ID: BD-V-044
- Suggested by: AI
- Priority: Essential
- Type: Image
- Historical page/note: 31; add a visual receiving activity and receive-screen competency exercise without real funds.
- Placement: SG: Under `### Receiving bitcoin`, after the receive steps. EG: under `### Receiving bitcoin`, replace the matching marker after the source text at the listed EG line. See section 3.8 for the exact anchor.
- Source locator: SG: 922; EG: 2072
- Text–visual link: Lets a learner identify the elements of a receive request before live practice.
- Design brief: Show receiver device, sample address or QR, sender verification, broadcast or pending status, and confirmation. Annotate amount, unit, network, address, and status. Use fictional data and mark the whole visual non-payable.
- Format: Annotated receiving flow; full width.

Use the exact heading and insertion direction in Placement as the target placement. Preserve all listed placements in metadata. Include source-brief revision, reference paths, factual sources, production date, reviewer status, checks, and unresolved judgments in README.md. Set `reviewStatus` to draft or review unless an authorized reviewer has approved it.
```
### [ ] BD-V-045 — Diagram

```text
You are building one production-ready, accessible My First Bitcoin Bitcoin Diploma visual from a supplied approved transparent PNG reference, its white-background JPG preview, and their JSON conformance report. Read the complete brief below before acting. The asset brief is the source of truth for lesson intent, content, safety, caption, alt text, placement, and localization. The reference image guides composition only. If it conflicts with the brief, the brief wins; report any unresolved factual or design-system gap before implementing.

Rebuild—not trace or embed—the reference as editable HTML, CSS, and inline SVG. Apply the supplied Claude Design System rather than the reference's provisional styling. Keep all essential geometry, arrows, labels, warnings, icons, and data editable. Preserve one clear teaching relationship, a decisive reading order, cultural replaceability, grayscale meaning, narrow-page responsiveness, phone and desktop usability, A4/US-Letter printing, expandable translated text, and future RTL adaptation.

Never invent facts, labels, numbers, providers, URLs, legal claims, safety claims, or brand choices. Preserve every prohibition and qualification in the brief. Do not include real seed phrases, private keys, payable addresses, private learner data, balances, or transactions. Use a verified QR, address, URL, interface, date, or fact only when the brief explicitly authorizes it and it has been checked. Do not imply investment returns, guaranteed outcomes, risk-free self-custody, inevitable adoption, or universal local conclusions. Do not turn a named service into a recommendation.

Produce a bundle in the guide-specific `Assets/diploma/<student-guide|educator-guide|shared>/<asset-id-lowercase>/` folder selected from the placement. Include `micrographic.html`, `micrographic.css`, `meta.json`, `preview.html` in a 458px review frame, `alt-text.md`, `README.md`, and `sanity-asset.json`. Prefix CSS selectors with a unique `.mg-<slug>` root; tag all translatable text with non-nested `data-t` keys; use no JavaScript, external assets, external fonts, CSS grid, vh/vw, rem, fixed/sticky positioning, or `@import`. Do not upload or publish to Sanity. Before declaring completion, report visual checks at 458px, phone, desktop, A4/US Letter, and grayscale.

Required inputs to attach
- Approved transparent PNG reference: Assets/Reference/bd-v-045-ref.jpg
- Matching white-background JPG preview: Assets/Reference/bd-v-045-ref.jpg
- Matching conformance report: Assets/Reference/bd-v-045-ref.json
- Current Claude Design System authoring instructions and closest approved micrographic bundle
- Current Sanity schema/publishing requirements, if available

Complete asset brief
- Asset ID: BD-V-045
- Suggested by: AI
- Priority: Essential
- Type: Diagram
- Historical page/note: 32; make sending, address, and network checks visual and explain how to perform them.
- Placement: SG: Under `### Sending bitcoin`, after the pre-send steps. EG: under `### Sending bitcoin`, replace the matching marker after the source text at the listed EG line. See section 3.8 for the exact anchor.
- Source locator: SG: 937; EG: 2106
- Text–visual link: Makes verification happen before approval and separates recipient checks from fee and timing decisions.
- Design brief: Show independently verified recipient and purpose → payment method → scan or copy and compare destination → check amount, unit, fee or expiry, and final summary → small test when unfamiliar → approve only if all checks match → check the result. Branch to stop and verify if anything differs. For on-chain payments, show pending/confirmation status and a sample txid; for Lightning, show success or failure without implying an on-chain txid for each payment. Mark approval as the point after which a valid payment is usually irreversible.
- Format: Preflight-to-settlement flow; full width.

Use the exact heading and insertion direction in Placement as the target placement. Preserve all listed placements in metadata. Include source-brief revision, reference paths, factual sources, production date, reviewer status, checks, and unresolved judgments in README.md. Set `reviewStatus` to draft or review unless an authorized reviewer has approved it.
```
### [ ] BD-V-046 — Diagram

```text
You are building one production-ready, accessible My First Bitcoin Bitcoin Diploma visual from a supplied approved transparent PNG reference, its white-background JPG preview, and their JSON conformance report. Read the complete brief below before acting. The asset brief is the source of truth for lesson intent, content, safety, caption, alt text, placement, and localization. The reference image guides composition only. If it conflicts with the brief, the brief wins; report any unresolved factual or design-system gap before implementing.

Rebuild—not trace or embed—the reference as editable HTML, CSS, and inline SVG. Apply the supplied Claude Design System rather than the reference's provisional styling. Keep all essential geometry, arrows, labels, warnings, icons, and data editable. Preserve one clear teaching relationship, a decisive reading order, cultural replaceability, grayscale meaning, narrow-page responsiveness, phone and desktop usability, A4/US-Letter printing, expandable translated text, and future RTL adaptation.

Never invent facts, labels, numbers, providers, URLs, legal claims, safety claims, or brand choices. Preserve every prohibition and qualification in the brief. Do not include real seed phrases, private keys, payable addresses, private learner data, balances, or transactions. Use a verified QR, address, URL, interface, date, or fact only when the brief explicitly authorizes it and it has been checked. Do not imply investment returns, guaranteed outcomes, risk-free self-custody, inevitable adoption, or universal local conclusions. Do not turn a named service into a recommendation.

Produce a bundle in the guide-specific `Assets/diploma/<student-guide|educator-guide|shared>/<asset-id-lowercase>/` folder selected from the placement. Include `micrographic.html`, `micrographic.css`, `meta.json`, `preview.html` in a 458px review frame, `alt-text.md`, `README.md`, and `sanity-asset.json`. Prefix CSS selectors with a unique `.mg-<slug>` root; tag all translatable text with non-nested `data-t` keys; use no JavaScript, external assets, external fonts, CSS grid, vh/vw, rem, fixed/sticky positioning, or `@import`. Do not upload or publish to Sanity. Before declaring completion, report visual checks at 458px, phone, desktop, A4/US Letter, and grayscale.

Required inputs to attach
- Approved transparent PNG reference: Assets/Reference/bd-v-046-ref.jpg
- Matching white-background JPG preview: Assets/Reference/bd-v-046-ref.jpg
- Matching conformance report: Assets/Reference/bd-v-046-ref.json
- Current Claude Design System authoring instructions and closest approved micrographic bundle
- Current Sanity schema/publishing requirements, if available

Complete asset brief
- Asset ID: BD-V-046
- Suggested by: Pablo
- Priority: Essential
- Type: Diagram
- Historical page/note: 32–33; add a *txid*/explorer activity and explain first confirmation, block depth, and privacy.
- Placement: SG: Under `### Verification, block explorers, and irreversible transactions`, after the confirmation explanation. EG: under `### Block explorers and verification`, replace the matching marker after the source text at the listed EG line. See section 3.8 for the exact anchor.
- Source locator: SG: 947; EG: 2153
- Text–visual link: Connects transaction status, block inclusion, and later confirmations.
- Design brief: Show a transaction first in the pending pool, then included in Block N as confirmation 1, followed by Blocks N+1, N+2, and N+3 increasing depth. Pair it with a small annotated fictional explorer panel showing *txid*, amount, fee, status, and confirmations. Add a privacy callout about searching personal data.
- Format: Confirmation timeline plus explorer inset; full width.

Use the exact heading and insertion direction in Placement as the target placement. Preserve all listed placements in metadata. Include source-brief revision, reference paths, factual sources, production date, reviewer status, checks, and unresolved judgments in README.md. Set `reviewStatus` to draft or review unless an authorized reviewer has approved it.
```
### [ ] BD-V-047 — Image

```text
You are building one production-ready, accessible My First Bitcoin Bitcoin Diploma visual from a supplied approved transparent PNG reference, its white-background JPG preview, and their JSON conformance report. Read the complete brief below before acting. The asset brief is the source of truth for lesson intent, content, safety, caption, alt text, placement, and localization. The reference image guides composition only. If it conflicts with the brief, the brief wins; report any unresolved factual or design-system gap before implementing.

Rebuild—not trace or embed—the reference as editable HTML, CSS, and inline SVG. Apply the supplied Claude Design System rather than the reference's provisional styling. Keep all essential geometry, arrows, labels, warnings, icons, and data editable. Preserve one clear teaching relationship, a decisive reading order, cultural replaceability, grayscale meaning, narrow-page responsiveness, phone and desktop usability, A4/US-Letter printing, expandable translated text, and future RTL adaptation.

Never invent facts, labels, numbers, providers, URLs, legal claims, safety claims, or brand choices. Preserve every prohibition and qualification in the brief. Do not include real seed phrases, private keys, payable addresses, private learner data, balances, or transactions. Use a verified QR, address, URL, interface, date, or fact only when the brief explicitly authorizes it and it has been checked. Do not imply investment returns, guaranteed outcomes, risk-free self-custody, inevitable adoption, or universal local conclusions. Do not turn a named service into a recommendation.

Produce a bundle in the guide-specific `Assets/diploma/<student-guide|educator-guide|shared>/<asset-id-lowercase>/` folder selected from the placement. Include `micrographic.html`, `micrographic.css`, `meta.json`, `preview.html` in a 458px review frame, `alt-text.md`, `README.md`, and `sanity-asset.json`. Prefix CSS selectors with a unique `.mg-<slug>` root; tag all translatable text with non-nested `data-t` keys; use no JavaScript, external assets, external fonts, CSS grid, vh/vw, rem, fixed/sticky positioning, or `@import`. Do not upload or publish to Sanity. Before declaring completion, report visual checks at 458px, phone, desktop, A4/US Letter, and grayscale.

Required inputs to attach
- Approved transparent PNG reference: Assets/Reference/bd-v-047-ref.jpg
- Matching white-background JPG preview: Assets/Reference/bd-v-047-ref.jpg
- Matching conformance report: Assets/Reference/bd-v-047-ref.json
- Current Claude Design System authoring instructions and closest approved micrographic bundle
- Current Sanity schema/publishing requirements, if available

Complete asset brief
- Asset ID: BD-V-047
- Suggested by: Pablo
- Priority: Supporting
- Type: Image
- Historical page/note: 33–34; add a red-flag image for a potential scam.
- Placement: SG: Under `### Safety checklist`, before the red-flag examples. EG: under `### Scam recognition and safe response`, replace the matching marker after the source text at the listed EG line. See section 3.8 for the exact anchor.
- Source locator: SG: 955; EG: 2187
- Text–visual link: Gives learners an immediate visual cue to pause when a message or offer shows scam signals.
- Design brief: Show a prominent red flag beside a generic, nonfunctional message or offer. Add concise warning cues for impersonation, urgency, guaranteed returns, giveaway or recovery requests, fake applications, phishing, relationship manipulation, and too-good-to-be-true claims. Include the action `stop, verify independently, and never share a seed phrase or private key`. Do not use a real brand, address, payment request, or a realistic phishing link.
- Format: Red-flag scam-warning illustration; half width.

Use the exact heading and insertion direction in Placement as the target placement. Preserve all listed placements in metadata. Include source-brief revision, reference paths, factual sources, production date, reviewer status, checks, and unresolved judgments in README.md. Set `reviewStatus` to draft or review unless an authorized reviewer has approved it.
```
### [ ] BD-V-048 — Diagram

```text
You are building one production-ready, accessible My First Bitcoin Bitcoin Diploma visual from a supplied approved transparent PNG reference, its white-background JPG preview, and their JSON conformance report. Read the complete brief below before acting. The asset brief is the source of truth for lesson intent, content, safety, caption, alt text, placement, and localization. The reference image guides composition only. If it conflicts with the brief, the brief wins; report any unresolved factual or design-system gap before implementing.

Rebuild—not trace or embed—the reference as editable HTML, CSS, and inline SVG. Apply the supplied Claude Design System rather than the reference's provisional styling. Keep all essential geometry, arrows, labels, warnings, icons, and data editable. Preserve one clear teaching relationship, a decisive reading order, cultural replaceability, grayscale meaning, narrow-page responsiveness, phone and desktop usability, A4/US-Letter printing, expandable translated text, and future RTL adaptation.

Never invent facts, labels, numbers, providers, URLs, legal claims, safety claims, or brand choices. Preserve every prohibition and qualification in the brief. Do not include real seed phrases, private keys, payable addresses, private learner data, balances, or transactions. Use a verified QR, address, URL, interface, date, or fact only when the brief explicitly authorizes it and it has been checked. Do not imply investment returns, guaranteed outcomes, risk-free self-custody, inevitable adoption, or universal local conclusions. Do not turn a named service into a recommendation.

Produce a bundle in the guide-specific `Assets/diploma/<student-guide|educator-guide|shared>/<asset-id-lowercase>/` folder selected from the placement. Include `micrographic.html`, `micrographic.css`, `meta.json`, `preview.html` in a 458px review frame, `alt-text.md`, `README.md`, and `sanity-asset.json`. Prefix CSS selectors with a unique `.mg-<slug>` root; tag all translatable text with non-nested `data-t` keys; use no JavaScript, external assets, external fonts, CSS grid, vh/vw, rem, fixed/sticky positioning, or `@import`. Do not upload or publish to Sanity. Before declaring completion, report visual checks at 458px, phone, desktop, A4/US Letter, and grayscale.

Required inputs to attach
- Approved transparent PNG reference: Assets/Reference/bd-v-048-ref.jpg
- Matching white-background JPG preview: Assets/Reference/bd-v-048-ref.jpg
- Matching conformance report: Assets/Reference/bd-v-048-ref.json
- Current Claude Design System authoring instructions and closest approved micrographic bundle
- Current Sanity schema/publishing requirements, if available

Complete asset brief
- Asset ID: BD-V-048
- Suggested by: Pablo
- Priority: Supporting
- Type: Diagram
- Historical page/note: 35; turn acquisition/exchange pathways into a one-page comparison activity.
- Placement: SG: Under `### Acquiring and exchanging bitcoin`, after `#### Awareness, not financial advice` and the pathway overview, and before the comparison questions. EG: under `### Acquiring and exchanging: awareness, not financial advice`, replace the matching marker after the source text at the listed EG line. See section 3.8 for the exact anchor.
- Source locator: SG: 971; EG: 2229
- Text–visual link: Shows that acquiring bitcoin is an end-to-end route with risks before and after the moment of exchange.
- Design brief: Map earning, peer-to-peer, exchange or broker, ATM or kiosk, and merchant or community receipt as separate paths into either self-custody or custodial balance. Label price or spread, fees, identity, reversibility, counterparty, withdrawal, and local-law checkpoints. Do not rank or recommend a provider.
- Format: Branching pathway map; full width.

Use the exact heading and insertion direction in Placement as the target placement. Preserve all listed placements in metadata. Include source-brief revision, reference paths, factual sources, production date, reviewer status, checks, and unresolved judgments in README.md. Set `reviewStatus` to draft or review unless an authorized reviewer has approved it.
```
### [ ] BD-V-049 — Table

```text
You are building one production-ready, accessible My First Bitcoin Bitcoin Diploma visual from a supplied approved transparent PNG reference, its white-background JPG preview, and their JSON conformance report. Read the complete brief below before acting. The asset brief is the source of truth for lesson intent, content, safety, caption, alt text, placement, and localization. The reference image guides composition only. If it conflicts with the brief, the brief wins; report any unresolved factual or design-system gap before implementing.

Rebuild—not trace or embed—the reference as editable HTML, CSS, and inline SVG. Apply the supplied Claude Design System rather than the reference's provisional styling. Keep all essential geometry, arrows, labels, warnings, icons, and data editable. Preserve one clear teaching relationship, a decisive reading order, cultural replaceability, grayscale meaning, narrow-page responsiveness, phone and desktop usability, A4/US-Letter printing, expandable translated text, and future RTL adaptation.

Never invent facts, labels, numbers, providers, URLs, legal claims, safety claims, or brand choices. Preserve every prohibition and qualification in the brief. Do not include real seed phrases, private keys, payable addresses, private learner data, balances, or transactions. Use a verified QR, address, URL, interface, date, or fact only when the brief explicitly authorizes it and it has been checked. Do not imply investment returns, guaranteed outcomes, risk-free self-custody, inevitable adoption, or universal local conclusions. Do not turn a named service into a recommendation.

Produce a bundle in the guide-specific `Assets/diploma/<student-guide|educator-guide|shared>/<asset-id-lowercase>/` folder selected from the placement. Include `micrographic.html`, `micrographic.css`, `meta.json`, `preview.html` in a 458px review frame, `alt-text.md`, `README.md`, and `sanity-asset.json`. Prefix CSS selectors with a unique `.mg-<slug>` root; tag all translatable text with non-nested `data-t` keys; use no JavaScript, external assets, external fonts, CSS grid, vh/vw, rem, fixed/sticky positioning, or `@import`. Do not upload or publish to Sanity. Before declaring completion, report visual checks at 458px, phone, desktop, A4/US Letter, and grayscale.

Required inputs to attach
- Approved transparent PNG reference: Assets/Reference/bd-v-049-ref.jpg
- Matching white-background JPG preview: Assets/Reference/bd-v-049-ref.jpg
- Matching conformance report: Assets/Reference/bd-v-049-ref.json
- Current Claude Design System authoring instructions and closest approved micrographic bundle
- Current Sanity schema/publishing requirements, if available

Complete asset brief
- Asset ID: BD-V-049
- Suggested by: Pablo
- Priority: Essential
- Type: Table
- Historical page/note: 35; make the acquisition-pathway questions practical and easy to scan.
- Placement: Under `### Acquiring and exchanging bitcoin`, replace the existing `Risk area / Question to ask` table visually while retaining an accessible text equivalent.
- Source locator: 975
- Text–visual link: Helps learners assess a complete acquisition or exchange route instead of focusing only on price.
- Design brief: Preserve the six existing risk-area rows and their questions: costs; custody; identity and privacy; withdrawal and settlement; counterparty and safety; local context. Keep each question editable, neutral, and locally verifiable. Include no provider names, rankings, or legal conclusions.
- Format: Icon-supported risk-check table; full width.

Use the exact heading and insertion direction in Placement as the target placement. Preserve all listed placements in metadata. Include source-brief revision, reference paths, factual sources, production date, reviewer status, checks, and unresolved judgments in README.md. Set `reviewStatus` to draft or review unless an authorized reviewer has approved it.
```
### [ ] BD-V-050 — Diagram

```text
You are building one production-ready, accessible My First Bitcoin Bitcoin Diploma visual from a supplied approved transparent PNG reference, its white-background JPG preview, and their JSON conformance report. Read the complete brief below before acting. The asset brief is the source of truth for lesson intent, content, safety, caption, alt text, placement, and localization. The reference image guides composition only. If it conflicts with the brief, the brief wins; report any unresolved factual or design-system gap before implementing.

Rebuild—not trace or embed—the reference as editable HTML, CSS, and inline SVG. Apply the supplied Claude Design System rather than the reference's provisional styling. Keep all essential geometry, arrows, labels, warnings, icons, and data editable. Preserve one clear teaching relationship, a decisive reading order, cultural replaceability, grayscale meaning, narrow-page responsiveness, phone and desktop usability, A4/US-Letter printing, expandable translated text, and future RTL adaptation.

Never invent facts, labels, numbers, providers, URLs, legal claims, safety claims, or brand choices. Preserve every prohibition and qualification in the brief. Do not include real seed phrases, private keys, payable addresses, private learner data, balances, or transactions. Use a verified QR, address, URL, interface, date, or fact only when the brief explicitly authorizes it and it has been checked. Do not imply investment returns, guaranteed outcomes, risk-free self-custody, inevitable adoption, or universal local conclusions. Do not turn a named service into a recommendation.

Produce a bundle in the guide-specific `Assets/diploma/<student-guide|educator-guide|shared>/<asset-id-lowercase>/` folder selected from the placement. Include `micrographic.html`, `micrographic.css`, `meta.json`, `preview.html` in a 458px review frame, `alt-text.md`, `README.md`, and `sanity-asset.json`. Prefix CSS selectors with a unique `.mg-<slug>` root; tag all translatable text with non-nested `data-t` keys; use no JavaScript, external assets, external fonts, CSS grid, vh/vw, rem, fixed/sticky positioning, or `@import`. Do not upload or publish to Sanity. Before declaring completion, report visual checks at 458px, phone, desktop, A4/US Letter, and grayscale.

Required inputs to attach
- Approved transparent PNG reference: Assets/Reference/bd-v-050-ref.jpg
- Matching white-background JPG preview: Assets/Reference/bd-v-050-ref.jpg
- Matching conformance report: Assets/Reference/bd-v-050-ref.json
- Current Claude Design System authoring instructions and closest approved micrographic bundle
- Current Sanity schema/publishing requirements, if available

Complete asset brief
- Asset ID: BD-V-050
- Suggested by: Pablo
- Priority: Essential
- Type: Diagram
- Historical page/note: 33 and 36–37; distinguish destinations, add examples and trade-offs, and route deeper mechanics to Advanced.
- Placement: SG: Under `### On-chain and Lightning payments`, after the introductory comparison. EG: under `### On-chain and Lightning payments`, replace the matching marker after the source text at the listed EG line. See section 3.8 for the exact anchor.
- Source locator: SG: 988; EG: 2253
- Text–visual link: Makes the layer relationship and appropriate-use distinction visible.
- Design brief: Show Bitcoin base-layer settlement beneath Lightning payment channels. Compare payment request, route, timing, fee conditions, custody variability, and failure modes. Use one small-payment and one final-settlement example. Do not imply that Lightning is a separate coin or that all Lightning wallets are self-custodial.
- Format: Layer diagram plus concise comparison; full width.

Use the exact heading and insertion direction in Placement as the target placement. Preserve all listed placements in metadata. Include source-brief revision, reference paths, factual sources, production date, reviewer status, checks, and unresolved judgments in README.md. Set `reviewStatus` to draft or review unless an authorized reviewer has approved it.
```
### [ ] BD-V-051 — Table

```text
You are building one production-ready, accessible My First Bitcoin Bitcoin Diploma visual from a supplied approved transparent PNG reference, its white-background JPG preview, and their JSON conformance report. Read the complete brief below before acting. The asset brief is the source of truth for lesson intent, content, safety, caption, alt text, placement, and localization. The reference image guides composition only. If it conflicts with the brief, the brief wins; report any unresolved factual or design-system gap before implementing.

Rebuild—not trace or embed—the reference as editable HTML, CSS, and inline SVG. Apply the supplied Claude Design System rather than the reference's provisional styling. Keep all essential geometry, arrows, labels, warnings, icons, and data editable. Preserve one clear teaching relationship, a decisive reading order, cultural replaceability, grayscale meaning, narrow-page responsiveness, phone and desktop usability, A4/US-Letter printing, expandable translated text, and future RTL adaptation.

Never invent facts, labels, numbers, providers, URLs, legal claims, safety claims, or brand choices. Preserve every prohibition and qualification in the brief. Do not include real seed phrases, private keys, payable addresses, private learner data, balances, or transactions. Use a verified QR, address, URL, interface, date, or fact only when the brief explicitly authorizes it and it has been checked. Do not imply investment returns, guaranteed outcomes, risk-free self-custody, inevitable adoption, or universal local conclusions. Do not turn a named service into a recommendation.

Produce a bundle in the guide-specific `Assets/diploma/<student-guide|educator-guide|shared>/<asset-id-lowercase>/` folder selected from the placement. Include `micrographic.html`, `micrographic.css`, `meta.json`, `preview.html` in a 458px review frame, `alt-text.md`, `README.md`, and `sanity-asset.json`. Prefix CSS selectors with a unique `.mg-<slug>` root; tag all translatable text with non-nested `data-t` keys; use no JavaScript, external assets, external fonts, CSS grid, vh/vw, rem, fixed/sticky positioning, or `@import`. Do not upload or publish to Sanity. Before declaring completion, report visual checks at 458px, phone, desktop, A4/US Letter, and grayscale.

Required inputs to attach
- Approved transparent PNG reference: Assets/Reference/bd-v-051-ref.jpg
- Matching white-background JPG preview: Assets/Reference/bd-v-051-ref.jpg
- Matching conformance report: Assets/Reference/bd-v-051-ref.json
- Current Claude Design System authoring instructions and closest approved micrographic bundle
- Current Sanity schema/publishing requirements, if available

Complete asset brief
- Asset ID: BD-V-051
- Suggested by: AI
- Priority: Supporting
- Type: Table
- Historical page/note: 33 and 36–37; provide an on-chain-versus-Lightning learner reference.
- Placement: Under `### On-chain and Lightning payments`, replace the existing `Question / On-chain Bitcoin / Lightning` table visually while retaining an accessible text equivalent.
- Source locator: 990
- Text–visual link: Lets learners compare payment requests, settlement, timing, fees, typical use, and introductory risks across the two paths.
- Design brief: Preserve the four current rows: receiving information, payment result, common use, and beginner checks. Keep invoice, offer, and supported Lightning-address wording, plus expiry and payment-result checks. Retain custody and fee qualifications from the adjacent prose. Do not imply that Lightning is a separate coin or that either path is universally better.
- Format: Payment-path comparison table; full width.

Use the exact heading and insertion direction in Placement as the target placement. Preserve all listed placements in metadata. Include source-brief revision, reference paths, factual sources, production date, reviewer status, checks, and unresolved judgments in README.md. Set `reviewStatus` to draft or review unless an authorized reviewer has approved it.
```
### [ ] BD-V-052 — Diagram

```text
You are building one production-ready, accessible My First Bitcoin Bitcoin Diploma visual from a supplied approved transparent PNG reference, its white-background JPG preview, and their JSON conformance report. Read the complete brief below before acting. The asset brief is the source of truth for lesson intent, content, safety, caption, alt text, placement, and localization. The reference image guides composition only. If it conflicts with the brief, the brief wins; report any unresolved factual or design-system gap before implementing.

Rebuild—not trace or embed—the reference as editable HTML, CSS, and inline SVG. Apply the supplied Claude Design System rather than the reference's provisional styling. Keep all essential geometry, arrows, labels, warnings, icons, and data editable. Preserve one clear teaching relationship, a decisive reading order, cultural replaceability, grayscale meaning, narrow-page responsiveness, phone and desktop usability, A4/US-Letter printing, expandable translated text, and future RTL adaptation.

Never invent facts, labels, numbers, providers, URLs, legal claims, safety claims, or brand choices. Preserve every prohibition and qualification in the brief. Do not include real seed phrases, private keys, payable addresses, private learner data, balances, or transactions. Use a verified QR, address, URL, interface, date, or fact only when the brief explicitly authorizes it and it has been checked. Do not imply investment returns, guaranteed outcomes, risk-free self-custody, inevitable adoption, or universal local conclusions. Do not turn a named service into a recommendation.

Produce a bundle in the guide-specific `Assets/diploma/<student-guide|educator-guide|shared>/<asset-id-lowercase>/` folder selected from the placement. Include `micrographic.html`, `micrographic.css`, `meta.json`, `preview.html` in a 458px review frame, `alt-text.md`, `README.md`, and `sanity-asset.json`. Prefix CSS selectors with a unique `.mg-<slug>` root; tag all translatable text with non-nested `data-t` keys; use no JavaScript, external assets, external fonts, CSS grid, vh/vw, rem, fixed/sticky positioning, or `@import`. Do not upload or publish to Sanity. Before declaring completion, report visual checks at 458px, phone, desktop, A4/US Letter, and grayscale.

Required inputs to attach
- Approved transparent PNG reference: Assets/Reference/bd-v-052-ref.jpg
- Matching white-background JPG preview: Assets/Reference/bd-v-052-ref.jpg
- Matching conformance report: Assets/Reference/bd-v-052-ref.json
- Current Claude Design System authoring instructions and closest approved micrographic bundle
- Current Sanity schema/publishing requirements, if available

Complete asset brief
- Asset ID: BD-V-052
- Suggested by: Pablo
- Priority: Supporting
- Type: Diagram
- Historical page/note: 38; clarify the responsibility map and turn it into an educator-guided exercise.
- Placement: Under `### Review: what does self-custody responsibility mean?`, immediately before `#### Key takeaways`.
- Source locator: 1011
- Text–visual link: Synthesizes the module as responsibilities surrounding key control.
- Design brief: Put `control of keys` in the center, surrounded by backup, recovery, receiving, sending, tool choice, acquisition path, privacy, and scam checks. For each, show the protected item and the consequence of failure in very short text.
- Format: Responsibility map; full width.

Use the exact heading and insertion direction in Placement as the target placement. Preserve all listed placements in metadata. Include source-brief revision, reference paths, factual sources, production date, reviewer status, checks, and unresolved judgments in README.md. Set `reviewStatus` to draft or review unless an authorized reviewer has approved it.
```
### [ ] BD-V-053 — Table

```text
You are building one production-ready, accessible My First Bitcoin Bitcoin Diploma visual from a supplied approved transparent PNG reference, its white-background JPG preview, and their JSON conformance report. Read the complete brief below before acting. The asset brief is the source of truth for lesson intent, content, safety, caption, alt text, placement, and localization. The reference image guides composition only. If it conflicts with the brief, the brief wins; report any unresolved factual or design-system gap before implementing.

Rebuild—not trace or embed—the reference as editable HTML, CSS, and inline SVG. Apply the supplied Claude Design System rather than the reference's provisional styling. Keep all essential geometry, arrows, labels, warnings, icons, and data editable. Preserve one clear teaching relationship, a decisive reading order, cultural replaceability, grayscale meaning, narrow-page responsiveness, phone and desktop usability, A4/US-Letter printing, expandable translated text, and future RTL adaptation.

Never invent facts, labels, numbers, providers, URLs, legal claims, safety claims, or brand choices. Preserve every prohibition and qualification in the brief. Do not include real seed phrases, private keys, payable addresses, private learner data, balances, or transactions. Use a verified QR, address, URL, interface, date, or fact only when the brief explicitly authorizes it and it has been checked. Do not imply investment returns, guaranteed outcomes, risk-free self-custody, inevitable adoption, or universal local conclusions. Do not turn a named service into a recommendation.

Produce a bundle in the guide-specific `Assets/diploma/<student-guide|educator-guide|shared>/<asset-id-lowercase>/` folder selected from the placement. Include `micrographic.html`, `micrographic.css`, `meta.json`, `preview.html` in a 458px review frame, `alt-text.md`, `README.md`, and `sanity-asset.json`. Prefix CSS selectors with a unique `.mg-<slug>` root; tag all translatable text with non-nested `data-t` keys; use no JavaScript, external assets, external fonts, CSS grid, vh/vw, rem, fixed/sticky positioning, or `@import`. Do not upload or publish to Sanity. Before declaring completion, report visual checks at 458px, phone, desktop, A4/US Letter, and grayscale.

Required inputs to attach
- Approved transparent PNG reference: Assets/Reference/bd-v-053-ref.jpg
- Matching white-background JPG preview: Assets/Reference/bd-v-053-ref.jpg
- Matching conformance report: Assets/Reference/bd-v-053-ref.json
- Current Claude Design System authoring instructions and closest approved micrographic bundle
- Current Sanity schema/publishing requirements, if available

Complete asset brief
- Asset ID: BD-V-053
- Suggested by: AI
- Priority: Supporting
- Type: Table
- Historical page/note: 38; make the responsibility map usable as a structured learner reference.
- Placement: Under `### Review: what does self-custody responsibility mean?`, immediately before `#### Key takeaways`, as a text-equivalent alternative to `BD-V-052`, not an additional recap.
- Source locator: 1011
- Text–visual link: Connects each task with what must be protected or checked and the consequence of failure.
- Design brief: Use rows for backup, receiving, sending, custody, tool choice, and acquisition. Keep language practical and non-alarmist.
- Format: Responsibility reference table; full width.

Use the exact heading and insertion direction in Placement as the target placement. Preserve all listed placements in metadata. Include source-brief revision, reference paths, factual sources, production date, reviewer status, checks, and unresolved judgments in README.md. Set `reviewStatus` to draft or review unless an authorized reviewer has approved it.
```

## 3.5 Module 4: Bitcoin in Your Community

### [ ] BD-V-055 — Table

```text
You are building one production-ready, accessible My First Bitcoin Bitcoin Diploma visual from a supplied approved transparent PNG reference, its white-background JPG preview, and their JSON conformance report. Read the complete brief below before acting. The asset brief is the source of truth for lesson intent, content, safety, caption, alt text, placement, and localization. The reference image guides composition only. If it conflicts with the brief, the brief wins; report any unresolved factual or design-system gap before implementing.

Rebuild—not trace or embed—the reference as editable HTML, CSS, and inline SVG. Apply the supplied Claude Design System rather than the reference's provisional styling. Keep all essential geometry, arrows, labels, warnings, icons, and data editable. Preserve one clear teaching relationship, a decisive reading order, cultural replaceability, grayscale meaning, narrow-page responsiveness, phone and desktop usability, A4/US-Letter printing, expandable translated text, and future RTL adaptation.

Never invent facts, labels, numbers, providers, URLs, legal claims, safety claims, or brand choices. Preserve every prohibition and qualification in the brief. Do not include real seed phrases, private keys, payable addresses, private learner data, balances, or transactions. Use a verified QR, address, URL, interface, date, or fact only when the brief explicitly authorizes it and it has been checked. Do not imply investment returns, guaranteed outcomes, risk-free self-custody, inevitable adoption, or universal local conclusions. Do not turn a named service into a recommendation.

Produce a bundle in the guide-specific `Assets/diploma/<student-guide|educator-guide|shared>/<asset-id-lowercase>/` folder selected from the placement. Include `micrographic.html`, `micrographic.css`, `meta.json`, `preview.html` in a 458px review frame, `alt-text.md`, `README.md`, and `sanity-asset.json`. Prefix CSS selectors with a unique `.mg-<slug>` root; tag all translatable text with non-nested `data-t` keys; use no JavaScript, external assets, external fonts, CSS grid, vh/vw, rem, fixed/sticky positioning, or `@import`. Do not upload or publish to Sanity. Before declaring completion, report visual checks at 458px, phone, desktop, A4/US Letter, and grayscale.

Required inputs to attach
- Approved transparent PNG reference: Assets/Reference/bd-v-055-ref.jpg
- Matching white-background JPG preview: Assets/Reference/bd-v-055-ref.jpg
- Matching conformance report: Assets/Reference/bd-v-055-ref.json
- Current Claude Design System authoring instructions and closest approved micrographic bundle
- Current Sanity schema/publishing requirements, if available

Complete asset brief
- Asset ID: BD-V-055
- Suggested by: AI
- Priority: Supporting
- Type: Table
- Historical page/note: 38–39; provide a clear editable record of the learner's Module 4 focus.
- Placement: Under `## Module 4: Bitcoin in Your Community`, replace the existing `Local learning choice / Your notes` table visually while retaining an accessible text equivalent.
- Source locator: 1034
- Text–visual link: Gives learners one place to record the module, local problem, tool or scenario, benefit, risk, evidence, and safe next step.
- Design brief: Preserve all seven local-learning-choice prompts and a generous editable notes column. Make it printable and reusable by different educators. Do not pre-fill a local tool, provider, or conclusion.
- Format: Editable Module 4 record table; full width.

Use the exact heading and insertion direction in Placement as the target placement. Preserve all listed placements in metadata. Include source-brief revision, reference paths, factual sources, production date, reviewer status, checks, and unresolved judgments in README.md. Set `reviewStatus` to draft or review unless an authorized reviewer has approved it.
```
### [ ] BD-V-054 — Diagram

```text
You are building one production-ready, accessible My First Bitcoin Bitcoin Diploma visual from a supplied approved transparent PNG reference, its white-background JPG preview, and their JSON conformance report. Read the complete brief below before acting. The asset brief is the source of truth for lesson intent, content, safety, caption, alt text, placement, and localization. The reference image guides composition only. If it conflicts with the brief, the brief wins; report any unresolved factual or design-system gap before implementing.

Rebuild—not trace or embed—the reference as editable HTML, CSS, and inline SVG. Apply the supplied Claude Design System rather than the reference's provisional styling. Keep all essential geometry, arrows, labels, warnings, icons, and data editable. Preserve one clear teaching relationship, a decisive reading order, cultural replaceability, grayscale meaning, narrow-page responsiveness, phone and desktop usability, A4/US-Letter printing, expandable translated text, and future RTL adaptation.

Never invent facts, labels, numbers, providers, URLs, legal claims, safety claims, or brand choices. Preserve every prohibition and qualification in the brief. Do not include real seed phrases, private keys, payable addresses, private learner data, balances, or transactions. Use a verified QR, address, URL, interface, date, or fact only when the brief explicitly authorizes it and it has been checked. Do not imply investment returns, guaranteed outcomes, risk-free self-custody, inevitable adoption, or universal local conclusions. Do not turn a named service into a recommendation.

Produce a bundle in the guide-specific `Assets/diploma/<student-guide|educator-guide|shared>/<asset-id-lowercase>/` folder selected from the placement. Include `micrographic.html`, `micrographic.css`, `meta.json`, `preview.html` in a 458px review frame, `alt-text.md`, `README.md`, and `sanity-asset.json`. Prefix CSS selectors with a unique `.mg-<slug>` root; tag all translatable text with non-nested `data-t` keys; use no JavaScript, external assets, external fonts, CSS grid, vh/vw, rem, fixed/sticky positioning, or `@import`. Do not upload or publish to Sanity. Before declaring completion, report visual checks at 458px, phone, desktop, A4/US Letter, and grayscale.

Required inputs to attach
- Approved transparent PNG reference: Assets/Reference/bd-v-054-ref.jpg
- Matching white-background JPG preview: Assets/Reference/bd-v-054-ref.jpg
- Matching conformance report: Assets/Reference/bd-v-054-ref.json
- Current Claude Design System authoring instructions and closest approved micrographic bundle
- Current Sanity schema/publishing requirements, if available

Complete asset brief
- Asset ID: BD-V-054
- Suggested by: AI
- Priority: Essential
- Type: Diagram
- Historical page/note: 38–39; define MFB versus educator responsibilities in the educator-curated Connect module.
- Placement: Under `### Your local Module 4`, after the four-item list beginning “Connect” and ending “Explain”.
- Source locator: 1057
- Text–visual link: Connects the four learner actions to local purpose, educator support, and safe choice.
- Design brief: Show the four learner actions `Connect → Compare → Practise safely → Explain`. Link shared earlier learning to a local need and realistic alternative, educator-selected safe practice, and a responsible next step. Show the educator and, where needed, a local expert supporting the learner. Keep required competencies and safety boundaries fixed. Detailed educator planning and verification remain in the Educator Guide.
- Format: Four-stage local-learning diagram; full width.

Use the exact heading and insertion direction in Placement as the target placement. Preserve all listed placements in metadata. Include source-brief revision, reference paths, factual sources, production date, reviewer status, checks, and unresolved judgments in README.md. Set `reviewStatus` to draft or review unless an authorized reviewer has approved it.
```
### [ ] BD-V-056 — Diagram

```text
You are building one production-ready, accessible My First Bitcoin Bitcoin Diploma visual from a supplied approved transparent PNG reference, its white-background JPG preview, and their JSON conformance report. Read the complete brief below before acting. The asset brief is the source of truth for lesson intent, content, safety, caption, alt text, placement, and localization. The reference image guides composition only. If it conflicts with the brief, the brief wins; report any unresolved factual or design-system gap before implementing.

Rebuild—not trace or embed—the reference as editable HTML, CSS, and inline SVG. Apply the supplied Claude Design System rather than the reference's provisional styling. Keep all essential geometry, arrows, labels, warnings, icons, and data editable. Preserve one clear teaching relationship, a decisive reading order, cultural replaceability, grayscale meaning, narrow-page responsiveness, phone and desktop usability, A4/US-Letter printing, expandable translated text, and future RTL adaptation.

Never invent facts, labels, numbers, providers, URLs, legal claims, safety claims, or brand choices. Preserve every prohibition and qualification in the brief. Do not include real seed phrases, private keys, payable addresses, private learner data, balances, or transactions. Use a verified QR, address, URL, interface, date, or fact only when the brief explicitly authorizes it and it has been checked. Do not imply investment returns, guaranteed outcomes, risk-free self-custody, inevitable adoption, or universal local conclusions. Do not turn a named service into a recommendation.

Produce a bundle in the guide-specific `Assets/diploma/<student-guide|educator-guide|shared>/<asset-id-lowercase>/` folder selected from the placement. Include `micrographic.html`, `micrographic.css`, `meta.json`, `preview.html` in a 458px review frame, `alt-text.md`, `README.md`, and `sanity-asset.json`. Prefix CSS selectors with a unique `.mg-<slug>` root; tag all translatable text with non-nested `data-t` keys; use no JavaScript, external assets, external fonts, CSS grid, vh/vw, rem, fixed/sticky positioning, or `@import`. Do not upload or publish to Sanity. Before declaring completion, report visual checks at 458px, phone, desktop, A4/US Letter, and grayscale.

Required inputs to attach
- Approved transparent PNG reference: Assets/Reference/bd-v-056-ref.jpg
- Matching white-background JPG preview: Assets/Reference/bd-v-056-ref.jpg
- Matching conformance report: Assets/Reference/bd-v-056-ref.json
- Current Claude Design System authoring instructions and closest approved micrographic bundle
- Current Sanity schema/publishing requirements, if available

Complete asset brief
- Asset ID: BD-V-056
- Suggested by: Pablo
- Priority: Supporting
- Type: Diagram
- Historical page/note: 40; create a clear Presentation → Practice → Production flow for practical workshops and demonstrations.
- Placement: SG: Under `### Practical workshops and demonstrations`, after the definitions of Presentation, Practice, and Production. EG: under `### Use Presentation → Practice → Production`, replace the matching marker after the source text at the listed EG line. See section 3.8 for the exact anchor.
- Source locator: SG: 1072; EG: 861
- Text–visual link: Shows how a safe practical skill develops from educator explanation to guided learner practice and then independent performance or explanation.
- Design brief: Create three connected sections in a clear left-to-right or top-to-bottom sequence: `Presentation` — educator shows the full process and explains purpose, terms, and risks; `Practice` — learner follows a guided process using printed screens, a test environment, or a very small amount; `Production` — learner completes a defined task or explains a decision independently. Add simple safety cues for no funds, test funds, or tiny value, plus an offline alternative at every stage.
- Format: Three-stage PPP flow diagram; full width.

Use the exact heading and insertion direction in Placement as the target placement. Preserve all listed placements in metadata. Include source-brief revision, reference paths, factual sources, production date, reviewer status, checks, and unresolved judgments in README.md. Set `reviewStatus` to draft or review unless an authorized reviewer has approved it.
```
### [ ] BD-V-057 — Table

```text
You are building one production-ready, accessible My First Bitcoin Bitcoin Diploma visual from a supplied approved transparent PNG reference, its white-background JPG preview, and their JSON conformance report. Read the complete brief below before acting. The asset brief is the source of truth for lesson intent, content, safety, caption, alt text, placement, and localization. The reference image guides composition only. If it conflicts with the brief, the brief wins; report any unresolved factual or design-system gap before implementing.

Rebuild—not trace or embed—the reference as editable HTML, CSS, and inline SVG. Apply the supplied Claude Design System rather than the reference's provisional styling. Keep all essential geometry, arrows, labels, warnings, icons, and data editable. Preserve one clear teaching relationship, a decisive reading order, cultural replaceability, grayscale meaning, narrow-page responsiveness, phone and desktop usability, A4/US-Letter printing, expandable translated text, and future RTL adaptation.

Never invent facts, labels, numbers, providers, URLs, legal claims, safety claims, or brand choices. Preserve every prohibition and qualification in the brief. Do not include real seed phrases, private keys, payable addresses, private learner data, balances, or transactions. Use a verified QR, address, URL, interface, date, or fact only when the brief explicitly authorizes it and it has been checked. Do not imply investment returns, guaranteed outcomes, risk-free self-custody, inevitable adoption, or universal local conclusions. Do not turn a named service into a recommendation.

Produce a bundle in the guide-specific `Assets/diploma/<student-guide|educator-guide|shared>/<asset-id-lowercase>/` folder selected from the placement. Include `micrographic.html`, `micrographic.css`, `meta.json`, `preview.html` in a 458px review frame, `alt-text.md`, `README.md`, and `sanity-asset.json`. Prefix CSS selectors with a unique `.mg-<slug>` root; tag all translatable text with non-nested `data-t` keys; use no JavaScript, external assets, external fonts, CSS grid, vh/vw, rem, fixed/sticky positioning, or `@import`. Do not upload or publish to Sanity. Before declaring completion, report visual checks at 458px, phone, desktop, A4/US Letter, and grayscale.

Required inputs to attach
- Approved transparent PNG reference: Assets/Reference/bd-v-057-ref.jpg
- Matching white-background JPG preview: Assets/Reference/bd-v-057-ref.jpg
- Matching conformance report: Assets/Reference/bd-v-057-ref.json
- Current Claude Design System authoring instructions and closest approved micrographic bundle
- Current Sanity schema/publishing requirements, if available

Complete asset brief
- Asset ID: BD-V-057
- Suggested by: Pablo
- Priority: Supporting
- Type: Table
- Historical page/note: 41–42; create a reusable local-tool comparison and place local-tool guidance in the Module 4 Educator Guide.
- Placement: Under `### Local Bitcoin tools and resources`, replace the existing `Area / What to verify` table visually while retaining an accessible text equivalent.
- Source locator: 1103
- Text–visual link: Helps learners see that an interface belongs to a custody, network, and support context.
- Design brief: Preserve purpose, custody, source, code, recovery, privacy, cost, compatibility, support, and law as editable rows with a `What to verify` column. Record the date checked. Do not show an approved-products badge or a globally recommended wallet.
- Format: Local tool evaluation table; full width.

Use the exact heading and insertion direction in Placement as the target placement. Preserve all listed placements in metadata. Include source-brief revision, reference paths, factual sources, production date, reviewer status, checks, and unresolved judgments in README.md. Set `reviewStatus` to draft or review unless an authorized reviewer has approved it.
```
### [ ] BD-V-058 — Table

```text
You are building one production-ready, accessible My First Bitcoin Bitcoin Diploma visual from a supplied approved transparent PNG reference, its white-background JPG preview, and their JSON conformance report. Read the complete brief below before acting. The asset brief is the source of truth for lesson intent, content, safety, caption, alt text, placement, and localization. The reference image guides composition only. If it conflicts with the brief, the brief wins; report any unresolved factual or design-system gap before implementing.

Rebuild—not trace or embed—the reference as editable HTML, CSS, and inline SVG. Apply the supplied Claude Design System rather than the reference's provisional styling. Keep all essential geometry, arrows, labels, warnings, icons, and data editable. Preserve one clear teaching relationship, a decisive reading order, cultural replaceability, grayscale meaning, narrow-page responsiveness, phone and desktop usability, A4/US-Letter printing, expandable translated text, and future RTL adaptation.

Never invent facts, labels, numbers, providers, URLs, legal claims, safety claims, or brand choices. Preserve every prohibition and qualification in the brief. Do not include real seed phrases, private keys, payable addresses, private learner data, balances, or transactions. Use a verified QR, address, URL, interface, date, or fact only when the brief explicitly authorizes it and it has been checked. Do not imply investment returns, guaranteed outcomes, risk-free self-custody, inevitable adoption, or universal local conclusions. Do not turn a named service into a recommendation.

Produce a bundle in the guide-specific `Assets/diploma/<student-guide|educator-guide|shared>/<asset-id-lowercase>/` folder selected from the placement. Include `micrographic.html`, `micrographic.css`, `meta.json`, `preview.html` in a 458px review frame, `alt-text.md`, `README.md`, and `sanity-asset.json`. Prefix CSS selectors with a unique `.mg-<slug>` root; tag all translatable text with non-nested `data-t` keys; use no JavaScript, external assets, external fonts, CSS grid, vh/vw, rem, fixed/sticky positioning, or `@import`. Do not upload or publish to Sanity. Before declaring completion, report visual checks at 458px, phone, desktop, A4/US Letter, and grayscale.

Required inputs to attach
- Approved transparent PNG reference: Assets/Reference/bd-v-058-ref.jpg
- Matching white-background JPG preview: Assets/Reference/bd-v-058-ref.jpg
- Matching conformance report: Assets/Reference/bd-v-058-ref.json
- Current Claude Design System authoring instructions and closest approved micrographic bundle
- Current Sanity schema/publishing requirements, if available

Complete asset brief
- Asset ID: BD-V-058
- Suggested by: AI
- Priority: Supporting
- Type: Table
- Historical page/note: 41–42; provide a structured, reusable record for documenting a locally used Bitcoin tool.
- Placement: Under `### Local Bitcoin tools and resources`, replace the existing `Local tool record` table visually while retaining an accessible text equivalent.
- Source locator: 1120
- Text–visual link: Helps learners record what was checked about a tool without treating it as a global recommendation.
- Design brief: Preserve the rows for tool and version, date checked, custody model, main use, benefit, risk, recovery method, and alternative. Keep all fields editable and date-stamped. Do not use an endorsement badge or provider ranking.
- Format: Editable local-tool record table; full width.

Use the exact heading and insertion direction in Placement as the target placement. Preserve all listed placements in metadata. Include source-brief revision, reference paths, factual sources, production date, reviewer status, checks, and unresolved judgments in README.md. Set `reviewStatus` to draft or review unless an authorized reviewer has approved it.
```
### [ ] BD-V-080 — Diagram

```text
You are building one production-ready, accessible My First Bitcoin Bitcoin Diploma visual from a supplied approved transparent PNG reference, its white-background JPG preview, and their JSON conformance report. Read the complete brief below before acting. The asset brief is the source of truth for lesson intent, content, safety, caption, alt text, placement, and localization. The reference image guides composition only. If it conflicts with the brief, the brief wins; report any unresolved factual or design-system gap before implementing.

Rebuild—not trace or embed—the reference as editable HTML, CSS, and inline SVG. Apply the supplied Claude Design System rather than the reference's provisional styling. Keep all essential geometry, arrows, labels, warnings, icons, and data editable. Preserve one clear teaching relationship, a decisive reading order, cultural replaceability, grayscale meaning, narrow-page responsiveness, phone and desktop usability, A4/US-Letter printing, expandable translated text, and future RTL adaptation.

Never invent facts, labels, numbers, providers, URLs, legal claims, safety claims, or brand choices. Preserve every prohibition and qualification in the brief. Do not include real seed phrases, private keys, payable addresses, private learner data, balances, or transactions. Use a verified QR, address, URL, interface, date, or fact only when the brief explicitly authorizes it and it has been checked. Do not imply investment returns, guaranteed outcomes, risk-free self-custody, inevitable adoption, or universal local conclusions. Do not turn a named service into a recommendation.

Produce a bundle in the guide-specific `Assets/diploma/<student-guide|educator-guide|shared>/<asset-id-lowercase>/` folder selected from the placement. Include `micrographic.html`, `micrographic.css`, `meta.json`, `preview.html` in a 458px review frame, `alt-text.md`, `README.md`, and `sanity-asset.json`. Prefix CSS selectors with a unique `.mg-<slug>` root; tag all translatable text with non-nested `data-t` keys; use no JavaScript, external assets, external fonts, CSS grid, vh/vw, rem, fixed/sticky positioning, or `@import`. Do not upload or publish to Sanity. Before declaring completion, report visual checks at 458px, phone, desktop, A4/US Letter, and grayscale.

Required inputs to attach
- Approved transparent PNG reference: Assets/Reference/bd-v-080-ref.jpg
- Matching white-background JPG preview: Assets/Reference/bd-v-080-ref.jpg
- Matching conformance report: Assets/Reference/bd-v-080-ref.json
- Current Claude Design System authoring instructions and closest approved micrographic bundle
- Current Sanity schema/publishing requirements, if available

Complete asset brief
- Asset ID: BD-V-080
- Suggested by: User
- Priority: Essential
- Type: Diagram
- Historical page/note: —; Show a Lightning address such as `donate@myfirstbitcoin.org` beside its matching QR code.
- Placement: Under `### Lightning payments where locally appropriate` in the [Student Guide](../publish/mfb-bd-26.10/mfb-bd-sg-26.10.md#lightning-payments-where-locally-appropriate), immediately after the paragraph beginning “A **Lightning address** is a human-readable identifier” and before “For a guided payment”.
- Source locator: 1148
- Text–visual link: Connects an email-like Lightning address with its scannable payment destination, while distinguishing it from an email account, an on-chain address, and a specific Lightning invoice.
- Design brief: Show the full Lightning address as readable, selectable text beside a QR code for the same destination, joined by `Same Lightning address, two formats`. Use [BLANK] for the Lightning address until My First Bitcoin supplies and approves an active, controlled destination; do not publish a working QR until TODO AST-003 is resolved. Generate a wallet-compatible Lightning QR for the confirmed address, not a `mailto:` link, website link, on-chain address, or fixed invoice. Label `Lightning address` and `SAMPLE — DO NOT PAY`. Do not preset an amount or turn this teaching illustration into a donation call to action; the optional support panel is `BD-V-074`. Verify that scanning the final print and screen exports in a compatible Lightning wallet resolves to the confirmed recipient and allows the payment details to be reviewed before approval. Keep the QR unobstructed with a clear border. Caption: `This looks like an email address, but it is used to request a Lightning payment. Check the recipient and payment details before paying.` Alt text: `A confirmed My First Bitcoin Lightning address shown as readable text beside a QR code for the same payment destination, labelled Lightning address and SAMPLE — DO NOT PAY.` Replace the generic address description in the final alt text with the confirmed address. Save the editable master as `Assets/Briefs/bd-v-080-brief.md`.
- Format: Side-by-side Lightning-address-and-QR diagram with editable labels; half width.

Use the exact heading and insertion direction in Placement as the target placement. Preserve all listed placements in metadata. Include source-brief revision, reference paths, factual sources, production date, reviewer status, checks, and unresolved judgments in README.md. Set `reviewStatus` to draft or review unless an authorized reviewer has approved it.
```
### [ ] BD-V-059 — Diagram

```text
You are building one production-ready, accessible My First Bitcoin Bitcoin Diploma visual from a supplied approved transparent PNG reference, its white-background JPG preview, and their JSON conformance report. Read the complete brief below before acting. The asset brief is the source of truth for lesson intent, content, safety, caption, alt text, placement, and localization. The reference image guides composition only. If it conflicts with the brief, the brief wins; report any unresolved factual or design-system gap before implementing.

Rebuild—not trace or embed—the reference as editable HTML, CSS, and inline SVG. Apply the supplied Claude Design System rather than the reference's provisional styling. Keep all essential geometry, arrows, labels, warnings, icons, and data editable. Preserve one clear teaching relationship, a decisive reading order, cultural replaceability, grayscale meaning, narrow-page responsiveness, phone and desktop usability, A4/US-Letter printing, expandable translated text, and future RTL adaptation.

Never invent facts, labels, numbers, providers, URLs, legal claims, safety claims, or brand choices. Preserve every prohibition and qualification in the brief. Do not include real seed phrases, private keys, payable addresses, private learner data, balances, or transactions. Use a verified QR, address, URL, interface, date, or fact only when the brief explicitly authorizes it and it has been checked. Do not imply investment returns, guaranteed outcomes, risk-free self-custody, inevitable adoption, or universal local conclusions. Do not turn a named service into a recommendation.

Produce a bundle in the guide-specific `Assets/diploma/<student-guide|educator-guide|shared>/<asset-id-lowercase>/` folder selected from the placement. Include `micrographic.html`, `micrographic.css`, `meta.json`, `preview.html` in a 458px review frame, `alt-text.md`, `README.md`, and `sanity-asset.json`. Prefix CSS selectors with a unique `.mg-<slug>` root; tag all translatable text with non-nested `data-t` keys; use no JavaScript, external assets, external fonts, CSS grid, vh/vw, rem, fixed/sticky positioning, or `@import`. Do not upload or publish to Sanity. Before declaring completion, report visual checks at 458px, phone, desktop, A4/US Letter, and grayscale.

Required inputs to attach
- Approved transparent PNG reference: Assets/Reference/bd-v-059-ref.jpg
- Matching white-background JPG preview: Assets/Reference/bd-v-059-ref.jpg
- Matching conformance report: Assets/Reference/bd-v-059-ref.json
- Current Claude Design System authoring instructions and closest approved micrographic bundle
- Current Sanity schema/publishing requirements, if available

Complete asset brief
- Asset ID: BD-V-059
- Suggested by: AI
- Priority: Supporting
- Type: Diagram
- Historical page/note: 36 and 43; explain Lightning trade-offs and provide a separate Lightning example page.
- Placement: SG: Under `### Lightning payments where locally appropriate`, after the six guided-payment steps. EG: under `### Lightning module checklist`, replace the matching marker after the source text at the listed EG line. See section 3.8 for the exact anchor.
- Source locator: SG: 1157; EG: 2613
- Text–visual link: Makes a Lightning payment sequence clear while keeping custody and failure risk visible.
- Design brief: Show receiver creates request; sender scans or copies; sender verifies recipient, amount, unit, expiry, and fee; sender approves; payment routes; both wallets report success or failure. Add custody labels on both wallets and a branch for failure. Use generic, nonfunctional screens.
- Format: Lightning payment sequence; full width.

Use the exact heading and insertion direction in Placement as the target placement. Preserve all listed placements in metadata. Include source-brief revision, reference paths, factual sources, production date, reviewer status, checks, and unresolved judgments in README.md. Set `reviewStatus` to draft or review unless an authorized reviewer has approved it.
```
### [ ] BD-V-060 — Diagram

```text
You are building one production-ready, accessible My First Bitcoin Bitcoin Diploma visual from a supplied approved transparent PNG reference, its white-background JPG preview, and their JSON conformance report. Read the complete brief below before acting. The asset brief is the source of truth for lesson intent, content, safety, caption, alt text, placement, and localization. The reference image guides composition only. If it conflicts with the brief, the brief wins; report any unresolved factual or design-system gap before implementing.

Rebuild—not trace or embed—the reference as editable HTML, CSS, and inline SVG. Apply the supplied Claude Design System rather than the reference's provisional styling. Keep all essential geometry, arrows, labels, warnings, icons, and data editable. Preserve one clear teaching relationship, a decisive reading order, cultural replaceability, grayscale meaning, narrow-page responsiveness, phone and desktop usability, A4/US-Letter printing, expandable translated text, and future RTL adaptation.

Never invent facts, labels, numbers, providers, URLs, legal claims, safety claims, or brand choices. Preserve every prohibition and qualification in the brief. Do not include real seed phrases, private keys, payable addresses, private learner data, balances, or transactions. Use a verified QR, address, URL, interface, date, or fact only when the brief explicitly authorizes it and it has been checked. Do not imply investment returns, guaranteed outcomes, risk-free self-custody, inevitable adoption, or universal local conclusions. Do not turn a named service into a recommendation.

Produce a bundle in the guide-specific `Assets/diploma/<student-guide|educator-guide|shared>/<asset-id-lowercase>/` folder selected from the placement. Include `micrographic.html`, `micrographic.css`, `meta.json`, `preview.html` in a 458px review frame, `alt-text.md`, `README.md`, and `sanity-asset.json`. Prefix CSS selectors with a unique `.mg-<slug>` root; tag all translatable text with non-nested `data-t` keys; use no JavaScript, external assets, external fonts, CSS grid, vh/vw, rem, fixed/sticky positioning, or `@import`. Do not upload or publish to Sanity. Before declaring completion, report visual checks at 458px, phone, desktop, A4/US Letter, and grayscale.

Required inputs to attach
- Approved transparent PNG reference: Assets/Reference/bd-v-060-ref.jpg
- Matching white-background JPG preview: Assets/Reference/bd-v-060-ref.jpg
- Matching conformance report: Assets/Reference/bd-v-060-ref.json
- Current Claude Design System authoring instructions and closest approved micrographic bundle
- Current Sanity schema/publishing requirements, if available

Complete asset brief
- Asset ID: BD-V-060
- Suggested by: Pablo
- Priority: Supporting
- Type: Diagram
- Historical page/note: 43; add seven simple icons for the daily uses of Bitcoin.
- Placement: Under `### Daily-life Bitcoin use`, after the seven use descriptions and before the three evaluation questions.
- Source locator: 1177
- Text–visual link: Makes the seven distinct ways Bitcoin may be used in daily life quick to identify without suggesting that every learner should use it in every way.
- Design brief: Create seven equally weighted illustrative icons, each clearly labelled: earning, saving, receiving, sending, spending, pricing and accounting, and donating. Arrange them in a clear row, grid, or gentle sequence; do not make the icons form a compulsory circular process. Use familiar, culturally adaptable symbols and no provider branding.
- Format: Seven-icon daily-use illustration; full width.

Use the exact heading and insertion direction in Placement as the target placement. Preserve all listed placements in metadata. Include source-brief revision, reference paths, factual sources, production date, reviewer status, checks, and unresolved judgments in README.md. Set `reviewStatus` to draft or review unless an authorized reviewer has approved it.
```
### [ ] BD-V-061 — Image

```text
You are building one production-ready, accessible My First Bitcoin Bitcoin Diploma visual from a supplied approved transparent PNG reference, its white-background JPG preview, and their JSON conformance report. Read the complete brief below before acting. The asset brief is the source of truth for lesson intent, content, safety, caption, alt text, placement, and localization. The reference image guides composition only. If it conflicts with the brief, the brief wins; report any unresolved factual or design-system gap before implementing.

Rebuild—not trace or embed—the reference as editable HTML, CSS, and inline SVG. Apply the supplied Claude Design System rather than the reference's provisional styling. Keep all essential geometry, arrows, labels, warnings, icons, and data editable. Preserve one clear teaching relationship, a decisive reading order, cultural replaceability, grayscale meaning, narrow-page responsiveness, phone and desktop usability, A4/US-Letter printing, expandable translated text, and future RTL adaptation.

Never invent facts, labels, numbers, providers, URLs, legal claims, safety claims, or brand choices. Preserve every prohibition and qualification in the brief. Do not include real seed phrases, private keys, payable addresses, private learner data, balances, or transactions. Use a verified QR, address, URL, interface, date, or fact only when the brief explicitly authorizes it and it has been checked. Do not imply investment returns, guaranteed outcomes, risk-free self-custody, inevitable adoption, or universal local conclusions. Do not turn a named service into a recommendation.

Produce a bundle in the guide-specific `Assets/diploma/<student-guide|educator-guide|shared>/<asset-id-lowercase>/` folder selected from the placement. Include `micrographic.html`, `micrographic.css`, `meta.json`, `preview.html` in a 458px review frame, `alt-text.md`, `README.md`, and `sanity-asset.json`. Prefix CSS selectors with a unique `.mg-<slug>` root; tag all translatable text with non-nested `data-t` keys; use no JavaScript, external assets, external fonts, CSS grid, vh/vw, rem, fixed/sticky positioning, or `@import`. Do not upload or publish to Sanity. Before declaring completion, report visual checks at 458px, phone, desktop, A4/US Letter, and grayscale.

Required inputs to attach
- Approved transparent PNG reference: Assets/Reference/bd-v-061-ref.jpg
- Matching white-background JPG preview: Assets/Reference/bd-v-061-ref.jpg
- Matching conformance report: Assets/Reference/bd-v-061-ref.json
- Current Claude Design System authoring instructions and closest approved micrographic bundle
- Current Sanity schema/publishing requirements, if available

Complete asset brief
- Asset ID: BD-V-061
- Suggested by: AI
- Priority: Supporting
- Type: Image
- Historical page/note: 43–44; use separate payment examples and preserve the locally grounded scenario approach.
- Placement: Under `### Local spending and receiving scenarios`, before Scenario 1.
- Source locator: 1191
- Text–visual link: Gives all local scenarios one reusable visual grammar so educators can substitute local actors and goods.
- Design brief: Create a four-frame template: need and actors; payment request and chosen path; verification and settlement; record, refund, custody, or conversion. Include editable slots for small purchase, work payment, family transfer, refund, or donation. The template must work with simulation or tiny value.
- Format: Reusable scenario storyboard; full width.

Use the exact heading and insertion direction in Placement as the target placement. Preserve all listed placements in metadata. Include source-brief revision, reference paths, factual sources, production date, reviewer status, checks, and unresolved judgments in README.md. Set `reviewStatus` to draft or review unless an authorized reviewer has approved it.
```
### [ ] BD-V-062 — Diagram

```text
You are building one production-ready, accessible My First Bitcoin Bitcoin Diploma visual from a supplied approved transparent PNG reference, its white-background JPG preview, and their JSON conformance report. Read the complete brief below before acting. The asset brief is the source of truth for lesson intent, content, safety, caption, alt text, placement, and localization. The reference image guides composition only. If it conflicts with the brief, the brief wins; report any unresolved factual or design-system gap before implementing.

Rebuild—not trace or embed—the reference as editable HTML, CSS, and inline SVG. Apply the supplied Claude Design System rather than the reference's provisional styling. Keep all essential geometry, arrows, labels, warnings, icons, and data editable. Preserve one clear teaching relationship, a decisive reading order, cultural replaceability, grayscale meaning, narrow-page responsiveness, phone and desktop usability, A4/US-Letter printing, expandable translated text, and future RTL adaptation.

Never invent facts, labels, numbers, providers, URLs, legal claims, safety claims, or brand choices. Preserve every prohibition and qualification in the brief. Do not include real seed phrases, private keys, payable addresses, private learner data, balances, or transactions. Use a verified QR, address, URL, interface, date, or fact only when the brief explicitly authorizes it and it has been checked. Do not imply investment returns, guaranteed outcomes, risk-free self-custody, inevitable adoption, or universal local conclusions. Do not turn a named service into a recommendation.

Produce a bundle in the guide-specific `Assets/diploma/<student-guide|educator-guide|shared>/<asset-id-lowercase>/` folder selected from the placement. Include `micrographic.html`, `micrographic.css`, `meta.json`, `preview.html` in a 458px review frame, `alt-text.md`, `README.md`, and `sanity-asset.json`. Prefix CSS selectors with a unique `.mg-<slug>` root; tag all translatable text with non-nested `data-t` keys; use no JavaScript, external assets, external fonts, CSS grid, vh/vw, rem, fixed/sticky positioning, or `@import`. Do not upload or publish to Sanity. Before declaring completion, report visual checks at 458px, phone, desktop, A4/US Letter, and grayscale.

Required inputs to attach
- Approved transparent PNG reference: Assets/Reference/bd-v-062-ref.jpg
- Matching white-background JPG preview: Assets/Reference/bd-v-062-ref.jpg
- Matching conformance report: Assets/Reference/bd-v-062-ref.json
- Current Claude Design System authoring instructions and closest approved micrographic bundle
- Current Sanity schema/publishing requirements, if available

Complete asset brief
- Asset ID: BD-V-062
- Suggested by: AI
- Priority: Essential
- Type: Diagram
- Historical page/note: 45; preserve but simplify the strongly approved on/off-ramp pathway comparison.
- Placement: SG: Under `### Local on-ramp and off-ramp pathways`, after the definition and pathway list and before the pathway comparison table. EG: under `### Module option F: on-ramp, off-ramp, KYC, and no-KYC comparison`, replace the matching marker after the source text at the listed EG line. See section 3.8 for the exact anchor.
- Source locator: SG: 1257; EG: 2749
- Text–visual link: Forces comparison of the complete route rather than only the advertised first fee.
- Design brief: Show local money, work, goods, or services entering through possible routes; custody and identity checkpoints; on-chain or Lightning transfer; self-custody or service balance; and final use, holding, or conversion. Label spread, fees, time, reversal, withdrawal, counterparty, privacy, support, and law along the route.
- Format: End-to-end pathway map; full width.

Use the exact heading and insertion direction in Placement as the target placement. Preserve all listed placements in metadata. Include source-brief revision, reference paths, factual sources, production date, reviewer status, checks, and unresolved judgments in README.md. Set `reviewStatus` to draft or review unless an authorized reviewer has approved it.
```
### [ ] BD-V-063 — Table

```text
You are building one production-ready, accessible My First Bitcoin Bitcoin Diploma visual from a supplied approved transparent PNG reference, its white-background JPG preview, and their JSON conformance report. Read the complete brief below before acting. The asset brief is the source of truth for lesson intent, content, safety, caption, alt text, placement, and localization. The reference image guides composition only. If it conflicts with the brief, the brief wins; report any unresolved factual or design-system gap before implementing.

Rebuild—not trace or embed—the reference as editable HTML, CSS, and inline SVG. Apply the supplied Claude Design System rather than the reference's provisional styling. Keep all essential geometry, arrows, labels, warnings, icons, and data editable. Preserve one clear teaching relationship, a decisive reading order, cultural replaceability, grayscale meaning, narrow-page responsiveness, phone and desktop usability, A4/US-Letter printing, expandable translated text, and future RTL adaptation.

Never invent facts, labels, numbers, providers, URLs, legal claims, safety claims, or brand choices. Preserve every prohibition and qualification in the brief. Do not include real seed phrases, private keys, payable addresses, private learner data, balances, or transactions. Use a verified QR, address, URL, interface, date, or fact only when the brief explicitly authorizes it and it has been checked. Do not imply investment returns, guaranteed outcomes, risk-free self-custody, inevitable adoption, or universal local conclusions. Do not turn a named service into a recommendation.

Produce a bundle in the guide-specific `Assets/diploma/<student-guide|educator-guide|shared>/<asset-id-lowercase>/` folder selected from the placement. Include `micrographic.html`, `micrographic.css`, `meta.json`, `preview.html` in a 458px review frame, `alt-text.md`, `README.md`, and `sanity-asset.json`. Prefix CSS selectors with a unique `.mg-<slug>` root; tag all translatable text with non-nested `data-t` keys; use no JavaScript, external assets, external fonts, CSS grid, vh/vw, rem, fixed/sticky positioning, or `@import`. Do not upload or publish to Sanity. Before declaring completion, report visual checks at 458px, phone, desktop, A4/US Letter, and grayscale.

Required inputs to attach
- Approved transparent PNG reference: Assets/Reference/bd-v-063-ref.jpg
- Matching white-background JPG preview: Assets/Reference/bd-v-063-ref.jpg
- Matching conformance report: Assets/Reference/bd-v-063-ref.json
- Current Claude Design System authoring instructions and closest approved micrographic bundle
- Current Sanity schema/publishing requirements, if available

Complete asset brief
- Asset ID: BD-V-063
- Suggested by: AI
- Priority: Supporting
- Type: Table
- Historical page/note: 45; provide a local pathway-comparison table that considers the complete route.
- Placement: Under `### Local on-ramp and off-ramp pathways`, replace the existing pathway comparison table visually while retaining an accessible text equivalent.
- Source locator: 1259
- Text–visual link: Helps learners compare received value, time, custody, privacy, reversal risk, and failure points across local options.
- Design brief: Preserve the editable rows for local option A, local option B, and an existing non-Bitcoin option, plus all comparison columns. Do not pre-fill services, rates, or legal claims.
- Format: Editable pathway-comparison table; full width.

Use the exact heading and insertion direction in Placement as the target placement. Preserve all listed placements in metadata. Include source-brief revision, reference paths, factual sources, production date, reviewer status, checks, and unresolved judgments in README.md. Set `reviewStatus` to draft or review unless an authorized reviewer has approved it.
```
### [ ] BD-V-064 — Table

```text
You are building one production-ready, accessible My First Bitcoin Bitcoin Diploma visual from a supplied approved transparent PNG reference, its white-background JPG preview, and their JSON conformance report. Read the complete brief below before acting. The asset brief is the source of truth for lesson intent, content, safety, caption, alt text, placement, and localization. The reference image guides composition only. If it conflicts with the brief, the brief wins; report any unresolved factual or design-system gap before implementing.

Rebuild—not trace or embed—the reference as editable HTML, CSS, and inline SVG. Apply the supplied Claude Design System rather than the reference's provisional styling. Keep all essential geometry, arrows, labels, warnings, icons, and data editable. Preserve one clear teaching relationship, a decisive reading order, cultural replaceability, grayscale meaning, narrow-page responsiveness, phone and desktop usability, A4/US-Letter printing, expandable translated text, and future RTL adaptation.

Never invent facts, labels, numbers, providers, URLs, legal claims, safety claims, or brand choices. Preserve every prohibition and qualification in the brief. Do not include real seed phrases, private keys, payable addresses, private learner data, balances, or transactions. Use a verified QR, address, URL, interface, date, or fact only when the brief explicitly authorizes it and it has been checked. Do not imply investment returns, guaranteed outcomes, risk-free self-custody, inevitable adoption, or universal local conclusions. Do not turn a named service into a recommendation.

Produce a bundle in the guide-specific `Assets/diploma/<student-guide|educator-guide|shared>/<asset-id-lowercase>/` folder selected from the placement. Include `micrographic.html`, `micrographic.css`, `meta.json`, `preview.html` in a 458px review frame, `alt-text.md`, `README.md`, and `sanity-asset.json`. Prefix CSS selectors with a unique `.mg-<slug>` root; tag all translatable text with non-nested `data-t` keys; use no JavaScript, external assets, external fonts, CSS grid, vh/vw, rem, fixed/sticky positioning, or `@import`. Do not upload or publish to Sanity. Before declaring completion, report visual checks at 458px, phone, desktop, A4/US Letter, and grayscale.

Required inputs to attach
- Approved transparent PNG reference: Assets/Reference/bd-v-064-ref.jpg
- Matching white-background JPG preview: Assets/Reference/bd-v-064-ref.jpg
- Matching conformance report: Assets/Reference/bd-v-064-ref.json
- Current Claude Design System authoring instructions and closest approved micrographic bundle
- Current Sanity schema/publishing requirements, if available

Complete asset brief
- Asset ID: BD-V-064
- Suggested by: AI
- Priority: Supporting
- Type: Table
- Historical page/note: 46; keep KYC/no-KYC trade-offs only where locally appropriate and fact-checked.
- Placement: Under `### KYC and no-KYC trade-offs where locally appropriate`, replace the existing `Question / KYC path / No-KYC path` table visually while retaining an accessible text equivalent.
- Source locator: 1281
- Text–visual link: Frames KYC and no-KYC as different bundles of benefits and risks, not as good versus bad.
- Design brief: Preserve all eight questions in the existing comparison table: identity data collected; storage and retention; on-chain linkability; fraud protection; counterparty risk; limits and fees; local law; dispute handling. Leave the two answer columns editable for a dated local comparison. Include `local law varies; verify current information`. Do not imply evasion or guaranteed privacy.
- Format: Balanced trade-off comparison; full width.

Use the exact heading and insertion direction in Placement as the target placement. Preserve all listed placements in metadata. Include source-brief revision, reference paths, factual sources, production date, reviewer status, checks, and unresolved judgments in README.md. Set `reviewStatus` to draft or review unless an authorized reviewer has approved it.
```
### [ ] BD-V-065 — Diagram

```text
You are building one production-ready, accessible My First Bitcoin Bitcoin Diploma visual from a supplied approved transparent PNG reference, its white-background JPG preview, and their JSON conformance report. Read the complete brief below before acting. The asset brief is the source of truth for lesson intent, content, safety, caption, alt text, placement, and localization. The reference image guides composition only. If it conflicts with the brief, the brief wins; report any unresolved factual or design-system gap before implementing.

Rebuild—not trace or embed—the reference as editable HTML, CSS, and inline SVG. Apply the supplied Claude Design System rather than the reference's provisional styling. Keep all essential geometry, arrows, labels, warnings, icons, and data editable. Preserve one clear teaching relationship, a decisive reading order, cultural replaceability, grayscale meaning, narrow-page responsiveness, phone and desktop usability, A4/US-Letter printing, expandable translated text, and future RTL adaptation.

Never invent facts, labels, numbers, providers, URLs, legal claims, safety claims, or brand choices. Preserve every prohibition and qualification in the brief. Do not include real seed phrases, private keys, payable addresses, private learner data, balances, or transactions. Use a verified QR, address, URL, interface, date, or fact only when the brief explicitly authorizes it and it has been checked. Do not imply investment returns, guaranteed outcomes, risk-free self-custody, inevitable adoption, or universal local conclusions. Do not turn a named service into a recommendation.

Produce a bundle in the guide-specific `Assets/diploma/<student-guide|educator-guide|shared>/<asset-id-lowercase>/` folder selected from the placement. Include `micrographic.html`, `micrographic.css`, `meta.json`, `preview.html` in a 458px review frame, `alt-text.md`, `README.md`, and `sanity-asset.json`. Prefix CSS selectors with a unique `.mg-<slug>` root; tag all translatable text with non-nested `data-t` keys; use no JavaScript, external assets, external fonts, CSS grid, vh/vw, rem, fixed/sticky positioning, or `@import`. Do not upload or publish to Sanity. Before declaring completion, report visual checks at 458px, phone, desktop, A4/US Letter, and grayscale.

Required inputs to attach
- Approved transparent PNG reference: Assets/Reference/bd-v-065-ref.jpg
- Matching white-background JPG preview: Assets/Reference/bd-v-065-ref.jpg
- Matching conformance report: Assets/Reference/bd-v-065-ref.json
- Current Claude Design System authoring instructions and closest approved micrographic bundle
- Current Sanity schema/publishing requirements, if available

Complete asset brief
- Asset ID: BD-V-065
- Suggested by: AI
- Priority: Essential
- Type: Diagram
- Historical page/note: 46–47; preserve the conclusion and add a stronger balanced circular-economy graphic.
- Placement: SG: Under `### Circular economies`, after the seven mapping questions. EG: under `### Module option G: circular economy and local resource map`, replace the matching marker after the source text at the listed EG line. See section 3.8 for the exact anchor.
- Source locator: SG: 1310; EG: 2775
- Text–visual link: Shows value circulating among participants and reveals where the loop depends on outside services or support.
- Design brief: Map workers, customers, merchants, suppliers, educators or support, and exchange or on/off-ramp points. Use separate arrows for value, goods or services, and support. Mark custody, volatility, connectivity, and conversion dependencies. Include broken-loop examples such as immediate conversion or one organizer processing everything.
- Format: Editable local network map; full width.

Use the exact heading and insertion direction in Placement as the target placement. Preserve all listed placements in metadata. Include source-brief revision, reference paths, factual sources, production date, reviewer status, checks, and unresolved judgments in README.md. Set `reviewStatus` to draft or review unless an authorized reviewer has approved it.
```
### [ ] BD-V-066 — Diagram

```text
You are building one production-ready, accessible My First Bitcoin Bitcoin Diploma visual from a supplied approved transparent PNG reference, its white-background JPG preview, and their JSON conformance report. Read the complete brief below before acting. The asset brief is the source of truth for lesson intent, content, safety, caption, alt text, placement, and localization. The reference image guides composition only. If it conflicts with the brief, the brief wins; report any unresolved factual or design-system gap before implementing.

Rebuild—not trace or embed—the reference as editable HTML, CSS, and inline SVG. Apply the supplied Claude Design System rather than the reference's provisional styling. Keep all essential geometry, arrows, labels, warnings, icons, and data editable. Preserve one clear teaching relationship, a decisive reading order, cultural replaceability, grayscale meaning, narrow-page responsiveness, phone and desktop usability, A4/US-Letter printing, expandable translated text, and future RTL adaptation.

Never invent facts, labels, numbers, providers, URLs, legal claims, safety claims, or brand choices. Preserve every prohibition and qualification in the brief. Do not include real seed phrases, private keys, payable addresses, private learner data, balances, or transactions. Use a verified QR, address, URL, interface, date, or fact only when the brief explicitly authorizes it and it has been checked. Do not imply investment returns, guaranteed outcomes, risk-free self-custody, inevitable adoption, or universal local conclusions. Do not turn a named service into a recommendation.

Produce a bundle in the guide-specific `Assets/diploma/<student-guide|educator-guide|shared>/<asset-id-lowercase>/` folder selected from the placement. Include `micrographic.html`, `micrographic.css`, `meta.json`, `preview.html` in a 458px review frame, `alt-text.md`, `README.md`, and `sanity-asset.json`. Prefix CSS selectors with a unique `.mg-<slug>` root; tag all translatable text with non-nested `data-t` keys; use no JavaScript, external assets, external fonts, CSS grid, vh/vw, rem, fixed/sticky positioning, or `@import`. Do not upload or publish to Sanity. Before declaring completion, report visual checks at 458px, phone, desktop, A4/US Letter, and grayscale.

Required inputs to attach
- Approved transparent PNG reference: Assets/Reference/bd-v-066-ref.jpg
- Matching white-background JPG preview: Assets/Reference/bd-v-066-ref.jpg
- Matching conformance report: Assets/Reference/bd-v-066-ref.json
- Current Claude Design System authoring instructions and closest approved micrographic bundle
- Current Sanity schema/publishing requirements, if available

Complete asset brief
- Asset ID: BD-V-066
- Suggested by: Pablo
- Priority: Supporting
- Type: Diagram
- Historical page/note: 40 and 48; turn merchant payment flow into a local case study and connect it to jurisdiction.
- Placement: SG: Under `### Merchant or community use cases`, after the merchant decision checklist and before the community-use examples. EG: under `### Module option D: merchant payment and refund flow`, replace the matching marker after the source text at the listed EG line. See section 3.8 for the exact anchor.
- Source locator: SG: 1331; EG: 2702
- Text–visual link: Shows that accepting Bitcoin is an operational process, not just displaying a QR code.
- Design brief: Trace pricing → payment request → customer verification → merchant confirmation → receipt or record → custody or conversion → refund or exception. Add staff, accounting, tax, device security, offline failure, and support callouts. Use local-law placeholders, not assertions.
- Format: Merchant payment operations flow; full width.

Use the exact heading and insertion direction in Placement as the target placement. Preserve all listed placements in metadata. Include source-brief revision, reference paths, factual sources, production date, reviewer status, checks, and unresolved judgments in README.md. Set `reviewStatus` to draft or review unless an authorized reviewer has approved it.
```
### [ ] BD-V-067 — Diagram

```text
You are building one production-ready, accessible My First Bitcoin Bitcoin Diploma visual from a supplied approved transparent PNG reference, its white-background JPG preview, and their JSON conformance report. Read the complete brief below before acting. The asset brief is the source of truth for lesson intent, content, safety, caption, alt text, placement, and localization. The reference image guides composition only. If it conflicts with the brief, the brief wins; report any unresolved factual or design-system gap before implementing.

Rebuild—not trace or embed—the reference as editable HTML, CSS, and inline SVG. Apply the supplied Claude Design System rather than the reference's provisional styling. Keep all essential geometry, arrows, labels, warnings, icons, and data editable. Preserve one clear teaching relationship, a decisive reading order, cultural replaceability, grayscale meaning, narrow-page responsiveness, phone and desktop usability, A4/US-Letter printing, expandable translated text, and future RTL adaptation.

Never invent facts, labels, numbers, providers, URLs, legal claims, safety claims, or brand choices. Preserve every prohibition and qualification in the brief. Do not include real seed phrases, private keys, payable addresses, private learner data, balances, or transactions. Use a verified QR, address, URL, interface, date, or fact only when the brief explicitly authorizes it and it has been checked. Do not imply investment returns, guaranteed outcomes, risk-free self-custody, inevitable adoption, or universal local conclusions. Do not turn a named service into a recommendation.

Produce a bundle in the guide-specific `Assets/diploma/<student-guide|educator-guide|shared>/<asset-id-lowercase>/` folder selected from the placement. Include `micrographic.html`, `micrographic.css`, `meta.json`, `preview.html` in a 458px review frame, `alt-text.md`, `README.md`, and `sanity-asset.json`. Prefix CSS selectors with a unique `.mg-<slug>` root; tag all translatable text with non-nested `data-t` keys; use no JavaScript, external assets, external fonts, CSS grid, vh/vw, rem, fixed/sticky positioning, or `@import`. Do not upload or publish to Sanity. Before declaring completion, report visual checks at 458px, phone, desktop, A4/US Letter, and grayscale.

Required inputs to attach
- Approved transparent PNG reference: Assets/Reference/bd-v-067-ref.jpg
- Matching white-background JPG preview: Assets/Reference/bd-v-067-ref.jpg
- Matching conformance report: Assets/Reference/bd-v-067-ref.json
- Current Claude Design System authoring instructions and closest approved micrographic bundle
- Current Sanity schema/publishing requirements, if available

Complete asset brief
- Asset ID: BD-V-067
- Suggested by: AI
- Priority: Supporting
- Type: Diagram
- Historical page/note: 39 and 48; help learners connect with the local ecosystem through practical field/community work.
- Placement: Under `### Local resource maps and community discovery`, immediately before `Record your local resources`.
- Source locator: 1363
- Text–visual link: Connects community discovery with verification and privacy rather than treating a map listing as proof.
- Design brief: Provide an editable neighborhood or regional map template with merchant, educator, meetup, technical support, exchange information, legal or tax information, and missing-support markers. Every listing includes `date verified` and a safety note. Do not include real personal locations without consent.
- Format: Local resource-map template; full width.

Use the exact heading and insertion direction in Placement as the target placement. Preserve all listed placements in metadata. Include source-brief revision, reference paths, factual sources, production date, reviewer status, checks, and unresolved judgments in README.md. Set `reviewStatus` to draft or review unless an authorized reviewer has approved it.
```
### [ ] BD-V-068 — Table

```text
You are building one production-ready, accessible My First Bitcoin Bitcoin Diploma visual from a supplied approved transparent PNG reference, its white-background JPG preview, and their JSON conformance report. Read the complete brief below before acting. The asset brief is the source of truth for lesson intent, content, safety, caption, alt text, placement, and localization. The reference image guides composition only. If it conflicts with the brief, the brief wins; report any unresolved factual or design-system gap before implementing.

Rebuild—not trace or embed—the reference as editable HTML, CSS, and inline SVG. Apply the supplied Claude Design System rather than the reference's provisional styling. Keep all essential geometry, arrows, labels, warnings, icons, and data editable. Preserve one clear teaching relationship, a decisive reading order, cultural replaceability, grayscale meaning, narrow-page responsiveness, phone and desktop usability, A4/US-Letter printing, expandable translated text, and future RTL adaptation.

Never invent facts, labels, numbers, providers, URLs, legal claims, safety claims, or brand choices. Preserve every prohibition and qualification in the brief. Do not include real seed phrases, private keys, payable addresses, private learner data, balances, or transactions. Use a verified QR, address, URL, interface, date, or fact only when the brief explicitly authorizes it and it has been checked. Do not imply investment returns, guaranteed outcomes, risk-free self-custody, inevitable adoption, or universal local conclusions. Do not turn a named service into a recommendation.

Produce a bundle in the guide-specific `Assets/diploma/<student-guide|educator-guide|shared>/<asset-id-lowercase>/` folder selected from the placement. Include `micrographic.html`, `micrographic.css`, `meta.json`, `preview.html` in a 458px review frame, `alt-text.md`, `README.md`, and `sanity-asset.json`. Prefix CSS selectors with a unique `.mg-<slug>` root; tag all translatable text with non-nested `data-t` keys; use no JavaScript, external assets, external fonts, CSS grid, vh/vw, rem, fixed/sticky positioning, or `@import`. Do not upload or publish to Sanity. Before declaring completion, report visual checks at 458px, phone, desktop, A4/US Letter, and grayscale.

Required inputs to attach
- Approved transparent PNG reference: Assets/Reference/bd-v-068-ref.jpg
- Matching white-background JPG preview: Assets/Reference/bd-v-068-ref.jpg
- Matching conformance report: Assets/Reference/bd-v-068-ref.json
- Current Claude Design System authoring instructions and closest approved micrographic bundle
- Current Sanity schema/publishing requirements, if available

Complete asset brief
- Asset ID: BD-V-068
- Suggested by: AI
- Priority: Supporting
- Type: Table
- Historical page/note: 48; provide a printable local-resource record with built-in verification and safety prompts.
- Placement: Under `### Local resource maps and community discovery`, replace the existing `Record your local resources` table visually while retaining an accessible text equivalent.
- Source locator: 1365
- Text–visual link: Helps learners document useful local support while recording when information was checked.
- Design brief: Preserve rows for education group, merchant directory, technical support, local exchange information, and legal or tax information, with purpose, verification date, contact or location, and safety note columns. Do not pre-fill personal locations or imply trustworthiness from a listing.
- Format: Editable local-resource record table; full width.

Use the exact heading and insertion direction in Placement as the target placement. Preserve all listed placements in metadata. Include source-brief revision, reference paths, factual sources, production date, reviewer status, checks, and unresolved judgments in README.md. Set `reviewStatus` to draft or review unless an authorized reviewer has approved it.
```
### [ ] BD-V-069 — Diagram

```text
You are building one production-ready, accessible My First Bitcoin Bitcoin Diploma visual from a supplied approved transparent PNG reference, its white-background JPG preview, and their JSON conformance report. Read the complete brief below before acting. The asset brief is the source of truth for lesson intent, content, safety, caption, alt text, placement, and localization. The reference image guides composition only. If it conflicts with the brief, the brief wins; report any unresolved factual or design-system gap before implementing.

Rebuild—not trace or embed—the reference as editable HTML, CSS, and inline SVG. Apply the supplied Claude Design System rather than the reference's provisional styling. Keep all essential geometry, arrows, labels, warnings, icons, and data editable. Preserve one clear teaching relationship, a decisive reading order, cultural replaceability, grayscale meaning, narrow-page responsiveness, phone and desktop usability, A4/US-Letter printing, expandable translated text, and future RTL adaptation.

Never invent facts, labels, numbers, providers, URLs, legal claims, safety claims, or brand choices. Preserve every prohibition and qualification in the brief. Do not include real seed phrases, private keys, payable addresses, private learner data, balances, or transactions. Use a verified QR, address, URL, interface, date, or fact only when the brief explicitly authorizes it and it has been checked. Do not imply investment returns, guaranteed outcomes, risk-free self-custody, inevitable adoption, or universal local conclusions. Do not turn a named service into a recommendation.

Produce a bundle in the guide-specific `Assets/diploma/<student-guide|educator-guide|shared>/<asset-id-lowercase>/` folder selected from the placement. Include `micrographic.html`, `micrographic.css`, `meta.json`, `preview.html` in a 458px review frame, `alt-text.md`, `README.md`, and `sanity-asset.json`. Prefix CSS selectors with a unique `.mg-<slug>` root; tag all translatable text with non-nested `data-t` keys; use no JavaScript, external assets, external fonts, CSS grid, vh/vw, rem, fixed/sticky positioning, or `@import`. Do not upload or publish to Sanity. Before declaring completion, report visual checks at 458px, phone, desktop, A4/US Letter, and grayscale.

Required inputs to attach
- Approved transparent PNG reference: Assets/Reference/bd-v-069-ref.jpg
- Matching white-background JPG preview: Assets/Reference/bd-v-069-ref.jpg
- Matching conformance report: Assets/Reference/bd-v-069-ref.json
- Current Claude Design System authoring instructions and closest approved micrographic bundle
- Current Sanity schema/publishing requirements, if available

Complete asset brief
- Asset ID: BD-V-069
- Suggested by: AI
- Priority: Supporting
- Type: Diagram
- Historical page/note: 49–50; frame the review around the learner's community and a specific local need.
- Placement: Under `### Review: connect this to your community`, after the paragraph beginning `**Module 4 answer:**` and before `#### Key takeaways`. The former final test table is no longer present.
- Source locator: 1379
- Text–visual link: Summarizes the community review as a sequence that begins with a need and ends with evidence and a responsible next step.
- Design brief: Show the decision path `real need → Bitcoin fit → payment method → custody → total cost and trade-offs → safety and local conditions → evidence of success`. Add a return arrow when Bitcoin is not the best available fit.
- Format: Decision path; full width.

Use the exact heading and insertion direction in Placement as the target placement. Preserve all listed placements in metadata. Include source-brief revision, reference paths, factual sources, production date, reviewer status, checks, and unresolved judgments in README.md. Set `reviewStatus` to draft or review unless an authorized reviewer has approved it.
```
### [ ] BD-V-070 — Table

```text
DEFERRED — this prompt does not release the item for production. Leave its checklist item unchecked. The batch selects BD-V-069 for the community review; this optional table alternative remains deferred.

Complete asset brief
- Asset ID: BD-V-070
- Suggested by: AI
- Priority: Conditional
- Type: Table
- Historical page/note: 49–50; make the final local-use test a concise decision and reflection table.
- Placement: Under `### Review: connect this to your community`, after the paragraph beginning `**Module 4 answer:**` and before `#### Key takeaways`, only as a table alternative to `BD-V-069`. This is a proposed summary, not a replacement for an existing table.
- Source locator: 1379
- Text–visual link: Offers a concise optional text equivalent for the community-review decision path.
- Design brief: If a table is clearer than `BD-V-069`, summarize the current review using rows for local need, function of money, realistic alternative, payment path, key control, benefit and risk, local conditions, and responsible next step. Use editable prompts rather than inventing a required test or assessment record. Keep any learner response space optional; formal evidence belongs in the educator assessment process.
- Format: Optional community-review summary table; full width.

Retain the complete brief for a later authorized production decision. Do not generate, upload, or publish an asset in the current batch.
```

## 3.6 Back of Diploma

### [ ] BD-V-071 — Diagram

```text
You are building one production-ready, accessible My First Bitcoin Bitcoin Diploma visual from a supplied approved transparent PNG reference, its white-background JPG preview, and their JSON conformance report. Read the complete brief below before acting. The asset brief is the source of truth for lesson intent, content, safety, caption, alt text, placement, and localization. The reference image guides composition only. If it conflicts with the brief, the brief wins; report any unresolved factual or design-system gap before implementing.

Rebuild—not trace or embed—the reference as editable HTML, CSS, and inline SVG. Apply the supplied Claude Design System rather than the reference's provisional styling. Keep all essential geometry, arrows, labels, warnings, icons, and data editable. Preserve one clear teaching relationship, a decisive reading order, cultural replaceability, grayscale meaning, narrow-page responsiveness, phone and desktop usability, A4/US-Letter printing, expandable translated text, and future RTL adaptation.

Never invent facts, labels, numbers, providers, URLs, legal claims, safety claims, or brand choices. Preserve every prohibition and qualification in the brief. Do not include real seed phrases, private keys, payable addresses, private learner data, balances, or transactions. Use a verified QR, address, URL, interface, date, or fact only when the brief explicitly authorizes it and it has been checked. Do not imply investment returns, guaranteed outcomes, risk-free self-custody, inevitable adoption, or universal local conclusions. Do not turn a named service into a recommendation.

Produce a bundle in the guide-specific `Assets/diploma/<student-guide|educator-guide|shared>/<asset-id-lowercase>/` folder selected from the placement. Include `micrographic.html`, `micrographic.css`, `meta.json`, `preview.html` in a 458px review frame, `alt-text.md`, `README.md`, and `sanity-asset.json`. Prefix CSS selectors with a unique `.mg-<slug>` root; tag all translatable text with non-nested `data-t` keys; use no JavaScript, external assets, external fonts, CSS grid, vh/vw, rem, fixed/sticky positioning, or `@import`. Do not upload or publish to Sanity. Before declaring completion, report visual checks at 458px, phone, desktop, A4/US Letter, and grayscale.

Required inputs to attach
- Approved transparent PNG reference: Assets/Reference/bd-v-071-ref.jpg
- Matching white-background JPG preview: Assets/Reference/bd-v-071-ref.jpg
- Matching conformance report: Assets/Reference/bd-v-071-ref.json
- Current Claude Design System authoring instructions and closest approved micrographic bundle
- Current Sanity schema/publishing requirements, if available

Complete asset brief
- Asset ID: BD-V-071
- Suggested by: AI
- Priority: Supporting
- Type: Diagram
- Historical page/note: 50–51; make next steps quick to scan and separate the available continuation paths.
- Placement: Under `### Continue with the Bitcoin Education Network`, after the paragraph beginning “If you want to teach”. The former “What now?” numbered list is no longer present.
- Source locator: 1425
- Text–visual link: Makes the current community, contribution, and educator pathways visible as voluntary next steps.
- Design brief: Show optional routes to connect with a learning community, learn or volunteer, contribute through the official forms, explore the Educator Training Program, or explore network participation for an existing education community. Reuse the pathway language of `BD-V-077` without implying automatic teaching eligibility or network membership. Do not depict Advanced modules as currently available.
- Format: Next-step pathway map; full width.

Use the exact heading and insertion direction in Placement as the target placement. Preserve all listed placements in metadata. Include source-brief revision, reference paths, factual sources, production date, reviewer status, checks, and unresolved judgments in README.md. Set `reviewStatus` to draft or review unless an authorized reviewer has approved it.
```
### [ ] BD-V-072 — Diagram

```text
You are building one production-ready, accessible My First Bitcoin Bitcoin Diploma visual from a supplied approved transparent PNG reference, its white-background JPG preview, and their JSON conformance report. Read the complete brief below before acting. The asset brief is the source of truth for lesson intent, content, safety, caption, alt text, placement, and localization. The reference image guides composition only. If it conflicts with the brief, the brief wins; report any unresolved factual or design-system gap before implementing.

Rebuild—not trace or embed—the reference as editable HTML, CSS, and inline SVG. Apply the supplied Claude Design System rather than the reference's provisional styling. Keep all essential geometry, arrows, labels, warnings, icons, and data editable. Preserve one clear teaching relationship, a decisive reading order, cultural replaceability, grayscale meaning, narrow-page responsiveness, phone and desktop usability, A4/US-Letter printing, expandable translated text, and future RTL adaptation.

Never invent facts, labels, numbers, providers, URLs, legal claims, safety claims, or brand choices. Preserve every prohibition and qualification in the brief. Do not include real seed phrases, private keys, payable addresses, private learner data, balances, or transactions. Use a verified QR, address, URL, interface, date, or fact only when the brief explicitly authorizes it and it has been checked. Do not imply investment returns, guaranteed outcomes, risk-free self-custody, inevitable adoption, or universal local conclusions. Do not turn a named service into a recommendation.

Produce a bundle in the guide-specific `Assets/diploma/<student-guide|educator-guide|shared>/<asset-id-lowercase>/` folder selected from the placement. Include `micrographic.html`, `micrographic.css`, `meta.json`, `preview.html` in a 458px review frame, `alt-text.md`, `README.md`, and `sanity-asset.json`. Prefix CSS selectors with a unique `.mg-<slug>` root; tag all translatable text with non-nested `data-t` keys; use no JavaScript, external assets, external fonts, CSS grid, vh/vw, rem, fixed/sticky positioning, or `@import`. Do not upload or publish to Sanity. Before declaring completion, report visual checks at 458px, phone, desktop, A4/US Letter, and grayscale.

Required inputs to attach
- Approved transparent PNG reference: Assets/Reference/bd-v-072-ref.jpg
- Matching white-background JPG preview: Assets/Reference/bd-v-072-ref.jpg
- Matching conformance report: Assets/Reference/bd-v-072-ref.json
- Current Claude Design System authoring instructions and closest approved micrographic bundle
- Current Sanity schema/publishing requirements, if available

Complete asset brief
- Asset ID: BD-V-072
- Suggested by: Pablo
- Priority: Essential
- Type: Diagram
- Historical page/note: 51; make the safety reminder scannable and define practical safety tasks precisely.
- Placement: SG: Under `### A safety reminder`, immediately before the reminder list. EG: under `### Final safety reminders`, replace the matching marker after the source text at the listed EG line. See section 3.8 for the exact anchor.
- Source locator: SG: 1439; EG: 3294
- Text–visual link: Makes the minimum stop-and-check behavior memorable at the point of course completion.
- Design brief: Show `stop → verify source and recipient → verify custody, network, destination, amount, and fee → start small → proceed only when understood`. Put seed or private-key secrecy above the whole sequence as a non-negotiable boundary.
- Format: Compact safety strip; half to full width.

Use the exact heading and insertion direction in Placement as the target placement. Preserve all listed placements in metadata. Include source-brief revision, reference paths, factual sources, production date, reviewer status, checks, and unresolved judgments in README.md. Set `reviewStatus` to draft or review unless an authorized reviewer has approved it.
```
### [ ] BD-V-073 — Image

```text
You are building one production-ready, accessible My First Bitcoin Bitcoin Diploma visual from a supplied approved transparent PNG reference, its white-background JPG preview, and their JSON conformance report. Read the complete brief below before acting. The asset brief is the source of truth for lesson intent, content, safety, caption, alt text, placement, and localization. The reference image guides composition only. If it conflicts with the brief, the brief wins; report any unresolved factual or design-system gap before implementing.

Rebuild—not trace or embed—the reference as editable HTML, CSS, and inline SVG. Apply the supplied Claude Design System rather than the reference's provisional styling. Keep all essential geometry, arrows, labels, warnings, icons, and data editable. Preserve one clear teaching relationship, a decisive reading order, cultural replaceability, grayscale meaning, narrow-page responsiveness, phone and desktop usability, A4/US-Letter printing, expandable translated text, and future RTL adaptation.

Never invent facts, labels, numbers, providers, URLs, legal claims, safety claims, or brand choices. Preserve every prohibition and qualification in the brief. Do not include real seed phrases, private keys, payable addresses, private learner data, balances, or transactions. Use a verified QR, address, URL, interface, date, or fact only when the brief explicitly authorizes it and it has been checked. Do not imply investment returns, guaranteed outcomes, risk-free self-custody, inevitable adoption, or universal local conclusions. Do not turn a named service into a recommendation.

Produce a bundle in the guide-specific `Assets/diploma/<student-guide|educator-guide|shared>/<asset-id-lowercase>/` folder selected from the placement. Include `micrographic.html`, `micrographic.css`, `meta.json`, `preview.html` in a 458px review frame, `alt-text.md`, `README.md`, and `sanity-asset.json`. Prefix CSS selectors with a unique `.mg-<slug>` root; tag all translatable text with non-nested `data-t` keys; use no JavaScript, external assets, external fonts, CSS grid, vh/vw, rem, fixed/sticky positioning, or `@import`. Do not upload or publish to Sanity. Before declaring completion, report visual checks at 458px, phone, desktop, A4/US Letter, and grayscale.

Required inputs to attach
- Approved transparent PNG reference: Assets/Reference/bd-v-073-ref.jpg
- Matching white-background JPG preview: Assets/Reference/bd-v-073-ref.jpg
- Matching conformance report: Assets/Reference/bd-v-073-ref.json
- Current Claude Design System authoring instructions and closest approved micrographic bundle
- Current Sanity schema/publishing requirements, if available

Complete asset brief
- Asset ID: BD-V-073
- Suggested by: Pablo
- Priority: Supporting
- Type: Image
- Historical page/note: 52; add a public GitHub contribution link or QR and verify official destinations.
- Placement: Under `### Source or update page, if included`, after the canonical source link.
- Source locator: 1469
- Text–visual link: Provides one durable route to updates and contributions without filling the Diploma with fragile QR codes.
- Design brief: Create one panel containing a tested QR code, printed short URL, destination name, edition or last-verified date, and plain-language purpose. The QR must resolve to the canonical maintained source: `https://github.com/MyFirstBitcoin/mfb-curriculum`. Keep donation and any future educator or issuer-specific certificate verification separate unless the landing page clearly distinguishes them. Do not imply a central My First Bitcoin certificate service.
- Format: QR and fallback-link panel; half page.

Use the exact heading and insertion direction in Placement as the target placement. Preserve all listed placements in metadata. Include source-brief revision, reference paths, factual sources, production date, reviewer status, checks, and unresolved judgments in README.md. Set `reviewStatus` to draft or review unless an authorized reviewer has approved it.
```
### [ ] BD-V-074 — Image

```text
You are building one production-ready, accessible My First Bitcoin Bitcoin Diploma visual from a supplied approved transparent PNG reference, its white-background JPG preview, and their JSON conformance report. Read the complete brief below before acting. The asset brief is the source of truth for lesson intent, content, safety, caption, alt text, placement, and localization. The reference image guides composition only. If it conflicts with the brief, the brief wins; report any unresolved factual or design-system gap before implementing.

Rebuild—not trace or embed—the reference as editable HTML, CSS, and inline SVG. Apply the supplied Claude Design System rather than the reference's provisional styling. Keep all essential geometry, arrows, labels, warnings, icons, and data editable. Preserve one clear teaching relationship, a decisive reading order, cultural replaceability, grayscale meaning, narrow-page responsiveness, phone and desktop usability, A4/US-Letter printing, expandable translated text, and future RTL adaptation.

Never invent facts, labels, numbers, providers, URLs, legal claims, safety claims, or brand choices. Preserve every prohibition and qualification in the brief. Do not include real seed phrases, private keys, payable addresses, private learner data, balances, or transactions. Use a verified QR, address, URL, interface, date, or fact only when the brief explicitly authorizes it and it has been checked. Do not imply investment returns, guaranteed outcomes, risk-free self-custody, inevitable adoption, or universal local conclusions. Do not turn a named service into a recommendation.

Produce a bundle in the guide-specific `Assets/diploma/<student-guide|educator-guide|shared>/<asset-id-lowercase>/` folder selected from the placement. Include `micrographic.html`, `micrographic.css`, `meta.json`, `preview.html` in a 458px review frame, `alt-text.md`, `README.md`, and `sanity-asset.json`. Prefix CSS selectors with a unique `.mg-<slug>` root; tag all translatable text with non-nested `data-t` keys; use no JavaScript, external assets, external fonts, CSS grid, vh/vw, rem, fixed/sticky positioning, or `@import`. Do not upload or publish to Sanity. Before declaring completion, report visual checks at 458px, phone, desktop, A4/US Letter, and grayscale.

Required inputs to attach
- Approved transparent PNG reference: Assets/Reference/bd-v-074-ref.jpg
- Matching white-background JPG preview: Assets/Reference/bd-v-074-ref.jpg
- Matching conformance report: Assets/Reference/bd-v-074-ref.json
- Current Claude Design System authoring instructions and closest approved micrographic bundle
- Current Sanity schema/publishing requirements, if available

Complete asset brief
- Asset ID: BD-V-074
- Suggested by: Pablo
- Priority: Supporting
- Type: Image
- Historical page/note: 52; add separate on-chain and Lightning support QR codes with their payment text printed underneath.
- Placement: Under `### Optional donate / support QR`, after the `Donate to My First Bitcoin` link and before the paragraph beginning “A printed edition may place one official support QR code here”.
- Source locator: 1489
- Text–visual link: Offers the single official support-page route described in the guide, with a readable fallback and voluntary participation.
- Design brief: Create one optional support panel with a QR code linking to the approved destination `https://donate.myfirstbitcoin.org/`, the readable matching URL, destination name, and last-verified date. Keep the adjacent donation-safety paragraph. Do not encode a payment address or invoice in this website QR or imply that a donation is required. Test the destination and final printed QR before publication. The historical two-payment-route proposal is not the current guide placement; separate live on-chain and Lightning QR codes would require official verified destinations and an aligned manuscript revision.
- Format: Single support-page QR panel; half width.

Use the exact heading and insertion direction in Placement as the target placement. Preserve all listed placements in metadata. Include source-brief revision, reference paths, factual sources, production date, reviewer status, checks, and unresolved judgments in README.md. Set `reviewStatus` to draft or review unless an authorized reviewer has approved it.
```
### [ ] BD-V-075 — Diagram

```text
DEFERRED — this prompt does not release the item for production. Leave its checklist item unchecked. DEC-11 defers this verification concept for 2026.10; no current placement or central My First Bitcoin verification service is authorized.

Complete asset brief
- Asset ID: BD-V-075
- Suggested by: AI
- Priority: Conditional
- Type: Diagram
- Historical page/note: —; Deferred after `DEC-11`.
- Placement: No 2026.10 Student Guide placement. The former central-verification section was replaced by `### Certificate meaning and issuer`.
- Source locator: —
- Text–visual link: Retained only as a possible future issuer-specific verification concept; it is not part of the current publication set.
- Design brief: Do not produce for 2026.10. Certification is educator-issued and My First Bitcoin does not operate a central verification service. A future separately governed issuer-specific method may revive this brief only after its real destination, privacy controls, correction and withdrawal rules, and minimum data display are approved and tested. It must identify the actual educator or issuing organization and must not imply central My First Bitcoin evaluation.
- Format: Deferred verification flow; no current asset.

Retain the complete brief for a later authorized production decision. Do not generate, upload, or publish an asset in the current batch.
```

## 3.9 Educator-only asset briefs

### [ ] BD-V-081 — Diagram

```text
You are building one production-ready, accessible My First Bitcoin Bitcoin Diploma visual from a supplied approved transparent PNG reference, its white-background JPG preview, and their JSON conformance report. Read the complete brief below before acting. The asset brief is the source of truth for lesson intent, content, safety, caption, alt text, placement, and localization. The reference image guides composition only. If it conflicts with the brief, the brief wins; report any unresolved factual or design-system gap before implementing.

Rebuild—not trace or embed—the reference as editable HTML, CSS, and inline SVG. Apply the supplied Claude Design System rather than the reference's provisional styling. Keep all essential geometry, arrows, labels, warnings, icons, and data editable. Preserve one clear teaching relationship, a decisive reading order, cultural replaceability, grayscale meaning, narrow-page responsiveness, phone and desktop usability, A4/US-Letter printing, expandable translated text, and future RTL adaptation.

Never invent facts, labels, numbers, providers, URLs, legal claims, safety claims, or brand choices. Preserve every prohibition and qualification in the brief. Do not include real seed phrases, private keys, payable addresses, private learner data, balances, or transactions. Use a verified QR, address, URL, interface, date, or fact only when the brief explicitly authorizes it and it has been checked. Do not imply investment returns, guaranteed outcomes, risk-free self-custody, inevitable adoption, or universal local conclusions. Do not turn a named service into a recommendation.

Produce a bundle in the guide-specific `Assets/diploma/<student-guide|educator-guide|shared>/<asset-id-lowercase>/` folder selected from the placement. Include `micrographic.html`, `micrographic.css`, `meta.json`, `preview.html` in a 458px review frame, `alt-text.md`, `README.md`, and `sanity-asset.json`. Prefix CSS selectors with a unique `.mg-<slug>` root; tag all translatable text with non-nested `data-t` keys; use no JavaScript, external assets, external fonts, CSS grid, vh/vw, rem, fixed/sticky positioning, or `@import`. Do not upload or publish to Sanity. Before declaring completion, report visual checks at 458px, phone, desktop, A4/US Letter, and grayscale.

Required inputs to attach
- Approved transparent PNG reference: Assets/Reference/bd-v-081-ref.jpg
- Matching white-background JPG preview: Assets/Reference/bd-v-081-ref.jpg
- Matching conformance report: Assets/Reference/bd-v-081-ref.json
- Current Claude Design System authoring instructions and closest approved micrographic bundle
- Current Sanity schema/publishing requirements, if available

Complete asset brief
- Asset ID: BD-V-081
- Suggested by: AI
- Priority: Essential
- Type: Diagram
- Historical page/note: —; Proposed in response to the request for educator diagrams.
- Placement: EG only: under `## Assessment at a glance`, after the line beginning `They are also not a combined numerical grade. Both components must be complete, and every requi…`. Replace the `BD-V-081` marker at EG line 45.
- Source locator: EG: 43
- Text–visual link: Makes the two separately required evidence components and their joint completion condition unmistakable.
- Design brief: **Two evidence components and the completion gate.** Use two equal lanes: educator-evaluated theory, C1–C8 (50%); directly observed practice, C9–C11 (50%). Both feed an AND gate labelled every required competency meets standard, then assessment-complete and educator-issued certification. Show a Not yet branch returning to practice and reassessment. Keep C12/C13 formative and optional app review outside the gate. State that percentages are neither teaching time nor a combined numerical grade. Do not invent a pass percentage, automatic certificate-issuing system, or central My First Bitcoin verification service. Caption: `Both evidence components must be complete; one cannot compensate for the other.` Alt text: `Theory competencies C1–C8 and practical competencies C9–C11 must each meet standard before assessment completion. Not yet evidence returns to practice and reassessment; attendance, optional app review, and formative reflection do not replace either component.` Master: `Assets/Briefs/bd-v-081-brief.md`.
- Format: Flow diagram; full width.

Use the exact heading and insertion direction in Placement as the target placement. Preserve all listed placements in metadata. Include source-brief revision, reference paths, factual sources, production date, reviewer status, checks, and unresolved judgments in README.md. Set `reviewStatus` to draft or review unless an authorized reviewer has approved it.
```
### [ ] BD-V-082 — Diagram

```text
You are building one production-ready, accessible My First Bitcoin Bitcoin Diploma visual from a supplied approved transparent PNG reference, its white-background JPG preview, and their JSON conformance report. Read the complete brief below before acting. The asset brief is the source of truth for lesson intent, content, safety, caption, alt text, placement, and localization. The reference image guides composition only. If it conflicts with the brief, the brief wins; report any unresolved factual or design-system gap before implementing.

Rebuild—not trace or embed—the reference as editable HTML, CSS, and inline SVG. Apply the supplied Claude Design System rather than the reference's provisional styling. Keep all essential geometry, arrows, labels, warnings, icons, and data editable. Preserve one clear teaching relationship, a decisive reading order, cultural replaceability, grayscale meaning, narrow-page responsiveness, phone and desktop usability, A4/US-Letter printing, expandable translated text, and future RTL adaptation.

Never invent facts, labels, numbers, providers, URLs, legal claims, safety claims, or brand choices. Preserve every prohibition and qualification in the brief. Do not include real seed phrases, private keys, payable addresses, private learner data, balances, or transactions. Use a verified QR, address, URL, interface, date, or fact only when the brief explicitly authorizes it and it has been checked. Do not imply investment returns, guaranteed outcomes, risk-free self-custody, inevitable adoption, or universal local conclusions. Do not turn a named service into a recommendation.

Produce a bundle in the guide-specific `Assets/diploma/<student-guide|educator-guide|shared>/<asset-id-lowercase>/` folder selected from the placement. Include `micrographic.html`, `micrographic.css`, `meta.json`, `preview.html` in a 458px review frame, `alt-text.md`, `README.md`, and `sanity-asset.json`. Prefix CSS selectors with a unique `.mg-<slug>` root; tag all translatable text with non-nested `data-t` keys; use no JavaScript, external assets, external fonts, CSS grid, vh/vw, rem, fixed/sticky positioning, or `@import`. Do not upload or publish to Sanity. Before declaring completion, report visual checks at 458px, phone, desktop, A4/US Letter, and grayscale.

Required inputs to attach
- Approved transparent PNG reference: Assets/Reference/bd-v-082-ref.jpg
- Matching white-background JPG preview: Assets/Reference/bd-v-082-ref.jpg
- Matching conformance report: Assets/Reference/bd-v-082-ref.json
- Current Claude Design System authoring instructions and closest approved micrographic bundle
- Current Sanity schema/publishing requirements, if available

Complete asset brief
- Asset ID: BD-V-082
- Suggested by: AI
- Priority: Essential
- Type: Diagram
- Historical page/note: —; Proposed in response to the request for educator diagrams.
- Placement: EG only: under `### Capacity and readiness check`, after the line beginning `Record the chosen C11 variant, practical environment, accessibility equivalents, assessor nam…`. Replace the `BD-V-082` marker at EG line 72.
- Source locator: EG: 70
- Text–visual link: Connects cohort size, observation time, assessor capacity, and the advertised course route.
- Design brief: **Observation capacity before scheduling.** Show learner count multiplied by estimated individual evidence minutes, distributed across available approved assessors. Label the quotient minimum observation time per assessor under balanced allocation, not total staff labour saved. Add setup, feedback, resets, accommodations, and reassessment before a fits the planned route decision. If no, loop to a smaller cohort, more approved assessor capacity, or a redesigned advertised schedule. Do not imply several learners can be observed simultaneously without identifiable evidence. Use symbols or clearly fictional numbers only; preserve the source formula as prose. Caption: `Plan enough time to observe each learner before confirming the course schedule.` Alt text: `Learner numbers and individual evidence time determine observation workload. After allowing for setup, feedback, resets, access needs, and reassessment, the educator checks capacity and revises cohort size, assessor capacity, or the advertised schedule if needed.` Master: `Assets/Briefs/bd-v-082-brief.md`.
- Format: Flow diagram; full width.

Use the exact heading and insertion direction in Placement as the target placement. Preserve all listed placements in metadata. Include source-brief revision, reference paths, factual sources, production date, reviewer status, checks, and unresolved judgments in README.md. Set `reviewStatus` to draft or review unless an authorized reviewer has approved it.
```
### [ ] BD-V-083 — Diagram

```text
You are building one production-ready, accessible My First Bitcoin Bitcoin Diploma visual from a supplied approved transparent PNG reference, its white-background JPG preview, and their JSON conformance report. Read the complete brief below before acting. The asset brief is the source of truth for lesson intent, content, safety, caption, alt text, placement, and localization. The reference image guides composition only. If it conflicts with the brief, the brief wins; report any unresolved factual or design-system gap before implementing.

Rebuild—not trace or embed—the reference as editable HTML, CSS, and inline SVG. Apply the supplied Claude Design System rather than the reference's provisional styling. Keep all essential geometry, arrows, labels, warnings, icons, and data editable. Preserve one clear teaching relationship, a decisive reading order, cultural replaceability, grayscale meaning, narrow-page responsiveness, phone and desktop usability, A4/US-Letter printing, expandable translated text, and future RTL adaptation.

Never invent facts, labels, numbers, providers, URLs, legal claims, safety claims, or brand choices. Preserve every prohibition and qualification in the brief. Do not include real seed phrases, private keys, payable addresses, private learner data, balances, or transactions. Use a verified QR, address, URL, interface, date, or fact only when the brief explicitly authorizes it and it has been checked. Do not imply investment returns, guaranteed outcomes, risk-free self-custody, inevitable adoption, or universal local conclusions. Do not turn a named service into a recommendation.

Produce a bundle in the guide-specific `Assets/diploma/<student-guide|educator-guide|shared>/<asset-id-lowercase>/` folder selected from the placement. Include `micrographic.html`, `micrographic.css`, `meta.json`, `preview.html` in a 458px review frame, `alt-text.md`, `README.md`, and `sanity-asset.json`. Prefix CSS selectors with a unique `.mg-<slug>` root; tag all translatable text with non-nested `data-t` keys; use no JavaScript, external assets, external fonts, CSS grid, vh/vw, rem, fixed/sticky positioning, or `@import`. Do not upload or publish to Sanity. Before declaring completion, report visual checks at 458px, phone, desktop, A4/US Letter, and grayscale.

Required inputs to attach
- Approved transparent PNG reference: Assets/Reference/bd-v-083-ref.jpg
- Matching white-background JPG preview: Assets/Reference/bd-v-083-ref.jpg
- Matching conformance report: Assets/Reference/bd-v-083-ref.json
- Current Claude Design System authoring instructions and closest approved micrographic bundle
- Current Sanity schema/publishing requirements, if available

Complete asset brief
- Asset ID: BD-V-083
- Suggested by: AI
- Priority: Essential
- Type: Diagram
- Historical page/note: —; Proposed in response to the request for educator diagrams.
- Placement: EG only: under `### Competency-to-evidence crosswalk`, after the line beginning `\*Planning times are per learner evidence time, not the full teaching time. They are planning e…`. Replace the `BD-V-083` marker at EG line 96.
- Source locator: EG: 94
- Text–visual link: Explains the relationship among task IDs, competency IDs, decimal criteria, and the Assessment Grid.
- Design brief: **Competencies, tasks, criteria, and records.** Map T1 to C1–C2, T2 to C3–C5, T3 to C6–C8; P9 to C9, P10 to C10, P11 to C11. Connect each competency to its required criteria and one final MS/NY record. Use C11.1 and C11.2 nested under C11 as the example of criteria that are not separate result rows. Expand MS as Meets standard and NY as Not yet. Include task, date, assessor, variant where applicable, and concise evidence reference as record metadata. No real learner data. Keep the detailed crosswalk table intact. Caption: `Tasks produce evidence for competencies; criteria support each competency decision.` Alt text: `Three theory interactions cover C1–C8, and three practical tasks cover C9–C11. All required criteria within a competency support one Meets standard or Not yet result recorded with concise evidence metadata.` Master: `Assets/Briefs/bd-v-083-brief.md`.
- Format: Task-to-competency map with one nested criterion example; full width.

Use the exact heading and insertion direction in Placement as the target placement. Preserve all listed placements in metadata. Include source-brief revision, reference paths, factual sources, production date, reviewer status, checks, and unresolved judgments in README.md. Set `reviewStatus` to draft or review unless an authorized reviewer has approved it.
```
### [ ] BD-V-084 — Diagram

```text
You are building one production-ready, accessible My First Bitcoin Bitcoin Diploma visual from a supplied approved transparent PNG reference, its white-background JPG preview, and their JSON conformance report. Read the complete brief below before acting. The asset brief is the source of truth for lesson intent, content, safety, caption, alt text, placement, and localization. The reference image guides composition only. If it conflicts with the brief, the brief wins; report any unresolved factual or design-system gap before implementing.

Rebuild—not trace or embed—the reference as editable HTML, CSS, and inline SVG. Apply the supplied Claude Design System rather than the reference's provisional styling. Keep all essential geometry, arrows, labels, warnings, icons, and data editable. Preserve one clear teaching relationship, a decisive reading order, cultural replaceability, grayscale meaning, narrow-page responsiveness, phone and desktop usability, A4/US-Letter printing, expandable translated text, and future RTL adaptation.

Never invent facts, labels, numbers, providers, URLs, legal claims, safety claims, or brand choices. Preserve every prohibition and qualification in the brief. Do not include real seed phrases, private keys, payable addresses, private learner data, balances, or transactions. Use a verified QR, address, URL, interface, date, or fact only when the brief explicitly authorizes it and it has been checked. Do not imply investment returns, guaranteed outcomes, risk-free self-custody, inevitable adoption, or universal local conclusions. Do not turn a named service into a recommendation.

Produce a bundle in the guide-specific `Assets/diploma/<student-guide|educator-guide|shared>/<asset-id-lowercase>/` folder selected from the placement. Include `micrographic.html`, `micrographic.css`, `meta.json`, `preview.html` in a 458px review frame, `alt-text.md`, `README.md`, and `sanity-asset.json`. Prefix CSS selectors with a unique `.mg-<slug>` root; tag all translatable text with non-nested `data-t` keys; use no JavaScript, external assets, external fonts, CSS grid, vh/vw, rem, fixed/sticky positioning, or `@import`. Do not upload or publish to Sanity. Before declaring completion, report visual checks at 458px, phone, desktop, A4/US Letter, and grayscale.

Required inputs to attach
- Approved transparent PNG reference: Assets/Reference/bd-v-084-ref.jpg
- Matching white-background JPG preview: Assets/Reference/bd-v-084-ref.jpg
- Matching conformance report: Assets/Reference/bd-v-084-ref.json
- Current Claude Design System authoring instructions and closest approved micrographic bundle
- Current Sanity schema/publishing requirements, if available

Complete asset brief
- Asset ID: BD-V-084
- Suggested by: AI
- Priority: Essential
- Type: Diagram
- Historical page/note: —; Proposed in response to the request for educator diagrams.
- Placement: EG only: under `### Common support, safety, and record rules`, after the line beginning `**Permitted support:** Before evidence is gathered, you may read the prompt, repeat it once, pr…`. Replace the `BD-V-084` marker at EG line 106.
- Source locator: EG: 104
- Text–visual link: Separates access support and safety intervention from prompting that supplies the answer.
- Design brief: **Support without supplying the assessed decision.** Use two time bands: before evidence and during practical observation. Before: read the prompt, repeat once, provide approved translation or communication accommodation, clarify a non-assessed word, prepare materials. During: safety stop or reset as permitted. Draw a clear boundary around the learner-owned explanation, comparison, verification, and action. Outside the permitted lane show supplying an answer, selecting a payment detail, or performing a required step. Use a conceptual example, not a new rubric. Read with each task’s specific permitted-support rules. Caption: `Support access and safety while the learner makes the assessed decisions.` Alt text: `An educator may provide the permitted preparation and access support and stop unsafe action. The learner must still supply the assessed explanation, select the relevant details, and perform or direct the required decisions.` Master: `Assets/Briefs/bd-v-084-brief.md`.
- Format: Two-stage support-boundary diagram; half to full width.

Use the exact heading and insertion direction in Placement as the target placement. Preserve all listed placements in metadata. Include source-brief revision, reference paths, factual sources, production date, reviewer status, checks, and unresolved judgments in README.md. Set `reviewStatus` to draft or review unless an authorized reviewer has approved it.
```
### [ ] BD-V-085 — Diagram

```text
You are building one production-ready, accessible My First Bitcoin Bitcoin Diploma visual from a supplied approved transparent PNG reference, its white-background JPG preview, and their JSON conformance report. Read the complete brief below before acting. The asset brief is the source of truth for lesson intent, content, safety, caption, alt text, placement, and localization. The reference image guides composition only. If it conflicts with the brief, the brief wins; report any unresolved factual or design-system gap before implementing.

Rebuild—not trace or embed—the reference as editable HTML, CSS, and inline SVG. Apply the supplied Claude Design System rather than the reference's provisional styling. Keep all essential geometry, arrows, labels, warnings, icons, and data editable. Preserve one clear teaching relationship, a decisive reading order, cultural replaceability, grayscale meaning, narrow-page responsiveness, phone and desktop usability, A4/US-Letter printing, expandable translated text, and future RTL adaptation.

Never invent facts, labels, numbers, providers, URLs, legal claims, safety claims, or brand choices. Preserve every prohibition and qualification in the brief. Do not include real seed phrases, private keys, payable addresses, private learner data, balances, or transactions. Use a verified QR, address, URL, interface, date, or fact only when the brief explicitly authorizes it and it has been checked. Do not imply investment returns, guaranteed outcomes, risk-free self-custody, inevitable adoption, or universal local conclusions. Do not turn a named service into a recommendation.

Produce a bundle in the guide-specific `Assets/diploma/<student-guide|educator-guide|shared>/<asset-id-lowercase>/` folder selected from the placement. Include `micrographic.html`, `micrographic.css`, `meta.json`, `preview.html` in a 458px review frame, `alt-text.md`, `README.md`, and `sanity-asset.json`. Prefix CSS selectors with a unique `.mg-<slug>` root; tag all translatable text with non-nested `data-t` keys; use no JavaScript, external assets, external fonts, CSS grid, vh/vw, rem, fixed/sticky positioning, or `@import`. Do not upload or publish to Sanity. Before declaring completion, report visual checks at 458px, phone, desktop, A4/US Letter, and grayscale.

Required inputs to attach
- Approved transparent PNG reference: Assets/Reference/bd-v-085-ref.jpg
- Matching white-background JPG preview: Assets/Reference/bd-v-085-ref.jpg
- Matching conformance report: Assets/Reference/bd-v-085-ref.json
- Current Claude Design System authoring instructions and closest approved micrographic bundle
- Current Sanity schema/publishing requirements, if available

Complete asset brief
- Asset ID: BD-V-085
- Suggested by: AI
- Priority: Essential
- Type: Diagram
- Historical page/note: —; Proposed in response to the request for educator diagrams.
- Placement: EG only: under `### Reassessment, calibration, and moderation`, after the line beginning `Use only versioned, approved task cards. Review local tools, current facts, translation, access…`. Replace the `BD-V-085` marker at EG line 204.
- Source locator: EG: 202
- Text–visual link: Distinguishes the learner reassessment loop from assessor calibration and cohort moderation.
- Design brief: **Reassessment and educator quality review.** Show three labelled lanes. Learner: Not yet → private criterion-specific feedback → focused practice → same or approved equivalent task → new evidence → update Grid only when sufficient; incomplete evidence loops back. Assessor before delivery: score annotated MS/NY examples for T2, P9, selected P11 → compare judgments → resolve differences → retain calibration record. Cohort: lead or approved second reviewer checks each variant setup and samples records including disputed, reassessed, and safety-critical cases → corrections through approved record process. No automatic promotion from Not yet, public rankings, lowered standards, or replacement of direct observation. Caption: `Improve evidence and consistency without lowering the standard.` Alt text: `Learners receive private feedback, practise, and provide new evidence after Not yet. Educators calibrate judgments before delivery and moderate cohort records through the approved process; review never substitutes for observed performance.` Master: `Assets/Briefs/bd-v-085-brief.md`.
- Format: Three-lane process diagram; full width.

Use the exact heading and insertion direction in Placement as the target placement. Preserve all listed placements in metadata. Include source-brief revision, reference paths, factual sources, production date, reviewer status, checks, and unresolved judgments in README.md. Set `reviewStatus` to draft or review unless an authorized reviewer has approved it.
```
### [ ] BD-V-086 — Diagram

```text
You are building one production-ready, accessible My First Bitcoin Bitcoin Diploma visual from a supplied approved transparent PNG reference, its white-background JPG preview, and their JSON conformance report. Read the complete brief below before acting. The asset brief is the source of truth for lesson intent, content, safety, caption, alt text, placement, and localization. The reference image guides composition only. If it conflicts with the brief, the brief wins; report any unresolved factual or design-system gap before implementing.

Rebuild—not trace or embed—the reference as editable HTML, CSS, and inline SVG. Apply the supplied Claude Design System rather than the reference's provisional styling. Keep all essential geometry, arrows, labels, warnings, icons, and data editable. Preserve one clear teaching relationship, a decisive reading order, cultural replaceability, grayscale meaning, narrow-page responsiveness, phone and desktop usability, A4/US-Letter printing, expandable translated text, and future RTL adaptation.

Never invent facts, labels, numbers, providers, URLs, legal claims, safety claims, or brand choices. Preserve every prohibition and qualification in the brief. Do not include real seed phrases, private keys, payable addresses, private learner data, balances, or transactions. Use a verified QR, address, URL, interface, date, or fact only when the brief explicitly authorizes it and it has been checked. Do not imply investment returns, guaranteed outcomes, risk-free self-custody, inevitable adoption, or universal local conclusions. Do not turn a named service into a recommendation.

Produce a bundle in the guide-specific `Assets/diploma/<student-guide|educator-guide|shared>/<asset-id-lowercase>/` folder selected from the placement. Include `micrographic.html`, `micrographic.css`, `meta.json`, `preview.html` in a 458px review frame, `alt-text.md`, `README.md`, and `sanity-asset.json`. Prefix CSS selectors with a unique `.mg-<slug>` root; tag all translatable text with non-nested `data-t` keys; use no JavaScript, external assets, external fonts, CSS grid, vh/vw, rem, fixed/sticky positioning, or `@import`. Do not upload or publish to Sanity. Before declaring completion, report visual checks at 458px, phone, desktop, A4/US Letter, and grayscale.

Required inputs to attach
- Approved transparent PNG reference: Assets/Reference/bd-v-086-ref.jpg
- Matching white-background JPG preview: Assets/Reference/bd-v-086-ref.jpg
- Matching conformance report: Assets/Reference/bd-v-086-ref.json
- Current Claude Design System authoring instructions and closest approved micrographic bundle
- Current Sanity schema/publishing requirements, if available

Complete asset brief
- Asset ID: BD-V-086
- Suggested by: AI
- Priority: Essential
- Type: Diagram
- Historical page/note: —; Proposed in response to the request for educator diagrams.
- Placement: EG only: under `### The learning ecosystem`, after the line beginning `&#124; Operational assessment protocol and Grid &#124; Approved assessment interactions and tasks, observ…`. Replace the `BD-V-086` marker at EG line 391.
- Source locator: EG: 389
- Text–visual link: Makes resource ownership and the route from teaching to recorded evidence visible.
- Design brief: **How the learning resources work together.** Map Student Guide → learner explanations; Educator Guide → preparation, facilitation, safety; Resources Hub → selected activities; operational protocol → approved tasks and standards; Assessment Grid → private competency results. Show the educator connecting teaching, practice, observation, and records. Place optional app self-checks on a separate review branch without a certification-evidence arrow. Any app name must use the required hyperlink. Keep the existing table as the detailed text equivalent. Caption: `Use each resource for its job in the learning and evidence process.` Alt text: `The Student Guide supplies explanations, the Educator Guide supports teaching, and selected Resources Hub activities support practice. The operational protocol governs evidence collection and the Assessment Grid holds private results. Optional app self-checks support review only.` Master: `Assets/Briefs/bd-v-086-brief.md`.
- Format: Resource relationship map; full width.

Use the exact heading and insertion direction in Placement as the target placement. Preserve all listed placements in metadata. Include source-brief revision, reference paths, factual sources, production date, reviewer status, checks, and unresolved judgments in README.md. Set `reviewStatus` to draft or review unless an authorized reviewer has approved it.
```
### [ ] BD-V-087 — Diagram

```text
You are building one production-ready, accessible My First Bitcoin Bitcoin Diploma visual from a supplied approved transparent PNG reference, its white-background JPG preview, and their JSON conformance report. Read the complete brief below before acting. The asset brief is the source of truth for lesson intent, content, safety, caption, alt text, placement, and localization. The reference image guides composition only. If it conflicts with the brief, the brief wins; report any unresolved factual or design-system gap before implementing.

Rebuild—not trace or embed—the reference as editable HTML, CSS, and inline SVG. Apply the supplied Claude Design System rather than the reference's provisional styling. Keep all essential geometry, arrows, labels, warnings, icons, and data editable. Preserve one clear teaching relationship, a decisive reading order, cultural replaceability, grayscale meaning, narrow-page responsiveness, phone and desktop usability, A4/US-Letter printing, expandable translated text, and future RTL adaptation.

Never invent facts, labels, numbers, providers, URLs, legal claims, safety claims, or brand choices. Preserve every prohibition and qualification in the brief. Do not include real seed phrases, private keys, payable addresses, private learner data, balances, or transactions. Use a verified QR, address, URL, interface, date, or fact only when the brief explicitly authorizes it and it has been checked. Do not imply investment returns, guaranteed outcomes, risk-free self-custody, inevitable adoption, or universal local conclusions. Do not turn a named service into a recommendation.

Produce a bundle in the guide-specific `Assets/diploma/<student-guide|educator-guide|shared>/<asset-id-lowercase>/` folder selected from the placement. Include `micrographic.html`, `micrographic.css`, `meta.json`, `preview.html` in a 458px review frame, `alt-text.md`, `README.md`, and `sanity-asset.json`. Prefix CSS selectors with a unique `.mg-<slug>` root; tag all translatable text with non-nested `data-t` keys; use no JavaScript, external assets, external fonts, CSS grid, vh/vw, rem, fixed/sticky positioning, or `@import`. Do not upload or publish to Sanity. Before declaring completion, report visual checks at 458px, phone, desktop, A4/US Letter, and grayscale.

Required inputs to attach
- Approved transparent PNG reference: Assets/Reference/bd-v-087-ref.jpg
- Matching white-background JPG preview: Assets/Reference/bd-v-087-ref.jpg
- Matching conformance report: Assets/Reference/bd-v-087-ref.json
- Current Claude Design System authoring instructions and closest approved micrographic bundle
- Current Sanity schema/publishing requirements, if available

Complete asset brief
- Asset ID: BD-V-087
- Suggested by: AI
- Priority: Essential
- Type: Diagram
- Historical page/note: —; Proposed in response to the request for educator diagrams.
- Placement: EG only: under `## 2. What stays fixed and what can change`, after the line beginning `- move advanced technical or professional content into the required Diploma at the cost of requ…`. Replace the `BD-V-087` marker at EG line 454.
- Source locator: EG: 452
- Text–visual link: Shows what educators can adapt while preserving the same Diploma standard.
- Design brief: **Fixed standards and local adaptation.** Use three labelled regions matching the source table: fixed, adaptable, flexible with guardrails. Keep required competencies, learner actions, safety, evidence, and passing standard inside a fixed boundary. Put examples, language, grouping, tools, and environment in the adaptable area. Route assessment or delivery changes through an equivalence check before use; if uncertain, use for practice and select an approved assessment route. Do not infer that any local change is an approved certificated variant. Preserve the existing table and both may/may-not lists. Caption: `Localize the route while preserving the required learner action and standard.` Alt text: `Local examples and teaching methods can change inside fixed competency, evidence, safety, and completion boundaries. Changes affecting assessment require an approved equivalent route.` Master: `Assets/Briefs/bd-v-087-brief.md`.
- Format: Three-region boundary diagram with an equivalence gate; full width.

Use the exact heading and insertion direction in Placement as the target placement. Preserve all listed placements in metadata. Include source-brief revision, reference paths, factual sources, production date, reviewer status, checks, and unresolved judgments in README.md. Set `reviewStatus` to draft or review unless an authorized reviewer has approved it.
```
### [ ] BD-V-099 — Diagram

```text
You are building one production-ready, accessible My First Bitcoin Bitcoin Diploma visual from a supplied approved transparent PNG reference, its white-background JPG preview, and their JSON conformance report. Read the complete brief below before acting. The asset brief is the source of truth for lesson intent, content, safety, caption, alt text, placement, and localization. The reference image guides composition only. If it conflicts with the brief, the brief wins; report any unresolved factual or design-system gap before implementing.

Rebuild—not trace or embed—the reference as editable HTML, CSS, and inline SVG. Apply the supplied Claude Design System rather than the reference's provisional styling. Keep all essential geometry, arrows, labels, warnings, icons, and data editable. Preserve one clear teaching relationship, a decisive reading order, cultural replaceability, grayscale meaning, narrow-page responsiveness, phone and desktop usability, A4/US-Letter printing, expandable translated text, and future RTL adaptation.

Never invent facts, labels, numbers, providers, URLs, legal claims, safety claims, or brand choices. Preserve every prohibition and qualification in the brief. Do not include real seed phrases, private keys, payable addresses, private learner data, balances, or transactions. Use a verified QR, address, URL, interface, date, or fact only when the brief explicitly authorizes it and it has been checked. Do not imply investment returns, guaranteed outcomes, risk-free self-custody, inevitable adoption, or universal local conclusions. Do not turn a named service into a recommendation.

Produce a bundle in the guide-specific `Assets/diploma/<student-guide|educator-guide|shared>/<asset-id-lowercase>/` folder selected from the placement. Include `micrographic.html`, `micrographic.css`, `meta.json`, `preview.html` in a 458px review frame, `alt-text.md`, `README.md`, and `sanity-asset.json`. Prefix CSS selectors with a unique `.mg-<slug>` root; tag all translatable text with non-nested `data-t` keys; use no JavaScript, external assets, external fonts, CSS grid, vh/vw, rem, fixed/sticky positioning, or `@import`. Do not upload or publish to Sanity. Before declaring completion, report visual checks at 458px, phone, desktop, A4/US Letter, and grayscale.

Required inputs to attach
- Approved transparent PNG reference: Assets/Reference/bd-v-099-ref.jpg
- Matching white-background JPG preview: Assets/Reference/bd-v-099-ref.jpg
- Matching conformance report: Assets/Reference/bd-v-099-ref.json
- Current Claude Design System authoring instructions and closest approved micrographic bundle
- Current Sanity schema/publishing requirements, if available

Complete asset brief
- Asset ID: BD-V-099
- Suggested by: AI
- Priority: Essential
- Type: Diagram
- Historical page/note: —; Proposed in response to the request for educator diagrams.
- Placement: EG only: under `### Local verification record`, after the line beginning `Prefer authoritative primary sources for current rules. If the evidence is incomplete, say so. …`. Replace the `BD-V-099` marker at EG line 708.
- Source locator: EG: 706
- Text–visual link: Connects changing local claims to dated sources, classroom wording, and a fallback.
- Design brief: **Verify, date, teach, and recheck local information.** Show identify claim → distinguish stable concept/changing detail → check authoritative primary source or qualified local expertise → record source, date, version, and limitation → use qualified classroom wording → recheck before reuse. Unverified or changed details branch to state uncertainty, a clearly hypothetical example, or a prepared safe fallback; live action must not depend on an unverified safety-critical claim. Include generic wallet-version, fee, rule, and merchant-listing examples without filling in current facts. Link to the existing record table rather than creating a second form. Caption: `A local example needs a source, a date, and a plan for change.` Alt text: `Educators distinguish stable concepts from changing details, verify current sources, record dates and limits, teach qualified examples, and recheck them before reuse. Uncertainty or change triggers a safer example or fallback.` Master: `Assets/Briefs/bd-v-099-brief.md`.
- Format: Verification lifecycle with an uncertainty branch; full width.

Use the exact heading and insertion direction in Placement as the target placement. Preserve all listed placements in metadata. Include source-brief revision, reference paths, factual sources, production date, reviewer status, checks, and unresolved judgments in README.md. Set `reviewStatus` to draft or review unless an authorized reviewer has approved it.
```
### [ ] BD-V-088 — Diagram

```text
You are building one production-ready, accessible My First Bitcoin Bitcoin Diploma visual from a supplied approved transparent PNG reference, its white-background JPG preview, and their JSON conformance report. Read the complete brief below before acting. The asset brief is the source of truth for lesson intent, content, safety, caption, alt text, placement, and localization. The reference image guides composition only. If it conflicts with the brief, the brief wins; report any unresolved factual or design-system gap before implementing.

Rebuild—not trace or embed—the reference as editable HTML, CSS, and inline SVG. Apply the supplied Claude Design System rather than the reference's provisional styling. Keep all essential geometry, arrows, labels, warnings, icons, and data editable. Preserve one clear teaching relationship, a decisive reading order, cultural replaceability, grayscale meaning, narrow-page responsiveness, phone and desktop usability, A4/US-Letter printing, expandable translated text, and future RTL adaptation.

Never invent facts, labels, numbers, providers, URLs, legal claims, safety claims, or brand choices. Preserve every prohibition and qualification in the brief. Do not include real seed phrases, private keys, payable addresses, private learner data, balances, or transactions. Use a verified QR, address, URL, interface, date, or fact only when the brief explicitly authorizes it and it has been checked. Do not imply investment returns, guaranteed outcomes, risk-free self-custody, inevitable adoption, or universal local conclusions. Do not turn a named service into a recommendation.

Produce a bundle in the guide-specific `Assets/diploma/<student-guide|educator-guide|shared>/<asset-id-lowercase>/` folder selected from the placement. Include `micrographic.html`, `micrographic.css`, `meta.json`, `preview.html` in a 458px review frame, `alt-text.md`, `README.md`, and `sanity-asset.json`. Prefix CSS selectors with a unique `.mg-<slug>` root; tag all translatable text with non-nested `data-t` keys; use no JavaScript, external assets, external fonts, CSS grid, vh/vw, rem, fixed/sticky positioning, or `@import`. Do not upload or publish to Sanity. Before declaring completion, report visual checks at 458px, phone, desktop, A4/US Letter, and grayscale.

Required inputs to attach
- Approved transparent PNG reference: Assets/Reference/bd-v-088-ref.jpg
- Matching white-background JPG preview: Assets/Reference/bd-v-088-ref.jpg
- Matching conformance report: Assets/Reference/bd-v-088-ref.json
- Current Claude Design System authoring instructions and closest approved micrographic bundle
- Current Sanity schema/publishing requirements, if available

Complete asset brief
- Asset ID: BD-V-088
- Suggested by: AI
- Priority: Essential
- Type: Diagram
- Historical page/note: —; Proposed in response to the request for educator diagrams.
- Placement: EG only: under `### The learning rhythm`, after the line beginning `8. **Connect:** Show how the idea prepares for the next part of the Diploma.`. Replace the `BD-V-088` marker at EG line 731.
- Source locator: EG: 729
- Text–visual link: Makes the educator’s eight-step teaching cycle quick to follow and repeat.
- Design brief: **The educator facilitation rhythm.** Show Purpose → Activate → Explain → Check → Apply → Produce → Debrief → Connect. Use short role labels and a return arrow from Check or Debrief to explanation or practice when needed. Identify Check as feedback unless the approved formal evidence conditions are met. Keep the learner doing the explaining or performing at Produce. This is a separate educator graphic: do not overwrite the five-stage SG rhythm in BD-V-006. Caption: `Move from a clear purpose to learner action, debrief, and connection.` Alt text: `The educator sets purpose, activates prior ideas, explains, checks, guides application, invites independent production, debriefs, and connects to the next concept. Unclear responses lead back to explanation or practice.` Master: `Assets/Briefs/bd-v-088-brief.md`.
- Format: Eight-stage cycle in two readable rows; full width.

Use the exact heading and insertion direction in Placement as the target placement. Preserve all listed placements in metadata. Include source-brief revision, reference paths, factual sources, production date, reviewer status, checks, and unresolved judgments in README.md. Set `reviewStatus` to draft or review unless an authorized reviewer has approved it.
```
### [ ] BD-V-101 — Diagram

```text
You are building one production-ready, accessible My First Bitcoin Bitcoin Diploma visual from a supplied approved transparent PNG reference, its white-background JPG preview, and their JSON conformance report. Read the complete brief below before acting. The asset brief is the source of truth for lesson intent, content, safety, caption, alt text, placement, and localization. The reference image guides composition only. If it conflicts with the brief, the brief wins; report any unresolved factual or design-system gap before implementing.

Rebuild—not trace or embed—the reference as editable HTML, CSS, and inline SVG. Apply the supplied Claude Design System rather than the reference's provisional styling. Keep all essential geometry, arrows, labels, warnings, icons, and data editable. Preserve one clear teaching relationship, a decisive reading order, cultural replaceability, grayscale meaning, narrow-page responsiveness, phone and desktop usability, A4/US-Letter printing, expandable translated text, and future RTL adaptation.

Never invent facts, labels, numbers, providers, URLs, legal claims, safety claims, or brand choices. Preserve every prohibition and qualification in the brief. Do not include real seed phrases, private keys, payable addresses, private learner data, balances, or transactions. Use a verified QR, address, URL, interface, date, or fact only when the brief explicitly authorizes it and it has been checked. Do not imply investment returns, guaranteed outcomes, risk-free self-custody, inevitable adoption, or universal local conclusions. Do not turn a named service into a recommendation.

Produce a bundle in the guide-specific `Assets/diploma/<student-guide|educator-guide|shared>/<asset-id-lowercase>/` folder selected from the placement. Include `micrographic.html`, `micrographic.css`, `meta.json`, `preview.html` in a 458px review frame, `alt-text.md`, `README.md`, and `sanity-asset.json`. Prefix CSS selectors with a unique `.mg-<slug>` root; tag all translatable text with non-nested `data-t` keys; use no JavaScript, external assets, external fonts, CSS grid, vh/vw, rem, fixed/sticky positioning, or `@import`. Do not upload or publish to Sanity. Before declaring completion, report visual checks at 458px, phone, desktop, A4/US Letter, and grayscale.

Required inputs to attach
- Approved transparent PNG reference: Assets/Reference/bd-v-101-ref.jpg
- Matching white-background JPG preview: Assets/Reference/bd-v-101-ref.jpg
- Matching conformance report: Assets/Reference/bd-v-101-ref.json
- Current Claude Design System authoring instructions and closest approved micrographic bundle
- Current Sanity schema/publishing requirements, if available

Complete asset brief
- Asset ID: BD-V-101
- Suggested by: AI
- Priority: Essential
- Type: Diagram
- Historical page/note: —; Proposed in response to the request for educator diagrams.
- Placement: EG only: under `### Scenario analysis`, after the line beginning `Change one condition after the first answer. For example: the internet fails, the address chang…`. Replace the `BD-V-101` marker at EG line 772.
- Source locator: EG: 770
- Text–visual link: Makes the educator’s use of changed conditions visible as a test of transferable reasoning.
- Design brief: **Scenario reasoning when a condition changes.** Trace goal → known facts/unknowns to verify → control of money/keys/records/rules → options and failure points → smallest safe next step. Then change one condition: connection fails, destination changes, recipient needs local currency, or fee rises. Loop to the affected fact, control, or option rather than automatically repeating the original action. Show stopping or declining a path as valid where justified. Use one fictional scenario, no personal financial disclosures or live payment instructions. This is facilitation, not a newly approved assessment task. Caption: `Change one condition and ask the learner to reconsider the decision.` Alt text: `A fictional scenario moves from goal and verified facts to control, options, risks, and a safe next step. A changed connection, destination, recipient need, or fee sends reasoning back to the affected decision.` Master: `Assets/Briefs/bd-v-101-brief.md`.
- Format: Decision path with a changed-condition return loop; full width.

Use the exact heading and insertion direction in Placement as the target placement. Preserve all listed placements in metadata. Include source-brief revision, reference paths, factual sources, production date, reviewer status, checks, and unresolved judgments in README.md. Set `reviewStatus` to draft or review unless an authorized reviewer has approved it.
```
### [ ] BD-V-089 — Diagram

```text
You are building one production-ready, accessible My First Bitcoin Bitcoin Diploma visual from a supplied approved transparent PNG reference, its white-background JPG preview, and their JSON conformance report. Read the complete brief below before acting. The asset brief is the source of truth for lesson intent, content, safety, caption, alt text, placement, and localization. The reference image guides composition only. If it conflicts with the brief, the brief wins; report any unresolved factual or design-system gap before implementing.

Rebuild—not trace or embed—the reference as editable HTML, CSS, and inline SVG. Apply the supplied Claude Design System rather than the reference's provisional styling. Keep all essential geometry, arrows, labels, warnings, icons, and data editable. Preserve one clear teaching relationship, a decisive reading order, cultural replaceability, grayscale meaning, narrow-page responsiveness, phone and desktop usability, A4/US-Letter printing, expandable translated text, and future RTL adaptation.

Never invent facts, labels, numbers, providers, URLs, legal claims, safety claims, or brand choices. Preserve every prohibition and qualification in the brief. Do not include real seed phrases, private keys, payable addresses, private learner data, balances, or transactions. Use a verified QR, address, URL, interface, date, or fact only when the brief explicitly authorizes it and it has been checked. Do not imply investment returns, guaranteed outcomes, risk-free self-custody, inevitable adoption, or universal local conclusions. Do not turn a named service into a recommendation.

Produce a bundle in the guide-specific `Assets/diploma/<student-guide|educator-guide|shared>/<asset-id-lowercase>/` folder selected from the placement. Include `micrographic.html`, `micrographic.css`, `meta.json`, `preview.html` in a 458px review frame, `alt-text.md`, `README.md`, and `sanity-asset.json`. Prefix CSS selectors with a unique `.mg-<slug>` root; tag all translatable text with non-nested `data-t` keys; use no JavaScript, external assets, external fonts, CSS grid, vh/vw, rem, fixed/sticky positioning, or `@import`. Do not upload or publish to Sanity. Before declaring completion, report visual checks at 458px, phone, desktop, A4/US Letter, and grayscale.

Required inputs to attach
- Approved transparent PNG reference: Assets/Reference/bd-v-089-ref.jpg
- Matching white-background JPG preview: Assets/Reference/bd-v-089-ref.jpg
- Matching conformance report: Assets/Reference/bd-v-089-ref.json
- Current Claude Design System authoring instructions and closest approved micrographic bundle
- Current Sanity schema/publishing requirements, if available

Complete asset brief
- Asset ID: BD-V-089
- Suggested by: AI
- Priority: Essential
- Type: Diagram
- Historical page/note: —; Proposed in response to the request for educator diagrams.
- Placement: EG only: under `### Media and tool fallbacks`, after the line beginning `Offline teaching and assessment are valid. Use offline knowledge checks for preparation and app…`. Replace the `BD-V-089` marker at EG line 843.
- Source locator: EG: 841
- Text–visual link: Shows why changing the medium must preserve the learner’s action and observed evidence.
- Design brief: **Equivalent learning and evidence across delivery modes.** Branch from one competency into prepared live tool, printed screens/cards, and an approved accessible communication or control route. Reconverge at the same learner decision/action, required verification, educator observation, and standard. Show barriers such as device, connection, language, or access needs leading to a prepared equivalent, not to lower criteria. Include a no valid equivalent branch returning to preparation/practice without certification. Draw examples from the adjacent table but retain its full list. Do not turn watching a video or another learner’s performance into evidence. Caption: `Change the medium, preserve the action and evidence.` Alt text: `Live tools, paper simulations, and approved accessible routes can support the same competency when the learner still makes the required decisions and the educator can judge equivalent evidence. Without equivalence, prepare another route before certification.` Master: `Assets/Briefs/bd-v-089-brief.md`.
- Format: Branch-and-rejoin equivalence diagram; full width.

Use the exact heading and insertion direction in Placement as the target placement. Preserve all listed placements in metadata. Include source-brief revision, reference paths, factual sources, production date, reviewer status, checks, and unresolved judgments in README.md. Set `reviewStatus` to draft or review unless an authorized reviewer has approved it.
```
### [ ] BD-V-090 — Diagram

```text
You are building one production-ready, accessible My First Bitcoin Bitcoin Diploma visual from a supplied approved transparent PNG reference, its white-background JPG preview, and their JSON conformance report. Read the complete brief below before acting. The asset brief is the source of truth for lesson intent, content, safety, caption, alt text, placement, and localization. The reference image guides composition only. If it conflicts with the brief, the brief wins; report any unresolved factual or design-system gap before implementing.

Rebuild—not trace or embed—the reference as editable HTML, CSS, and inline SVG. Apply the supplied Claude Design System rather than the reference's provisional styling. Keep all essential geometry, arrows, labels, warnings, icons, and data editable. Preserve one clear teaching relationship, a decisive reading order, cultural replaceability, grayscale meaning, narrow-page responsiveness, phone and desktop usability, A4/US-Letter printing, expandable translated text, and future RTL adaptation.

Never invent facts, labels, numbers, providers, URLs, legal claims, safety claims, or brand choices. Preserve every prohibition and qualification in the brief. Do not include real seed phrases, private keys, payable addresses, private learner data, balances, or transactions. Use a verified QR, address, URL, interface, date, or fact only when the brief explicitly authorizes it and it has been checked. Do not imply investment returns, guaranteed outcomes, risk-free self-custody, inevitable adoption, or universal local conclusions. Do not turn a named service into a recommendation.

Produce a bundle in the guide-specific `Assets/diploma/<student-guide|educator-guide|shared>/<asset-id-lowercase>/` folder selected from the placement. Include `micrographic.html`, `micrographic.css`, `meta.json`, `preview.html` in a 458px review frame, `alt-text.md`, `README.md`, and `sanity-asset.json`. Prefix CSS selectors with a unique `.mg-<slug>` root; tag all translatable text with non-nested `data-t` keys; use no JavaScript, external assets, external fonts, CSS grid, vh/vw, rem, fixed/sticky positioning, or `@import`. Do not upload or publish to Sanity. Before declaring completion, report visual checks at 458px, phone, desktop, A4/US Letter, and grayscale.

Required inputs to attach
- Approved transparent PNG reference: Assets/Reference/bd-v-090-ref.jpg
- Matching white-background JPG preview: Assets/Reference/bd-v-090-ref.jpg
- Matching conformance report: Assets/Reference/bd-v-090-ref.json
- Current Claude Design System authoring instructions and closest approved micrographic bundle
- Current Sanity schema/publishing requirements, if available

Complete asset brief
- Asset ID: BD-V-090
- Suggested by: AI
- Priority: Essential
- Type: Diagram
- Historical page/note: —; Proposed in response to the request for educator diagrams.
- Placement: EG only: under `### Universal stop conditions`, after the line beginning `Stopping is a successful safety behavior. Do not shame the learner who notices a problem.`. Replace the `BD-V-090` marker at EG line 909.
- Source locator: EG: 907
- Text–visual link: Turns the safety triggers into an educator response rather than a list to memorize.
- Design brief: **Stop, protect, verify, and choose a safe route.** Feed source triggers into STOP: secret exposure, mismatch, unverified source, urgency, changed behaviour, uncertain funds, privacy exposure, failed safety check, or educator uncertainty. Then protect people and information → verify independently without collecting secrets → choose a prepared safe equivalent or postpone. Resume only when the relevant safety checks can be satisfied. Add a distinct formal-assessment branch: a safety-critical error produces NY under the protocol, followed by feedback, practice, and reassessment. Do not label every device failure a learner failure or offer an improvised funds-recovery procedure. Caption: `Stopping protects learning; resume through a verified safe route.` Alt text: `An unsafe or unexplained condition stops the activity. The educator protects people and secrets, verifies the issue, and uses a safe prepared route or postpones. A learner safety-critical assessment error is recorded Not yet under the protocol.` Master: `Assets/Briefs/bd-v-090-brief.md`.
- Format: Flow diagram; full width.

Use the exact heading and insertion direction in Placement as the target placement. Preserve all listed placements in metadata. Include source-brief revision, reference paths, factual sources, production date, reviewer status, checks, and unresolved judgments in README.md. Set `reviewStatus` to draft or review unless an authorized reviewer has approved it.
```
### [ ] BD-V-100 — Diagram

```text
You are building one production-ready, accessible My First Bitcoin Bitcoin Diploma visual from a supplied approved transparent PNG reference, its white-background JPG preview, and their JSON conformance report. Read the complete brief below before acting. The asset brief is the source of truth for lesson intent, content, safety, caption, alt text, placement, and localization. The reference image guides composition only. If it conflicts with the brief, the brief wins; report any unresolved factual or design-system gap before implementing.

Rebuild—not trace or embed—the reference as editable HTML, CSS, and inline SVG. Apply the supplied Claude Design System rather than the reference's provisional styling. Keep all essential geometry, arrows, labels, warnings, icons, and data editable. Preserve one clear teaching relationship, a decisive reading order, cultural replaceability, grayscale meaning, narrow-page responsiveness, phone and desktop usability, A4/US-Letter printing, expandable translated text, and future RTL adaptation.

Never invent facts, labels, numbers, providers, URLs, legal claims, safety claims, or brand choices. Preserve every prohibition and qualification in the brief. Do not include real seed phrases, private keys, payable addresses, private learner data, balances, or transactions. Use a verified QR, address, URL, interface, date, or fact only when the brief explicitly authorizes it and it has been checked. Do not imply investment returns, guaranteed outcomes, risk-free self-custody, inevitable adoption, or universal local conclusions. Do not turn a named service into a recommendation.

Produce a bundle in the guide-specific `Assets/diploma/<student-guide|educator-guide|shared>/<asset-id-lowercase>/` folder selected from the placement. Include `micrographic.html`, `micrographic.css`, `meta.json`, `preview.html` in a 458px review frame, `alt-text.md`, `README.md`, and `sanity-asset.json`. Prefix CSS selectors with a unique `.mg-<slug>` root; tag all translatable text with non-nested `data-t` keys; use no JavaScript, external assets, external fonts, CSS grid, vh/vw, rem, fixed/sticky positioning, or `@import`. Do not upload or publish to Sanity. Before declaring completion, report visual checks at 458px, phone, desktop, A4/US Letter, and grayscale.

Required inputs to attach
- Approved transparent PNG reference: Assets/Reference/bd-v-100-ref.jpg
- Matching white-background JPG preview: Assets/Reference/bd-v-100-ref.jpg
- Matching conformance report: Assets/Reference/bd-v-100-ref.json
- Current Claude Design System authoring instructions and closest approved micrographic bundle
- Current Sanity schema/publishing requirements, if available

Complete asset brief
- Asset ID: BD-V-100
- Suggested by: AI
- Priority: Essential
- Type: Diagram
- Historical page/note: —; Proposed in response to the request for educator diagrams.
- Placement: EG only: under `### Bitcoin, stablecoins, and other crypto-assets`, after the line beginning `Do not imply that every non-Bitcoin [asset](mfb-bd-lx.md#term-asset) has the same structure. Th…`. Replace the `BD-V-100` marker at EG line 1634.
- Source locator: EG: 1632
- Text–visual link: Helps educators explain similar-looking interfaces backed by different control and verification relationships.
- Design brief: **Compare digital-asset trust dependencies.** Use three lanes for Bitcoin, a generic stablecoin model, and a generic other-asset model. Apply the same questions about issuance/control, supply support, independent verification, and counterparties. Show public node-enforced rules for Bitcoin; design-dependent reserves/redemption or other mechanisms for stablecoins; varying project rules/governance for other assets. Add a separate service/custody layer across all lanes so Bitcoin service risk remains visible. Keep every design qualification from the existing table. No brands, tickers, logos, prices, rankings, recommendations, or suggestion every model works alike. Preserve the table as detailed reference. Caption: `Compare who controls the rules and which claims can be verified.` Alt text: `Three generic asset models are compared through issuance, supply support, verification, and counterparties. Wallets and custodians form a separate dependency layer across all three; similar interfaces do not establish the same trust model.` Master: `Assets/Briefs/bd-v-100-brief.md`.
- Format: Three-lane dependency diagram; full width.

Use the exact heading and insertion direction in Placement as the target placement. Preserve all listed placements in metadata. Include source-brief revision, reference paths, factual sources, production date, reviewer status, checks, and unresolved judgments in README.md. Set `reviewStatus` to draft or review unless an authorized reviewer has approved it.
```
### [ ] BD-V-092 — Diagram

```text
You are building one production-ready, accessible My First Bitcoin Bitcoin Diploma visual from a supplied approved transparent PNG reference, its white-background JPG preview, and their JSON conformance report. Read the complete brief below before acting. The asset brief is the source of truth for lesson intent, content, safety, caption, alt text, placement, and localization. The reference image guides composition only. If it conflicts with the brief, the brief wins; report any unresolved factual or design-system gap before implementing.

Rebuild—not trace or embed—the reference as editable HTML, CSS, and inline SVG. Apply the supplied Claude Design System rather than the reference's provisional styling. Keep all essential geometry, arrows, labels, warnings, icons, and data editable. Preserve one clear teaching relationship, a decisive reading order, cultural replaceability, grayscale meaning, narrow-page responsiveness, phone and desktop usability, A4/US-Letter printing, expandable translated text, and future RTL adaptation.

Never invent facts, labels, numbers, providers, URLs, legal claims, safety claims, or brand choices. Preserve every prohibition and qualification in the brief. Do not include real seed phrases, private keys, payable addresses, private learner data, balances, or transactions. Use a verified QR, address, URL, interface, date, or fact only when the brief explicitly authorizes it and it has been checked. Do not imply investment returns, guaranteed outcomes, risk-free self-custody, inevitable adoption, or universal local conclusions. Do not turn a named service into a recommendation.

Produce a bundle in the guide-specific `Assets/diploma/<student-guide|educator-guide|shared>/<asset-id-lowercase>/` folder selected from the placement. Include `micrographic.html`, `micrographic.css`, `meta.json`, `preview.html` in a 458px review frame, `alt-text.md`, `README.md`, and `sanity-asset.json`. Prefix CSS selectors with a unique `.mg-<slug>` root; tag all translatable text with non-nested `data-t` keys; use no JavaScript, external assets, external fonts, CSS grid, vh/vw, rem, fixed/sticky positioning, or `@import`. Do not upload or publish to Sanity. Before declaring completion, report visual checks at 458px, phone, desktop, A4/US Letter, and grayscale.

Required inputs to attach
- Approved transparent PNG reference: Assets/Reference/bd-v-092-ref.jpg
- Matching white-background JPG preview: Assets/Reference/bd-v-092-ref.jpg
- Matching conformance report: Assets/Reference/bd-v-092-ref.json
- Current Claude Design System authoring instructions and closest approved micrographic bundle
- Current Sanity schema/publishing requirements, if available

Complete asset brief
- Asset ID: BD-V-092
- Suggested by: AI
- Priority: Essential
- Type: Diagram
- Historical page/note: —; Proposed in response to the request for educator diagrams.
- Placement: EG only: under `### Address history and reuse lookup`, after the line beginning `**Offline fallback:** Use a printed sequence showing one address used once and another reused a…`. Replace the `BD-V-092` marker at EG line 1933.
- Source locator: EG: 1931
- Text–visual link: Makes address reuse and the limits of public-data inference visible without exposing anyone’s transactions.
- Design brief: **Address reuse and information linkage.** Use fictional non-address labels A/B/C, arrows, and invented receipts. Compare multiple receipts to one address with separate fresh receiving addresses. Show an observer linking reused receipts, plus a dotted uncertain link from external identifying information. Add a separate explorer-search arrow showing that a service may learn which address interests a device. State that an address alone does not prove legal identity and fresh addresses do not guarantee anonymity. No real addresses, txids, amounts belonging to people, or scannable QR codes. Related BD-V-046 concerns confirmations, not identity linkage. Caption: `Fresh addresses reduce easy linkage; they do not guarantee anonymity.` Alt text: `Several fictional receipts share one reused address and are easily linked. Fresh receiving addresses reduce that direct link, but outside information and explorer searches can still reveal relationships. Public data does not by itself prove a person’s identity.` Master: `Assets/Briefs/bd-v-092-brief.md`.
- Format: Two-panel linkage diagram with an explorer privacy inset; full width.

Use the exact heading and insertion direction in Placement as the target placement. Preserve all listed placements in metadata. Include source-brief revision, reference paths, factual sources, production date, reviewer status, checks, and unresolved judgments in README.md. Set `reviewStatus` to draft or review unless an authorized reviewer has approved it.
```
### [ ] BD-V-091 — Diagram

```text
You are building one production-ready, accessible My First Bitcoin Bitcoin Diploma visual from a supplied approved transparent PNG reference, its white-background JPG preview, and their JSON conformance report. Read the complete brief below before acting. The asset brief is the source of truth for lesson intent, content, safety, caption, alt text, placement, and localization. The reference image guides composition only. If it conflicts with the brief, the brief wins; report any unresolved factual or design-system gap before implementing.

Rebuild—not trace or embed—the reference as editable HTML, CSS, and inline SVG. Apply the supplied Claude Design System rather than the reference's provisional styling. Keep all essential geometry, arrows, labels, warnings, icons, and data editable. Preserve one clear teaching relationship, a decisive reading order, cultural replaceability, grayscale meaning, narrow-page responsiveness, phone and desktop usability, A4/US-Letter printing, expandable translated text, and future RTL adaptation.

Never invent facts, labels, numbers, providers, URLs, legal claims, safety claims, or brand choices. Preserve every prohibition and qualification in the brief. Do not include real seed phrases, private keys, payable addresses, private learner data, balances, or transactions. Use a verified QR, address, URL, interface, date, or fact only when the brief explicitly authorizes it and it has been checked. Do not imply investment returns, guaranteed outcomes, risk-free self-custody, inevitable adoption, or universal local conclusions. Do not turn a named service into a recommendation.

Produce a bundle in the guide-specific `Assets/diploma/<student-guide|educator-guide|shared>/<asset-id-lowercase>/` folder selected from the placement. Include `micrographic.html`, `micrographic.css`, `meta.json`, `preview.html` in a 458px review frame, `alt-text.md`, `README.md`, and `sanity-asset.json`. Prefix CSS selectors with a unique `.mg-<slug>` root; tag all translatable text with non-nested `data-t` keys; use no JavaScript, external assets, external fonts, CSS grid, vh/vw, rem, fixed/sticky positioning, or `@import`. Do not upload or publish to Sanity. Before declaring completion, report visual checks at 458px, phone, desktop, A4/US Letter, and grayscale.

Required inputs to attach
- Approved transparent PNG reference: Assets/Reference/bd-v-091-ref.jpg
- Matching white-background JPG preview: Assets/Reference/bd-v-091-ref.jpg
- Matching conformance report: Assets/Reference/bd-v-091-ref.json
- Current Claude Design System authoring instructions and closest approved micrographic bundle
- Current Sanity schema/publishing requirements, if available

Complete asset brief
- Asset ID: BD-V-091
- Suggested by: AI
- Priority: Essential
- Type: Diagram
- Historical page/note: —; Proposed in response to the request for educator diagrams.
- Placement: EG only: under `#### Activity: recovery-readiness simulation`, after the line beginning `7. return the fictional material securely or destroy it as instructed.`. Replace the `BD-V-091` marker at EG line 2005.
- Source locator: EG: 2003
- Text–visual link: Separates what the learner controls from what the educator may observe during recovery practice.
- Design brief: **Recovery practice without observing secrets.** Use learner and educator lanes around a private-material boundary. Preserve the seven EG production steps: official instructions, compatibility, private work, approved backup-check/recovery method, expected receiving information or history, clear temporary device, return or destroy fictional material as instructed. The educator observes sequence, decisions, and safe handling without seeing real recovery words. Use placeholders only and no recovery-entry screenshot. Label prepared fake material or disposable empty training wallet. Related BD-V-043 supplies the SG six-step overview; this asset adds educator visibility boundaries and the EG material-return step. Do not represent this diagram as the P10 rubric. Caption: `Observe the recovery process without observing a learner’s secrets.` Alt text: `The learner follows seven prepared recovery-practice steps in a private area, checks the expected result, clears the device, and returns or destroys fictional material. The educator observes decisions and safe handling across a boundary that hides secret information.` Master: `Assets/Briefs/bd-v-091-brief.md`.
- Format: Two-lane privacy-boundary workflow; full width.

Use the exact heading and insertion direction in Placement as the target placement. Preserve all listed placements in metadata. Include source-brief revision, reference paths, factual sources, production date, reviewer status, checks, and unresolved judgments in README.md. Set `reviewStatus` to draft or review unless an authorized reviewer has approved it.
```
### [ ] BD-V-093 — Diagram

```text
You are building one production-ready, accessible My First Bitcoin Bitcoin Diploma visual from a supplied approved transparent PNG reference, its white-background JPG preview, and their JSON conformance report. Read the complete brief below before acting. The asset brief is the source of truth for lesson intent, content, safety, caption, alt text, placement, and localization. The reference image guides composition only. If it conflicts with the brief, the brief wins; report any unresolved factual or design-system gap before implementing.

Rebuild—not trace or embed—the reference as editable HTML, CSS, and inline SVG. Apply the supplied Claude Design System rather than the reference's provisional styling. Keep all essential geometry, arrows, labels, warnings, icons, and data editable. Preserve one clear teaching relationship, a decisive reading order, cultural replaceability, grayscale meaning, narrow-page responsiveness, phone and desktop usability, A4/US-Letter printing, expandable translated text, and future RTL adaptation.

Never invent facts, labels, numbers, providers, URLs, legal claims, safety claims, or brand choices. Preserve every prohibition and qualification in the brief. Do not include real seed phrases, private keys, payable addresses, private learner data, balances, or transactions. Use a verified QR, address, URL, interface, date, or fact only when the brief explicitly authorizes it and it has been checked. Do not imply investment returns, guaranteed outcomes, risk-free self-custody, inevitable adoption, or universal local conclusions. Do not turn a named service into a recommendation.

Produce a bundle in the guide-specific `Assets/diploma/<student-guide|educator-guide|shared>/<asset-id-lowercase>/` folder selected from the placement. Include `micrographic.html`, `micrographic.css`, `meta.json`, `preview.html` in a 458px review frame, `alt-text.md`, `README.md`, and `sanity-asset.json`. Prefix CSS selectors with a unique `.mg-<slug>` root; tag all translatable text with non-nested `data-t` keys; use no JavaScript, external assets, external fonts, CSS grid, vh/vw, rem, fixed/sticky positioning, or `@import`. Do not upload or publish to Sanity. Before declaring completion, report visual checks at 458px, phone, desktop, A4/US Letter, and grayscale.

Required inputs to attach
- Approved transparent PNG reference: Assets/Reference/bd-v-093-ref.jpg
- Matching white-background JPG preview: Assets/Reference/bd-v-093-ref.jpg
- Matching conformance report: Assets/Reference/bd-v-093-ref.json
- Current Claude Design System authoring instructions and closest approved micrographic bundle
- Current Sanity schema/publishing requirements, if available

Complete asset brief
- Asset ID: BD-V-093
- Suggested by: AI
- Priority: Essential
- Type: Diagram
- Historical page/note: —; Proposed in response to the request for educator diagrams.
- Placement: EG only: under `### Integrated Module 3 practice circuit`, after the line beginning `Do not use the stations as formal assessment unless the exact tasks, variants, criteria, and re…`. Replace the `BD-V-093` marker at EG line 2295.
- Source locator: EG: 2293
- Text–visual link: Shows how station rotation supports practice without confusing group participation with assessment.
- Design brief: **Practice stations and individual observation.** Arrange the eight current stations in a suggested rotation: wallet/custody, public or secret, receive, send, recovery, explorer, scam, pathway. Mark a private recovery zone, prepared materials, device reset between learners, and a separate individual-observation lane. Label stations practice unless exact approved task, variant, criteria, and records are in place. Show one learner making or directing decisions; peers may support practice but cannot supply another learner’s assessed performance. Keep the original station table and avoid implying all stations fit a fixed two-hour session. Caption: `Use groups for practice and preserve individual evidence for assessment.` Alt text: `Eight practice stations cover custody, public and secret information, receiving, sending, recovery, explorers, scams, and pathways. A separate approved observation route identifies each learner’s decisions; shared-device resets and private recovery space protect participants.` Master: `Assets/Briefs/bd-v-093-brief.md`.
- Format: Station layout and separate observation lane; full width.

Use the exact heading and insertion direction in Placement as the target placement. Preserve all listed placements in metadata. Include source-brief revision, reference paths, factual sources, production date, reviewer status, checks, and unresolved judgments in README.md. Set `reviewStatus` to draft or review unless an authorized reviewer has approved it.
```
### [ ] BD-V-094 — Diagram

```text
You are building one production-ready, accessible My First Bitcoin Bitcoin Diploma visual from a supplied approved transparent PNG reference, its white-background JPG preview, and their JSON conformance report. Read the complete brief below before acting. The asset brief is the source of truth for lesson intent, content, safety, caption, alt text, placement, and localization. The reference image guides composition only. If it conflicts with the brief, the brief wins; report any unresolved factual or design-system gap before implementing.

Rebuild—not trace or embed—the reference as editable HTML, CSS, and inline SVG. Apply the supplied Claude Design System rather than the reference's provisional styling. Keep all essential geometry, arrows, labels, warnings, icons, and data editable. Preserve one clear teaching relationship, a decisive reading order, cultural replaceability, grayscale meaning, narrow-page responsiveness, phone and desktop usability, A4/US-Letter printing, expandable translated text, and future RTL adaptation.

Never invent facts, labels, numbers, providers, URLs, legal claims, safety claims, or brand choices. Preserve every prohibition and qualification in the brief. Do not include real seed phrases, private keys, payable addresses, private learner data, balances, or transactions. Use a verified QR, address, URL, interface, date, or fact only when the brief explicitly authorizes it and it has been checked. Do not imply investment returns, guaranteed outcomes, risk-free self-custody, inevitable adoption, or universal local conclusions. Do not turn a named service into a recommendation.

Produce a bundle in the guide-specific `Assets/diploma/<student-guide|educator-guide|shared>/<asset-id-lowercase>/` folder selected from the placement. Include `micrographic.html`, `micrographic.css`, `meta.json`, `preview.html` in a 458px review frame, `alt-text.md`, `README.md`, and `sanity-asset.json`. Prefix CSS selectors with a unique `.mg-<slug>` root; tag all translatable text with non-nested `data-t` keys; use no JavaScript, external assets, external fonts, CSS grid, vh/vw, rem, fixed/sticky positioning, or `@import`. Do not upload or publish to Sanity. Before declaring completion, report visual checks at 458px, phone, desktop, A4/US Letter, and grayscale.

Required inputs to attach
- Approved transparent PNG reference: Assets/Reference/bd-v-094-ref.jpg
- Matching white-background JPG preview: Assets/Reference/bd-v-094-ref.jpg
- Matching conformance report: Assets/Reference/bd-v-094-ref.json
- Current Claude Design System authoring instructions and closest approved micrographic bundle
- Current Sanity schema/publishing requirements, if available

Complete asset brief
- Asset ID: BD-V-094
- Suggested by: AI
- Priority: Essential
- Type: Diagram
- Historical page/note: —; Proposed in response to the request for educator diagrams.
- Placement: EG only: under `### The seven-step module builder`, before the line beginning `#### 1. Learn the local context`. Replace the `BD-V-094` marker at EG line 2404.
- Source locator: EG: 2410
- Text–visual link: Gives educators a map of the seven-step planning process before its detailed subsections.
- Design brief: **Build a local Connect lesson.** Show the exact seven steps: learn local context; define need/opportunity; select focused module; verify facts/tools/expertise; design Presentation → Practice → Production; define safety/evidence; debrief and choose a safe next step. Carry the existing non-Bitcoin alternative from need to debrief. Mark C11.1 safe sequence and C11.2 explanation as preserved requirements, not new result rows. Use a loop from failed verification to task selection, and a legitimate conclusion of not suitable here. Link visually to BD-V-056 and the readiness gate BD-V-095. Do not make a named product the starting point. Caption: `Begin with a local need and finish with evidence and a responsible next step.` Alt text: `Seven planning stages connect local context and need to a focused, verified task, safe teaching sequence, observable evidence, and debrief. The existing alternative stays in view, and unsuitable options return to planning.` Master: `Assets/Briefs/bd-v-094-brief.md`.
- Format: Seven-stage planning map; full width.

Use the exact heading and insertion direction in Placement as the target placement. Preserve all listed placements in metadata. Include source-brief revision, reference paths, factual sources, production date, reviewer status, checks, and unresolved judgments in README.md. Set `reviewStatus` to draft or review unless an authorized reviewer has approved it.
```
### [ ] BD-V-095 — Diagram

```text
You are building one production-ready, accessible My First Bitcoin Bitcoin Diploma visual from a supplied approved transparent PNG reference, its white-background JPG preview, and their JSON conformance report. Read the complete brief below before acting. The asset brief is the source of truth for lesson intent, content, safety, caption, alt text, placement, and localization. The reference image guides composition only. If it conflicts with the brief, the brief wins; report any unresolved factual or design-system gap before implementing.

Rebuild—not trace or embed—the reference as editable HTML, CSS, and inline SVG. Apply the supplied Claude Design System rather than the reference's provisional styling. Keep all essential geometry, arrows, labels, warnings, icons, and data editable. Preserve one clear teaching relationship, a decisive reading order, cultural replaceability, grayscale meaning, narrow-page responsiveness, phone and desktop usability, A4/US-Letter printing, expandable translated text, and future RTL adaptation.

Never invent facts, labels, numbers, providers, URLs, legal claims, safety claims, or brand choices. Preserve every prohibition and qualification in the brief. Do not include real seed phrases, private keys, payable addresses, private learner data, balances, or transactions. Use a verified QR, address, URL, interface, date, or fact only when the brief explicitly authorizes it and it has been checked. Do not imply investment returns, guaranteed outcomes, risk-free self-custody, inevitable adoption, or universal local conclusions. Do not turn a named service into a recommendation.

Produce a bundle in the guide-specific `Assets/diploma/<student-guide|educator-guide|shared>/<asset-id-lowercase>/` folder selected from the placement. Include `micrographic.html`, `micrographic.css`, `meta.json`, `preview.html` in a 458px review frame, `alt-text.md`, `README.md`, and `sanity-asset.json`. Prefix CSS selectors with a unique `.mg-<slug>` root; tag all translatable text with non-nested `data-t` keys; use no JavaScript, external assets, external fonts, CSS grid, vh/vw, rem, fixed/sticky positioning, or `@import`. Do not upload or publish to Sanity. Before declaring completion, report visual checks at 458px, phone, desktop, A4/US Letter, and grayscale.

Required inputs to attach
- Approved transparent PNG reference: Assets/Reference/bd-v-095-ref.jpg
- Matching white-background JPG preview: Assets/Reference/bd-v-095-ref.jpg
- Matching conformance report: Assets/Reference/bd-v-095-ref.json
- Current Claude Design System authoring instructions and closest approved micrographic bundle
- Current Sanity schema/publishing requirements, if available

Complete asset brief
- Asset ID: BD-V-095
- Suggested by: AI
- Priority: Essential
- Type: Diagram
- Historical page/note: —; Proposed in response to the request for educator diagrams.
- Placement: EG only: under `### Module 4 readiness gate`, after the line beginning `&#124; Can evidence be observed? &#124; The educator can see the learner's decisions and hear the explana…`. Replace the `BD-V-095` marker at EG line 2528.
- Source locator: EG: 2526
- Text–visual link: Shows that every readiness condition must be satisfied before live delivery.
- Design brief: **Readiness before live local practice.** Use eight labelled checks in the source order: real need, clear competency/approved task, educator capability, verified tool, understood local rules, low risk, equitable access, observable evidence. All satisfactory leads to planned live delivery; any gap branches to the corresponding source-table remedy, such as simulation, expert support, accessible equivalent, or revised observation capacity. Feed the remedy back into readiness review. Preserve the full table as the detailed text equivalent. No aggregate readiness score; seven out of eight is not sufficient. Simulation may be the chosen first route. Caption: `Resolve each readiness gap before live delivery.` Alt text: `Eight checks cover purpose, competency, educator capability, tools, local rules, safety, access, and observation. Every check must be satisfactory for live delivery; a gap leads to a safer route or revised plan and another readiness review.` Master: `Assets/Briefs/bd-v-095-brief.md`.
- Format: Flow diagram; full width.

Use the exact heading and insertion direction in Placement as the target placement. Preserve all listed placements in metadata. Include source-brief revision, reference paths, factual sources, production date, reviewer status, checks, and unresolved judgments in README.md. Set `reviewStatus` to draft or review unless an authorized reviewer has approved it.
```
### [ ] BD-V-096 — Diagram

```text
You are building one production-ready, accessible My First Bitcoin Bitcoin Diploma visual from a supplied approved transparent PNG reference, its white-background JPG preview, and their JSON conformance report. Read the complete brief below before acting. The asset brief is the source of truth for lesson intent, content, safety, caption, alt text, placement, and localization. The reference image guides composition only. If it conflicts with the brief, the brief wins; report any unresolved factual or design-system gap before implementing.

Rebuild—not trace or embed—the reference as editable HTML, CSS, and inline SVG. Apply the supplied Claude Design System rather than the reference's provisional styling. Keep all essential geometry, arrows, labels, warnings, icons, and data editable. Preserve one clear teaching relationship, a decisive reading order, cultural replaceability, grayscale meaning, narrow-page responsiveness, phone and desktop usability, A4/US-Letter printing, expandable translated text, and future RTL adaptation.

Never invent facts, labels, numbers, providers, URLs, legal claims, safety claims, or brand choices. Preserve every prohibition and qualification in the brief. Do not include real seed phrases, private keys, payable addresses, private learner data, balances, or transactions. Use a verified QR, address, URL, interface, date, or fact only when the brief explicitly authorizes it and it has been checked. Do not imply investment returns, guaranteed outcomes, risk-free self-custody, inevitable adoption, or universal local conclusions. Do not turn a named service into a recommendation.

Produce a bundle in the guide-specific `Assets/diploma/<student-guide|educator-guide|shared>/<asset-id-lowercase>/` folder selected from the placement. Include `micrographic.html`, `micrographic.css`, `meta.json`, `preview.html` in a 458px review frame, `alt-text.md`, `README.md`, and `sanity-asset.json`. Prefix CSS selectors with a unique `.mg-<slug>` root; tag all translatable text with non-nested `data-t` keys; use no JavaScript, external assets, external fonts, CSS grid, vh/vw, rem, fixed/sticky positioning, or `@import`. Do not upload or publish to Sanity. Before declaring completion, report visual checks at 458px, phone, desktop, A4/US Letter, and grayscale.

Required inputs to attach
- Approved transparent PNG reference: Assets/Reference/bd-v-096-ref.jpg
- Matching white-background JPG preview: Assets/Reference/bd-v-096-ref.jpg
- Matching conformance report: Assets/Reference/bd-v-096-ref.json
- Current Claude Design System authoring instructions and closest approved micrographic bundle
- Current Sanity schema/publishing requirements, if available

Complete asset brief
- Asset ID: BD-V-096
- Suggested by: AI
- Priority: Essential
- Type: Diagram
- Historical page/note: —; Proposed in response to the request for educator diagrams.
- Placement: EG only: under `### Community custody and shared funds`, after the line beginning `Do not turn [community-custody](mfb-bd-lx.md#term-community-custody) design into a beginner imp…`. Replace the `BD-V-096` marker at EG line 2811.
- Source locator: EG: 2809
- Text–visual link: Reveals who controls shared funds and which responsibilities remain separate.
- Design brief: **Community funds and concentrated responsibility.** Map fictional contributors/beneficiaries, key controller or custodian, payment authorization, and records/review. Use distinct arrows for value, authority, and information. Flag concentration when one organizer controls every function. Surround the map with backup/succession, privacy, disputes/loss, legal context, and transparency questions from the prose. Treat separation of duties as a question to examine, not a prescribed implementation. No actual funds, addresses, wallet configuration, multisignature setup, legal conclusions, or assumption that community reputation guarantees safety. Related BD-V-065 maps circulation; this maps control. Caption: `Community purpose does not remove custody risk.` Alt text: `Contributors depend on whoever controls shared funds. A role map separates key control, spending authority, records, and review and highlights concentrated trust, continuity, privacy, dispute, and legal questions.` Master: `Assets/Briefs/bd-v-096-brief.md`.
- Format: Role-and-responsibility map with distinct arrow types; full width.

Use the exact heading and insertion direction in Placement as the target placement. Preserve all listed placements in metadata. Include source-brief revision, reference paths, factual sources, production date, reviewer status, checks, and unresolved judgments in README.md. Set `reviewStatus` to draft or review unless an authorized reviewer has approved it.
```
### [ ] BD-V-097 — Diagram

```text
You are building one production-ready, accessible My First Bitcoin Bitcoin Diploma visual from a supplied approved transparent PNG reference, its white-background JPG preview, and their JSON conformance report. Read the complete brief below before acting. The asset brief is the source of truth for lesson intent, content, safety, caption, alt text, placement, and localization. The reference image guides composition only. If it conflicts with the brief, the brief wins; report any unresolved factual or design-system gap before implementing.

Rebuild—not trace or embed—the reference as editable HTML, CSS, and inline SVG. Apply the supplied Claude Design System rather than the reference's provisional styling. Keep all essential geometry, arrows, labels, warnings, icons, and data editable. Preserve one clear teaching relationship, a decisive reading order, cultural replaceability, grayscale meaning, narrow-page responsiveness, phone and desktop usability, A4/US-Letter printing, expandable translated text, and future RTL adaptation.

Never invent facts, labels, numbers, providers, URLs, legal claims, safety claims, or brand choices. Preserve every prohibition and qualification in the brief. Do not include real seed phrases, private keys, payable addresses, private learner data, balances, or transactions. Use a verified QR, address, URL, interface, date, or fact only when the brief explicitly authorizes it and it has been checked. Do not imply investment returns, guaranteed outcomes, risk-free self-custody, inevitable adoption, or universal local conclusions. Do not turn a named service into a recommendation.

Produce a bundle in the guide-specific `Assets/diploma/<student-guide|educator-guide|shared>/<asset-id-lowercase>/` folder selected from the placement. Include `micrographic.html`, `micrographic.css`, `meta.json`, `preview.html` in a 458px review frame, `alt-text.md`, `README.md`, and `sanity-asset.json`. Prefix CSS selectors with a unique `.mg-<slug>` root; tag all translatable text with non-nested `data-t` keys; use no JavaScript, external assets, external fonts, CSS grid, vh/vw, rem, fixed/sticky positioning, or `@import`. Do not upload or publish to Sanity. Before declaring completion, report visual checks at 458px, phone, desktop, A4/US Letter, and grayscale.

Required inputs to attach
- Approved transparent PNG reference: Assets/Reference/bd-v-097-ref.jpg
- Matching white-background JPG preview: Assets/Reference/bd-v-097-ref.jpg
- Matching conformance report: Assets/Reference/bd-v-097-ref.json
- Current Claude Design System authoring instructions and closest approved micrographic bundle
- Current Sanity schema/publishing requirements, if available

Complete asset brief
- Asset ID: BD-V-097
- Suggested by: AI
- Priority: Essential
- Type: Diagram
- Historical page/note: —; Proposed in response to the request for educator diagrams.
- Placement: EG only: under `### Translation workflow`, after the line beginning `9. Confirm that the language version preserves the competencies, safety instructions, and asses…`. Replace the `BD-V-097` marker at EG line 2980.
- Source locator: EG: 2978
- Text–visual link: Shows translation as a review-and-test process, not a one-way text conversion.
- Design brief: **Translation with meaning and safety checks.** Preserve all nine steps as compact numbered labels grouped into prepare meaning (1–3), translate/localize (4–5), and review/test/confirm equivalence (6–9). Show language specialist and subject-matter educator at review; difficult safety instructions return to wording when learner testing exposes ambiguity. Preserve competency, task difficulty, rubric, and stop conditions. Do not imply machine translation or a language review alone approves assessment equivalence. Keep the existing numbered list as the text equivalent. Caption: `Translate the meaning and test that the same safe action is understood.` Alt text: `Clear source meaning and terminology lead to translation and authorized localization, then language and subject review, learner safety testing, and confirmation of equivalent competencies and assessment standards. Ambiguity returns to revision.` Master: `Assets/Briefs/bd-v-097-brief.md`.
- Format: Flow diagram; full width.

Use the exact heading and insertion direction in Placement as the target placement. Preserve all listed placements in metadata. Include source-brief revision, reference paths, factual sources, production date, reviewer status, checks, and unresolved judgments in README.md. Set `reviewStatus` to draft or review unless an authorized reviewer has approved it.
```
### [ ] BD-V-098 — Diagram

```text
You are building one production-ready, accessible My First Bitcoin Bitcoin Diploma visual from a supplied approved transparent PNG reference, its white-background JPG preview, and their JSON conformance report. Read the complete brief below before acting. The asset brief is the source of truth for lesson intent, content, safety, caption, alt text, placement, and localization. The reference image guides composition only. If it conflicts with the brief, the brief wins; report any unresolved factual or design-system gap before implementing.

Rebuild—not trace or embed—the reference as editable HTML, CSS, and inline SVG. Apply the supplied Claude Design System rather than the reference's provisional styling. Keep all essential geometry, arrows, labels, warnings, icons, and data editable. Preserve one clear teaching relationship, a decisive reading order, cultural replaceability, grayscale meaning, narrow-page responsiveness, phone and desktop usability, A4/US-Letter printing, expandable translated text, and future RTL adaptation.

Never invent facts, labels, numbers, providers, URLs, legal claims, safety claims, or brand choices. Preserve every prohibition and qualification in the brief. Do not include real seed phrases, private keys, payable addresses, private learner data, balances, or transactions. Use a verified QR, address, URL, interface, date, or fact only when the brief explicitly authorizes it and it has been checked. Do not imply investment returns, guaranteed outcomes, risk-free self-custody, inevitable adoption, or universal local conclusions. Do not turn a named service into a recommendation.

Produce a bundle in the guide-specific `Assets/diploma/<student-guide|educator-guide|shared>/<asset-id-lowercase>/` folder selected from the placement. Include `micrographic.html`, `micrographic.css`, `meta.json`, `preview.html` in a 458px review frame, `alt-text.md`, `README.md`, and `sanity-asset.json`. Prefix CSS selectors with a unique `.mg-<slug>` root; tag all translatable text with non-nested `data-t` keys; use no JavaScript, external assets, external fonts, CSS grid, vh/vw, rem, fixed/sticky positioning, or `@import`. Do not upload or publish to Sanity. Before declaring completion, report visual checks at 458px, phone, desktop, A4/US Letter, and grayscale.

Required inputs to attach
- Approved transparent PNG reference: Assets/Reference/bd-v-098-ref.jpg
- Matching white-background JPG preview: Assets/Reference/bd-v-098-ref.jpg
- Matching conformance report: Assets/Reference/bd-v-098-ref.json
- Current Claude Design System authoring instructions and closest approved micrographic bundle
- Current Sanity schema/publishing requirements, if available

Complete asset brief
- Asset ID: BD-V-098
- Suggested by: AI
- Priority: Essential
- Type: Diagram
- Historical page/note: —; Proposed in response to the request for educator diagrams.
- Placement: EG only: under `### Adapt a summative practical task`, after the line beginning `If equivalence is uncertain, use the adaptation for practice and select an assessment task whos…`. Replace the `BD-V-098` marker at EG line 3177.
- Source locator: EG: 3175
- Text–visual link: Distinguishes freedom to adapt practice from the conditions required for certificated evidence.
- Design brief: **Learning activity or approved assessment?.** Branch from intended use into learning/formative practice and formal assessment. Practice may adapt names, roles, medium, timing, and scaffolding while preserving concept, learner action, safety, and key comparison. Formal theory needs the approved competency-aligned interaction and record; practical assessment needs an approved equivalent variant preserving sequence, verification, independence, rubric, safety errors, and record. A missing condition leads to practice and selection of an approved task, not automatic certification. Keep this as educator planning guidance; do not create an approval authority or modify approved tasks. Caption: `An engaging activity becomes assessment only under the approved evidence conditions.` Alt text: `Practice activities allow contextual and access adaptations. Formal theory or practical assessment must preserve the approved evidence, criteria, independence, safety, and record conditions. Uncertain equivalence returns the activity to practice and an approved assessment route.` Master: `Assets/Briefs/bd-v-098-brief.md`.
- Format: Two-branch activity-selection decision diagram; full width.

Use the exact heading and insertion direction in Placement as the target placement. Preserve all listed placements in metadata. Include source-brief revision, reference paths, factual sources, production date, reviewer status, checks, and unresolved judgments in README.md. Set `reviewStatus` to draft or review unless an authorized reviewer has approved it.
```

## Final handoff check

Before marking an item complete, verify that the master is editable rather than raster-only, the final alt text and caption match the asset brief, the output uses the correct guide folder, every stated safety/localization constraint survives the implementation, and no production asset has been uploaded or published without authorization.


---

# Claude cloud handoff prompt

---



---


Use this prompt when handing one Bitcoin Diploma visual to Claude through a cloud conversation. Replace every bracketed field and attach the related files in the marked slots before sending.

```text
You are rebuilding one editable, accessible My First Bitcoin Bitcoin Diploma visual.

Do not publish, upload, merge, or modify the manuscript. Prepare a reviewable draft bundle only.

ASSET
- Asset ID: [BD-V-000]
- Short title: [TITLE]
- Intended guide: [Student Guide | Educator Guide | Shared]
- Exact placement and heading: [PASTE FROM ASSET BRIEF]
- Requested output folder or project location: [CLOUD PROJECT/FOLDER]

ATTACHMENTS — REQUIRED
1. Complete asset brief and section 7 classification record: [ATTACH FILE]
2. Approved transparent PNG reference: [ATTACH FILE]
3. Matching white-background JPG preview: [ATTACH FILE]
4. JSON conformance report: [ATTACH FILE]
5. Exact reference prompt record: [ATTACH FILE]

ATTACHMENTS — ADD WHEN AVAILABLE
6. Relevant adjacent guide excerpt: [ATTACH FILE OR PASTE EXCERPT]
7. Claude Design System authoring instructions: [ATTACH FILE]
8. Closest approved micrographic example: [ATTACH FILE]
9. Current Sanity schema or publishing requirements: [ATTACH FILE]
10. Accessibility, localization, or print requirements: [ATTACH FILE]
11. Factual sources approved for this asset: [ATTACH FILES OR LINKS]
12. Reviewer comments or prior decisions: [ATTACH FILE]

SOURCE-OF-TRUTH ORDER
1. The complete asset brief and section 7 record control teaching intent, required elements, counts, relationships, reading order, strings, safety, factual limits, placement, caption, alt text, and localization.
2. The supplied Claude Design System controls production styling, components, typography, iconography, and tokens.
3. Relevant shared-register entries control reusable actors, props, symbols, interfaces, and notation.
4. The approved PNG and JPG guide composition and visual treatment only. Rebuild them; never trace, embed, or publish them.
5. Adjacent guide text clarifies context but cannot override the asset brief.
6. Supplied schema controls metadata and export fields. Do not invent schema fields or upload endpoints.

If sources conflict, stop and list the exact conflict. If a required fact, URL, value, QR destination, legal statement, or safety condition is missing, leave it unresolved and do not invent a substitute.

IMPLEMENTATION
Rebuild the visual as editable HTML, CSS, and inline SVG. Keep all geometry, labels, arrows, connectors, icons, interface shapes, warnings, and data editable. Do not use the reference image as a background or raster master.

Create:
- micrographic.html with one root `<div class="mg-[SLUG]">`
- micrographic.css with every selector scoped to `.mg-[SLUG]`
- meta.json
- preview.html with a 458px review frame
- alt-text.md with final alt text and a concise text equivalent
- README.md with sources, revision, checks, reviewer status, and unresolved items
- sanity-asset.json only if the supplied schema supports it

Use no JavaScript, external images, external fonts, CSS grid, `vh`, `vw`, `rem`, fixed/sticky positioning, or `@import`. Tag each translatable text element with a unique non-nested `data-t` key. Keep layouts responsive at phone width, desktop width, 458px content width, A4/US Letter, grayscale, and future translation expansion/RTL adaptation.

SAFETY AND CONTENT
- Never include real seed phrases, private keys, payable addresses, private learner data, balances, or transactions.
- Do not invent prices, dates, providers, URLs, legal claims, safety claims, or current facts.
- Use QR codes, addresses, payment values, or named destinations only when the brief supplies and authorizes them and the final values have been verified.
- Preserve every qualification, prohibition, role distinction, and related-asset boundary.
- Do not imply investment returns, guaranteed outcomes, risk-free custody, inevitable adoption, or universal local conclusions.
- Do not turn a named wallet, exchange, service, or local resource into a general recommendation.

REVIEW BEFORE HANDOFF
Check the source brief against the implementation, visible text, reading order, responsive behavior, accessibility, grayscale meaning, print layout, factual accuracy, safety, and localization. Confirm the PNG reference is not embedded or published. Report any deviation, unresolved item, or schema limitation.

RETURN IN THIS ORDER
1. Files created, with cloud links or attachment names.
2. A short implementation summary.
3. Responsive, print, grayscale, accessibility, and factual checks.
4. Unresolved decisions and required human approvals.
5. A statement that nothing was uploaded or published.
```

Before sending, attach the asset-specific files rather than relying on local paths. For the current batch, the three deferred IDs—`BD-V-001`, `BD-V-070`, and `BD-V-075`—must remain deferred. Payment and destination placeholders for `BD-V-036`, `BD-V-078`, and `BD-V-080` must remain unresolved until approved production values are supplied.
