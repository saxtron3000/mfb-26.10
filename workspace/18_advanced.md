# Bitcoin Diploma Advanced Module Holding File

## Purpose

This file is the active holding place for future Advanced module work connected to the Bitcoin Diploma redesign.

It collects:

- Advanced module title ideas;
- follow-on pathway ideas;
- content moved out of the shorter beginner Diploma;
- technical, economic, philosophical, and practical material that should not be lost;
- legacy source trails from the 2026.04 Diploma and reference chapters;
- future module seeds, activity seeds, research notes, and open design questions.

The Advanced modules are not part of the current beginner Diploma publication work. Work on Advanced modules should begin only after the redesigned Bitcoin Diploma is published.

For now, this file preserves ideas and source material so the shorter Diploma can stay concise without deleting useful material.

---

# 1. Status And Use

## Current Status

Status: holding file.

This is not a finished Advanced curriculum, a module sequence, a public table of contents, or a publication-ready document.

Use this file as a collection point for material that may later become:

- optional extensions;
- separate Advanced modules;
- educator background;
- technical demonstration workshops;
- follow-on courses;
- specialized community modules;
- future research or editorial tasks.

## Timing Rule

Do not begin full Advanced module design until the redesigned Bitcoin Diploma has been published.

The beginner Diploma must remain the priority. Advanced work should not pull time, scope, or complexity back into the Core pathway.

## Preservation Rule

If useful information is edited out of the newer beginner Diploma, do not treat it as deleted.

Place it here with enough context to recover it later:

- topic;
- source file;
- likely Advanced module;
- reason it was removed from Core;
- notes for future use.

The absence of a topic from `08_student.md` does not mean the topic is unimportant. It may simply be too detailed, too local, too technical, too current-data-dependent, or too risky for an 8-hour beginner pathway.

---

# 2. Ownership Boundaries

| Topic | Owner document |
|---|---|
| Four-block beginner architecture | `06_plan.md` |
| Core / Custom / Advanced boundary rules | `06_plan.md` |
| Advanced title inventory | `18_advanced.md` |
| Advanced follow-on pathway ideas | `18_advanced.md` |
| Redacted legacy material for future Advanced use | `18_advanced.md` |
| Student-facing beginner guide | `08_student.md` |
| Beginner objectives | `05_objectives.md` |
| Beginner assessment | `13_assessment.md` |
| Activity templates | `10_activities.md` |
| Educator facilitation guidance | `12_educator-draft.md` |
| Publication rules | `17_spec.md` |

`06_plan.md` remains the source of truth for the active beginner redesign structure.

`18_advanced.md` is the source of truth for Advanced module ideas, title inventory, source trails, and parked content.

---

# 3. Advanced Boundary From The Plan

Advanced outcomes are ongoing and should be designed module by module.

Advanced content should not overload the beginner pathway. It may become optional extensions, separate workshops, educator background, or follow-on courses.

Advanced content may include deeper:

- monetary history;
- economics;
- investment, risk, and capital-allocation reasoning;
- fiat-system analysis;
- Bitcoin history;
- cryptography;
- transaction mechanics;
- UTXO analysis;
- mempool analysis;
- node operation;
- mining mechanics;
- consensus;
- Lightning operations;
- privacy;
- security;
- custody models;
- business operations;
- community and circular economy development;
- philosophy;
- human rights;
- open-source contribution;
- communication networks;
- Bitcoin education practice.

Core learners should not be expected to master these topics inside the 8-hour beginner Diploma.

---

# 4. Candidate Advanced Module Titles

The full Advanced module title list should appear only in this file.

Candidate Advanced module titles:

- History of Money (localisation)
- Monetary Economics
- History of Bitcoin
- Philosophy of Bitcoin
- Transactions & Settlement
- Mining & Consensus
- Privacy & Security
- Payments & Exchange
- Bitcoin for Business
- Infrastructure & Maintenance
- Communities & Circular Economies
- Money & Society
- Money & Human Rights
- Energy & Mining
- Open Source Software
- Nostr & Decentralized Communication
- Communication Networks
- Bitcoin Education
- Bitcoin for Families
- Bitcoin for Organizations
- Bitcoin Treasury and Organizational Custody
- Bitcoin Risk Management and Scenario Planning
- Bitcoin Policy and Governance
- Bitcoin and AI Payments
- On-Chain Analytics
- Bitcoin for ... (Communities & Populations)
- Cryptography
- Computer Science Fundamentals
- Online privacy and safety

Note: `Bitcoin for X` is a flexible Advanced category for population- or community-specific modules, such as Bitcoin for women, Bitcoin for Muslims, or other locally relevant communities. These modules should be developed with community input and should avoid treating any group as monolithic.

The Organizations-derived titles were added after reviewing the retiring `../ref/bitcoin-for-organizations/en` pathway. They may later be merged into broader modules if the Advanced pathway needs fewer titles, but they are strong enough to preserve as candidate modules for now.

---

# 5. Follow-On Pathway Ideas

Future follow-on pathways may include:

1. Bitcoin Fundamentals: the redesigned Diploma.
2. Bitcoin Self-Custody: deeper wallet, backup, verification, and safety practice.
3. Lightning Network: deeper payment, routing, liquidity, and trade-off study.
4. Bitcoin Technical Foundations: deeper protocol and system mechanics.
5. Bitcoin Economics: deeper monetary history, policy, incentives, and economic reasoning.

These are pathway ideas, not final product names.

---

# 6. Legacy Migration Notes For Advanced

`../ref/01_bd_202604_contents.csv` and `../input/Bitcoin Diploma - L1 & L2.md` were reviewed as legacy structure proposals and migration sources.

Reading rule:

- `ADVANCED` means old content becomes Advanced pathway material.
- `OUT` does not mean deletion when the same item is marked Custom or Advanced.
- No reviewed section should be treated as out-only deletion without checking whether the content belongs in Custom or Advanced.

Migration summary for Advanced:

| Destination | Legacy content signal | Redesign decision |
|---|---|---|
| Advanced | deeper psychology, detailed mining, mempool, detailed transactions, philosophy, future scenarios | Move into Advanced pathways or educator background. |
| Advanced | L1 UTXOs; L2 detailed monetary history, protocol mechanics, Lightning operation, and high-security custody | Preserve as module seeds; do not return them to the beginner Core. |

Split decisions:

- Psychology of money stays in Core as a foundation; deeper behavioral analysis moves to Advanced.
- Nodes and miners stay in Core only as simple roles; technical mechanics move to Advanced.
- Transaction concepts stay in Core only where needed for safe use and verification; detailed models move to Advanced.
- CBDCs may appear briefly in Block 1 or locally in Block 4; policy and technical depth moves to Advanced.
- Lightning distinctions may be introduced briefly, but wallet setup and payment practice normally belongs in Custom.
- Buying and selling bitcoin may appear in Core as a conceptual risk map, but provider-specific practice belongs in Custom or Advanced.
- Named services, wallets, exchanges, peer-to-peer platforms, and local recommendations should not become global Student Book recommendations.

### L2 Module Seeds

The earlier L2 proposal supplies concise sequences for future module design. These are seeds only; they are not approved module outlines or Advanced outcomes.

| Future module | Suggested sequence recovered from L2 | Boundary |
|---|---|---|
| History of Money (localisation) | Bretton Woods context; 1971 end of dollar-to-gold convertibility; local and global consequences | Keep only the brief historical marker in Core. |
| Mining & Consensus | Transaction relay and validation; candidate-block construction; proof of work; hashes and block headers; difficulty adjustment; block propagation; consensus; optional Merkle trees | Core keeps participant roles and simplified proof of work. |
| Infrastructure & Maintenance | Connect a wallet or application to a Bitcoin node; compare connection and verification trade-offs; troubleshoot supported local connectivity | Core keeps only the beginner roles of nodes and the meaning of verification. |
| Lightning Network | Channel opening and closing; payment channels; HTLCs; routing; liquidity; routing failures; operational trade-offs | Core distinguishes on-chain from Lightning; Custom may support locally appropriate payment practice. |
| Bitcoin Self-Custody | Hot, hardware, and air-gapped signing; passphrases; multisig; encrypted-backup trade-offs; recovery and inheritance planning | Core gives an introductory hardware-wallet and recovery-safety overview. |

---

# 7. What Moves Out Of Core

| Beginner Core keeps | Advanced may develop |
|---|---|
| Money, fiat, inflation, purchasing power | Detailed monetary theory and long policy history |
| Double coincidence of wants, fiat-system roles, fractional reserve banking, bank runs, and brief CBDC orientation | Detailed banking policy, CBDC policy, and long monetary-policy history |
| Bitcoin origin, purpose, properties, finite supply, sats, and beginner timeline | Deep protocol and cryptography detail |
| Overview of users, nodes, miners, and proof of work | Detailed mining mechanics, mempool, transaction lifecycle |
| Wallets, addresses, keys, seed phrases, custody trade-offs, wallet recovery basics, and seed phrase testing | Advanced custody models and operational security |
| Receiving, sending, verification, address checking, beginner safety, scam awareness, and start-small guidance | Advanced troubleshooting and technical analysis |
| Beginner acquiring and exchanging pathways as risk orientation | Named provider recommendations, live exchange setup, deep KYC/no-KYC trade-off analysis, and tax/legal advice |
| High-level distinctions between on-chain and Lightning | Lightning channel mechanics, routing, liquidity, and node operations |
| Local daily-life Bitcoin use as Custom source material | Fixed global requirements for specific local tools, merchants, exchanges, or communities |
| Guided discussion and practical orientation | Full technical demonstration sequences and optional extensions |

---

# 8. Redacted Content Collection

This section preserves material that exists in the legacy Diploma or workspace but is intentionally reduced, compressed, or omitted from `08_student.md`.

## Money Psychology And Economic Behavior

Primary sources:

- `../ref/chapters/1-what-is-money/6-the-psychology-of-money.md`
- `../ref/00_bd_202604-en.md`, section `1.6 The Psychology of Money`
- `02_research.md`, Hackfest repository research on activation energy and concept dependencies

Content to preserve:

- scarcity as a decision-making problem;
- artificial scarcity versus natural scarcity;
- centralized scarcity versus decentralized scarcity;
- time preference;
- opportunity cost;
- delayed gratification;
- survival pressure and short-term decision-making;
- the candy or marshmallow activity;
- discussion prompts about real-life high and low time preference;
- connection between fiat inflation, planning, savings behavior, and time preference.

Possible Advanced modules:

- Monetary Economics
- Money & Society
- Money & Human Rights
- Bitcoin Education

Reason moved out of Core:

Core should introduce scarcity, time preference, and opportunity cost through essential ideas. Deeper behavioral analysis requires more time and more careful facilitation.

## Investment, Risk, Reward, And Capital Allocation

Primary sources:

- `../ref/bitcoin-for-organizations/en/4-impact-on-industry-verticals/2-bitcoin-and-investment-management.md`
- `../ref/bitcoin-for-organizations/en/1-bitcoin-and-risk-management/`
- `../ref/bitcoin-for-organizations/en/5-impact-on-internal-functions/2-what-is-a-bitcoin-treasury.md`

Content to preserve:

- capital allocation as the process of deciding which available uses receive limited capital, including holding liquidity, meeting known obligations, funding productive work, or taking an investment exposure;
- opportunity cost: choosing one use of capital means declining another;
- the difference between a possible reward, an expected return, a promised return, and an actual outcome;
- the relationship between risk and reward: greater possible reward does not guarantee a better outcome, and a lower-volatility or familiar option is not automatically low risk;
- time horizon, liquidity needs, drawdown tolerance, concentration, correlation, counterparty exposure, custody and operational risk as distinct considerations;
- the limits of historical returns, back-tests, correlations, and risk-adjusted-return measures: each describes selected past data and depends on assumptions, periods, and definitions;
- scenario analysis using fictional cases, including the possibility of loss, prolonged drawdowns, inability to sell at the desired time, or an investment failing to meet its purpose;
- the different responsibilities of an individual, a business, a nonprofit, and a professional investment manager when making capital-allocation decisions.

Possible Advanced modules:

- Monetary Economics
- Bitcoin Risk Management and Scenario Planning
- Bitcoin Treasury and Organizational Custody
- Bitcoin for Business

Teaching boundary:

This material should teach decision frameworks, terminology, evidence limits, and trade-offs. It must not recommend Bitcoin, a portfolio weight, a product, a provider, a timing decision, or a personal capital allocation. Use fictional and clearly labelled scenarios rather than learner balances or personal financial details. Learners may evaluate the reasoning and missing information in a scenario; they should not be assessed on choosing an investment or producing a portfolio.

Reason moved out of Core:

Investment and capital-allocation reasoning assumes a longer time horizon, more economic background, and careful treatment of personal and organizational context. It belongs in Advanced study and must remain distinct from financial, legal, tax, accounting, or investment advice.

## Detailed History Of Money

Primary sources:

- `../ref/chapters/2-the-history-of-money/1-from-barter-to-modern-currency.md`
- `../ref/chapters/2-the-history-of-money/2-digital-currency.md`
- `../ref/00_bd_202604-en.md`, chapter `2. The History of Money`

Content to preserve:

- detailed barter scenarios;
- commodity money emergence;
- cattle, shells, wheat, salt, gold, and silver as historical money examples;
- drawbacks of metal coins;
- coin debasement and fraud;
- paper receipts backed by metal;
- Sweden and early fractional reserve examples;
- transition from sound to unsound money;
- industrial revolution, banks, stock markets, and central banks;
- World War I, the 1929 crisis, Bretton Woods, and the Nixon Shock;
- dollar reserve-currency role;
- paper to plastic;
- credit cards, online banking, e-commerce, and digital money.

Possible Advanced modules:

- History of Money (localisation)
- Monetary Economics
- Money & Society

Reason moved out of Core:

Core needs a short history from barter to modern fiat. Detailed chronology, local monetary histories, and policy context belong in follow-on study.

## Fiat System, Banking, Debt, And Policy

Primary sources:

- `../ref/chapters/3-what-is-fiat-money/2-the-fiat-system.md`
- `../ref/chapters/4-how-problems-lead-to-solutions/1-money-buys-less.md`
- `../ref/chapters/4-how-problems-lead-to-solutions/1-the-global-debt-burden-and-social-inequality.md`
- `../ref/00_bd_202604-en.md`, chapters `3` and `4`

Content to preserve:

- legal tender law;
- fiat money by decree;
- fiat money pros and cons;
- commodity-backed systems;
- debt-driven money creation;
- fractional-reserve banking as a featured case study: bank balance sheets, deposit liabilities, loans and other assets, liquidity, solvency, credit creation, and bank-run dynamics;
- the distinction between reserve requirements, capital requirements, liquidity requirements, and the other legal, economic, and risk constraints on bank lending;
- the Cantillon effect: when new money or credit enters an economy through particular recipients, those recipients may be able to spend it before prices and wages have fully adjusted; later recipients may face changed prices first;
- how the distribution channel, timing, contracts, market conditions, and credit demand can affect who experiences those changes and when;
- commercial-bank revenue models;
- reserve requirements;
- central banks as lender of last resort;
- bailouts, moral hazard, and "too big to fail";
- boom-and-bust cycle;
- government debt and bond issuance;
- wealthy individuals and asset ownership under inflation;
- commercial banks and financial-sector incentives;
- central banks, interest rates, monetary policy, and fiscal policy;
- target rates, expansionary fiscal policy, contractionary fiscal policy;
- exchange-rate policy, supply shocks, and price controls;
- detailed purchasing-power examples;
- productivity versus wages;
- global debt spiral;
- inflation, consumerism, social unrest, economic mobility, and wealth concentration;
- country-specific or local history prompts.

Possible Advanced modules:

- Monetary Economics
- Money & Society
- Money & Human Rights
- History of Money (localisation)

### Cantillon Effect Teaching Note

The Cantillon effect is a framework for examining the distributional effects of money and credit creation. It asks who receives new money or credit first, what they can buy or finance before prices adjust, and how later price, wage, and asset changes affect other people. It does not mean that every price increase has one cause or that the effects are identical in every case. Advanced learners should compare specific, sourced scenarios and distinguish the timing and distribution of new money or credit from broader causes of inflation and changes in relative prices.

### Fractional-Reserve Banking Teaching Note

Fractional-reserve banking should be a featured Monetary Economics strand, not a passing definition. Use simplified bank balance sheets to show that deposits are liabilities of a bank, while loans and other investments are assets. A bank can be solvent yet face a liquidity problem if it cannot meet withdrawals when due; it can also be insolvent when its assets are worth less than its liabilities. Learners should examine how lending, repayment, withdrawals, losses, capital, liquidity, and confidence interact in fictional scenarios.

Avoid presenting one reserve ratio as a universal explanation of money creation. Rules and practices differ by jurisdiction and time, and lending is also constrained by capital, liquidity, regulation, borrower creditworthiness, funding, and demand for credit. Use current, locally relevant banking rules only when they are verified, dated, and appropriately sourced.

Reason moved out of Core:

Core should give a plain-language account of fiat-system problems. Advanced modules can examine policy, institutions, debt dynamics, and social consequences with more precision and context.

Fact-check notes:

- Any statistics about debt, purchasing power, productivity, wages, inflation, country policy, or global finance must be verified and dated before publication.
- Some old examples use United States data and should be localized or clearly framed as examples.

## CBDCs And Digital Fiat

Primary sources:

- `../ref/chapters/3-what-is-fiat-money/3-central-bank-digital-currencies.md`
- `../ref/chapters/10-what-future-can-bitcoin-build/1-what-are-central-bank-digital-currencies-cbdcs.md`
- `../ref/00_bd_202604-en.md`, sections `3.3` and `10.1`
- `08_student.md`, section `CBDCs as a beginner fiat-system example where appropriate`

Content to preserve:

- CBDCs as digital fiat issued or controlled by central banks;
- difference between digital fiat, bank deposits, physical cash, and CBDCs;
- institutional versus retail CBDC designs;
- programmable money concerns;
- transaction monitoring;
- transaction blocking or freezing;
- account or identity linkage;
- monetary policy and fiat supply;
- local CBDC status research;
- CBDC versus Bitcoin comparison;
- human-rights and civil-liberties implications.

Possible Advanced modules:

- Money & Human Rights
- Monetary Economics
- Money & Society
- Privacy & Security

Reason moved out of Core:

Core may use CBDCs briefly as a fiat-system example. Detailed CBDC policy, surveillance, programmability, and country-specific status belong in Advanced or local Custom material.

Fact-check notes:

- CBDC country counts, GDP percentages, and country-status claims change often. Verify, date, and cite them before any public use.
- Do not imply all CBDC designs are identical.

## Cypherpunks, Digital Cash, And Decentralized Systems

Primary sources:

- `../ref/chapters/4-how-problems-lead-to-solutions/3-the-quest-for-a-decentralized-currency.md`
- `../ref/chapters/2-the-history-of-money/2-digital-currency.md`
- `../ref/00_bd_202604-en.md`, sections `2.2` and `4.3`
- `08_student.md`, Block 2 sections on Cypherpunk context and early digital-money attempts

Content to preserve:

- personal computers and the internet as social turning points;
- privacy, surveillance, and control in digital systems;
- Cypherpunk movement;
- Eric Hughes, Timothy C. May, John Gilmore, Hal Finney, Phil Zimmermann, and PGP;
- `A Cypherpunk Manifesto`;
- cryptography as a tool for privacy and freedom;
- centralized versus decentralized system comparison;
- central points of failure;
- censorship and restriction;
- autonomy, transparency, resilience, privacy, and permissionless participation;
- Tor as an example of a decentralized communication network;
- David Chaum and DigiCash;
- Hashcash, Bit Gold, and other digital-money attempts;
- the unsolved decentralized digital-currency problem before Bitcoin.

Possible Advanced modules:

- History of Bitcoin
- Communication Networks
- Online privacy and safety
- Nostr & Decentralized Communication
- Cryptography

Reason moved out of Core:

Core should introduce the search for decentralized digital money without overloading beginners with a long technical or historical timeline.

## Bitcoin Consensus, Network Roles, And Open Development

Primary sources:

- `../ref/chapters/5-what-is-bitcoin/1-how-does-bitcoin-work.md`
- `../ref/chapters/9-how-does-bitcoin-mining-work/1-bitcoin-nodes-and-miners.md`
- `../ref/00_bd_202604-en.md`, sections `5.1`, `9.1`
- `02_research.md`, Hackfest repository research
- `08_student.md`, Block 2 sections on users, nodes, miners, and proof of work

Content to preserve:

- Nakamoto Consensus;
- consensus as agreement on shared rules;
- board-game rule analogy;
- 21 million limit as a consensus rule;
- miners, nodes, users, developers, and projects as network participants;
- developers and open-source contribution;
- Bitcoin software review and protocol change process;
- Byzantine Generals Problem as educator background;
- consensus activity;
- decentralized coordination without a defined leader;
- relationship between nodes, miners, proof of work, and rule enforcement;
- how new nodes sync and verify;
- why running a node reduces trust.

A merchant, exchange, or other economically active user that verifies payments with a node is sometimes called an **economic node**. Its influence comes from the economic activity it accepts, not from authority over other participants. Running a node also requires storage, bandwidth, maintenance, and technical attention.

Possible Advanced modules:

- Mining & Consensus
- Infrastructure & Maintenance
- Open Source Software
- Bitcoin Education
- Computer Science Fundamentals

Reason moved out of Core:

Core should explain roles simply. Exact consensus mechanics and open-source governance need more time and stronger prerequisites.

## Cryptography

Primary sources:

- `../ref/chapters/8-how-bitcoin-works/1-security-through-cryptography.md`
- `../ref/00_bd_202604-en.md`, section `8.1`
- `02_research.md`, Hackfest repository research on hashing and proof of work

Content to preserve:

- cryptography definition;
- encryption and decryption;
- shared-secret cryptography versus public-key cryptography;
- public keys and private keys;
- digital signatures;
- transaction authorization;
- functions, one-way functions, and hash functions;
- SHA-256 and RIPEMD-160;
- hashes as fixed-length fingerprints;
- deterministic outputs;
- pre-image resistance;
- avalanche effect;
- collision resistance;
- fast verification;
- address creation through hashing public keys;
- SHA-256 activity;
- demo-before-abstraction teaching method.

Possible Advanced modules:

- Cryptography
- Computer Science Fundamentals
- Transactions & Settlement
- Privacy & Security

Reason moved out of Core:

Core needs a practical introduction to keys and signatures. Cryptographic properties, hash functions, and address-generation detail are Advanced technical foundations.

Activity seeds:

- Generate a SHA-256 hash from different inputs.
- Show how a tiny input change changes the hash.
- Connect hashing to block integrity and proof of work.

## UTXOs And Transaction Structure

Primary sources:

- `../ref/chapters/8-how-bitcoin-works/2-the-utxo-model.md`
- `../ref/chapters/9-how-does-bitcoin-mining-work/3-how-transactions-work.md`
- `../ref/chapters/6-how-to-use-bitcoin/4-receiving-and-sending-transactions.md`
- `../ref/00_bd_202604-en.md`, sections `6.4`, `8.2`, `9.3`
- `08_student.md`, Block 3 transaction and verification sections

Content to preserve:

- UTXOs as pieces of bitcoin rather than account balances;
- wallet balance as sum of controlled UTXOs;
- transaction inputs and outputs;
- change outputs;
- transaction fees;
- spent and unspent outputs;
- transaction signing;
- broadcast to peer-to-peer network;
- node validation;
- mempool entry;
- miner block selection;
- confirmations;
- transaction finality;
- privacy risk from revealing UTXOs;
- comparison between property transfer and cash transfer;
- transaction roles: sender, recipient, miners, node operators.

Possible Advanced modules:

- Transactions & Settlement
- Privacy & Security
- Computer Science Fundamentals
- Infrastructure & Maintenance

Reason moved out of Core:

Core should teach only the transaction knowledge needed for safe beginner use. UTXO mechanics, fee strategy, privacy analysis, and full transaction lifecycle belong in Advanced.

## Mining, Difficulty, Issuance, And Fees

Primary sources:

- `../ref/chapters/9-how-does-bitcoin-mining-work/0-introduction.md`
- `../ref/chapters/9-how-does-bitcoin-mining-work/1-bitcoin-nodes-and-miners.md`
- `../ref/chapters/9-how-does-bitcoin-mining-work/2-what-is-the-mempool.md`
- `../ref/chapters/9-how-does-bitcoin-mining-work/3-how-transactions-work.md`
- `../ref/00_bd_202604-en.md`, chapter `9`
- `02_research.md`, Hackfest repository research on block pace, halving, and mining demonstrations

Content to preserve:

- miners collecting transactions into candidate blocks;
- block reward and transaction fees;
- supply schedule;
- halving every 210,000 blocks;
- approximate four-year halving rhythm;
- issuance declining toward the 21 million cap;
- 2140 as approximate final issuance horizon;
- valid block hashes;
- previous-block hashes linking blocks;
- difficulty target;
- mining as repeated hashing;
- proof of work as costly work that is easy to verify;
- block-header fields as the compact data miners repeatedly hash;
- difficulty adjustment every 2,016 blocks;
- 10-minute average block interval;
- competing blocks and discarded alternatives;
- block propagation and how independently validating nodes relay valid blocks;
- Merkle trees as an optional data-structure extension for connecting transactions to a block;
- miner incentives;
- transaction-fee market;
- future fee-revenue importance;
- hash rate, pools, mining map, and block-space visualization as possible demonstrations.

Possible Advanced modules:

- Mining & Consensus
- Energy & Mining
- Transactions & Settlement
- Infrastructure & Maintenance
- Computer Science Fundamentals

Reason moved out of Core:

Core needs a foundational explanation of proof of work. Detailed mining mechanics, issuance math, fee markets, and difficulty adjustment belong in Advanced.

Fact-check notes:

- Halving tables, mined-supply percentages, hashrate, mining distribution, fee rates, and energy examples must be verified and dated before publication.

## Mempool And Block Explorers

Primary sources:

- `../ref/chapters/9-how-does-bitcoin-mining-work/2-what-is-the-mempool.md`
- `../ref/chapters/6-how-to-use-bitcoin/5-don-t-trust-verify.md`
- `08_student.md`, section `Verification, block explorers, and irreversible transactions`
- `02_research.md`, Hackfest repository research

Content to preserve:

- mempool as each node's set of unconfirmed transactions;
- no single universal mempool;
- transaction broadcast and waiting;
- node validation before mempool acceptance;
- miner selection from mempool;
- fee-rate observation;
- mempool.space as one visual block explorer, not the protocol itself;
- block explorers as helpful but privacy-relevant interfaces;
- live network observation;
- low-connectivity alternatives for demonstrations.

Possible Advanced modules:

- Transactions & Settlement
- Mining & Consensus
- Infrastructure & Maintenance
- Privacy & Security

Reason moved out of Core:

Core may include simple block explorer orientation. Detailed mempool analysis and fee market behavior are Advanced.

## Wallets, Custody, Recovery, And Operational Security

Primary sources:

- `../ref/chapters/6-how-to-use-bitcoin/2-introduction-to-wallets.md`
- `../ref/chapters/6-how-to-use-bitcoin/3-setting-up-a-mobile-wallet.md`
- `../ref/chapters/6-how-to-use-bitcoin/4-receiving-and-sending-transactions.md`
- `../ref/chapters/6-how-to-use-bitcoin/5-don-t-trust-verify.md`
- `08_student.md`, Block 3 self-custody sections

Content to preserve:

- wallet as key management plus interface;
- master private key and public addresses;
- self-custodial versus custodial wallets;
- installation-flow differences between custodial and self-custodial wallets;
- online, mobile, desktop, and hardware wallets;
- hot versus cold storage;
- wallet choice criteria: security, privacy, ease of use, compatibility, fees, reputation, control;
- open-source versus closed-source wallet software;
- mobile wallet setup;
- recovery phrase backup;
- recovery phrase confirmation;
- wallet restoration from seed phrase;
- receiving via address, link, or QR code;
- sending and double-checking;
- confirmation waiting;
- "not your keys, not your coins";
- "do not trust, verify";
- threat models for large balances;
- hardware wallet security models;
- Bitcoin-only firmware;
- airgapped signing;
- passphrases and the added recovery risk they create;
- multisig, encrypted-backup trade-offs, and inheritance as future possible additions.

Possible Advanced modules:

- Privacy & Security
- Bitcoin Self-Custody
- Infrastructure & Maintenance
- Online privacy and safety

Reason moved out of Core:

Core gives beginner orientation and safety rules. Advanced modules can teach operational security, troubleshooting, deeper wallet selection, and high-stakes custody practices.

Safety notes:

- Do not use real learner seed phrases in public demonstrations.
- Do not normalize moving meaningful funds during class.
- Any live wallet practice should be low-stakes, locally prepared, and educator-supervised.

## Acquiring, Exchanging, KYC, And No-KYC Trade-Offs

Primary sources:

- `../ref/chapters/6-how-to-use-bitcoin/1-acquiring-bitcoin.md`
- `08_student.md`, sections on acquiring/exchanging and local on-ramp/off-ramp pathways

Content to preserve:

- earning bitcoin;
- mining bitcoin as acquisition;
- in-person peer-to-peer exchange;
- online peer-to-peer platforms;
- escrow concepts;
- centralized exchanges and brokers;
- identity verification;
- withdrawal risk;
- custodian risk;
- misappropriation and proof-of-reserves concerns;
- fraud and physical safety;
- liquidity, fees, spread, jurisdiction, tax, and record-keeping;
- local on-ramp and off-ramp mapping.

Possible Advanced modules:

- Payments & Exchange
- Privacy & Security
- Bitcoin for Business
- Money & Human Rights

Reason moved out of Core:

Core should teach acquisition pathways as risk awareness, not as instructions or provider recommendations. Specific providers, KYC/no-KYC practice, and legal/tax considerations require local expertise.

Safety and publication notes:

- Do not publish named provider recommendations globally unless explicitly approved.
- Legal, tax, and regulatory claims require current local review.

## Lightning Network And Second-Layer Payments

Primary sources:

- `../ref/chapters/7-using-bitcoin-in-daily-life/0-introduction.md`
- `../ref/chapters/7-using-bitcoin-in-daily-life/1-the-lightning-network.md`
- `../ref/chapters/7-using-bitcoin-in-daily-life/2-types-of-lightning-wallets.md`
- `../ref/chapters/7-using-bitcoin-in-daily-life/3-setting-up-a-bitcoin-lightning-wallet.md`
- `../ref/chapters/7-using-bitcoin-in-daily-life/4-sending-and-receiving-lightning-transactions.md`
- `08_student.md`, Block 3 Lightning distinction and Block 4 Lightning sections

Content to preserve:

- Lightning as a payment network built on top of Bitcoin;
- payment channels;
- channel opening and closing;
- hash time-locked contracts (HTLCs) as the conditional-payment mechanism behind many Lightning payment paths;
- shared-wallet or tab analogy;
- off-chain payments;
- settlement back to the blockchain;
- routing through other participants;
- direct and indirect payment paths;
- on-chain versus Lightning comparison;
- Lightning invoices;
- Lightning addresses;
- custodial and self-custodial Lightning wallets;
- open-source versus closed-source Lightning wallets;
- moving funds from on-chain to Lightning;
- routing failures;
- liquidity constraints;
- Lightning node operators and routing fees;
- Lightning network map;
- Lightning relay activity;
- current capacity or throughput claims as fact-check-only material.

Possible Advanced modules:

- Lightning Network
- Payments & Exchange
- Infrastructure & Maintenance
- Privacy & Security
- Bitcoin for Business

Reason moved out of Core:

Core should distinguish on-chain and Lightning at a high-level overview. Detailed Lightning setup, channel management, routing, liquidity, and node operation belong in Custom or Advanced.

Fact-check notes:

- Lightning capacity, node count, channel count, speed claims, fee claims, and Visa comparisons must be verified, dated, cited, or rewritten as evergreen explanations.

## Merchant Tools, BTCPay Server, And Business Use

Primary sources:

- `../ref/chapters/7-using-bitcoin-in-daily-life/5-buying-coffee-and-groceries-with-bitcoin.md`
- `08_student.md`, Block 4 merchant and community use-case sections

Content to preserve:

- payment processing flow for card payments;
- merchant fees and intermediaries;
- merchant benefits and risks of direct Bitcoin payments;
- BTCPay Server;
- self-hosted payment processing;
- non-custodial invoice generation;
- xpub-based invoice generation;
- in-person wallet acceptance;
- staff training;
- receipts and refunds;
- accounting and tax context;
- device security;
- conversion policy;
- vouchers, gift cards, and payment cards as transitional tools;
- BTCMap or equivalent merchant discovery.

Possible Advanced modules:

- Bitcoin for Business
- Payments & Exchange
- Infrastructure & Maintenance
- Communities & Circular Economies

Reason moved out of Core:

Core may discuss local use cases. Business implementation, payment processors, accounting, staff process, and named tools require separate workshops and local expertise.

Fact-check notes:

- Card-fee examples, provider claims, URLs, plugin details, tax treatment, and merchant-tool features must be verified before publication.

## Circular Economies And Communities

Primary sources:

- `../ref/chapters/7-using-bitcoin-in-daily-life/5-buying-coffee-and-groceries-with-bitcoin.md`
- `../ref/chapters/11-back-matter/1-real-world-case-studies.md`
- `08_student.md`, Block 4 circular economy, local resource map, and community discovery sections
- `public/MFB-BD-Keynote.md`, public redesign explanation

Content to preserve:

- circular economy definition;
- local earning, spending, saving, receiving, and exchange loops;
- merchant discovery;
- BTCMap community and merchant listings;
- Bitcoin Beach and Arnhem as historical examples;
- local education and technical support;
- voluntary participation;
- adoption quality versus adoption numbers;
- community custody risk;
- case studies from Indonesia and The Core;
- local resource maps;
- community problem-solving workshops.

Possible Advanced modules:

- Communities & Circular Economies
- Bitcoin Education
- Bitcoin for Organizations
- Bitcoin for Families
- Bitcoin for ... (Communities & Populations)

Reason moved out of Core:

Block 4 can introduce local practice. Deeper community development, governance, support, and sustainability belong in separate modules or local programs.

## Philosophy, Human Rights, And Future Scenarios

Primary sources:

- `../ref/chapters/10-what-future-can-bitcoin-build/0-introduction.md`
- `../ref/chapters/10-what-future-can-bitcoin-build/2-the-philosophy-of-bitcoin.md`
- `../ref/chapters/10-what-future-can-bitcoin-build/3-the-benefits-of-bitcoin.md`
- `../ref/chapters/10-what-future-can-bitcoin-build/4-an-empowered-future.md`
- `../ref/00_bd_202604-en.md`, chapter `10`

Content to preserve:

- self-sovereignty;
- financial independence;
- critical thinking;
- self-determination;
- control over money as a rights question;
- censorship resistance;
- node running as rule verification;
- fixed supply and social incentives;
- hyperbitcoinization as a hypothetical future scenario;
- store-of-value claims;
- monetary policy implications;
- transparency and traceability;
- remittances;
- abundant energy and mining;
- final reflection on how learner views changed;
- "what is my next step?" prompts.

Possible Advanced modules:

- Philosophy of Bitcoin
- Money & Human Rights
- Money & Society
- Energy & Mining
- Bitcoin Education

Reason moved out of Core:

Core should help learners reason independently without overloading them with broad future claims. Philosophy and future scenarios need careful claim/evidence/reasoning structure.

Fact-check and tone notes:

- Treat future scenarios as possibilities, not promises.
- Avoid unsupported guarantees about price, adoption, social outcomes, or political effects.

## Open Source Software And Contribution

Primary sources:

- `../ref/chapters/5-what-is-bitcoin/1-how-does-bitcoin-work.md`
- `../ref/chapters/6-how-to-use-bitcoin/2-introduction-to-wallets.md`
- `../ref/chapters/6-how-to-use-bitcoin/5-don-t-trust-verify.md`
- `../ref/chapters/7-using-bitcoin-in-daily-life/5-buying-coffee-and-groceries-with-bitcoin.md`
- `08_student.md`, references to open-source wallets and open-source education

Content to preserve:

- Bitcoin as open-source software;
- inspectability and review;
- open-source wallet preference;
- community review as a form of verification;
- BTCPay Server as an open-source payment processor;
- protocol contribution;
- project contribution beyond code;
- maintainers, reviewers, educators, translators, designers, and local contributors.

Possible Advanced modules:

- Open Source Software
- Bitcoin Education
- Infrastructure & Maintenance
- Bitcoin for Organizations

Reason moved out of Core:

Core can mention open-source preference. Contribution pathways, software review, maintainership, and project governance require separate treatment.

## Communication Networks, Nostr, And Online Privacy

Primary sources:

- `../ref/chapters/4-how-problems-lead-to-solutions/3-the-quest-for-a-decentralized-currency.md`
- `02_research.md`, Hackfest repository research
- Candidate title list in this file, originally moved from `06_plan.md`

Content to preserve:

- internet freedom versus internet surveillance;
- encryption for communication;
- Tor as a decentralized communication example;
- Nostr as a future decentralized communication module;
- online privacy and safety;
- identity, metadata, and account-control risks;
- relationship between money, speech, and communication infrastructure.

Possible Advanced modules:

- Nostr & Decentralized Communication
- Communication Networks
- Online privacy and safety
- Privacy & Security
- Money & Human Rights

Reason moved out of Core:

The beginner Diploma should stay focused on money and Bitcoin. Decentralized communication networks are important adjacent topics but should not expand the beginner scope.

---

# 9. Candidate Module Seed Catalog

This section sketches possible directions for the candidate modules. These are seeds, not final scopes.

| Candidate module | Possible focus | Parked source material |
|---|---|---|
| History of Money (localisation) | Local money histories, commodity money, coinage, paper receipts, gold standard, Bretton Woods, Nixon Shock, modern digital money | Legacy chapters 2 and 3; local educator input |
| Monetary Economics | Scarcity, time preference, opportunity cost, inflation, purchasing power, fractional-reserve banking, liquidity and solvency, debt, policy tools, the Cantillon effect, and risk/reward and capital-allocation reasoning | Legacy chapters 1.6, 3.2, 4.1, 4.2; Organizations investment-management material |
| History of Bitcoin | Cypherpunks, digital cash attempts, Satoshi, whitepaper, Genesis Block, early transactions, Pizza Day | Legacy chapters 4.3, 5.0, 5.1 |
| Philosophy of Bitcoin | Self-sovereignty, autonomy, critical thinking, rule verification, rights, future scenarios | Legacy chapter 10 |
| Transactions & Settlement | UTXOs, inputs, outputs, change, signatures, broadcast, mempool, confirmations, settlement finality | Legacy chapters 6.4, 8.2, 9.2, 9.3 |
| Mining & Consensus | Nakamoto Consensus, proof of work, nodes, miners, block templates, valid hashes, difficulty, halvings | Legacy chapters 5.1 and 9 |
| Privacy & Security | Threat models, UTXO privacy, block explorer privacy, KYC trade-offs, wallet security, scams, online safety | Legacy chapters 6, 8, 9; `08_student.md` safety sections |
| Payments & Exchange | P2P exchange, centralized exchanges, escrow, on/off ramps, Lightning payments, gift cards, merchant payments | Legacy chapters 6.1 and 7 |
| Bitcoin for Business | Merchant workflows, BTCPay Server, receipts, refunds, accounting, staff training, payment operations | Legacy chapter 7.5; Block 4 draft |
| Infrastructure & Maintenance | Running nodes, wallet infrastructure, explorers, BTCPay, Lightning nodes, maintenance habits | Legacy chapters 7, 8, 9 |
| Communities & Circular Economies | Local resource maps, merchant discovery, circular-economy design, education support, community case studies | Legacy chapter 7.5 and case studies |
| Money & Society | Fiat social effects, wealth concentration, consumerism, debt culture, savings, planning, trust | Legacy chapters 3.2, 4.2, 10 |
| Money & Human Rights | Financial censorship, CBDCs, privacy, access, self-sovereignty, remittances, rights framing | Legacy chapter 10.1, 10.2 |
| Energy & Mining | Mining energy use, surplus energy, grid interaction, incentives, energy claims, public debate | Legacy chapter 10.3; mining chapter |
| Open Source Software | Bitcoin Core, wallet code, BTCPay, contribution models, review, licenses, community development | Legacy chapters 5.1, 6.2, 7.5 |
| Nostr & Decentralized Communication | Decentralized communication, relays, identity, censorship resistance, social publishing | Candidate title; Cypherpunk material |
| Communication Networks | Internet, Tor, encryption, peer-to-peer networks, censorship resistance, network resilience | Legacy chapter 4.3 |
| Bitcoin Education | How to teach Bitcoin, concept maps, prerequisite chains, demo-before-abstraction, activity design | `02_research.md`, `10_activities.md`, `12_educator-draft.md` |
| Bitcoin for Families | Family custody conversations, inheritance basics, safety culture, youth education, shared decision-making | Candidate title; custody and safety material |
| Bitcoin for Organizations | Treasury policy, custody roles, governance, payments, donations, accounting, staff training | Candidate title; business and custody material |
| Bitcoin Treasury and Organizational Custody | Treasury policy, balance-sheet exposure, custody roles, approval workflows, controls, accounting boundaries, institutional risk | `../ref/bitcoin-for-organizations/en/5-impact-on-internal-functions/2-what-is-a-bitcoin-treasury.md`; `../ref/bitcoin-for-organizations/en/4-impact-on-industry-verticals/2-bitcoin-and-investment-management.md` |
| Bitcoin Risk Management and Scenario Planning | Risk registers, likelihood, magnitude, time horizon, mitigations, strategic scenarios, organizational decision-making | `../ref/bitcoin-for-organizations/en/1-bitcoin-and-risk-management/` |
| Bitcoin Policy and Governance | CBDCs, government bans, self-custody restrictions, law versus protocol, organizational governance, public-sector implications | `../ref/bitcoin-for-organizations/en/4-impact-on-industry-verticals/6-government.md`; `../ref/bitcoin-for-organizations/en/2-dispelling-misconceptions/5-will-governments-ban-bitcoin.md`; `../ref/bitcoin-for-organizations/en/2-dispelling-misconceptions/9-will-a-cbdc-render-bitcoin-obsolete.md` |
| Bitcoin and AI Payments | AI agents, machine payments, L402-style payment flows, Lightning-enabled APIs, automated service purchasing | `../ref/bitcoin-for-organizations/en/7-bitcoin-s-possible-future/4-the-convergence-of-bitcoin-and-ai.md`; `../ref/bitcoin-for-organizations/en/5-impact-on-internal-functions/1-bitcoin-s-impact-on-it-leaders.md` |
| On-Chain Analytics | Open-ledger inspection, block explorer literacy, transaction graphs, public metrics, Pizza Day transaction analysis, privacy limits | `../ref/bitcoin-for-organizations/en/8-the-bitcoin-economy/` |
| Bitcoin for ... | Community-specific modules co-designed with the relevant community | Candidate title; local Custom experience |
| Cryptography | Public/private keys, digital signatures, hashing, SHA-256, one-way functions, address hashing | Legacy chapter 8.1 |
| Computer Science Fundamentals | Functions, hashes, networks, databases, peer-to-peer systems, block structure, verification | Legacy chapters 8 and 9; Hackfest research |
| Online privacy and safety | Device hygiene, metadata, scams, identity exposure, communication privacy, wallet privacy | Safety sections; Cypherpunk material |

---

# 10. Advanced Activity And Demonstration Seeds

These activities may become Advanced modules, educator background, or optional workshops.

| Activity seed | Possible module | Source |
|---|---|---|
| Time preference activity | Monetary Economics | Legacy chapter 1.6 |
| Fractional-reserve banking balance-sheet simulation | Monetary Economics | Use a fictional bank to distinguish deposits, loans, reserves or liquid assets, capital, liquidity pressure, and insolvency. Change one condition at a time and ask learners to explain the consequence; do not use it to make claims about a real bank. |
| Fictional capital-allocation scenario | Monetary Economics | Compare liquidity, time horizon, opportunity cost, possible reward, and market, custody, concentration, and operational risks without selecting or recommending an allocation. |
| Claim / evidence / reasoning on fiat problems | Money & Society | `10_activities.md` |
| Cypherpunk timeline | History of Bitcoin | Legacy chapter 4.3 |
| Consensus activity | Mining & Consensus | Legacy chapter 5.1 |
| Wallet evaluation exercise | Privacy & Security | Legacy chapter 6.2 |
| Wallet setup and recovery lab | Bitcoin Self-Custody | Legacy chapter 6.3 |
| Transactions in action | Transactions & Settlement | Legacy chapter 6.4 |
| SHA-256 hashing demo | Cryptography | Legacy chapter 8.1 |
| UTXO change-output exercise | Transactions & Settlement | Legacy chapter 8.2 |
| Mempool observation | Transactions & Settlement | Legacy chapter 9.2 |
| Block-time and halving demonstration | Mining & Consensus | `02_research.md` Hackfest notes |
| Lightning relay race | Lightning Network | Legacy chapter 7.4 |
| Merchant payment workflow | Bitcoin for Business | Legacy chapter 7.5 |
| Circular economy map | Communities & Circular Economies | Legacy chapter 7.5 and `08_student.md` |
| CBDC comparison workshop | Money & Human Rights | Legacy chapters 3.3 and 10.1 |
| Final reflection on changed perspective | Philosophy of Bitcoin | Legacy chapter 10.4 |
| Concept-map completion | Bitcoin Education | `02_research.md` Hackfest notes |
| Misconception clinic | Bitcoin Education | `../ref/bitcoin-for-organizations/en/2-dispelling-misconceptions/` |
| Organizational risk register | Bitcoin Risk Management and Scenario Planning | `../ref/bitcoin-for-organizations/en/1-bitcoin-and-risk-management/` |
| Settlement comparison: card, on-chain, Lightning | Transactions & Settlement; Payments & Exchange | `../ref/bitcoin-for-organizations/en/4-impact-on-industry-verticals/3-banking-and-payments.md` |
| Treasury policy role-play | Bitcoin Treasury and Organizational Custody | `../ref/bitcoin-for-organizations/en/5-impact-on-internal-functions/2-what-is-a-bitcoin-treasury.md` |
| Energy claim audit | Energy & Mining | `../ref/bitcoin-for-organizations/en/2-dispelling-misconceptions/2-bitcoin-is-bad-for-the-environment.md`; `../ref/bitcoin-for-organizations/en/4-impact-on-industry-verticals/1-bitcoin-and-energy.md` |
| Open-ledger investigation | On-Chain Analytics | `../ref/bitcoin-for-organizations/en/8-the-bitcoin-economy/` |

Every future activity should include:

- objective;
- prerequisites;
- materials;
- low-tech alternative;
- safety notes;
- current-data fact-check notes;
- local expert notes where relevant;
- evidence of learning;
- adaptation notes.

---

# 11. Source Trail

Use these source files when future Advanced module work begins.

## Active Workspace Sources

- `00_index.md`: active workspace map.
- `01_review.md`: diagnosis that the old Diploma mixed beginner and advanced material.
- `02_research.md`: evidence needs, Hackfest technical teaching notes, concept-map ideas.
- `03_scope.md`: Advanced pathway workstream and out-of-scope timing.
- `04_design.md`: simple-over-technical principle and Core / Custom / Advanced separation.
- `05_objectives.md`: Advanced outcomes boundary.
- `06_plan.md`: active beginner architecture and legacy migration rules.
- `08_student.md`: current beginner draft; useful for identifying what has been compressed or removed.
- `10_activities.md`: activity template and activity categories.
- `12_educator-draft.md`: educator guidance on moving complex side topics to Advanced.
- `17_spec.md`: publication rules, fact-check rules, QR rules, and public communication rules.

## Legacy Reference Sources

- `../ref/00_bd_202604-en.md`: full prior English Diploma source.
- `../ref/01_bd_202604_contents.csv`: old table of contents.
- `../ref/01_bd_202604_contents.md`: old table of contents in Markdown.
- `../ref/02_bd_202604_educator_guide.md`: legacy educator guide.
- `../ref/chapters/1-what-is-money/6-the-psychology-of-money.md`
- `../ref/chapters/2-the-history-of-money/1-from-barter-to-modern-currency.md`
- `../ref/chapters/2-the-history-of-money/2-digital-currency.md`
- `../ref/chapters/3-what-is-fiat-money/1-brief-history-of-fiat-money.md`
- `../ref/chapters/3-what-is-fiat-money/2-the-fiat-system.md`
- `../ref/chapters/3-what-is-fiat-money/3-central-bank-digital-currencies.md`
- `../ref/chapters/4-how-problems-lead-to-solutions/0-introduction.md`
- `../ref/chapters/4-how-problems-lead-to-solutions/1-money-buys-less.md`
- `../ref/chapters/4-how-problems-lead-to-solutions/1-the-global-debt-burden-and-social-inequality.md`
- `../ref/chapters/4-how-problems-lead-to-solutions/3-the-quest-for-a-decentralized-currency.md`
- `../ref/chapters/5-what-is-bitcoin/0-the-creation-of-bitcoin.md`
- `../ref/chapters/5-what-is-bitcoin/1-how-does-bitcoin-work.md`
- `../ref/chapters/5-what-is-bitcoin/2-bitcoin-as-sound-digital-money.md`
- `../ref/chapters/6-how-to-use-bitcoin/1-acquiring-bitcoin.md`
- `../ref/chapters/6-how-to-use-bitcoin/2-introduction-to-wallets.md`
- `../ref/chapters/6-how-to-use-bitcoin/3-setting-up-a-mobile-wallet.md`
- `../ref/chapters/6-how-to-use-bitcoin/4-receiving-and-sending-transactions.md`
- `../ref/chapters/6-how-to-use-bitcoin/5-don-t-trust-verify.md`
- `../ref/chapters/7-using-bitcoin-in-daily-life/0-introduction.md`
- `../ref/chapters/7-using-bitcoin-in-daily-life/1-the-lightning-network.md`
- `../ref/chapters/7-using-bitcoin-in-daily-life/2-types-of-lightning-wallets.md`
- `../ref/chapters/7-using-bitcoin-in-daily-life/3-setting-up-a-bitcoin-lightning-wallet.md`
- `../ref/chapters/7-using-bitcoin-in-daily-life/4-sending-and-receiving-lightning-transactions.md`
- `../ref/chapters/7-using-bitcoin-in-daily-life/5-buying-coffee-and-groceries-with-bitcoin.md`
- `../ref/chapters/8-how-bitcoin-works/0-introduction.md`
- `../ref/chapters/8-how-bitcoin-works/1-security-through-cryptography.md`
- `../ref/chapters/8-how-bitcoin-works/2-the-utxo-model.md`
- `../ref/chapters/9-how-does-bitcoin-mining-work/0-introduction.md`
- `../ref/chapters/9-how-does-bitcoin-mining-work/1-bitcoin-nodes-and-miners.md`
- `../ref/chapters/9-how-does-bitcoin-mining-work/2-what-is-the-mempool.md`
- `../ref/chapters/9-how-does-bitcoin-mining-work/3-how-transactions-work.md`
- `../ref/chapters/10-what-future-can-bitcoin-build/0-introduction.md`
- `../ref/chapters/10-what-future-can-bitcoin-build/1-what-are-central-bank-digital-currencies-cbdcs.md`
- `../ref/chapters/10-what-future-can-bitcoin-build/2-the-philosophy-of-bitcoin.md`
- `../ref/chapters/10-what-future-can-bitcoin-build/3-the-benefits-of-bitcoin.md`
- `../ref/chapters/10-what-future-can-bitcoin-build/4-an-empowered-future.md`
- `../ref/chapters/11-back-matter/1-real-world-case-studies.md`
- `../ref/chapters/11-back-matter/2-additional-resources.md`
- `../ref/chapters/11-back-matter/3-key-concepts.md`
- `../ref/chapters/11-back-matter/4-glossary.md`

## Retiring Organizations Reference Sources

Bitcoin for Organizations is being cannibalized by the redesigned Diploma and Advanced pathway. The old Organizations path should not continue as a standalone course after the redesign, but its strongest material should be preserved here as Advanced source material.

Primary source path:

- `../ref/bitcoin-for-organizations/en`

Reviewed Organizations module folders:

- `../ref/bitcoin-for-organizations/en/1-bitcoin-and-risk-management/`: risk registers, scenario planning, likelihood, magnitude, timeframe, and mitigations.
- `../ref/bitcoin-for-organizations/en/2-dispelling-misconceptions/`: intrinsic value, energy, speed, innovation, bans, competing coins, decentralization, use as money, CBDCs, and obsolescence objections.
- `../ref/bitcoin-for-organizations/en/3-bitcoin-technical-history/`: TCP/IP, public-key cryptography, DigiCash, Hashcash, BitTorrent, reusable proof of work, and Bitcoin's technical synthesis.
- `../ref/bitcoin-for-organizations/en/4-impact-on-industry-verticals/`: energy, investment management, banking and payments, technology, professional services, government, charities, and nonprofit use cases.
- `../ref/bitcoin-for-organizations/en/5-impact-on-internal-functions/`: IT leadership, treasury, custody, organizational risk, and operational implementation.
- `../ref/bitcoin-for-organizations/en/6-adopting-bitcoin/`: digital scarcity and adoption cycles.
- `../ref/bitcoin-for-organizations/en/7-bitcoin-s-possible-future/`: future monetary functions, renewable grid arguments, underbanked access, and Bitcoin plus AI.
- `../ref/bitcoin-for-organizations/en/8-the-bitcoin-economy/`: public ledger concepts, block explorer use, network metrics, and Pizza Day transaction analysis.

---

# 12. Bitcoin For Organizations Cannibalization

## Cannibalization Decision

Bitcoin for Organizations should not remain a separate pathway after the redesign.

Its content should be transformed into:

- a small number of beginner-appropriate additions to the new Diploma, tracked in `advanced/mergefromorganizations.md`;
- Advanced module source trails, module seeds, activity seeds, and research notes in this file;
- educator background where the material is useful but not yet student-facing.

Most Organizations content belongs in Advanced because it assumes strategic, operational, financial, policy, technical, or sector-specific reasoning.

## Advanced Destination Map

| Advanced module destination | Organizations content to merge | Source files | Transformation notes |
|---|---|---|---|
| Monetary Economics | value, intrinsic value, store of value, monetization sequence, Gresham's Law, monetary premium, inflation, credit, savings behavior, adoption curves, and investment, risk/reward, and capital-allocation frameworks | `2-dispelling-misconceptions/1-bitcoin-has-no-intrinsic-value.md`; `2-dispelling-misconceptions/8-bitcoin-is-not-widely-used-so-is-it-money.md`; `4-impact-on-industry-verticals/2-bitcoin-and-investment-management.md`; `6-adopting-bitcoin/2-the-bitcoin-adoption-cycle.md`; `7-bitcoin-s-possible-future/1-the-potential-future-for-bitcoin.md` | Use as deeper economic reasoning and scenario analysis. Do not prescribe allocations, products, or timing; remove investment-advice tone and date and verify market claims. |
| History of Bitcoin | Cypherpunks, TCP/IP context, public-key cryptography, DigiCash, Hashcash, BitTorrent, reusable proof of work, B-money, Bit Gold, Satoshi's synthesis | `3-bitcoin-technical-history/`; `6-adopting-bitcoin/1-the-discovery-of-digital-scarcity.md` | Use as a full technical-history module. Beginner Diploma only needs the short timeline. |
| Philosophy of Bitcoin | value as social judgment, Bitcoin as protocol/discovery, decentralization, political control of money, technology versus law, rules-not-rulers framing | `2-dispelling-misconceptions/1-bitcoin-has-no-intrinsic-value.md`; `2-dispelling-misconceptions/10-will-bitcoin-be-overtaken-by-another-technology.md`; `4-impact-on-industry-verticals/6-government.md` | Keep as discussion and reasoning material. Review tone carefully before publication. |
| Transactions & Settlement | settlement finality, block explorers, confirmations, transaction transparency, card-payment flow versus Lightning flow, high-value settlement, signing ceremony ideas | `4-impact-on-industry-verticals/3-banking-and-payments.md`; `7-bitcoin-s-possible-future/1-the-potential-future-for-bitcoin.md`; `8-the-bitcoin-economy/` | Strong fit. Include practical transaction analysis and settlement comparison activities. |
| Mining & Consensus | proof of work, double-spend defense, confirmations, reorganizations, 51% attack analysis, mining centralization, miner incentives, difficulty adjustment | `6-adopting-bitcoin/1-the-discovery-of-digital-scarcity.md`; `3-bitcoin-technical-history/7-bitcoin.md`; `2-dispelling-misconceptions/2-bitcoin-is-bad-for-the-environment.md` | Use for deeper consensus. Probability tables and attack scenarios stay Advanced. |
| Privacy & Security | public ledger privacy trade-offs, self-custody bans, key custody, KYC/no-KYC implications, organizational cybersecurity, cryptojacking, wallet privacy practices | `2-dispelling-misconceptions/5-will-governments-ban-bitcoin.md`; `4-impact-on-industry-verticals/4-the-impact-on-the-technology-industry.md`; `5-impact-on-internal-functions/1-bitcoin-s-impact-on-it-leaders.md`; `8-the-bitcoin-economy/` | Separate individual privacy, organizational security, and public ledger analysis. Avoid tactical illegal guidance. |
| Payments & Exchange | Lightning, payment disintermediation, remittances, merchant payments, micropayments, on/off-ramp comparison, stablecoin comparison where relevant | `4-impact-on-industry-verticals/3-banking-and-payments.md`; `5-impact-on-internal-functions/1-bitcoin-s-impact-on-it-leaders.md`; `7-bitcoin-s-possible-future/1-the-potential-future-for-bitcoin.md`; `7-bitcoin-s-possible-future/3-banking-the-un-der-banked.md` | Strong fit. Use local examples and current-data checks. Keep stablecoins as comparison, not curriculum focus. |
| Bitcoin for Business | treasury strategy, business risk analysis, merchant acceptance, operational implementation, professional services, IT leaders, business SWOT, customer education | `1-bitcoin-and-risk-management/`; `4-impact-on-industry-verticals/2-bitcoin-and-investment-management.md`; `4-impact-on-industry-verticals/4-the-impact-on-the-technology-industry.md`; `4-impact-on-industry-verticals/5-professional-services.md`; `5-impact-on-internal-functions/` | One of the largest destinations. Split into business strategy, treasury, payments, and operations lessons. |
| Infrastructure & Maintenance | organizational implementation, IT risk, cloud cryptojacking, custody vendors, service management, support, operational continuity, data-center/mining overlap | `5-impact-on-internal-functions/1-bitcoin-s-impact-on-it-leaders.md`; `5-impact-on-internal-functions/2-what-is-a-bitcoin-treasury.md`; `7-bitcoin-s-possible-future/4-the-convergence-of-bitcoin-and-ai.md` | Useful for advanced operators. Keep vendor-specific material as examples only. |
| Communities & Circular Economies | underbanked access, local payment loops, nonprofit service delivery, donations, community resources, grassroots adoption, Bitcoin Beach-style examples | `4-impact-on-industry-verticals/7-charities-and-not-for-profit-organisations.md`; `7-bitcoin-s-possible-future/3-banking-the-un-der-banked.md`; `5-impact-on-internal-functions/2-what-is-a-bitcoin-treasury.md` | Use to build community operations and nonprofit modules. Local adaptation required. |
| Money & Society | financial exclusion, wealth inequality, debt-driven consumption, consumer behavior, institutional trust, state funding pressures, social change | `4-impact-on-industry-verticals/6-government.md`; `4-impact-on-industry-verticals/7-charities-and-not-for-profit-organisations.md`; `7-bitcoin-s-possible-future/1-the-potential-future-for-bitcoin.md`; `7-bitcoin-s-possible-future/3-banking-the-un-der-banked.md` | Good discussion material. Frame claims as scenarios or arguments, not settled facts. |
| Money & Human Rights | CBDCs, permissionless access, underbanked populations, self-custody restrictions, privacy, censorship resistance, identity barriers, Global South monetary conditions | `2-dispelling-misconceptions/5-will-governments-ban-bitcoin.md`; `2-dispelling-misconceptions/9-will-a-cbdc-render-bitcoin-obsolete.md`; `4-impact-on-industry-verticals/6-government.md`; `7-bitcoin-s-possible-future/3-banking-the-un-der-banked.md` | Strong fit. Requires careful local legal review and nonpartisan tone. |
| Energy & Mining | energy as security, stranded energy, demand response, methane/flared gas, renewable grid support, heat reuse, remote power projects | `2-dispelling-misconceptions/2-bitcoin-is-bad-for-the-environment.md`; `4-impact-on-industry-verticals/1-bitcoin-and-energy.md`; `7-bitcoin-s-possible-future/2-building-the-renewable-energy-grid.md` | Major destination. Verify all energy percentages, regional claims, and case studies. |
| Open Source Software | Bitcoin Core, open-source development, BIPs/RFC analogy, open-source wallets, public review, protocol governance, contribution pathways | `3-bitcoin-technical-history/1-the-development-of-tcp-ip.md`; `4-impact-on-industry-verticals/4-the-impact-on-the-technology-industry.md`; `2-dispelling-misconceptions/7-bitcoin-is-not-truly-decentralised.md` | Strong support for OSS module. Avoid overloading with full TCP/IP detail unless teaching protocol history. |
| Nostr & Decentralized Communication | Nostr, decentralized communications, censorship resistance, Lightning integration, marketing/community use, healthcare data examples | `4-impact-on-industry-verticals/5-professional-services.md`; `4-impact-on-industry-verticals/6-government.md`; `7-bitcoin-s-possible-future/4-the-convergence-of-bitcoin-and-ai.md` | Use as a Nostr/decentralized communication bridge. Keep healthcare examples optional and fact-checked. |
| Communication Networks | TCP/IP, layered protocols, Bitcoin as value-transfer protocol, HTTPS analogy, network effects, peer-to-peer networks, BitTorrent | `3-bitcoin-technical-history/1-the-development-of-tcp-ip.md`; `3-bitcoin-technical-history/5-bittorrent.md`; `2-dispelling-misconceptions/3-bitcoin-is-too-slow-to-be-global-money.md`; `2-dispelling-misconceptions/4-there-s-no-innovation-happening-in-bitcoin.md` | Strong fit. This can bridge technical foundations and public explanation. |
| Bitcoin Education | misconception handling, learner objections, public communication, beginner versus Advanced boundaries, scenario workshops | `2-dispelling-misconceptions/`; `1-bitcoin-and-risk-management/`; `8-the-bitcoin-economy/1-the-nature-of-bitcoin-s-ledger.md`; `8-the-bitcoin-economy/4-the-pizza-day-transaction.md` | Use for educator training and facilitation practice. |
| Bitcoin for Organizations | overall strategic pathway, risk management, internal functions, industry verticals, treasury, policy, nonprofit, IT, business adoption | All files in `../ref/bitcoin-for-organizations/en` | Keep as a meta-pathway or capstone, but do not preserve the old course unchanged. Use it as a curated pathway through other Advanced modules. |
| Bitcoin for ... (Communities & Populations) | underbanked people, nonprofits, charities, local communities, organizational types, Global South considerations | `7-bitcoin-s-possible-future/3-banking-the-un-der-banked.md`; `4-impact-on-industry-verticals/7-charities-and-not-for-profit-organisations.md`; `4-impact-on-industry-verticals/6-government.md` | Use cautiously with community input. Avoid treating populations as monolithic. |
| Cryptography | public-key cryptography, hash functions, Merkle trees, elliptic curve signatures, digital signatures, encryption | `3-bitcoin-technical-history/2-public-key-cryptography-and-protocols.md`; `3-bitcoin-technical-history/7-bitcoin.md`; `6-adopting-bitcoin/1-the-discovery-of-digital-scarcity.md` | Strong source material. Keep mathematical depth optional. |
| Computer Science Fundamentals | protocols, networks, hashes, distributed systems, Byzantine fault, proof of work, peer-to-peer systems, protocol layers | `3-bitcoin-technical-history/`; `6-adopting-bitcoin/1-the-discovery-of-digital-scarcity.md`; `6-adopting-bitcoin/2-the-bitcoin-adoption-cycle.md` | Strong source material. Could be sequenced before Cryptography. |
| Online privacy and safety | KYC/no-KYC, phishing, cryptojacking, wallet privacy, public ledger privacy, data breaches, identity exposure | `4-impact-on-industry-verticals/4-the-impact-on-the-technology-industry.md`; `5-impact-on-internal-functions/1-bitcoin-s-impact-on-it-leaders.md`; `7-bitcoin-s-possible-future/3-banking-the-un-der-banked.md`; `8-the-bitcoin-economy/` | Useful as an individual and organizational safety module. |

## Existing Titles With Little Direct Organizations Content

| Existing Advanced module title | Decision |
|---|---|
| History of Money (localisation) | Use only lightly. Organizations adds CBDCs, Global South monetary conditions, debt, and fiat-system scenarios, but it is not primarily a history-of-money source. |
| Bitcoin for Families | No direct fit. Some self-custody, underbanked, remittance, and local support examples may be adapted later, but not from an organizations angle. |

## Organizations-Derived Module Candidates

These titles have already been added to the candidate title inventory above, but they may later be merged into broader modules if the Advanced pathway needs a smaller public catalogue.

| Candidate title | Why it may be needed | Source files |
|---|---|---|
| Bitcoin Treasury and Organizational Custody | The treasury and institutional custody material is large enough to become its own module instead of being hidden under Bitcoin for Business. | `5-impact-on-internal-functions/2-what-is-a-bitcoin-treasury.md`; `4-impact-on-industry-verticals/2-bitcoin-and-investment-management.md` |
| Bitcoin Risk Management and Scenario Planning | The risk-register method is a reusable organizational workshop and could serve businesses, nonprofits, educators, and policy groups. | `1-bitcoin-and-risk-management/` |
| Bitcoin Policy and Governance | Government, CBDCs, self-custody bans, law versus technology, and policy options may be too large for Money & Human Rights alone. | `4-impact-on-industry-verticals/6-government.md`; `2-dispelling-misconceptions/5-will-governments-ban-bitcoin.md`; `2-dispelling-misconceptions/9-will-a-cbdc-render-bitcoin-obsolete.md` |
| Bitcoin and AI Payments | The AI and L402-style material is specialized and may not fit neatly under existing Lightning, business, or infrastructure modules. | `7-bitcoin-s-possible-future/4-the-convergence-of-bitcoin-and-ai.md`; `5-impact-on-internal-functions/1-bitcoin-s-impact-on-it-leaders.md` |
| On-Chain Analytics | The open-ledger metrics material is distinct from beginner verification and deserves a research/data module if expanded. | `8-the-bitcoin-economy/` |

## Source Coverage By Organizations Module

| Organizations module | Advanced destination summary |
|---|---|
| 1. Bitcoin and Risk Management | Bitcoin for Organizations; Bitcoin for Business; Bitcoin Education; Bitcoin Risk Management and Scenario Planning |
| 2. Dispelling Misconceptions | Bitcoin Education; Philosophy of Bitcoin; Monetary Economics; Energy & Mining; Payments & Exchange; Money & Human Rights; Communication Networks |
| 3. Bitcoin Technical History | History of Bitcoin; Cryptography; Computer Science Fundamentals; Communication Networks; Open Source Software |
| 4. Impact on Industry Verticals | Energy & Mining; Bitcoin for Business; Payments & Exchange; Money & Society; Money & Human Rights; Nostr & Decentralized Communication; Communities & Circular Economies |
| 5. Impact on Internal Functions | Bitcoin for Business; Infrastructure & Maintenance; Privacy & Security; Bitcoin Treasury and Organizational Custody |
| 6. Adopting Bitcoin | History of Bitcoin; Mining & Consensus; Monetary Economics; Computer Science Fundamentals |
| 7. Bitcoin's Possible Future | Money & Society; Payments & Exchange; Energy & Mining; Money & Human Rights; Infrastructure & Maintenance; Bitcoin and AI Payments |
| 8. The Bitcoin Economy | Transactions & Settlement; Privacy & Security; Mining & Consensus; On-Chain Analytics |

## Priority For Advanced Migration

| Priority | Destination | Rationale |
|---|---|---|
| 1 | Bitcoin Education / Misconceptions | Useful immediately for educators and public communication. |
| 2 | History of Bitcoin / Computer Science Fundamentals / Cryptography | Strong source material that deepens Block 2 without burdening the beginner Diploma. |
| 3 | Payments & Exchange / Transactions & Settlement | Direct follow-on from Block 3 and Block 4 practical learning. |
| 4 | Bitcoin for Business / Treasury | Core of the old Organizations path; high value for organizational audiences. |
| 5 | Energy & Mining | Large, coherent content set; needs significant fact-checking. |
| 6 | Money & Human Rights / Money & Society / Policy | Valuable but tone-sensitive and locally sensitive. |
| 7 | Open Ledger / On-Chain Analytics | Strong but specialized; should be separated from beginner verification. |
| 8 | Bitcoin and AI Payments | Interesting, but speculative and dependency-heavy. |

## Organizations Publication Guardrails

Before any Organizations material is published in Advanced modules:

- remove or soften financial, legal, tax, and investment advice language;
- convert predictions into scenarios or discussion prompts;
- verify current-data claims and date them;
- check cited links and image rights;
- distinguish Bitcoin from broader crypto without turning every section into an altcoin debate;
- separate conceptual claims from local legal or regulatory facts;
- add not-financial/legal/tax-advice boundaries where relevant;
- frame risk, reward, investment, and capital-allocation material as general education and fictional scenario analysis, never individualized recommendations;
- review tone for global audiences and translation readiness.

Current-data claims requiring verification include:

- ETF approvals, flows, assets, and performance records;
- Bitcoin price, market cap, holder estimates, hashrate, fees, and supply figures;
- Lightning usage and capacity claims;
- CBDC project counts and country status;
- corporate and national Bitcoin holdings;
- accounting, tax, AML, KYC, and regulatory rules;
- energy-use percentages, renewable-energy claims, grid-cost examples, and methane claims;
- named company, wallet, custodian, exchange, and service-provider examples.

## Material To Keep As Background Only

Do not automatically make the following student-facing:

- provocative political language;
- dated company examples used as proof of inevitability;
- named provider recommendations;
- specific tax or accounting instructions;
- investment-performance comparisons;
- claims about future government adoption;
- highly technical AI-payment workflows;
- controversial policy claims without structured evidence and counterarguments.

These can inform educator preparation, scenario design, or research notes.

---

# 13. Fact-Check And Publication Warnings

Advanced modules will likely use more current data, named tools, legal context, and technical claims than the beginner Diploma. Treat these as high-maintenance content.

Before any Advanced module is published, verify, date, cite, localize, or rewrite:

- CBDC country counts and country-status claims;
- debt, inflation, purchasing-power, wage, and productivity statistics;
- bitcoin mined-supply figures;
- halving tables and future issuance estimates;
- hashrate, mining distribution, mining-pool, and energy data;
- large-transaction fee examples;
- Visa or card-network comparisons;
- Lightning capacity, channel count, node count, speed, and fee claims;
- provider names, wallet names, exchange names, and platform names;
- legal, tax, KYC, privacy, sanctions, accounting, and regulatory claims;
- merchant fee examples;
- URLs, QR codes, and external resource links;
- safety claims about wallets, hardware devices, or custody practices.

Evergreen explanations are preferred when current data is not essential.

---

# 14. Future Design Questions

Do not resolve these before the beginner Diploma is published unless the answer is required for publication.

- Which Advanced modules should be designed first?
- Which Advanced modules are learner-facing, educator-facing, or both?
- Which topics become workshops rather than written modules?
- Which topics require local legal, tax, privacy, or safety review?
- Which topics require technical reviewers?
- Which topics require community co-design?
- What prerequisites should learners complete before each module?
- Should the Advanced pathway have levels, such as intermediate and advanced?
- How should Advanced modules connect to combined knowledge and approved-assessor-observed competency assessment and a future Advanced certification standard?
- Which older activities should be revived, redesigned, or retired?
- Which named tools can appear as global examples, and which must remain local?
- What maintenance process is needed for Advanced modules with current data?
- Which modules should be translated first after publication?

---

# 15. Parking Lot For Future Additions

Use this section for new Advanced material discovered during editing.

When adding an item, include:

- short topic name;
- source file or note origin;
- potential module;
- why it does not belong in Core;
- whether it needs fact-checking, technical review, legal review, or local adaptation.

Template:

| Topic | Source | Potential module | Why not Core | Review needed |
|---|---|---|---|---|
|  |  |  |  |  |
