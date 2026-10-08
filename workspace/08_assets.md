# Bitcoin Diploma Asset Index

## Table of contents

- [Bitcoin Diploma Asset Index](#bitcoin-diploma-asset-index)
  - [Table of contents](#table-of-contents)
  - [Purpose](#purpose)
  - [How to use this index](#how-to-use-this-index)
  - [Asset types](#asset-types)
  - [Folder Structure and Naming Coventions](#folder-structure-and-naming-coventions)
  - [1. Rules](#1-rules)
    - [Asset rules](#asset-rules)
    - [Formatting rules](#formatting-rules)
    - [Design rules](#design-rules)
  - [2. Visual index](#2-visual-index)
    - [Visual index by guide section](#visual-index-by-guide-section)
  - [3. Style and branding](#3-style-and-branding)
    - [My First Bitcoin branding](#my-first-bitcoin-branding)
    - [Visual style](#visual-style)
    - [Guidelines](#guidelines)
  - [4. Placement](#4-placement)
    - [Assets that replace existing guide elements](#assets-that-replace-existing-guide-elements)
  - [5. AI Production Workflow \& Handoff](#5-ai-production-workflow--handoff)
    - [Make and review](#make-and-review)
    - [Reuse rules](#reuse-rules)
  - [6. Asset workflow](#6-asset-workflow)

## Purpose

An asset is a standalone visual in the Bitcoin Diploma. It can be a diagram, table, illustration, image, QR panel, or interface example.

Use an asset when a visual explains an idea, process, comparison, or safety step better than prose alone. Do not use assets as decoration.

## How to use this index

1. Find the asset in the visual index.
2. Read the adjacent guide text.
3. Make the asset described in the row.
4. Place it at the listed guide location. Use the exact heading and nearby text as the final anchor.
5. Add clear alt text. Update this index when the asset or its placement changes.

`SG` means Student Guide. `EG` means Educator Guide. Line numbers are quick finders, not permanent anchors.

## Asset types

| Type | Use it for |
|---|---|
| Diagram | A process, relationship, map, timeline, or system. |
| Table (Standalone) | A new comparison, checklist, or editable record that keeps the adjacent guide text. |
| Table (Replacement) | A comparison, checklist, or editable record that replaces an existing guide table. |
| Illustration | A concrete scene or everyday example. |
| Image | A logo, QR panel, or other simple graphic. |

A **Table (Standalone)** adds a new visual reference and keeps the adjacent guide text. A **Table (Replacement)** takes the place of an existing guide table. Every table asset row must use one of these two types.

## Folder Structure and Naming Coventions


Store each asset here:

```text
workspace/
└── 08_assets.md                 # master asset document

assets/
├── assets-list.md               # required asset filenames
├── Prompts/
│   ├── prompt-codex.md          # prompt used by Codex
│   └── prompt-claude.md         # prompt used by Claude
├── Briefs/
│   └── bd-v-###-brief.md        # one brief for each required asset
└── Reference/
    ├── bd-v-###-ref.json        # Codex reference record
    ├── bd-v-###-ref.svg         # Codex-generated SVG reference
    └── bd-v-###-ref.png         # Codex-generated PNG rendering
```

Use lowercase names and three digits: `bd-v-###-brief.md`, `bd-v-###-ref.json`, `bd-v-###-ref.svg`, and `bd-v-###-ref.png`.

Keep one brief per asset. Use the shared prompt files. Do not create extra asset folders or per-asset prompts.

This file covers guide visuals only. Put activity visuals on the [Resources Hub](https://programs.myfirstbitcoin.org/resources/). Keep ordinary tables and forms in the guide unless this index calls for a separate visual.

---

## 1. Rules

### Asset rules

- Teach one idea with plain labels, familiar objects, clear reading order, editable/translatable text, and useful alt text; it must work in color, grayscale, print, and on a phone.
- Use fictional interface/example data; label fictional payment screens and QR codes `SAMPLE — DO NOT PAY`.
- Date local facts and do not endorse tools or services.
- Do not add decoration without instruction, real secrets or personal/payment data, or live balances.
- Do not imply guaranteed, risk-free, or universally legal Bitcoin; do not show bitcoin in a wallet, miners making rules, or a single controller.
- Restricted-pilot My First Bitcoin App microlearning has no learner-facing download route. Do not create, place, or refer readers to an app download QR panel until public release.

### Formatting rules

- Use SG for learner visuals and EG for educator visuals; use the exact heading and text anchor, not line numbers.
- Keep adjacent text unless the entry says to replace it. An EG marker reserves its whole location until an approved visual replaces it.
- Write useful alt text, never a filename, and update this index if an anchor or visual meaning changes.
- `BD-V-076` is deferred pending public app release. It has no current placement.

Use this source marker:

```markdown
<!-- VISUAL: BD-V-001
SANITY: Required — add the approved official Creative Commons Attribution-ShareAlike 4.0 licence mark here during Sanity production.
ALT: Alt text that communicates the instructional meaning.
-->
```

Replace the marker only after approval. Use names such as `bd-v-001.svg` and keep an editable SVG master.

---

### Design rules

- Teach one idea, not decoration, using familiar people, objects, arrows, and comparisons; keep protocol, wallet, service, and person roles separate.
- Do not show bitcoin in a wallet, miners making rules, or one actor controlling Bitcoin; never show real secrets, payment details, learner data, or live balances.
- Mark fictional payment screens and QR codes `SAMPLE — DO NOT PAY`; do not promise returns, safety, adoption, or legal outcomes, and date local facts without endorsing tools or services.
- Use short, editable, translatable text. Work in color and grayscale, using labels, shapes, or patterns in addition to color.
- Check print and phone use, reading order, contrast, and alt text; follow the approved My First Bitcoin visual system.

---

## 2. Visual index

### Visual index by guide section

| Section / asset ID | Type | Suggested by | Priority | SG | EG | Purpose | Format | Description | Note |
|---|---|---|---|---|---|---|---|---|---|
| **Welcome and learning setup** |  |  |  |  |  |  |  |  |  |
| `BD-V-001` | Image | Pablo | Supporting | 13 |  | Gives the open licence a recognisable visual marker while leaving the written licence terms primary. | Official licence mark with short text lockup; small inline or corner placement. | Use the official Creative Commons BY-SA 4.0 mark at small but legible size. Keep the written licence statement, attribution requirement, and adaptation condition beside or immediately above it. Do not redraw, recolour, distort, or use the logo as a replacement for the licence text or link. | — |
| `BD-V-002` | Diagram | Pablo | Supporting | 48 |  | Makes “teach how to think, not what to think” into a repeatable learner action. | Horizontal process strip or circular loop; half page. | Show a six-step loop: identify the claim; separate fact from preference; inspect evidence and source; compare alternatives; name a trade-off or uncertainty; form a provisional conclusion or question. The loop must allow revision rather than ending in certainty. | — |
| `BD-V-076` | Deferred image | User | Deferred | — | — | Reserved for a future public app download route after release approval. | No current asset or placement. | Restricted-pilot microlearning has no public download route. Do not produce, link, print, or place this QR panel until public release. After approval, use the checklist in `18_horizon.md` to approve the destination, copy, accessibility, and placements before restoring this brief. | Reconsider only after the public app destination is live and tested. |
| `BD-V-077` | Diagram | User | Essential | 102 | 420 | Shows how the Bitcoin Diploma fits into a wider pathway from first learning to teaching and community participation. | Four-stage pathway diagram with editable text; full width. | Show [Introduction to Bitcoin](https://myfirstbitcoin.org/learn/programs#intro) → Bitcoin Diploma → [Educator Training Program](https://etp.myfirstbitcoin.org/) → Joining the Bitcoin Education Network. Link the final stage to the [Bitcoin Education Network](https://leaderboard.myfirstbitcoin.org) dashboard in digital versions. Add short labels: `Explore the basics`, `Build a beginner foundation`, `Develop teaching… | — |
| `BD-V-006` | Diagram | AI | Supporting | 146 |  | Shows how a learner moves through a typical concept rather than only reading it. | Five-step rhythm strip; half to full width. | Use the five stages in the current list: `Learn a key idea → Show what you can explain or apply → Apply the idea → Explain in your own words → Review the connection to the next module`. Keep discussion, safe practice, and offline participation available throughout. Do not turn this learning rhythm into an assessment score or imply that self-report proves competency. | — |
| `BD-V-003` | Diagram | AI | Essential | 234 | 478 | Clarifies that all four modules are the Bitcoin Diploma, while educators adapt Module 3 practice and curate the required Connect Module 4. | Layered pathway diagram; full width. | Show all four modules inside a `Bitcoin Diploma: all learners` container, labeled Problem → Solution → Action → Connect. Mark Modules 1–2 as shared core learning, Module 3 as educator-adapted practical learning, and Module 4 as `Connect: educator-curated local learning; required`. Show that Connect applies the earlier learning to a local need and realistic alternative. Show Advanced as a separate onward path. Use arrows to show… | — |
| `BD-V-004` | Diagram | AI | Essential | 241 |  | Gives learners a mental map of the Bitcoin Diploma before they enter Module 1. | Four-stage roadmap; full width. | Show one connected sequence: `1 Problem: Understanding Money → 2 Solution: How Bitcoin Works → 3 Action: Using Bitcoin Safely → 4 Connect: Bitcoin in Your Community`. Mark Modules 1–3 as shared learning and Module 4 as educator-curated, locally relevant, and required. Show that Connect links the first three stages to a local need, realistic alternative, safe task, and next step. Include each module's guiding question in… | — |
| `BD-V-005` | Table (Replacement) | AI | Supporting | 253 |  | Lets learners compare each Bitcoin Diploma module's role, guiding question, and promise at a glance. | Four-module reference table; full width. | Preserve the columns `Module`, `Role`, `Guiding question`, and `Learner promise`. Use four clearly separated, editable rows for Problem: Understanding Money, Solution: How Bitcoin Works, Action: Using Bitcoin Safely, and Connect: Bitcoin in Your Community. Mark Modules 1–3 as shared learning and Module 4 as educator-curated, locally relevant, and required for Bitcoin Diploma completion. | — |
| **Module 1: Understanding Money** |  |  |  |  |  |  |  |  |  |
| `BD-V-007` | Table (Replacement) | AI | Supporting | 317 |  | Gives learners a reusable set of questions for assessing whether a form of money is useful. | Icon-supported property-question table; full width. | Preserve durability, portability, divisibility, fungibility, scarcity, acceptability, and verifiability, each paired with its existing question. Add restrained, distinct icons only as supporting cues. Do not score currencies or name a universal winner. | — |
| `BD-V-008` | Diagram | Pablo | Essential | 324 | 1046 | Separates what money does from the qualities that make it useful. | Icon-led two-layer diagram; full width. | Use two linked layers. Layer 1 shows the three functions with small, simple icons: exchange arrows for medium of exchange; a price tag or measuring symbol for unit of account; and a clock with protected value for store of value. Layer 2 shows the seven properties: durability, portability, divisibility, fungibility, scarcity, acceptability, verifiability. Use cash, gold, and a generic digital monetary asset only as… | — |
| `BD-V-009` | Illustration | Pablo | Essential | 339 | 1078 | Makes the failed direct-exchange relationships in the prose visible. | Single three-role barter-mismatch illustration; full width. | Full-width, approachable flat-vector illustration of Amina (rice, wants shoes), Luis (shoes, wants cooking oil), and Mei (cooking oil, wants repair work), with clear broken arrows showing no direct exchange works; use editable localization-ready labels and objects, and include no money, Bitcoin, successful trade, or solution. | — |
| `BD-V-010` | Diagram | User | Essential | 356 | 1086 | Shows that a commonly accepted medium lets a person sell to one party and buy from another. | Single money-mediated exchange flow; half to full width. | Show Amina selling rice to one person for a generic commonly accepted medium, then using that medium to buy shoes from another person. Use a simple two-step sequence with distinct arrows for selling and buying. Keep names, goods, and the generic medium editable for localization. Do not use a specific currency, price, brand, wallet, QR code, or claim that money removes every exchange problem. | — |
| `BD-V-011` | Illustration | Pablo | Essential | 367 |  | Makes the same good's changing value and price clear through a concrete example. | Two-panel contextual-value illustration; half to full width. | Use two parallel images of the same quantity of clean water. Panel 1: near a safe public source, readily available, with an illustrative lower-price label. Panel 2: during a shortage, limited access and urgent need, with an illustrative higher-price label. State clearly that availability, need, and circumstances change value and price; do not imply that water scarcity or high prices are ethically acceptable. Keep people,… | — |
| `BD-V-012` | Illustration | Pablo | Supporting | 380 | 1112 | Connects three abstract choice concepts to one everyday decision. | Branching choice illustration; half page. | Show one person choosing between two uses of limited money or time. Label the chosen benefit, the best alternative forgone, the present-versus-future preference, and the resulting trade-off. Do not moralize the learner's choice or imply one time preference is always correct. | — |
| `BD-V-013` | Diagram | Pablo | Essential | 406 | 1134 | Prevents the history from appearing as one universal, inevitable sequence. | Braided or layered timeline; full-page width. | Create several overlapping tracks rather than one straight progress arrow: direct exchange and local records; commodity forms; standard coins; representative paper; bank and government money; modern fiat; digital fiat. Mark that different forms coexist and developed differently across places. Include 1971 only as a dated milestone in the modern-fiat track, not as the origin of all fiat money. | — |
| `BD-V-014` | Table (Replacement) | AI | Supporting | 433 |  | Clarifies the different roles of central banks, commercial banks, governments, and citizens or businesses. | Participant-and-role reference table; full width. | Preserve the four participant rows and their main roles. Use neutral role icons and editable text. Do not imply that every country has the same institutions, powers, or rules. | — |
| `BD-V-015` | Diagram | Pablo | Supporting | 428 | 1165 | Shows where trust, claims, and control sit in a fiat payment system. | Actor-and-flow system map; full width. | Map central bank, commercial bank, government, citizens and businesses, and payment services. Use distinct arrows for money or claims, policy or rules, taxes and spending, and payment instructions. Show that a bank deposit is the bank's liability to the customer. Avoid suggesting that every country has identical institutions or rules. | — |
| `BD-V-016` | Diagram | Pablo | Essential | 456 | 1190 | Makes deposit creation and the bank balance sheet clear without relying on a misleading money-multiplier story. | Numbered balance-sheet flow; full width. | Trace a simplified loan: bank approves loan; bank records a loan asset and a matching deposit liability; borrower can transfer the deposit; settlement and liquidity requirements remain. Label assets and liabilities on both sides. State `simplified example; exact rules vary`. Do not show banks lending out the same physical deposit repeatedly. | — |
| `BD-V-017` | Table (Standalone) | Pablo | Essential | 470 | 1203 | Prevents learners from treating liquidity and solvency as the same problem. | Side-by-side balance-sheet comparison; half to full width. | Show two parallel simplified bank snapshots. In the liquidity case, assets exceed liabilities but too little is immediately available. In the solvency case, asset value is below liabilities. Use small round example numbers and label them as fictional. | — |
| `BD-V-018` | Illustration | Pablo | Essential | 487 | 1234 | Shows the inverse relationship between a rising basket price and what a fixed amount of money can buy. | Before-and-after quantity illustration; full width. | Use the same fixed amount of currency at two dates. At Date A it buys the full basket; at Date B the basket costs more and the fixed amount buys less. Distinguish `price level` from `purchasing power`. Use fictional or sourced-and-dated local values; never mix the two. | — |
| `BD-V-020` | Table (Replacement) | AI | Supporting | 520 |  | Helps learners compare why an asset may be chosen alongside its important trade-offs. | Alternatives trade-off table; full width. | Preserve precious metals, real estate, and stocks with columns for `Why people may choose it` and `Important trade-offs`. Add simple, non-promotional icons. Do not add investment advice, price predictions, or a best-choice ranking. | — |
| `BD-V-021` | Diagram | AI | Supporting | 527 |  | Reinforces that each alternative serves some purposes while introducing different constraints. | Trade-off landscape; full width. | Place cash, precious metals, real estate, stocks, and Bitcoin around the needs `daily payment`, `long-term saving`, `portability`, `income or productive use`, and `direct control`. Use qualitative callouts, not a ranked score or investment recommendation. | — |
| `BD-V-019` | Table (Standalone) | AI | Supporting | 546 | 1302 | Clarifies that digital, centralized, decentralized, private, and scarce are different attributes. | Layered comparison matrix with icons; full width. | Compare physical cash, commercial-bank digital deposits, a generic retail CBDC, and Bitcoin across issuer or controller, form, access permission, visibility, supply-rule control, and independent verifiability. Mark CBDC features as design-dependent. Do not imply that all CBDCs have identical surveillance or control features. | — |
| **Module 2: How Bitcoin Works** |  |  |  |  |  |  |  |  |  |
| `BD-V-022` | Diagram | AI | Essential | 597 | 1434 | Contrasts a central ledger keeper with Bitcoin's distributed verification model. | Two-system comparison diagram; full width. | Left panel: sender and receiver depend on one intermediary that keeps and approves the ledger. Right panel: signed transactions propagate to independent nodes; miners propose blocks; nodes verify the same public rules. Emphasize reduced dependence on a central settlement authority, not removal of all trust. | — |
| `BD-V-023` | Diagram | AI | Supporting | 618 |  | Shows that Bitcoin combined prior ideas rather than appearing without context. | Converging idea timeline; full width. | Create an idea lineage with DigiCash, Hashcash, Bit Gold, B-money, reusable proof of work, and peer-to-peer file sharing feeding distinct contributions toward Bitcoin. Label contributions carefully; do not imply that every project directly supplied code or that Bitcoin has one intellectual predecessor. | — |
| `BD-V-024` | Diagram | AI | Essential | 651 | 1468 | Explains how a conflicting second spend is resolved without a central database. | Five-feature conflict-resolution flow; full width. | Begin with one spendable output and two conflicting payment attempts. Show the five linked features from the text: peer-to-peer announcement; digital signatures; blocks and mining; independent verification; and a shared valid history with the most accumulated proof of work. Show the conflicting second spend rejected. Do not imply that one miner decides validity or that the longest chain is accepted regardless of its validity. | — |
| `BD-V-027` | Diagram | AI | Supporting | 666 |  | Distinguishes a written supply claim from a supply rule independently enforced in practice. | Credibility comparison diagram; half to full width. | Compare `claim on a website or issuer database` with `public rule checked by many independent nodes`. Show that signatures, transaction history, proof of work, and node verification jointly prevent invalid creation or double spending. Avoid saying that scarcity alone creates value. | — |
| `BD-V-026` | Diagram | AI | Essential | 697 | 1500 | Makes the distribution and limits of participant power visible. | Roles-and-rules network map; full width. | Place users, nodes, miners, developers, and services around the shared protocol and public ledger. For each, show `can do` and `cannot do unilaterally`. Services must sit outside the protocol boundary. Show unequal influence and points of dependence without adding a central controller. | — |
| `BD-V-030` | Diagram | AI | Supporting | 716 |  | Separates direct settlement rules from the communications and service infrastructure a transaction may pass through. | Layered transfer-path diagram; full width. | Show sender wallet → network peers → recipient wallet, with optional exchange, hosted wallet, payment service, and internet provider around the path. Use different line styles for transaction propagation, custody, and communications. The presence of network infrastructure must not be mistaken for central approval. | — |
| `BD-V-031` | Diagram | AI | Essential | 739 | 1518 | Gives beginners a durable model of who does what in Bitcoin. | Participant role map; full width. | Show users signing or accepting transactions; nodes validating and relaying; miners assembling candidate blocks and performing proof of work; developers proposing software; services serving customers. Then show the checks among roles. Do not label all wallet users as nodes or developers as rule-makers. | — |
| `BD-V-032` | Diagram | Pablo | Essential | 763 | 1548 | Makes costly-to-produce and easy-to-verify work visible. | Sequential process diagram; full width. | Show candidate block data entering repeated hash attempts; many results miss the target; one result meets it; the miner broadcasts the block; nodes quickly verify proof and all other rules; accepted blocks add accumulated work. Include difficulty adjustment as a small feedback loop. Do not depict mining as solving an externally useful puzzle. | — |
| `BD-V-028` | Diagram | Pablo | Essential | 794 | 1576 | Separates maximum supply, issuance, block subsidy, halving, and miner fees. | Paired issuance chart; full width. | Show a descending step chart for block subsidy by halving era and a rising cumulative issuance curve approaching 21 million. Mark halvings by block height or era and `roughly four years`, not guaranteed calendar dates. Show transaction fees separately from new issuance. Include no price curve or adoption prediction. | — |
| `BD-V-029` | Table (Replacement) | Pablo | Essential | 821 | 1605 | Makes divisibility intuitive and counters the belief that a learner needs one whole bitcoin. | Illustrated denomination reference table; half to full width. | Start with `1 BTC = 100,000,000 sats`, then zoom into 0.1 BTC, 0.01 BTC, 0.001 BTC, and 1 sat. Show that differently displayed amounts can represent the same value, using `100,000 sats = 0.001 BTC`. Do not show a current fiat price. | — |
| `BD-V-033` | Table (Replacement) | Pablo | Essential | 850 |  | Makes each monetary property concrete without treating Bitcoin as universally superior. | Icon-supported properties table; full width. | Retain a learner-friendly table with one small icon and concise plain-language explanation for each property: durability, portability, divisibility, fungibility, scarcity, verifiability, and acceptability. State the relevant qualification already in the text, especially that acceptance varies and public history can affect how services treat particular funds. Do not turn the properties into a total score or claim that… | — |
| `BD-V-025` | Table (Replacement) | Pablo | Essential | 910 |  | Connects the four historical events to why each matters. | Illustrated four-milestone reference table; full width. | Show 31 Oct 2008 whitepaper; 3 Jan 2009 Genesis Block; 12 Jan 2009 first recorded person-to-person transaction; 22 May 2010 Pizza Day. Pair each event with a short significance line. Use document-style illustrations or rights-cleared source images only; avoid portraits or identity speculation for Satoshi. | — |
| `BD-V-034` | Table (Replacement) | Pablo | Essential | 948 |  | Reconnects the entire Module 2 explanation to the Module 1 problems and the new responsibilities introduced by Bitcoin. | Bridge diagram or visual table; full width. | Preserve the three current columns and all five rows: supply policy; intermediary dependence; central ledger control; institutional access; and ordering digital payments. Retain the corresponding responsibilities for rule verification, irreversible errors, privacy, key protection, and mining equipment and energy. Do not label the middle column `perfect solution` or add unsupported promises. | — |
| **Module 3: Using Bitcoin Safely** |  |  |  |  |  |  |  |  |  |
| `BD-V-035` | Diagram | AI | Essential | 996 | 1859 | Corrects the most important beginner wallet misconception. | Conceptual layer diagram; full width. | Show the Bitcoin ledger as the record of spendable outputs; the wallet holding or managing keys and constructing instructions; the user authorizing an action; and the network verifying it. Do not draw coins sitting inside a phone or hardware device. | — |
| `BD-V-036` | Diagram | Pablo; User | Essential | 1009 |  | Shows that the alphanumeric address and QR code represent the same public receiving information; neither is a private key or a recovery phrase. | Side-by-side text-to-QR diagram with editable labels; half to full width. | Show the full My First Bitcoin test address as readable, untruncated text beside a QR code encoding exactly that address, joined by the label `Same address, two formats`. Use [BLANK] for the official test address and [BLANK] for the exact test-network name until My First Bitcoin supplies and approves both values; do not generate a QR until TODO AST-001 is resolved. Do not invent an address or substitute a live donation… | Pablo: add an address/QR graphic, explain who creates addresses, and show address checks. User: show a My First Bitcoin test address as alphanumeric text and its matching QR code. |
| `BD-V-078` | Diagram | User | Essential | 1018 |  | Shows how a Lightning invoice carries a payment request and how its readable details relate to the QR code; complements the on-chain address example in `BD-V-036`. | Side-by-side invoice-and-QR diagram with editable labels; full width. | Show a My First Bitcoin test Lightning invoice as a readable payment-request panel on the left and its matching QR code on the right, joined by `Same payment request, two formats`. Include recipient `My First Bitcoin — test`, payment method `Lightning`, confirmed test network, amount with an explicit unit, description, expiry, and the invoice string labelled `Lightning payment request`. Use the invoice string as the… | Show an invoice with its amount, destination, and other payment details beside its matching QR code. |
| `BD-V-037` | Diagram | Pablo; User | Essential | 1045 | 1976 | Reinforces the rule “Public receiving information can be shared. Private spending information must remain secret” by showing how public information relates to a secret private key. | One-way key-relationship diagram with a prominent private-key warning and a supporting signing branch; full width. | Show `Private key → Public key → Receiving address`, with the first arrow labelled `Derived from` and the address step labelled `Created from public-key information`. Place the private key inside a clearly marked secret boundary. Add a prominent warning beside it: `Never share your private key. Anyone with it can spend your bitcoin.` Use a warning symbol and readable text so the warning works in grayscale. Label the… | — |
| `BD-V-038` | Diagram | AI | Essential | 1056 | 1994 | Places the seed phrase correctly in the recovery chain without teaching that every wallet uses an identical recovery method. | Recovery relationship diagram; half to full width. | Show seed or wallet backup → wallet recreates keys → expected addresses and transaction access return. Mark the backup as secret and offline. Add `method and compatibility depend on the wallet`. Do not show actual words, screenshots of recovery entry, or educator access. | — |
| `BD-V-079` | Illustration | User | Essential | 1072 |  | Makes writing a private, offline backup concrete and reinforces preserving word order and spelling. Complements the recovery relationship in `BD-V-038`. | Screen-to-paper illustration with numbered placeholders, editable labels, and a prominent safety warning; half to full width. | Show one person privately copying a 12-word seed phrase from a generic wallet backup screen onto paper with a pen. Show twelve clearly numbered positions on both screen and paper, in the same reading order, using matching placeholders `WORD 01` through `WORD 12` rather than an actual recovery phrase. Depict the hand completing the final entry; use a simple directional cue from screen to paper and a callout `Check every… | — |
| `BD-V-039` | Diagram | AI | Essential | 1085 | 2053 | Makes custody a question of key control rather than interface appearance. | Side-by-side custody model; full width. | Left: user logs into a service; service controls keys and authorizes withdrawal. Right: user controls keys; wallet signs under the user's authority; network checks the transaction. Show recovery responsibility and failure point in both paths. Avoid portraying self-custody as morally superior or risk free. | — |
| `BD-V-040` | Table (Replacement) | AI | Supporting | 1096 |  | Makes key control, recovery, and failure points comparable without moralising either model. | Custody comparison table; full width. | Preserve the current rows `Who holds the keys?`, `Who handles recovery?`, and `Main trade-off`, with the custodial and self-custodial explanations. Use neutral icons and editable text. Do not add a recommendation badge or treat either model as risk free. | — |
| `BD-V-042` | Diagram | Pablo | Supporting | 1111 | 2070 | Connects wallet type to exposure and use rather than treating `hot`, `cold`, and `custodial` as one scale. | Two-axis classification graphic; full width. | Use two axes or layers: key control (`custodial` versus `self-custodial`) and connectivity or signing environment (`hot` versus `cold or hardware`). Place common use patterns and threat examples in the correct areas. Explicitly show that a custodial account is not a type of self-custodial wallet. | — |
| `BD-V-041` | Table (Replacement) | AI | Supporting | 1122 |  | Prevents learners from treating custody and connectivity as one scale. | Wallet-use comparison table; full width. | Preserve the current columns and the rows for hot wallet, hardware or cold wallet, and custodial account. Distinguish key control from signing environment; use the qualifications in `BD-V-042` to prevent treating custody and connectivity as one scale. Preserve one common strength and one responsibility for each arrangement. | — |
| `BD-V-043` | Diagram | Pablo | Essential | 1144 |  | Turns the recovery text into a safe sequence a learner can rehearse. | Safety-gated workflow; full width. | Follow the six current steps: use official instructions for the exact training wallet; confirm compatibility; work privately; use the approved backup-check or recovery method; confirm expected receiving information or training history; reset or clear the temporary environment. Use only prepared, empty, or simulated materials. Put `educator never sees the secret` outside every step. Do not instruct learners to erase a… | — |
| `BD-V-044` | Illustration | AI | Essential | 1163 | 2094 | Lets a learner identify the elements of a receive request before live practice. | Annotated receiving flow; full width. | Show receiver device, sample address or QR, sender verification, broadcast or pending status, and confirmation. Annotate amount, unit, network, address, and status. Use fictional data and mark the whole visual non-payable. | — |
| `BD-V-045` | Diagram | AI | Essential | 1183 | 2128 | Makes verification happen before approval and separates recipient checks from fee and timing decisions. | Preflight-to-settlement flow; full width. | Show independently verified recipient and purpose → payment method → scan or copy and compare destination → check amount, unit, fee or expiry, and final summary → small test when unfamiliar → approve only if all checks match → check the result. Branch to stop and verify if anything differs. For on-chain payments, show pending/confirmation status and a sample txid; for Lightning, show success or failure without implying an… | — |
| `BD-V-046` | Diagram | Pablo | Essential | 1202 | 2175 | Connects transaction status, block inclusion, and later confirmations. | Confirmation timeline plus explorer inset; full width. | Show a transaction first in the pending pool, then included in Block N as confirmation 1, followed by Blocks N+1, N+2, and N+3 increasing depth. Pair it with a small annotated fictional explorer panel showing *txid*, amount, fee, status, and confirmations. Add a privacy callout about searching personal data. | — |
| `BD-V-047` | Illustration | Pablo | Supporting | 1211 | 2209 | Gives learners an immediate visual cue to pause when a message or offer shows scam signals. | Red-flag scam-warning illustration; half width. | Show a prominent red flag beside a generic, nonfunctional message or offer. Add concise warning cues for impersonation, urgency, guaranteed returns, giveaway or recovery requests, fake applications, phishing, relationship manipulation, and too-good-to-be-true claims. Include the action `stop, verify independently, and never share a seed phrase or private key`. Do not use a real brand, address, payment request, or a… | — |
| `BD-V-048` | Diagram | Pablo | Supporting | 1234 | 2251 | Shows that acquiring bitcoin is an end-to-end route with risks before and after the moment of exchange. | Branching pathway map; full width. | Map earning, peer-to-peer, exchange or broker, ATM or kiosk, and merchant or community receipt as separate paths into either self-custody or custodial balance. Label price or spread, fees, identity, reversibility, counterparty, withdrawal, and local-law checkpoints. Do not rank or recommend a provider. | — |
| `BD-V-049` | Table (Replacement) | Pablo | Essential | 1248 |  | Helps learners assess a complete acquisition or exchange route instead of focusing only on price. | Icon-supported risk-check table; full width. | Preserve the six existing risk-area rows and their questions: costs; custody; identity and privacy; withdrawal and settlement; counterparty and safety; local context. Keep each question editable, neutral, and locally verifiable. Include no provider names, rankings, or legal conclusions. | — |
| `BD-V-050` | Diagram | Pablo | Essential | 1257 | 2275 | Makes the layer relationship and appropriate-use distinction visible. | Layer diagram plus concise comparison; full width. | Show Bitcoin base-layer settlement beneath Lightning payment channels. Compare payment request, route, timing, fee conditions, custody variability, and failure modes. Use one small-payment and one final-settlement example. Do not imply that Lightning is a separate coin or that all Lightning wallets are self-custodial. | — |
| `BD-V-051` | Table (Replacement) | AI | Supporting | 1271 |  | Lets learners compare payment requests, settlement, timing, fees, typical use, and introductory risks across the two paths. | Payment-path comparison table; full width. | Preserve the four current rows: receiving information, payment result, common use, and beginner checks. Keep invoice, offer, and supported Lightning-address wording, plus expiry and payment-result checks. Retain custody and fee qualifications from the adjacent prose. Do not imply that Lightning is a separate coin or that either path is universally better. | — |
| `BD-V-052` | Diagram | Pablo | Supporting | 1288 |  | Synthesizes the module as responsibilities surrounding key control. | Responsibility map; full width. | Put `control of keys` in the center, surrounded by backup, recovery, receiving, sending, tool choice, acquisition path, privacy, and scam checks. For each, show the protected item and the consequence of failure in very short text. | — |
| `BD-V-053` | Table (Standalone) | AI | Supporting | 1293 |  | Connects each task with what must be protected or checked and the consequence of failure. | Responsibility reference table; full width. | Use rows for backup, receiving, sending, custody, tool choice, and acquisition. Keep language practical and non-alarmist. | — |
| **Module 4: Bitcoin in Your Community** |  |  |  |  |  |  |  |  |  |
| `BD-V-055` | Table (Replacement) | AI | Supporting | 1313 |  | Gives learners one place to record the module, local problem, tool or scenario, benefit, risk, evidence, and safe next step. | Editable Module 4 record table; full width. | Preserve all seven local-learning-choice prompts and a generous editable notes column. Make it printable and reusable by different educators. Do not pre-fill a local tool, provider, or conclusion. | — |
| `BD-V-054` | Diagram | AI | Essential | 1340 |  | Connects the four learner actions to local purpose, educator support, and safe choice. | Four-stage local-learning diagram; full width. | Show the four learner actions `Connect → Compare → Practise safely → Explain`. Link shared earlier learning to a local need and realistic alternative, educator-selected safe practice, and a responsible next step. Show the educator and, where needed, a local expert supporting the learner. Keep required competencies and safety boundaries fixed. Detailed educator planning and verification remain in the Educator Guide. | — |
| `BD-V-056` | Diagram | Pablo | Supporting | 1371 | 875 | Shows how a safe practical skill develops from educator explanation to guided learner practice and then independent performance or explanation. | Three-stage PPP flow diagram; full width. | Create three connected sections in a clear left-to-right or top-to-bottom sequence: `Presentation` — educator shows the full process and explains purpose, terms, and risks; `Practice` — learner follows a guided process using printed screens, a test environment, or a very small amount; `Production` — learner completes a defined task or explains a decision independently. Add simple safety cues for no funds, test funds, or… | — |
| `BD-V-057` | Table (Replacement) | Pablo | Supporting | 1403 |  | Helps learners see that an interface belongs to a custody, network, and support context. | Local tool evaluation table; full width. | Preserve purpose, custody, source, code, recovery, privacy, cost, compatibility, support, and law as editable rows with a `What to verify` column. Record the date checked. Do not show an approved-products badge or a globally recommended wallet. | — |
| `BD-V-058` | Table (Replacement) | AI | Supporting | 1408 |  | Helps learners record what was checked about a tool without treating it as a global recommendation. | Editable local-tool record table; full width. | Preserve the rows for tool and version, date checked, custody model, main use, benefit, risk, recovery method, and alternative. Keep all fields editable and date-stamped. Do not use an endorsement badge or provider ranking. | — |
| `BD-V-080` | Diagram | User | Essential | 1447 |  | Connects an email-like Lightning address with its scannable payment destination, while distinguishing it from an email account, an on-chain address, and a specific Lightning invoice. | Side-by-side Lightning-address-and-QR diagram with editable labels; half width. | Show the full Lightning address as readable, selectable text beside a QR code for the same destination, joined by `Same Lightning address, two formats`. Use [BLANK] for the Lightning address until My First Bitcoin supplies and approves an active, controlled destination; do not publish a working QR until TODO AST-003 is resolved. Generate a wallet-compatible Lightning QR for the confirmed address, not a `mailto:` link,… | Show a Lightning address such as `donate@myfirstbitcoin.org` beside its matching QR code. |
| `BD-V-059` | Diagram | AI | Supporting | 1452 | 2635 | Makes a Lightning payment sequence clear while keeping custody and failure risk visible. | Lightning payment sequence; full width. | Show receiver creates request; sender scans or copies; sender verifies recipient, amount, unit, expiry, and fee; sender approves; payment routes; both wallets report success or failure. Add custody labels on both wallets and a branch for failure. Use generic, nonfunctional screens. | — |
| `BD-V-060` | Diagram | Pablo | Supporting | 1487 |  | Makes the seven distinct ways Bitcoin may be used in daily life quick to identify without suggesting that every learner should use it in every way. | Seven-icon daily-use illustration; full width. | Create seven equally weighted illustrative icons, each clearly labelled: earning, saving, receiving, sending, spending, pricing and accounting, and donating. Arrange them in a clear row, grid, or gentle sequence; do not make the icons form a compulsory circular process. Use familiar, culturally adaptable symbols and no provider branding. | — |
| `BD-V-061` | Illustration | AI | Supporting | 1518 |  | Gives all local scenarios one reusable visual grammar so educators can substitute local actors and goods. | Reusable scenario storyboard; full width. | Create a four-frame template: need and actors; payment request and chosen path; verification and settlement; record, refund, custody, or conversion. Include editable slots for small purchase, work payment, family transfer, refund, or donation. The template must work with simulation or tiny value. | — |
| `BD-V-062` | Diagram | AI | Essential | 1579 | 2771 | Forces comparison of the complete route rather than only the advertised first fee. | End-to-end pathway map; full width. | Show local money, work, goods, or services entering through possible routes; custody and identity checkpoints; on-chain or Lightning transfer; self-custody or service balance; and final use, holding, or conversion. Label spread, fees, time, reversal, withdrawal, counterparty, privacy, support, and law along the route. | — |
| `BD-V-063` | Table (Replacement) | AI | Supporting | 1584 |  | Helps learners compare received value, time, custody, privacy, reversal risk, and failure points across local options. | Editable pathway-comparison table; full width. | Preserve the editable rows for local option A, local option B, and an existing non-Bitcoin option, plus all comparison columns. Do not pre-fill services, rates, or legal claims. | — |
| `BD-V-064` | Table (Replacement) | AI | Supporting | 1615 |  | Frames KYC and no-KYC as different bundles of benefits and risks, not as good versus bad. | Balanced trade-off comparison; full width. | Preserve all eight questions in the existing comparison table: identity data collected; storage and retention; on-chain linkability; fraud protection; counterparty risk; limits and fees; local law; dispute handling. Leave the two answer columns editable for a dated local comparison. Include `local law varies; verify current information`. Do not imply evasion or guaranteed privacy. | — |
| `BD-V-065` | Diagram | AI | Essential | 1645 | 2797 | Shows value circulating among participants and reveals where the loop depends on outside services or support. | Editable local network map; full width. | Map workers, customers, merchants, suppliers, educators or support, and exchange or on/off-ramp points. Use separate arrows for value, goods or services, and support. Mark custody, volatility, connectivity, and conversion dependencies. Include broken-loop examples such as immediate conversion or one organizer processing everything. | — |
| `BD-V-066` | Diagram | Pablo | Supporting | 1672 | 2724 | Shows that accepting Bitcoin is an operational process, not just displaying a QR code. | Merchant payment operations flow; full width. | Trace pricing → payment request → customer verification → merchant confirmation → receipt or record → custody or conversion → refund or exception. Add staff, accounting, tax, device security, offline failure, and support callouts. Use local-law placeholders, not assertions. | — |
| `BD-V-067` | Diagram | AI | Supporting | 1709 |  | Connects community discovery with verification and privacy rather than treating a map listing as proof. | Local resource-map template; full width. | Provide an editable neighborhood or regional map template with merchant, educator, meetup, technical support, exchange information, legal or tax information, and missing-support markers. Every listing includes `date verified` and a safety note. Do not include real personal locations without consent. | — |
| `BD-V-068` | Table (Replacement) | AI | Supporting | 1714 |  | Helps learners document useful local support while recording when information was checked. | Editable local-resource record table; full width. | Preserve rows for education group, merchant directory, technical support, local exchange information, and legal or tax information, with purpose, verification date, contact or location, and safety note columns. Do not pre-fill personal locations or imply trustworthiness from a listing. | — |
| `BD-V-069` | Diagram | AI | Supporting | 1746 |  | Summarizes the community review as a sequence that begins with a need and ends with evidence and a responsible next step. | Decision path; full width. | Show the decision path `real need → Bitcoin fit → payment method → custody → total cost and trade-offs → safety and local conditions → evidence of success`. Add a return arrow when Bitcoin is not the best available fit. | — |
| `BD-V-070` | Table (Standalone) | AI | Conditional | 1751 |  | Offers a concise optional text equivalent for the community-review decision path. | Optional community-review summary table; full width. | If a table is clearer than `BD-V-069`, summarize the current review using rows for local need, function of money, realistic alternative, payment path, key control, benefit and risk, local conditions, and responsible next step. Use editable prompts rather than inventing a required test or assessment record. Keep any learner response space optional; formal evidence belongs in the educator assessment process. | — |
| **Back of Bitcoin Diploma** |  |  |  |  |  |  |  |  |  |
| `BD-V-071` | Diagram | AI | Supporting | 1792 |  | Makes the current community, contribution, and educator pathways visible as voluntary next steps. | Next-step pathway map; full width. | Show optional routes to connect with a learning community, learn or volunteer, contribute through the official forms, explore the Educator Training Program, or explore network participation for an existing education community. Reuse the pathway language of `BD-V-077` without implying automatic teaching eligibility or network membership. Do not depict [Advanced modules](https://curriculum.myfirstbitcoin.org/programs/advanced-modules/) as currently available. | — |
| `BD-V-072` | Diagram | Pablo | Essential | 1801 | 3316 | Makes the minimum stop-and-check behavior memorable at the point of course completion. | Compact safety strip; half to full width. | Show `stop → verify source and recipient → verify custody, network, destination, amount, and fee → start small → proceed only when understood`. Put seed or private-key secrecy above the whole sequence as a non-negotiable boundary. | — |
| `BD-V-073` | Image | Pablo | Supporting | 1823 |  | Provides one durable route to updates and contributions without filling the Bitcoin Diploma with fragile QR codes. | QR and fallback-link panel; half page. | Create one panel containing a tested QR code, printed short URL, destination name, edition or last-verified date, and plain-language purpose. The QR must resolve to the canonical maintained source: `https://github.com/MyFirstBitcoin/mfb-curriculum`. Keep donation and any future educator or issuer-specific certificate verification separate unless the landing page clearly distinguishes them. Do not imply a central My First… | — |
| `BD-V-074` | Image | Pablo | Supporting | 1848 |  | Offers the single official support-page route described in the guide, with a readable fallback and voluntary participation. | Single support-page QR panel; half width. | Create one optional support panel with a QR code linking to the approved destination `https://donate.myfirstbitcoin.org/`, the readable matching URL, destination name, and last-verified date. Keep the adjacent donation-safety paragraph. Do not encode a payment address or invoice in this website QR or imply that a donation is required. Test the destination and final printed QR before publication. The historical… | — |
| `BD-V-075` | Diagram | AI | Conditional | — |  | Retained only as a possible future issuer-specific verification concept; it is not part of the current publication set. | Deferred verification flow; no current asset. | Do not produce for 2026.10. Certification is educator-issued and My First Bitcoin does not operate a central verification service. The [Certificate Tool](https://tools.myfirstbitcoin.org/certificate) may prepare educator-confirmed certificates in batches, but it is not a verification service and requires no QR asset. A future separately governed issuer-specific method may revive this brief only after its real destination, privacy controls, correction and withdrawal rules, and minimum data display are approved and tested. It must identify the actual educator or issuing organization and must not imply central… | — |

| **Educator-only assets** |  |  |  |  |  |  |  |  |  |
| `BD-V-081` | Diagram | AI | Essential |  | 43 | Makes the two separately required evidence components and their joint completion condition unmistakable. | Flow diagram; full width. | Two equal lanes: theory C1–C5 and practice C6–C7. Both require a Yes for showing competency. Not yet returns to practice and building competency. | — |
| `BD-V-082` | Diagram | AI | Essential |  | 70 | Connects cohort size, observation time, assessor capacity, and the advertised course route. | Flow diagram; full width. | Learner count × minutes per learner ÷ approved assessors. Include setup, feedback, access needs, and reassessment. Change the plan if it does not fit. | — |
| `BD-V-083` | Diagram | AI | Essential |  | 94 | Explains the relationship among task IDs, competency IDs, decimal criteria, and the Assessment Grid. | Task-to-competency map with one nested criterion example; full width. | Map T1–T3 to C1–C5 and P6a–P7 to C6–C7. Show criteria feeding one Yes or Not yet record. Use no learner data. | — |
| `BD-V-084` | Diagram | AI | Essential |  | 104 | Separates access support and safety intervention from prompting that supplies the answer. | Two-stage support-boundary diagram; half to full width. | Show permitted support before and during evidence. Keep the learner’s explanation, choices, and actions inside a clear no-help boundary. | — |
| `BD-V-085` | Diagram | AI | Essential |  | 202 | Distinguishes the learner reassessment loop from assessor calibration and cohort moderation. | Three-lane process diagram; full width. | Show three lanes: learner reassessment, assessor calibration, and cohort moderation. Do not lower the standard or replace direct observation. | — |
| `BD-V-086` | Diagram | AI | Essential |  | 389 | Makes resource ownership and the route from teaching to recorded evidence visible. | Resource relationship map; full width. | Map Student Guide, Educator Guide, Resources Hub, protocol, and Assessment Grid. Keep independent review outside certification evidence. | — |
| `BD-V-087` | Diagram | AI | Essential |  | 452 | Shows what educators can adapt while preserving the same Bitcoin Diploma standard. | Three-region boundary diagram with an equivalence gate; full width. | Show fixed standards, adaptable teaching choices, and flexible choices with limits. Assessment changes need an approved equivalent route. | — |
| `BD-V-099` | Diagram | AI | Essential |  | 706 | Connects changing local claims to dated sources, classroom wording, and a fallback. | Verification lifecycle with an uncertainty branch; full width. | Show: identify claim → verify source → record date and limit → teach → recheck. Use a safe fallback when facts are uncertain. | — |
| `BD-V-088` | Diagram | AI | Essential |  | 729 | Makes the educator’s eight-step teaching cycle quick to follow and repeat. | Eight-stage cycle in two readable rows; full width. | Show Purpose → Activate → Explain → Check → Apply → Produce → Debrief → Connect. Allow a return to explain or practise. | — |
| `BD-V-101` | Diagram | AI | Essential |  | 770 | Makes the educator’s use of changed conditions visible as a test of transferable reasoning. | Decision path with a changed-condition return loop; full width. | Show goal → facts to verify → control → options → smallest safe next step. Change one condition, then reconsider the decision. | — |
| `BD-V-089` | Diagram | AI | Essential |  | 841 | Shows why changing the medium must preserve the learner’s action and observed evidence. | Branch-and-rejoin equivalence diagram; full width. | Show live tools, paper simulations, and accessible routes joining at the same learner action, evidence, and standard. | — |
| `BD-V-090` | Diagram | AI | Essential |  | 907 | Turns the safety triggers into an educator response rather than a list to memorize. | Flow diagram; full width. | Show unsafe trigger → stop → protect → verify → safe route or postpone. Keep the formal-assessment Not yet branch separate. | — |
| `BD-V-100` | Diagram | AI | Essential |  | 1632 | Helps educators explain similar-looking interfaces backed by different control and verification relationships. | Three-lane dependency diagram; full width. | Compare Bitcoin, a generic stablecoin, and a generic other asset using control, supply support, verification, and counterparties. Keep service risk separate. | — |
| `BD-V-092` | Diagram | AI | Essential |  | 1931 | Makes address reuse and the limits of public-data inference visible without exposing anyone’s transactions. | Two-panel linkage diagram with an explorer privacy inset; full width. | Compare address reuse with fresh addresses. Show linkage risk and explorer privacy. Use fictional labels only. | — |
| `BD-V-091` | Diagram | AI | Essential |  | 2003 | Separates what the learner controls from what the educator may observe during recovery practice. | Two-lane privacy-boundary workflow; full width. | Show the learner’s private recovery work and the educator’s observation lane. The educator must not see secrets. | — |
| `BD-V-093` | Diagram | AI | Essential |  | 2293 | Shows how station rotation supports practice without confusing group participation with assessment. | Station layout and separate observation lane; full width. | Show teacher-led, peer, and independent practice routes. Each must keep learner action and safety clear. | — |
| `BD-V-094` | Diagram | AI | Essential |  | 2410 | Gives educators a map of the seven-step planning process before its detailed subsections. | Seven-stage planning map; full width. | Show a ready-to-teach check: people, materials, local facts, safety, access, and assessment route. Fix gaps before delivery. | — |
| `BD-V-095` | Diagram | AI | Essential |  | 2526 | Shows that every readiness condition must be satisfied before live delivery. | Flow diagram; full width. | Show a live-practice readiness check. Any gap leads to a safer route or a revised plan. | — |
| `BD-V-096` | Diagram | AI | Essential |  | 2809 | Reveals who controls shared funds and which responsibilities remain separate. | Role-and-responsibility map with distinct arrow types; full width. | Map contributors, beneficiaries, key control, payment approval, records, and review. Flag concentrated control. Do not show real funds or setup. | — |
| `BD-V-097` | Diagram | AI | Essential |  | 2978 | Shows translation as a review-and-test process, not a one-way text conversion. | Flow diagram; full width. | Show prepare → translate → review → learner test → confirm. Return to wording when safety instructions are unclear. | — |
| `BD-V-098` | Diagram | AI | Essential |  | 3175 | Distinguishes freedom to adapt practice from the conditions required for certificated evidence. | Two-branch activity-selection decision diagram; full width. | Split learning practice from formal assessment. Formal assessment needs approved evidence, criteria, safety, independence, and records. | — |

## 3. Style and branding

### My First Bitcoin branding

Use the [Illustration Style Guide](../assets/style/STYLE.md) as the production translation of the My First Bitcoin brand for Bitcoin Diploma visuals. It sets the working visual direction, `MFB Angular Editorial Illustration`, and points to the higher-order MFB Design System and `brand-spec.md` for brand colour, typography, and voice decisions. If a mark is needed, use an official MFB logo or B-tag asset; do not redraw it.

The brand basics for Bitcoin Diploma visuals are a purple-led palette, paper or white surfaces, cool-gray dividers, and a small amount of orange only to identify the most important point. Use IBM Plex Sans for text inside assets. Keep artwork flat, print-safe, calm, practical, human, and independent; it must not resemble a trading promotion, glossy fintech interface, or generic corporate cartoon.

### Visual style

The reference material is kept in [`assets/style/`](../assets/style/):

**Required for human figures:** If an asset includes people or other human figures, use [`bible/`](../assets/style/bible/), [`layouts/`](../assets/style/layouts/), and [`CHARACTERS.md`](../assets/style/CHARACTERS.md) as the reference set before creating or reviewing it. These sources define the approved cast and their visual treatment, as well as the composition context in which they appear.

| Location | What it contains | Use it for |
|---|---|---|
| [STYLE.md](../assets/style/STYLE.md) | The complete illustration, diagram, data-graphic, and table style guide. | The primary rulebook for every Bitcoin Diploma visual: palette, type, 13° geometry, linework, texture, props, chart/table patterns, AI-reference language, and final-production checks. |
| [layouts/](../assets/style/layouts/) | `mfb-assets-full-page`, `mfb-assets-line-up`, and `mfb-assets-one-page` PNG layout studies, with versioned variants. | Composition and spacing references; use the latest reviewed variant of the layout that fits the asset, rather than inventing a new visual treatment. |
| [CHARACTERS.md](../assets/style/CHARACTERS.md) | The six-person recurring cast, learning roles, pose library, use rules, and recommended combinations. | Select and name people consistently in illustration briefs and filenames, for example `C03_reading_v01`. |
| [bible/](../assets/style/bible/) | Versioned `mfb-assets-character-bible` PNG character-reference boards. | Compare faces, proportions, clothing, hands, outline weight, and colour treatment when drawing or reviewing people. |

Start with an existing visual pattern: comparison pair, layer stack, timeline, process flow, bar chart, proportion bar, big stat, trend line, callout, definition, or key takeaways. Each asset should teach one clear point with direct labels, generous negative space, upright text and icons, and only the detail needed for learning.

### Guidelines

- Use a single 13° structural slant for frames, diagonal cuts, rules, or hatching. Keep faces, icons, and text upright.
- Use purple for structure and orange for one focal point, warning, active value, or key takeaway. Do not rely on colour alone; pair data series with hatch or another clear distinction so they work in grayscale.
- Use short, literal, left-aligned labels. Learner-facing type is at least 12pt; final labels must be live, editable, and translatable.
- Build diagrams with straight or right-angle connectors, open chevron arrowheads, and filled dots at stops or junctions. Prefer a proportion bar to a pie chart and avoid dashboard-like density.
- Keep tables on white or paper, with purple headers, cool-gray hairlines, short translation-safe cells, and right-aligned comparable numbers.
- When people appear, use the approved cast and its character IDs. Show only people needed to teach the point; preserve their fixed visual details and treat the older learner as an active, capable participant.
- Make final production assets editable and supply an appropriate export, review PNG/PDF, alt text, and a one-sentence educational purpose. For HTML/CSS micrographics, follow the scoped-selector and translation requirements in [STYLE.md](../assets/style/STYLE.md).
- Before handoff, check that the asset is print-safe, works on a phone and in grayscale, uses no gradients or glossy effects, avoids crypto-hype imagery, and follows the Style Guide pre-flight checklist.

## 4. Placement

Each index row identifies an SG or EG location by guide heading and nearby text. Most assets are additions to the [Student Guide](../publish/mfb-bd-26.10/mfb-bd-sg-26.10.md) or [Educator Guide](../publish/mfb-bd-26.10/mfb-bd-eg-26.10.md) and leave adjacent content unchanged. The assets below replace an existing Student Guide table and retain an accessible text equivalent.

### Assets that replace existing guide elements

| Asset | Type | Guide | Element to replace |
|---|---|---|---|
| `BD-V-005` | Table (Replacement) | SG | The four-row table under `### How the 4-module learning path is organized` |
| `BD-V-007` | Table (Replacement) | SG | The `Property / Question to ask` table under `### Functions and properties of money` |
| `BD-V-014` | Table (Replacement) | SG | The `Participant / Main role` table under `### Fiat money` |
| `BD-V-020` | Table (Replacement) | SG | The comparison table under `### Alternatives for saving and holding value` |
| `BD-V-029` | Table (Replacement) | SG | The unit table under `### Satoshis and unit bias` |
| `BD-V-033` | Table (Replacement) | SG | The property table under `### Bitcoin as sound digital money` |
| `BD-V-025` | Table (Replacement) | SG | The date/event table under `### Bitcoin origin timeline` |
| `BD-V-034` | Table (Replacement) | SG | The `Potential modern money-system flaw / Bitcoin's response / New responsibility or trade-off` table under `### Review: how does Bitcoin respond to modern money-system flaws?` |
| `BD-V-040` | Table (Replacement) | SG | The `Question / Custodial use / Self-custodial use` table under `### Custodial and non-custodial use` |
| `BD-V-041` | Table (Replacement) | SG | The `Arrangement / Common strength / Responsibility to remember` table under `### Hot and cold wallets` |
| `BD-V-049` | Table (Replacement) | SG | The `Risk area / Question to ask` table under `### Acquiring and exchanging bitcoin` |
| `BD-V-051` | Table (Replacement) | SG | The `Question / On-chain Bitcoin / Lightning` table under `### On-chain and Lightning payments` |
| `BD-V-055` | Table (Replacement) | SG | The `Local learning choice / Your notes` table under `## Module 4: Bitcoin in Your Community` |
| `BD-V-057` | Table (Replacement) | SG | The `Area / What to verify` table under `### Local Bitcoin tools and resources` |
| `BD-V-058` | Table (Replacement) | SG | The `Local tool record` table under `### Local Bitcoin tools and resources` |
| `BD-V-063` | Table (Replacement) | SG | The pathway-comparison table under `### Local on-ramp and off-ramp pathways` |
| `BD-V-064` | Table (Replacement) | SG | The `Question / KYC path / No-KYC path` table under `### KYC and no-KYC trade-offs where locally appropriate` |
| `BD-V-068` | Table (Replacement) | SG | The `Record your local resources` table under `### Local resource maps and community discovery` |

A source marker is a non-rendered HTML comment in a guide source file. It records the asset ID, production note, alt text, and reserved visual location. For example:

```markdown
<!-- VISUAL: BD-V-001
SANITY: Required — add the approved official Creative Commons Attribution-ShareAlike 4.0 licence mark here during Sanity production.
ALT: Official Creative Commons Attribution-ShareAlike 4.0 licence mark beside the written licence statement.
-->
```

The final Markdown or production asset reference replaces the complete marker after approval. The index row's heading, nearby text, and insertion direction remain the placement authority; line numbers are finders only.





## 5. AI Production Workflow & Handoff

For each approved asset, create:

```yaml
id: BD-V-000
brief: assets/briefs/bd-v-000-brief.md
reference_svg: assets/reference/bd-v-000-ref.svg
reference_png: assets/reference/bd-v-000-ref.png
record: assets/reference/bd-v-000-ref.json
placement: exact guide heading and text anchor
alt_text: short text equivalent
status: draft | review | approved | published
```

Use the asset row as the brief. Write a separate brief only when the row is not enough.

### Make and review

1. Read the asset row and adjacent guide text.
2. Create a reference image only for layout or illustration direction.
3. Build diagrams, tables, text, and QR codes as editable vector or code.
4. Review the asset before insertion.
5. Replace the marker or add the Markdown image after approval.

Check these points:

- It teaches the stated idea.
- It matches the guide text and anchor.
- Labels are short, editable, and translatable.
- It is safe and factually accurate.
- It has alt text.
- It works in grayscale, print, and on a phone.
- QR codes and links work when used.

### Reuse rules

- Reuse one interface style for receiving, sending, and explorer visuals.
- Reuse custody labels. Do not treat custody and hot/cold storage as the same thing.
- Reuse on-chain and Lightning labels. Do not treat Lightning as a separate coin.
- Make local maps, tools, and scenarios editable.
- Keep separate concepts separate: keys versus wallets, supply versus price, payment layers versus custody, and QR panels versus diagrams.

## 6. Asset workflow

1. Gather visual-asset definitions, styling, guidelines, and scope in `workspace/08_assets.md`.
2. Record each asset’s key information, index, description, and progress in `assets/assets-list.md`.
3. Create one design brief per asset, including a precise generation prompt: `assets/briefs/bd-v-###-brief.md`.
4. Generate an asset JSON file using `assets/prompts/prompt-01-json.md` and the relevant design brief.
5. Repeat until every asset in `assets/assets-list.md` has a JSON file in `assets/reference/bd-v-###-ref.json`.
6. Use the asset brief, JSON reference file, and `assets/prompts/prompt-02-svg-png.md` to have Codex generate the SVG reference and matching PNG rendering: `assets/reference/bd-v-###-ref.svg` and `assets/reference/bd-v-###-ref.png`.
7. Upload the SVG (`assets/reference/bd-v-###-ref.svg`), PNG (`assets/reference/bd-v-###-ref.png`), JSON (`assets/reference/bd-v-###-ref.json`), and asset brief (`assets/briefs/bd-v-###-brief.md`) to the My First Bitcoin Virtual Machine.
8. Use `assets/prompts/prompt-03-mg.md` with Claude Design or Claude Code to produce an HTML/CSS ZIP package.
9. Manually upload the ZIP package to Sanity.
