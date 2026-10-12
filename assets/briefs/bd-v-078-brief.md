# BD-V-078 design brief

## Source snapshot

- Source capture: complete asset-index record preserved below.
- Brief status: production-ready.
- Source captured: 2026-10-08; brief revision 2026-10-08.
- This brief is the primary authority for later JSON-reference creation. Consult the asset index only to resolve a documented incompleteness or conflict.

```markdown
| `BD-V-078` | Diagram | User | Essential | 1018 |  | Shows how a Lightning invoice carries a payment request and how its readable details relate to the QR code; complements the on-chain address example in `BD-V-036`. | Side-by-side invoice-and-QR diagram with editable labels; full width. | Show a My First Bitcoin test Lightning invoice as a readable payment-request panel on the left and its matching QR code on the right, joined by `Same payment request, two formats`. Include recipient `My First Bitcoin — test`, payment method `Lightning`, confirmed test network, amount with an explicit unit, description, expiry, and the invoice string labelled `Lightning payment request`. Use the invoice string as the… | Show an invoice with its amount, destination, and other payment details beside its matching QR code. |
```

## Asset definition

- Type: Diagram
- Priority: Essential
- Suggested by: User
- Educational purpose: Teach the relationship in the controlling direction: Tablet sample Lightning invoice.
- Required format: Landscape 16:9 reference canvas, 960 × 540; Side-by-side invoice-and-QR diagram with editable labels; full width.
- Required construction, elements, relationships, reading order, and qualifications: Show a tablet displaying a clearly marked sample Lightning invoice: QR code, Lightning symbol, and amount. It must be nonfunctional and labelled `SAMPLE — DO NOT PAY`.
- Register note: Show an invoice with its amount, destination, and other payment details beside its matching QR code.

## Placement anchor

- Student Guide: exact heading `### Addresses`; source anchor:

```markdown
<!-- VISUAL: BD-V-078
ALT: My First Bitcoin test Lightning invoice and matching sample QR code with payment method, amount, recipient, and expiry.
ASSET: assets/briefs/bd-v-078-brief.md
-->
```
- Educator Guide: not applicable

The heading and nearby text above are the placement authority; register line numbers are finders only.

## Detailed visual specification

### Teaching point and learner outcome

Teach the relationship in the controlling direction: Tablet sample Lightning invoice. The learner should be able to explain the specific distinction or sequence: Tablet sample Lightning invoice; Nonfunctional sample QR region; Lightning symbol; Amount and SAMPLE — DO NOT PAY. Preserve the qualifications below when explaining it.

### Composition and reading order

Pattern: Callout. Layout skeleton: teaching-page. Reference topology: tablet. Landscape 16:9 reference canvas, 960 × 540; Side-by-side invoice-and-QR diagram with editable labels; full width.

Tablet centered; QR region prominent, lightning cue separate. All amount, recipient, network, description, expiry and invoice-string fields live; no payable encoding.

Controlling construction: Show a tablet displaying a clearly marked sample Lightning invoice: QR code, Lightning symbol, and amount. It must be nonfunctional and labelled `SAMPLE — DO NOT PAY`.

Reading order: Tablet sample Lightning invoice → Nonfunctional sample QR region → Lightning symbol → Amount and SAMPLE — DO NOT PAY.

### Content and live text

- Editable content requirement 1: Tablet sample Lightning invoice
- Editable content requirement 2: Nonfunctional sample QR region
- Editable content requirement 3: Lightning symbol
- Editable content requirement 4: Amount and SAMPLE — DO NOT PAY
- Authoritative content requirement: Show a tablet displaying a clearly marked sample Lightning invoice: QR code, Lightning symbol, and amount. It must be nonfunctional and labelled `SAMPLE — DO NOT PAY`.
- All labels, data, examples, qualifications and warnings remain editable and translation-ready. Retain source-supported wording; content requirements describe meaning and are not invented final copy.
- Reference-stage suppression: leave copy areas clear; no visible text, numerals, punctuation, placeholder words or data in SVG/PNG. Do not draw dummy text lines as substitute copy.

### Accessibility and production handoff

- Alt text: Tablet sample Lightning invoice; Nonfunctional sample QR region; Lightning symbol; Amount and SAMPLE — DO NOT PAY. Tablet centered; QR region prominent, lightning cue separate. All amount, recipient, network, description, expiry and invoice-string fields live; no payable encoding.
- Editable source: retain separately addressable geometry and live-label regions; later micrographic copy, table cells and data remain editable and translatable. The SVG and PNG are private visual references, not production assets.
- Reference image output: Codex must provide `assets/reference/bd-v-078-ref.svg` and a matching `assets/reference/bd-v-078-ref.png` when the production gate is clear; never JPG.
- Use in colour, grayscale, print, and on a phone: inspect the stated reading order at 960 × 540 and at phone width; distinguish relationships by position, shape or line style as well as colour; retain a white background, generous copy space and live 12pt-or-larger learner text in production. Check that arrows and object silhouettes remain distinguishable without colour.

## Required visual treatment

Selected pattern: Callout. Selected layout: teaching-page; full-width figure region.

Primary purple #422C70 and deep purple #2B1C58 for structure; white #FFFFFF background; paper #F6F6F8 within quiet table/record surfaces; cool divider #D8D8E7 for separators; body neutral #25252B for later live text; orange #F7941F only at one instructional focal point.

Live IBM Plex Sans, 400 body and 500 labels; use 600 only for a single controlled emphasis. Learner-facing print copy at least 12pt. Short literal labels, left aligned and translation-ready; do not bake copy into reference artwork.

Flat shapes, restrained monoline outlines, butt caps and miter joins; straight or right-angle connectors, open chevron heads and filled node dots. Use exactly 13° only for meaningful structural cuts or hatch, never tilt people or labels. No decorative frames.

No people; no character props.

## Safety, exclusions, and qualifications

- No financial, legal, tax, accounting, compliance or investment advice; no provider recommendation, guaranteed safety/returns/adoption or universal local/legal conclusion.
- No real secrets, seed words, private keys, identities, balances, payable addresses, invoices or payment QR data. Fictional payment screens require editable SAMPLE — DO NOT PAY in later production.
- Keep user, educator, wallet, service, node, miner and protocol roles distinct; Bitcoin is not stored inside a wallet, miners do not make the rules, and no single controller approves Bitcoin.
- No restricted-pilot app links, QR assets, calls to download or assessment/certification evidence.
- No crypto hype, gold Bitcoin coins, generic blockchain imagery, corporate-cartoon proportions, gradients, glossy or 3D effects, shadows, decorative clutter, unapproved icons or redrawn official MFB marks.
- Reference only: white background; render no visible text, letters, numerals, punctuation, placeholder text or encoded payment data. Preserve all live copy and warnings in this brief and JSON for later editable implementation.

## Source conflicts or unresolved decisions

- The index’s Dictated production directions control conflicting purpose, construction, format and type. The complete original row above is archival source evidence, not permission to reintroduce superseded scenes. The controlling direction is preserved below.
- The original index row contains a literal ellipsis; it is preserved verbatim. No missing wording is reconstructed. The complete dictated direction controls the reference composition; omitted legacy endings are not invented.
- Dictated nonfunctional sample treatment supersedes the earlier live test-data composition. No address, invoice payload, actual QR encoding or live test data is authorized for this reference. Sample warning and all data fields are editable production content; reference prompt 02 suppresses visible copy.

## Completion criteria

- Preserve the complete BD-V-078 row and apply the controlling direction without restoring superseded construction.
- Include all 4 specified content-bearing elements in the stated composition and reading order.
- Match the exact current guide headings and source anchors; never edit guide content or replace a marker in this workflow.
- Keep each label, qualifier and warning live and translation-ready for later production; include the instructional alt text.
- Check the specific composition in grayscale, print and at phone width; preserve purple-led flat geometry, white reference background and clear negative space.
- Verify that no real secrets, personal/payment data, hype, invented local conclusions or prohibited visible copy enter the references.
- Provide the matching SVG and PNG only after the JSON passes the brief and safety review.
