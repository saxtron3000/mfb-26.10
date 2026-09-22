# OpenAI reference-image prompt

## Purpose

**Attach** this file to every OpenAI image-generation request for a Bitcoin Diploma asset. Every eligible asset requires a low-resolution transparent PNG reference, a white-background JPG preview of the same image, and a matching conformance report before coded production. The reference and preview are never publication assets.

The current batch contains 101 indexed assets: 98 eligible and three deferred (`BD-V-001`, `BD-V-070`, and `BD-V-075`). Do not generate references for deferred items. `BD-V-001` retains its official licence-mark brief for later production; an AI redraw or an empty reference would not meet that brief.

The section 7 specification is the contract. It settles element identity and count, composition, relationships, reading order, strings, prohibitions, safety, and localization before generation. The reference image contributes only spatial arrangement and visual treatment. It is not a final Diploma asset and does not authorize publication.

The curriculum text and [08_assets.md](08_assets.md) are the instructional source of truth. [27_assets-style.md](27_assets-style.md) is the binding reference-image style authority. If its visual treatment conflicts with an instructional, safety, or structural requirement, the asset brief wins; record the conflict in `unresolved`.

## Folder routing

ChatGPT creates working reference material only. It must never treat its PNG, JPG, or JSON as a production asset, place them in `assets/`, or propose a direct manuscript insertion. Store outputs in the ignored local-work area:

```text
assets-work/
├── references/bd-v-000-ref.png
├── references/bd-v-000-ref.jpg
├── references/bd-v-000-ref.json
└── prompts/bd-v-000-ref.txt
```

Replace `bd-v-000` with the lowercase stable asset ID. The later Claude implementation belongs in the tracked `assets/diploma/` tree. This separation keeps experiments out of version control and makes approved, editable source reviewable.

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

Save the transparent PNG as `assets-work/references/bd-v-000-ref.png`, the white-background JPG preview as `assets-work/references/bd-v-000-ref.jpg`, their conformance report as `assets-work/references/bd-v-000-ref.json`, and the completed prompt, model or tool, settings (including the JPG export), generation date, source-brief revision, and review note as `assets-work/prompts/bd-v-000-ref.txt`. Replace `bd-v-000` with the lowercase stable asset ID.

Review both images against the brief. Verify actual transparent background pixels in the PNG, a solid white background in the JPG, matching dimensions and composition, and no prohibited visible content in either file. Record actual formats and background treatments in `canvas`; set the three export-verification flags to true only after checking the files. An alpha channel containing only opaque pixels does not satisfy transparency. Change a checklist item to `[X]` only after all four files exist and pass review; deferred and blocked items remain unchecked.

The report is deliberately smaller than the earlier descriptive schema. Element identity, relationships, reading order, labels, and prohibitions live in the specification, so the report carries only placement, treatment, and deviations. At review, `textPresentInImage` must be empty. `elementsAdded` must be empty or justified.

Self-reported conformance is weak evidence. A model will tend to claim it complied. The report narrows what a human or Claude must check. It does not replace the check.
