# OpenAI reference-image prompt

## Purpose

**Attach** this file to every OpenAI image-generation request for a Bitcoin Diploma asset. Every indexed asset requires a low-resolution JPG reference and a matching conformance report before coded production. The reference is never a publication asset.

The section 7 specification is the contract. It settles element identity and count, composition, relationships, reading order, strings, prohibitions, safety, and localization before generation. The reference image contributes only spatial arrangement and visual treatment. It is not a final Diploma asset and does not authorize publication.

The curriculum text and [08_assets.md](08_assets.md) are the instructional source of truth. The My First Bitcoin visual system is the source of truth for brand and visual decisions.

## Folder routing

ChatGPT creates working reference material only. It must never treat its JPG or JSON as a production asset, place either in `assets/`, or propose a direct manuscript insertion. Store outputs in the ignored local-work area:

```text
assets-work/
├── references/bd-v-000-ref.jpg
├── references/bd-v-000-ref.json
└── prompts/bd-v-000-ref.txt
```

Replace `bd-v-000` with the lowercase stable asset ID. The later Claude implementation belongs in the tracked `assets/diploma/` tree. This separation keeps experiments out of version control and makes approved, editable source reviewable.

## Complete prompt

```text
Create one low-resolution JPG reference image for a My First Bitcoin Bitcoin
Diploma visual. It is a private working reference for a later Claude
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

Render zero text, letters, or numerals anywhere in the image. Do not render
labels, placeholder bars, punctuation, logos, URLs, QR codes, captions,
warnings, data, or decorative characters. Every string belongs only in the
live, translatable coding stage.

Visual construction
Use flat vector artwork on a transparent background. Draw front-on,
orthographic forms with no perspective or depth. Use one uniform outline
weight, butt caps, mitered joins, zero corner rounding, and solid flat fills.
Use no gradients, shading, shadows, texture, or grain. Restrict shapes to
rectangles, circles, ellipses, triangles, trapezoids, and simple arcs. Keep to
a hard budget of 24 closed shapes for each prop and 60 for each person.

Use only these flat colours, with no orange:
- deep purple #2B1C58
- purple #422C70
- mid purple #5E378E
- ink #1A1A24
- paper #F6F6F8
- cool greys #6B6B7B and #D6D6DE
- skin tones #B07A5A, #8A5A3C, and #6E4630

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
1. One JPG reference image.
2. One JSON code block named [asset-id-lowercase]-ref.json. It is a
   conformance report, not a description of the image.

Use this schema:
{
  "assetId": "BD-V-000",
  "specVersion": 1,
  "canvas": {
    "aspectRatio": "",
    "orientation": "landscape | portrait | square",
    "suggestedWidthPx": 1024
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
    "shapeBudgetEstimate": 0
  },
  "unresolved": [
    "anything the specification did not settle that the image had to resolve arbitrarily"
  ]
}
```

## Save and review

Save the JPG as `assets-work/references/bd-v-000-ref.jpg`, its conformance report as `assets-work/references/bd-v-000-ref.json`, and the completed prompt, model or tool, settings, generation date, source-brief revision, and review note as `assets-work/prompts/bd-v-000-ref.txt`. Replace `bd-v-000` with the lowercase stable asset ID.

The report is deliberately smaller than the earlier descriptive schema. Element identity, relationships, reading order, labels, and prohibitions live in the specification, so the report carries only placement, treatment, and deviations. At review, `textPresentInImage` must be empty. `elementsAdded` must be empty or justified.

Self-reported conformance is weak evidence. A model will tend to claim it complied. The report narrows what a human or Claude must check. It does not replace the check.
