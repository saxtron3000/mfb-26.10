# Bitcoin Diploma — Codex reference-image workflow

## Function

Create reviewed working references only, per eligible Bitcoin Diploma asset: transparent PNG + matching white-background JPG + JSON conformance report + exact prompt record. References guide later editable HTML/CSS/inline-SVG production; never publish, upload to Sanity, insert in a guide, or treat as a brand/production asset.

## Inputs

Read before batch: `workspace/08_assets.md`, `workspace/22_openai-reference-image-prompt.md`, `workspace/24_codex-reference-image-prompt-checklist.md`, `workspace/26_codex-reference-image-batch-prompt.md`, `assets/style/STYLE.md`.

Per ID: complete section-3 brief as incorporated by section-7 classification record; relevant section-8 shared-register entries; adjacent guide excerpt only if it clarifies the lesson. The source files, rather than a copied queue here, contain all 101 briefs and checklist states.

Authority: asset brief/section 7 = instructional/structural contract (elements, counts, composition, relationships, reading order, strings, exclusions, safety, localization, caption/alt text, verification, editable-text needs, related-asset boundary, placement). `08_assets.md`/curriculum = instructional truth. Section 8 = reusable definitions; do not merge distinct roles. `assets/style/STYLE.md` = reference visual style. Brief wins over style; record conflict in `unresolved`.

Interpret index fields: `ID` stable; `Suggested by`, historic `Page`/`Note`, and source locator = provenance only; `Priority` = planning only, never lower review; `Placement`, `Text–visual link`, `Design brief`, `Format` = binding. Every ID is independently placeable; never combine adjacent/related assets.

Deferred: `BD-V-001`, `BD-V-070`, `BD-V-075`; do not generate; leave unchecked. `BD-V-001`: retain official CC BY-SA 4.0 mark/text for later production; no redraw, blank substitute, or alternative.

## Process

Run one listed eligible ID at a time, in order; resumable batch; keep completion log. Read its full contract. Carry every section-7 `open` item to `unresolved`; if it blocks required structure, do not generate. Never invent absent facts, labels, numbers, providers, URLs, legal/safety claims, local details, or confirmation-dependent content. Use a neutral text-free structural placeholder only when permitted; flag it.

Create one low-resolution composition, normally landscape 4:3/16:9 unless brief says otherwise:

- PNG: genuine transparent pixels; no checkerboard.
- JPG: composite that exact PNG on `#FFFFFF`; identical dimensions/composition.
- Build exactly specified elements, counts, composition, relationships, reading order; add nothing. Reference conveys spatial arrangement/treatment only. Store future arrows/connectors in JSON, not image.
- Render no text, letters, numerals, placeholder bars, punctuation, logos, URLs, QR codes, captions, warnings, data, arrows, connectors, bubbles, frames, borders, or decorative characters.
- Style: flat, front-on orthographic editorial vector; uniform outline, rounded corners/soft joins, solid fills; purple-led palette with restrained soft violet/white/warm-orange; ample transparent negative space; grayscale legibility via shape/layout/line/position/contrast. No perspective, gradients, shading, shadows, texture/grain, scenery, decorative framing. Shapes only rectangles, rounded rectangles, circles, ellipses, triangles, trapezoids, simple arcs; ≤24 closed shapes/prop, ≤60/person.
- Safety: no real seed/private key/payable address, private learner data/balance/transaction, unverified real QR/URL/address/interface/transaction/price/date/factual datum; no return/guarantee/risk-free/inevitable-adoption/universal-local-or-legal claim; no global recommendation. Preserve qualifications/trade-offs; keep protocol, wallet, service, user, node, miner, educator distinct. Avoid decorative Bitcoin coins, rockets, price charts, wealth claims, cyberpunk.

Special values: `BD-V-036`, `BD-V-078`, `BD-V-080` use text-free structural compositions only; no QR/payment destination; `unresolved`: `TODO AST-001`, `AST-002`, `AST-003` respectively. `BD-V-073` GitHub destination and `BD-V-074` donation destination are later-production-only; never render them in references.

## Outputs and routing

Return/order: 1) PNG, 2) JPG, 3) `<id-lower>-ref.json` code block. JSON is conformance evidence, not image description; it does not replace review.

```json
{
  "assetId": "BD-V-000", "specVersion": 3,
  "canvas": {"aspectRatio": "", "orientation": "landscape | portrait | square", "suggestedWidthPx": 1024, "reference": {"fileName": "bd-v-000-ref.png", "format": "PNG", "background": "transparent"}, "preview": {"fileName": "bd-v-000-ref.jpg", "format": "JPEG", "background": "#FFFFFF"}},
  "placement": [{"elementId": "spec element id", "boundsPercent": {"x": 0, "y": 0, "width": 0, "height": 0}, "zIndex": 1, "treatmentNotes": ""}],
  "conformance": {"elementsRendered": [], "elementsMissing": [], "elementsAdded": [{"description": "", "why": ""}], "compositionFollowed": true, "compositionDeviation": "", "countDeviations": [], "mustNotViolations": [], "textPresentInImage": [], "shapeBudgetEstimate": 0, "pngTransparencyVerified": true, "jpgWhiteBackgroundVerified": true, "exportsMatch": true},
  "unresolved": []
}
```

Working files only: `assets/references/<id>-ref.png|jpg|json`; exact prompt record: `assets/prompts/<id>-ref.txt`; rejected concepts: `assets/rejected/`. Do not place them in `assets/diploma/`. If legacy uppercase `assets/Reference`/`assets/Prompts` instructions conflict, verify repository convention before writing; never silently change extensions/paths.

Prompt record: completed prompt, model/tool, generation/JPG-export settings, date, source-brief revision, review note, block reason if any.

## Test/review

Review both exports against the complete brief. Verify actual PNG transparency (opaque-only alpha fails), solid-white JPG, identical dimensions/composition, no visible prohibited content, clear relationship/reading order, editable-rebuild feasibility, safety, asset-specific conditions, and JSON-to-image match. `textPresentInImage` empty; `elementsAdded` empty or justified; verification flags true only after file inspection.

Reject/regenerate if unclear, noncompliant, unsafe, ambiguous, unjustifiably additive, or not rebuildable. Mark only that source checklist item `[X]` after PNG, JPG, JSON, prompt record all exist and pass; blocked/deferred stay unchecked with exact reason. Before handoff, leave confirmation-dependent factual/QR/address content pending/marked. Final batch report: all 101 IDs as completed/deferred/blocked, paths, unresolved items. Never claim publication.
