# BD-V-014 design brief

## Cancellation record

- Type and status: CANCELED as of 2026-10-16.
- Decision: this asset is not needed because BD-V-015 covers the fiat-system participants.
- The Student Guide marker has been removed; no Educator Guide marker exists. Do not produce, upload, place, or restore this asset.
- The specification below is archived and superseded, including its former type, blocked status, guide anchor, and production instructions. Retain it for history only. The current asset register records the cancellation.

## Archived source snapshot (superseded)

- Source capture: complete asset-index record preserved below from `workspace/mfb-bd-workspace/08_assets.md`.
- Brief status: blocked.
- Source captured: 2026-10-16; brief revision 2026-10-16.
- This brief is the primary authority for later JSON-reference creation after any documented source decisions are resolved. Consult the asset index only to resolve a documented incompleteness or conflict.

```markdown
| `BD-V-014` | Table (Replacement) | AI | Supporting | 433 |  | Clarifies the different roles of central banks, commercial banks, governments, and citizens or businesses. | Participant-and-role reference table; full width. | Preserve the four participant rows and their main roles. Use neutral role icons and editable text. Do not imply that every country has the same institutions, powers, or rules. | — |
```

## Asset definition

- Type: Table (Replacement)
- Priority: Supporting
- Suggested by: AI
- Educational purpose: Clarifies the different roles of central banks, commercial banks, governments, and citizens or businesses.
- Required format: Participant-and-role reference table; full width. Future reference canvas: landscape 16:9, 960 × 540; no image is created in this task.
- Required construction, elements, relationships, reading order, and qualifications: Preserve the four participant rows and their main roles. Use neutral role icons and editable text. Do not imply that every country has the same institutions, powers, or rules.
- Register note: —
- Production workflow: resolve any source conflicts below, then follow the standard JSON, reference, and production workflow. Keep guide content and anchors until an approved replacement is ready.

## Placement anchor

- Student Guide: exact heading `### [Fiat money](https://programs.myfirstbitcoin.org/lexicon/en/#fiat-money)`; retained source anchor:

```markdown
<!-- VISUAL: BD-V-014
TYPE: Table (Replacement)
ALT: Comparison of the main fiat-system participants and their roles.
ASSET: assets/briefs/bd-v-014-brief.md
-->
```

- Educator Guide: not applicable; no placement listed and no current marker.

The heading and nearby text above are the placement authority; register line numbers are finders only. Replace a marker only when its approved production asset is ready.

## Detailed visual specification

### Teaching point and learner outcome

Clarifies the different roles of central banks, commercial banks, governments, and citizens or businesses. The learner can distinguish the main roles of central banks, commercial banks, governments, and citizens or businesses without assuming identical institutions everywhere.

### Composition and reading order

Pattern: Comparison table. Layout skeleton: `teaching-page`, within the guide figure region at the width stated above. Future reference orientation: landscape 16:9, 960 × 540. Preserve reading order and learner-readable type when adapting to the final print region; do not shrink a dense table to fit an arbitrary height.

Use a full-width two-column reference table: Participant and Main role. Preserve four rows in the guide order. Place a small neutral first-party role icon beside each participant without turning it into a person or country stereotype. Read each participant with its associated role, top to bottom. Add a short jurisdiction-variation qualifier beneath the table. Retain the current guide table until its approved replacement is ready.

### Content and live text

Preserve the four complete current role descriptions in the source table below. Keep may act as lender of last resort and usually defines the national unit of account as qualifications, not universal powers. All labels and role text remain editable. Do not insert country-specific institutions, current policy, legal conclusions, or a ranked hierarchy of importance.

Current Student Guide source table (capture preserved verbatim; all text and values stay live in a future implementation):

```markdown
| Participant | Main role |
| --- | --- |
| [Central bank](https://programs.myfirstbitcoin.org/lexicon/en/#central-bank) | Issues base money, manages monetary policy, supports payment settlement, and may act as lender of last resort. |
| Commercial bank | Holds customer deposits, provides payments, and creates [deposit money](https://programs.myfirstbitcoin.org/lexicon/en/#bank-deposit) when it issues loans. |
| Government | Collects taxes, spends, borrows, creates laws, and usually defines the national [unit of account](https://programs.myfirstbitcoin.org/lexicon/en/#unit-of-account). |
| Citizens and businesses | Earn, save, borrow, invest, pay taxes, set [prices](https://programs.myfirstbitcoin.org/lexicon/en/#price), and exchange goods and services. |
```

All learner-facing titles, labels, cells, values, qualifiers, and warnings must remain editable and translation-ready. Source table links identify terminology references; retain their meaning and do not render Markdown syntax as artwork. No invented final copy or completed local findings are authorized.

In a later SVG/PNG reference, keep a solid white background and leave copy areas clear: no visible letters, numerals, punctuation, placeholder text, or dummy text lines. Keep all required live copy in the brief and later JSON for editable implementation. A text-free reference is not an accessible or publishable substitute for the final labeled asset.

### Accessibility and production handoff

- Alt text: Four fiat-system participant groups have different roles: central banking, commercial banking, government, and citizens or businesses. Institutional powers and rules vary by jurisdiction.
- Editable source: retain separate geometry and live text groups. For a future table, preserve semantic headers, row associations, and editable cells; an image alone cannot replace the accessible text equivalent. Translation must preserve reading order and all qualifications.
- Reference image output: after resolution of any documented source issues, provide `assets/reference/bd-v-014-ref.svg` and a matching `assets/reference/bd-v-014-ref.png`; never a JPG reference.
- Use in colour, grayscale, print, and on a phone: verify the specific relationships and row/stage order above without color; use positional and line/shape distinctions. Keep learner-facing print text at least 12pt. At phone width, preserve each label with its related content and allow wrapping or a clearly ordered stacked equivalent rather than illegible shrink-to-fit. Check contrast, connector continuity, numeric alignment where applicable, and a complete text alternative before any future release.

## Required visual treatment

Selected Tier 3 pattern: Comparison table. Selected layout: `teaching-page`; use the stated half-page or full-width region without decorative shared chrome.

Use primary purple `#422C70` for structure and headings, deep purple `#2B1C58` for strong detail, white `#FFFFFF` for reference backgrounds, paper `#F6F6F8` for quiet internal surfaces, cool divider `#D8D8E7` for separators, and body neutral `#25252B` for live text. Orange `#F7941F` marks at most one teaching emphasis and never a dominant field or a safety ranking. Purple/white/paper lead; color never carries meaning alone.

Use live IBM Plex Sans, 400 body and 500 headings/labels, with at most two weights; learner-facing print text is at least 12pt. Keep copy short, literal, left aligned, upright, and translatable. Use flat geometry, restrained monoline outlines, butt caps, and miter joins. Any meaningful structural cut or slant uses exactly 13°; contents remain upright. Do not add a frame or slant merely as decoration. White/paper table ground, purple heading/section label, cool-gray hairlines; left-aligned prose and right-aligned comparable numbers. Keep cells short, preserve source row order, and allow translation wrapping. No heavy borders, colored rating cells, or decorative-icon overload.

Use only approved first-party MFB icons: 24 × 24u canvas, 20 × 20u live area, 2u padding; use the 2.5u print cut, butt caps, miter joins, and hard corners. Icon supply remains an unresolved handoff dependency.

No people are required. Do not add cast members, portraits, or character props. The character bible applies only if a later reviewed scope change makes people instructionally necessary.

## Safety, exclusions, and qualifications

- Do not depict every government as directly controlling every payment or equate bank deposits with physical cash held for each customer.
- Preserve the original purpose, format, priority, description, and guide anchors. Existing tables remain in the guides until their approved replacements are ready. Follow the standard production and placement checks before publication.
- No financial, legal, tax, accounting, compliance, or investment advice; no provider recommendations, guaranteed safety, returns, adoption, or universal local conclusions. Any later local facts require approved, dated source material.
- No real secrets, private keys, seed words, learner identities, personal/payment data, live balances, invoices, or payable destinations. These assets require no functional payment screen or QR. Any later approved fictional payment screen or QR must be nonfunctional and carry live `SAMPLE — DO NOT PAY` wording.
- Keep protocol, wallet, service, user, educator, node, and miner roles distinct when mentioned. Never show bitcoin stored in a wallet, miners making rules, or a single controller of Bitcoin.
- No restricted-pilot app download link, QR panel, installation instruction, or implication that a diagram or self-report certifies competency.
- No crypto hype, gold Bitcoin coins, generic blockchain imagery, corporate-cartoon proportions, gradients, glossy/3D effects, shadows, decorative clutter, third-party icon substitution, or redrawn official MFB marks.

## Source conflicts or unresolved decisions

- The design requires first-party MFB icon cues. No reusable first-party icon set is supplied in assets/style/. Before later production, supply approved icons or obtain a reviewed change to those cues; do not substitute a third-party set or redraw official marks. This does not prevent saving the brief.

## Completion criteria

- The filename, H1, complete source row, guide-marker ID, and production-log path all identify BD-V-014.
- All four participants retain their complete roles and conditional language, with no claim that every country has the same arrangements.
- Preserve the existing guide table and marker; this brief does not replace either.
- Use the specified pattern, teaching-page region, purple-led palette, flat 13° geometry where relevant, live text, and instructional alt text.
- Future accessibility review must verify grayscale, print at 12pt or larger, phone reading order, contrast, and complete source-supported content; saving this brief does not claim those visual checks have occurred.
- Carry every source gap or conflict into later review; do not silently complete truncated descriptions, invent a local fact, or remove a safety qualification.
- Follow the standard asset workflow after resolving any source conflicts; record each deliverable only after its file exists.
