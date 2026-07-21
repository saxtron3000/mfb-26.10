# Bitcoin Diploma Visual–Text Index

## Purpose

This document is the index between the written Bitcoin Diploma and the visual explanations that belong inside it.

It identifies:

- which concepts in `08_draft.md` need a diagram, illustration, timeline, annotated interface, or other explanatory graphic;
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

Activity visuals belong in `10_activities.md`. Educator-only visuals belong in `11_guide.md`. Presentation visuals belong with the relevant presentation source. Ordinary tables and forms remain part of the Diploma manuscript unless they require a separate explanatory graphic listed here.

---

# 1. Source And Placement Rules

The current source of truth is `08_draft.md`.

Use exact Markdown section headings as the primary anchors. Do not use current page numbers as the main placement method because pagination will change during design and translation.

Each visual entry provides:

| Field | Meaning |
|---|---|
| ID | Stable identifier used in filenames, alt text, source comments, and review notes. |
| Priority | `Essential`, `Supporting`, or `Conditional`. |
| Placement | Exact heading in `08_draft.md` and the position within that section. |
| Text–visual link | The idea in the prose that the visual must help the learner understand. |
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
<!-- VISUAL: BD-V01 -->
![Alt text that communicates the instructional meaning.](../assets/diploma/bd-v01.svg)
```

Recommended filenames are `bd-v01.svg`, `bd-v02.svg`, and so on. Keep an editable SVG master. Export print and screen versions only during production.

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

## 3.1 Welcome And Learning Setup

| ID | Priority | Placement | Text–visual link | Design brief | Format |
|---|---|---|---|---|---|
| `BD-V01` | Supporting | Under `### What we stand for: accessibility, critical thinking, community, and self-sovereignty`, after the paragraph on examining claims and trade-offs. | Makes “teach how to think, not what to think” into a repeatable learner action. | Show a six-step loop: identify the claim; separate fact from preference; inspect evidence and source; compare alternatives; name a trade-off or uncertainty; form a provisional conclusion or question. The loop must allow revision rather than ending in certainty. | Horizontal process strip or circular loop; half page. |
| `BD-V02` | Essential | Under `### What belongs in Core, Custom, and Advanced learning`, after the three definitions and before the closing paragraph. | Clarifies the boundaries among the shared beginner path, local educator choice, and follow-on depth. | Show Blocks 1–3 inside a `Core: all learners` container; Block 4 as `Custom: educator-selected local learning`; and Advanced as a separate onward path. Use arrows to show progression, not a hierarchy of importance. Do not imply that Advanced is required for Diploma completion. | Layered pathway diagram; full width. |
| `BD-V03` | Essential | Under `### How the 4-block learning path is organized`, immediately before the existing four-row table. | Gives learners a mental map of the Diploma before they enter Block 1. | Show one connected sequence: `1 Problem / Fiat → 2 Solution / Bitcoin → 3 Action / Self-Custody → 4 Custom / Bitcoin as Money`. Put a Core bracket under Blocks 1–3 and an educator-choice marker on Block 4. Include each block's core question in short editable text. The final block must not be reduced to spending. | Four-stage roadmap; full width. |
| `BD-V04` | Supporting | Under `### Learning style: in-person preferred, discussion, reflection, practice, and guided activities`, after the description of the learning style. | Shows how a learner moves through a typical concept rather than only reading it. | Show the repeating rhythm `short explanation → guided discussion → safe practice → reflection → explain in your own words`. Include an offline pathway and avoid depicting device use as mandatory. | Five-step rhythm strip; half to full width. |

## 3.2 Block 1: Problem / Fiat

| ID | Priority | Placement | Text–visual link | Design brief | Format |
|---|---|---|---|---|---|
| `BD-V05` | Essential | Under `### Functions and properties of money`, after the properties table and before “No form of money scores perfectly.” | Separates what money does from the qualities that make it useful. | Use two linked layers. Layer 1 shows the three functions: medium of exchange, unit of account, store of value. Layer 2 shows the seven properties: durability, portability, divisibility, fungibility, scarcity, acceptability, verifiability. Use cash, gold, and a generic digital monetary asset only as examples; do not assign a universal winner or a simplistic total score. | Two-layer concept map; full width. |
| `BD-V06` | Essential | Under `### Barter and the double coincidence of wants`, after the Amina, Luis, and Mei scenario and before the formal definition. | Makes the failed exchange relationships in the prose visible. | Show Amina with rice wanting shoes, Luis with shoes wanting cooking oil, and Mei with cooking oil wanting repair work. Use broken or unmatched arrows to show why no direct pair satisfies both wants. Add a second small panel showing how commonly accepted money separates selling from buying. Keep names and objects editable for localization. | Two-panel illustrated flow; full width. |
| `BD-V07` | Supporting | Under `### Scarcity, value, and exchange`, after the definitions of opportunity cost, time preference, and trade-off. | Connects three abstract choice concepts to one everyday decision. | Show one person choosing between two uses of limited money or time. Label the chosen benefit, the best alternative forgone, the present-versus-future preference, and the resulting trade-off. Do not moralize the learner's choice or imply one time preference is always correct. | Branching choice illustration; half page. |
| `BD-V08` | Essential | Under `### Beginner monetary history from barter to modern fiat`, after the `Digital fiat` paragraph. | Prevents the history from appearing as one universal, inevitable sequence. | Create several overlapping tracks rather than one straight progress arrow: direct exchange and local records; commodity forms; standard coins; representative paper; bank and government money; modern fiat; digital fiat. Mark that different forms coexist and developed differently across places. Include 1971 only as a dated milestone in the modern-fiat track, not as the origin of all fiat money. | Braided or layered timeline; full-page width. |
| `BD-V09` | Supporting | Under `### Fiat money`, after the participant table. | Shows where trust, claims, and control sit in a fiat payment system. | Map central bank, commercial bank, government, citizens and businesses, and payment services. Use distinct arrows for money or claims, policy or rules, taxes and spending, and payment instructions. Show that a bank deposit is the bank's liability to the customer. Avoid suggesting that every country has identical institutions or rules. | Actor-and-flow system map; full width. |
| `BD-V10` | Essential | Under `### Fractional reserve banking at beginner level`, after the paragraph beginning “When a commercial bank approves a loan” and before the definition of fractional reserve banking. | Makes deposit creation and the bank balance sheet understandable without relying on a misleading money-multiplier story. | Trace a simplified loan: bank approves loan; bank records a loan asset and a matching deposit liability; borrower can transfer the deposit; settlement and liquidity requirements remain. Label assets and liabilities on both sides. State `simplified example; exact rules vary`. Do not show banks lending out the same physical deposit repeatedly. | Numbered balance-sheet flow; full width. |
| `BD-V11` | Essential | Under `### Fractional reserve banking at beginner level`, after the liquidity-risk and solvency-risk definitions. | Prevents learners from treating liquidity and solvency as the same problem. | Show two parallel simplified bank snapshots. In the liquidity case, assets exceed liabilities but too little is immediately available. In the solvency case, asset value is below liabilities. Use small round example numbers and label them as fictional. | Side-by-side balance-sheet comparison; half to full width. |
| `BD-V12` | Essential | Under `### Inflation and purchasing power`, after the basket example in the second paragraph. | Shows the inverse relationship between a rising basket price and what a fixed amount of money can buy. | Use the same fixed amount of currency at two dates. At Date A it buys the full basket; at Date B the basket costs more and the fixed amount buys less. Distinguish `price level` from `purchasing power`. Use fictional or sourced-and-dated local values; never mix the two. | Before-and-after quantity illustration; full width. |
| `BD-V13` | Supporting | Under `### CBDCs as a beginner fiat-system example where appropriate`, after the paragraph beginning “A CBDC does not create a fixed monetary supply.” | Clarifies that digital, centralized, decentralized, private, and scarce are different attributes. | Compare physical cash, commercial-bank digital deposits, a generic retail CBDC, and Bitcoin across issuer or controller, form, access permission, visibility, supply-rule control, and independent verifiability. Mark CBDC features as design-dependent. Do not imply that all CBDCs have identical surveillance or control features. | Layered comparison matrix with icons; full width. |
| `BD-V14` | Supporting | Under `### Why people look for alternatives (Precious Metals, Real Estate, Stocks)`, after the existing comparison table. | Reinforces that each alternative serves some purposes while introducing different constraints. | Place cash, precious metals, real estate, stocks, and Bitcoin around the needs `daily payment`, `long-term saving`, `portability`, `income or productive use`, and `direct control`. Use qualitative callouts, not a ranked score or investment recommendation. | Trade-off landscape; full width. |

## 3.3 Block 2: Solution / Bitcoin

| ID | Priority | Placement | Text–visual link | Design brief | Format |
|---|---|---|---|---|---|
| `BD-V15` | Essential | Under `### Why Bitcoin was created`, after the paragraph beginning “Bitcoin was created to solve this problem.” | Contrasts a central ledger keeper with Bitcoin's distributed verification model. | Left panel: sender and receiver depend on one intermediary that keeps and approves the ledger. Right panel: signed transactions propagate to independent nodes; miners propose blocks; nodes verify the same public rules. Emphasize reduced dependence on a central settlement authority, not removal of all trust. | Two-system comparison diagram; full width. |
| `BD-V16` | Supporting | Under `### The search for digital and decentralized money`, after “Bitcoin grew from decades of work by many people.” | Shows that Bitcoin combined prior ideas rather than appearing without context. | Create an idea lineage with DigiCash, Hashcash, Bit Gold, B-money, reusable proof of work, and peer-to-peer file sharing feeding distinct contributions toward Bitcoin. Label contributions carefully; do not imply that every project directly supplied code or that Bitcoin has one intellectual predecessor. | Converging idea timeline; full width. |
| `BD-V17` | Essential | Under `### Early digital-money attempts and the double-spend problem`, after the four-step numbered explanation. | Explains how a conflicting second spend is resolved without a central database. | Begin with one spendable output and two conflicting payment attempts. Show transactions announced, miners proposing order in candidate blocks, nodes rejecting invalid or conflicting history, and the valid chain with the most accumulated work becoming accepted. Use the text's four-step vocabulary. Do not imply that one miner decides validity. | Four-step conflict-resolution flow; full width. |
| `BD-V18` | Essential | Under `### Bitcoin origin timeline`, replace the current date/event table visually while retaining an accessible text equivalent. | Connects the four historical events to why each matters. | Show 31 Oct 2008 whitepaper; 3 Jan 2009 Genesis Block; 12 Jan 2009 first recorded person-to-person transaction; 22 May 2010 Pizza Day. Pair each event with a short significance line. Use document-style illustrations or rights-cleared source images only; avoid portraits or identity speculation for Satoshi. | Four-milestone timeline; full width. |
| `BD-V19` | Essential | Under `### Decentralization`, after the list of decentralizing features and before the paragraph beginning “Decentralization is not the same as equal influence.” | Makes the distribution and limits of participant power visible. | Place users, nodes, miners, developers, and services around the shared protocol and public ledger. For each, show `can do` and `cannot do unilaterally`. Services must sit outside the protocol boundary. Show unequal influence and points of dependence without adding a central controller. | Roles-and-rules network map; full width. |
| `BD-V20` | Supporting | Under `### Digital scarcity and credible scarcity`, after the second paragraph. | Distinguishes a written supply claim from a supply rule independently enforced in practice. | Compare `claim on a website or issuer database` with `public rule checked by many independent nodes`. Show that signatures, transaction history, proof of work, and node verification jointly prevent invalid creation or double spending. Avoid saying that scarcity alone creates value. | Credibility comparison diagram; half to full width. |
| `BD-V21` | Essential | Under `### Finite supply`, after the paragraph describing halvings. | Separates maximum supply, issuance, block subsidy, halving, and miner fees. | Show a descending step chart for block subsidy by halving era and a rising cumulative issuance curve approaching 21 million. Mark halvings by block height or era and `roughly four years`, not guaranteed calendar dates. Show transaction fees separately from new issuance. Include no price curve or adoption prediction. | Paired issuance chart; full width. |
| `BD-V22` | Essential | Under `### Satoshis and unit bias`, replace the unit table visually while retaining a text equivalent. | Makes divisibility intuitive and counters the belief that a learner needs one whole bitcoin. | Start with `1 BTC = 100,000,000 sats`, then zoom into 0.1 BTC, 0.01 BTC, 0.001 BTC, and 1 sat. Show that differently displayed amounts can represent the same value, using `100,000 sats = 0.001 BTC`. Do not show a current fiat price. | Zooming denomination graphic; half to full width. |
| `BD-V23` | Supporting | Under `### Peer-to-peer transfer`, after the paragraph explaining that peer-to-peer does not always mean only two computers communicate. | Separates direct settlement rules from the communications and service infrastructure a transaction may pass through. | Show sender wallet → network peers → recipient wallet, with optional exchange, hosted wallet, payment service, and internet provider around the path. Use different line styles for transaction propagation, custody, and communications. The presence of network infrastructure must not be mistaken for central approval. | Layered transfer-path diagram; full width. |
| `BD-V24` | Essential | Under `### Users, nodes, and miners`, after the paragraph on developers and before “These roles limit one another.” | Gives beginners a durable model of who does what in Bitcoin. | Show users signing or accepting transactions; nodes validating and relaying; miners assembling candidate blocks and performing proof of work; developers proposing software; services serving customers. Then show the checks among roles. Do not label all wallet users as nodes or developers as rule-makers. | Participant role map; full width. |
| `BD-V25` | Essential | Under `### Proof of work at a beginner level`, after the paragraph beginning “When a miner finds a valid result.” | Makes costly-to-produce and easy-to-verify work visible. | Show candidate block data entering repeated hash attempts; many results miss the target; one result meets it; the miner broadcasts the block; nodes quickly verify proof and all other rules; accepted blocks add accumulated work. Include difficulty adjustment as a small feedback loop. Do not depict mining as solving an externally useful puzzle. | Sequential process diagram; full width. |
| `BD-V26` | Essential | Under `### Review: how does Bitcoin respond to fiat problems?`, immediately before the existing problem/response table. | Reconnects the entire Block 2 explanation to the Block 1 problems and the new responsibilities introduced by Bitcoin. | Use three aligned columns: fiat-system issue; Bitcoin design response; new responsibility or trade-off. Include supply policy, intermediary dependence, central ledger control, access, purchasing power uncertainty, and institutional recovery. Do not label the middle column `perfect solution`. | Bridge diagram or visual table; full width. |

## 3.4 Block 3: Action / Self-Custody

| ID | Priority | Placement | Text–visual link | Design brief | Format |
|---|---|---|---|---|---|
| `BD-V27` | Essential | Under `### Wallets`, after the paragraph explaining that bitcoin is not stored inside the wallet. | Corrects the most important beginner wallet misconception. | Show the Bitcoin ledger as the record of spendable outputs; the wallet holding or managing keys and constructing instructions; the user authorizing an action; and the network verifying it. Do not draw coins sitting inside a phone or hardware device. | Conceptual layer diagram; full width. |
| `BD-V28` | Essential | Under `### Addresses`, after the explanation of an address and before any practice instructions. | Shows what an address is, what is safe to share, and what must be checked. | Use a fictional on-chain receive screen with a sample address, matching QR, network label, optional amount, and `SAMPLE — DO NOT PAY`. Annotate who creates the address, what may be shared, and which fields the sender and receiver compare. Do not use live wallet branding unless approved and dated. | Annotated interface mockup; half to full width. |
| `BD-V29` | Essential | Under `### Keys`, after the definitions of private and public keys. | Explains the one-way relationship among private key, public information, signing, and verification. | Show private key kept secret; public key or address information derived for receiving or verification; a signature created without revealing the private key; nodes verifying the signature. Use conceptual symbols, never realistic secret strings. Do not show arrows implying a private key can be derived from an address. | One-way cryptography relationship diagram; full width. |
| `BD-V30` | Essential | Under `### Seed phrases`, after the explanation of what a seed phrase does. | Places the seed phrase correctly in the recovery chain without teaching that every wallet uses an identical recovery method. | Show seed or wallet backup → wallet recreates keys → expected addresses and transaction access return. Mark the backup as secret and offline. Add `method and compatibility depend on the wallet`. Do not show actual words, screenshots of recovery entry, or educator access. | Recovery relationship diagram; half to full width. |
| `BD-V31` | Essential | Under `### Custodial and non-custodial use`, before the existing comparison table. | Makes custody a question of key control rather than interface appearance. | Left: user logs into a service; service controls keys and authorizes withdrawal. Right: user controls keys; wallet signs under the user's authority; network checks the transaction. Show recovery responsibility and failure point in both paths. Avoid portraying self-custody as morally superior or risk free. | Side-by-side custody model; full width. |
| `BD-V32` | Supporting | Under `### Hot and cold wallets`, after the existing wallet comparison table. | Connects wallet type to exposure and use rather than treating `hot`, `cold`, and `custodial` as one scale. | Use two axes or layers: key control (`custodial` versus `self-custodial`) and connectivity or signing environment (`hot` versus `cold or hardware`). Place common use patterns and threat examples in the correct areas. Explicitly show that a custodial account is not a type of self-custodial wallet. | Two-axis classification graphic; full width. |
| `BD-V33` | Essential | Under `### Wallet recovery and seed phrase testing`, after the numbered safe recovery principles. | Turns the recovery text into a safe sequence a learner can rehearse. | Show `create empty or tiny-value training wallet → record backup privately → verify using the approved wallet method → reset or use a separate training environment → recover → compare expected receiving information or history → securely clear temporary device`. Put `educator never sees the secret` outside every step. | Safety-gated workflow; full width. |
| `BD-V34` | Essential | Under `### Receiving bitcoin`, after the numbered on-chain receiving steps. | Lets a learner identify the elements of a receive request before live practice. | Show receiver device, sample address or QR, sender verification, broadcast or pending status, and confirmation. Annotate amount, unit, network, address, and status. Use fictional data and mark the whole visual non-payable. | Annotated receiving flow; full width. |
| `BD-V35` | Essential | Under `### Sending bitcoin`, after the numbered pre-send steps. | Makes verification happen before approval and separates recipient checks from fee and timing decisions. | Show a staged confirmation screen: independently verify recipient; scan or enter destination; compare network and address or invoice; confirm amount and unit; review fee and timing; use small test when needed; approve; save TXID. Put an irreversible boundary immediately after approval. | Preflight-to-settlement flow; full width. |
| `BD-V36` | Essential | Under `### Verification, block explorers, and irreversible transactions`, after the paragraph defining the first confirmation and increasing depth. | Connects transaction status, block inclusion, and later confirmations. | Show a transaction first in the pending pool, then included in Block N as confirmation 1, followed by Blocks N+1, N+2, and N+3 increasing depth. Pair it with a small annotated fictional explorer panel showing TXID, amount, fee, status, and confirmations. Add a privacy callout about searching personal data. | Confirmation timeline plus explorer inset; full width. |
| `BD-V37` | Supporting | Under `### Safety checklist: seed phrases, address checks, scams, and starting small`, immediately before the checklist. | Gives learners a simple priority order when the full checklist feels dense. | Show four gates: protect secrets; verify software and contacts; verify destination, network, amount, and fee; limit the size of mistakes. Surround them with the rule `pressure or uncertainty → stop`. Do not compress away the detailed checklist below it. | Four-gate safety map; half to full width. |
| `BD-V38` | Supporting | Under `### Acquiring and exchanging bitcoin as pathway awareness, not financial advice`, after the five pathway descriptions and before the comparison questions. | Shows that acquiring bitcoin is an end-to-end route with risks before and after the moment of exchange. | Map earning, peer-to-peer, exchange or broker, ATM or kiosk, and merchant or community receipt as separate paths into either self-custody or custodial balance. Label price or spread, fees, identity, reversibility, counterparty, withdrawal, and local-law checkpoints. Do not rank or recommend a provider. | Branching pathway map; full width. |
| `BD-V39` | Essential | Under `### On-chain and Lightning payments at beginner level`, immediately before the existing feature table. | Makes the layer relationship and appropriate-use distinction visible. | Show Bitcoin base-layer settlement beneath Lightning payment channels. Compare payment request, route, timing, fee conditions, custody variability, and failure modes. Use one small-payment and one final-settlement example. Do not imply that Lightning is a separate coin or that all Lightning wallets are self-custodial. | Layer diagram plus concise comparison; full width. |
| `BD-V40` | Supporting | Under `### Review: what does self-custody responsibility mean?`, immediately before the responsibility table. | Synthesizes the block as responsibilities surrounding key control. | Put `control of keys` in the center, surrounded by backup, recovery, receiving, sending, tool choice, acquisition path, privacy, and scam checks. For each, show the protected item and the consequence of failure in very short text. | Responsibility map; full width. |

## 3.5 Block 4: Custom / Bitcoin As Money

| ID | Priority | Placement | Text–visual link | Design brief | Format |
|---|---|---|---|---|---|
| `BD-V41` | Essential | Under `### Educator-selected local modules`, after the explanation of what remains shared and what can change locally. | Explains how Block 4 stays coherent while adapting to a community. | Show MFB supplying shared outcomes, templates, and safety boundaries; educator selecting and adapting local practice; local expert or community validating tools, laws, risks, language, and infrastructure; learner completing one relevant local pathway. Do not show the educator changing Core outcomes. | Responsibility-and-choice diagram; full width. |
| `BD-V42` | Supporting | Under `### Practical workshops and demonstrations`, after the definitions of Presentation, Practice, and Production. | Shows how a safe practical skill develops from observation to independent explanation or performance. | Create three stages: Presentation by educator; guided Practice with mockup, test environment, or tiny value; Production by learner with evidence and reflection. Add safety gates for no funds, test funds, or tiny value and an offline alternative at every stage. | Three-stage PPP workflow; full width. |
| `BD-V43` | Conditional | Under `### Local Bitcoin tools and resources`, after the tool-selection questions and before `Local tool record`. | Helps learners see that an interface belongs to a custody, network, and support context. | Show a generic tool at the center linked to need, custody model, network or layer, recovery, cost, privacy, support, limits, and local law. All fields must be editable and date-stamped. Do not show an approved-products badge or a globally recommended wallet. | Local tool evaluation wheel; half to full width. |
| `BD-V44` | Conditional | Under `### Lightning payments where locally appropriate`, after the six guided-payment steps. | Makes a Lightning payment understandable while keeping custody and failure risk visible. | Show receiver creates request; sender scans or copies; sender verifies recipient, amount, unit, expiry, and fee; sender approves; payment routes; both wallets report success or failure. Add custody labels on both wallets and a branch for failure. Use generic, nonfunctional screens. | Lightning payment sequence; full width. |
| `BD-V45` | Supporting | Under `### Daily-life Bitcoin use`, after the seven use descriptions and before the three evaluation questions. | Broadens `Bitcoin as money` beyond spending. | Place a person or community need at the center with earning, saving, receiving, sending, spending, pricing or accounting, and donating around it. Each use gets one benefit and one new responsibility. Do not make all arrows circular or imply every learner should perform every use. | Use-case wheel; full width. |
| `BD-V46` | Conditional | Under `### Local spending and receiving scenarios`, before Scenario 1. | Gives all local scenarios one reusable visual grammar so educators can substitute local actors and goods. | Create a four-frame template: need and actors; payment request and chosen path; verification and settlement; record, refund, custody, or conversion. Include editable slots for small purchase, work payment, family transfer, refund, or donation. The template must work with simulation or tiny value. | Reusable scenario storyboard; full width. |
| `BD-V47` | Essential | Under `### Local on-ramp and off-ramp pathways`, after the definition and pathway list and before the pathway comparison table. | Forces comparison of the complete route rather than only the advertised first fee. | Show local money, work, goods, or services entering through possible routes; custody and identity checkpoints; on-chain or Lightning transfer; self-custody or service balance; and final use, holding, or conversion. Label spread, fees, time, reversal, withdrawal, counterparty, privacy, support, and law along the route. | End-to-end pathway map; full width. |
| `BD-V48` | Conditional | Under `### KYC and no-KYC trade-offs where locally appropriate`, immediately before the comparison table. | Frames KYC and non-KYC as different bundles of benefits and risks, not as good versus bad. | Compare data collection, account recovery, bank access, legal conditions, fraud protection, counterparty exposure, liquidity, price, support, and on-chain linkability. Include `local law varies; verify current information`. Do not imply evasion or guaranteed privacy. | Balanced trade-off comparison; full width. |
| `BD-V49` | Essential | Under `### Circular economies`, after the seven mapping questions. | Shows value circulating among participants and reveals where the loop depends on outside services or support. | Map workers, customers, merchants, suppliers, educators or support, and exchange or on/off-ramp points. Use separate arrows for value, goods or services, and support. Mark custody, volatility, connectivity, and conversion dependencies. Include broken-loop examples such as immediate conversion or one organizer processing everything. | Editable local network map; full width. |
| `BD-V50` | Supporting | Under `### Merchant or community use cases`, after the merchant decision checklist and before the community-use examples. | Shows that accepting Bitcoin is an operational process, not just displaying a QR code. | Trace pricing → payment request → customer verification → merchant confirmation → receipt or record → custody or conversion → refund or exception. Add staff, accounting, tax, device security, offline failure, and support callouts. Use local-law placeholders, not assertions. | Merchant payment operations flow; full width. |
| `BD-V51` | Conditional | Under `### Local resource maps and community discovery`, immediately before `Record your local resources`. | Connects community discovery with verification and privacy rather than treating a map listing as proof. | Provide an editable neighborhood or regional map template with merchant, educator, meetup, technical support, exchange information, legal or tax information, and missing-support markers. Every listing includes `date verified` and a safety note. Do not include real personal locations without consent. | Local resource-map template; full width. |
| `BD-V52` | Supporting | Under `### Review: how can Bitcoin function as money in this community?`, immediately before the final `Need / Fit / Method / Custody / Cost / Safety / Local context / Evidence` table. | Turns the final test into a sequence that begins with a need and ends with evidence, rather than beginning with a tool. | Show the decision path `real need → Bitcoin fit → payment method → custody → total cost and trade-offs → safety and local conditions → evidence of success`. Add a return arrow when Bitcoin is not the best available fit. | Decision path; full width. |

## 3.6 Back Of Diploma

| ID | Priority | Placement | Text–visual link | Design brief | Format |
|---|---|---|---|---|---|
| `BD-V53` | Supporting | Under `### A short “What now?” next-steps list`, after the numbered list. | Helps learners choose one safe continuation without suggesting that all paths are required. | Branch from the Diploma foundation to repeat a practical skill, improve a safety plan, join a responsible community, continue to Advanced learning, become or support an educator, contribute a translation or correction, and support the project. Keep the branches equal and voluntary. | Next-step pathway map; full width. |
| `BD-V54` | Essential | Under `### A safety reminder`, immediately before the reminder list. | Makes the minimum stop-and-check behavior memorable at the point of course completion. | Show `stop → verify source and recipient → verify custody, network, destination, amount, and fee → start small → proceed only when understood`. Put seed or private-key secrecy above the whole sequence as a non-negotiable boundary. | Compact safety strip; half to full width. |
| `BD-V55` | Conditional | Under `### Source or update page, if included`, after the canonical source link. | Provides one durable route to updates and contributions without filling the Diploma with fragile QR codes. | Create one panel containing a tested QR code, printed short URL, destination name, edition or last-verified date, and plain-language purpose. The QR must resolve to the canonical maintained source or landing page. Keep donation and certificate verification separate unless the landing page clearly distinguishes them. | QR and fallback-link panel; half page. |
| `BD-V56` | Conditional | Under `### Certificate verification`, after the opening paragraph. | Shows a privacy-respecting verification process if the issuing system supports one. | Show certificate holder or verifier → official verification destination → code, signature, or identifier check → result with course, edition, issuer, date, status, and minimum necessary learner data. Do not invent a verification system or show personal data. Produce only after the real method is confirmed. | Verification flow; half to full width. |

---

# 4. Reuse And Combination Rules

The index contains conceptual requirements, not a command to create the largest possible number of files. Combine visuals only when the combined result remains readable and preserves each placement's learning purpose.

Preferred reuse:

- `BD-V05` establishes the visual language for later money-property comparisons.
- `BD-V09`, `BD-V19`, and `BD-V24` should share actor symbols while keeping fiat-system and Bitcoin roles distinct.
- `BD-V28`, `BD-V34`, `BD-V35`, and `BD-V36` should use one generic, nonfunctional interface family.
- `BD-V31` and `BD-V32` should share custody labels and definitions.
- `BD-V38` and `BD-V47` should share pathway symbols, but Block 3 remains global orientation while Block 4 is locally completed.
- `BD-V39` and `BD-V44` should share on-chain and Lightning layer notation.
- `BD-V41`, `BD-V46`, `BD-V49`, and `BD-V51` should be designed as editable templates for localization.
- `BD-V37` and `BD-V54` should use the same safety-gate vocabulary.

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
id: BD-V00
priority: essential | supporting | conditional
source_document: workspace/08_draft.md
source_heading: Exact heading from the placement field
insert_position: Exact before/after instruction
text_concept: The prose idea this visual explains
learning_intent: What the learner should understand after viewing it
visual_type: Diagram | illustration | timeline | annotated interface | map
required_elements: []
guardrails: []
title: Short learner-facing title
caption: What the learner should notice
asset_master: assets/diploma/bd-v00.svg
screen_export: assets/diploma/bd-v00.png
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

This index should be revised whenever `08_draft.md` changes materially. It should remain a map from text to visual meaning, not become the production tracker for the visual files themselves.
