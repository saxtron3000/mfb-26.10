# BD-V-017 design brief

## Source snapshot

- Source capture: complete asset-index record preserved below.
- Brief status: production-ready.
- Source captured: 2026-10-08; brief revision 2026-10-08.
- This brief is the primary authority for later JSON-reference creation. Consult the asset index only to resolve a documented incompleteness or conflict.

```markdown
| `BD-V-017` | Table (Standalone) | Pablo | Essential | 470 | 1203 | Prevents learners from treating liquidity and solvency as the same problem. | Side-by-side balance-sheet comparison; half to full width. | Show two parallel simplified bank snapshots. In the liquidity case, assets exceed liabilities but too little is immediately available. In the solvency case, asset value is below liabilities. Use small round example numbers and label them as fictional. | — |
```

## Asset definition

- Type: Table (Standalone)
- Priority: Essential
- Suggested by: Pablo
- Educational purpose: Teach the relationship in the controlling direction: Liquidity: people queue at bank to withdraw.
- Required format: Landscape 16:9 reference canvas, 960 × 540; Side-by-side balance-sheet comparison; half to full width.
- Required construction, elements, relationships, reading order, and qualifications: Create a side-by-side comparison. For liquidity risk, show people queueing at a bank to withdraw money. For solvency risk, show homes associated with defaulted mortgage payments. Use fictional, non-identifying examples and labels that distinguish the two risks.
- Register note: —

## Placement anchor

- Student Guide: exact heading `### [Fractional reserve banking](https://programs.myfirstbitcoin.org/lexicon/en/#fractional-reserve-banking)`; source anchor:

```markdown
<!-- VISUAL: BD-V-017
ALT: Side-by-side fictional examples distinguishing liquidity risk from solvency risk.
ASSET: assets/briefs/bd-v-017-brief.md
-->
```
- Educator Guide: exact heading `### Fractional-reserve banking, liquidity, and solvency`; source anchor:

```markdown
<!-- VISUAL: BD-V-017
ALT: Two fictional balance sheets distinguish insufficient immediately available funds from assets worth less than obligations.
ASSET: assets/briefs/bd-v-017-brief.md
USE: Shared Student Guide master.
-->
```

The heading and nearby text above are the placement authority; register line numbers are finders only.

## Detailed visual specification

### Teaching point and learner outcome

Teach the relationship in the controlling direction: Liquidity: people queue at bank to withdraw. The learner should be able to explain the specific distinction or sequence: Liquidity: people queue at bank to withdraw; Solvency: homes associated with mortgage defaults. Preserve the qualifications below when explaining it.

### Composition and reading order

Pattern: Comparison pair. Layout skeleton: teaching-page. Reference topology: bank-risk. Landscape 16:9 reference canvas, 960 × 540; Side-by-side balance-sheet comparison; half to full width.

Equal panels: withdrawal access at left; mortgage asset loss at right. Editable risk labels distinguish cash availability from assets below liabilities; no real borrower data.

Controlling construction: Create a side-by-side comparison. For liquidity risk, show people queueing at a bank to withdraw money. For solvency risk, show homes associated with defaulted mortgage payments. Use fictional, non-identifying examples and labels that distinguish the two risks.

Reading order: Liquidity: people queue at bank to withdraw → Solvency: homes associated with mortgage defaults.

### Content and live text

- Editable content requirement 1: Liquidity: people queue at bank to withdraw
- Editable content requirement 2: Solvency: homes associated with mortgage defaults
- Authoritative content requirement: Create a side-by-side comparison. For liquidity risk, show people queueing at a bank to withdraw money. For solvency risk, show homes associated with defaulted mortgage payments. Use fictional, non-identifying examples and labels that distinguish the two risks.
- All labels, data, examples, qualifications and warnings remain editable and translation-ready. Retain source-supported wording; content requirements describe meaning and are not invented final copy.
- Reference-stage suppression: leave copy areas clear; no visible text, numerals, punctuation, placeholder words or data in SVG/PNG. Do not draw dummy text lines as substitute copy.

### Accessibility and production handoff

- Alt text: Liquidity: people queue at bank to withdraw; Solvency: homes associated with mortgage defaults. Equal panels: withdrawal access at left; mortgage asset loss at right. Editable risk labels distinguish cash availability from assets below liabilities; no real borrower data.
- Editable source: retain separately addressable geometry and live-label regions; later micrographic copy, table cells and data remain editable and translatable. The SVG and PNG are private visual references, not production assets.
- Reference image output: Codex must provide `assets/reference/bd-v-017-ref.svg` and a matching `assets/reference/bd-v-017-ref.png` when the production gate is clear; never JPG.
- Use in colour, grayscale, print, and on a phone: inspect the stated reading order at 960 × 540 and at phone width; distinguish relationships by position, shape or line style as well as colour; retain a white background, generous copy space and live 12pt-or-larger learner text in production. Compare all table rows and column boundaries in grayscale; retain the text equivalent.

## Required visual treatment

Selected pattern: Comparison pair. Selected layout: teaching-page; full-width figure region.

Primary purple #422C70 and deep purple #2B1C58 for structure; white #FFFFFF background; paper #F6F6F8 within quiet table/record surfaces; cool divider #D8D8E7 for separators; body neutral #25252B for later live text; orange #F7941F only at one instructional focal point.

Live IBM Plex Sans, 400 body and 500 labels; use 600 only for a single controlled emphasis. Learner-facing print copy at least 12pt. Short literal labels, left aligned and translation-ready; do not bake copy into reference artwork.

Flat shapes, restrained monoline outlines, butt caps and miter joins; straight or right-angle connectors, open chevron heads and filled node dots. Use exactly 13° only for meaningful structural cuts or hatch, never tilt people or labels. No decorative frames. Tables: white/paper ground, purple heading region, cool-gray hairlines, short cells, prose left aligned and comparable numbers right aligned; no decorative-icon overload.

Named approved cast: C01 Sara (educator): dark hair in a high bun, lilac skin, purple blazer and trousers over a white top; calm, capable adult; C02 Luis (beginner learner): backward purple cap, orange-tan skin, white hoodie and purple trousers; attentive adult; C03 Ernesto (older learner): short white hair and beard, rectangular glasses, purple sweater over a white collar, light gray trousers; active and capable; C04 Amina (business owner): long dark hair, deep purple-brown skin, orange jacket over white top and dark trousers; practical adult. Match assets/style/bible/mfb-assets-character-bible.v3.png; use only the purposeful actions and props listed above. These reference poses require review against the fixed cast before production reuse.

## Safety, exclusions, and qualifications

- No financial, legal, tax, accounting, compliance or investment advice; no provider recommendation, guaranteed safety/returns/adoption or universal local/legal conclusion.
- No real secrets, seed words, private keys, identities, balances, payable addresses, invoices or payment QR data. Fictional payment screens require editable SAMPLE — DO NOT PAY in later production.
- Keep user, educator, wallet, service, node, miner and protocol roles distinct; Bitcoin is not stored inside a wallet, miners do not make the rules, and no single controller approves Bitcoin.
- No restricted-pilot app links, QR assets, calls to download or assessment/certification evidence.
- No crypto hype, gold Bitcoin coins, generic blockchain imagery, corporate-cartoon proportions, gradients, glossy or 3D effects, shadows, decorative clutter, unapproved icons or redrawn official MFB marks.
- Reference only: white background; render no visible text, letters, numerals, punctuation, placeholder text or encoded payment data. Preserve all live copy and warnings in this brief and JSON for later editable implementation.

## Source conflicts or unresolved decisions

- The index’s Dictated production directions control conflicting purpose, construction, format and type. The complete original row above is archival source evidence, not permission to reintroduce superseded scenes. The controlling direction is preserved below.

## Completion criteria

- Preserve the complete BD-V-017 row and apply the controlling direction without restoring superseded construction.
- Include all 2 specified content-bearing elements in the stated composition and reading order.
- Match the exact current guide headings and source anchors; never edit guide content or replace a marker in this workflow.
- Keep each label, qualifier and warning live and translation-ready for later production; include the instructional alt text.
- Check the specific composition in grayscale, print and at phone width; preserve purple-led flat geometry, white reference background and clear negative space.
- Verify that no real secrets, personal/payment data, hype, invented local conclusions or prohibited visible copy enter the references.
- Provide the matching SVG and PNG only after the JSON passes the brief and safety review.
