# Bitcoin For Organizations Diploma Merge Map

## Purpose

This document shows what, if anything, from the retiring `ref/bitcoin-for-organizations/en` path should be merged into the redesigned beginner Bitcoin Diploma.

Review date: 2026-06-26

Sources reviewed:

- `ref/bitcoin-for-organizations/en`
- `workspace/03_scope.md`
- `workspace/05_objectives.md`
- `workspace/07_contents.md`
- `workspace/08_draft.md`

Related Advanced merge map:

- `workspace/advancedorganizations.md`

## Cannibalization Decision

Bitcoin for Organizations will no longer exist as a standalone path after the redesign.

Its content should be cannibalized into:

- the beginner Diploma only where it helps beginners meet the existing scope and objectives;
- Advanced modules where the material is strategic, operational, technical, financial, legal, policy-oriented, or sector-specific.

Most Organizations content is too advanced for the 8-hour beginner Diploma.

The key beginner question is:

Does this information help a beginner explain money, fiat, Bitcoin, custody, verification, safety, or local Bitcoin use more clearly?

If yes, it is listed here. If no, it belongs in `advancedorganizations.md` and later in `17_advanced.md`.

## Summary Decision

Use Organizations content in the Diploma only as compressed support for:

- Block 1: CBDCs as digital fiat and a trust/control comparison;
- Block 2: digital scarcity, the double-spend problem, Bitcoin's technical lineage, credible scarcity, decentralization, and protocol/layers framing;
- Block 3: confirmations, block explorer verification, public ledger transparency, and privacy trade-offs;
- Block 4: local merchant, remittance, nonprofit, underbanked, and circular-economy scenarios;
- Educator Guide and Activity Bank: misconception prompts, claim/evidence/trade-off discussion, and local scenario activities.

Do not import the Organizations path as prose chapters into the Student Book.

## Fit With Scope And Objectives

The useful beginner material supports these scope items from `03_scope.md`:

- content reduction and essential versus Advanced classification;
- practical learning redesign;
- Activity Bank development;
- Educator Guide misconception support;
- safety notes and fact-check notes for live tools, named services, and current data;
- beginner clarification for sats, Lightning distinctions, acquisition-pathway risks, scam awareness, verification, and local practice.

It supports these objectives from `05_objectives.md`:

- Objective 5: describe fiat-system problems;
- Objective 6: explain why Bitcoin was created;
- Objective 7: identify decentralization, finite supply, peer-to-peer transfer, and verifiability;
- Objective 8: describe users, nodes, miners, proof of work, 21 million limit, halving, and sats at beginner level;
- Objective 12: identify safety practices and beginner risks;
- Objective 13: describe receiving, sending, recovery, seed phrase testing, and verification at beginner level;
- Objective 14: distinguish on-chain and Lightning payments;
- Objective 15: identify beginner acquisition or exchange pathways without recommendation;
- Objective 16: distinguish beginner practical Bitcoin use from advanced technical theory;
- Objective 17: participate in guided discussion using clear explanations and basic reasoning.

## Recommended Beginner Merge Items

| Priority | Useful Organizations content | Beginner value | Scope/objective fit | Where in `07_contents.md` | Where in `08_draft.md` | Action |
|---|---|---|---|---|---|---|
| High | CBDCs as digital fiat, not Bitcoin | Helps beginners compare central-bank digital money with Bitcoin without assuming all digital money is the same | Objectives 5, 7, 17 | Block 1: `CBDCs as a beginner fiat-system example where appropriate` | Block 1: `CBDCs as a beginner fiat-system example where appropriate` | Keep and lightly strengthen. Emphasize issuer, supply, permission, privacy, rule changes, and verification. Do not include country counts. |
| High | Digital scarcity and double-spend problem | Helps beginners understand why Bitcoin was created and why a decentralized digital money was difficult | Objectives 6, 7, 8 | Block 2: `Early digital-money attempts and the double-spend problem`; `Why Bitcoin was created` | Block 2: `Why Bitcoin was created`; `Early digital-money attempts and the double-spend problem` | Add or preserve plain-language digital-copy explanation. Avoid attack probability tables. |
| High | Technical origin lineage: Cypherpunks, DigiCash, Hashcash, BitTorrent, B-money/Bit Gold, reusable proof of work | Shows Bitcoin as a synthesis of earlier attempts, not a random invention | Objectives 6, 8, 16 | Block 2: `The search for digital and decentralized money`; `Bitcoin origin timeline` | Block 2: `The search for digital and decentralized money`; `Early digital-money attempts...`; `Bitcoin origin timeline` | Use only a short timeline and one-sentence contributions. Route cryptography/protocol depth to Advanced. |
| High | Verification through block explorers and public ledger inspection | Supports practical competence and "don't trust, verify" | Objectives 12, 13, 17 | Block 3: `Verification, block explorers, and irreversible transactions` | Block 3: `Verification, block explorers, and irreversible transactions` | Keep as a beginner demonstration or Activity Bank task. Include privacy warning. |
| Medium | Confirmations and settlement confidence | Helps learners understand transaction status and irreversible settlement | Objectives 13, 14 | Block 3: `Verification, block explorers, and irreversible transactions` | Block 3: `Verification, block explorers, and irreversible transactions` | Add only beginner wording: more confirmations increase confidence. Keep six-confirmation math and reorg scenarios Advanced. |
| Medium | Protocol/layers framing for scalability and innovation objections | Helps beginners distinguish base-layer settlement from Lightning without seeing slowness as failure | Objectives 7, 14, 16, 17 | Block 2: `Peer-to-peer transfer`; `Proof of work`; Block 3: `On-chain and Lightning payments at beginner level` | Block 2: `Bitcoin as sound digital money`; Block 3: `On-chain and Lightning payments at beginner level` | Use a short educator note or one paragraph. Detailed TCP/IP, Liquid, Fedimint, Cashu, and sidechains remain Advanced. |
| Medium | Who controls Bitcoin: developers, miners, nodes, users | Strengthens beginner decentralization and rule-verification understanding | Objectives 7, 8, 16 | Block 2: `Decentralization`; `Users, nodes, and miners` | Block 2: `Decentralization`; `Users, nodes, and miners` | Keep at role level. Do not teach full soft fork/hard fork governance in Core. |
| Medium | Credible scarcity versus "many coins" | Helps answer a common beginner confusion without turning the Diploma into a crypto survey | Objectives 7, 16, 17 | Block 2: `Finite supply`; possibly Educator Guide FAQ, not TOC | Block 2: `Finite supply`; optional educator note | Use as an educator-guided misconception prompt. Avoid naming many coins or making market predictions. |
| Medium | Local merchant/payment/remittance/nonprofit scenarios | Gives Block 4 practical local relevance | Custom outcomes; Objectives 14, 15, 17 | Block 4: `Local spending and receiving scenarios`; `Merchant or community use cases`; `Circular economies`; `Local on-ramp and off-ramp pathways` | Block 4 scenario sections | Use as optional Custom scenario cards. Local educator must verify tools, fees, law, and safety. |
| Low | Monetization sequence: store of value, medium of exchange, unit of account | Helps answer "if I cannot spend it everywhere, is it money?" | Objectives 1, 3, 4, 7, 17 | Block 2: `Bitcoin as sound digital money`; Block 4 review | Block 2: `Bitcoin as sound digital money`; Block 4 `Daily-life Bitcoin use` | Use sparingly. Keep Gresham's Law and adoption theory Advanced unless educator uses a simple prompt. |
| Low | Energy as security | Helps with a predictable beginner misconception | Objectives 8, 17 | Block 2: `Proof of work at a beginner level` | Block 2: `Proof of work at a beginner level` | Keep one balanced paragraph. Detailed energy grid, methane, ESG, and mining economics go Advanced. |

## Block-By-Block Recommendations

### Block 1: Problem / Broken Money

Organizations source:

- `ref/bitcoin-for-organizations/en/2-dispelling-misconceptions/9-will-a-cbdc-render-bitcoin-obsolete.md`
- selected policy context from `ref/bitcoin-for-organizations/en/4-impact-on-industry-verticals/6-government.md`

Recommended Diploma use:

- Keep CBDCs as an example of digital fiat.
- Make sure learners compare CBDCs and Bitcoin using beginner questions:
  - who issues it?
  - can supply rules change?
  - who can approve or block payments?
  - what information is collected?
  - can users verify the rules independently?

Where:

- `07_contents.md`: already listed under Block 1.
- `08_draft.md`: already has `CBDCs as a beginner fiat-system example where appropriate`.

Suggested refinement:

- No major new section needed.
- If editing later, add one sentence: "A CBDC may be digital, but digital does not mean decentralized or scarce."

Keep out:

- CBDC country counts;
- current implementation lists;
- detailed surveillance or policy arguments;
- legal predictions.

### Block 2: Solution / Bitcoin

Organizations sources:

- `ref/bitcoin-for-organizations/en/3-bitcoin-technical-history/*.md`
- `ref/bitcoin-for-organizations/en/6-adopting-bitcoin/1-the-discovery-of-digital-scarcity.md`
- `ref/bitcoin-for-organizations/en/2-dispelling-misconceptions/3-bitcoin-is-too-slow-to-be-global-money.md`
- `ref/bitcoin-for-organizations/en/2-dispelling-misconceptions/4-there-s-no-innovation-happening-in-bitcoin.md`
- `ref/bitcoin-for-organizations/en/2-dispelling-misconceptions/6-there-are-thousands-of-other-coins.md`
- `ref/bitcoin-for-organizations/en/2-dispelling-misconceptions/7-bitcoin-is-not-truly-decentralised.md`
- `ref/bitcoin-for-organizations/en/2-dispelling-misconceptions/10-will-bitcoin-be-overtaken-by-another-technology.md`

Recommended Diploma use:

- Strengthen the explanation of digital scarcity and double spending.
- Preserve a short pre-Bitcoin lineage:
  - Cypherpunks: privacy and digital freedom context;
  - DigiCash: private digital cash but centralized;
  - Hashcash: proof of work as anti-spam cost;
  - B-money / Bit Gold: proposals for scarce digital money;
  - BitTorrent: peer-to-peer network model;
  - reusable proof of work: another partial attempt;
  - Bitcoin: working system combining public ledger, signatures, proof of work, nodes, miners, and incentives.
- Use the protocol/layers idea to support on-chain versus Lightning later.
- Use "who controls Bitcoin?" to explain developers, miners, nodes, and users at beginner level.
- Use credible scarcity only as a short misconception prompt.

Where:

- `07_contents.md`: Block 2 already includes `The search for digital and decentralized money`, `Early digital-money attempts and the double-spend problem`, `Bitcoin origin timeline`, `Decentralization`, `Finite supply`, `Users, nodes, and miners`, and `Proof of work at a beginner level`.
- `08_draft.md`: Block 2 already has matching sections. The Organizations path can refine these sections rather than create new ones.

Suggested refinements:

- In `Early digital-money attempts and the double-spend problem`, add one-line roles for BitTorrent and reusable proof of work if the section needs slightly more lineage.
- In `Finite supply`, add a simple warning that many coins can claim scarcity but credible scarcity depends on rules, decentralization, and time.
- In `Proof of work at a beginner level`, keep the balanced energy/security paragraph and avoid energy-policy depth.

Keep out:

- OSI model and TCP/IP implementation detail;
- elliptic curve cryptography;
- Merkle tree mechanics;
- Byzantine generals explanation beyond a plain-language mention;
- 51% attack probability tables;
- soft fork/hard fork governance;
- Liquid, Fedimint, Cashu, L402, sidechain, and AI-payment detail.

### Block 3: Action / Self-Custody

Organizations sources:

- `ref/bitcoin-for-organizations/en/8-the-bitcoin-economy/1-the-nature-of-bitcoin-s-ledger.md`
- `ref/bitcoin-for-organizations/en/8-the-bitcoin-economy/4-the-pizza-day-transaction.md`
- `ref/bitcoin-for-organizations/en/6-adopting-bitcoin/1-the-discovery-of-digital-scarcity.md`
- privacy/security notes from `ref/bitcoin-for-organizations/en/4-impact-on-industry-verticals/4-the-impact-on-the-technology-industry.md`

Recommended Diploma use:

- Keep block explorer use as verification orientation.
- Add or preserve a simple activity where learners inspect a transaction, identify confirmation status, fee, amount, and visible public data.
- Mention that public data creates privacy trade-offs.
- Keep confirmations beginner-level.

Where:

- `07_contents.md`: Block 3 already includes `Verification, block explorers, and irreversible transactions`.
- `08_draft.md`: Block 3 already has `Verification, block explorers, and irreversible transactions`.

Suggested refinement:

- Add Pizza Day transaction as an optional educator demonstration or Activity Bank item, not required Student Book content.

Keep out:

- address metrics;
- HODL waves;
- Coin Days Destroyed;
- MVRV;
- Puell Multiple;
- market-cycle analysis;
- institutional custody due diligence;
- corporate treasury custody.

### Block 4: Custom / Bitcoin As Money

Organizations sources:

- `ref/bitcoin-for-organizations/en/4-impact-on-industry-verticals/3-banking-and-payments.md`
- `ref/bitcoin-for-organizations/en/4-impact-on-industry-verticals/7-charities-and-not-for-profit-organisations.md`
- `ref/bitcoin-for-organizations/en/7-bitcoin-s-possible-future/3-banking-the-un-der-banked.md`
- selected local-use material from `ref/bitcoin-for-organizations/en/5-impact-on-internal-functions/1-bitcoin-s-impact-on-it-leaders.md`

Recommended Diploma use:

Use as optional Custom scenario material:

- merchant accepting a Lightning or on-chain payment;
- family remittance or cross-border payment comparison;
- nonprofit donation flow;
- local underbanked access scenario;
- community/circular-economy map;
- local on-ramp/off-ramp comparison;
- local business payment or settlement scenario.

Where:

- `07_contents.md`: Block 4 already includes local tools, Lightning, daily-life use, on/off-ramps, KYC/no-KYC, circular economies, merchant/community use cases, and resource maps.
- `08_draft.md`: Block 4 already has sections that can absorb these examples.

Suggested refinement:

- Add an Activity Bank card titled `Local Payment Path Comparison`.
- Add an Activity Bank card titled `Community Donation Scenario`.
- Add an Educator Guide note that Organizations examples are templates, not global recommendations.

Keep out:

- treasury strategy;
- payroll;
- employee benefits;
- investment management;
- legal, tax, accounting, AML, and KYC instruction;
- named payment companies as recommendations;
- AI-agent payments;
- government policy strategy.

## Educator Guide Recommendations

Organizations provides strong material for educator preparation.

Add a Misconception Bank to `workspace/11_guide.md` later, using Organizations as source material.

Recommended entries:

- Bitcoin has no intrinsic value.
- Bitcoin uses too much energy.
- Bitcoin is too slow.
- Nothing is being built on Bitcoin.
- Governments will ban Bitcoin.
- There are thousands of other coins.
- Bitcoin is not decentralized.
- Bitcoin is not widely used, so is it money?
- CBDCs will replace Bitcoin.
- A better technology will overtake Bitcoin.

Format:

- learner question;
- beginner-safe answer;
- one discussion prompt;
- what not to overclaim;
- source trail for Advanced learning.

## Activity Bank Recommendations

Add these later to `workspace/10_activities.md` if Activity Bank work continues.

### Claim, Evidence, Trade-Off

Source:

- `ref/bitcoin-for-organizations/en/2-dispelling-misconceptions/*.md`

Purpose:

Learners practice guided critical discussion without memorizing slogans.

Learner task:

- choose a claim;
- identify evidence needed;
- name one trade-off;
- explain what remains uncertain.

### Explore The Ledger

Source:

- `ref/bitcoin-for-organizations/en/8-the-bitcoin-economy/1-the-nature-of-bitcoin-s-ledger.md`
- `ref/bitcoin-for-organizations/en/8-the-bitcoin-economy/4-the-pizza-day-transaction.md`

Purpose:

Learners connect verification, confirmations, public data, and privacy.

Learner task:

- inspect a transaction or printed explorer screenshot;
- identify amount, fee, confirmations, and public information;
- explain one privacy risk.

### Local Payment Path Comparison

Source:

- `ref/bitcoin-for-organizations/en/4-impact-on-industry-verticals/3-banking-and-payments.md`
- `ref/bitcoin-for-organizations/en/7-bitcoin-s-possible-future/3-banking-the-un-der-banked.md`

Purpose:

Learners compare an existing local payment method with a Bitcoin or Lightning path.

Learner task:

- compare fees, timing, custody, privacy, reversibility, and failure points.

### Community Donation Scenario

Source:

- `ref/bitcoin-for-organizations/en/4-impact-on-industry-verticals/7-charities-and-not-for-profit-organisations.md`

Purpose:

Learners examine a local nonprofit/community use case without requiring real donations.

Learner task:

- design a safe donation flow;
- identify custody, transparency, verification, and recordkeeping needs.

## Source Audit By Organizations Module

| Organizations module | Beginner usefulness | Diploma destination | Main reason most content does or does not fit |
|---|---|---|---|
| 1. Bitcoin and Risk Management | Low to Medium | Block 4 discussion / Activity Bank only | Scenario thinking is useful, but risk-register methods are organizational and Advanced. |
| 2. Dispelling Misconceptions | Medium to High | Educator Guide; selected Block 1/2/3 prompts | Beginner questions are common, but full rebuttal essays are too long and advanced. |
| 3. Bitcoin Technical History | Medium | Block 2 timeline and double-spend context | Useful lineage, but cryptography and protocol mechanics are Advanced. |
| 4. Impact on Industry Verticals | Low for Core; Medium for Custom | Block 4 scenario cards only | Sector analysis is Advanced; local merchant/remittance/nonprofit examples can support Custom. |
| 5. Impact on Internal Functions | Low | Mostly Advanced | IT leadership, treasury, payroll, and business operations exceed beginner scope. |
| 6. Adopting Bitcoin | Medium | Block 2 digital scarcity; Block 3 confirmations | Digital scarcity is useful; adoption-cycle and reorg math are Advanced. |
| 7. Bitcoin's Possible Future | Low for Core; Medium for Custom discussion | Block 4 local future scenario only | Most future claims are speculative; local reflection can be useful if framed carefully. |
| 8. The Bitcoin Economy | Medium | Block 3 verification; Activity Bank | Block explorers support beginner verification; on-chain analytics are Advanced. |

## Material Explicitly Rejected For The Beginner Diploma

Do not add the following to the required beginner Student Book:

- corporate treasury strategy;
- investment management;
- portfolio allocation;
- Sharpe ratio, Sortino ratio, correlation, TAM, hurdle rate;
- tax, legal, accounting, AML, KYC, and reporting instruction;
- institutional custody vendor selection;
- business SWOT/PESTLE/Porter's Five Forces;
- government policy options;
- detailed CBDC rollout status;
- energy-grid economics;
- methane/flaring and renewable project finance;
- AI-agent payments, L402, and HTTP 402;
- Nostr, healthcare data, e-voting, sats rewards as full topics;
- Liquid, Fedimint, Cashu, sidechains, Chaumian mints;
- on-chain market indicators;
- reorg probability tables;
- detailed cryptography;
- named companies, wallets, exchanges, custodians, or service providers as recommendations.

All of this should go to `workspace/advancedorganizations.md` and later `workspace/17_advanced.md`.

## Fact-Check Flags If Used In Beginner Materials

If any Organizations-derived examples are used in public beginner materials, verify and date them first:

- CBDC country/project status;
- Bitcoin holder estimates;
- Bitcoin price, market cap, hashrate, fees, or supply figures;
- Lightning usage claims;
- legal tender and national policy status;
- merchant maps and local resources;
- wallet, exchange, custodian, or payment-service names;
- local fees, taxes, laws, and KYC/no-KYC requirements;
- energy-use claims;
- company or nonprofit examples.

## Recommended Next Action

When the Diploma draft is edited, use this file as a checklist:

1. Keep the beginner Student Book lean.
2. Add only the high-priority beginner items if they are not already covered.
3. Put misconception handling mostly in the Educator Guide.
4. Put practical scenario material mostly in the Activity Bank and Custom block templates.
5. Route everything advanced to `advancedorganizations.md` and `17_advanced.md`.

The redesigned Diploma should gain clarity from Bitcoin for Organizations, not inherit its complexity.
