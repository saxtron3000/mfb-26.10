# BD-V-015 design brief

## Source snapshot

- Source capture: complete asset-index record preserved below from `workspace/mfb-bd-workspace/08_assets.md`.
- Brief status: production-ready.
- Source captured: 2026-10-16; brief revision 2026-10-16.
- This brief is the primary authority for later JSON-reference creation after any documented source decisions are resolved. Consult the asset index only to resolve a documented incompleteness or conflict.

```markdown
| `BD-V-015` | Diagram | Pablo | Supporting | 428 | 1165 | Shows where trust, claims, and control sit in a fiat payment system. | Actor-and-flow system map; full width. | Map central bank, commercial bank, government, citizens and businesses, and payment services. Use distinct arrows for money or claims, policy or rules, taxes and spending, and payment instructions. Show that a bank deposit is the bank's liability to the customer. Avoid suggesting that every country has identical institutions or rules. | — |
```

## Asset definition

- Type: Diagram
- Priority: Supporting
- Suggested by: Pablo
- Educational purpose: Shows where trust, claims, and control sit in a fiat payment system.
- Required format: Actor-and-flow system map; full width. Future reference canvas: landscape 16:9, 960 × 540; no image is created in this task.
- Required construction, elements, relationships, reading order, and qualifications: Map central bank, commercial bank, government, citizens and businesses, and payment services. Use distinct arrows for money or claims, policy or rules, taxes and spending, and payment instructions. Show that a bank deposit is the bank's liability to the customer. Avoid suggesting that every country has identical institutions or rules.
- Register note: —
- Production workflow: resolve any source conflicts below, then follow the standard JSON, reference, and production workflow. Keep guide content and anchors until an approved replacement is ready.

## Placement anchor

- Student Guide: exact heading `### [Fiat money](https://programs.myfirstbitcoin.org/lexicon/en/#fiat-money)`; retained source anchor:

```markdown
<!-- VISUAL: BD-V-015
TYPE: Diagram
ALT: Fiat-system map showing participants, claims, rules, taxes, spending, and payment instructions.
ASSET: assets/briefs/bd-v-015-brief.md
-->
```

- Educator Guide: exact heading `### Fiat money and the local system`; retained source anchor:

```markdown
<!-- VISUAL: BD-V-015
TYPE: Diagram
ALT: A fiat-payment map distinguishes central-bank, commercial-bank, government, citizen, business, and payment-service roles, claims, instructions, and dependencies.
ASSET: assets/briefs/bd-v-015-brief.md
USE: Shared Student Guide master.
-->
```

The heading and nearby text above are the placement authority; register line numbers are finders only. Replace a marker only when its approved production asset is ready.

## Detailed visual specification

### Teaching point and learner outcome

Shows where trust, claims, and control sit in a fiat payment system. The learner can trace a simplified fiat payment and identify the difference between a claim, a payment instruction, and institutional rules or public flows.

### Composition and reading order

Pattern: Process flow with grouped actor lanes. Layout skeleton: `teaching-page`, within the guide figure region at the width stated above. Future reference orientation: landscape 16:9, 960 × 540. Preserve reading order and learner-readable type when adapting to the final print region; do not shrink a dense table to fit an arbitrary height.

Use a full-width actor-and-flow diagram, not a geographic map. Arrange five labeled actor areas in a stable hierarchy: central bank at the top, commercial bank and payment services in the middle, citizens and businesses at the bottom, government to one side. Start reading at the actor labels, then trace directly labeled flows. Separate money or claims, policy or rules, taxes and spending, and payment instructions using labels and distinct line treatments as well as color. Show the customer claim and the commercial bank’s matching deposit liability together. Commercial-bank settlement relates to central-bank infrastructure; a payment-service instruction must not appear to create money. Preserve citizens/businesses ↔ bank payment relationships and taxes to government / spending from government as separate directions.

### Content and live text

Live actor labels: central bank; commercial bank; government; citizens and businesses; payment services. Live flow labels: money or claims; policy or rules; taxes; spending; payment instructions. Include bank deposit: bank liability to the customer and exact institutions and rules vary. Use general roles from the adjacent guide, not a new local system. Do not add quantities or a claim that every payment passes through every actor.

All learner-facing titles, labels, cells, values, qualifiers, and warnings must remain editable and translation-ready. Source table links identify terminology references; retain their meaning and do not render Markdown syntax as artwork. No invented final copy or completed local findings are authorized.

In a later SVG/PNG reference, keep a solid white background and leave copy areas clear: no visible letters, numerals, punctuation, placeholder text, or dummy text lines. Keep all required live copy in the brief and later JSON for editable implementation. A text-free reference is not an accessible or publishable substitute for the final labeled asset.

### Accessibility and production handoff

- Alt text: A simplified fiat-payment system separates five participant roles and distinguishes money or claims, rules, taxes and spending, and payment instructions. A customer’s bank deposit is the bank’s liability.
- Editable source: retain separate geometry and live text groups. For a future table, preserve semantic headers, row associations, and editable cells; an image alone cannot replace the accessible text equivalent. Translation must preserve reading order and all qualifications.
- Reference image output: after resolution of any documented source issues, provide `assets/reference/bd-v-015-ref.svg` and a matching `assets/reference/bd-v-015-ref.png`; never a JPG reference.
- Use in colour, grayscale, print, and on a phone: verify the specific relationships and row/stage order above without color; use positional and line/shape distinctions. Keep learner-facing print text at least 12pt. At phone width, preserve each label with its related content and allow wrapping or a clearly ordered stacked equivalent rather than illegible shrink-to-fit. Check contrast, connector continuity, numeric alignment where applicable, and a complete text alternative before any future release.

## Required visual treatment

Selected Tier 3 pattern: Process flow with grouped actor lanes. Selected layout: `teaching-page`; use the stated half-page or full-width region without decorative shared chrome.

Use primary purple `#422C70` for structure and headings, deep purple `#2B1C58` for strong detail, white `#FFFFFF` for reference backgrounds, paper `#F6F6F8` for quiet internal surfaces, cool divider `#D8D8E7` for separators, and body neutral `#25252B` for live text. Orange `#F7941F` marks at most one teaching emphasis and never a dominant field or a safety ranking. Purple/white/paper lead; color never carries meaning alone.

Use live IBM Plex Sans, 400 body and 500 headings/labels, with at most two weights; learner-facing print text is at least 12pt. Keep copy short, literal, left aligned, upright, and translatable. Use flat geometry, restrained monoline outlines, butt caps, and miter joins. Any meaningful structural cut or slant uses exactly 13°; contents remain upright. Do not add a frame or slant merely as decoration. Use directly labeled diagram elements and straight or right-angle connectors. Arrows have open-chevron heads, never filled triangles; junctions use filled node dots. Distinguish different relationship families with labels and line styles as well as color; never depend on a distant legend.

Use diagram primitives or the specified record structure; do not add decorative icons or an unapproved icon library.

No people are required. Do not add cast members, portraits, or character props. The character bible applies only if a later reviewed scope change makes people instructionally necessary.

## Safety, exclusions, and qualifications

- Do not imply a universal institutional arrangement, a central authority approving every payment, or that fiat value comes only from compulsion. Any future local variant needs dated, approved sources; this brief supplies no legal or policy advice.
- Preserve the original purpose, format, priority, description, and guide anchors. Existing tables remain in the guides until their approved replacements are ready. Follow the standard production and placement checks before publication.
- No financial, legal, tax, accounting, compliance, or investment advice; no provider recommendations, guaranteed safety, returns, adoption, or universal local conclusions. Any later local facts require approved, dated source material.
- No real secrets, private keys, seed words, learner identities, personal/payment data, live balances, invoices, or payable destinations. These assets require no functional payment screen or QR. Any later approved fictional payment screen or QR must be nonfunctional and carry live `SAMPLE — DO NOT PAY` wording.
- Keep protocol, wallet, service, user, educator, node, and miner roles distinct when mentioned. Never show bitcoin stored in a wallet, miners making rules, or a single controller of Bitcoin.
- No restricted-pilot app download link, QR panel, installation instruction, or implication that a diagram or self-report certifies competency.
- No crypto hype, gold Bitcoin coins, generic blockchain imagery, corporate-cartoon proportions, gradients, glossy/3D effects, shadows, decorative clutter, third-party icon substitution, or redrawn official MFB marks.

## Source conflicts or unresolved decisions

- None.

## Completion criteria

- The filename, H1, complete source row, guide-marker ID, and production-log path all identify BD-V-015.
- All five actor areas and four flow families are distinguishable without color; bank liability and customer claim remain paired; no geographic map is introduced.
- Preserve all current guide markers and adjacent text; do not insert the proposed visual.
- Use the specified pattern, teaching-page region, purple-led palette, flat 13° geometry where relevant, live text, and instructional alt text.
- Future accessibility review must verify grayscale, print at 12pt or larger, phone reading order, contrast, and complete source-supported content; saving this brief does not claim those visual checks have occurred.
- Carry every source gap or conflict into later review; do not silently complete truncated descriptions, invent a local fact, or remove a safety qualification.
- Follow the standard asset workflow after resolving any source conflicts; record each deliverable only after its file exists.
