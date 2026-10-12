# BD-V-032 design brief

## Source snapshot

- Source capture: complete asset-index record preserved below.
- Brief status: production-ready.
- Source captured: 2026-10-08; brief revision 2026-10-08.
- This brief is the primary authority for later JSON-reference creation. Consult the asset index only to resolve a documented incompleteness or conflict.

```markdown
| `BD-V-032` | Diagram | Pablo | Essential | 763 | 1548 | Makes costly-to-produce and easy-to-verify work visible. | Sequential process diagram; full width. | Show candidate block data entering repeated hash attempts; many results miss the target; one result meets it; the miner broadcasts the block; nodes quickly verify proof and all other rules; accepted blocks add accumulated work. Include difficulty adjustment as a small feedback loop. Do not depict mining as solving an externally useful puzzle. | — |
```

## Asset definition

- Type: Diagram
- Priority: Essential
- Suggested by: Pablo
- Educational purpose: Teach the relationship in the controlling direction: Mining hardware finds proof for a candidate block.
- Required format: Landscape 16:9 reference canvas, 960 × 540; Sequential process diagram; full width.
- Required construction, elements, relationships, reading order, and qualifications: Show mining hardware finding a checked block, submitting it to a decentralized network, nodes independently checking it, and the accepted block joining the blockchain. Do not imply miners alone decide validity.
- Register note: —

## Placement anchor

- Student Guide: exact heading `### [Proof of work](https://programs.myfirstbitcoin.org/lexicon/en/#proof-of-work)`; source anchor:

```markdown
<!-- VISUAL: BD-V-032
ALT: Proof-of-work process from candidate block through costly search, quick verification, and broadcast.
ASSET: assets/briefs/bd-v-032-brief.md
-->
```
- Educator Guide: exact heading `### Proof of work`; source anchor:

```markdown
<!-- VISUAL: BD-V-032
ALT: Many computational attempts seek a result below the target; a miner broadcasts a candidate block and nodes verify its work and rules before accepting it.
ASSET: assets/briefs/bd-v-032-brief.md
USE: Shared Student Guide master.
-->
```

The heading and nearby text above are the placement authority; register line numbers are finders only.

## Detailed visual specification

### Teaching point and learner outcome

Teach the relationship in the controlling direction: Mining hardware finds proof for a candidate block. The learner should be able to explain the specific distinction or sequence: Mining hardware finds proof for a candidate block; Block broadcast to peers; Nodes independently check proof and all rules; Accepted block joins history. Preserve the qualifications below when explaining it.

### Composition and reading order

Pattern: Process flow. Layout skeleton: teaching-page. Reference topology: mining. Landscape 16:9 reference canvas, 960 × 540; Sequential process diagram; full width.

Left-to-right four stages; multiple node checks before history. Repeated attempts and difficulty feedback retained as secondary loop; miners do not alone decide validity.

Controlling construction: Show mining hardware finding a checked block, submitting it to a decentralized network, nodes independently checking it, and the accepted block joining the blockchain. Do not imply miners alone decide validity.

Reading order: Mining hardware finds proof for a candidate block → Block broadcast to peers → Nodes independently check proof and all rules → Accepted block joins history.

### Content and live text

- Editable content requirement 1: Mining hardware finds proof for a candidate block
- Editable content requirement 2: Block broadcast to peers
- Editable content requirement 3: Nodes independently check proof and all rules
- Editable content requirement 4: Accepted block joins history
- Authoritative content requirement: Show mining hardware finding a checked block, submitting it to a decentralized network, nodes independently checking it, and the accepted block joining the blockchain. Do not imply miners alone decide validity.
- All labels, data, examples, qualifications and warnings remain editable and translation-ready. Retain source-supported wording; content requirements describe meaning and are not invented final copy.
- Reference-stage suppression: leave copy areas clear; no visible text, numerals, punctuation, placeholder words or data in SVG/PNG. Do not draw dummy text lines as substitute copy.

### Accessibility and production handoff

- Alt text: Mining hardware finds proof for a candidate block; Block broadcast to peers; Nodes independently check proof and all rules; Accepted block joins history. Left-to-right four stages; multiple node checks before history. Repeated attempts and difficulty feedback retained as secondary loop; miners do not alone decide validity.
- Editable source: retain separately addressable geometry and live-label regions; later micrographic copy, table cells and data remain editable and translatable. The SVG and PNG are private visual references, not production assets.
- Reference image output: Codex must provide `assets/reference/bd-v-032-ref.svg` and a matching `assets/reference/bd-v-032-ref.png` when the production gate is clear; never JPG.
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
- Do not depict mining as solving an externally useful puzzle.

## Source conflicts or unresolved decisions

- The index’s Dictated production directions control conflicting purpose, construction, format and type. The complete original row above is archival source evidence, not permission to reintroduce superseded scenes. The controlling direction is preserved below.

## Completion criteria

- Preserve the complete BD-V-032 row and apply the controlling direction without restoring superseded construction.
- Include all 4 specified content-bearing elements in the stated composition and reading order.
- Match the exact current guide headings and source anchors; never edit guide content or replace a marker in this workflow.
- Keep each label, qualifier and warning live and translation-ready for later production; include the instructional alt text.
- Check the specific composition in grayscale, print and at phone width; preserve purple-led flat geometry, white reference background and clear negative space.
- Verify that no real secrets, personal/payment data, hype, invented local conclusions or prohibited visible copy enter the references.
- Provide the matching SVG and PNG only after the JSON passes the brief and safety review.
