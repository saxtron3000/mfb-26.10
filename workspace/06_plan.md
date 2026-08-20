# Bitcoin Diploma Redesign Plan

## Purpose

This is the source of truth for the current Bitcoin Diploma redesign structure.

It defines:

- the 4-module architecture;
- what belongs in Core, Custom, and Advanced pathways at a boundary level;
- how legacy content is being migrated;
- how in-class time should be used;
- which documents own detailed implementation work.

Detailed activities belong in the external Activity Bank project. Detailed facilitation guidance belongs in `../publish/mfb-bd-26.10/mfb-bd-eg-26.10.md`; `10_educator-plan.md` is the supporting structure plan. Detailed objectives belong in `05_objectives.md`. App question-bank structure belongs in `12_microlearning-plan.md`. Advanced module ideas, follow-on pathway notes, and redacted legacy content for later use belong in `15_advanced.md`.

`06_plan.md` is the active plan source of truth. The older duplicated plan file has been archived at `../y_archive/y_13_plan_superseded.md`.

---

# 1. Design Decision Summary

The redesigned Diploma should be shorter, clearer, more practical, and easier to teach while preserving the open-source, community-led, Bitcoin-only identity of the original Diploma.

Current design commitments:

- educator-facilitated delivery in person or online;
- low-tech, offline-capable print/PDF instructional content, with no app, device, or connectivity requirement for learning, assessment, completion, or certification;
- an approximately 8-hour delivery pathway that includes required teaching, practice, assessment, feedback, and recording;
- 4 modules that may be delivered in four two-hour sessions, eight one-hour sessions, or another schedule that preserves the learning sequence and required evidence;
- Core, Custom, and Advanced content separation;
- shared Core theory and outcomes with localized, educator-led practice;
- English-first drafting with simplicity, tone, style, terminology, and translation-readiness review before translation or publication;
- practical learning in every module;
- a separate Activity Bank;
- an Educator Guide designed for facilitation, pacing, adaptation, and safety;
- a combined theoretical and practical assessment model tied directly to the learning objectives;
- a 50% educator-led theoretical and 50% educator-observed practical assessment allocation;
- optional app-based microlearning for recap, self-checks, discovery, and connection to My First Bitcoin updates;
- educator-evaluated theory evidence through approved objective-aligned interactions; other educator-led theory work remains formative;
- practical assessment directly evaluated by an educator, with observation concentrated in Modules 3 and 4;
- Advanced technical material outside the beginner pathway;
- sparse QR code use in printed learner materials;
- future instructional branches documented without changing Core outcomes: online PDF, online cohort, self-paced, web, optional app self-assessment support, and cross-modal continuation. The app remains an optional self-assessment resource, not an assessment feature.

The public explanation is simple:

The Diploma is being reorganized, not replaced.

---

# 2. Four-Module Architecture

| Module | Role | Title | Core question |
|---|---|---|---|
| 1 | Problem | Broken Money | How can money break? |
| 2 | Solution | Bitcoin | Why was Bitcoin created, and how does it respond? |
| 3 | Action | Self-custody | How do I take responsibility for using and securing Bitcoin? |
| 4 | Custom | Bitcoin as Money | How can Bitcoin function as money in this community? |

## Module 1: Understanding Money

Keep this module focused on money and the problems that can arise in modern money systems.

Core content:

- opening questions about money;
- what money is;
- functions and properties of money;
- barter limitations, including the double coincidence of wants;
- scarcity, time preference, and opportunity cost through essential ideas;
- short history from barter to modern money, including coin debasement as a historical example, the Nixon Shock as a brief historical marker and, where useful, Executive Order 6102 as a clearly labelled U.S.-specific example;
- fiat systems, including central banks, commercial banks, governments, and citizens with a simple role map;
- fractional reserve banking and bank runs as an overview;
- inflation and purchasing power;
- CBDCs as a beginner fiat-system example where appropriate, emphasizing that digital fiat is not the same as decentralized or scarce money.

Outcome:

Learners can explain the money problems Bitcoin responds to.

## Module 2: How Bitcoin Works

Keep this module focused on why Bitcoin exists and what makes it different.

Core content:

- search for digital and decentralized money, including the Cypherpunk context;
- earlier digital-money attempts and influences such as DigiCash, Hashcash, Bit Gold, B-money, BitTorrent, and reusable proof of work in a brief historical survey;
- the double-spend problem in plain language;
- digital scarcity and credible scarcity through core examples;
- Bitcoin origin story and timeline, including the whitepaper, Genesis Block, first transaction, and Pizza Day;
- decentralization;
- users, nodes, and miners as network roles;
- developer, miner, node, and user role boundaries with clear role distinctions;
- proof of work with a simplified process; introduce hash functions only as the mechanism that makes proof of work costly to produce and quick to check, not as a calculation or cryptography lesson;
- finite supply and halving;
- satoshis and unit bias;
- peer-to-peer transfer;
- verifiability;
- the "don't trust, verify" principle as a bridge from public-rule verification to personal safety practice;
- Bitcoin as sound digital money;
- personal responsibility as the bridge into self-custody.

Outcome:

Learners can explain Bitcoin's purpose and how it differs from fiat money.

## Module 3: Using Bitcoin Safely

Keep this module practical and safety-oriented.

Core content:

- wallets as interfaces;
- addresses, keys, and seed phrases;
- custodial and non-custodial use;
- hot and cold wallet distinction;
- wallet recovery and seed phrase testing;
- receiving bitcoin;
- sending bitcoin;
- verification, confirmations, and basic block explorer orientation where they support beginner understanding;
- public-ledger privacy trade-offs as an introductory discussion;
- irreversible transactions and address verification;
- beginner safety practices, including common scams, copy/paste address risks, seed phrase protection, open-source wallet preference, and starting small;
- acquiring and exchanging bitcoin as a concept, not financial advice;
- only the transaction detail needed for responsible beginner use.

Outcome:

Learners can explain beginner self-custody concepts and demonstrate required wallet, transaction, verification, recovery-readiness, and safety actions under approved, supported conditions.

## Module 4: Bitcoin in Your Community

This module is educator-selected.

Educators choose Custom modules because they understand their students, tools, risks, opportunities, and local conditions better than a centralized curriculum can.

Custom modules should usually be practical workshops or demonstrations.

Possible Custom content:

- local wallet tools;
- Lightning payments where locally appropriate;
- custodial Lightning wallet demonstrations where locally appropriate;
- Lightning invoices and Lightning addresses where locally appropriate;
- merchant payments;
- family remittance or cross-border payment comparison;
- nonprofit or community donation scenario;
- underbanked or restricted-access scenario where locally appropriate;
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

Learners can demonstrate at least one approved, educator-assessed way Bitcoin can function as money in local daily life and explain the relevant trade-offs and safety considerations.

Spending is an important possible Module 4 practice, but Module 4 should remain Bitcoin in Your Community because local use may also include earning, saving, receiving, resource discovery, circular economy mapping, merchant discovery, and community problem-solving.

---

# 3. Legacy Content Migration

`../ref/01_bd_202604_contents.csv` was reviewed as a legacy table-of-contents migration map.

Reading rule:

- `CORE` means old content moves into Core Modules 1–3.
- `CUSTOM` means old content becomes educator-selected Module 4 material.
- `ADVANCED` means old content becomes Advanced pathway material.
- `OUT` does not mean deletion when the same item is marked Custom or Advanced.
- In the reviewed table, no section is marked as out-only.
- Daily-life Bitcoin use should become Custom module source material unless a local delivery plan selects it.

Migration summary:

| Destination | Legacy content signal | Redesign decision |
|---|---|---|
| Core Module 1 | money, money history, fiat, early problem framing | Keep beginner monetary foundations and fiat problem material. |
| Core Module 2 | decentralized currency search, Bitcoin origin, Bitcoin benefits | Keep beginner Bitcoin purpose and properties. |
| Core Module 3 | wallet use, receiving, sending, verification, selected technical orientation | Keep practical use and safety material. |
| Custom Module 4 | daily-life Bitcoin use, local tools, Lightning payments, local spending | Move into educator-selected workshops and demonstrations. |
| Advanced | deeper psychology, detailed mining, mempool, detailed transactions, philosophy, future scenarios | Move into Advanced pathways or educator background. |

Split decisions:

- Psychology of money stays in Core as a foundation; deeper behavioral analysis moves to Advanced.
- Nodes and miners stay in Core only as simple roles; technical mechanics move to Advanced.
- Transaction concepts stay in Core only where needed for safe use and verification; detailed models move to Advanced.
- CBDCs may appear briefly in Module 1 or locally in Module 4; policy and technical depth moves to Advanced.
- Lightning distinctions may be introduced briefly, but wallet setup and payment practice normally belongs in Custom.
- Buying and selling bitcoin may appear in Core as a conceptual risk map, but provider-specific practice belongs in Custom.
- Named services, wallets, exchanges, peer-to-peer platforms, and local recommendations should not become global Student Book recommendations.

## Bitcoin For Organizations Cannibalization

`15_advanced.md` is the sole holding authority for material from the retiring `../ref/bitcoin-for-organizations/en` pathway. It records both beginner-safe merge decisions and the larger Advanced source trail.

Beginner merge decision:

- Do not import Organizations chapters into the Student Book.
- Use Organizations material only where it improves existing beginner outcomes.
- Keep the Student Book lean; put misconception handling mostly in `../publish/mfb-bd-26.10/mfb-bd-eg-26.10.md` and scenario practice mostly in the external Activity Bank project or Module 4 Custom templates.

Organizations content may support:

- Module 1: CBDCs as digital fiat and a trust/control comparison.
- Module 2: digital scarcity, double spending, short technical lineage, credible scarcity, protocol/layers framing, and role boundaries among developers, miners, nodes, and users.
- Module 3: confirmations, explorer orientation, public-ledger transparency, irreversible settlement, and privacy trade-offs.
- Module 4: local merchant, remittance, nonprofit, underbanked-access, circular-economy, on-ramp, and off-ramp scenarios.
- Educator Guide: misconception prompts and claim/evidence/trade-off facilitation.
- Activity Bank: ledger exploration, local payment path comparison, community donation scenarios, and local resource mapping.

Organizations content should not become beginner Core when it requires:

- treasury strategy;
- investment management;
- legal, tax, accounting, AML, KYC, or compliance instruction;
- institutional custody vendor selection;
- organizational risk registers as required learner work;
- government policy strategy;
- sector-by-sector business analysis;
- AI payments;
- on-chain market indicators;
- detailed cryptography, reorg math, or protocol governance.

## Publication Guardrails

Fact-check rule:

Current-data examples must be verified, dated, cited, or replaced with evergreen explanations before publication. This includes CBDC country counts, bitcoin mined-supply figures, large-transaction fee examples, Visa transaction comparisons, Lightning capacity or speed claims, fee amounts, provider names, legal or tax statements, energy-use claims, merchant maps, nonprofit examples, company examples, holder estimates, and organizational adoption claims.

Tone and claims rule:

Preserve the Diploma's conviction, clarity, and Bitcoin-only identity, but avoid turning interpretive claims into unsupported facts. Where a claim is likely to invite disagreement or depend on context, prefer guided comparison, claim/evidence/reasoning prompts, or local discussion.

Print QR rule:

Printed PDFs should use QR codes sparingly. QR codes should point only to stable, high-value destinations such as the source repository, canonical update page, educator resources, support or donation page, or certificate verification if available.

Multilingual source rule:

Draft source material in English first. Before translation or publication, review the English source for beginner readability, simple sentence structure, consistent tone and style, terminology and glossary alignment, ambiguity, idioms, and culturally narrow references. After translation, review each language version for preserved meaning, simple language, appropriate tone, terminology consistency, and local appropriateness.

Delivery-branch rule:

Low-tech, offline-capable print/PDF is the first content-publication mode and may support in-person facilitation or online facilitation. Online PDF, online cohort, self-paced, web, optional app self-assessment support, and cross-modal versions should branch from the same Core outcomes rather than become separate curricula. The My First Bitcoin app is optional in 2026.10 and may be used for recap, self-checks, discovery, and updates.

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

Custom completes Module 4.

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

Advanced module ideas, follow-on pathway notes, and redacted legacy content for later use are collected in `15_advanced.md`.

Advanced outcomes are ongoing and should be designed module by module after the redesigned beginner Diploma is published.

Advanced content should not overload the beginner pathway. It may later become optional extensions, separate workshops, educator background, or follow-on courses.

---

# 5. In-Class Time Rules

Class time should be used for learning that benefits from live facilitation.

Begin time planning with the objectives, required practice, and assessment evidence. Do not shorten or waive these merely to fit a one- or two-hour session; schedule a follow-up when necessary. Educators may assign the relevant Student Book chapter or optional app recap before class, but must not make pre-reading, a learner-owned device, app use, or continuous connectivity a condition for Core instruction.

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

Each module should close with a short review point. The review should include key takeaways, a learner explanation prompt, a link to the next module, and an evidence-of-learning opportunity that can connect to `11_assessment.md`.

Suggested delivery sequencing belongs in the Educator Guide. It can divide Module 1 into money foundations and modern fiat-system trade-offs, and Module 3 into custody foundations and transaction verification/safety, while preserving educator choice about activities and local pacing.

Each module should follow a simple rhythm:

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
| Overview of users, nodes, miners, and proof of work | Detailed mining mechanics, mempool, transaction lifecycle |
| Wallets, addresses, keys, seed phrases, custody trade-offs, wallet recovery basics, and seed phrase testing | Advanced custody models and operational security |
| Receiving, sending, verification, address checking, beginner safety, scam awareness, and start-small guidance | Advanced troubleshooting and technical analysis |
| Beginner acquiring and exchanging pathways as risk orientation | Named provider recommendations, live exchange setup, deep KYC/no-KYC trade-off analysis, and tax/legal advice |
| High-level distinctions between on-chain and Lightning | Lightning channel mechanics, routing, liquidity, and node operations |
| Local daily-life Bitcoin use as Custom source material | Fixed global requirements for specific local tools, merchants, exchanges, or communities |
| Guided discussion and practical orientation | Full activity instructions, facilitation scripts, and optional extensions |

Activities leave the main student-facing text and move to the external Activity Bank project.

Educator preparation, timing, adaptation, misconception support, and debrief guidance move to `../publish/mfb-bd-26.10/mfb-bd-eg-26.10.md`.

---

# 7. Material Ownership

| Material | Owner document |
|---|---|
| Student Guide publication draft | `../publish/mfb-bd-26.10/mfb-bd-sg-26.10.md` |
| Learning objectives and competencies | `05_objectives.md` |
| Activity categories and activity template | the external Activity Bank project |
| Educator facilitation and Custom selection guidance | `../publish/mfb-bd-26.10/mfb-bd-eg-26.10.md` |
| Combined assessment, objective-aligned evidence, and passing requirements | `11_assessment.md` |
| App microlearning question-bank structure | `12_microlearning-plan.md` |
| Two-part assessment prerequisite for certification and governance questions | `13_certification.md` |
| Diploma overview for collaborators and stakeholders | `14_spec.md` |
| Organizations merge decisions and Advanced source trail | `15_advanced.md` |
| Advanced module ideas and redacted content collection | `15_advanced.md` |
| Public keynote and stakeholder brief | `../public/MFB-BD-Keynote.md` |

---

# 8. October 2026 Output

The October 2026 redesign should produce:

- a 4-module beginner Diploma;
- an approximately 8-hour delivery path;
- clear learning objectives;
- Student Guide;
- Educator Guide;
- Activity Bank;
- Custom module templates;
- educator-led theoretical and practical certification-prerequisite framework, with optional app recap and self-check resources;
- publication-ready source files;
- public communication materials.

The Diploma should remain the entry point into a wider learning ecosystem, not the container for every valuable Bitcoin topic.

---

# 9. Follow-On Pathways

Follow-on pathway ideas are collected in `15_advanced.md`.

---

# 10. Open Decisions

The redesign still needs decisions on:

- final Custom module options;
- minimum Custom module templates for October 2026;
- minimum required practical tasks;
- how much learner-facing prose should appear in the Student Book versus educator-led explanation;
- whether sats should be introduced primarily in Module 2 or Module 3;
- which safety practices are required Core versus optional Custom;
- which named tools or services may appear in published materials, and where;
- final QR code destination list for print materials;
- delivery-mode branch requirements for online PDF, online cohort, self-paced, web, optional app self-assessment support, and cross-modal continuation;
- multilingual glossary readiness;
- ownership and approval criteria for English-source simplicity and translation-readiness review;
- ownership and approval criteria for post-translation language review;
- optional app self-assessment question-bank maintenance and learner-feedback requirements;
- educator theory-interaction and practical tasks, rubrics, training, calibration, moderation, and reassessment rules;
- certificate governance and future verification options, including possible on-chain timestamping;
- low-connectivity delivery assumptions;
- pilot and educator review process;
- exact publication formats;
- Advanced module objectives and sequencing, tracked in `15_advanced.md`.

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
