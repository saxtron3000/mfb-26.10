# Bitcoin Diploma Visual–Text Index

## Purpose

This document is the index between the written Bitcoin Diploma and the visual explanations that belong inside it.

It identifies:

- which concepts in `../publish/mfb-bd-26.10/mfb-bd-sg-26.10.md` need a diagram, illustration, timeline, annotated interface, or other explanatory graphic;
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

Activity visuals belong on the [Resources Hub](https://programs.myfirstbitcoin.org/resources/). Educator-only visuals belong in `../publish/mfb-bd-26.10/mfb-bd-eg-26.10.md`. Presentation visuals belong with the relevant presentation source. Ordinary tables and forms remain part of the Diploma manuscript unless they require a separate explanatory graphic listed here.

---

# 1. Source And Placement Rules

The current source of truth is `../publish/mfb-bd-26.10/mfb-bd-sg-26.10.md`.

Printed-note page references come from `../feedback/202602721_final_draft_notes.md`, which transcribes the 53 annotated pages in `../feedback/20260715_PABLO_draft_notes.pdf`. The `Page` and `Note` columns refer to those printed PDF page numbers and annotations, not to future Diploma pagination.

Use exact Markdown section headings as the primary anchors. Do not use current page numbers as the main placement method because pagination will change during design and translation.

Line references are a snapshot of the current `../publish/mfb-bd-26.10/mfb-bd-sg-26.10.md`; recalculate them whenever an edit shifts the manuscript.

Each visual entry provides:

| Field | Meaning |
|---|---|
| ID | Stable identifier used in filenames, alt text, source comments, and review notes. |
| Suggested by | `Pablo` when the asset is directly grounded in a handwritten note; `AI` when the visual asset or its form was inferred through prompting. |
| Priority | `Essential`, `Supporting`, or `Conditional`. |
| Type | `Table` for a structured comparison or template; `Diagram` for a relationship, process, map, or timeline; `Image` for an illustrative scene, source image, or interface mockup. |
| Page | Matching printed page number or numbers; `—` means no matching page-specific note was found. |
| Note | Short description of the matching Pablo note; `—` means no matching page-specific note was found. |
| Placement | Exact heading in `../publish/mfb-bd-26.10/mfb-bd-sg-26.10.md` and the position within that section. |
| Line | Current `../publish/mfb-bd-26.10/mfb-bd-sg-26.10.md` line: insert immediately after it, or immediately before it when `Placement` says before or replace. |
| Text–visual link | The idea in the prose that the visual must make clear for the learner. |
| Design brief | What the visual must show and what it must not imply. |
| Format | Recommended visual form and approximate layout role. |

When inserting a completed visual into the manuscript:

1. Find the exact heading named in the entry.
2. Find the described paragraph, list, or table within that section.
3. Insert the visual immediately after or before that element as directed.
4. Keep the original explanatory prose unless the entry explicitly says the visual replaces an existing table.
5. Add a Markdown image reference and useful alt text; do not use the filename as alt text.
6. If the anchor text changes, update this index in the same revision.

Recommended source marker:

```markdown
<!-- VISUAL: BD-V-001
ALT: Alt text that communicates the instructional meaning.
ASSET: assets/diploma/bd-v-001.svg
-->
```

Replace the marker with a Markdown image reference only after the asset exists. Recommended filenames are `bd-v-001.svg`, `bd-v-002.svg`, and so on. Keep an editable SVG master. Export print and screen versions only during production.

---

# 2. Shared Design Requirements

These requirements apply to every entry in the index.

## Instructional Function

- The visual must explain an idea from the adjacent text. It must not be decorative filler.
- One visual should communicate one primary idea. Related sub-points may support it, but should not compete with it.
- Captions should state what the learner should notice, not merely repeat the title.
- Visuals must preserve nuance and trade-offs. Do not turn qualified text into absolute promotional claims.

## Beginner Clarity

- Prefer familiar actors, arrows, sequences, comparisons, and concrete quantities.
- Define or avoid symbols that require technical knowledge.
- Keep protocol, wallet, service, and user roles visually distinct.
- Do not imply that bitcoin is physically stored inside a wallet, that a miner approves Bitcoin's rules, or that a central actor controls the network.

## Safety

- Never display a real seed phrase, private key, payable address, invoice, balance, identity, or transaction associated with a learner.
- Interface examples and QR codes must be clearly marked `SAMPLE — DO NOT PAY` where relevant.
- Do not visually imply guaranteed returns, inevitable adoption, risk-free self-custody, or a universal legal or financial conclusion.
- Locally variable tools, laws, prices, fees, and services must be presented as dated examples, not global facts or endorsements.

## Accessibility, Translation, And Production

- Design for grayscale printing as well as color. Never use color as the only carrier of meaning.
- Use high contrast, readable type, clear reading order, and patterns or labels that remain visible to color-blind readers.
- Keep text inside graphics short and editable. Avoid idioms, wordplay, flags, and culturally narrow metaphors.
- Prefer vector shapes and live text. Avoid rasterized labels.
- Provide alt text and a text-equivalent explanation for complex diagrams.
- Keep essential detail legible on an A4 or US Letter page and on a phone-width PDF.
- Use the approved My First Bitcoin visual system when it becomes available; do not invent permanent brand colors in this index.

---

# 3. Visual Index

## Pablo-Suggested Assets By Printed Page

- Page 1 — `BD-V-001`: Creative Commons Attribution-ShareAlike 4.0 licence mark.
- Page 2 — `BD-V-002`: Critical-thinking checkpoints.
- Page 8 — `BD-V-008`: Functions and properties of money diagram with three function icons.
- Pages 8–9 — `BD-V-009`: Barter and double-coincidence diagram.
- Page 10 — `BD-V-010`: Water-in-context value and price comparison.
- Page 10 — `BD-V-011`: Opportunity cost, time preference, and trade-off illustration.
- Pages 10–11 — `BD-V-012`: Non-linear history of money timeline.
- Page 12 — `BD-V-014`: Fiat-system participant map.
- Page 12 — `BD-V-015`: Bank lending and deposit-money diagram.
- Page 12 — `BD-V-016`: Liquidity-versus-solvency comparison.
- Page 13 — `BD-V-017`: Inflation and purchasing-power graphic.
- Page 18 — `BD-V-024`: Bitcoin origin timeline and source images.
- Page 19 — `BD-V-027`: Bitcoin issuance, supply, and halving chart.
- Page 20 — `BD-V-028`: Bitcoin and satoshi denomination graphic.
- Page 22 — `BD-V-031`: Proof-of-work process diagram.
- Page 23 — `BD-V-032`: Icon-supported Bitcoin-properties table.
- Page 24 — `BD-V-033`: Fiat problems, Bitcoin responses, and trade-offs comparison.
- Page 26 — `BD-V-035`: Bitcoin address and sample QR graphic.
- Page 27 — `BD-V-036`: Private key, public information, and signature diagram.
- Pages 28–30 — `BD-V-042`: Safe wallet recovery workflow.
- Page 29 — `BD-V-041`: Hot, cold, hardware, and custodial wallet comparison.
- Pages 32–33 — `BD-V-045`: Confirmations timeline and block-explorer example.
- Pages 33–34 — `BD-V-046`: Potential-scam red-flag image.
- Pages 33 and 36–37 — `BD-V-049`: On-chain and Lightning comparison.
- Page 35 — `BD-V-047`: Bitcoin acquisition and exchange pathway map.
- Page 35 — `BD-V-048`: Risk-area and questions-to-ask table.
- Page 38 — `BD-V-051`: Self-custody responsibility map.
- Page 40 — `BD-V-055`: Presentation → Practice → Production workshop flow.
- Pages 40 and 48 — `BD-V-065`: Merchant payment operations flow.
- Pages 41–42 — `BD-V-056`: Local Bitcoin tool comparison template.
- Page 43 — `BD-V-059`: Seven daily-life Bitcoin-use icons.
- Page 51 — `BD-V-071`: Final safety reminder.
- Page 52 — `BD-V-072`: Source and contribution QR panel.
- Page 52 — `BD-V-073`: Two-route support panel: on-chain and Lightning QR codes.

## 3.1 Welcome And Learning Setup

| ID | Suggested by | Priority | Type | Page | Note | Placement | Line | Text–visual link | Design brief | Format |
|---|---|---|---|---|---|---|---|---|---|---|
| `BD-V-001` | Pablo | Supporting | Image | 1 | add the Creative Commons Attribution-ShareAlike 4.0 licence logo. | At the Creative Commons Attribution-ShareAlike 4.0 licence statement near the front of `../publish/mfb-bd-26.10/mfb-bd-sg-26.10.md`, immediately after the licence paragraph and before the horizontal rule. | 11 | Gives the open licence a recognisable visual marker while leaving the written licence terms primary. | Use the official Creative Commons BY-SA 4.0 mark or an approved official variant, at small but legible size. Keep the written licence statement, attribution requirement, and adaptation condition beside or immediately above it. Do not redraw, recolour, distort, or use the logo as a replacement for the licence text or link. | Official licence mark with short text lockup; small inline or corner placement. |
| `BD-V-002` | Pablo | Supporting | Diagram | 2 | teach a critical-thinking process with scans, tips, or checkpoints. | Under `### What we stand for: accessibility, critical thinking, community, and self-sovereignty`, after the paragraph on examining claims and trade-offs. | 37 | Makes “teach how to think, not what to think” into a repeatable learner action. | Show a six-step loop: identify the claim; separate fact from preference; inspect evidence and source; compare alternatives; name a trade-off or uncertainty; form a provisional conclusion or question. The loop must allow revision rather than ending in certainty. | Horizontal process strip or circular loop; half page. |
| `BD-V-003` | AI | Essential | Diagram | 6 | clarify the four-module Diploma, educator-curated Modules 3–4, and Advanced boundaries. | Under `### The four-module Diploma, educator-curated Module 4, and Advanced learning`, after the three definitions and before the closing paragraph. | 215 | Clarifies that all four modules are the Diploma, while educators adapt Module 3 practice and curate the required Connect Module 4. | Show all four modules inside a `Diploma: all learners` container, labeled Problem → Solution → Action → Connect. Mark Modules 1–2 as shared core learning, Module 3 as educator-adapted practical learning, and Module 4 as `Connect: educator-curated local learning; required`. Show that Connect applies the earlier learning to a local need and realistic alternative. Show Advanced as a separate onward path. Use arrows to show progression, not a hierarchy of importance. | Layered pathway diagram; full width. |
| `BD-V-004` | AI | Essential | Diagram | 6–7 | clarify the Problem → Solution → Action → Connect module structure and show timing as adaptable. | Under `### How the 4-module learning path is organized`, immediately before the existing four-row table. | 191 | Gives learners a mental map of the Diploma before they enter Module 1. | Show one connected sequence: `1 Problem: Understanding Money → 2 Solution: How Bitcoin Works → 3 Action: Using Bitcoin Safely → 4 Connect: Bitcoin in Your Community`. Mark Modules 1–3 as shared learning and Module 4 as educator-curated, locally relevant, and required. Show that Connect links the first three stages to a local need, realistic alternative, safe task, and next step. Include each module's guiding question in short editable text. The final module must not be reduced to spending. | Four-stage roadmap; full width. |
| `BD-V-005` | AI | Supporting | Table | 6–7 | turn the Problem → Solution → Action → Connect learning-path table into a clear visual reference. | Under `### How the 4-module learning path is organized`, replace the existing four-row table visually while retaining an accessible text equivalent. | 191 | Lets learners compare each Diploma module's role, guiding question, and promise at a glance. | Preserve the columns `Module`, `Role`, `Guiding question`, and `Learner promise`. Use four clearly separated, editable rows for Problem: Understanding Money, Solution: How Bitcoin Works, Action: Using Bitcoin Safely, and Connect: Bitcoin in Your Community. Mark Modules 1–3 as shared learning and Module 4 as educator-curated, locally relevant, and required for Diploma completion. | Four-module reference table; full width. |
| `BD-V-006` | AI | Supporting | Diagram | 4 | apply the five-step learning rhythm consistently. | Under `### Flexible learning: in person, online, or through low-tech delivery`, after the description of the learning style. | 112 | Shows how a learner moves through a typical concept rather than only reading it. | Show the repeating rhythm `short explanation → guided discussion → safe practice → reflection → explain in your own words`. Show that teaching and assessment may follow an offline or low-tech path. Depict the two educator-evaluated assessment components: theoretical competency shown through explanation, comparison, or application (50%) and observed practical competence (50%). | Five-step rhythm strip; half to full width. |
| `BD-V-007` | AI | Supporting | Table | 8 | make the money-properties table easy to scan and compare. | Under `### Functions and properties of money`, replace the existing `Property / Question to ask` table visually while retaining an accessible text equivalent. | 244 | Gives learners a reusable set of questions for assessing whether a form of money is useful. | Preserve durability, portability, divisibility, fungibility, scarcity, acceptability, and verifiability, each paired with its existing question. Add restrained, distinct icons only as supporting cues. Do not score currencies or name a universal winner. | Icon-supported property-question table; full width. |

## 3.2 Module 1: Understanding Money

| ID | Suggested by | Priority | Type | Page | Note | Placement | Line | Text–visual link | Design brief | Format |
|---|---|---|---|---|---|---|---|---|---|---|
| `BD-V-008` | Pablo | Essential | Diagram | 8 | illustrate the functions and properties of money. | Under `### Functions and properties of money`, after the properties table and before “No form of money scores perfectly.” | 253 | Separates what money does from the qualities that make it useful. | Use two linked layers. Layer 1 shows the three functions with small, simple icons: exchange arrows for medium of exchange; a price tag or measuring symbol for unit of account; and a clock with protected value for store of value. Layer 2 shows the seven properties: durability, portability, divisibility, fungibility, scarcity, acceptability, verifiability. Use cash, gold, and a generic digital monetary asset only as examples; do not assign a universal winner or a simplistic total score. | Icon-led two-layer diagram; full width. |
| `BD-V-009` | Pablo | Essential | Image | 8–9 | add exchange-difficulty examples and a local three-role barter graphic. | Under `### Barter and the double coincidence of wants`, after the Amina, Luis, and Mei scenario and before the formal definition. | 262 | Makes the failed exchange relationships in the prose visible. | Show Amina with rice wanting shoes, Luis with shoes wanting cooking oil, and Mei with cooking oil wanting repair work. Use broken or unmatched arrows to show why no direct pair satisfies both wants. Add a second small panel showing how commonly accepted money separates selling from buying. Keep names and objects editable for localization. | Two-panel illustrated flow; full width. |
| `BD-V-010` | Pablo | Essential | Image | 10 | compare clean water in two contexts to show context-dependent value and price. | Under `### Scarcity, value, and exchange`, immediately after the sentence “Clean water may be inexpensive near a safe public source and extremely valuable during a shortage.” | 280 | Makes the same good's changing value and price clear through a concrete example. | Use two parallel images of the same quantity of clean water. Panel 1: near a safe public source, readily available, with an illustrative lower-price label. Panel 2: during a shortage, limited access and urgent need, with an illustrative higher-price label. State clearly that availability, need, and circumstances change value and price; do not imply that water scarcity or high prices are ethically acceptable. Keep people, setting, language, and price units editable for localization. | Two-panel contextual-value illustration; half to full width. |
| `BD-V-011` | Pablo | Supporting | Image | 10 | expand opportunity cost, time preference, and trade-offs with examples and graphics. | Under `### Scarcity, value, and exchange`, after the definitions of opportunity cost, time preference, and trade-off. | 288 | Connects three abstract choice concepts to one everyday decision. | Show one person choosing between two uses of limited money or time. Label the chosen benefit, the best alternative forgone, the present-versus-future preference, and the resulting trade-off. Do not moralize the learner's choice or imply one time preference is always correct. | Branching choice illustration; half page. |
| `BD-V-012` | Pablo | Essential | Diagram | 10–11 | add a non-linear money timeline and historical context through modern fiat. | Under `### Beginner monetary history from barter to digital money`, after the `Digital money` paragraph. | 350 | Prevents the history from appearing as one universal, inevitable sequence. | Create several overlapping tracks rather than one straight progress arrow: direct exchange and local records; commodity forms; standard coins; representative paper; bank and government money; modern fiat; digital fiat. Mark that different forms coexist and developed differently across places. Include 1971 only as a dated milestone in the modern-fiat track, not as the origin of all fiat money. | Braided or layered timeline; full-page width. |
| `BD-V-013` | AI | Supporting | Table | 12 | make the fiat-system participant table clear and easy to compare. | Under `### Fiat money`, replace the existing `Participant / Main role` table visually while retaining an accessible text equivalent. | 320 | Clarifies the different roles of central banks, commercial banks, governments, and citizens or businesses. | Preserve the four participant rows and their main roles. Use neutral role icons and editable text. Do not imply that every country has the same institutions, powers, or rules. | Participant-and-role reference table; full width. |
| `BD-V-014` | Pablo | Supporting | Diagram | 12 | turn the fiat-participant table into a guided explanation and clarify liabilities. | Under `### Fiat money`, after the participant table. | 325 | Shows where trust, claims, and control sit in a fiat payment system. | Map central bank, commercial bank, government, citizens and businesses, and payment services. Use distinct arrows for money or claims, policy or rules, taxes and spending, and payment instructions. Show that a bank deposit is the bank's liability to the customer. Avoid suggesting that every country has identical institutions or rules. | Actor-and-flow system map; full width. |
| `BD-V-015` | Pablo | Essential | Diagram | 12 | explain deposit-money creation, define liability, and diagram fractional-reserve banking. | Under `### Fractional reserve banking`, after the paragraph beginning “When a commercial bank approves a loan” and before the definition of fractional reserve banking. | 335 | Makes deposit creation and the bank balance sheet clear without relying on a misleading money-multiplier story. | Trace a simplified loan: bank approves loan; bank records a loan asset and a matching deposit liability; borrower can transfer the deposit; settlement and liquidity requirements remain. Label assets and liabilities on both sides. State `simplified example; exact rules vary`. Do not show banks lending out the same physical deposit repeatedly. | Numbered balance-sheet flow; full width. |
| `BD-V-016` | Pablo | Essential | Table | 12 | add liquidity-versus-solvency examples. | Under `### Fractional reserve banking`, after the liquidity-risk and solvency-risk definitions. | 342 | Prevents learners from treating liquidity and solvency as the same problem. | Show two parallel simplified bank snapshots. In the liquidity case, assets exceed liabilities but too little is immediately available. In the solvency case, asset value is below liabilities. Use small round example numbers and label them as fictional. | Side-by-side balance-sheet comparison; half to full width. |
| `BD-V-017` | Pablo | Essential | Image | 13 | turn inflation and purchasing-power definitions into graphics and local examples. | Under `### Inflation and purchasing power`, after the basket example in the second paragraph. | 352 | Shows the inverse relationship between a rising basket price and what a fixed amount of money can buy. | Use the same fixed amount of currency at two dates. At Date A it buys the full basket; at Date B the basket costs more and the fixed amount buys less. Distinguish `price level` from `purchasing power`. Use fictional or sourced-and-dated local values; never mix the two. | Before-and-after quantity illustration; full width. |
| `BD-V-018` | AI | Supporting | Table | 14 | add current CBDC examples and explain risks, benefits, privacy, and control. | Under `### Central Bank Digital Currencies (CBDCs)`, after the paragraph beginning “A CBDC does not create a fixed monetary supply.” | 448 | Clarifies that digital, centralized, decentralized, private, and scarce are different attributes. | Compare physical cash, commercial-bank digital deposits, a generic retail CBDC, and Bitcoin across issuer or controller, form, access permission, visibility, supply-rule control, and independent verifiability. Mark CBDC features as design-dependent. Do not imply that all CBDCs have identical surveillance or control features. | Layered comparison matrix with icons; full width. |
| `BD-V-019` | AI | Supporting | Table | 14–15 | make the alternatives comparison table easy to evaluate without ranking assets. | Under `### Why people look for alternatives`, replace the existing comparison table visually while retaining an accessible text equivalent. | 389 | Helps learners compare why an asset may be chosen alongside its important trade-offs. | Preserve precious metals, real estate, and stocks with columns for `Why people may choose it` and `Important trade-offs`. Add simple, non-promotional icons. Do not add investment advice, price predictions, or a best-choice ranking. | Alternatives trade-off table; full width. |
| `BD-V-020` | AI | Supporting | Diagram | 14–15 | add local real-estate context and clarify assets versus money. | Under `### Why people look for alternatives`, after the existing comparison table. | 393 | Reinforces that each alternative serves some purposes while introducing different constraints. | Place cash, precious metals, real estate, stocks, and Bitcoin around the needs `daily payment`, `long-term saving`, `portability`, `income or productive use`, and `direct control`. Use qualitative callouts, not a ranked score or investment recommendation. | Trade-off landscape; full width. |

## 3.3 Module 2: How Bitcoin Works

| ID | Suggested by | Priority | Type | Page | Note | Placement | Line | Text–visual link | Design brief | Format |
|---|---|---|---|---|---|---|---|---|---|---|
| `BD-V-021` | AI | Essential | Diagram | 16 | make intermediary power and risk concrete and define digital signatures. | Under `### Why Bitcoin was created`, after the paragraph beginning “Bitcoin was created to solve this problem.” | 433 | Contrasts a central ledger keeper with Bitcoin's distributed verification model. | Left panel: sender and receiver depend on one intermediary that keeps and approves the ledger. Right panel: signed transactions propagate to independent nodes; miners propose blocks; nodes verify the same public rules. Emphasize reduced dependence on a central settlement authority, not removal of all trust. | Two-system comparison diagram; full width. |
| `BD-V-022` | AI | Supporting | Diagram | 17 | attribute the earlier contributors and ideas on which Bitcoin was built. | Under `### The search for digital and decentralized money`, after “Bitcoin grew from decades of work by many people.” | 447 | Shows that Bitcoin combined prior ideas rather than appearing without context. | Create an idea lineage with DigiCash, Hashcash, Bit Gold, B-money, reusable proof of work, and peer-to-peer file sharing feeding distinct contributions toward Bitcoin. Label contributions carefully; do not imply that every project directly supplied code or that Bitcoin has one intellectual predecessor. | Converging idea timeline; full width. |
| `BD-V-023` | AI | Essential | Diagram | 17 | format, visually clarify, and fact-check the four-step transaction/miner/node process. | Under `### Early digital-money attempts and the double-spend problem`, after the four-step numbered explanation. | 472 | Explains how a conflicting second spend is resolved without a central database. | Begin with one spendable output and two conflicting payment attempts. Show transactions announced, miners proposing order in candidate blocks, nodes rejecting invalid or conflicting history, and the valid chain with the most accumulated work becoming accepted. Use the text's four-step vocabulary. Do not imply that one miner decides validity. | Four-step conflict-resolution flow; full width. |
| `BD-V-024` | Pablo | Essential | Table | 18 | add images or links for the whitepaper, Genesis Block, first transaction, and Pizza Day. | Under `### Bitcoin origin timeline`, replace the current date/event table visually while retaining an accessible text equivalent. | 480 | Connects the four historical events to why each matters. | Show 31 Oct 2008 whitepaper; 3 Jan 2009 Genesis Block; 12 Jan 2009 first recorded person-to-person transaction; 22 May 2010 Pizza Day. Pair each event with a short significance line. Use document-style illustrations or rights-cleared source images only; avoid portraits or identity speculation for Satoshi. | Illustrated four-milestone reference table; full width. |
| `BD-V-025` | AI | Essential | Diagram | 19 | clarify decentralization roles, unilateral limits, economic nodes, and trade-offs. | Under `### Decentralization`, after the list of decentralizing features and before the paragraph beginning “Decentralization is not the same as equal influence.” | 507 | Makes the distribution and limits of participant power visible. | Place users, nodes, miners, developers, and services around the shared protocol and public ledger. For each, show `can do` and `cannot do unilaterally`. Services must sit outside the protocol boundary. Show unequal influence and points of dependence without adding a central controller. | Roles-and-rules network map; full width. |
| `BD-V-026` | AI | Supporting | Diagram | 19 | distinguish supply claims, subsidy, and node-enforced issuance facts. | Under `### Digital scarcity and credible scarcity`, after the second paragraph. | 517 | Distinguishes a written supply claim from a supply rule independently enforced in practice. | Compare `claim on a website or issuer database` with `public rule checked by many independent nodes`. Show that signatures, transaction history, proof of work, and node verification jointly prevent invalid creation or double spending. Avoid saying that scarcity alone creates value. | Credibility comparison diagram; half to full width. |
| `BD-V-027` | Pablo | Essential | Diagram | 19 | add a finite-supply and halving graphic with block-based timing. | Under `### Finite supply`, after the paragraph describing halvings. | 525 | Separates maximum supply, issuance, block subsidy, halving, and miner fees. | Show a descending step chart for block subsidy by halving era and a rising cumulative issuance curve approaching 21 million. Mark halvings by block height or era and `roughly four years`, not guaranteed calendar dates. Show transaction fees separately from new issuance. Include no price curve or adoption prediction. | Paired issuance chart; full width. |
| `BD-V-028` | Pablo | Essential | Table | 20 | turn the bitcoin-and-sats table into a graphic. | Under `### Satoshis and unit bias`, replace the unit table visually while retaining a text equivalent. | 541 | Makes divisibility intuitive and counters the belief that a learner needs one whole bitcoin. | Start with `1 BTC = 100,000,000 sats`, then zoom into 0.1 BTC, 0.01 BTC, 0.001 BTC, and 1 sat. Show that differently displayed amounts can represent the same value, using `100,000 sats = 0.001 BTC`. Do not show a current fiat price. | Illustrated denomination reference table; half to full width. |
| `BD-V-029` | AI | Supporting | Diagram | 21 | distinguish the Bitcoin network from services and intermediaries. | Under `### Peer-to-peer transfer`, after the paragraph explaining that peer-to-peer does not always mean only two computers communicate. | 561 | Separates direct settlement rules from the communications and service infrastructure a transaction may pass through. | Show sender wallet → network peers → recipient wallet, with optional exchange, hosted wallet, payment service, and internet provider around the path. Use different line styles for transaction propagation, custody, and communications. The presence of network infrastructure must not be mistaken for central approval. | Layered transfer-path diagram; full width. |
| `BD-V-030` | AI | Essential | Diagram | 21 | clarify users, wallet clients, full nodes, and developer proposals. | Under `### Users, nodes, and miners`, after the paragraph on developers and before “These roles limit one another.” | 579 | Gives beginners a durable model of who does what in Bitcoin. | Show users signing or accepting transactions; nodes validating and relaying; miners assembling candidate blocks and performing proof of work; developers proposing software; services serving customers. Then show the checks among roles. Do not label all wallet users as nodes or developers as rule-makers. | Participant role map; full width. |
| `BD-V-031` | Pablo | Essential | Diagram | 22 | demonstrate proof of work and difficulty, and diagram proof of work's purposes. | Under `### Proof of work`, after the paragraph beginning “When a miner finds a valid result.” | 596 | Makes costly-to-produce and easy-to-verify work visible. | Show candidate block data entering repeated hash attempts; many results miss the target; one result meets it; the miner broadcasts the block; nodes quickly verify proof and all other rules; accepted blocks add accumulated work. Include difficulty adjustment as a small feedback loop. Do not depict mining as solving an externally useful puzzle. | Sequential process diagram; full width. |
| `BD-V-032` | Pablo | Essential | Table | 23 | add graphics to explain Bitcoin's properties in plain language. | Under `### Bitcoin as sound digital money`, replace the existing property table visually while retaining an accessible text equivalent. | 615 | Makes each monetary property concrete without treating Bitcoin as universally superior. | Retain a learner-friendly table with one small icon and concise plain-language explanation for each property: durability, portability, divisibility, fungibility, scarcity, verifiability, and acceptability. State the relevant qualification already in the text, especially that acceptance varies and public history can affect how services treat particular funds. Do not turn the properties into a total score or claim that Bitcoin performs every function equally well everywhere. | Icon-supported properties table; full width. |
| `BD-V-033` | Pablo | Essential | Table | 24 | add graphics to the Module 2 comparison and make the Module 3 transition explicit. | Under `### Review: how does Bitcoin respond to fiat problems?`, immediately before the existing problem/response table. | 657 | Reconnects the entire Module 2 explanation to the Module 1 problems and the new responsibilities introduced by Bitcoin. | Use three aligned columns: fiat-system issue; Bitcoin design response; new responsibility or trade-off. Include supply policy, intermediary dependence, central ledger control, access, purchasing power uncertainty, and institutional recovery. Do not label the middle column `perfect solution`. | Bridge diagram or visual table; full width. |

## 3.4 Module 3: Using Bitcoin Safely

| ID | Suggested by | Priority | Type | Page | Note | Placement | Line | Text–visual link | Design brief | Format |
|---|---|---|---|---|---|---|---|---|---|---|
z| `BD-V-034` | AI | Essential | Diagram | 25 | clarify that wallets coordinate keys and instructions while bitcoin remains on the ledger. | Under `### Wallets`, after the paragraph explaining that bitcoin is not stored inside the wallet. | 806 | Corrects the most important beginner wallet misconception. | Show the Bitcoin ledger as the record of spendable outputs; the wallet holding or managing keys and constructing instructions; the user authorizing an action; and the network verifying it. Do not draw coins sitting inside a phone or hardware device. | Conceptual layer diagram; full width. |
| `BD-V-035` | Pablo | Essential | Image | 26 | add an address/QR graphic, explain who creates addresses, and show address checks. | Under `### Addresses`, after the explanation of an address and before the receive walkthrough. | 822 | Shows what an address is, what is safe to share, and what must be checked. | Use a fictional on-chain receive screen with a sample address, matching QR, network label, optional amount, and `SAMPLE — DO NOT PAY`. Annotate who creates the address, what may be shared, and which fields the sender and receiver compare. Do not use live wallet branding unless approved and dated. | Annotated interface mockup; half to full width. |
| `BD-V-036` | Pablo | Essential | Diagram | 27 | add a public/private-key image and optional physical teaching tool. | Under `### Keys`, after the definitions of private and public keys. | 832 | Explains the one-way relationship among private key, public information, signing, and verification. | Show private key kept secret; public key or address information derived for receiving or verification; a signature created without revealing the private key; nodes verifying the signature. Use conceptual symbols, never realistic secret strings. Do not show arrows implying a private key can be derived from an address. | One-way cryptography relationship diagram; full width. |
| `BD-V-037` | AI | Essential | Diagram | 27 and 30 | show recovery language without implying every wallet uses an identical method. | Under `### Seed phrases`, after the explanation of what a seed phrase does. | 840 | Places the seed phrase correctly in the recovery chain without teaching that every wallet uses an identical recovery method. | Show seed or wallet backup → wallet recreates keys → expected addresses and transaction access return. Mark the backup as secret and offline. Add `method and compatibility depend on the wallet`. Do not show actual words, screenshots of recovery entry, or educator access. | Recovery relationship diagram; half to full width. |
| `BD-V-038` | AI | Essential | Diagram | 26 and 29 | compare custody choices and custodial versus self-custodial wallet control. | Under `### Custodial and non-custodial use`, after the custody explanation. | 850 | Makes custody a question of key control rather than interface appearance. | Left: user logs into a service; service controls keys and authorizes withdrawal. Right: user controls keys; wallet signs under the user's authority; network checks the transaction. Show recovery responsibility and failure point in both paths. Avoid portraying self-custody as morally superior or risk free. | Side-by-side custody model; full width. |
| `BD-V-039` | AI | Supporting | Table | 29 | provide a custodial-versus-self-custodial reference. | Under `### Custodial and non-custodial use`, beside or after `BD-V-038`, with an accessible text equivalent. | 850 | Makes key control, recovery, and failure points comparable without moralising either model. | Use rows for key control, recovery, access restriction, and a main failure point. Use neutral icons and no recommendation badge. | Custody comparison table; full width. |
| `BD-V-040` | AI | Supporting | Table | 29 | make hot, cold, hardware, and custody distinctions easy to scan. | Under `### Hot and cold wallets`, after the introductory explanation, with an accessible text equivalent. | 863 | Prevents learners from treating custody and connectivity as one scale. | Use rows for hot wallet, cold or hardware wallet, and custodial service. Distinguish key control from signing environment and show one practical benefit and one responsibility for each. Do not imply that any option is risk free or suitable for everyone. | Wallet-use comparison table; full width. |
| `BD-V-041` | Pablo | Supporting | Diagram | 29 | add a graphic comparing hot, hardware/cold, and custodial wallets or accounts. | Under `### Hot and cold wallets`, after the introductory explanation. | 863 | Connects wallet type to exposure and use rather than treating `hot`, `cold`, and `custodial` as one scale. | Use two axes or layers: key control (`custodial` versus `self-custodial`) and connectivity or signing environment (`hot` versus `cold or hardware`). Place common use patterns and threat examples in the correct areas. Explicitly show that a custodial account is not a type of self-custodial wallet. | Two-axis classification graphic; full width. |
| `BD-V-042` | Pablo | Essential | Diagram | 28–30 | add a visual recovery-readiness activity and keep practice private and low risk. | Under `### Wallet recovery and seed phrase testing`, after the recovery-practice guidance. | 875 | Turns the recovery text into a safe sequence a learner can rehearse. | Show `create empty or tiny-value training wallet → record backup privately → verify using the approved wallet method → reset or use a separate training environment → recover → compare expected receiving information or history → securely clear temporary device`. Put `educator never sees the secret` outside every step. | Safety-gated workflow; full width. |
| `BD-V-043` | AI | Essential | Image | 31 | add a visual receiving activity and receive-screen competency exercise without real funds. | Under `### Receiving bitcoin`, after the receive steps. | 892 | Lets a learner identify the elements of a receive request before live practice. | Show receiver device, sample address or QR, sender verification, broadcast or pending status, and confirmation. Annotate amount, unit, network, address, and status. Use fictional data and mark the whole visual non-payable. | Annotated receiving flow; full width. |
| `BD-V-044` | AI | Essential | Diagram | 32 | make sending, address, and network checks visual and explain how to perform them. | Under `### Sending bitcoin`, after the pre-send steps. | 906 | Makes verification happen before approval and separates recipient checks from fee and timing decisions. | Show a staged confirmation screen: independently verify recipient; scan or enter destination; compare network and address or invoice; confirm amount and unit; review fee and timing; use small test when needed; approve; save TXID. Put an irreversible boundary immediately after approval. | Preflight-to-settlement flow; full width. |
| `BD-V-045` | Pablo | Essential | Diagram | 32–33 | add a TXID/explorer activity and explain first confirmation, block depth, and privacy. | Under `### Verification, block explorers, and irreversible transactions`, after the confirmation explanation. | 923 | Connects transaction status, block inclusion, and later confirmations. | Show a transaction first in the pending pool, then included in Block N as confirmation 1, followed by Blocks N+1, N+2, and N+3 increasing depth. Pair it with a small annotated fictional explorer panel showing TXID, amount, fee, status, and confirmations. Add a privacy callout about searching personal data. | Confirmation timeline plus explorer inset; full width. |
| `BD-V-046` | Pablo | Supporting | Image | 33–34 | add a red-flag image for a potential scam. | Under `### Safety checklist`, before the red-flag examples. | 931 | Gives learners an immediate visual cue to pause when a message or offer shows scam signals. | Show a prominent red flag beside a generic, nonfunctional message or offer. Add concise warning cues for impersonation, urgency, guaranteed returns, giveaway or recovery requests, fake applications, phishing, relationship manipulation, and too-good-to-be-true claims. Include the action `stop, verify independently, and never share a seed phrase or private key`. Do not use a real brand, address, payment request, or a realistic phishing link. | Red-flag scam-warning illustration; half width. |
| `BD-V-047` | Pablo | Supporting | Diagram | 35 | turn acquisition/exchange pathways into a one-page comparison activity. | Under `### Acquiring and exchanging bitcoin`, after `#### Pathway awareness, not financial advice` and the pathway overview, and before the comparison questions. | 947 | Shows that acquiring bitcoin is an end-to-end route with risks before and after the moment of exchange. | Map earning, peer-to-peer, exchange or broker, ATM or kiosk, and merchant or community receipt as separate paths into either self-custody or custodial balance. Label price or spread, fees, identity, reversibility, counterparty, withdrawal, and local-law checkpoints. Do not rank or recommend a provider. | Branching pathway map; full width. |
| `BD-V-048` | Pablo | Essential | Table | 35 | make the acquisition-pathway questions practical and easy to scan. | Under `### Acquiring and exchanging bitcoin`, after the comparison questions, with an accessible text equivalent. | 958 | Helps learners assess a complete acquisition or exchange route instead of focusing only on price. | Use two columns, `Risk area` and `Question to ask`, for fees, custody, identity, withdrawal, counterparty, safety, and law or tax. Keep each question editable, neutral, and locally verifiable. Include no provider names, rankings, or legal conclusions. | Icon-supported risk-check table; full width. |
| `BD-V-049` | Pablo | Essential | Diagram | 33 and 36–37 | distinguish destinations, add examples and trade-offs, and route deeper mechanics to Advanced. | Under `### On-chain and Lightning payments`, after the introductory comparison. | 964 | Makes the layer relationship and appropriate-use distinction visible. | Show Bitcoin base-layer settlement beneath Lightning payment channels. Compare payment request, route, timing, fee conditions, custody variability, and failure modes. Use one small-payment and one final-settlement example. Do not imply that Lightning is a separate coin or that all Lightning wallets are self-custodial. | Layer diagram plus concise comparison; full width. |
| `BD-V-050` | AI | Supporting | Table | 33 and 36–37 | provide an on-chain-versus-Lightning learner reference. | Under `### On-chain and Lightning payments`, beside or after `BD-V-049`, with an accessible text equivalent. | 964 | Lets learners compare payment requests, settlement, timing, fees, typical use, and introductory risks across the two paths. | Compare payment request, settlement status, timing, fee conditions, custody variability, and introductory failure points. Add only simple layer and request icons. Do not imply that Lightning is a separate coin or that either path is universally better. | Payment-path comparison table; full width. |
| `BD-V-051` | Pablo | Supporting | Diagram | 38 | clarify the responsibility map and turn it into an educator-guided exercise. | Under `### Review: what does self-custody responsibility mean?`, before the key takeaways. | 985 | Synthesizes the module as responsibilities surrounding key control. | Put `control of keys` in the center, surrounded by backup, recovery, receiving, sending, tool choice, acquisition path, privacy, and scam checks. For each, show the protected item and the consequence of failure in very short text. | Responsibility map; full width. |
| `BD-V-052` | AI | Supporting | Table | 38 | make the responsibility map usable as a structured learner reference. | Under `### Review: what does self-custody responsibility mean?`, beside or after `BD-V-051`, with an accessible text equivalent. | 985 | Connects each task with what must be protected or checked and the consequence of failure. | Use rows for backup, receiving, sending, custody, tool choice, and acquisition. Keep language practical and non-alarmist. | Responsibility reference table; full width. |

## 3.5 Module 4: Bitcoin in Your Community

| ID | Suggested by | Priority | Type | Page | Note | Placement | Line | Text–visual link | Design brief | Format |
|---|---|---|---|---|---|---|---|---|---|---|
| `BD-V-053` | AI | Essential | Diagram | 38–39 | define MFB versus educator responsibilities in the educator-curated Connect module. | Under `### Educator-curated local modules`, after the explanation of what remains shared and what can change locally. | 1058 | Explains how Module 4 stays coherent while the educator curates it for a community. | Show MFB supplying required Diploma competency standards, templates, and safety boundaries; educator curating Module 4 with local subject-matter expertise; local expert or community validating tools, laws, risks, language, and infrastructure; learner completing one relevant local pathway. Do not show the educator changing required Diploma competency standards. | Responsibility-and-choice diagram; full width. |
| `BD-V-054` | AI | Supporting | Table | 38–39 | provide a clear editable record of the learner's Module 4 focus. | Under `## Module 4: Bitcoin in Your Community`, replace the existing `Local learning choice / Your notes` table visually while retaining an accessible text equivalent. | 1012 | Gives learners one place to record the module, local problem, tool or scenario, benefit, risk, evidence, and safe next step. | Preserve all seven local-learning-choice prompts and a generous editable notes column. Make it printable and reusable by different educators. Do not pre-fill a local tool, provider, or conclusion. | Editable Module 4 record table; full width. |
| `BD-V-055` | Pablo | Supporting | Diagram | 40 | create a clear Presentation → Practice → Production flow for practical workshops and demonstrations. | Under `### Practical workshops and demonstrations`, after the definitions of Presentation, Practice, and Production. | 1107 | Shows how a safe practical skill develops from educator explanation to guided learner practice and then independent performance or explanation. | Create three connected sections in a clear left-to-right or top-to-bottom sequence: `Presentation` — educator shows the full process and explains purpose, terms, and risks; `Practice` — learner follows a guided process using printed screens, a test environment, or a very small amount; `Production` — learner completes a defined task or explains a decision independently. Add simple safety cues for no funds, test funds, or tiny value, plus an offline alternative at every stage. | Three-stage PPP flow diagram; full width. |
| `BD-V-056` | Pablo | Conditional | Table | 41–42 | create a reusable local-tool comparison and place local-tool guidance in the Module 4 Educator Guide. | Under `### Local Bitcoin tools and resources`, replace the existing `Area / What to verify` table visually while retaining an accessible text equivalent. | 1139 | Helps learners see that an interface belongs to a custody, network, and support context. | Preserve purpose, custody, source, code, recovery, privacy, cost, compatibility, support, and law as editable rows with a `What to verify` column. Record the date checked. Do not show an approved-products badge or a globally recommended wallet. | Local tool evaluation table; full width. |
| `BD-V-057` | AI | Supporting | Table | 41–42 | provide a structured, reusable record for documenting a locally used Bitcoin tool. | Under `### Local Bitcoin tools and resources`, replace the existing `Local tool record` table visually while retaining an accessible text equivalent. | 1156 | Helps learners record what was checked about a tool without treating it as a global recommendation. | Preserve the rows for tool and version, date checked, custody model, main use, benefit, risk, recovery method, and alternative. Keep all fields editable and date-stamped. Do not use an endorsement badge or provider ranking. | Editable local-tool record table; full width. |
| `BD-V-058` | AI | Conditional | Diagram | 36 and 43 | explain Lightning trade-offs and provide a separate Lightning example page. | Under `### Lightning payments where locally appropriate`, after the six guided-payment steps. | 1193 | Makes a Lightning payment sequence clear while keeping custody and failure risk visible. | Show receiver creates request; sender scans or copies; sender verifies recipient, amount, unit, expiry, and fee; sender approves; payment routes; both wallets report success or failure. Add custody labels on both wallets and a branch for failure. Use generic, nonfunctional screens. | Lightning payment sequence; full width. |
| `BD-V-059` | Pablo | Supporting | Diagram | 43 | add seven simple icons for the daily uses of Bitcoin. | Under `### Daily-life Bitcoin use`, after the seven use descriptions and before the three evaluation questions. | 1213 | Makes the seven distinct ways Bitcoin may be used in daily life quick to identify without suggesting that every learner should use it in every way. | Create seven equally weighted illustrative icons, each clearly labelled: earning, saving, receiving, sending, spending, pricing and accounting, and donating. Arrange them in a clear row, grid, or gentle sequence; do not make the icons form a compulsory circular process. Use familiar, culturally adaptable symbols and no provider branding. | Seven-icon daily-use illustration; full width. |
| `BD-V-060` | AI | Conditional | Image | 43–44 | use separate payment examples and preserve the locally grounded scenario approach. | Under `### Local spending and receiving scenarios`, before Scenario 1. | 1227 | Gives all local scenarios one reusable visual grammar so educators can substitute local actors and goods. | Create a four-frame template: need and actors; payment request and chosen path; verification and settlement; record, refund, custody, or conversion. Include editable slots for small purchase, work payment, family transfer, refund, or donation. The template must work with simulation or tiny value. | Reusable scenario storyboard; full width. |
| `BD-V-061` | AI | Essential | Diagram | 45 | preserve but simplify the strongly approved on/off-ramp pathway comparison. | Under `### Local on-ramp and off-ramp pathways`, after the definition and pathway list and before the pathway comparison table. | 1291 | Forces comparison of the complete route rather than only the advertised first fee. | Show local money, work, goods, or services entering through possible routes; custody and identity checkpoints; on-chain or Lightning transfer; self-custody or service balance; and final use, holding, or conversion. Label spread, fees, time, reversal, withdrawal, counterparty, privacy, support, and law along the route. | End-to-end pathway map; full width. |
| `BD-V-062` | AI | Supporting | Table | 45 | provide a local pathway-comparison table that considers the complete route. | Under `### Local on-ramp and off-ramp pathways`, replace the existing pathway comparison table visually while retaining an accessible text equivalent. | 1295 | Helps learners compare received value, time, custody, privacy, reversal risk, and failure points across local options. | Preserve the editable rows for local option A, local option B, and an existing non-Bitcoin option, plus all comparison columns. Do not pre-fill services, rates, or legal claims. | Editable pathway-comparison table; full width. |
| `BD-V-063` | AI | Conditional | Table | 46 | keep KYC/no-KYC trade-offs only where locally appropriate and fact-checked. | Under `### KYC and no-KYC trade-offs where locally appropriate`, immediately before the comparison table. | 1317 | Frames KYC and no-KYC as different bundles of benefits and risks, not as good versus bad. | Compare data collection, account recovery, bank access, legal conditions, fraud protection, counterparty exposure, liquidity, price, support, and on-chain linkability. Include `local law varies; verify current information`. Do not imply evasion or guaranteed privacy. | Balanced trade-off comparison; full width. |
| `BD-V-064` | AI | Essential | Diagram | 46–47 | preserve the conclusion and add a stronger balanced circular-economy graphic. | Under `### Circular economies`, after the seven mapping questions. | 1344 | Shows value circulating among participants and reveals where the loop depends on outside services or support. | Map workers, customers, merchants, suppliers, educators or support, and exchange or on/off-ramp points. Use separate arrows for value, goods or services, and support. Mark custody, volatility, connectivity, and conversion dependencies. Include broken-loop examples such as immediate conversion or one organizer processing everything. | Editable local network map; full width. |
| `BD-V-065` | Pablo | Supporting | Diagram | 40 and 48 | turn merchant payment flow into a local case study and connect it to jurisdiction. | Under `### Merchant or community use cases`, after the merchant decision checklist and before the community-use examples. | 1365 | Shows that accepting Bitcoin is an operational process, not just displaying a QR code. | Trace pricing → payment request → customer verification → merchant confirmation → receipt or record → custody or conversion → refund or exception. Add staff, accounting, tax, device security, offline failure, and support callouts. Use local-law placeholders, not assertions. | Merchant payment operations flow; full width. |
| `BD-V-066` | AI | Conditional | Diagram | 39 and 48 | help learners connect with the local ecosystem through practical field/community work. | Under `### Local resource maps and community discovery`, immediately before `Record your local resources`. | 1397 | Connects community discovery with verification and privacy rather than treating a map listing as proof. | Provide an editable neighborhood or regional map template with merchant, educator, meetup, technical support, exchange information, legal or tax information, and missing-support markers. Every listing includes `date verified` and a safety note. Do not include real personal locations without consent. | Local resource-map template; full width. |
| `BD-V-067` | AI | Supporting | Table | 48 | provide a printable local-resource record with built-in verification and safety prompts. | Under `### Local resource maps and community discovery`, replace the existing `Record your local resources` table visually while retaining an accessible text equivalent. | 1399 | Helps learners document useful local support while recording when information was checked. | Preserve rows for education group, merchant directory, technical support, local exchange information, and legal or tax information, with purpose, verification date, contact or location, and safety note columns. Do not pre-fill personal locations or imply trustworthiness from a listing. | Editable local-resource record table; full width. |
| `BD-V-068` | AI | Supporting | Diagram | 49–50 | frame the review around the learner's community and a specific local need. | Under `### Review: how do the problem, solution, and safe action connect to your community?`, immediately before the final `Need / Fit / Method / Custody / Cost / Safety / Local context / Evidence` table. | 1363 | Turns the final test into a sequence that begins with a need and ends with evidence, rather than beginning with a tool. | Show the decision path `real need → Bitcoin fit → payment method → custody → total cost and trade-offs → safety and local conditions → evidence of success`. Add a return arrow when Bitcoin is not the best available fit. | Decision path; full width. |
| `BD-V-069` | AI | Supporting | Table | 49–50 | make the final local-use test a concise decision and reflection table. | Under `### Review: how do the problem, solution, and safe action connect to your community?`, replace the existing `Test / Your answer` table visually while retaining an accessible text equivalent. | 1363 | Helps learners test a proposed use against need, fit, method, custody, cost, safety, local context, and evidence. | Preserve every test row and a generous answer column. Keep the return-to-need logic visible and leave all answers open for local context. Do not treat Bitcoin as the default solution. | Final local-use test table; full width. |

## 3.6 Back Of Diploma

| ID | Suggested by | Priority | Type | Page | Note | Placement | Line | Text–visual link | Design brief | Format |
|---|---|---|---|---|---|---|---|---|---|---|
| `BD-V-070` | AI | Supporting | Diagram | 50–51 | make next steps quick to scan and separate the available continuation paths. | Under `### A short “What now?” next-steps list`, after the numbered list. | 1453 | Helps learners choose one safe continuation without suggesting that all paths are required. | Branch from the Diploma foundation to repeat a practical skill, improve a safety plan, join a responsible community, continue to Advanced learning, become or support an educator, contribute a translation or correction, and support the project. Keep the branches equal and voluntary. | Next-step pathway map; full width. |
| `BD-V-071` | Pablo | Essential | Diagram | 51 | make the safety reminder scannable and define practical safety tasks precisely. | Under `### A safety reminder`, immediately before the reminder list. | 1461 | Makes the minimum stop-and-check behavior memorable at the point of course completion. | Show `stop → verify source and recipient → verify custody, network, destination, amount, and fee → start small → proceed only when understood`. Put seed or private-key secrecy above the whole sequence as a non-negotiable boundary. | Compact safety strip; half to full width. |
| `BD-V-072` | Pablo | Conditional | Image | 52 | add a public GitHub contribution link or QR and verify official destinations. | Under `### Source or update page, if included`, after the canonical source link. | 1490 | Provides one durable route to updates and contributions without filling the Diploma with fragile QR codes. | Create one panel containing a tested QR code, printed short URL, destination name, edition or last-verified date, and plain-language purpose. The QR must resolve to the canonical maintained source or landing page. Keep donation and certificate verification separate unless the landing page clearly distinguishes them. | QR and fallback-link panel; half page. |
| `BD-V-073` | Pablo | Conditional | Image | 52 | add separate on-chain and Lightning support QR codes with their payment text printed underneath. | Under `### Optional donate / support QR`, immediately after the official Support Us link and before the donation-safety paragraph. | 1510 | Lets a willing supporter choose the correct Bitcoin payment route while retaining a readable fallback when a QR code cannot be scanned. | Create two clearly separated, equally prominent panels: `On-chain Bitcoin` and `Lightning`. Each panel must contain its own verified, live QR code and the exact matching payment text directly underneath: an on-chain address for the on-chain route and a Lightning invoice, offer, or Lightning address for the Lightning route. Include the official destination name, a last-verified date, and `optional support — verify recipient, network, and amount before paying`. Do not use placeholders or publish either QR until My First Bitcoin has supplied and tested the official destinations. | Two-column support QR panel; half to full width. |
| `BD-V-074` | AI | Conditional | Diagram | — | — | Under `### Certificate verification`, after the opening paragraph. | 1516 | Shows a privacy-respecting verification process if the issuing system supports one. | Show certificate holder or verifier → official verification destination → code, signature, or identifier check → result with course, edition, issuer, date, and valid/revoked status. The internal eligibility gate must require two recorded educator-evaluated components: theoretical competency shown through explanation, comparison, or application (50%) and observed practical competence (50%). The components are non-compensatory. The public result should reveal only the minimum necessary learner data and should not expose scores or assessment evidence. Do not invent a verification system or show personal data. Produce only after the real method is confirmed. | Verification flow; half to full width. |

---

# 4. Reuse And Combination Rules

The index contains conceptual requirements, not a command to create the largest possible number of files. Combine visuals only when the combined result remains readable and preserves each placement's learning purpose.

Preferred reuse:

- `BD-V-008` establishes the visual language for later money-property comparisons.
- `BD-V-014`, `BD-V-025`, and `BD-V-030` should share actor symbols while keeping fiat-system and Bitcoin roles distinct.
- `BD-V-035`, `BD-V-043`, `BD-V-044`, and `BD-V-045` should use one generic, nonfunctional interface family.
- `BD-V-038` and `BD-V-041` should share custody labels and definitions.
- `BD-V-047` and `BD-V-061` should share pathway symbols, but Module 3 remains global orientation while Module 4 is locally completed.
- `BD-V-049` and `BD-V-058` should share on-chain and Lightning layer notation.
- `BD-V-053`, `BD-V-060`, `BD-V-064`, and `BD-V-066` should be designed as editable templates for localization.
- `BD-V-071` should retain the safety-gate vocabulary used in the final reminder.

Do not combine visuals merely because they are adjacent. In particular:

- keep `wallet / keys / ledger` separate from `custodial / self-custodial`;
- keep `finite supply` separate from price or investment claims;
- keep `proof of work` separate from the general participant-role map;
- keep `on-chain versus Lightning` separate from wallet custody;
- keep QR destinations separate from conceptual diagrams.

---

# 5. Generation And Review Handoff

For each selected entry, the design handoff should return:

```yaml
id: BD-V-001
suggested_by: Pablo | AI
priority: essential | supporting | conditional
type: Table | Diagram | Image
source_document: ../publish/mfb-bd-26.10/mfb-bd-sg-26.10.md
source_heading: Exact heading from the placement field
insert_position: Exact before/after instruction
source_line: Current line from the Line column
pablo_note_pages: []
pablo_note_summary: Matching note text, or null when no page-specific note exists
text_concept: The prose idea this visual explains
learning_intent: What the learner should be able to explain or do after viewing it
visual_type: Diagram | illustration | timeline | annotated interface | map
required_elements: []
guardrails: []
title: Short learner-facing title
caption: What the learner should notice
asset_master: assets/diploma/bd-v-000.svg
screen_export: assets/diploma/bd-v-000.png
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
3. Can a beginner explain the main relationship after viewing it?
4. Does it preserve the qualifications and trade-offs in the text?
5. Are protocol, service, wallet, and participant roles accurate?
6. Is it safe, nonfunctional where required, and free of private data?
7. Is all factual or current information sourced and dated?
8. Is the reading order accessible and the alt text complete?
9. Does it work in grayscale, print, and a narrow screen?
10. Can labels be translated or locally replaced without redrawing the visual?

`Essential` means the concept is sufficiently relational, procedural, or misconception-prone that a visual should be planned into the Diploma. `Supporting` means the visual is useful if space and testing justify it. `Conditional` means it should be generated only after the local context, technical method, or publication decision is confirmed.

This index should be revised whenever `../publish/mfb-bd-26.10/mfb-bd-sg-26.10.md` changes materially. It should remain a map from text to visual meaning, not become the production tracker for the visual files themselves.
