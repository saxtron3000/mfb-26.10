# BD-V-037 design brief

## Source snapshot

- Source capture: complete asset-index record preserved below.
- Brief status: blocked.
- Source captured: 2026-10-08; brief revision 2026-10-08.
- This brief is the primary authority for later JSON-reference creation. Consult the asset index only to resolve a documented incompleteness or conflict.

```markdown
| `BD-V-037` | Diagram | Pablo; User | Essential | 1045 | 1976 | Reinforces the rule “Public receiving information can be shared. Private spending information must remain secret” by showing how public information relates to a secret private key. | One-way key-relationship diagram with a prominent private-key warning and a supporting signing branch; full width. | Show `Private key → Public key → Receiving address`, with the first arrow labelled `Derived from` and the address step labelled `Created from public-key information`. Place the private key inside a clearly marked secret boundary. Add a prominent warning beside it: `Never share your private key. Anyone with it can spend your bitcoin.` Use a warning symbol and readable text so the warning works in grayscale. Label the… | — |
```

## Asset definition

- Type: Diagram
- Priority: Essential
- Suggested by: Pablo; User
- Educational purpose: Reinforces the rule “Public receiving information can be shared. Private spending information must remain secret” by showing how public information relates to a secret private key.
- Required format: Landscape 16:9 reference canvas, 960 × 540; One-way key-relationship diagram with a prominent private-key warning and a supporting signing branch; full width.
- Required construction, elements, relationships, reading order, and qualifications: Show `Private key → Public key → Receiving address`, with the first arrow labelled `Derived from` and the address step labelled `Created from public-key information`. Place the private key inside a clearly marked secret boundary. Add a prominent warning beside it: `Never share your private key. Anyone with it can spend your bitcoin.` Use a warning symbol and readable text so the warning works in grayscale. Label the…
- Register note: —

## Placement anchor

- Student Guide: exact heading `### Keys`; source anchor:

```markdown
<!-- VISUAL: BD-V-037
ALT: Public receiving information (an address or payment request) separated from secret spending information (a private key, seed phrase, password, or recovery code), with signing and verification and a warning never to share secrets.
ASSET: assets/briefs/bd-v-037-brief.md
-->
```
- Educator Guide: exact heading `### Keys and digital authorization`; source anchor:

```markdown
<!-- VISUAL: BD-V-037
ALT: A secret private key relates to public-key and receiving-address information and creates signatures that nodes can verify without learning the private key.
ASSET: assets/briefs/bd-v-037-brief.md
USE: Shared Student Guide master.
-->
```

The heading and nearby text above are the placement authority; register line numbers are finders only.

## Detailed visual specification

### Teaching point and learner outcome

Reinforces the rule “Public receiving information can be shared. Private spending information must remain secret” by showing how public information relates to a secret private key. The learner should be able to explain the specific distinction or sequence: Private key within secret boundary; Public key derived from private key; Receiving address created from public-key information; Private key authorizes signature; Nodes verify signature without receiving secret. Preserve the qualifications below when explaining it.

### Composition and reading order

Pattern: Process flow. Layout skeleton: teaching-page. Reference topology: keys. Landscape 16:9 reference canvas, 960 × 540; One-way key-relationship diagram with a prominent private-key warning and a supporting signing branch; full width.

Main derivation path across top; signing branch down from private key to transaction and verification. Prominent live never-share warning belongs beside secret boundary.

Controlling construction: Show `Private key → Public key → Receiving address`, with the first arrow labelled `Derived from` and the address step labelled `Created from public-key information`. Place the private key inside a clearly marked secret boundary. Add a prominent warning beside it: `Never share your private key. Anyone with it can spend your bitcoin.` Use a warning symbol and readable text so the warning works in grayscale. Label the…

Reading order: Private key within secret boundary → Public key derived from private key → Receiving address created from public-key information → Private key authorizes signature → Nodes verify signature without receiving secret.

### Content and live text

- Editable content requirement 1: Private key within secret boundary
- Editable content requirement 2: Public key derived from private key
- Editable content requirement 3: Receiving address created from public-key information
- Editable content requirement 4: Private key authorizes signature
- Editable content requirement 5: Nodes verify signature without receiving secret
- Authoritative content requirement: Show `Private key → Public key → Receiving address`, with the first arrow labelled `Derived from` and the address step labelled `Created from public-key information`. Place the private key inside a clearly marked secret boundary. Add a prominent warning beside it: `Never share your private key. Anyone with it can spend your bitcoin.` Use a warning symbol and readable text so the warning works in grayscale. Label the…
- All labels, data, examples, qualifications and warnings remain editable and translation-ready. Retain source-supported wording; content requirements describe meaning and are not invented final copy.
- Reference-stage suppression: leave copy areas clear; no visible text, numerals, punctuation, placeholder words or data in SVG/PNG. Do not draw dummy text lines as substitute copy.

### Accessibility and production handoff

- Alt text: Private key within secret boundary; Public key derived from private key; Receiving address created from public-key information; Private key authorizes signature; Nodes verify signature without receiving secret. Main derivation path across top; signing branch down from private key to transaction and verification. Prominent live never-share warning belongs beside secret boundary.
- Editable source: retain separately addressable geometry and live-label regions; later micrographic copy, table cells and data remain editable and translatable. The SVG and PNG are private visual references, not production assets.
- Reference image output: Codex must provide `assets/reference/bd-v-037-ref.svg` and a matching `assets/reference/bd-v-037-ref.png` when the production gate is clear; never JPG.
- Use in colour, grayscale, print, and on a phone: inspect the stated reading order at 960 × 540 and at phone width; distinguish relationships by position, shape or line style as well as colour; retain a white background, generous copy space and live 12pt-or-larger learner text in production. Check that arrows and object silhouettes remain distinguishable without colour.

## Required visual treatment

Selected pattern: Process flow. Selected layout: teaching-page; full-width figure region.

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
- Production restriction: Asset-index description ends at “Label the…” and assets/asset-description.md supplies no completion. The missing labeling requirement must be restored before production.

## Source conflicts or unresolved decisions

- The original index row contains a literal ellipsis; it is preserved verbatim. No missing wording is reconstructed. The missing source ending is identified in the decision record below.
- Asset-index description ends at “Label the…” and assets/asset-description.md supplies no completion. The missing labeling requirement must be restored before production.

## Completion criteria

- Preserve the complete BD-V-037 row and apply the controlling direction without restoring superseded construction.
- Include all 5 specified content-bearing elements in the stated composition and reading order.
- Match the exact current guide headings and source anchors; never edit guide content or replace a marker in this workflow.
- Keep each label, qualifier and warning live and translation-ready for later production; include the instructional alt text.
- Check the specific composition in grayscale, print and at phone width; preserve purple-led flat geometry, white reference background and clear negative space.
- Verify that no real secrets, personal/payment data, hype, invented local conclusions or prohibited visible copy enter the references.
- Keep downstream creation blocked until the decision above is resolved; a complete brief does not authorize the visual.
