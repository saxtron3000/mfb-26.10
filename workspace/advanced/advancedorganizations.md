# Bitcoin For Organizations Advanced Merge Map

## Purpose

This document shows how the retiring `ref/bitcoin-for-organizations/en` path can be cannibalized into the Advanced module holding file, `workspace/17_advanced.md`.

Review date: 2026-06-26

Source reviewed: every Markdown file in `ref/bitcoin-for-organizations/en`.

Destination: the Advanced module titles already listed in `workspace/17_advanced.md`, with a small number of suggested new module titles where the Organizations path contains useful material that does not fit cleanly into the current list.

## Cannibalization Decision

Bitcoin for Organizations should not remain a standalone path after the Diploma redesign.

Its content should be transformed into:

- a small number of beginner-appropriate additions to the new Diploma, tracked in `workspace/mergefromorganizations.md`;
- a much larger set of Advanced module source trails, tracked here and later merged into `workspace/17_advanced.md`;
- educator background, activity seeds, and future research notes where the content is useful but not yet publication-ready.

Most Organizations content is Advanced because it assumes strategic, operational, financial, policy, technical, or sector-specific reasoning.

## How To Use This File

When updating `17_advanced.md`, use the table below to add source trails under the existing candidate Advanced module titles.

Each entry identifies:

- the `17_advanced.md` module title or proposed new title;
- Organizations content that should feed it;
- source files;
- how the material should be transformed;
- notes or guardrails.

This is not a finished Advanced curriculum.

## Merge Map To Existing `17_advanced.md` Titles

| Existing Advanced module title | Organizations content to merge | Source files | Transformation notes |
|---|---|---|---|
| Monetary Economics | value, intrinsic value, store of value, monetization sequence, Gresham's Law, monetary premium, inflation, credit, savings behavior, adoption curves | `2-dispelling-misconceptions/1-bitcoin-has-no-intrinsic-value.md`; `2-dispelling-misconceptions/8-bitcoin-is-not-widely-used-so-is-it-money.md`; `4-impact-on-industry-verticals/2-bitcoin-and-investment-management.md`; `6-adopting-bitcoin/2-the-bitcoin-adoption-cycle.md`; `7-bitcoin-s-possible-future/1-the-potential-future-for-bitcoin.md` | Use as deeper economic reasoning. Remove investment advice tone. Date and verify market claims. |
| History of Bitcoin | Cypherpunks, TCP/IP context, public-key cryptography, DigiCash, Hashcash, BitTorrent, reusable proof of work, B-money, Bit Gold, Satoshi's synthesis | `3-bitcoin-technical-history/*.md`; `6-adopting-bitcoin/1-the-discovery-of-digital-scarcity.md` | Use as a full technical-history module. Beginner Diploma only needs the short timeline. |
| Philosophy of Bitcoin | value as social judgment, Bitcoin as protocol/discovery, decentralization, political control of money, technology versus law, "rules not rulers" framing | `2-dispelling-misconceptions/1-bitcoin-has-no-intrinsic-value.md`; `2-dispelling-misconceptions/10-will-bitcoin-be-overtaken-by-another-technology.md`; `4-impact-on-industry-verticals/6-government.md` | Keep as discussion and reasoning material. Review tone carefully before publication. |
| Transactions & Settlement | settlement finality, block explorers, confirmations, transaction transparency, card-payment flow versus Lightning flow, high-value settlement, signing ceremony ideas | `4-impact-on-industry-verticals/3-banking-and-payments.md`; `7-bitcoin-s-possible-future/1-the-potential-future-for-bitcoin.md`; `8-the-bitcoin-economy/*.md` | Strong fit. Include practical transaction analysis and settlement comparison activities. |
| Mining & Consensus | proof of work, double-spend defense, confirmations, reorganizations, 51% attack analysis, mining centralization, miner incentives, difficulty adjustment | `6-adopting-bitcoin/1-the-discovery-of-digital-scarcity.md`; `3-bitcoin-technical-history/7-bitcoin.md`; `2-dispelling-misconceptions/2-bitcoin-is-bad-for-the-environment.md` | Use for deeper consensus module. Probability tables and attack scenarios stay Advanced. |
| Privacy & Security | public ledger privacy trade-offs, self-custody bans, key custody, KYC/no-KYC implications, organizational cybersecurity, cryptojacking, wallet privacy practices | `2-dispelling-misconceptions/5-will-governments-ban-bitcoin.md`; `4-impact-on-industry-verticals/4-the-impact-on-the-technology-industry.md`; `5-impact-on-internal-functions/1-bitcoin-s-impact-on-it-leaders.md`; `8-the-bitcoin-economy/*.md` | Separate individual privacy, organizational security, and public ledger analysis. Avoid tactical illegal guidance. |
| Payments & Exchange | Lightning, payment disintermediation, remittances, merchant payments, micropayments, on/off-ramp comparison, stablecoin comparison where relevant | `4-impact-on-industry-verticals/3-banking-and-payments.md`; `5-impact-on-internal-functions/1-bitcoin-s-impact-on-it-leaders.md`; `7-bitcoin-s-possible-future/1-the-potential-future-for-bitcoin.md`; `7-bitcoin-s-possible-future/3-banking-the-un-der-banked.md` | Strong fit. Use local examples and current-data checks. Keep stablecoins as comparison, not curriculum focus. |
| Bitcoin for Business | treasury strategy, business risk analysis, merchant acceptance, operational implementation, professional services, IT leaders, business SWOT, customer education | `1-bitcoin-and-risk-management/*.md`; `4-impact-on-industry-verticals/2-bitcoin-and-investment-management.md`; `4-impact-on-industry-verticals/4-the-impact-on-the-technology-industry.md`; `4-impact-on-industry-verticals/5-professional-services.md`; `5-impact-on-internal-functions/*.md` | This is one of the largest destinations. Split into business strategy, treasury, payments, and operations lessons. |
| Infrastructure & Maintenance | organizational implementation, IT risk, cloud cryptojacking, custody vendors, service management, support, operational continuity, data-center/mining overlap | `5-impact-on-internal-functions/1-bitcoin-s-impact-on-it-leaders.md`; `5-impact-on-internal-functions/2-what-is-a-bitcoin-treasury.md`; `7-bitcoin-s-possible-future/4-the-convergence-of-bitcoin-and-ai.md` | Useful for advanced operators. Keep vendor-specific material as examples only. |
| Communities & Circular Economies | underbanked access, local payment loops, nonprofit service delivery, donations, community resources, grassroots adoption, Bitcoin Beach-style examples | `4-impact-on-industry-verticals/7-charities-and-not-for-profit-organisations.md`; `7-bitcoin-s-possible-future/3-banking-the-un-der-banked.md`; `5-impact-on-internal-functions/2-what-is-a-bitcoin-treasury.md` | Use to build community operations and nonprofit modules. Local adaptation required. |
| Money & Society | financial exclusion, wealth inequality, debt-driven consumption, consumer behavior, institutional trust, state funding pressures, social change | `4-impact-on-industry-verticals/6-government.md`; `4-impact-on-industry-verticals/7-charities-and-not-for-profit-organisations.md`; `7-bitcoin-s-possible-future/1-the-potential-future-for-bitcoin.md`; `7-bitcoin-s-possible-future/3-banking-the-un-der-banked.md` | Good discussion material. Claims should be framed as scenarios or arguments, not settled facts. |
| Money & Human Rights | CBDCs, permissionless access, underbanked populations, self-custody restrictions, privacy, censorship resistance, identity barriers, Global South monetary conditions | `2-dispelling-misconceptions/5-will-governments-ban-bitcoin.md`; `2-dispelling-misconceptions/9-will-a-cbdc-render-bitcoin-obsolete.md`; `4-impact-on-industry-verticals/6-government.md`; `7-bitcoin-s-possible-future/3-banking-the-un-der-banked.md` | Strong fit. Requires careful local legal review and nonpartisan tone. |
| Energy & Mining | energy as security, stranded energy, demand response, methane/flared gas, renewable grid support, heat reuse, remote power projects | `2-dispelling-misconceptions/2-bitcoin-is-bad-for-the-environment.md`; `4-impact-on-industry-verticals/1-bitcoin-and-energy.md`; `7-bitcoin-s-possible-future/2-building-the-renewable-energy-grid.md` | Major destination. Verify all energy percentages, regional claims, and case studies. |
| Open Source Software | Bitcoin Core, open-source development, BIPs/RFC analogy, open-source wallets, public review, protocol governance, contribution pathways | `3-bitcoin-technical-history/1-the-development-of-tcp-ip.md`; `4-impact-on-industry-verticals/4-the-impact-on-the-technology-industry.md`; `2-dispelling-misconceptions/7-bitcoin-is-not-truly-decentralised.md` | Strong support for OSS module. Avoid overloading with full TCP/IP detail unless teaching protocol history. |
| Nostr & Decentralized Communication | Nostr, decentralized communications, censorship resistance, Lightning integration, marketing/community use, healthcare data examples | `4-impact-on-industry-verticals/5-professional-services.md`; `4-impact-on-industry-verticals/6-government.md`; `7-bitcoin-s-possible-future/4-the-convergence-of-bitcoin-and-ai.md` | Use as a Nostr/decentralized communication bridge. Keep healthcare examples optional and fact-checked. |
| Communication Networks | TCP/IP, layered protocols, Bitcoin as value-transfer protocol, HTTPS analogy, network effects, peer-to-peer networks, BitTorrent | `3-bitcoin-technical-history/1-the-development-of-tcp-ip.md`; `3-bitcoin-technical-history/5-bittorrent.md`; `2-dispelling-misconceptions/3-bitcoin-is-too-slow-to-be-global-money.md`; `2-dispelling-misconceptions/4-there-s-no-innovation-happening-in-bitcoin.md` | Strong fit. This can bridge technical foundations and public explanation. |
| Bitcoin Education | misconception handling, learner objections, public communication, beginner versus Advanced boundaries, scenario workshops | `2-dispelling-misconceptions/*.md`; `1-bitcoin-and-risk-management/*.md`; `8-the-bitcoin-economy/1-the-nature-of-bitcoin-s-ledger.md`; `8-the-bitcoin-economy/4-the-pizza-day-transaction.md` | Use for educator training and facilitation practice. |
| Bitcoin for Organizations | overall strategic pathway, risk management, internal functions, industry verticals, treasury, policy, nonprofit, IT, business adoption | All files in `ref/bitcoin-for-organizations/en` | Keep as a meta-pathway or capstone, but do not preserve the old course unchanged. Use it as a curated pathway through other Advanced modules. |
| Bitcoin for ... (Communities & Populations) | underbanked people, nonprofits, charities, local communities, organizational types, Global South considerations | `7-bitcoin-s-possible-future/3-banking-the-un-der-banked.md`; `4-impact-on-industry-verticals/7-charities-and-not-for-profit-organisations.md`; `4-impact-on-industry-verticals/6-government.md` | Use cautiously with community input. Avoid treating populations as monolithic. |
| Cryptography | public-key cryptography, hash functions, Merkle trees, elliptic curve signatures, digital signatures, encryption | `3-bitcoin-technical-history/2-public-key-cryptography-and-protocols.md`; `3-bitcoin-technical-history/7-bitcoin.md`; `6-adopting-bitcoin/1-the-discovery-of-digital-scarcity.md` | Strong source material. Keep mathematical depth optional. |
| Computer Science Fundamentals | protocols, networks, hashes, distributed systems, Byzantine fault, proof of work, peer-to-peer systems, protocol layers | `3-bitcoin-technical-history/*.md`; `6-adopting-bitcoin/1-the-discovery-of-digital-scarcity.md`; `6-adopting-bitcoin/2-the-bitcoin-adoption-cycle.md` | Strong source material. Could be sequenced before Cryptography. |
| Online privacy and safety | KYC/no-KYC, phishing, cryptojacking, wallet privacy, public ledger privacy, data breaches, identity exposure | `4-impact-on-industry-verticals/4-the-impact-on-the-technology-industry.md`; `5-impact-on-internal-functions/1-bitcoin-s-impact-on-it-leaders.md`; `7-bitcoin-s-possible-future/3-banking-the-un-der-banked.md`; `8-the-bitcoin-economy/*.md` | Useful as an individual and organizational safety module. |

## Existing Titles With Little Direct Organizations Content

| Existing Advanced module title | Decision |
|---|---|
| History of Money (localisation) | Use only lightly. Organizations adds CBDCs, Global South monetary conditions, debt, and fiat-system scenarios, but it is not primarily a history-of-money source. |
| Bitcoin for Families | No direct fit. Some self-custody, underbanked, remittance, and local support examples may be adapted later, but not from an organizations angle. |

## Suggested New Advanced Module Titles

The existing title list in `17_advanced.md` is broad enough to absorb most material. If new titles are added later, these are the strongest candidates:

| Suggested new title | Why it may be needed | Source files |
|---|---|---|
| Bitcoin Treasury And Organizational Custody | The treasury and institutional custody material is large enough to become its own module instead of being hidden under Bitcoin for Business. | `5-impact-on-internal-functions/2-what-is-a-bitcoin-treasury.md`; `4-impact-on-industry-verticals/2-bitcoin-and-investment-management.md` |
| Bitcoin Risk Management And Scenario Planning | The risk-register method is a reusable organizational workshop and could serve businesses, nonprofits, educators, and policy groups. | `1-bitcoin-and-risk-management/*.md` |
| Bitcoin Policy And Governance | Government, CBDCs, self-custody bans, law versus technology, and policy options may be too large for Money & Human Rights alone. | `4-impact-on-industry-verticals/6-government.md`; `2-dispelling-misconceptions/5-will-governments-ban-bitcoin.md`; `2-dispelling-misconceptions/9-will-a-cbdc-render-bitcoin-obsolete.md` |
| Bitcoin And AI Payments | The AI and L402 material is highly specialized and may not fit neatly under existing Lightning, business, or infrastructure modules. | `7-bitcoin-s-possible-future/4-the-convergence-of-bitcoin-and-ai.md`; `5-impact-on-internal-functions/1-bitcoin-s-impact-on-it-leaders.md` |
| On-Chain Analytics | The open-ledger metrics material is distinct from beginner verification and deserves a research/data module if expanded. | `8-the-bitcoin-economy/*.md` |

## Source Coverage By Organizations Module

| Organizations module | Advanced destination summary |
|---|---|
| 1. Bitcoin and Risk Management | Bitcoin for Organizations; Bitcoin for Business; Bitcoin Education; proposed Bitcoin Risk Management And Scenario Planning |
| 2. Dispelling Misconceptions | Bitcoin Education; Philosophy of Bitcoin; Monetary Economics; Energy & Mining; Payments & Exchange; Money & Human Rights; Communication Networks |
| 3. Bitcoin Technical History | History of Bitcoin; Cryptography; Computer Science Fundamentals; Communication Networks; Open Source Software |
| 4. Impact on Industry Verticals | Energy & Mining; Bitcoin for Business; Payments & Exchange; Money & Society; Money & Human Rights; Nostr & Decentralized Communication; Communities & Circular Economies |
| 5. Impact on Internal Functions | Bitcoin for Business; Infrastructure & Maintenance; Privacy & Security; proposed Bitcoin Treasury And Organizational Custody |
| 6. Adopting Bitcoin | History of Bitcoin; Mining & Consensus; Monetary Economics; Computer Science Fundamentals |
| 7. Bitcoin's Possible Future | Money & Society; Payments & Exchange; Energy & Mining; Money & Human Rights; Infrastructure & Maintenance; proposed Bitcoin And AI Payments |
| 8. The Bitcoin Economy | Transactions & Settlement; Privacy & Security; Mining & Consensus; proposed On-Chain Analytics |

## Recommended Additions To `17_advanced.md`

Add a new section to `17_advanced.md` after the current legacy migration notes or near the redacted content collection:

Suggested section title:

`Bitcoin For Organizations Cannibalization`

Suggested content structure:

1. State that Bitcoin for Organizations will not remain a separate pathway after the redesign.
2. Preserve the source path: `../ref/bitcoin-for-organizations/en`.
3. Link to this file as the detailed merge map.
4. Add a summary table of module destinations:
   - Bitcoin for Business;
   - Energy & Mining;
   - Payments & Exchange;
   - Money & Human Rights;
   - Transactions & Settlement;
   - Mining & Consensus;
   - History of Bitcoin;
   - Cryptography;
   - Computer Science Fundamentals;
   - Open Source Software;
   - Nostr & Decentralized Communication;
   - Communities & Circular Economies;
   - Bitcoin Education;
   - Bitcoin for Organizations.
5. Note that beginner-appropriate items are separately tracked in `mergefromorganizations.md`.

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

## Publication Guardrails

Before any Organizations material is published in Advanced modules:

- remove or soften financial, legal, tax, and investment advice language;
- convert predictions into scenarios or discussion prompts;
- verify current-data claims and date them;
- check cited links and image rights;
- distinguish Bitcoin from broader crypto without turning every section into an altcoin debate;
- separate conceptual claims from local legal or regulatory facts;
- add "not financial/legal/tax advice" boundaries where relevant;
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

## Relationship To Other Workspace Files

Use:

- `workspace/17_advanced.md` as the official Advanced holding file;
- `workspace/mergefromorganizations.md` for beginner Diploma merge decisions;
- `workspace/06_plan.md` for Core, Custom, and Advanced boundaries;
- `workspace/10_activities.md` for future activity templates;
- `workspace/11_guide.md` for educator-facing misconception guidance.

This file should remain the detailed Organizations-to-Advanced source map until its strongest material has been migrated into `17_advanced.md`.
