# Bitcoin Diploma Redesign Plan

## Purpose

This is the source of truth for the current Bitcoin Diploma redesign structure.

It defines:

- the 4-block architecture;
- what belongs in Core, Custom, and Advanced pathways at a boundary level;
- how legacy content is being migrated;
- how in-class time should be used;
- which documents own detailed implementation work.

Detailed activities belong in `10_activities.md`. Detailed facilitation guidance belongs in `11_guide.md`. Detailed objectives belong in `05_objectives.md`. Advanced module ideas, follow-on pathway notes, and redacted legacy content for later use belong in `16_advanced.md`.

`06_plan.md` is the active plan source of truth. The older duplicated plan file has been archived at `../y_archive/y_13_plan_superseded.md`.

---

# 1. Design Decision Summary

The redesigned Diploma should be shorter, clearer, more practical, and easier to teach while preserving the open-source, community-led, Bitcoin-only identity of the original Diploma.

Current design commitments:

- in-person first;
- offline-capable print or PDF first;
- approximately 8 hours total;
- 4 blocks of approximately 2 hours each;
- Core, Custom, and Advanced content separation;
- shared Core theory and outcomes with localized, educator-led practice;
- English-first drafting with simplicity, tone, style, terminology, and translation-readiness review before translation or publication;
- practical learning in every block;
- a separate Activity Bank;
- an Educator Guide designed for facilitation, pacing, adaptation, and safety;
- Advanced technical material outside the beginner pathway;
- sparse QR code use in printed learner materials;
- future delivery branches documented without changing Core outcomes: online PDF, online cohort, self-paced, web, app, and cross-modal continuation.

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
- local spending and receiving scenarios;
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

Spending is an important possible Block 4 practice, but Block 4 should remain Custom / Bitcoin as Money because local use may also include earning, saving, receiving, resource discovery, circular economy mapping, merchant discovery, and community problem-solving.

---

# 3. Legacy Content Migration

`../ref/01_bd_202604_contents.csv` was reviewed as a legacy table-of-contents migration map.

Reading rule:

- `BLOCK` means old content moves into Core blocks 1-3.
- `CUSTOM` means old content becomes educator-selected Block 4 material.
- `ADVANCED` means old content becomes Advanced pathway material.
- `OUT` does not mean deletion when the same item is marked Custom or Advanced.
- In the reviewed table, no section is marked as out-only.
- Daily-life Bitcoin use should become Custom module source material unless a local delivery plan selects it.

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

## Publication Guardrails

Fact-check rule:

Current-data examples must be verified, dated, cited, or replaced with evergreen explanations before publication. This includes CBDC country counts, bitcoin mined-supply figures, large-transaction fee examples, Visa transaction comparisons, Lightning capacity or speed claims, fee amounts, provider names, and legal or tax statements.

Tone and claims rule:

Preserve the Diploma's conviction, clarity, and Bitcoin-only identity, but avoid turning interpretive claims into unsupported facts. Where a claim is likely to invite disagreement or depend on context, prefer guided comparison, claim/evidence/reasoning prompts, or local discussion.

Print QR rule:

Printed PDFs should use QR codes sparingly. QR codes should point only to stable, high-value destinations such as the source repository, canonical update page, educator resources, support or donation page, or certificate verification if available.

Multilingual source rule:

Draft source material in English first. Before translation or publication, review the English source for beginner readability, simple sentence structure, consistent tone and style, terminology and glossary alignment, ambiguity, idioms, and culturally narrow references. After translation, review each language version for preserved meaning, simple language, appropriate tone, terminology consistency, and local appropriateness.

Delivery-branch rule:

Offline/in-person PDF is the first implementation mode. Online PDF, online cohort, self-paced, web, app, and cross-modal versions should branch from the same Core outcomes rather than become separate curricula.

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

Core should function as the shared theory layer across languages and delivery modes.

## Custom

Custom completes Block 4.

Custom should:

- be selected by the educator;
- connect Bitcoin to local daily life;
- use tools and resources local bitcoiners actually use;
- be guided by educators or local experts who understand local risks and learner readiness;
- focus on workshops, demonstrations, and local problem-solving;
- include safety notes and realistic next steps.

Template Custom units should include:

- local problem or opportunity;
- learner profile;
- tools or resources;
- local legal, tax, and safety context where relevant;
- language or terminology notes where relevant;
- delivery-mode notes where relevant;
- workshop or demonstration;
- safety warnings;
- educator preparation;
- learner task;
- evidence of learning;
- local adaptation notes.

## Advanced

Advanced module ideas, follow-on pathway notes, and redacted legacy content for later use are collected in `16_advanced.md`.

Advanced outcomes are ongoing and should be designed module by module after the redesigned beginner Diploma is published.

Advanced content should not overload the beginner pathway. It may later become optional extensions, separate workshops, educator background, or follow-on courses.

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

Internal performance rule:

Treat the beginner pathway like a lean, high-performance learning experience. Every required component should improve learner clarity, completion likelihood, practice, educator usability, safety, translation readiness, or maintainability.

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
| Advanced module ideas and redacted content collection | `16_advanced.md` |
| Public keynote and stakeholder brief | `../public/MFB-BD-Keynote.md` |

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

Follow-on pathway ideas are collected in `16_advanced.md`.

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
- final QR code destination list for print materials;
- delivery-mode branch requirements for online PDF, online cohort, self-paced, web, app, and cross-modal continuation;
- multilingual glossary readiness;
- ownership and approval criteria for English-source simplicity and translation-readiness review;
- ownership and approval criteria for post-translation language review;
- final assessment format;
- future certification verification options, including possible on-chain timestamping;
- low-connectivity delivery assumptions;
- pilot and educator review process;
- exact publication formats;
- Advanced module objectives and sequencing, tracked in `16_advanced.md`.

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
