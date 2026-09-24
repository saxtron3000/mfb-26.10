# Bitcoin Diploma Visual–Text Index

## Table of contents

- [Purpose](#purpose)
- [1. Source and placement rules](#1-source-and-placement-rules)
- [2. Shared design requirements](#2-shared-design-requirements)
  - [Instructional function](#instructional-function)
  - [Beginner clarity](#beginner-clarity)
  - [Safety](#safety)
  - [Accessibility, translation, and production](#accessibility-translation-and-production)
- [3. Visual index](#3-visual-index)
  - [Pablo-suggested assets by printed page](#pablo-suggested-assets-by-printed-page)
  - [3.1 Welcome and learning setup](#31-welcome-and-learning-setup)
  - [3.2 Module 1: Understanding Money](#32-module-1-understanding-money)
  - [3.3 Module 2: How Bitcoin Works](#33-module-2-how-bitcoin-works)
  - [3.4 Module 3: Using Bitcoin Safely](#34-module-3-using-bitcoin-safely)
  - [3.5 Module 4: Bitcoin in Your Community](#35-module-4-bitcoin-in-your-community)
  - [3.6 Back of Diploma](#36-back-of-diploma)
  - [3.7 Educator Guide use crosswalk](#37-educator-guide-use-crosswalk)
  - [3.8 Shared assets inserted in the Educator Guide](#38-shared-assets-inserted-in-the-educator-guide)
  - [3.9 Educator-only asset briefs](#39-educator-only-asset-briefs)
- [4. Reuse and combination rules](#4-reuse-and-combination-rules)
- [5. Generation and review handoff](#5-generation-and-review-handoff)
- [6. Intended AI-to-code workflow](#6-intended-ai-to-code-workflow)
  - [Reusable prompt attachments](#reusable-prompt-attachments)
  - [Asset working structure](#asset-working-structure)
  - [Reference-image and coded-asset rules](#reference-image-and-coded-asset-rules)
  - [Brand and visual-direction requirements](#brand-and-visual-direction-requirements)
  - [Extended coded-asset handoff fields](#extended-coded-asset-handoff-fields)
- [7. Reference specifications](#7-reference-specifications)
  - [3.1 Welcome and learning setup](#31-welcome-and-learning-setup-1)
  - [Complete reference classification registry](#complete-reference-classification-registry)
- [8. Shared actor, prop and interface register](#8-shared-actor-prop-and-interface-register)

## Purpose

This document is the index between the written Bitcoin Diploma and the visual explanations that belong inside it.

It identifies:

- which learner concepts and educator processes need a diagram, illustration, timeline, annotated interface, or other explanatory graphic in either guide;
- the exact section and position where each visual belongs;
- what relationship, process, comparison, or mental model the visual must communicate;
- the content and constraints a designer or design model needs to create it;
- which visuals are essential, supporting, or dependent on local or editorial decisions.

This index is intended to become a structured handoff to Claude Design or another design system. A design system should be able to read one entry, create the specified visual, give it the correct filename and alt text, and insert it at the stated anchor in the Diploma.

This file is not:

- an inventory of existing public files;
- a list of visual assets for presentations or the Prague keynote;
- a production-status tracker;
- a rights-management or publication log;
- an index of every table, checklist, worksheet, activity card, or page-layout treatment.

Activity visuals belong on the [Resources Hub](https://programs.myfirstbitcoin.org/resources/). The shared app-download panel `BD-V-076` specifies all four placements across the two guides. The educator-use crosswalk maps the other visuals to relevant teaching guidance. Educator-only visuals are specified in this index and placed in the [Educator Guide](../publish/mfb-bd-26.10/mfb-bd-eg-26.10.md); they do not need a Student Guide placement. Presentation visuals belong with the relevant presentation source. Ordinary tables and forms remain part of the Diploma manuscript unless they require a separate explanatory graphic listed here.

---

## 1. Source and placement rules

The sources of truth are the [Student Guide](../publish/mfb-bd-26.10/mfb-bd-sg-26.10.md) (`SG`) for learner explanations and the [Educator Guide](../publish/mfb-bd-26.10/mfb-bd-eg-26.10.md) (`EG`) for teaching, adaptation, and assessment guidance. Placements in sections 3.1–3.6 are in SG unless explicitly labelled EG. Section 3.8 specifies shared EG insertions; section 3.9 contains educator-only briefs. The educator-use crosswalk maps the original SG assets to teaching guidance; only explicit EG placements and markers specify insertions.

Printed-note page references come from `../feedback/202602721_final_draft_notes.md`, which transcribes the 53 annotated pages in `../feedback/20260715_PABLO_draft_notes.pdf`. The `Page` and `Note` columns refer to those printed PDF page numbers and annotations, not to future Diploma pagination.

Use exact Markdown section headings as the primary anchors. Do not use current page numbers as the main placement method because pagination will change during design and translation.

Line references were checked against both guide manuscripts on 19 September 2026. They are one-based snapshots; recalculate them whenever an edit shifts either manuscript. Exact headings and the described text take precedence over line numbers. Historical `Page` and `Note` fields preserve suggestion provenance; they do not override the current placement or design brief.

Each visual entry provides:

| Field | Meaning |
|---|---|
| ID | Stable identifier used in filenames, alt text, source comments, and review notes. |
| Suggested by | `Pablo` when the asset is directly grounded in a handwritten note; `AI` when the visual asset or its form was inferred through prompting; `User` when directly requested during review. |
| Priority | `Essential`, `Supporting`, or `Conditional`. |
| Type | `Table` for a structured comparison or template; `Diagram` for a relationship, process, map, or timeline; `Image` for an illustrative scene, source image, or interface mockup. |
| Page | Matching printed page number or numbers; `—` means no matching page-specific note was found. |
| Note | Short description of the matching Pablo note; `—` means no matching page-specific note was found. |
| Placement | Exact source heading and position within that section; SG unless explicitly labelled EG. |
| Line | Source line: insert immediately after it, or immediately before it when `Placement` says before. For a table replacement, this is the table header line; replace the whole table while retaining its accessible text equivalent. Multiple placements list every source and line. |
| Text–visual link | The idea or process in the adjacent prose that the visual must make clear for its learner or educator audience. |
| Design brief | What the visual must show and what it must not imply. |
| Format | Recommended visual form and approximate layout role. |
| prompt | AI-ready visual description written as a brief to a graphic designer: the teaching purpose, scene, objects, and relationships the image should show. Styling and production settings remain in the shared guidance. |

The `prompt` column is being trialled with `BD-V-009`; all other asset prompts are intentionally blank.

When inserting a completed visual into the manuscript:

1. Open the specified guide and find the exact heading named in the entry.
2. Find the described paragraph, list, or table within that section.
3. Insert the visual immediately after or before that element as directed.
4. Keep the original explanatory prose unless the entry explicitly says the visual replaces an existing table.
5. Add a Markdown image reference and useful alt text; do not use the filename as alt text.
6. If the anchor text changes, update this index in the same revision.
7. For `BD-V-076`, use exactly two download panels per guide. EG contains two matching markers; SG placements remain the two specified calls to action. Do not add app QR panels elsewhere.
8. EG markers are production comments, not image files. Replace the whole comment when the finished visual exists. During Sanity publication, resolve it to the appropriate uploaded image and alt text; the local path alone does not publish an image.

Recommended source marker:

```markdown
<!-- VISUAL: BD-V-001
SANITY: Required — add the approved official Creative Commons Attribution-ShareAlike 4.0 licence mark here during Sanity production.
ALT: Alt text that communicates the instructional meaning.
-->
```

Replace the marker with a Markdown image reference only after the asset exists. Recommended filenames are `bd-v-001.svg`, `bd-v-002.svg`, and so on. Keep an editable SVG master. Export print and screen versions only during production.

---

## 2. Shared design requirements

These requirements apply to every entry in the index.

### Instructional function

- The visual must explain an idea from the adjacent text. It must not be decorative filler.
- One visual should communicate one primary idea. Related sub-points may support it, but should not compete with it.
- Each asset ID is one independently placeable graphic. Do not combine two self-contained diagrams, scenes, or processes into side-by-side panels under one ID. A comparison, sequence, map, or chart may contain multiple elements only when they work together to explain one relationship and cannot usefully stand alone. When adjacent prose introduces a second relationship, give it a separate asset ID and placement.
- Captions should state what the learner should notice, not merely repeat the title.
- Visuals must preserve nuance and trade-offs. Do not turn qualified text into absolute promotional claims.

### Beginner clarity

- Prefer familiar actors, arrows, sequences, comparisons, and concrete quantities.
- Define or avoid symbols that require technical knowledge.
- Keep protocol, wallet, service, and user roles visually distinct.
- Do not imply that bitcoin is physically stored inside a wallet, that a miner approves Bitcoin's rules, or that a central actor controls the network.

### Safety

- Never display a real seed phrase, private key, payable address, invoice, balance, identity, or transaction associated with a learner.
- Interface examples and QR codes must be clearly marked `SAMPLE — DO NOT PAY` where relevant.
- Do not visually imply guaranteed returns, inevitable adoption, risk-free self-custody, or a universal legal or financial conclusion.
- Locally variable tools, laws, prices, fees, and services must be presented as dated examples, not global facts or endorsements.

### Accessibility, translation, and production

- Design for grayscale printing as well as color. Never use color as the only carrier of meaning.
- Use high contrast, readable type, clear reading order, and patterns or labels that remain visible to color-blind readers.
- Keep text inside graphics short and editable. Avoid idioms, wordplay, flags, and culturally narrow metaphors.
- Prefer vector shapes and live text. Avoid rasterized labels.
- Provide alt text and a text-equivalent explanation for complex diagrams.
- Keep essential detail legible on an A4 or US Letter page and on a phone-width PDF.
- Use the approved My First Bitcoin visual system as the source of truth for brand and visual decisions. The curriculum text and this index remain the source of truth for instructional content.

---

## 3. Visual index

### Pablo-suggested assets by printed page

- Page 1 — `BD-V-001`: Creative Commons Attribution-ShareAlike 4.0 licence mark.
- Page 2 — `BD-V-002`: Critical-thinking checkpoints.
- Page 8 — `BD-V-008`: Functions and properties of money diagram with three function icons.
- Pages 8–9 — `BD-V-009`: Barter and double-coincidence diagram.
- Page 9 — `BD-V-010`: Commonly accepted money separates selling from buying.
- Page 10 — `BD-V-011`: Water-in-context value and price comparison.
- Page 10 — `BD-V-012`: Opportunity cost, time preference, and trade-off illustration.
- Pages 10–11 — `BD-V-013`: Non-linear history of money timeline.
- Page 12 — `BD-V-015`: Fiat-system participant map.
- Page 12 — `BD-V-016`: Bank lending and deposit-money diagram.
- Page 12 — `BD-V-017`: Liquidity-versus-solvency comparison.
- Page 13 — `BD-V-018`: Inflation and purchasing-power graphic.
- Page 18 — `BD-V-025`: Bitcoin origin timeline and source images.
- Page 19 — `BD-V-028`: Bitcoin issuance, supply, and halving chart.
- Page 20 — `BD-V-029`: Bitcoin and satoshi denomination graphic.
- Page 22 — `BD-V-032`: Proof-of-work process diagram.
- Page 23 — `BD-V-033`: Icon-supported Bitcoin-properties table.
- Page 24 — `BD-V-034`: Fiat problems, Bitcoin responses, and trade-offs comparison.
- Page 26 — `BD-V-036`: Bitcoin address and sample QR graphic.
- Page 27 — `BD-V-037`: Private key, public information, and signature diagram.
- Pages 28–30 — `BD-V-043`: Safe wallet recovery workflow.
- Page 29 — `BD-V-042`: Hot, cold, hardware, and custodial wallet comparison.
- Pages 32–33 — `BD-V-046`: Confirmations timeline and block-explorer example.
- Pages 33–34 — `BD-V-047`: Potential-scam red-flag image.
- Pages 33 and 36–37 — `BD-V-050`: On-chain and Lightning comparison.
- Page 35 — `BD-V-048`: Bitcoin acquisition and exchange pathway map.
- Page 35 — `BD-V-049`: Risk-area and questions-to-ask table.
- Page 38 — `BD-V-052`: Self-custody responsibility map.
- Page 40 — `BD-V-056`: Presentation → Practice → Production workshop flow.
- Pages 40 and 48 — `BD-V-066`: Merchant payment operations flow.
- Pages 41–42 — `BD-V-057`: Local Bitcoin tool comparison template.
- Page 43 — `BD-V-060`: Seven daily-life Bitcoin-use icons.
- Page 51 — `BD-V-072`: Final safety reminder.
- Page 52 — `BD-V-073`: Source and contribution QR panel.
- Page 52 — `BD-V-074`: Support-page QR panel (historical suggestion: two payment routes).

### 3.1 Welcome and learning setup

| ID | Suggested by | Priority | Type | Page | Note | Placement | Line | Text–visual link | Design brief | Format | prompt |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `BD-V-001` | Pablo | Supporting | Image | 1 | add the Creative Commons Attribution-ShareAlike 4.0 licence logo in Sanity. | At the Creative Commons Attribution-ShareAlike 4.0 licence statement near the front of `../publish/mfb-bd-26.10/mfb-bd-sg-26.10.md`, immediately after the licence paragraph and before the horizontal rule. | 11 | Gives the open licence a recognisable visual marker while leaving the written licence terms primary. | Use the official Creative Commons BY-SA 4.0 mark at small but legible size. Keep the written licence statement, attribution requirement, and adaptation condition beside or immediately above it. Do not redraw, recolour, distort, or use the logo as a replacement for the licence text or link. | Official licence mark with short text lockup; small inline or corner placement. | |
| `BD-V-002` | Pablo | Supporting | Diagram | 2 | teach a critical-thinking process with scans, tips, or checkpoints. | Under `### What we stand for: accessibility, critical thinking, community, and self-sovereignty`, after the paragraph on examining claims and trade-offs. | 41 | Makes “teach how to think, not what to think” into a repeatable learner action. | Show a six-step loop: identify the claim; separate fact from preference; inspect evidence and source; compare alternatives; name a trade-off or uncertainty; form a provisional conclusion or question. The loop must allow revision rather than ending in certainty. | Horizontal process strip or circular loop; half page. | |
| `BD-V-076` | User | Essential | Image | — | Provide an app-download call to action with a QR code at the introduction and end of both guides only. | SG: after the download call to action under `### Learn more with the [My First Bitcoin App](https://myfirstbitcoin.app/)` and `## Continue learning`. EG: after the download calls under `## About this guide` and `## Continue learning`; replace the two matching markers. All four source lines are listed here. | SG: 51, 1514; EG: 9, 3619 | Gives learners and educators an optional download route at the start and end of each guide. | Reuse one QR panel at exactly these four download calls to action: two per guide. Use `https://myfirstbitcoin.app/` for the QR destination, hyperlink, and readable printed URL. Label the panel Download the [My First Bitcoin App](https://myfirstbitcoin.app/) and state that use is optional. Do not place this app QR elsewhere in either guide or in other publications. Other app mentions remain text hyperlinks. Test the link and printed QR before publication. | Reusable compact download QR panel with a readable URL. | |
| `BD-V-077` | User | Essential | Diagram | — | Add the learning-to-teaching pathway beside the Student Guide paragraph beginning “If you have limited time”. | SG: Under `### How learners can use this course as a starting point`, immediately after the paragraph beginning “If you have limited time”. EG: under `### The pathway from learner to educator`, replace the matching marker after the source text at the listed EG line. See section 3.8 for the exact anchor. | SG: 85; EG: 408 | Shows how the Diploma fits into a wider pathway from first learning to teaching and community participation. | Show [Introduction to Bitcoin](https://myfirstbitcoin.org/learn/programs#intro) → Bitcoin Diploma → [Educator Training Program](https://etp.myfirstbitcoin.org/) → Joining the Bitcoin Education Network. Link the final stage to the [Bitcoin Education Network](https://leaderboard.myfirstbitcoin.org) dashboard in digital versions. Add short labels: `Explore the basics`, `Build a beginner foundation`, `Develop teaching practice`, and `Connect and contribute`. Present this as an optional progression, with direct entry to the Diploma possible. Do not imply that Diploma completion automatically qualifies someone to teach or grants network membership. Align with `### The pathway from learner to educator` in the Educator Guide. | Four-stage pathway diagram with editable text; full width. | |
| `BD-V-006` | AI | Supporting | Diagram | 4 | apply the five-step learning rhythm consistently. | Under `### Flexible learning: in person, online, or through low-tech delivery`, after the five-item list beginning “Learn a key idea”. | 124 | Shows how a learner moves through a typical concept rather than only reading it. | Use the five stages in the current list: `Learn a key idea → Show what you can explain or apply → Apply the idea → Explain in your own words → Review the connection to the next module`. Keep discussion, safe practice, and offline participation available throughout. Do not turn this learning rhythm into an assessment score or imply that self-report proves competency. | Five-step rhythm strip; half to full width. | |
| `BD-V-003` | AI | Essential | Diagram | 6 | clarify the four-module Diploma, educator-curated Modules 3–4, and Advanced boundaries. | SG: Under `### The four-module Diploma, educator-curated Module 4, and Advanced Learning`, after the paragraph beginning “Advanced Learning is outside the Diploma” and before “A topic is not unimportant”. EG: under `### Four-module Diploma and Advanced boundaries`, replace the matching marker after the source text at the listed EG line. See section 3.8 for the exact anchor. | SG: 205; EG: 466 | Clarifies that all four modules are the Diploma, while educators adapt Module 3 practice and curate the required Connect Module 4. | Show all four modules inside a `Diploma: all learners` container, labeled Problem → Solution → Action → Connect. Mark Modules 1–2 as shared core learning, Module 3 as educator-adapted practical learning, and Module 4 as `Connect: educator-curated local learning; required`. Show that Connect applies the earlier learning to a local need and realistic alternative. Show Advanced as a separate onward path. Use arrows to show progression, not a hierarchy of importance. | Layered pathway diagram; full width. | |
| `BD-V-004` | AI | Essential | Diagram | 6–7 | clarify the Problem → Solution → Action → Connect module structure and show timing as adaptable. | Under `### How the 4-module learning path is organized`, immediately before the existing four-row table. | 211 | Gives learners a mental map of the Diploma before they enter Module 1. | Show one connected sequence: `1 Problem: Understanding Money → 2 Solution: How Bitcoin Works → 3 Action: Using Bitcoin Safely → 4 Connect: Bitcoin in Your Community`. Mark Modules 1–3 as shared learning and Module 4 as educator-curated, locally relevant, and required. Show that Connect links the first three stages to a local need, realistic alternative, safe task, and next step. Include each module's guiding question in short editable text. The final module must not be reduced to spending. | Four-stage roadmap; full width. | |
| `BD-V-005` | AI | Supporting | Table | 6–7 | turn the Problem → Solution → Action → Connect learning-path table into a clear visual reference. | Under `### How the 4-module learning path is organized`, replace the existing four-row table visually while retaining an accessible text equivalent. | 211 | Lets learners compare each Diploma module's role, guiding question, and promise at a glance. | Preserve the columns `Module`, `Role`, `Guiding question`, and `Learner promise`. Use four clearly separated, editable rows for Problem: Understanding Money, Solution: How Bitcoin Works, Action: Using Bitcoin Safely, and Connect: Bitcoin in Your Community. Mark Modules 1–3 as shared learning and Module 4 as educator-curated, locally relevant, and required for Diploma completion. | Four-module reference table; full width. | |

### 3.2 Module 1: Understanding Money

| ID | Suggested by | Priority | Type | Page | Note | Placement | Line | Text–visual link | Design brief | Format | prompt |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `BD-V-007` | AI | Supporting | Table | 8 | make the money-properties table easy to scan and compare. | Under `### Functions and properties of money`, replace the existing `Property / Question to ask` table visually while retaining an accessible text equivalent. | 267 | Gives learners a reusable set of questions for assessing whether a form of money is useful. | Preserve durability, portability, divisibility, fungibility, scarcity, acceptability, and verifiability, each paired with its existing question. Add restrained, distinct icons only as supporting cues. Do not score currencies or name a universal winner. | Icon-supported property-question table; full width. | |
| `BD-V-008` | Pablo | Essential | Diagram | 8 | illustrate the functions and properties of money. | SG: Under `### Functions and properties of money`, after the properties table and before “No form of money scores perfectly.” EG: under `### Functions and properties of money`, replace the matching marker after the source text at the listed EG line. See section 3.8 for the exact anchor. | SG: 275; EG: 1032 | Separates what money does from the qualities that make it useful. | Use two linked layers. Layer 1 shows the three functions with small, simple icons: exchange arrows for medium of exchange; a price tag or measuring symbol for unit of account; and a clock with protected value for store of value. Layer 2 shows the seven properties: durability, portability, divisibility, fungibility, scarcity, acceptability, verifiability. Use cash, gold, and a generic digital monetary asset only as examples; do not assign a universal winner or a simplistic total score. | Icon-led two-layer diagram; full width. | |
| `BD-V-009` | Pablo | Essential | Image | 8–9 | add exchange-difficulty examples and a local three-role barter graphic. | SG: Under `### Barter and the double coincidence of wants`, after the Amina, Luis, and Mei scenario and before the formal definition. EG: under `### Barter and the double coincidence of wants`, after the sentence beginning `First, let the group attempt direct exchange`. See section 3.8 for the exact anchor. | SG: 337; EG: 1076 | Makes the failed direct-exchange relationships in the prose visible. | Show Amina with rice wanting shoes, Luis with shoes wanting cooking oil, and Mei with cooking oil wanting repair work. Use broken or unmatched arrows to show why no direct pair satisfies both wants. Keep names and objects editable for localization. Do not show money or a solution in this graphic. Keep this as a single failed-direct-exchange graphic; `BD-V-010` alone shows the money-mediated exchange. | Single three-role barter-mismatch illustration; full width. | Create one illustration that helps a beginner see why a direct barter exchange can fail even when everyone has something useful to offer. Arrange three people from left to right in one shared scene: Amina with an open sack of rice, Luis with a pair of shoes, and Mei with a bottle of cooking oil. Beside each person, clearly distinguish what they have from what they want: Amina has rice and wants shoes; Luis has shoes and wants cooking oil; Mei has cooking oil and wants repair work. Show each wanted item as a separate small visual cue, using a damaged chair with repair tools to represent the repair service Mei needs. Use short “Has” and “Wants” labels to distinguish possessions from needs. Use visibly interrupted exchange arrows between Amina and Luis, and between Luis and Mei, to show that each proposed swap leaves one person’s need unmet. Leave Mei’s repair need visibly unmatched; none of these three people offers that service. Their gestures should suggest an exchange being discussed but not completed, with all goods still beside their owners. The viewer should understand that no pair wants what the other offers in return. Keep names and objects adaptable to local contexts. Do not show money, a completed exchange, or a solution. |
| `BD-V-010` | User | Essential | Diagram | 9 | separate the money-mediated exchange explanation from the barter-mismatch graphic. | SG: Under `### Barter and the double coincidence of wants`, after the paragraph beginning `A commonly accepted money separates selling from buying`. EG: under `### Barter and the double coincidence of wants`, after the sentence beginning `Then introduce a commonly accepted medium`. See section 3.8 for the exact anchor. | SG: 354; EG: 1084 | Shows that a commonly accepted medium lets a person sell to one party and buy from another. | Show Amina selling rice to one person for a generic commonly accepted medium, then using that medium to buy shoes from another person. Use a simple two-step sequence with distinct arrows for selling and buying. Keep names, goods, and the generic medium editable for localization. Do not use a specific currency, price, brand, wallet, QR code, or claim that money removes every exchange problem. | Single money-mediated exchange flow; half to full width. | |
| `BD-V-011` | Pablo | Essential | Image | 10 | compare clean water in two contexts to show context-dependent value and price. | Under `### Scarcity, value, and exchange`, immediately after the sentence “Clean water may be inexpensive near a safe public source and extremely valuable during a shortage.” | 303 | Makes the same good's changing value and price clear through a concrete example. | Use two parallel images of the same quantity of clean water. Panel 1: near a safe public source, readily available, with an illustrative lower-price label. Panel 2: during a shortage, limited access and urgent need, with an illustrative higher-price label. State clearly that availability, need, and circumstances change value and price; do not imply that water scarcity or high prices are ethically acceptable. Keep people, setting, language, and price units editable for localization. | Two-panel contextual-value illustration; half to full width. | |
| `BD-V-012` | Pablo | Supporting | Image | 10 | expand opportunity cost, time preference, and trade-offs with examples and graphics. | SG: Under `### Scarcity, value, and exchange`, after the definitions of opportunity cost, time preference, and trade-off. EG: under `### Scarcity, value, and exchange`, replace the matching marker after the source text at the listed EG line. See section 3.8 for the exact anchor. | SG: 311; EG: 1090 | Connects three abstract choice concepts to one everyday decision. | Show one person choosing between two uses of limited money or time. Label the chosen benefit, the best alternative forgone, the present-versus-future preference, and the resulting trade-off. Do not moralize the learner's choice or imply one time preference is always correct. | Branching choice illustration; half page. | |
| `BD-V-013` | Pablo | Essential | Diagram | 10–11 | add a non-linear money timeline and historical context through modern fiat. | SG: Under `### Beginner monetary history from barter to digital money`, after the `Digital money` paragraph. EG: under `### Beginner monetary history`, replace the matching marker after the source text at the listed EG line. See section 3.8 for the exact anchor. | SG: 332; EG: 1112 | Prevents the history from appearing as one universal, inevitable sequence. | Create several overlapping tracks rather than one straight progress arrow: direct exchange and local records; commodity forms; standard coins; representative paper; bank and government money; modern fiat; digital fiat. Mark that different forms coexist and developed differently across places. Include 1971 only as a dated milestone in the modern-fiat track, not as the origin of all fiat money. | Braided or layered timeline; full-page width. | |
| `BD-V-014` | AI | Supporting | Table | 12 | make the fiat-system participant table clear and easy to compare. | Under `### Fiat money`, replace the existing `Participant / Main role` table visually while retaining an accessible text equivalent. | 344 | Clarifies the different roles of central banks, commercial banks, governments, and citizens or businesses. | Preserve the four participant rows and their main roles. Use neutral role icons and editable text. Do not imply that every country has the same institutions, powers, or rules. | Participant-and-role reference table; full width. | |
| `BD-V-015` | Pablo | Supporting | Diagram | 12 | turn the fiat-participant table into a guided explanation and clarify liabilities. | SG: Under `### Fiat money`, after the participant table. EG: under `### Fiat money and the local system`, replace the matching marker after the source text at the listed EG line. See section 3.8 for the exact anchor. | SG: 349; EG: 1143 | Shows where trust, claims, and control sit in a fiat payment system. | Map central bank, commercial bank, government, citizens and businesses, and payment services. Use distinct arrows for money or claims, policy or rules, taxes and spending, and payment instructions. Show that a bank deposit is the bank's liability to the customer. Avoid suggesting that every country has identical institutions or rules. | Actor-and-flow system map; full width. | |
| `BD-V-016` | Pablo | Essential | Diagram | 12 | explain deposit-money creation, define liability, and diagram fractional-reserve banking. | SG: Under `### Fractional reserve banking`, after the paragraph beginning “When a commercial bank approves a loan” and before the definition of fractional reserve banking. EG: under `### Fractional-reserve banking, liquidity, and solvency`, replace the matching marker after the source text at the listed EG line. See section 3.8 for the exact anchor. | SG: 367; EG: 1168 | Makes deposit creation and the bank balance sheet clear without relying on a misleading money-multiplier story. | Trace a simplified loan: bank approves loan; bank records a loan asset and a matching deposit liability; borrower can transfer the deposit; settlement and liquidity requirements remain. Label assets and liabilities on both sides. State `simplified example; exact rules vary`. Do not show banks lending out the same physical deposit repeatedly. | Numbered balance-sheet flow; full width. | |
| `BD-V-017` | Pablo | Essential | Table | 12 | add liquidity-versus-solvency examples. | SG: Under `### Fractional reserve banking`, after the liquidity-risk and solvency-risk definitions. EG: under `### Fractional-reserve banking, liquidity, and solvency`, replace the matching marker after the source text at the listed EG line. See section 3.8 for the exact anchor. | SG: 376; EG: 1181 | Prevents learners from treating liquidity and solvency as the same problem. | Show two parallel simplified bank snapshots. In the liquidity case, assets exceed liabilities but too little is immediately available. In the solvency case, asset value is below liabilities. Use small round example numbers and label them as fictional. | Side-by-side balance-sheet comparison; half to full width. | |
| `BD-V-018` | Pablo | Essential | Image | 13 | turn inflation and purchasing-power definitions into graphics and local examples. | SG: Under `### Inflation and purchasing power`, after the basket example in the second paragraph. EG: under `### Inflation and purchasing power`, replace the matching marker after the source text at the listed EG line. See section 3.8 for the exact anchor. | SG: 388; EG: 1212 | Shows the inverse relationship between a rising basket price and what a fixed amount of money can buy. | Use the same fixed amount of currency at two dates. At Date A it buys the full basket; at Date B the basket costs more and the fixed amount buys less. Distinguish `price level` from `purchasing power`. Use fictional or sourced-and-dated local values; never mix the two. | Before-and-after quantity illustration; full width. | |
| `BD-V-020` | AI | Supporting | Table | 14–15 | make the alternatives comparison table easy to evaluate without ranking assets. | Under `### Why people look for alternatives`, replace the existing comparison table visually while retaining an accessible text equivalent. | 412 | Helps learners compare why an asset may be chosen alongside its important trade-offs. | Preserve precious metals, real estate, and stocks with columns for `Why people may choose it` and `Important trade-offs`. Add simple, non-promotional icons. Do not add investment advice, price predictions, or a best-choice ranking. | Alternatives trade-off table; full width. | |
| `BD-V-021` | AI | Supporting | Diagram | 14–15 | add local real-estate context and clarify assets versus money. | Under `### Why people look for alternatives`, after the existing comparison table. | 416 | Reinforces that each alternative serves some purposes while introducing different constraints. | Place cash, precious metals, real estate, stocks, and Bitcoin around the needs `daily payment`, `long-term saving`, `portability`, `income or productive use`, and `direct control`. Use qualitative callouts, not a ranked score or investment recommendation. | Trade-off landscape; full width. | |
| `BD-V-019` | AI | Supporting | Table | 14 | add current CBDC examples and explain risks, benefits, privacy, and control. | SG: Under `### Central Bank Digital Currencies (CBDCs)`, after the paragraph beginning “A CBDC does not create a fixed monetary supply” EG: under `### CBDCs as digital fiat`, replace the matching marker after the source text at the listed EG line. See section 3.8 for the exact anchor. | SG: 432; EG: 1280 | Clarifies that digital, centralized, decentralized, private, and scarce are different attributes. | Compare physical cash, commercial-bank digital deposits, a generic retail CBDC, and Bitcoin across issuer or controller, form, access permission, visibility, supply-rule control, and independent verifiability. Mark CBDC features as design-dependent. Do not imply that all CBDCs have identical surveillance or control features. | Layered comparison matrix with icons; full width. | |

### 3.3 Module 2: How Bitcoin Works

| ID | Suggested by | Priority | Type | Page | Note | Placement | Line | Text–visual link | Design brief | Format | prompt |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `BD-V-022` | AI | Essential | Diagram | 16 | make intermediary power and risk concrete and define digital signatures. | SG: Under `### Why Bitcoin was created`, after the paragraph beginning “Bitcoin was created to solve this problem” EG: under `### Why Bitcoin was created`, replace the matching marker after the source text at the listed EG line. See section 3.8 for the exact anchor. | SG: 478; EG: 1412 | Contrasts a central ledger keeper with Bitcoin's distributed verification model. | Left panel: sender and receiver depend on one intermediary that keeps and approves the ledger. Right panel: signed transactions propagate to independent nodes; miners propose blocks; nodes verify the same public rules. Emphasize reduced dependence on a central settlement authority, not removal of all trust. | Two-system comparison diagram; full width. | |
| `BD-V-023` | AI | Supporting | Diagram | 17 | attribute the earlier contributors and ideas on which Bitcoin was built. | Under `### The search for digital and decentralized money`, after the paragraph beginning “Bitcoin was built upon decades of work by many people.” | 494 | Shows that Bitcoin combined prior ideas rather than appearing without context. | Create an idea lineage with DigiCash, Hashcash, Bit Gold, B-money, reusable proof of work, and peer-to-peer file sharing feeding distinct contributions toward Bitcoin. Label contributions carefully; do not imply that every project directly supplied code or that Bitcoin has one intellectual predecessor. | Converging idea timeline; full width. | |
| `BD-V-024` | AI | Essential | Diagram | 17 | format, visually clarify, and fact-check the four-step transaction/miner/node process. | SG: Under `### Early digital-money attempts and the double-spend problem`, after the five numbered features introduced by “The whitepaper brought together the features needed for that approach”. EG: under `### Explain the combined response`, replace the matching marker after the source text at the listed EG line. See section 3.8 for the exact anchor. | SG: 522; EG: 1446 | Explains how a conflicting second spend is resolved without a central database. | Begin with one spendable output and two conflicting payment attempts. Show the five linked features from the text: peer-to-peer announcement; digital signatures; blocks and mining; independent verification; and a shared valid history with the most accumulated proof of work. Show the conflicting second spend rejected. Do not imply that one miner decides validity or that the longest chain is accepted regardless of its validity. | Five-feature conflict-resolution flow; full width. | |
| `BD-V-027` | AI | Supporting | Diagram | 19 | distinguish supply claims, subsidy, and node-enforced issuance facts. | Under `### Digital scarcity and credible scarcity`, after the final paragraph beginning “Scarcity is more credible”. | 532 | Distinguishes a written supply claim from a supply rule independently enforced in practice. | Compare `claim on a website or issuer database` with `public rule checked by many independent nodes`. Show that signatures, transaction history, proof of work, and node verification jointly prevent invalid creation or double spending. Avoid saying that scarcity alone creates value. | Credibility comparison diagram; half to full width. | |
| `BD-V-026` | AI | Essential | Diagram | 19 | clarify decentralization roles, unilateral limits, economic nodes, and trade-offs. | SG: Under `### Decentralization`, after the list of decentralizing features and before the paragraph beginning “Decentralization is not the same as equal influence.” EG: under `### Decentralization and peer-to-peer transfer`, replace the matching marker after the source text at the listed EG line. See section 3.8 for the exact anchor. | SG: 556; EG: 1478 | Makes the distribution and limits of participant power visible. | Place users, nodes, miners, developers, and services around the shared protocol and public ledger. For each, show `can do` and `cannot do unilaterally`. Services must sit outside the protocol boundary. Show unequal influence and points of dependence without adding a central controller. | Roles-and-rules network map; full width. | |
| `BD-V-030` | AI | Supporting | Diagram | 21 | distinguish the Bitcoin network from services and intermediaries. | Under `### Peer-to-peer transfer`, after the paragraph explaining that peer-to-peer does not always mean only two computers communicate. | 572 | Separates direct settlement rules from the communications and service infrastructure a transaction may pass through. | Show sender wallet → network peers → recipient wallet, with optional exchange, hosted wallet, payment service, and internet provider around the path. Use different line styles for transaction propagation, custody, and communications. The presence of network infrastructure must not be mistaken for central approval. | Layered transfer-path diagram; full width. | |
| `BD-V-031` | AI | Essential | Diagram | 21 | clarify users, wallet clients, full nodes, and developer proposals. | SG: Under `### Users, nodes, and miners`, after the paragraph on developers and before “These roles limit one another.” EG: under `### Users, nodes, miners, developers, and services`, replace the matching marker after the source text at the listed EG line. See section 3.8 for the exact anchor. | SG: 590; EG: 1496 | Gives beginners a durable model of who does what in Bitcoin. | Show users signing or accepting transactions; nodes validating and relaying; miners assembling candidate blocks and performing proof of work; developers proposing software; services serving customers. Then show the checks among roles. Do not label all wallet users as nodes or developers as rule-makers. | Participant role map; full width. | |
| `BD-V-032` | Pablo | Essential | Diagram | 22 | demonstrate proof of work and difficulty, and diagram proof of work's purposes. | SG: Under `### Proof of work`, after the paragraph beginning “When a miner finds a valid result” EG: under `### Proof of work`, replace the matching marker after the source text at the listed EG line. See section 3.8 for the exact anchor. | SG: 609; EG: 1526 | Makes costly-to-produce and easy-to-verify work visible. | Show candidate block data entering repeated hash attempts; many results miss the target; one result meets it; the miner broadcasts the block; nodes quickly verify proof and all other rules; accepted blocks add accumulated work. Include difficulty adjustment as a small feedback loop. Do not depict mining as solving an externally useful puzzle. | Sequential process diagram; full width. | |
| `BD-V-028` | Pablo | Essential | Diagram | 19 | add a finite-supply and halving graphic with block-based timing. | SG: Under `### Finite supply`, after the paragraph beginning “The subsidy began at 50 BTC per block”, following the halving table. EG: under `### Finite supply and halving`, replace the matching marker after the source text at the listed EG line. See section 3.8 for the exact anchor. | SG: 635; EG: 1554 | Separates maximum supply, issuance, block subsidy, halving, and miner fees. | Show a descending step chart for block subsidy by halving era and a rising cumulative issuance curve approaching 21 million. Mark halvings by block height or era and `roughly four years`, not guaranteed calendar dates. Show transaction fees separately from new issuance. Include no price curve or adoption prediction. | Paired issuance chart; full width. | |
| `BD-V-029` | Pablo | Essential | Table | 20 | turn the bitcoin-and-sats table into a graphic. | SG: Under `### Satoshis and unit bias`, replace the unit table visually while retaining a text equivalent. EG: under `### Sats and unit bias`, replace the matching marker after the source text at the listed EG line. See section 3.8 for the exact anchor. | SG: 651; EG: 1583 | Makes divisibility intuitive and counters the belief that a learner needs one whole bitcoin. | Start with `1 BTC = 100,000,000 sats`, then zoom into 0.1 BTC, 0.01 BTC, 0.001 BTC, and 1 sat. Show that differently displayed amounts can represent the same value, using `100,000 sats = 0.001 BTC`. Do not show a current fiat price. | Illustrated denomination reference table; half to full width. | |
| `BD-V-033` | Pablo | Essential | Table | 23 | add graphics to explain Bitcoin's properties in plain language. | Under `### Bitcoin as sound digital money`, replace the existing property table visually while retaining an accessible text equivalent. | 673 | Makes each monetary property concrete without treating Bitcoin as universally superior. | Retain a learner-friendly table with one small icon and concise plain-language explanation for each property: durability, portability, divisibility, fungibility, scarcity, verifiability, and acceptability. State the relevant qualification already in the text, especially that acceptance varies and public history can affect how services treat particular funds. Do not turn the properties into a total score or claim that Bitcoin performs every function equally well everywhere. | Icon-supported properties table; full width. | |
| `BD-V-025` | Pablo | Essential | Table | 18 | add images or links for the whitepaper, Genesis Block, first transaction, and Pizza Day. | Under `### Bitcoin origin timeline`, replace the current date/event table visually while retaining an accessible text equivalent. | 731 | Connects the four historical events to why each matters. | Show 31 Oct 2008 whitepaper; 3 Jan 2009 Genesis Block; 12 Jan 2009 first recorded person-to-person transaction; 22 May 2010 Pizza Day. Pair each event with a short significance line. Use document-style illustrations or rights-cleared source images only; avoid portraits or identity speculation for Satoshi. | Illustrated four-milestone reference table; full width. | |
| `BD-V-034` | Pablo | Essential | Table | 24 | add graphics to the Module 2 comparison and make the Module 3 transition explicit. | Under `### Review: how does Bitcoin respond to fiat problems?`, replace the existing `Fiat-system issue / Bitcoin's response / New responsibility or trade-off` table visually while retaining an accessible text equivalent. | 764 | Reconnects the entire Module 2 explanation to the Module 1 problems and the new responsibilities introduced by Bitcoin. | Preserve the three current columns and all five rows: supply policy; intermediary dependence; central ledger control; institutional access; and ordering digital payments. Retain the corresponding responsibilities for rule verification, irreversible errors, privacy, key protection, and mining equipment and energy. Do not label the middle column `perfect solution` or add unsupported promises. | Bridge diagram or visual table; full width. | |

### 3.4 Module 3: Using Bitcoin Safely

| ID | Suggested by | Priority | Type | Page | Note | Placement | Line | Text–visual link | Design brief | Format | prompt |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `BD-V-035` | AI | Essential | Diagram | 25 | clarify that wallets coordinate keys and instructions while bitcoin remains on the ledger. | SG: Under `### Wallets`, after the paragraph explaining that bitcoin is not stored inside the wallet. EG: under `### Wallets are interfaces`, replace the matching marker after the source text at the listed EG line. See section 3.8 for the exact anchor. | SG: 810; EG: 1837 | Corrects the most important beginner wallet misconception. | Show the Bitcoin ledger as the record of spendable outputs; the wallet holding or managing keys and constructing instructions; the user authorizing an action; and the network verifying it. Do not draw coins sitting inside a phone or hardware device. | Conceptual layer diagram; full width. | |
| `BD-V-036` | Pablo; User | Essential | Diagram | 26 | Pablo: add an address/QR graphic, explain who creates addresses, and show address checks. User: show a My First Bitcoin test address as alphanumeric text and its matching QR code. | Under `### Addresses` in the [Student Guide](../publish/mfb-bd-26.10/mfb-bd-sg-26.10.md#addresses), immediately after the opening paragraph beginning “A Bitcoin **address** is public receiving information” and before “If you want to receive an on-chain payment”. | 818 | Shows that the alphanumeric address and QR code represent the same public receiving information; neither is a private key or a recovery phrase. | Show the full My First Bitcoin test address as readable, untruncated text beside a QR code encoding exactly that address, joined by the label `Same address, two formats`. Use [BLANK] for the official test address and [BLANK] for the exact test-network name until My First Bitcoin supplies and approves both values; do not generate a QR until TODO AST-001 is resolved. Do not invent an address or substitute a live donation address. Label `My First Bitcoin test address`, the confirmed test network, and `SAMPLE — DO NOT PAY`. Explain briefly that the wallet creates the receiving address and that the sender checks the decoded destination against the trusted receive screen. Encode only the address, without an amount, URL, or Lightning invoice. Generate the QR from the supplied text and verify that scanning the final print and screen exports returns the identical full address. Keep the QR unobstructed with a clear border. Caption: `Scan or copy: both give the same receiving address. Check the destination before sending.` Alt text: `A My First Bitcoin test address shown as alphanumeric text beside a QR code containing the same address, labelled with its test network and SAMPLE — DO NOT PAY.` Save the editable master as `Assets/Briefs/bd-v-036-brief.md`. | Side-by-side text-to-QR diagram with editable labels; half to full width. | |
| `BD-V-078` | User | Essential | Diagram | — | Show an invoice with its amount, destination, and other payment details beside its matching QR code. | Under `### Addresses` in the [Student Guide](../publish/mfb-bd-26.10/mfb-bd-sg-26.10.md#addresses), immediately after the paragraph beginning “For every payment request, confirm the intended payment method” and before “When a payment matters”. | 822 | Shows how a Lightning invoice carries a payment request and how its readable details relate to the QR code; complements the on-chain address example in `BD-V-036`. | Show a My First Bitcoin test Lightning invoice as a readable payment-request panel on the left and its matching QR code on the right, joined by `Same payment request, two formats`. Include recipient `My First Bitcoin — test`, payment method `Lightning`, confirmed test network, amount with an explicit unit, description, expiry, and the invoice string labelled `Lightning payment request`. Use the invoice string as the destination to scan or copy; do not label it as an on-chain address or imply that a Lightning invoice requires one. Distinguish the recipient display label from the encoded invoice details; a familiar name alone does not verify the recipient. Use [BLANK] for the official test invoice, network, amount, description, and expiry until My First Bitcoin supplies and approves them; do not generate a QR until TODO AST-002 is resolved. Mark `SAMPLE — DO NOT PAY`; explain that this is a fixed teaching example and may be expired. Encode the complete supplied invoice in the QR, not an address or a summary of the displayed fields. Verify that scanning the final print and screen exports returns the identical invoice and that a compatible test wallet displays matching payment details. Keep the QR unobstructed with a clear border, and keep the complete invoice available as selectable text. Do not show private keys, recovery phrases, or a live donation request. Caption: `Check the payment method, recipient, amount, and expiry after scanning.` Alt text: `A My First Bitcoin test Lightning invoice with its recipient, network, amount, description, expiry, and payment-request text beside a QR code encoding the same invoice, marked SAMPLE — DO NOT PAY.` Save the editable master as `Assets/Briefs/bd-v-078-brief.md`. | Side-by-side invoice-and-QR diagram with editable labels; full width. | |
| `BD-V-037` | Pablo; User | Essential | Diagram | 27 | Pablo: add a public/private-key image and optional physical teaching tool. User: place a public/private-key relationship diagram after this section with an explicit warning never to share a private key. | SG: At the end of `### Keys` in the [Student Guide](../publish/mfb-bd-26.10/mfb-bd-sg-26.10.md#keys), after the `Try it` sorting prompt and immediately before `### Seed phrases`. EG: under `### Keys and digital authorization`, replace the matching marker after the source text at the listed EG line. See section 3.8 for the exact anchor. | SG: 844; EG: 1954 | Reinforces the rule “Public receiving information can be shared. Private spending information must remain secret” by showing how public information relates to a secret private key. | Show `Private key → Public key → Receiving address`, with the first arrow labelled `Derived from` and the address step labelled `Created from public-key information`. Place the private key inside a clearly marked secret boundary. Add a prominent warning beside it: `Never share your private key. Anyone with it can spend your bitcoin.` Use a warning symbol and readable text so the warning works in grayscale. Label the receiving address `Public receiving information`. Add a small signing branch: the private key creates a digital signature; nodes use the public key to verify it without seeing the private key. Keep the private key inside the secret boundary throughout. Do not imply that a public key or address can reveal the private key, that an address and public key are identical, or that a signature contains the private key. Use conceptual symbols only, never real or realistic private-key strings, recovery phrases, or scannable secrets. Caption: `Public information supports receiving and verification. The private key authorizes spending and must stay secret.` Alt text: `A private key kept inside a secret boundary derives a public key, from which receiving-address information is created. A separate branch shows signing and public verification without revealing the private key. Warning: never share your private key; anyone with it can spend your bitcoin.` Save the editable master as `Assets/Briefs/bd-v-037-brief.md`. | One-way key-relationship diagram with a prominent private-key warning and a supporting signing branch; full width. | |
| `BD-V-038` | AI | Essential | Diagram | 27 and 30 | show recovery language without implying every wallet uses an identical method. | SG: Under `### Seed phrases`, after the explanation of what a seed phrase does. EG: under `### Seed phrases and recovery`, replace the matching marker after the source text at the listed EG line. See section 3.8 for the exact anchor. | SG: 850; EG: 1972 | Places the seed phrase correctly in the recovery chain without teaching that every wallet uses an identical recovery method. | Show seed or wallet backup → wallet recreates keys → expected addresses and transaction access return. Mark the backup as secret and offline. Add `method and compatibility depend on the wallet`. Do not show actual words, screenshots of recovery entry, or educator access. | Recovery relationship diagram; half to full width. | |
| `BD-V-079` | User | Essential | Image | — | Show a 12-word seed phrase being copied onto paper after the seed-phrase section. | At the end of `### Seed phrases` in the [Student Guide](../publish/mfb-bd-26.10/mfb-bd-sg-26.10.md#seed-phrases), immediately after the paragraph beginning “Some wallets use additional passphrases” and before `### Custodial and non-custodial use`. | 861 | Makes writing a private, offline backup concrete and reinforces preserving word order and spelling. Complements the recovery relationship in `BD-V-038`. | Show one person privately copying a 12-word seed phrase from a generic wallet backup screen onto paper with a pen. Show twelve clearly numbered positions on both screen and paper, in the same reading order, using matching placeholders `WORD 01` through `WORD 12` rather than an actual recovery phrase. Depict the hand completing the final entry; use a simple directional cue from screen to paper and a callout `Check every word and its number`. Label the illustration `EXAMPLE ONLY — NOT A VALID RECOVERY PHRASE`. Add a prominent warning: `Never share your seed phrase. Never photograph it or save it online.` Show no camera, cloud backup, messaging, website entry, or second person viewing the phrase. Use a generic interface without wallet branding. Note `12-word example; follow your wallet’s backup instructions` so the illustration does not imply that all wallets use twelve words. Caption: `Copy each word in order onto paper. Check it privately and store it securely offline.` Alt text: `A person uses a pen to copy twelve numbered placeholder words from a wallet backup screen onto paper in the same order. Labels remind the learner to check every word, keep the backup offline, and never share or photograph a seed phrase. The example is not a valid recovery phrase.` Save the editable master as `Assets/Briefs/bd-v-079-brief.md`. | Screen-to-paper illustration with numbered placeholders, editable labels, and a prominent safety warning; half to full width. | |
| `BD-V-039` | AI | Essential | Diagram | 26 and 29 | compare custody choices and custodial versus self-custodial wallet control. | SG: Under `### Custodial and non-custodial use`, after the custody explanation. EG: under `### Custodial and self-custodial use`, replace the matching marker after the source text at the listed EG line. See section 3.8 for the exact anchor. | SG: 869; EG: 2031 | Makes custody a question of key control rather than interface appearance. | Left: user logs into a service; service controls keys and authorizes withdrawal. Right: user controls keys; wallet signs under the user's authority; network checks the transaction. Show recovery responsibility and failure point in both paths. Avoid portraying self-custody as morally superior or risk free. | Side-by-side custody model; full width. | |
| `BD-V-040` | AI | Supporting | Table | 29 | provide a custodial-versus-self-custodial reference. | Under `### Custodial and non-custodial use`, replace the existing `Question / Custodial use / Self-custodial use` table visually while retaining an accessible text equivalent. | 871 | Makes key control, recovery, and failure points comparable without moralising either model. | Preserve the current rows `Who holds the keys?`, `Who handles recovery?`, and `Main trade-off`, with the custodial and self-custodial explanations. Use neutral icons and editable text. Do not add a recommendation badge or treat either model as risk free. | Custody comparison table; full width. | |
| `BD-V-042` | Pablo | Supporting | Diagram | 29 | add a graphic comparing hot, hardware/cold, and custodial wallets or accounts. | SG: Under `### Hot and cold wallets`, after the introductory explanation. EG: under `### Hot, cold, hardware, and custodial are different dimensions`, replace the matching marker after the source text at the listed EG line. See section 3.8 for the exact anchor. | SG: 885; EG: 2048 | Connects wallet type to exposure and use rather than treating `hot`, `cold`, and `custodial` as one scale. | Use two axes or layers: key control (`custodial` versus `self-custodial`) and connectivity or signing environment (`hot` versus `cold or hardware`). Place common use patterns and threat examples in the correct areas. Explicitly show that a custodial account is not a type of self-custodial wallet. | Two-axis classification graphic; full width. | |
| `BD-V-041` | AI | Supporting | Table | 29 | make hot, cold, hardware, and custody distinctions easy to scan. | Under `### Hot and cold wallets`, replace the existing `Arrangement / Common strength / Responsibility to remember` table visually while retaining an accessible text equivalent. | 887 | Prevents learners from treating custody and connectivity as one scale. | Preserve the current columns and the rows for hot wallet, hardware or cold wallet, and custodial account. Distinguish key control from signing environment; use the qualifications in `BD-V-042` to prevent treating custody and connectivity as one scale. Preserve one common strength and one responsibility for each arrangement. | Wallet-use comparison table; full width. | |
| `BD-V-043` | Pablo | Essential | Diagram | 28–30 | add a visual recovery-readiness activity and keep practice private and low risk. | Under `### Wallet recovery and seed phrase testing`, after the six numbered recovery-readiness steps and before “The point is not to make recovery feel easy”. | 908 | Turns the recovery text into a safe sequence a learner can rehearse. | Follow the six current steps: use official instructions for the exact training wallet; confirm compatibility; work privately; use the approved backup-check or recovery method; confirm expected receiving information or training history; reset or clear the temporary environment. Use only prepared, empty, or simulated materials. Put `educator never sees the secret` outside every step. Do not instruct learners to erase a wallet before verifying its backup or introduce real funds. | Safety-gated workflow; full width. | |
| `BD-V-044` | AI | Essential | Image | 31 | add a visual receiving activity and receive-screen competency exercise without real funds. | SG: Under `### Receiving bitcoin`, after the receive steps. EG: under `### Receiving bitcoin`, replace the matching marker after the source text at the listed EG line. See section 3.8 for the exact anchor. | SG: 922; EG: 2072 | Lets a learner identify the elements of a receive request before live practice. | Show receiver device, sample address or QR, sender verification, broadcast or pending status, and confirmation. Annotate amount, unit, network, address, and status. Use fictional data and mark the whole visual non-payable. | Annotated receiving flow; full width. | |
| `BD-V-045` | AI | Essential | Diagram | 32 | make sending, address, and network checks visual and explain how to perform them. | SG: Under `### Sending bitcoin`, after the pre-send steps. EG: under `### Sending bitcoin`, replace the matching marker after the source text at the listed EG line. See section 3.8 for the exact anchor. | SG: 937; EG: 2106 | Makes verification happen before approval and separates recipient checks from fee and timing decisions. | Show independently verified recipient and purpose → payment method → scan or copy and compare destination → check amount, unit, fee or expiry, and final summary → small test when unfamiliar → approve only if all checks match → check the result. Branch to stop and verify if anything differs. For on-chain payments, show pending/confirmation status and a sample txid; for Lightning, show success or failure without implying an on-chain txid for each payment. Mark approval as the point after which a valid payment is usually irreversible. | Preflight-to-settlement flow; full width. | |
| `BD-V-046` | Pablo | Essential | Diagram | 32–33 | add a *txid*/explorer activity and explain first confirmation, block depth, and privacy. | SG: Under `### Verification, block explorers, and irreversible transactions`, after the confirmation explanation. EG: under `### Block explorers and verification`, replace the matching marker after the source text at the listed EG line. See section 3.8 for the exact anchor. | SG: 947; EG: 2153 | Connects transaction status, block inclusion, and later confirmations. | Show a transaction first in the pending pool, then included in Block N as confirmation 1, followed by Blocks N+1, N+2, and N+3 increasing depth. Pair it with a small annotated fictional explorer panel showing *txid*, amount, fee, status, and confirmations. Add a privacy callout about searching personal data. | Confirmation timeline plus explorer inset; full width. | |
| `BD-V-047` | Pablo | Supporting | Image | 33–34 | add a red-flag image for a potential scam. | SG: Under `### Safety checklist`, before the red-flag examples. EG: under `### Scam recognition and safe response`, replace the matching marker after the source text at the listed EG line. See section 3.8 for the exact anchor. | SG: 955; EG: 2187 | Gives learners an immediate visual cue to pause when a message or offer shows scam signals. | Show a prominent red flag beside a generic, nonfunctional message or offer. Add concise warning cues for impersonation, urgency, guaranteed returns, giveaway or recovery requests, fake applications, phishing, relationship manipulation, and too-good-to-be-true claims. Include the action `stop, verify independently, and never share a seed phrase or private key`. Do not use a real brand, address, payment request, or a realistic phishing link. | Red-flag scam-warning illustration; half width. | |
| `BD-V-048` | Pablo | Supporting | Diagram | 35 | turn acquisition/exchange pathways into a one-page comparison activity. | SG: Under `### Acquiring and exchanging bitcoin`, after `#### Awareness, not financial advice` and the pathway overview, and before the comparison questions. EG: under `### Acquiring and exchanging: awareness, not financial advice`, replace the matching marker after the source text at the listed EG line. See section 3.8 for the exact anchor. | SG: 971; EG: 2229 | Shows that acquiring bitcoin is an end-to-end route with risks before and after the moment of exchange. | Map earning, peer-to-peer, exchange or broker, ATM or kiosk, and merchant or community receipt as separate paths into either self-custody or custodial balance. Label price or spread, fees, identity, reversibility, counterparty, withdrawal, and local-law checkpoints. Do not rank or recommend a provider. | Branching pathway map; full width. | |
| `BD-V-049` | Pablo | Essential | Table | 35 | make the acquisition-pathway questions practical and easy to scan. | Under `### Acquiring and exchanging bitcoin`, replace the existing `Risk area / Question to ask` table visually while retaining an accessible text equivalent. | 975 | Helps learners assess a complete acquisition or exchange route instead of focusing only on price. | Preserve the six existing risk-area rows and their questions: costs; custody; identity and privacy; withdrawal and settlement; counterparty and safety; local context. Keep each question editable, neutral, and locally verifiable. Include no provider names, rankings, or legal conclusions. | Icon-supported risk-check table; full width. | |
| `BD-V-050` | Pablo | Essential | Diagram | 33 and 36–37 | distinguish destinations, add examples and trade-offs, and route deeper mechanics to Advanced. | SG: Under `### On-chain and Lightning payments`, after the introductory comparison. EG: under `### On-chain and Lightning payments`, replace the matching marker after the source text at the listed EG line. See section 3.8 for the exact anchor. | SG: 988; EG: 2253 | Makes the layer relationship and appropriate-use distinction visible. | Show Bitcoin base-layer settlement beneath Lightning payment channels. Compare payment request, route, timing, fee conditions, custody variability, and failure modes. Use one small-payment and one final-settlement example. Do not imply that Lightning is a separate coin or that all Lightning wallets are self-custodial. | Layer diagram plus concise comparison; full width. | |
| `BD-V-051` | AI | Supporting | Table | 33 and 36–37 | provide an on-chain-versus-Lightning learner reference. | Under `### On-chain and Lightning payments`, replace the existing `Question / On-chain Bitcoin / Lightning` table visually while retaining an accessible text equivalent. | 990 | Lets learners compare payment requests, settlement, timing, fees, typical use, and introductory risks across the two paths. | Preserve the four current rows: receiving information, payment result, common use, and beginner checks. Keep invoice, offer, and supported Lightning-address wording, plus expiry and payment-result checks. Retain custody and fee qualifications from the adjacent prose. Do not imply that Lightning is a separate coin or that either path is universally better. | Payment-path comparison table; full width. | |
| `BD-V-052` | Pablo | Supporting | Diagram | 38 | clarify the responsibility map and turn it into an educator-guided exercise. | Under `### Review: what does self-custody responsibility mean?`, immediately before `#### Key takeaways`. | 1011 | Synthesizes the module as responsibilities surrounding key control. | Put `control of keys` in the center, surrounded by backup, recovery, receiving, sending, tool choice, acquisition path, privacy, and scam checks. For each, show the protected item and the consequence of failure in very short text. | Responsibility map; full width. | |
| `BD-V-053` | AI | Supporting | Table | 38 | make the responsibility map usable as a structured learner reference. | Under `### Review: what does self-custody responsibility mean?`, immediately before `#### Key takeaways`, as a text-equivalent alternative to `BD-V-052`, not an additional recap. | 1011 | Connects each task with what must be protected or checked and the consequence of failure. | Use rows for backup, receiving, sending, custody, tool choice, and acquisition. Keep language practical and non-alarmist. | Responsibility reference table; full width. | |

### 3.5 Module 4: Bitcoin in Your Community

| ID | Suggested by | Priority | Type | Page | Note | Placement | Line | Text–visual link | Design brief | Format | prompt |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `BD-V-055` | AI | Supporting | Table | 38–39 | provide a clear editable record of the learner's Module 4 focus. | Under `## Module 4: Bitcoin in Your Community`, replace the existing `Local learning choice / Your notes` table visually while retaining an accessible text equivalent. | 1034 | Gives learners one place to record the module, local problem, tool or scenario, benefit, risk, evidence, and safe next step. | Preserve all seven local-learning-choice prompts and a generous editable notes column. Make it printable and reusable by different educators. Do not pre-fill a local tool, provider, or conclusion. | Editable Module 4 record table; full width. | |
| `BD-V-054` | AI | Essential | Diagram | 38–39 | define MFB versus educator responsibilities in the educator-curated Connect module. | Under `### Your local Module 4`, after the four-item list beginning “Connect” and ending “Explain”. | 1057 | Connects the four learner actions to local purpose, educator support, and safe choice. | Show the four learner actions `Connect → Compare → Practise safely → Explain`. Link shared earlier learning to a local need and realistic alternative, educator-selected safe practice, and a responsible next step. Show the educator and, where needed, a local expert supporting the learner. Keep required competencies and safety boundaries fixed. Detailed educator planning and verification remain in the Educator Guide. | Four-stage local-learning diagram; full width. | |
| `BD-V-056` | Pablo | Supporting | Diagram | 40 | create a clear Presentation → Practice → Production flow for practical workshops and demonstrations. | SG: Under `### Practical workshops and demonstrations`, after the definitions of Presentation, Practice, and Production. EG: under `### Use Presentation → Practice → Production`, replace the matching marker after the source text at the listed EG line. See section 3.8 for the exact anchor. | SG: 1072; EG: 861 | Shows how a safe practical skill develops from educator explanation to guided learner practice and then independent performance or explanation. | Create three connected sections in a clear left-to-right or top-to-bottom sequence: `Presentation` — educator shows the full process and explains purpose, terms, and risks; `Practice` — learner follows a guided process using printed screens, a test environment, or a very small amount; `Production` — learner completes a defined task or explains a decision independently. Add simple safety cues for no funds, test funds, or tiny value, plus an offline alternative at every stage. | Three-stage PPP flow diagram; full width. | |
| `BD-V-057` | Pablo | Supporting | Table | 41–42 | create a reusable local-tool comparison and place local-tool guidance in the Module 4 Educator Guide. | Under `### Local Bitcoin tools and resources`, replace the existing `Area / What to verify` table visually while retaining an accessible text equivalent. | 1103 | Helps learners see that an interface belongs to a custody, network, and support context. | Preserve purpose, custody, source, code, recovery, privacy, cost, compatibility, support, and law as editable rows with a `What to verify` column. Record the date checked. Do not show an approved-products badge or a globally recommended wallet. | Local tool evaluation table; full width. | |
| `BD-V-058` | AI | Supporting | Table | 41–42 | provide a structured, reusable record for documenting a locally used Bitcoin tool. | Under `### Local Bitcoin tools and resources`, replace the existing `Local tool record` table visually while retaining an accessible text equivalent. | 1120 | Helps learners record what was checked about a tool without treating it as a global recommendation. | Preserve the rows for tool and version, date checked, custody model, main use, benefit, risk, recovery method, and alternative. Keep all fields editable and date-stamped. Do not use an endorsement badge or provider ranking. | Editable local-tool record table; full width. | |
| `BD-V-080` | User | Essential | Diagram | — | Show a Lightning address such as `donate@myfirstbitcoin.org` beside its matching QR code. | Under `### Lightning payments where locally appropriate` in the [Student Guide](../publish/mfb-bd-26.10/mfb-bd-sg-26.10.md#lightning-payments-where-locally-appropriate), immediately after the paragraph beginning “A **Lightning address** is a human-readable identifier” and before “For a guided payment”. | 1148 | Connects an email-like Lightning address with its scannable payment destination, while distinguishing it from an email account, an on-chain address, and a specific Lightning invoice. | Show the full Lightning address as readable, selectable text beside a QR code for the same destination, joined by `Same Lightning address, two formats`. Use [BLANK] for the Lightning address until My First Bitcoin supplies and approves an active, controlled destination; do not publish a working QR until TODO AST-003 is resolved. Generate a wallet-compatible Lightning QR for the confirmed address, not a `mailto:` link, website link, on-chain address, or fixed invoice. Label `Lightning address` and `SAMPLE — DO NOT PAY`. Do not preset an amount or turn this teaching illustration into a donation call to action; the optional support panel is `BD-V-074`. Verify that scanning the final print and screen exports in a compatible Lightning wallet resolves to the confirmed recipient and allows the payment details to be reviewed before approval. Keep the QR unobstructed with a clear border. Caption: `This looks like an email address, but it is used to request a Lightning payment. Check the recipient and payment details before paying.` Alt text: `A confirmed My First Bitcoin Lightning address shown as readable text beside a QR code for the same payment destination, labelled Lightning address and SAMPLE — DO NOT PAY.` Replace the generic address description in the final alt text with the confirmed address. Save the editable master as `Assets/Briefs/bd-v-080-brief.md`. | Side-by-side Lightning-address-and-QR diagram with editable labels; half width. | |
| `BD-V-059` | AI | Supporting | Diagram | 36 and 43 | explain Lightning trade-offs and provide a separate Lightning example page. | SG: Under `### Lightning payments where locally appropriate`, after the six guided-payment steps. EG: under `### Lightning module checklist`, replace the matching marker after the source text at the listed EG line. See section 3.8 for the exact anchor. | SG: 1157; EG: 2613 | Makes a Lightning payment sequence clear while keeping custody and failure risk visible. | Show receiver creates request; sender scans or copies; sender verifies recipient, amount, unit, expiry, and fee; sender approves; payment routes; both wallets report success or failure. Add custody labels on both wallets and a branch for failure. Use generic, nonfunctional screens. | Lightning payment sequence; full width. | |
| `BD-V-060` | Pablo | Supporting | Diagram | 43 | add seven simple icons for the daily uses of Bitcoin. | Under `### Daily-life Bitcoin use`, after the seven use descriptions and before the three evaluation questions. | 1177 | Makes the seven distinct ways Bitcoin may be used in daily life quick to identify without suggesting that every learner should use it in every way. | Create seven equally weighted illustrative icons, each clearly labelled: earning, saving, receiving, sending, spending, pricing and accounting, and donating. Arrange them in a clear row, grid, or gentle sequence; do not make the icons form a compulsory circular process. Use familiar, culturally adaptable symbols and no provider branding. | Seven-icon daily-use illustration; full width. | |
| `BD-V-061` | AI | Supporting | Image | 43–44 | use separate payment examples and preserve the locally grounded scenario approach. | Under `### Local spending and receiving scenarios`, before Scenario 1. | 1191 | Gives all local scenarios one reusable visual grammar so educators can substitute local actors and goods. | Create a four-frame template: need and actors; payment request and chosen path; verification and settlement; record, refund, custody, or conversion. Include editable slots for small purchase, work payment, family transfer, refund, or donation. The template must work with simulation or tiny value. | Reusable scenario storyboard; full width. | |
| `BD-V-062` | AI | Essential | Diagram | 45 | preserve but simplify the strongly approved on/off-ramp pathway comparison. | SG: Under `### Local on-ramp and off-ramp pathways`, after the definition and pathway list and before the pathway comparison table. EG: under `### Module option F: on-ramp, off-ramp, KYC, and no-KYC comparison`, replace the matching marker after the source text at the listed EG line. See section 3.8 for the exact anchor. | SG: 1257; EG: 2749 | Forces comparison of the complete route rather than only the advertised first fee. | Show local money, work, goods, or services entering through possible routes; custody and identity checkpoints; on-chain or Lightning transfer; self-custody or service balance; and final use, holding, or conversion. Label spread, fees, time, reversal, withdrawal, counterparty, privacy, support, and law along the route. | End-to-end pathway map; full width. | |
| `BD-V-063` | AI | Supporting | Table | 45 | provide a local pathway-comparison table that considers the complete route. | Under `### Local on-ramp and off-ramp pathways`, replace the existing pathway comparison table visually while retaining an accessible text equivalent. | 1259 | Helps learners compare received value, time, custody, privacy, reversal risk, and failure points across local options. | Preserve the editable rows for local option A, local option B, and an existing non-Bitcoin option, plus all comparison columns. Do not pre-fill services, rates, or legal claims. | Editable pathway-comparison table; full width. | |
| `BD-V-064` | AI | Supporting | Table | 46 | keep KYC/no-KYC trade-offs only where locally appropriate and fact-checked. | Under `### KYC and no-KYC trade-offs where locally appropriate`, replace the existing `Question / KYC path / No-KYC path` table visually while retaining an accessible text equivalent. | 1281 | Frames KYC and no-KYC as different bundles of benefits and risks, not as good versus bad. | Preserve all eight questions in the existing comparison table: identity data collected; storage and retention; on-chain linkability; fraud protection; counterparty risk; limits and fees; local law; dispute handling. Leave the two answer columns editable for a dated local comparison. Include `local law varies; verify current information`. Do not imply evasion or guaranteed privacy. | Balanced trade-off comparison; full width. | |
| `BD-V-065` | AI | Essential | Diagram | 46–47 | preserve the conclusion and add a stronger balanced circular-economy graphic. | SG: Under `### Circular economies`, after the seven mapping questions. EG: under `### Module option G: circular economy and local resource map`, replace the matching marker after the source text at the listed EG line. See section 3.8 for the exact anchor. | SG: 1310; EG: 2775 | Shows value circulating among participants and reveals where the loop depends on outside services or support. | Map workers, customers, merchants, suppliers, educators or support, and exchange or on/off-ramp points. Use separate arrows for value, goods or services, and support. Mark custody, volatility, connectivity, and conversion dependencies. Include broken-loop examples such as immediate conversion or one organizer processing everything. | Editable local network map; full width. | |
| `BD-V-066` | Pablo | Supporting | Diagram | 40 and 48 | turn merchant payment flow into a local case study and connect it to jurisdiction. | SG: Under `### Merchant or community use cases`, after the merchant decision checklist and before the community-use examples. EG: under `### Module option D: merchant payment and refund flow`, replace the matching marker after the source text at the listed EG line. See section 3.8 for the exact anchor. | SG: 1331; EG: 2702 | Shows that accepting Bitcoin is an operational process, not just displaying a QR code. | Trace pricing → payment request → customer verification → merchant confirmation → receipt or record → custody or conversion → refund or exception. Add staff, accounting, tax, device security, offline failure, and support callouts. Use local-law placeholders, not assertions. | Merchant payment operations flow; full width. | |
| `BD-V-067` | AI | Supporting | Diagram | 39 and 48 | help learners connect with the local ecosystem through practical field/community work. | Under `### Local resource maps and community discovery`, immediately before `Record your local resources`. | 1363 | Connects community discovery with verification and privacy rather than treating a map listing as proof. | Provide an editable neighborhood or regional map template with merchant, educator, meetup, technical support, exchange information, legal or tax information, and missing-support markers. Every listing includes `date verified` and a safety note. Do not include real personal locations without consent. | Local resource-map template; full width. | |
| `BD-V-068` | AI | Supporting | Table | 48 | provide a printable local-resource record with built-in verification and safety prompts. | Under `### Local resource maps and community discovery`, replace the existing `Record your local resources` table visually while retaining an accessible text equivalent. | 1365 | Helps learners document useful local support while recording when information was checked. | Preserve rows for education group, merchant directory, technical support, local exchange information, and legal or tax information, with purpose, verification date, contact or location, and safety note columns. Do not pre-fill personal locations or imply trustworthiness from a listing. | Editable local-resource record table; full width. | |
| `BD-V-069` | AI | Supporting | Diagram | 49–50 | frame the review around the learner's community and a specific local need. | Under `### Review: connect this to your community`, after the paragraph beginning `**Module 4 answer:**` and before `#### Key takeaways`. The former final test table is no longer present. | 1379 | Summarizes the community review as a sequence that begins with a need and ends with evidence and a responsible next step. | Show the decision path `real need → Bitcoin fit → payment method → custody → total cost and trade-offs → safety and local conditions → evidence of success`. Add a return arrow when Bitcoin is not the best available fit. | Decision path; full width. | |
| `BD-V-070` | AI | Conditional | Table | 49–50 | make the final local-use test a concise decision and reflection table. | Under `### Review: connect this to your community`, after the paragraph beginning `**Module 4 answer:**` and before `#### Key takeaways`, only as a table alternative to `BD-V-069`. This is a proposed summary, not a replacement for an existing table. | 1379 | Offers a concise optional text equivalent for the community-review decision path. | If a table is clearer than `BD-V-069`, summarize the current review using rows for local need, function of money, realistic alternative, payment path, key control, benefit and risk, local conditions, and responsible next step. Use editable prompts rather than inventing a required test or assessment record. Keep any learner response space optional; formal evidence belongs in the educator assessment process. | Optional community-review summary table; full width. | |

### 3.6 Back of Diploma

| ID | Suggested by | Priority | Type | Page | Note | Placement | Line | Text–visual link | Design brief | Format | prompt |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `BD-V-071` | AI | Supporting | Diagram | 50–51 | make next steps quick to scan and separate the available continuation paths. | Under `### Continue with the Bitcoin Education Network`, after the paragraph beginning “If you want to teach”. The former “What now?” numbered list is no longer present. | 1425 | Makes the current community, contribution, and educator pathways visible as voluntary next steps. | Show optional routes to connect with a learning community, learn or volunteer, contribute through the official forms, explore the Educator Training Program, or explore network participation for an existing education community. Reuse the pathway language of `BD-V-077` without implying automatic teaching eligibility or network membership. Do not depict Advanced modules as currently available. | Next-step pathway map; full width. | |
| `BD-V-072` | Pablo | Essential | Diagram | 51 | make the safety reminder scannable and define practical safety tasks precisely. | SG: Under `### A safety reminder`, immediately before the reminder list. EG: under `### Final safety reminders`, replace the matching marker after the source text at the listed EG line. See section 3.8 for the exact anchor. | SG: 1439; EG: 3294 | Makes the minimum stop-and-check behavior memorable at the point of course completion. | Show `stop → verify source and recipient → verify custody, network, destination, amount, and fee → start small → proceed only when understood`. Put seed or private-key secrecy above the whole sequence as a non-negotiable boundary. | Compact safety strip; half to full width. | |
| `BD-V-073` | Pablo | Supporting | Image | 52 | add a public GitHub contribution link or QR and verify official destinations. | Under `### Source or update page, if included`, after the canonical source link. | 1469 | Provides one durable route to updates and contributions without filling the Diploma with fragile QR codes. | Create one panel containing a tested QR code, printed short URL, destination name, edition or last-verified date, and plain-language purpose. The QR must resolve to the canonical maintained source: `https://github.com/MyFirstBitcoin/mfb-curriculum`. Keep donation and any future educator or issuer-specific certificate verification separate unless the landing page clearly distinguishes them. Do not imply a central My First Bitcoin certificate service. | QR and fallback-link panel; half page. | |
| `BD-V-074` | Pablo | Supporting | Image | 52 | add separate on-chain and Lightning support QR codes with their payment text printed underneath. | Under `### Optional donate / support QR`, after the `Donate to My First Bitcoin` link and before the paragraph beginning “A printed edition may place one official support QR code here”. | 1489 | Offers the single official support-page route described in the guide, with a readable fallback and voluntary participation. | Create one optional support panel with a QR code linking to the approved destination `https://donate.myfirstbitcoin.org/`, the readable matching URL, destination name, and last-verified date. Keep the adjacent donation-safety paragraph. Do not encode a payment address or invoice in this website QR or imply that a donation is required. Test the destination and final printed QR before publication. The historical two-payment-route proposal is not the current guide placement; separate live on-chain and Lightning QR codes would require official verified destinations and an aligned manuscript revision. | Single support-page QR panel; half width. | |
| `BD-V-075` | AI | Conditional | Diagram | — | Deferred after `DEC-11`. | No 2026.10 Student Guide placement. The former central-verification section was replaced by `### Certificate meaning and issuer`. | — | Retained only as a possible future issuer-specific verification concept; it is not part of the current publication set. | Do not produce for 2026.10. Certification is educator-issued and My First Bitcoin does not operate a central verification service. A future separately governed issuer-specific method may revive this brief only after its real destination, privacy controls, correction and withdrawal rules, and minimum data display are approved and tested. It must identify the actual educator or issuing organization and must not imply central My First Bitcoin evaluation. | Deferred verification flow; no current asset. | |

### 3.7 Educator Guide use crosswalk

The original SG assets are mapped below to teaching guidance or an explicit SG-only restriction. Educator-only assets are specified separately in section 3.9. `EG heading line` identifies the heading, not an insertion point. Educators may refer to the SG visual while teaching; these references do not require extra copies in EG. Preserve the full educator instructions, approved assessment tasks, and private evidence records. Selected shared visuals now have explicit EG insertion placements in section 3.8. The crosswalk alone is not an insertion instruction. The four app-download locations remain restricted to `BD-V-076`.

| Asset IDs | Exact EG section | EG heading line | Use and boundary |
|---|---|---|---|
| `BD-V-001` | `### Translation workflow` | 2966 | Keep attribution and licence terms with adaptations; the licence mark itself remains at the SG front matter. |
| `BD-V-002` | `### Teach how to think, not what to think` | 501 | Use the claim/evidence/trade-off loop to support discussion and revision. |
| `BD-V-003` | `### Four-module Diploma and Advanced boundaries` | 460 | Explain the required Diploma and the separate Advanced scope. EG insertion specified in section 3.8 for `BD-V-003`. |
| `BD-V-004`, `BD-V-005` | `## The Diploma at a glance` | 330 | Reuse the roadmap or reference table to introduce the four-stage arc. |
| `BD-V-006` | `### The learning rhythm` | 718 | Use the SG five-stage learner view alongside the educator facilitation rhythm; do not replace the EG teaching sequence. |
| `BD-V-007`, `BD-V-008` | `### Functions and properties of money` | 1027 | Separate functions from properties and apply the comparison questions. EG insertion specified in section 3.8 for `BD-V-008`. |
| `BD-V-009`, `BD-V-010` | `### Barter and the double coincidence of wants` | 1074 | Use the barter-mismatch graphic before introducing money, then the money-mediated exchange graphic. EG insertions are specified in section 3.8. |
| `BD-V-011`, `BD-V-012` | `### Scarcity, value, and exchange` | 1083 | Use familiar examples of context, choice, and trade-offs. EG insertion specified in section 3.8 for `BD-V-012`. |
| `BD-V-013` | `### Beginner monetary history` | 1102 | Show overlapping forms of money, not a universal progress sequence. EG insertion specified in section 3.8 for `BD-V-013`. |
| `BD-V-014`, `BD-V-015` | `### Fiat money and the local system` | 1130 | Keep institutional roles and local variation visible. EG insertion specified in section 3.8 for `BD-V-015`. |
| `BD-V-016`, `BD-V-017` | `### Fractional-reserve banking, liquidity, and solvency` | 1160 | Distinguish deposit creation, liquidity, and solvency. EG insertion specified in section 3.8 for `BD-V-016`, `BD-V-017`. |
| `BD-V-018` | `### Inflation and purchasing power` | 1210 | Compare the same fixed amount and basket using fictional or dated values. EG insertion specified in section 3.8 for `BD-V-018`. |
| `BD-V-019` | `### CBDCs as digital fiat` | 1270 | Compare control, issuer, and verification without assuming one CBDC design. EG insertion specified in section 3.8 for `BD-V-019`. |
| `BD-V-020`, `BD-V-021` | `### Why people look for alternatives` | 1258 | Compare purpose and trade-offs without ranking investments. |
| `BD-V-022` | `### Why Bitcoin was created` | 1408 | Explain the change in dependence on a central ledger keeper. EG insertion specified in section 3.8 for `BD-V-022`. |
| `BD-V-023`, `BD-V-025` | `### Earlier digital-money context` | 1426 | Use the idea lineage and origin milestones as historical context. |
| `BD-V-024`, `BD-V-027` | `### Explain the combined response` | 1438 | Show how the features work together to address double spending and digital scarcity. EG insertion specified in section 3.8 for `BD-V-024`. |
| `BD-V-026`, `BD-V-030` | `### Decentralization and peer-to-peer transfer` | 1467 | Separate network roles from intermediaries and communications dependencies. EG insertion specified in section 3.8 for `BD-V-026`. |
| `BD-V-028` | `### Finite supply and halving` | 1546 | Keep supply, subsidy, fees, and price distinct. EG insertion specified in section 3.8 for `BD-V-028`. |
| `BD-V-029` | `### Sats and unit bias` | 1572 | Practise reading equivalent BTC and sat amounts. EG insertion specified in section 3.8 for `BD-V-029`. |
| `BD-V-031` | `### Users, nodes, miners, developers, and services` | 1486 | Ask learners to explain each role and its limits. EG insertion specified in section 3.8 for `BD-V-031`. |
| `BD-V-032` | `### Proof of work` | 1518 | Distinguish costly production from independent verification. EG insertion specified in section 3.8 for `BD-V-032`. |
| `BD-V-033` | `### Bitcoin as sound digital money` | 1595 | Use the same comparison criteria and retain qualifications. |
| `BD-V-034` | `### Review and bridge to Module 3` | 1716 | Connect each response to a remaining trade-off or new responsibility. |
| `BD-V-035` | `### Wallets are interfaces` | 1826 | Keep keys and wallet interfaces separate from the ledger. EG insertion specified in section 3.8 for `BD-V-035`. |
| `BD-V-036`, `BD-V-078` | `### Addresses and payment requests` | 1864 | Compare prepared on-chain and Lightning receiving information and matching QR formats. |
| `BD-V-037` | `### Keys and digital authorization` | 1939 | Keep the private key inside the secret boundary when explaining signatures. EG insertion specified in section 3.8 for `BD-V-037`. |
| `BD-V-038`, `BD-V-079` | `### Seed phrases and recovery` | 1962 | Use conceptual or placeholder examples only; never expose learner recovery material. EG insertion specified in section 3.8 for `BD-V-038`. |
| `BD-V-039`, `BD-V-040` | `### Custodial and self-custodial use` | 2015 | Compare key control and recovery responsibility. EG insertion specified in section 3.8 for `BD-V-039`. |
| `BD-V-041`, `BD-V-042` | `### Hot, cold, hardware, and custodial are different dimensions` | 2039 | Distinguish custody from signing environment. EG insertion specified in section 3.8 for `BD-V-042`. |
| `BD-V-043` | `#### Activity: recovery-readiness simulation` | 1989 | Use the safe workflow as teaching support; it does not replace the approved practical task. |
| `BD-V-044` | `### Receiving bitcoin` | 2058 | Use prepared screens to identify receiving information and check results. EG insertion specified in section 3.8 for `BD-V-044`. |
| `BD-V-045` | `### Sending bitcoin` | 2093 | Rehearse verification before approval and stop on mismatches. EG insertion specified in section 3.8 for `BD-V-045`. |
| `BD-V-046` | `### Block explorers and verification` | 2143 | Connect confirmation status to evidence and explorer privacy limits. EG insertion specified in section 3.8 for `BD-V-046`. |
| `BD-V-047` | `### Scam recognition and safe response` | 2170 | Ask learners to identify the red flag and first safe action. EG insertion specified in section 3.8 for `BD-V-047`. |
| `BD-V-048`, `BD-V-049` | `### Acquiring and exchanging: awareness, not financial advice` | 2207 | Compare pathways without recommending providers or financial action. EG insertion specified in section 3.8 for `BD-V-048`. |
| `BD-V-050`, `BD-V-051` | `### On-chain and Lightning payments` | 2239 | Compare requests, payment result, custody, and failure risks. EG insertion specified in section 3.8 for `BD-V-050`. |
| `BD-V-052`, `BD-V-053` | `### Review and bridge to Module 4` | 2339 | Select the responsibility map or its text equivalent for recap. |
| `BD-V-054` | `### Begin with a need, not a tool` | 2387 | Use the learner Connect/Compare/Practise/Explain view; detailed planning stays in the seven-step module builder. |
| `BD-V-055` | `### Module 4 planning record` | 2534 | The SG learner record complements this educator planning record; do not substitute it for planning or assessment evidence. |
| `BD-V-056` | `### Use Presentation → Practice → Production` | 855 | Use the same safe learning progression for local workshops. EG insertion specified in section 3.8 for `BD-V-056`. |
| `BD-V-057`, `BD-V-058` | `### Local Bitcoin tool review` | 2577 | Support a dated local review; retain the fuller educator verification requirements. |
| `BD-V-059`, `BD-V-080` | `### Lightning module checklist` | 2599 | Use only when locally appropriate and prepared; explain request type, custody, result, and failure. EG insertion specified in section 3.8 for `BD-V-059`. |
| `BD-V-060` | `### Module option A: local payment-path comparison` | 2621 | Use the daily-use icons to identify a purpose before selecting a payment path. |
| `BD-V-061` | `### Module option B: small purchase` | 2647 | Reuse the storyboard for the selected scenario; the following module options provide work, remittance, refund, and donation variants. |
| `BD-V-062`, `BD-V-063`, `BD-V-064` | `### Module option F: on-ramp, off-ramp, KYC, and no-KYC comparison` | 2734 | Compare the complete local route with a realistic alternative and current local conditions. EG insertion specified in section 3.8 for `BD-V-062`. |
| `BD-V-065`, `BD-V-067`, `BD-V-068` | `### Module option G: circular economy and local resource map` | 2761 | Use editable maps and dated records without exposing personal locations. EG insertion specified in section 3.8 for `BD-V-065`. |
| `BD-V-066` | `### Module option D: merchant payment and refund flow` | 2686 | Trace verification, records, custody, failure, and refund handling. EG insertion specified in section 3.8 for `BD-V-066`. |
| `BD-V-069`, `BD-V-070` | `### Review and course bridge` | 2869 | Choose one community-review format; neither creates a new certification gate. |
| `BD-V-071`, `BD-V-077` | `### The pathway from learner to educator` | 397 | Introduce and revisit voluntary learning, contribution, teaching, and network pathways. EG insertion specified in section 3.8 for `BD-V-077`. |
| `BD-V-072` | `### Final safety reminders` | 3284 | Use the final stop-and-check strip for closure. EG insertion specified in section 3.8 for `BD-V-072`. |
| `BD-V-073` | `### Maintain local content` | 3354 | Use the SG source/update route when checking editions and preparing corrections. |
| `BD-V-075` | `### Confirm what the certificate means` | 3271 | Deferred for 2026.10. Explain educator-issued certification in text; do not show or imply a central My First Bitcoin verification system. |
| `BD-V-074` | — | — | SG only. EG has no matching optional-support call to action; do not insert a donation QR into an educator teaching example. |
| `BD-V-076` | `## About this guide`; `## Continue learning` | 5; 3617 | Two EG download panels after lines 9 and 3619; the two SG panels remain after lines 51 and 1514. See section 3.8 for marker locations. No other app QR placements. |


### 3.8 Shared assets inserted in the Educator Guide

Reuse the existing Student Guide master and brief for the placements below. Keep the full educator explanation, activity instructions, and existing tables. These visuals clarify the adjacent concepts; they do not replace approved assessment materials or change permitted support during formal evidence collection. Conditional assets remain conditional on the verified local context. A marker reserves a production location and does not mean the SVG already exists.

`EG source line` identifies the text before or after which the marker is placed. `EG marker line` identifies the opening comment to replace at production. Recalculate both after guide edits. A same-ID graphic uses the same meaning and labels in both guides; a materially different educator graphic gets its own ID in section 3.9.

| Asset | Exact EG heading | Position and text anchor | EG source line | EG marker line |
|---|---|---|---|---|
| `BD-V-076` | `## About this guide` | After the line beginning `Download the [My First Bitcoin App](https://myfirstbitcoin.app/) for optional microlearning, se…`; replace the marker. | 9 | 11 |
| `BD-V-077` | `### The pathway from learner to educator` | After the line beginning `Present this as an available progression. Learners may begin with the Diploma and choose whethe…`; replace the marker. | 408 | 410 |
| `BD-V-003` | `### Four-module Diploma and Advanced boundaries` | After the line beginning `**Advanced** is optional follow-on learning beyond the Diploma. Detailed [mining](mfb-bd-lx.md#…`; replace the marker. | 466 | 468 |
| `BD-V-056` | `### Use Presentation → Practice → Production` | After the line beginning `**Production:** Learners complete a defined practical task or direct the decisions without step…`; replace the marker. | 861 | 863 |
| `BD-V-008` | `### Functions and properties of money` | After the line beginning `- A **property** describes a quality that can make it useful: [durability](mfb-bd-lx.md#term-du…`; replace the marker. | 1032 | 1034 |
| `BD-V-009` | `### Barter and the double coincidence of wants` | After the sentence beginning `First, let the group attempt direct exchange`; replace the marker. | 1076 | 1078 |
| `BD-V-010` | `### Barter and the double coincidence of wants` | After the sentence beginning `Then introduce a commonly accepted medium`; replace the marker. | 1084 | 1086 |
| `BD-V-012` | `### Scarcity, value, and exchange` | After the line beginning `- **Trade-off:** a choice gains one benefit while accepting a cost or giving up another.`; replace the marker. | 1090 | 1092 |
| `BD-V-013` | `### Beginner monetary history` | After the line beginning `- digital interfaces to fiat-denominated claims.`; replace the marker. | 1112 | 1114 |
| `BD-V-015` | `### Fiat money and the local system` | After the line beginning `6. what would make the payment harder if acceptance or trust broke down.`; replace the marker. | 1143 | 1145 |
| `BD-V-016` | `### Fractional-reserve banking, liquidity, and solvency` | After the line beginning `- exact rules vary by jurisdiction.`; replace the marker. | 1168 | 1170 |
| `BD-V-017` | `### Fractional-reserve banking, liquidity, and solvency` | After the line beginning `- **[Solvency risk](mfb-bd-lx.md#term-solvency-risk):** the bank's [assets](mfb-bd-lx.md#term-a…`; replace the marker. | 1181 | 1183 |
| `BD-V-018` | `### Inflation and purchasing power` | After the line beginning `Teach [price inflation](mfb-bd-lx.md#term-price-inflation) as a sustained rise in the general […`; replace the marker. | 1212 | 1214 |
| `BD-V-019` | `### CBDCs as digital fiat` | After the line beginning `Explain that a [CBDC](mfb-bd-lx.md#term-cbdc) is a central-bank [liability](mfb-bd-lx.md#term-l…`; replace the marker. | 1280 | 1282 |
| `BD-V-022` | `### Why Bitcoin was created` | After the line beginning `A central digital-payment system can keep one authoritative [ledger](mfb-bd-lx.md#term-ledger) …`; replace the marker. | 1412 | 1414 |
| `BD-V-024` | `### Explain the combined response` | After the line beginning `5. Participants converge on the valid history with the most [accumulated work](mfb-bd-lx.md#ter…`; replace the marker. | 1446 | 1448 |
| `BD-V-026` | `### Decentralization and peer-to-peer transfer` | After the line beginning `Peer-to-peer does not mean only two computers communicate directly or that no infrastructure is…`; replace the marker. | 1478 | 1480 |
| `BD-V-031` | `### Users, nodes, miners, developers, and services` | After the line beginning `&#124; [Bitcoin service](mfb-bd-lx.md#term-bitcoin-service) &#124; Provides a wallet, exchange, explorer,…`; replace the marker. | 1496 | 1498 |
| `BD-V-032` | `### Proof of work` | After the line beginning `- [difficulty](mfb-bd-lx.md#term-difficulty) adjusts so blocks arrive about every ten minutes o…`; replace the marker. | 1526 | 1528 |
| `BD-V-028` | `### Finite supply and halving` | After the line beginning `- [transaction fees](mfb-bd-lx.md#term-transaction-fee) also compensate [miners](mfb-bd-lx.md#t…`; replace the marker. | 1554 | 1556 |
| `BD-V-029` | `### Sats and unit bias` | After the line beginning `- 1 [sat](mfb-bd-lx.md#term-sat) = 0.00000001 bitcoin.`; replace the marker. | 1583 | 1585 |
| `BD-V-035` | `### Wallets are interfaces` | After the line beginning `- any external service the wallet depends on.`; replace the marker. | 1837 | 1839 |
| `BD-V-037` | `### Keys and digital authorization` | After the line beginning `No legitimate educator, wallet company, exchange employee, developer, support worker, or public…`; replace the marker. | 1954 | 1956 |
| `BD-V-038` | `### Seed phrases and recovery` | After the line beginning `- a seed that may have been exposed should be treated as compromised.`; replace the marker. | 1972 | 1974 |
| `BD-V-039` | `### Custodial and self-custodial use` | After the line beginning `Do not treat [self-custody](mfb-bd-lx.md#term-self-custody) as a moral test. A beginner may cho…`; replace the marker. | 2031 | 2033 |
| `BD-V-042` | `### Hot, cold, hardware, and custodial are different dimensions` | After the line beginning `A Lightning wallet can be custodial or self-custodial. A [hardware wallet](mfb-bd-lx.md#term-ha…`; replace the marker. | 2048 | 2050 |
| `BD-V-044` | `### Receiving bitcoin` | After the line beginning `Explain that a message or screenshot saying “sent” is not proof of receipt. The receiver should…`; replace the marker. | 2072 | 2074 |
| `BD-V-045` | `### Sending bitcoin` | After the line beginning `10. Verify the result in the appropriate wallet or transaction view.`; replace the marker. | 2106 | 2108 |
| `BD-V-046` | `### Block explorers and verification` | After the line beginning `- information that becomes public.`; replace the marker. | 2153 | 2155 |
| `BD-V-047` | `### Scam recognition and safe response` | After the line beginning `> Pause. Share nothing. Send nothing. Close the channel. Verify independently through a known s…`; replace the marker. | 2187 | 2189 |
| `BD-V-048` | `### Acquiring and exchanging: awareness, not financial advice` | After the line beginning `- Which local law, tax, or reporting rule may apply?`; replace the marker. | 2229 | 2231 |
| `BD-V-050` | `### On-chain and Lightning payments` | After the line beginning `Lightning is not a separate coin. A successful Lightning payment does not prove the wallet is s…`; replace the marker. | 2253 | 2255 |
| `BD-V-059` | `### Lightning module checklist` | After the line beginning `A successful small Lightning payment shows that the selected path worked once. It does not prov…`; replace the marker. | 2613 | 2615 |
| `BD-V-066` | `### Module option D: merchant payment and refund flow` | After the line beginning `- support and escalation.`; replace the marker. | 2702 | 2704 |
| `BD-V-062` | `### Module option F: on-ramp, off-ramp, KYC, and no-KYC comparison` | After the line beginning `- Which local rule applies?`; replace the marker. | 2749 | 2751 |
| `BD-V-065` | `### Module option G: circular economy and local resource map` | After the line beginning `9. whether the loop depends on giveaways or one organizer.`; replace the marker. | 2775 | 2777 |
| `BD-V-072` | `### Final safety reminders` | After the line beginning `- accept that “not yet” or “not for this case” can be responsible conclusions.`; replace the marker. | 3294 | 3296 |
| `BD-V-076` | `## Continue learning` | After the line beginning `Download the [My First Bitcoin App](https://myfirstbitcoin.app/) for optional microlearning, se…`; replace the marker. | 3619 | 3621 |

### 3.9 Educator-only asset briefs

These diagrams clarify educator processes and relationships. They have no required Student Guide placement. Each entry is grounded in the current EG text and uses the same visual standards as the learner assets: one primary idea, readable editable labels, grayscale-safe distinctions, an accessible text equivalent, and no decorative filler. Preserve the adjacent prose as the complete explanation. The next unused ID after this set is `BD-V-102`.

Ordinary checklists, schedules, planning records, and comparison tables remain text when they already communicate clearly. Related processes are grouped in one diagram where this improves understanding. Detailed printable activity cards remain on the Resources Hub; actual learner evidence remains in the Assessment Grid.

| ID | Suggested by | Priority | Type | Page | Note | Placement | Line | Text–visual link | Design brief | Format | prompt |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `BD-V-081` | AI | Essential | Diagram | — | Proposed in response to the request for educator diagrams. | EG only: under `## Assessment at a glance`, after the line beginning `They are also not a combined numerical grade. Both components must be complete, and every requi…`. Replace the `BD-V-081` marker at EG line 45. | EG: 43 | Makes the two separately required evidence components and their joint completion condition unmistakable. | **Two evidence components and the completion gate.** Use two equal lanes: educator-evaluated theory, C1–C8 (50%); directly observed practice, C9–C11 (50%). Both feed an AND gate labelled every required competency meets standard, then assessment-complete and educator-issued certification. Show a Not yet branch returning to practice and reassessment. Keep C12/C13 formative and optional app review outside the gate. State that percentages are neither teaching time nor a combined numerical grade. Do not invent a pass percentage, automatic certificate-issuing system, or central My First Bitcoin verification service. Caption: `Both evidence components must be complete; one cannot compensate for the other.` Alt text: `Theory competencies C1–C8 and practical competencies C9–C11 must each meet standard before assessment completion. Not yet evidence returns to practice and reassessment; attendance, optional app review, and formative reflection do not replace either component.` Master: `Assets/Briefs/bd-v-081-brief.md`. | Flow diagram; full width. | |
| `BD-V-082` | AI | Essential | Diagram | — | Proposed in response to the request for educator diagrams. | EG only: under `### Capacity and readiness check`, after the line beginning `Record the chosen C11 variant, practical environment, accessibility equivalents, assessor nam…`. Replace the `BD-V-082` marker at EG line 72. | EG: 70 | Connects cohort size, observation time, assessor capacity, and the advertised course route. | **Observation capacity before scheduling.** Show learner count multiplied by estimated individual evidence minutes, distributed across available approved assessors. Label the quotient minimum observation time per assessor under balanced allocation, not total staff labour saved. Add setup, feedback, resets, accommodations, and reassessment before a fits the planned route decision. If no, loop to a smaller cohort, more approved assessor capacity, or a redesigned advertised schedule. Do not imply several learners can be observed simultaneously without identifiable evidence. Use symbols or clearly fictional numbers only; preserve the source formula as prose. Caption: `Plan enough time to observe each learner before confirming the course schedule.` Alt text: `Learner numbers and individual evidence time determine observation workload. After allowing for setup, feedback, resets, access needs, and reassessment, the educator checks capacity and revises cohort size, assessor capacity, or the advertised schedule if needed.` Master: `Assets/Briefs/bd-v-082-brief.md`. | Flow diagram; full width. | |
| `BD-V-083` | AI | Essential | Diagram | — | Proposed in response to the request for educator diagrams. | EG only: under `### Competency-to-evidence crosswalk`, after the line beginning `\*Planning times are per learner evidence time, not the full teaching time. They are planning e…`. Replace the `BD-V-083` marker at EG line 96. | EG: 94 | Explains the relationship among task IDs, competency IDs, decimal criteria, and the Assessment Grid. | **Competencies, tasks, criteria, and records.** Map T1 to C1–C2, T2 to C3–C5, T3 to C6–C8; P9 to C9, P10 to C10, P11 to C11. Connect each competency to its required criteria and one final MS/NY record. Use C11.1 and C11.2 nested under C11 as the example of criteria that are not separate result rows. Expand MS as Meets standard and NY as Not yet. Include task, date, assessor, variant where applicable, and concise evidence reference as record metadata. No real learner data. Keep the detailed crosswalk table intact. Caption: `Tasks produce evidence for competencies; criteria support each competency decision.` Alt text: `Three theory interactions cover C1–C8, and three practical tasks cover C9–C11. All required criteria within a competency support one Meets standard or Not yet result recorded with concise evidence metadata.` Master: `Assets/Briefs/bd-v-083-brief.md`. | Task-to-competency map with one nested criterion example; full width. | |
| `BD-V-084` | AI | Essential | Diagram | — | Proposed in response to the request for educator diagrams. | EG only: under `### Common support, safety, and record rules`, after the line beginning `**Permitted support:** Before evidence is gathered, you may read the prompt, repeat it once, pr…`. Replace the `BD-V-084` marker at EG line 106. | EG: 104 | Separates access support and safety intervention from prompting that supplies the answer. | **Support without supplying the assessed decision.** Use two time bands: before evidence and during practical observation. Before: read the prompt, repeat once, provide approved translation or communication accommodation, clarify a non-assessed word, prepare materials. During: safety stop or reset as permitted. Draw a clear boundary around the learner-owned explanation, comparison, verification, and action. Outside the permitted lane show supplying an answer, selecting a payment detail, or performing a required step. Use a conceptual example, not a new rubric. Read with each task’s specific permitted-support rules. Caption: `Support access and safety while the learner makes the assessed decisions.` Alt text: `An educator may provide the permitted preparation and access support and stop unsafe action. The learner must still supply the assessed explanation, select the relevant details, and perform or direct the required decisions.` Master: `Assets/Briefs/bd-v-084-brief.md`. | Two-stage support-boundary diagram; half to full width. | |
| `BD-V-085` | AI | Essential | Diagram | — | Proposed in response to the request for educator diagrams. | EG only: under `### Reassessment, calibration, and moderation`, after the line beginning `Use only versioned, approved task cards. Review local tools, current facts, translation, access…`. Replace the `BD-V-085` marker at EG line 204. | EG: 202 | Distinguishes the learner reassessment loop from assessor calibration and cohort moderation. | **Reassessment and educator quality review.** Show three labelled lanes. Learner: Not yet → private criterion-specific feedback → focused practice → same or approved equivalent task → new evidence → update Grid only when sufficient; incomplete evidence loops back. Assessor before delivery: score annotated MS/NY examples for T2, P9, selected P11 → compare judgments → resolve differences → retain calibration record. Cohort: lead or approved second reviewer checks each variant setup and samples records including disputed, reassessed, and safety-critical cases → corrections through approved record process. No automatic promotion from Not yet, public rankings, lowered standards, or replacement of direct observation. Caption: `Improve evidence and consistency without lowering the standard.` Alt text: `Learners receive private feedback, practise, and provide new evidence after Not yet. Educators calibrate judgments before delivery and moderate cohort records through the approved process; review never substitutes for observed performance.` Master: `Assets/Briefs/bd-v-085-brief.md`. | Three-lane process diagram; full width. | |
| `BD-V-086` | AI | Essential | Diagram | — | Proposed in response to the request for educator diagrams. | EG only: under `### The learning ecosystem`, after the line beginning `&#124; Operational assessment protocol and Grid &#124; Approved assessment interactions and tasks, observ…`. Replace the `BD-V-086` marker at EG line 391. | EG: 389 | Makes resource ownership and the route from teaching to recorded evidence visible. | **How the learning resources work together.** Map Student Guide → learner explanations; Educator Guide → preparation, facilitation, safety; Resources Hub → selected activities; operational protocol → approved tasks and standards; Assessment Grid → private competency results. Show the educator connecting teaching, practice, observation, and records. Place optional app self-checks on a separate review branch without a certification-evidence arrow. Any app name must use the required hyperlink. Keep the existing table as the detailed text equivalent. Caption: `Use each resource for its job in the learning and evidence process.` Alt text: `The Student Guide supplies explanations, the Educator Guide supports teaching, and selected Resources Hub activities support practice. The operational protocol governs evidence collection and the Assessment Grid holds private results. Optional app self-checks support review only.` Master: `Assets/Briefs/bd-v-086-brief.md`. | Resource relationship map; full width. | |
| `BD-V-087` | AI | Essential | Diagram | — | Proposed in response to the request for educator diagrams. | EG only: under `## 2. What stays fixed and what can change`, after the line beginning `- move advanced technical or professional content into the required Diploma at the cost of requ…`. Replace the `BD-V-087` marker at EG line 454. | EG: 452 | Shows what educators can adapt while preserving the same Diploma standard. | **Fixed standards and local adaptation.** Use three labelled regions matching the source table: fixed, adaptable, flexible with guardrails. Keep required competencies, learner actions, safety, evidence, and passing standard inside a fixed boundary. Put examples, language, grouping, tools, and environment in the adaptable area. Route assessment or delivery changes through an equivalence check before use; if uncertain, use for practice and select an approved assessment route. Do not infer that any local change is an approved certificated variant. Preserve the existing table and both may/may-not lists. Caption: `Localize the route while preserving the required learner action and standard.` Alt text: `Local examples and teaching methods can change inside fixed competency, evidence, safety, and completion boundaries. Changes affecting assessment require an approved equivalent route.` Master: `Assets/Briefs/bd-v-087-brief.md`. | Three-region boundary diagram with an equivalence gate; full width. | |
| `BD-V-099` | AI | Essential | Diagram | — | Proposed in response to the request for educator diagrams. | EG only: under `### Local verification record`, after the line beginning `Prefer authoritative primary sources for current rules. If the evidence is incomplete, say so. …`. Replace the `BD-V-099` marker at EG line 708. | EG: 706 | Connects changing local claims to dated sources, classroom wording, and a fallback. | **Verify, date, teach, and recheck local information.** Show identify claim → distinguish stable concept/changing detail → check authoritative primary source or qualified local expertise → record source, date, version, and limitation → use qualified classroom wording → recheck before reuse. Unverified or changed details branch to state uncertainty, a clearly hypothetical example, or a prepared safe fallback; live action must not depend on an unverified safety-critical claim. Include generic wallet-version, fee, rule, and merchant-listing examples without filling in current facts. Link to the existing record table rather than creating a second form. Caption: `A local example needs a source, a date, and a plan for change.` Alt text: `Educators distinguish stable concepts from changing details, verify current sources, record dates and limits, teach qualified examples, and recheck them before reuse. Uncertainty or change triggers a safer example or fallback.` Master: `Assets/Briefs/bd-v-099-brief.md`. | Verification lifecycle with an uncertainty branch; full width. | |
| `BD-V-088` | AI | Essential | Diagram | — | Proposed in response to the request for educator diagrams. | EG only: under `### The learning rhythm`, after the line beginning `8. **Connect:** Show how the idea prepares for the next part of the Diploma.`. Replace the `BD-V-088` marker at EG line 731. | EG: 729 | Makes the educator’s eight-step teaching cycle quick to follow and repeat. | **The educator facilitation rhythm.** Show Purpose → Activate → Explain → Check → Apply → Produce → Debrief → Connect. Use short role labels and a return arrow from Check or Debrief to explanation or practice when needed. Identify Check as feedback unless the approved formal evidence conditions are met. Keep the learner doing the explaining or performing at Produce. This is a separate educator graphic: do not overwrite the five-stage SG rhythm in BD-V-006. Caption: `Move from a clear purpose to learner action, debrief, and connection.` Alt text: `The educator sets purpose, activates prior ideas, explains, checks, guides application, invites independent production, debriefs, and connects to the next concept. Unclear responses lead back to explanation or practice.` Master: `Assets/Briefs/bd-v-088-brief.md`. | Eight-stage cycle in two readable rows; full width. | |
| `BD-V-101` | AI | Essential | Diagram | — | Proposed in response to the request for educator diagrams. | EG only: under `### Scenario analysis`, after the line beginning `Change one condition after the first answer. For example: the internet fails, the address chang…`. Replace the `BD-V-101` marker at EG line 772. | EG: 770 | Makes the educator’s use of changed conditions visible as a test of transferable reasoning. | **Scenario reasoning when a condition changes.** Trace goal → known facts/unknowns to verify → control of money/keys/records/rules → options and failure points → smallest safe next step. Then change one condition: connection fails, destination changes, recipient needs local currency, or fee rises. Loop to the affected fact, control, or option rather than automatically repeating the original action. Show stopping or declining a path as valid where justified. Use one fictional scenario, no personal financial disclosures or live payment instructions. This is facilitation, not a newly approved assessment task. Caption: `Change one condition and ask the learner to reconsider the decision.` Alt text: `A fictional scenario moves from goal and verified facts to control, options, risks, and a safe next step. A changed connection, destination, recipient need, or fee sends reasoning back to the affected decision.` Master: `Assets/Briefs/bd-v-101-brief.md`. | Decision path with a changed-condition return loop; full width. | |
| `BD-V-089` | AI | Essential | Diagram | — | Proposed in response to the request for educator diagrams. | EG only: under `### Media and tool fallbacks`, after the line beginning `Offline teaching and assessment are valid. Use offline knowledge checks for preparation and app…`. Replace the `BD-V-089` marker at EG line 843. | EG: 841 | Shows why changing the medium must preserve the learner’s action and observed evidence. | **Equivalent learning and evidence across delivery modes.** Branch from one competency into prepared live tool, printed screens/cards, and an approved accessible communication or control route. Reconverge at the same learner decision/action, required verification, educator observation, and standard. Show barriers such as device, connection, language, or access needs leading to a prepared equivalent, not to lower criteria. Include a no valid equivalent branch returning to preparation/practice without certification. Draw examples from the adjacent table but retain its full list. Do not turn watching a video or another learner’s performance into evidence. Caption: `Change the medium, preserve the action and evidence.` Alt text: `Live tools, paper simulations, and approved accessible routes can support the same competency when the learner still makes the required decisions and the educator can judge equivalent evidence. Without equivalence, prepare another route before certification.` Master: `Assets/Briefs/bd-v-089-brief.md`. | Branch-and-rejoin equivalence diagram; full width. | |
| `BD-V-090` | AI | Essential | Diagram | — | Proposed in response to the request for educator diagrams. | EG only: under `### Universal stop conditions`, after the line beginning `Stopping is a successful safety behavior. Do not shame the learner who notices a problem.`. Replace the `BD-V-090` marker at EG line 909. | EG: 907 | Turns the safety triggers into an educator response rather than a list to memorize. | **Stop, protect, verify, and choose a safe route.** Feed source triggers into STOP: secret exposure, mismatch, unverified source, urgency, changed behaviour, uncertain funds, privacy exposure, failed safety check, or educator uncertainty. Then protect people and information → verify independently without collecting secrets → choose a prepared safe equivalent or postpone. Resume only when the relevant safety checks can be satisfied. Add a distinct formal-assessment branch: a safety-critical error produces NY under the protocol, followed by feedback, practice, and reassessment. Do not label every device failure a learner failure or offer an improvised funds-recovery procedure. Caption: `Stopping protects learning; resume through a verified safe route.` Alt text: `An unsafe or unexplained condition stops the activity. The educator protects people and secrets, verifies the issue, and uses a safe prepared route or postpones. A learner safety-critical assessment error is recorded Not yet under the protocol.` Master: `Assets/Briefs/bd-v-090-brief.md`. | Flow diagram; full width. | |
| `BD-V-100` | AI | Essential | Diagram | — | Proposed in response to the request for educator diagrams. | EG only: under `### Bitcoin, stablecoins, and other crypto-assets`, after the line beginning `Do not imply that every non-Bitcoin [asset](mfb-bd-lx.md#term-asset) has the same structure. Th…`. Replace the `BD-V-100` marker at EG line 1634. | EG: 1632 | Helps educators explain similar-looking interfaces backed by different control and verification relationships. | **Compare digital-asset trust dependencies.** Use three lanes for Bitcoin, a generic stablecoin model, and a generic other-asset model. Apply the same questions about issuance/control, supply support, independent verification, and counterparties. Show public node-enforced rules for Bitcoin; design-dependent reserves/redemption or other mechanisms for stablecoins; varying project rules/governance for other assets. Add a separate service/custody layer across all lanes so Bitcoin service risk remains visible. Keep every design qualification from the existing table. No brands, tickers, logos, prices, rankings, recommendations, or suggestion every model works alike. Preserve the table as detailed reference. Caption: `Compare who controls the rules and which claims can be verified.` Alt text: `Three generic asset models are compared through issuance, supply support, verification, and counterparties. Wallets and custodians form a separate dependency layer across all three; similar interfaces do not establish the same trust model.` Master: `Assets/Briefs/bd-v-100-brief.md`. | Three-lane dependency diagram; full width. | |
| `BD-V-092` | AI | Essential | Diagram | — | Proposed in response to the request for educator diagrams. | EG only: under `### Address history and reuse lookup`, after the line beginning `**Offline fallback:** Use a printed sequence showing one address used once and another reused a…`. Replace the `BD-V-092` marker at EG line 1933. | EG: 1931 | Makes address reuse and the limits of public-data inference visible without exposing anyone’s transactions. | **Address reuse and information linkage.** Use fictional non-address labels A/B/C, arrows, and invented receipts. Compare multiple receipts to one address with separate fresh receiving addresses. Show an observer linking reused receipts, plus a dotted uncertain link from external identifying information. Add a separate explorer-search arrow showing that a service may learn which address interests a device. State that an address alone does not prove legal identity and fresh addresses do not guarantee anonymity. No real addresses, txids, amounts belonging to people, or scannable QR codes. Related BD-V-046 concerns confirmations, not identity linkage. Caption: `Fresh addresses reduce easy linkage; they do not guarantee anonymity.` Alt text: `Several fictional receipts share one reused address and are easily linked. Fresh receiving addresses reduce that direct link, but outside information and explorer searches can still reveal relationships. Public data does not by itself prove a person’s identity.` Master: `Assets/Briefs/bd-v-092-brief.md`. | Two-panel linkage diagram with an explorer privacy inset; full width. | |
| `BD-V-091` | AI | Essential | Diagram | — | Proposed in response to the request for educator diagrams. | EG only: under `#### Activity: recovery-readiness simulation`, after the line beginning `7. return the fictional material securely or destroy it as instructed.`. Replace the `BD-V-091` marker at EG line 2005. | EG: 2003 | Separates what the learner controls from what the educator may observe during recovery practice. | **Recovery practice without observing secrets.** Use learner and educator lanes around a private-material boundary. Preserve the seven EG production steps: official instructions, compatibility, private work, approved backup-check/recovery method, expected receiving information or history, clear temporary device, return or destroy fictional material as instructed. The educator observes sequence, decisions, and safe handling without seeing real recovery words. Use placeholders only and no recovery-entry screenshot. Label prepared fake material or disposable empty training wallet. Related BD-V-043 supplies the SG six-step overview; this asset adds educator visibility boundaries and the EG material-return step. Do not represent this diagram as the P10 rubric. Caption: `Observe the recovery process without observing a learner’s secrets.` Alt text: `The learner follows seven prepared recovery-practice steps in a private area, checks the expected result, clears the device, and returns or destroys fictional material. The educator observes decisions and safe handling across a boundary that hides secret information.` Master: `Assets/Briefs/bd-v-091-brief.md`. | Two-lane privacy-boundary workflow; full width. | |
| `BD-V-093` | AI | Essential | Diagram | — | Proposed in response to the request for educator diagrams. | EG only: under `### Integrated Module 3 practice circuit`, after the line beginning `Do not use the stations as formal assessment unless the exact tasks, variants, criteria, and re…`. Replace the `BD-V-093` marker at EG line 2295. | EG: 2293 | Shows how station rotation supports practice without confusing group participation with assessment. | **Practice stations and individual observation.** Arrange the eight current stations in a suggested rotation: wallet/custody, public or secret, receive, send, recovery, explorer, scam, pathway. Mark a private recovery zone, prepared materials, device reset between learners, and a separate individual-observation lane. Label stations practice unless exact approved task, variant, criteria, and records are in place. Show one learner making or directing decisions; peers may support practice but cannot supply another learner’s assessed performance. Keep the original station table and avoid implying all stations fit a fixed two-hour session. Caption: `Use groups for practice and preserve individual evidence for assessment.` Alt text: `Eight practice stations cover custody, public and secret information, receiving, sending, recovery, explorers, scams, and pathways. A separate approved observation route identifies each learner’s decisions; shared-device resets and private recovery space protect participants.` Master: `Assets/Briefs/bd-v-093-brief.md`. | Station layout and separate observation lane; full width. | |
| `BD-V-094` | AI | Essential | Diagram | — | Proposed in response to the request for educator diagrams. | EG only: under `### The seven-step module builder`, before the line beginning `#### 1. Learn the local context`. Replace the `BD-V-094` marker at EG line 2404. | EG: 2410 | Gives educators a map of the seven-step planning process before its detailed subsections. | **Build a local Connect lesson.** Show the exact seven steps: learn local context; define need/opportunity; select focused module; verify facts/tools/expertise; design Presentation → Practice → Production; define safety/evidence; debrief and choose a safe next step. Carry the existing non-Bitcoin alternative from need to debrief. Mark C11.1 safe sequence and C11.2 explanation as preserved requirements, not new result rows. Use a loop from failed verification to task selection, and a legitimate conclusion of not suitable here. Link visually to BD-V-056 and the readiness gate BD-V-095. Do not make a named product the starting point. Caption: `Begin with a local need and finish with evidence and a responsible next step.` Alt text: `Seven planning stages connect local context and need to a focused, verified task, safe teaching sequence, observable evidence, and debrief. The existing alternative stays in view, and unsuitable options return to planning.` Master: `Assets/Briefs/bd-v-094-brief.md`. | Seven-stage planning map; full width. | |
| `BD-V-095` | AI | Essential | Diagram | — | Proposed in response to the request for educator diagrams. | EG only: under `### Module 4 readiness gate`, after the line beginning `&#124; Can evidence be observed? &#124; The educator can see the learner's decisions and hear the explana…`. Replace the `BD-V-095` marker at EG line 2528. | EG: 2526 | Shows that every readiness condition must be satisfied before live delivery. | **Readiness before live local practice.** Use eight labelled checks in the source order: real need, clear competency/approved task, educator capability, verified tool, understood local rules, low risk, equitable access, observable evidence. All satisfactory leads to planned live delivery; any gap branches to the corresponding source-table remedy, such as simulation, expert support, accessible equivalent, or revised observation capacity. Feed the remedy back into readiness review. Preserve the full table as the detailed text equivalent. No aggregate readiness score; seven out of eight is not sufficient. Simulation may be the chosen first route. Caption: `Resolve each readiness gap before live delivery.` Alt text: `Eight checks cover purpose, competency, educator capability, tools, local rules, safety, access, and observation. Every check must be satisfactory for live delivery; a gap leads to a safer route or revised plan and another readiness review.` Master: `Assets/Briefs/bd-v-095-brief.md`. | Flow diagram; full width. | |
| `BD-V-096` | AI | Essential | Diagram | — | Proposed in response to the request for educator diagrams. | EG only: under `### Community custody and shared funds`, after the line beginning `Do not turn [community-custody](mfb-bd-lx.md#term-community-custody) design into a beginner imp…`. Replace the `BD-V-096` marker at EG line 2811. | EG: 2809 | Reveals who controls shared funds and which responsibilities remain separate. | **Community funds and concentrated responsibility.** Map fictional contributors/beneficiaries, key controller or custodian, payment authorization, and records/review. Use distinct arrows for value, authority, and information. Flag concentration when one organizer controls every function. Surround the map with backup/succession, privacy, disputes/loss, legal context, and transparency questions from the prose. Treat separation of duties as a question to examine, not a prescribed implementation. No actual funds, addresses, wallet configuration, multisignature setup, legal conclusions, or assumption that community reputation guarantees safety. Related BD-V-065 maps circulation; this maps control. Caption: `Community purpose does not remove custody risk.` Alt text: `Contributors depend on whoever controls shared funds. A role map separates key control, spending authority, records, and review and highlights concentrated trust, continuity, privacy, dispute, and legal questions.` Master: `Assets/Briefs/bd-v-096-brief.md`. | Role-and-responsibility map with distinct arrow types; full width. | |
| `BD-V-097` | AI | Essential | Diagram | — | Proposed in response to the request for educator diagrams. | EG only: under `### Translation workflow`, after the line beginning `9. Confirm that the language version preserves the competencies, safety instructions, and asses…`. Replace the `BD-V-097` marker at EG line 2980. | EG: 2978 | Shows translation as a review-and-test process, not a one-way text conversion. | **Translation with meaning and safety checks.** Preserve all nine steps as compact numbered labels grouped into prepare meaning (1–3), translate/localize (4–5), and review/test/confirm equivalence (6–9). Show language specialist and subject-matter educator at review; difficult safety instructions return to wording when learner testing exposes ambiguity. Preserve competency, task difficulty, rubric, and stop conditions. Do not imply machine translation or a language review alone approves assessment equivalence. Keep the existing numbered list as the text equivalent. Caption: `Translate the meaning and test that the same safe action is understood.` Alt text: `Clear source meaning and terminology lead to translation and authorized localization, then language and subject review, learner safety testing, and confirmation of equivalent competencies and assessment standards. Ambiguity returns to revision.` Master: `Assets/Briefs/bd-v-097-brief.md`. | Flow diagram; full width. | |
| `BD-V-098` | AI | Essential | Diagram | — | Proposed in response to the request for educator diagrams. | EG only: under `### Adapt a summative practical task`, after the line beginning `If equivalence is uncertain, use the adaptation for practice and select an assessment task whos…`. Replace the `BD-V-098` marker at EG line 3177. | EG: 3175 | Distinguishes freedom to adapt practice from the conditions required for certificated evidence. | **Learning activity or approved assessment?.** Branch from intended use into learning/formative practice and formal assessment. Practice may adapt names, roles, medium, timing, and scaffolding while preserving concept, learner action, safety, and key comparison. Formal theory needs the approved competency-aligned interaction and record; practical assessment needs an approved equivalent variant preserving sequence, verification, independence, rubric, safety errors, and record. A missing condition leads to practice and selection of an approved task, not automatic certification. Keep this as educator planning guidance; do not create an approval authority or modify approved tasks. Caption: `An engaging activity becomes assessment only under the approved evidence conditions.` Alt text: `Practice activities allow contextual and access adaptations. Formal theory or practical assessment must preserve the approved evidence, criteria, independence, safety, and record conditions. Uncertain equivalence returns the activity to practice and an approved assessment route.` Master: `Assets/Briefs/bd-v-098-brief.md`. | Two-branch activity-selection decision diagram; full width. | |

---

## 4. Reuse and combination rules

The index contains conceptual requirements, not a command to create the largest possible number of files. Combine visuals only when the combined result remains readable and preserves each placement's learning purpose.

Preferred reuse:

- Where a diagram and a table explain the same idea, choose a readable combination or use the table as the accessible equivalent. In particular, avoid duplicating `BD-V-004`/`BD-V-005`, `BD-V-039`/`BD-V-040`, `BD-V-041`/`BD-V-042`, and `BD-V-050`/`BD-V-051`. Use `BD-V-053` as an alternative to `BD-V-052`, and `BD-V-070` only as an alternative to `BD-V-069`.

- `BD-V-008` establishes the visual language for later money-property comparisons.
- `BD-V-015`, `BD-V-026`, and `BD-V-031` should share actor symbols while keeping fiat-system and Bitcoin roles distinct.
- `BD-V-044`, `BD-V-045`, and `BD-V-046` should use one generic, nonfunctional interface family. Coordinate typography and labels with `BD-V-036`, whose QR must decode to the My First Bitcoin-supplied test address and must be clearly labelled for its test network.
- `BD-V-039` and `BD-V-042` should share custody labels and definitions.
- `BD-V-048` and `BD-V-062` should share pathway symbols, but Module 3 remains global orientation while Module 4 is locally completed.
- `BD-V-050` and `BD-V-059` should share on-chain and Lightning layer notation.
- `BD-V-054`, `BD-V-061`, `BD-V-065`, and `BD-V-067` should be designed as editable templates for localization.
- `BD-V-072` should retain the safety-gate vocabulary used in the final reminder.

Do not combine visuals merely because they are adjacent. In particular:

- keep `wallet / keys / ledger` separate from `custodial / self-custodial`;
- keep `finite supply` separate from price or investment claims;
- keep `proof of work` separate from the general participant-role map;
- keep `on-chain versus Lightning` separate from wallet custody;
- keep QR destinations separate from conceptual diagrams.

---

## 5. Generation and review handoff

For each selected entry, the design handoff should return:

```yaml
id: BD-V-001
suggested_by: Pablo | AI | User
priority: essential | supporting | conditional
type: Table | Diagram | Image
audience: learner | educator | both
placements:
  - source_document: ../publish/mfb-bd-26.10/mfb-bd-sg-26.10.md
    source_heading: Exact heading from the placement field
    insert_position: Exact before/after/replace instruction
    source_line: Current line from the Line column
    marker_line: Opening VISUAL comment line, when a marker is present
# Repeat the placement object for every required SG or EG location; BD-V-076 has four.
# Use the Educator Guide source path for educator-only placements.
# Educator-use crosswalk entries are teaching references, not extra insertions.
pablo_note_pages: []
pablo_note_summary: Matching note text, or null when no page-specific note exists
text_concept: The prose idea this visual explains
learning_intent: What the intended reader should be able to explain or do after viewing it
visual_type: Diagram | illustration | timeline | annotated interface | map
required_elements: []
guardrails: []
title: Short title for the intended reader
caption: What the intended reader should notice
asset_master: Assets/Briefs/bd-v-000-brief.md
screen_export: Assets/Briefs/bd-v-000-brief.md
alt_text: Complete instructional text equivalent
editable_labels: true
localization_fields: []
factual_sources: []
review_required:
  - curriculum
  - technical
  - accessibility
  - localization
```

Before insertion, every visual must pass these questions:

1. Does it clarify the adjacent text faster than prose alone?
2. Is its placement anchor still exact?
3. Can the intended reader explain the main relationship after viewing it, without requiring knowledge beyond the relevant guide?
4. Does it preserve the qualifications and trade-offs in the text?
5. Are protocol, service, wallet, and participant roles accurate?
6. Is it safe, nonfunctional where required, and free of private data?
7. Is all factual or current information sourced and dated?
8. Is the reading order accessible and the alt text complete?
9. Does it work in grayscale, print, and a narrow screen?
10. Can labels be translated or locally replaced without redrawing the visual?

`Essential` means the concept is sufficiently relational, procedural, or misconception-prone that a visual should be planned into the Diploma. `Supporting` means the visual is useful if space and testing justify it. `Conditional` means it should be generated only after the local context, technical method, or publication decision is confirmed.

This index should be revised whenever either guide changes materially. It should remain a map from text to visual meaning, not become the production tracker for the visual files themselves.

---

## 6. Intended AI-to-code workflow

The initial guide visuals use an iterative reference-image-to-code workflow. Every eligible asset requires one low-resolution transparent PNG reference, a white-background JPG preview of the same image, and a matching JSON conformance report before coded production begins. Generate the composition once and export the JPG from the PNG at the same dimensions. JPEG cannot preserve transparency. The references are visual direction only; they do not produce the final published asset.

The current reference batch has 101 indexed items: 98 eligible and three deferred (`BD-V-001`, `BD-V-070`, and `BD-V-075`). `BD-V-001` remains an official licence-mark task for later production; do not generate an AI reference, redraw the mark, or replace its logo and text with invented elements. Its section 3 brief remains binding.

1. **Specify the structure.** Select an asset entry and use its reference specification in section 7 as the source contract. It decides element counts, relationships, reading order, labels, localization, prohibitions, and safety requirements before any image is generated.
2. **Generate a reference image.** Use OpenAI image generation or Gemini for each eligible asset. Build exactly the specified composition and elements. Save a low-resolution transparent PNG reference and export its white-background (#FFFFFF) JPG preview in the ignored `Assets/Reference/` directory. Save the prompt and relevant generation/export settings in `Assets/Prompts/prompt-codex.md
3. **Review the conformance report and both images.** Check instructional accuracy, beginner clarity, safety, cultural flexibility, and whether the concept can be reconstructed with editable code. Verify actual transparent background pixels in the PNG, a solid white background in the JPG, and matching composition and dimensions; record the formats, backgrounds, and checks in the JSON. Check the report against the specification, especially that `textPresentInImage` is empty and that `elementsAdded` is empty or justified. Reject or revise concepts that depend on baked-in text, unverified claims, real private data, brand imitation, or decorative imagery without instructional purpose.
4. **Code the selected concept.** Give Claude Design or Claude Code the selected asset ID, its complete `workspace/08_assets.md` entry, the approved PNG reference and JPG preview, and the adjacent guide text where useful. Treat both images as visual direction only. Recreate layout, shapes, icons, arrows, interface elements, and labels as editable code or vector elements wherever practical. Use the Claude Design System as the source of truth for brand and design decisions.
5. **Localize and make accessible.** Keep instructional text outside the reference image. Put labels, captions, alt text, and localization-dependent content in editable data or content fields. Preserve reading order, responsive behavior, grayscale meaning, and a text equivalent for complex visuals.
6. **Review the coded asset.** Render the project at desktop, phone, A4 or US Letter, print, and grayscale sizes. Check factual accuracy, text overflow, translation expansion, contrast, alt text, safe sample data, QR behavior where applicable, and alignment with the adjacent guide prose.
7. **Prepare the Sanity project.** Save the approved implementation and its supporting metadata in a tracked `Assets/diploma/` subfolder. Download or export the project as required for Sanity and verify that the published result matches the approved source.
8. **Insert only after approval.** Replace the source marker or add the Markdown reference only when the coded asset has passed curriculum, technical, accessibility, and localization review. Update this index if the anchor, text, or visual meaning changes.

The workflow is provisional and may change as the Sanity implementation develops. The source of truth for instructional content is the curriculum text and this visual index; [27_assets-style.md](27_assets-style.md) controls reference-image styling, the Claude Design System controls coded production styling, and the approved coded asset is the publication source. The generated reference images are not sources of truth.

### Reusable prompt attachments

Attach [22_openai-reference-image-prompt.md](22_openai-reference-image-prompt.md) to every OpenAI image-generation request. It defines the contract-first reference-image visual language and the JSON conformance report.

Attach [23_claude-design-sanity-asset-prompt.md](23_claude-design-sanity-asset-prompt.md) to each Claude Design request. It directs Claude to rebuild—not publish—the reference as an editable, localized, accessible source bundle and to prepare only schema-compatible, upload-ready Sanity deliverables.

Save the transparent PNG reference as `Assets/Reference/bd-v-000-ref.jpg`, its white-background JPG preview as `Assets/Reference/bd-v-000-ref.jpg`, their conformance report as `Assets/Reference/bd-v-000-ref.json`, and the completed prompt, generation date, tool or model, generation/export settings, and review note as `Assets/Prompts/prompt-codex.md Replace `bd-v-000` with the stable asset ID in lowercase. The `-ref` suffix identifies all four as reference materials, not final assets. Mark a reference checklist item complete only after all four files exist and pass review. Once structure is pre-specified, the only genuinely new information an image contributes is spatial arrangement and visual treatment. Element counts, relationships, labels, reading order, and prohibitions are already decided. The report carries placement, treatment, export checks, and deviations. Self-reported conformance is weak evidence: a model will tend to claim it complied. The report narrows what a human or Claude must check; it does not replace that check.

### Asset working structure

Use this separation so exploratory material does not enter version control while approved source and implementation files remain reviewable:

```text
Assets/                    # ignored working material
├── references/                 # transparent PNG references, JPG previews, JSON reports
├── prompts/                    # prompts, settings, and generation notes
└── rejected/                   # rejected concepts retained temporarily

assets/                         # tracked approved assets
└── diploma/
    ├── student-guide/          # Student Guide visual projects and exports
    ├── educator-guide/         # Educator Guide visual projects and exports
    └── shared/                 # assets reused by both guides
```

For an individual coded visual, keep the implementation together in its guide or shared folder using the stable asset ID, for example `bd-v-037/`, with the HTML/CSS/SVG source, approved exports, alt-text record, and a short README when needed. Preserve the flat `Assets/Briefs/bd-v-000-brief.md` naming convention in handoff examples only when the publication pipeline requires a direct asset path.

### Reference-image and coded-asset rules

- Treat AI-generated PNGs and their JPG previews as low-resolution references, not final publication files.
- Never place text, letters, or numerals anywhere in a generated reference image. Keep all strings in the specification and recreate them as live translatable nodes in code.
- Recreate essential text as HTML or editable SVG text so it can be translated, corrected, resized, and checked for accessibility.
- Use AI image generation primarily for composition, illustration, visual metaphor, and art direction. Use code or vector construction for diagrams, tables, timelines, interface mockups, QR codes, and any visual requiring exact text or geometry.
- Keep people, places, names, currencies, prices, examples, and local scenarios replaceable through content fields or localization data.
- Define responsive states for desktop, phone-width, and print layouts. Do not rely on a single fixed image crop to communicate the concept.
- Preserve the index's safety rules in the coded output: no real seed phrases, private keys, payable addresses, learner balances, identities, or transactions; label fictional interfaces and QR codes clearly.
- Preserve the index's teaching meaning. Do not make a visually attractive reference more authoritative, promotional, certain, or universal than the adjacent prose.
- Use recurring symbols and visual grammar across related assets, while keeping protocol, wallet, service, user, node, miner, and educator roles distinct.
- Design for grayscale and color-blind access. Color must not be the only carrier of meaning; use labels, patterns, line styles, position, or shape as well.
- Keep implementation text translatable. Allow for longer translated strings, alternate line breaks, and future right-to-left layout without redrawing the visual.
- Record the reference prompt, generation tool, generation date, factual sources, reviewer, and implementation status in the asset handoff or project README.

### Brand and visual-direction requirements

Before generating a production batch, maintain an approved visual-token reference covering:

- colors and grayscale equivalents;
- primary and fallback fonts;
- heading, label, caption, and body-text hierarchy;
- icon and illustration style;
- line weights, corner radius, spacing, and arrow conventions;
- preferred composition patterns such as comparison panels, timelines, process strips, and role maps;
- examples of approved and rejected visual treatments.

Use the approved My First Bitcoin visual system for brand and visual decisions. Avoid generic decorative Bitcoin imagery, price-promotion language, rockets, glowing network backgrounds, and other visual shortcuts that do not clarify the adjacent lesson.

### Extended coded-asset handoff fields

When the image-to-code workflow is used, extend the handoff object with:

```yaml
reference_image: Assets/Reference/bd-v-000-ref.jpg
reference_preview: Assets/Reference/bd-v-000-ref.jpg
reference_specification: Assets/Reference/bd-v-000-ref.json
reference_prompt: Assets/Prompts/prompt-codex.md
reference_tool: OpenAI | Gemini
reference_generated_at: YYYY-MM-DD
implementation_type: html-css-svg
implementation_source: Assets/diploma/shared/bd-v-000/
sanity_project: true
published_asset: Assets/Briefs/bd-v-000-brief.md
editable_text: true
responsive_states:
  - desktop
  - phone
  - print
text_equivalent: Assets/diploma/shared/bd-v-000/alt-text.md
review_status: draft | review | approved | published
reviewers: []
```

---

## 7. Reference specifications

These specifications are the contract for the reference-image stage and the coded asset. They remove ambiguity before generation. A reference image may contribute spatial arrangement and visual treatment, but it must not decide element identity, relationships, reading order, labels, or prohibitions.

### 3.1 Welcome and learning setup

```yaml
id: BD-V-001
spec_version: 1
type: Image
illustration_need: reference_required
composition: one small official licence mark with one adjacent short text lockup
elements:
  - id: licence-mark
    what: official Creative Commons BY-SA 4.0 mark
    instructional_role: identifies the open licence visually
  - id: licence-text-lockup
    what: adjacent written licence statement
    instructional_role: keeps licence terms primary
relationships:
  - licence-text-lockup -> licence-mark: written terms identify the mark
reading_order: [licence-text-lockup, licence-mark]
text_layer:
  total_count: 1
  licence-statement: STRING-TODO
  note: Use the current written licence statement beside or immediately above the mark.
fixed_text: []
localizable: [licence-statement]
must_not:
  - Do not redraw, recolour, or distort the logo.
  - Do not use the logo as a replacement for the licence text or link.
safety: Use the official Creative Commons BY-SA 4.0 mark or an approved official variant.
greyscale_carrier: official mark shape and adjacent written licence statement
open: []
```

```yaml
id: BD-V-002
spec_version: 1
type: Diagram
illustration_need: reference_required
composition: one six-step circular loop
elements:
  - id: identify-claim
    what: claim checkpoint
    instructional_role: starts critical examination
  - id: separate-fact-preference
    what: fact and preference checkpoint
    instructional_role: distinguishes kinds of statements
  - id: inspect-evidence-source
    what: evidence and source checkpoint
    instructional_role: checks support for claim
  - id: compare-alternatives
    what: alternatives checkpoint
    instructional_role: broadens possible explanations
  - id: name-tradeoff-uncertainty
    what: trade-off or uncertainty checkpoint
    instructional_role: preserves qualification and limits
  - id: provisional-conclusion-question
    what: conclusion or question checkpoint
    instructional_role: ends without false certainty
relationships:
  - identify-claim -> separate-fact-preference: examine the claim type
  - separate-fact-preference -> inspect-evidence-source: inspect support
  - inspect-evidence-source -> compare-alternatives: compare interpretations
  - compare-alternatives -> name-tradeoff-uncertainty: identify limits
  - name-tradeoff-uncertainty -> provisional-conclusion-question: form provisional view
  - provisional-conclusion-question -> identify-claim: revision remains possible
reading_order: [identify-claim, separate-fact-preference, inspect-evidence-source, compare-alternatives, name-tradeoff-uncertainty, provisional-conclusion-question]
text_layer:
  total_count: 6
  identify-claim: "identify the claim"
  separate-fact-preference: "separate fact from preference"
  inspect-evidence-source: "inspect evidence and source"
  compare-alternatives: "compare alternatives"
  name-tradeoff-uncertainty: "name a trade-off or uncertainty"
  provisional-conclusion-question: "form a provisional conclusion or question"
fixed_text: []
localizable: [identify-claim, separate-fact-preference, inspect-evidence-source, compare-alternatives, name-tradeoff-uncertainty, provisional-conclusion-question]
must_not:
  - Do not end the loop in certainty.
safety: []
greyscale_carrier: clockwise position and numbered sequence
open: []
```

```yaml
id: BD-V-003
spec_version: 1
type: Diagram
illustration_need: reference_required
composition: one Diploma container with four sequential modules and one separate onward path
elements:
  - id: diploma-container
    what: all-learners Diploma container
    instructional_role: contains all required modules
  - id: module-1
    what: Problem module
    instructional_role: starts shared core learning
  - id: module-2
    what: Solution module
    instructional_role: continues shared core learning
  - id: module-3
    what: Action module
    instructional_role: marks educator-adapted practical learning
  - id: module-4
    what: Connect module
    instructional_role: marks required locally curated learning
  - id: local-need
    what: local need
    instructional_role: grounds Connect application
  - id: realistic-alternative
    what: realistic alternative
    instructional_role: keeps Connect comparative
  - id: advanced-path
    what: separate Advanced path
    instructional_role: separates onward learning scope
relationships:
  - module-1 -> module-2: progression
  - module-2 -> module-3: progression
  - module-3 -> module-4: progression
  - module-4 -> local-need: Connect applies earlier learning locally
  - module-4 -> realistic-alternative: Connect compares a realistic alternative
  - diploma-container -> advanced-path: Advanced is outside the Diploma
reading_order: [diploma-container, module-1, module-2, module-3, module-4, local-need, realistic-alternative, advanced-path]
text_layer:
  total_count: 10
  diploma: "Diploma: all learners"
  module-1: "Problem"
  module-2: "Solution"
  module-3: "Action"
  module-4: "Connect"
  shared-core: "shared core learning"
  educator-adapted: "educator-adapted practical learning"
  connect-description: "Connect: educator-curated local learning; required"
  local-need: "Local need"
  realistic-alternative: "Realistic alternative"
  note: Use generic editable labels; localization supplies context without adding a requirement.
fixed_text: []
localizable: [diploma, module-1, module-2, module-3, module-4, shared-core, educator-adapted, connect-description, local-need, realistic-alternative]
must_not:
  - Do not show Advanced as part of the Diploma.
  - Do not imply a hierarchy of importance through the progression arrows.
safety: []
greyscale_carrier: containment, sequence position, and distinct module patterns
open: []
```

```yaml
id: BD-V-004
spec_version: 1
type: Diagram
illustration_need: reference_required
composition: left-to-right sequence of four stages, single row
elements:
  - id: problem
    what: Problem stage
    instructional_role: frames understanding money
  - id: solution
    what: Solution stage
    instructional_role: frames how Bitcoin works
  - id: action
    what: Action stage
    instructional_role: frames using Bitcoin safely
  - id: connect
    what: Connect stage
    instructional_role: frames local community learning
  - id: local-need
    what: local need
    instructional_role: grounds Connect in context
  - id: realistic-alternative
    what: realistic alternative
    instructional_role: preserves comparison in Connect
  - id: safe-task
    what: safe task
    instructional_role: applies earlier learning safely
  - id: next-step
    what: next step
    instructional_role: carries learning onward
relationships:
  - problem -> solution: learning progression
  - solution -> action: learning progression
  - action -> connect: learning progression
  - connect -> local-need: local application
  - connect -> realistic-alternative: local comparison
  - connect -> safe-task: safe application
  - connect -> next-step: onward action
reading_order: [problem, solution, action, connect, local-need, realistic-alternative, safe-task, next-step]
text_layer:
  total_count: 7
  problem: "1 Problem: Understanding Money"
  solution: "2 Solution: How Bitcoin Works"
  action: "3 Action: Using Bitcoin Safely"
  connect: "4 Connect: Bitcoin in Your Community"
  shared-learning: "Modules 1–3: shared learning"
  connect-status: "Module 4: educator-curated, locally relevant, and required"
  guiding-question: STRING-TODO
  note: Supply each module's existing guiding question from the adjacent course text.
fixed_text: ["1", "2", "3", "4"]
localizable: [problem, solution, action, connect, shared-learning, connect-status, guiding-question]
must_not:
  - Do not reduce the final module to spending.
safety: []
greyscale_carrier: left-to-right position, stage number, and distinct stage patterns
open: []
```

```yaml
id: BD-V-005
spec_version: 1
type: Table
illustration_need: reference_required
composition: one four-row reference table with four columns
elements:
  - id: module-column
    what: Module column
    instructional_role: names each course module
  - id: role-column
    what: Role column
    instructional_role: states each module purpose
  - id: guiding-question-column
    what: Guiding question column
    instructional_role: prompts learner inquiry
  - id: learner-promise-column
    what: Learner promise column
    instructional_role: states learner outcome
  - id: problem-row
    what: Problem row
    instructional_role: records first module
  - id: solution-row
    what: Solution row
    instructional_role: records second module
  - id: action-row
    what: Action row
    instructional_role: records third module
  - id: connect-row
    what: Connect row
    instructional_role: records required local module
relationships:
  - module-column -> problem-row: identifies first module
  - module-column -> solution-row: identifies second module
  - module-column -> action-row: identifies third module
  - module-column -> connect-row: identifies fourth module
reading_order: [module-column, role-column, guiding-question-column, learner-promise-column, problem-row, solution-row, action-row, connect-row]
text_layer:
  total_count: 11
  module: "Module"
  role: "Role"
  guiding-question: "Guiding question"
  learner-promise: "Learner promise"
  problem: "Problem: Understanding Money"
  solution: "Solution: How Bitcoin Works"
  action: "Action: Using Bitcoin Safely"
  connect: "Connect: Bitcoin in Your Community"
  shared-learning: "Modules 1–3: shared learning"
  connect-status: "Module 4: educator-curated, locally relevant, and required for Diploma completion"
  row-content: STRING-TODO
  note: Copy each existing role, guiding question, and learner promise from the replaced table.
fixed_text: []
localizable: [module, role, guiding-question, learner-promise, problem, solution, action, connect, shared-learning, connect-status, row-content]
must_not: []
safety: []
greyscale_carrier: table position, row rules, and column headings
open: []
```

```yaml
id: BD-V-006
spec_version: 1
type: Diagram
illustration_need: reference_required
composition: left-to-right sequence of five stages, single row
elements:
  - id: learn-key-idea
    what: key idea stage
    instructional_role: introduces the concept
  - id: show-explanation-or-application
    what: demonstration stage
    instructional_role: shows possible understanding
  - id: apply-idea
    what: application stage
    instructional_role: uses the concept
  - id: explain-own-words
    what: explanation stage
    instructional_role: checks personal understanding
  - id: review-next-connection
    what: review stage
    instructional_role: links to next module
relationships:
  - learn-key-idea -> show-explanation-or-application: learning rhythm
  - show-explanation-or-application -> apply-idea: learning rhythm
  - apply-idea -> explain-own-words: learning rhythm
  - explain-own-words -> review-next-connection: learning rhythm
reading_order: [learn-key-idea, show-explanation-or-application, apply-idea, explain-own-words, review-next-connection]
text_layer:
  total_count: 5
  learn-key-idea: "Learn a key idea"
  show-explanation-or-application: "Show what you can explain or apply"
  apply-idea: "Apply the idea"
  explain-own-words: "Explain in your own words"
  review-next-connection: "Review the connection to the next module"
fixed_text: []
localizable: [learn-key-idea, show-explanation-or-application, apply-idea, explain-own-words, review-next-connection]
must_not:
  - Do not turn this learning rhythm into an assessment score.
  - Do not imply that self-report proves competency.
safety: Keep discussion, safe practice, and offline participation available throughout.
greyscale_carrier: left-to-right position and stage number
open: []
```

```yaml
id: BD-V-076
spec_version: 1
type: Image
illustration_need: reference_required
composition: one compact download panel with one QR code and one readable URL
elements:
  - id: download-call-to-action
    what: optional app download call
    instructional_role: offers a voluntary download route
  - id: qr-code
    what: tested app-download QR code
    instructional_role: opens the app destination
  - id: printed-url
    what: readable app URL
    instructional_role: provides non-QR access
relationships:
  - download-call-to-action -> qr-code: call directs to download route
  - download-call-to-action -> printed-url: call provides readable fallback
reading_order: [download-call-to-action, qr-code, printed-url]
text_layer:
  total_count: 3
  download: "Download the My First Bitcoin App"
  optional: "use is optional"
  url: "https://myfirstbitcoin.app/"
fixed_text: ["https://myfirstbitcoin.app/"]
localizable: [download, optional]
must_not:
  - Do not place this app QR elsewhere in either guide or in other publications.
safety: Use `https://myfirstbitcoin.app/` for the QR destination, hyperlink, and readable printed URL. Test the link and printed QR before publication.
greyscale_carrier: QR pattern, position, and readable URL
open: []
```

```yaml
id: BD-V-077
spec_version: 1
type: Diagram
illustration_need: reference_required
composition: left-to-right sequence of four stages, single row
elements:
  - id: introduction-to-bitcoin
    what: Introduction to Bitcoin stage
    instructional_role: offers basic exploration
  - id: bitcoin-diploma
    what: Bitcoin Diploma stage
    instructional_role: builds beginner foundation
  - id: educator-training-program
    what: Educator Training Program stage
    instructional_role: develops teaching practice
  - id: bitcoin-education-network
    what: Bitcoin Education Network stage
    instructional_role: connects and contributes
relationships:
  - introduction-to-bitcoin -> bitcoin-diploma: optional progression
  - bitcoin-diploma -> educator-training-program: optional progression
  - educator-training-program -> bitcoin-education-network: optional progression
reading_order: [introduction-to-bitcoin, bitcoin-diploma, educator-training-program, bitcoin-education-network]
text_layer:
  total_count: 9
  direct-entry: "Start here: Bitcoin Diploma"
  introduction-to-bitcoin: "Introduction to Bitcoin"
  bitcoin-diploma: "Bitcoin Diploma"
  educator-training-program: "Educator Training Program"
  bitcoin-education-network: "Joining the Bitcoin Education Network"
  explore-basics: "Explore the basics"
  beginner-foundation: "Build a beginner foundation"
  teaching-practice: "Develop teaching practice"
  connect-contribute: "Connect and contribute"
fixed_text: []
localizable: [direct-entry, introduction-to-bitcoin, bitcoin-diploma, educator-training-program, bitcoin-education-network, explore-basics, beginner-foundation, teaching-practice, connect-contribute]
must_not:
  - Do not imply that Diploma completion automatically qualifies someone to teach.
  - Do not imply that Diploma completion grants network membership.
safety: Link the final stage to the Bitcoin Education Network dashboard in digital versions. Present this as an optional progression, with direct entry to the Diploma possible.
greyscale_carrier: left-to-right position, stage number, and distinct stage patterns
open: []
```

---

### Complete reference classification registry

This registry applies to the complete, stable ID range `BD-V-001` through `BD-V-101`, inclusive. The current batch classifies 98 items as `reference_required` and defers `BD-V-001`, `BD-V-070`, and `BD-V-075`. Deferral leaves each checklist item unchecked and does not remove its brief or authorize production. `BD-V-001` is deferred only from AI reference generation: later production must use the official licence mark under its existing brief. There are no `none`, `light`, or `scene` generation tiers.

For each ID, its complete section 3 asset-index entry is incorporated as the section 7 structural contract. It is therefore binding for the asset type, teaching relationship, placement, design brief, caption, alt text, factual and safety limits, required verification, localization, and format. The shared requirements in section 2 and relevant section 8 register entries are also incorporated. This avoids maintaining two divergent copies of the 101 detailed briefs.

```yaml
specification_version: 3
applies_to: BD-V-001 through BD-V-101
reference_required: true for eligible items
batch_total: 101
batch_eligible: 98
batch_deferred: [BD-V-001, BD-V-070, BD-V-075]
reference_format: low-resolution transparent PNG plus white-background JPG preview and JSON conformance report
reference_export: Generate once; composite the PNG over solid white at the same dimensions for the JPG.
contract_fields:
  composition: section 3 Design brief and Format
  elements_and_relationships: section 3 Design brief and Text–visual link
  reading_order: section 3 Text–visual link, Design brief, and Format
  text_and_localization: section 3 Design brief, caption, alt text, and section 2 requirements
  prohibitions_and_safety: section 2 requirements and section 3 Design brief
  shared_components: relevant section 8 register entries
  unresolved_decisions: every explicit pending, conditional, confirmation, or verification condition in section 3
production_gate: For eligible items, both reference images, the conformance report, and prompt record must exist and pass review before production coding. Deferred items are not released by this gate.
```

The eight legacy per-asset records above remain useful examples of the contract shape. Their `illustration_need` value is superseded by this registry. Do not create a new per-asset structure contract outside the asset-index entry unless the entry is materially insufficient; if one is needed, add it here and update the generated execution checklists in the same revision.

---

## 8. Shared actor, prop and interface register

This register defines recurring items before illustration or code work begins. Entries are ordered by reuse count, which is the build order for the shared library.

```yaml
- id: generic-interface-family
  kind: interface
  appears_in: [BD-V-036, BD-V-044, BD-V-045, BD-V-046]
  description: A generic, nonfunctional wallet or explorer interface with empty or clearly sample fields. It uses no real learner data and preserves a consistent screen structure across receiving, sending, and verification.
  distinct_from: [wallet, ledger, payment-service, real-payment-interface]

- id: learner
  kind: actor
  appears_in: [BD-V-006, BD-V-012, BD-V-043, BD-V-044, BD-V-045, BD-V-047, BD-V-052, BD-V-054, BD-V-061, BD-V-069, BD-V-072, BD-V-091, BD-V-093]
  description: A generic person who learns, practises, makes decisions, or handles prepared material. The learner is not an educator, service, node, miner, or protocol component.
  distinct_from: [educator, service, wallet, node, miner, protocol]

- id: generic-wallet
  kind: prop
  appears_in: [BD-V-035, BD-V-036, BD-V-038, BD-V-039, BD-V-040, BD-V-041, BD-V-042, BD-V-043, BD-V-044, BD-V-045, BD-V-052, BD-V-059, BD-V-091]
  description: A wallet interface or signing environment, shown as a tool for receiving, sending, or key control. It never depicts bitcoin as physically stored inside it.
  distinct_from: [ledger, bitcoin-network, custodian, private-key, seed-phrase]

- id: educator
  kind: actor
  appears_in: [BD-V-056, BD-V-065, BD-V-066, BD-V-067, BD-V-089, BD-V-090, BD-V-091, BD-V-093, BD-V-094, BD-V-095, BD-V-097, BD-V-098]
  description: A generic person who facilitates, observes, prepares a safe route, or plans a module. The educator does not act as a node, miner, wallet, or payment service.
  distinct_from: [learner, service, wallet, node, miner, protocol]

- id: safety-stop
  kind: symbol
  appears_in: [BD-V-045, BD-V-047, BD-V-052, BD-V-072, BD-V-090, BD-V-095]
  description: A distinct stop marker for a mismatch, uncertainty, unsafe condition, or incomplete check. It means pause and verify, not failure or automatic loss.
  distinct_from: [warning-only, assessment-result, payment-failure]

- id: payment-request-qr
  kind: prop
  appears_in: [BD-V-036, BD-V-044, BD-V-045, BD-V-050, BD-V-059, BD-V-066, BD-V-074, BD-V-076]
  description: A QR-shaped payment or download request shown only when the brief requires it. It is clearly sample or points to the stated tested destination, as applicable.
  distinct_from: [private-key, seed-phrase, payable-learner-address, generic-square-pattern]

- id: custody-labels
  kind: notation
  appears_in: [BD-V-039, BD-V-040, BD-V-041, BD-V-042, BD-V-052, BD-V-096]
  description: The shared labels and visual distinction for custodial and self-custodial use, centred on who controls keys and recovery responsibility. They do not rank one arrangement as universally correct.
  distinct_from: [hot-cold-environment, hardware-device, wallet-interface]

- id: payment-pathway-symbols
  kind: symbol
  appears_in: [BD-V-048, BD-V-049, BD-V-058, BD-V-062, BD-V-063, BD-V-064]
  description: Reusable symbols for the stages and dependencies in an acquisition, exchange, payment, or conversion pathway. They keep local options editable and distinguish routes from recommendations.
  distinct_from: [investment-chart, provider-endorsement, universal-service-map]

- id: on-chain-lightning-layer-notation
  kind: notation
  appears_in: [BD-V-050, BD-V-051, BD-V-059, BD-V-066]
  description: A shared distinction between on-chain and Lightning payment layers, requests, results, and failure risks. It does not stand for wallet custody.
  distinct_from: [custody-labels, wallet-interface, payment-service]

- id: protocol-node-symbol
  kind: symbol
  appears_in: [BD-V-024, BD-V-026, BD-V-030, BD-V-031, BD-V-032, BD-V-100]
  description: A neutral network participant symbol used for independent verification and node-enforced rules. It is not a wallet, miner, service, or central controller.
  distinct_from: [miner, wallet, payment-service, central-authority]

- id: miner-symbol
  kind: symbol
  appears_in: [BD-V-026, BD-V-031, BD-V-032, BD-V-033]
  description: A distinct network-role symbol for proof-of-work block production. It never approves Bitcoin's rules or controls the network.
  distinct_from: [node, protocol, wallet, payment-service]

- id: fiat-system-actors
  kind: actor
  appears_in: [BD-V-014, BD-V-015, BD-V-016, BD-V-017, BD-V-019]
  description: A consistent set of central bank, commercial bank, government, citizens or businesses, and payment-service symbols. Each role remains separate because institutions and rules vary by country.
  distinct_from: [bitcoin-node, miner, wallet, universal-institution-model]

- id: local-resource-map-symbols
  kind: symbol
  appears_in: [BD-V-057, BD-V-065, BD-V-067, BD-V-068, BD-V-071]
  description: Editable map symbols for merchants, educators, meetups, technical support, exchange information, and missing support. A listing records verification, not trustworthiness.
  distinct_from: [provider-endorsement, personal-location, verified-safety-claim]

- id: private-material-boundary
  kind: notation
  appears_in: [BD-V-037, BD-V-038, BD-V-043, BD-V-091]
  description: A clear boundary that contains private keys, recovery material, or private learner actions. It makes visible what an educator or observer must not see.
  distinct_from: [public-address, payment-request, explorer-result]

- id: circular-economy-actors
  kind: actor
  appears_in: [BD-V-060, BD-V-065, BD-V-066, BD-V-096]
  description: Generic workers, customers, merchants, suppliers, educators or support, and conversion points used to map local value and responsibility. They are roles, not named local people or services.
  distinct_from: [bitcoin-protocol-roles, verified-local-provider, real-person]
```
