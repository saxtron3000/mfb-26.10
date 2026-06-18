# Bitcoin Diploma Redesign Plan

## Purpose

This is the source of truth for the current Bitcoin Diploma redesign structure.

It defines:

- the 4-block architecture;
- what belongs in Core, Custom, and Advanced pathways;
- how legacy content is being migrated;
- how the split-modules review informs the redesign;
- how in-class time should be used;
- which documents own detailed implementation work.

Detailed activities belong in `10_activities.md`. Detailed facilitation guidance belongs in `11_guide.md`. Detailed objectives belong in `05_objectives.md`.

`06_plan.md` is the active plan source of truth. Any duplicated or older plan file, including `13_plan.md`, should be reconciled or archived before publication.

---

# 1. Design Decision Summary

The redesigned Diploma should be shorter, clearer, more practical, and easier to teach while preserving the open-source, community-led, Bitcoin-only identity of the original Diploma.

Current design commitments:

- in-person first;
- approximately 8 hours total;
- 4 blocks of approximately 2 hours each;
- Core, Custom, and Advanced content separation;
- practical learning in every block;
- a separate Activity Bank;
- an Educator Guide designed for facilitation, pacing, adaptation, and safety;
- Advanced technical material outside the beginner pathway.

The public explanation is simple:

The Diploma is being reorganized, not replaced.

---

# 2. Four-Block Architecture

| Block | Role | Title | Core question |
|---|---|---|---|
| 1 | Problem | Fiat | What problem does fiat money create? |
| 2 | Solution | Bitcoin | Why was Bitcoin created, and how does it respond? |
| 3 | Action | Self-custody | How do I take responsibility for using and securing Bitcoin? |
| 4 | Custom | Bitcoin as Money | How can Bitcoin function as money in this community? |

## Block 1: Problem / Fiat

Keep this block focused on money and the fiat problem.

Core content:

- opening questions about money;
- what money is;
- functions and properties of money;
- barter limitations, including the double coincidence of wants;
- scarcity, time preference, and opportunity cost at beginner level;
- short history from barter to modern money, including the Nixon Shock as a brief historical marker;
- fiat systems, including central banks, commercial banks, governments, and citizens at beginner level;
- fractional reserve banking and bank runs at beginner level;
- inflation and purchasing power;
- CBDCs as a beginner fiat-system example where appropriate.

Outcome:

Learners can explain why fiat money is the problem Bitcoin responds to.

## Block 2: Solution / Bitcoin

Keep this block focused on why Bitcoin exists and what makes it different.

Core content:

- search for digital and decentralized money, including the Cypherpunk context;
- earlier digital-money attempts such as DigiCash, Hashcash, and Bit Gold at beginner level;
- the double-spend problem at beginner level;
- Bitcoin origin story and timeline, including the whitepaper, Genesis Block, first transaction, and Pizza Day;
- decentralization;
- users, nodes, and miners at beginner level;
- proof of work at beginner level;
- finite supply and halving;
- satoshis and unit bias;
- peer-to-peer transfer;
- verifiability;
- Bitcoin as sound digital money;
- personal responsibility as the bridge into self-custody.

Outcome:

Learners can explain Bitcoin's purpose and how it differs from fiat money.

## Block 3: Action / Self-custody

Keep this block practical and safety-oriented.

Core content:

- wallets as interfaces;
- addresses, keys, and seed phrases;
- custodial and non-custodial use;
- hot and cold wallet distinction;
- wallet recovery and seed phrase testing;
- receiving bitcoin;
- sending bitcoin;
- verification, including basic block explorer orientation where it supports beginner understanding;
- irreversible transactions and address verification;
- beginner safety practices, including common scams, copy/paste address risks, seed phrase protection, open-source wallet preference, and starting small;
- acquiring and exchanging bitcoin as a concept, not financial advice;
- only the transaction detail needed for responsible beginner use.

Outcome:

Learners can explain beginner self-custody concepts and identify basic safety practices.

## Block 4: Custom / Bitcoin as Money

This block is educator-selected.

Educators choose Custom modules because they understand their students, tools, risks, opportunities, and local conditions better than a centralized curriculum can.

Custom modules should usually be practical workshops or demonstrations.

Possible Custom content:

- local wallet tools;
- Lightning payments where locally appropriate;
- custodial Lightning wallet demonstrations where locally appropriate;
- Lightning invoices and Lightning addresses where locally appropriate;
- merchant payments;
- everyday purchase scenarios;
- buying and selling bitcoin in the community;
- KYC and no-KYC trade-offs where locally appropriate;
- exchanges, peer-to-peer exchange, earning bitcoin, and Bitcoin ATMs as local pathway examples;
- local resource maps;
- BTCMap or equivalent local-resource discovery;
- circular economies;
- local Bitcoin communities;
- local monetary problems;
- CBDCs in the local context;
- community-specific Bitcoin use cases.

Outcome:

Learners can identify beginner-appropriate ways Bitcoin can function as money in local daily life.

---

# 3. Legacy Content Migration

`../ref/01_bd_202604_contents.csv` was reviewed as a legacy table-of-contents migration map.

The split-modules document in `../docs/` was reviewed as a learner-facing reconstruction of old Diploma content organized into four modules. It should be treated as internal drafting source material, not as the controlling architecture.

Reading rule:

- `BLOCK` means old content moves into Core blocks 1-3.
- `CUSTOM` means old content becomes educator-selected Block 4 material.
- `ADVANCED` means old content becomes Advanced pathway material.
- `OUT` does not mean deletion when the same item is marked Custom or Advanced.
- In the reviewed table, no section is marked as out-only.
- The four reconstructed modules map broadly onto the four-block structure, but they do not override Core, Custom, and Advanced boundaries.
- Learner-facing explanations from the split-modules document may be reused in the Student Book draft after trimming and fact-checking.
- Activity placeholders from the split-modules document belong in `10_activities.md`.
- Facilitation implications from the split-modules document belong in `11_guide.md`.
- The fixed Module 4 sequence should become Custom module source material unless a local delivery plan selects it.

Migration summary:

| Destination | Legacy content signal | Redesign decision |
|---|---|---|
| Core Block 1 | money, money history, fiat, early problem framing | Keep beginner monetary foundations and fiat problem material. |
| Core Block 2 | decentralized currency search, Bitcoin origin, Bitcoin benefits | Keep beginner Bitcoin purpose and properties. |
| Core Block 3 | wallet use, receiving, sending, verification, selected technical orientation | Keep practical use and safety material. |
| Custom Block 4 | daily-life Bitcoin use, local tools, Lightning payments, local spending | Move into educator-selected workshops and demonstrations. |
| Advanced | deeper psychology, detailed mining, mempool, detailed transactions, philosophy, future scenarios | Move into Advanced pathways or educator background. |

Split decisions:

- Psychology of money stays in Core only at beginner level; deeper behavioral analysis moves to Advanced.
- Nodes and miners stay in Core only as simple roles; technical mechanics move to Advanced.
- Transaction concepts stay in Core only where needed for safe use and verification; detailed models move to Advanced.
- CBDCs may appear briefly in Block 1 or locally in Block 4; policy and technical depth moves to Advanced.
- Lightning distinctions may be introduced briefly, but wallet setup and payment practice normally belongs in Custom.
- Buying and selling bitcoin may appear in Core as a conceptual risk map, but provider-specific practice belongs in Custom.
- Named services, wallets, exchanges, peer-to-peer platforms, and local recommendations should not become global Student Book recommendations.

## Split-Modules Review

The split-modules document is useful because it turns legacy content into draft learner prose, concrete examples, activity placeholders, and end-of-module takeaways.

Migration decisions from the split-modules document:

| Split-modules content | Destination |
|---|---|
| Learner-facing explanations | Student Book draft in `08_draft.md`, after trimming for the 8-hour pathway. |
| Opening money questions and module review prompts | Student Book draft and assessment prompts. |
| Activity placeholders | Activity Bank in `10_activities.md`. |
| Fiat-system roles, fractional reserve banking, bank runs, Nixon Shock, and CBDCs | Core Block 1 at beginner level; deeper policy and history move to Advanced. |
| Cypherpunks, DigiCash, Hashcash, Bit Gold, double-spend problem, and Bitcoin origin timeline | Core Block 2 as concise background and narrative bridge. |
| Satoshis and unit-bias framing | Core Block 2, with reinforcement in custody and payments content. |
| Wallet setup, recovery, seed phrase testing, address verification, and safety warnings | Core Block 3 and aligned activities. |
| Block explorer and mempool references | Core only when used for beginner verification; deeper mechanics move to Advanced or educator demonstration notes. |
| Lightning daily-use section | Custom Block 4 candidate material. |
| Buying and selling section | Core Block 3 as concept and risk orientation; Custom Block 4 for local practice. |
| KYC/no-KYC, exchanges, P2P, ATMs, gift cards, and earning bitcoin | Local Custom guidance or Advanced trade-off analysis; avoid provider endorsement. |
| BTCMap, circular economies, local merchant payments, and local communities | Custom Block 4 candidate material. |
| Named platforms and services | Local educator guidance only, unless publication rules later approve specific examples. |
| Current statistics and legal/tax statements | Fact-check before publication or convert to evergreen wording. |

Fact-check rule:

Current-data examples must be verified, dated, cited, or replaced with evergreen explanations before publication. This includes CBDC country counts, bitcoin mined-supply figures, large-transaction fee examples, Visa transaction comparisons, Lightning capacity or speed claims, fee amounts, provider names, and legal or tax statements.

Tone and claims rule:

Preserve the Diploma's conviction, clarity, and Bitcoin-only identity, but avoid turning interpretive claims into unsupported facts. Where a claim is likely to invite disagreement or depend on context, prefer guided comparison, claim/evidence/reasoning prompts, or local discussion.

---

# 4. Core, Custom, And Advanced Boundaries

## Core

Core is required for every learner.

Core should include:

- money foundations;
- fiat problems;
- Bitcoin purpose and core properties;
- sats as a beginner unit concept;
- beginner custody concepts;
- wallet recovery basics;
- receiving, sending, and verification orientation;
- beginner safety practices, including seed phrase protection, seed phrase testing, scam awareness, address verification, and starting small;
- acquiring and exchanging pathways as beginner concepts, not recommendations;
- guided discussion and reflection.

Core should not promise independent mastery of economics, technical systems, or high-stakes custody.

## Custom

Custom completes Block 4.

Custom should:

- be selected by the educator;
- connect Bitcoin to local daily life;
- use tools and resources local bitcoiners actually use;
- focus on workshops, demonstrations, and local problem-solving;
- include safety notes and realistic next steps.

Template Custom units should include:

- local problem or opportunity;
- learner profile;
- tools or resources;
- local legal, tax, and safety context where relevant;
- workshop or demonstration;
- safety warnings;
- educator preparation;
- learner task;
- evidence of learning;
- local adaptation notes.

## Advanced

Advanced outcomes are ongoing and should be designed module by module.

Advanced content should not overload the beginner pathway. It may become optional extensions, separate workshops, educator background, or follow-on courses.

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
- Bitcoin for X: Communities & Populations
- Cryptography
- Computer Science Fundamentals
- Online privacy and safety

Note: `Bitcoin for X` is a flexible Advanced category for population- or community-specific modules, such as Bitcoin for women, Bitcoin for Muslims, or other locally relevant communities. These modules should be developed with community input and should avoid treating any group as monolithic.

The full Advanced module title list should appear only in this file.

---

# 5. In-Class Time Rules

Class time should be used for learning that benefits from live facilitation.

Prioritize:

- discussion;
- questions;
- misconception correction;
- guided practice;
- scenario analysis;
- peer explanation;
- reflection;
- local application;
- educator-led synthesis.

Minimize:

- long readings;
- extended lectures;
- dense technical background;
- long definitions without application;
- advanced optional content.

Each block should close with a short review point. The review should include key takeaways, a learner explanation prompt, a link to the next block, and an evidence-of-learning opportunity that can connect to `12_assessment.md`.

Each block should follow a simple rhythm:

1. Present the core idea briefly.
2. Check understanding.
3. Practice through a scenario, activity, comparison, or demonstration.
4. Ask learners to explain, decide, apply, or reflect.
5. Review the connection to the wider Diploma and capture evidence of learning.

---

# 6. What Stays And What Moves

| Stays in Core | Moves elsewhere |
|---|---|
| Money, fiat, inflation, purchasing power | Detailed monetary theory and long policy history |
| Double coincidence of wants, fiat-system roles, fractional reserve banking, bank runs, and brief CBDC orientation | Detailed banking policy, CBDC policy, and long monetary-policy history |
| Bitcoin origin, purpose, properties, finite supply, sats, and beginner timeline | Deep protocol and cryptography detail |
| Users, nodes, miners, proof of work at beginner level | Detailed mining mechanics, mempool, transaction lifecycle |
| Wallets, addresses, keys, seed phrases, custody trade-offs, wallet recovery basics, and seed phrase testing | Advanced custody models and operational security |
| Receiving, sending, verification, address checking, beginner safety, scam awareness, and start-small guidance | Advanced troubleshooting and technical analysis |
| Beginner acquiring and exchanging pathways as risk orientation | Named provider recommendations, live exchange setup, deep KYC/no-KYC trade-off analysis, and tax/legal advice |
| On-chain and Lightning distinctions at beginner level | Lightning channel mechanics, routing, liquidity, and node operations |
| Local daily-life Bitcoin use as Custom source material | Fixed global requirements for specific local tools, merchants, exchanges, or communities |
| Guided discussion and practical orientation | Full activity instructions, facilitation scripts, and optional extensions |

Activities leave the main student-facing text and move to `10_activities.md`.

Educator preparation, timing, adaptation, misconception support, and debrief guidance move to `11_guide.md`.

---

# 7. Material Ownership

| Material | Owner document |
|---|---|
| Student-facing draft scaffold | `08_draft.md` |
| Learning objectives and competencies | `05_objectives.md` |
| Activity categories and activity template | `10_activities.md` |
| Educator facilitation and Custom selection guidance | `11_guide.md` |
| Assessment evidence and direction | `12_assessment.md` |
| Certification boundaries | `13_certification.md` |
| Publication rules | `15_spec.md` |
| Public brief | `../public/mfb-bd-prague.md` |
| Short keynote handoff | `../public/mfb-bd-prague-keynote.md` |

---

# 8. October 2026 Output

The October 2026 redesign should produce:

- a 4-block beginner Diploma;
- an approximately 8-hour delivery path;
- clear learning objectives;
- Student Book draft;
- Educator Guide;
- Activity Bank;
- Custom module templates;
- assessment framework;
- publication-ready source files;
- public communication materials.

The Diploma should remain the entry point into a wider learning ecosystem, not the container for every valuable Bitcoin topic.

---

# 9. Follow-On Pathways

Future follow-on pathways may include:

1. Bitcoin Fundamentals: the redesigned Diploma.
2. Bitcoin Self-Custody: deeper wallet, backup, verification, and safety practice.
3. Lightning Network: deeper payment, routing, liquidity, and trade-off study.
4. Bitcoin Technical Foundations: deeper protocol and system mechanics.
5. Bitcoin Economics: deeper monetary history, policy, incentives, and economic reasoning.

---

# 10. Open Decisions

The redesign still needs decisions on:

- final Custom module options;
- minimum Custom module templates for October 2026;
- minimum required practical tasks;
- how much learner-facing prose should appear in the Student Book versus educator-led explanation;
- whether sats should be introduced primarily in Block 2 or Block 3;
- which safety practices are required Core versus optional Custom;
- which named tools or services may appear in published materials, and where;
- how to reconcile or archive duplicated planning files such as `13_plan.md`;
- final assessment format;
- future certification verification options, including possible on-chain timestamping;
- low-connectivity delivery assumptions;
- pilot and educator review process;
- exact publication formats;
- Advanced module objectives and sequencing.

---

# 11. Working Principle

Use class time for what class time does best:

- conversation;
- reasoning;
- practice;
- feedback;
- reflection;
- local application.

Content should support those experiences, not crowd them out.
