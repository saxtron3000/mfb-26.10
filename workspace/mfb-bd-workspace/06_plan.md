# Bitcoin Diploma Redesign Plan

## Purpose

This is the source of truth for the current Bitcoin Diploma redesign structure.

It defines:

- the 4-module architecture
- what belongs in the complete four-module Bitcoin Diploma, how educators adapt Modules 3–4 within it, and what belongs in [Advanced Learning](https://curriculum.myfirstbitcoin.org/programs/advanced-modules/)
- how legacy content is being migrated
- how in-class time should be used
- which documents own detailed implementation work

`10_activities.md` defines activity boundaries, quality requirements, and release priorities; detailed activities are available on the [Resources Hub](https://programs.myfirstbitcoin.org/resources/). Detailed facilitation guidance belongs in the [Educator Guide](../publish/mfb-bd-26.10/mfb-bd-eg-26.10.md); `12_educator-plan.md` is the supporting structure plan. The detailed competency framework and observable criteria belong in `05_competencies.md`. Restricted-pilot app question-bank structure belongs in `14_microlearning-plan.md`. [Advanced module](https://curriculum.myfirstbitcoin.org/programs/advanced-modules/) ideas, follow-on pathway notes, and redacted legacy content for later use belong in `17_advanced.md`.

`06_plan.md` is the active plan source of truth. The older duplicated plan file has been archived at `../y_archive/y_13_plan_superseded.md`.

---

# 1. Design Decision Summary

The redesigned Bitcoin Diploma should be shorter, clearer, more practical, and easier to teach while preserving the open-source, community-led, Bitcoin-only identity of the original Bitcoin Diploma.

Current design commitments:

- educator-facilitated delivery in person or online
- low-tech, offline-capable print/PDF instructional content, with no app, device, or connectivity requirement for learning, assessment, completion, or certification
- a minimum 8-hour delivery pathway that includes required teaching, practice, assessment, feedback, and recording, with no upper limit when learners need more time
- 4 modules that may be delivered in four two-hour sessions, eight one-hour sessions, or another schedule that gives learners appropriate time and preserves the learning sequence and required evidence
- all four required Bitcoin Diploma modules, with educator-adapted practical learning in Modules 3–4 and [Advanced Learning](https://curriculum.myfirstbitcoin.org/programs/advanced-modules/) outside the Bitcoin Diploma
- shared Modules 1–2 core learning, with educator-adapted Module 3 practice and educator-curated Module 4 Connect practice
- English-first drafting with simplicity, tone, style, terminology, and translation-readiness review before translation or publication
- practical learning in every module
- activities available on the [Resources Hub](https://programs.myfirstbitcoin.org/resources/)
- an Educator Guide designed for facilitation, pacing, adaptation, and safety
- a combined theoretical and practical assessment model tied directly to assessed competencies and observable criteria
- an operational assessment protocol in the Educator Guide with the approved evidence crosswalk, theory interactions, practical tasks, rubrics, support rules, equivalent routes, reassessment, calibration, and moderation
- a 50% educator-led theoretical and 50% educator-observed practical assessment allocation
- restricted-pilot app-based microlearning for recap, self-checks, discovery, and connection to My First Bitcoin updates; it is not a normal Bitcoin Diploma resource. The public app is not released with this publication; any learner-facing guide coverage is a later post-publication addition, governed by `18_horizon.md`
- educator-evaluated theory evidence through approved competency-aligned interactions; other educator-led theory work remains formative
- practical assessment directly evaluated by an educator, with observation concentrated in Modules 3 and 4
- Advanced technical material outside the beginner pathway
- sparse QR code use in printed learner materials
- a short set of direct, named My First Bitcoin programme links as optional further learning, never as required Bitcoin Diploma instruction, practice, assessment, or certification
- October publication outputs that include the offline-capable print/PDF package, online PDF, and website-ready content published through Sanity
- future instructional branches documented without changing required Bitcoin Diploma competency standards: online cohort, self-paced, app-supported self-assessment, and cross-modal continuation. Restricted-pilot app use is not an assessment feature or a normal Bitcoin Diploma resource

The public explanation is simple:

The Bitcoin Diploma is being reorganized, not replaced.

---

# 2. Four-Module Architecture

| Module | Role | Title | Guiding question |
|---|---|---|---|
| 1 | Problem | Broken Money | How can money break? |
| 2 | Solution | Bitcoin | Why was Bitcoin created, and how does it respond? |
| 3 | Action | Self-custody | How do I take responsibility for using and securing Bitcoin? |
| 4 | Connect | Bitcoin in Your Community | How do the problem, solution, and safe action connect to this community? |

The four modules form one learning arc: **Problem → Solution → Action → Connect**. Module 4 is not an optional add-on or a generic spending lesson. It connects the shared learning from Modules 1–3 to a locally relevant need or opportunity, compares the Bitcoin path with a realistic alternative, supports safe practical action, and ends with a responsible next step. A learner may reasonably conclude that a particular path is not suitable in their context.

## Module 1: Understanding Money

Keep this module focused on money and the problems that can arise in modern money systems.

Bitcoin Diploma content:

- opening questions about money
- what money is
- functions and properties of money
- barter limitations, including the double coincidence of wants
- scarcity, time preference, and opportunity cost through essential ideas
- short history from barter to modern money, including coin debasement as a historical example, the Nixon Shock as a brief historical marker and, where useful, Executive Order 6102 as a clearly labelled U.S.-specific example
- fiat systems, including central banks, commercial banks, governments, and citizens with a simple role map
- fractional reserve banking and bank runs as an overview
- inflation and purchasing power
- CBDCs as a beginner fiat-system example where appropriate, emphasizing that digital fiat is not the same as decentralized or scarce money

Observable competency:

Learners can explain the money problems Bitcoin responds to.

## Module 2: How Bitcoin Works

Keep this module focused on why Bitcoin exists and what makes it different.

Bitcoin Diploma content:

- search for digital and decentralized money, including the Cypherpunk context
- earlier digital-money attempts and influences such as DigiCash, Hashcash, Bit Gold, B-money, BitTorrent, and reusable proof of work in a brief historical survey
- the double-spend problem in plain language
- digital scarcity and credible scarcity through key examples
- Bitcoin origin story and timeline, including the whitepaper, Genesis Block, first transaction, and Pizza Day
- decentralization
- users, nodes, and miners as network roles
- developer, miner, node, and user role boundaries with clear role distinctions
- proof of work with a simplified process; introduce hash functions only as the mechanism that makes proof of work costly to produce and quick to check, not as a calculation or cryptography lesson
- finite supply and halving
- satoshis and unit bias
- peer-to-peer transfer
- verifiability
- the "don't trust, verify" principle as a bridge from public-rule verification to personal safety practice
- Bitcoin as sound digital money
- personal responsibility as the bridge into self-custody

Observable competency:

Learners can explain Bitcoin's purpose and how it differs from fiat money.

## Module 3: Using Bitcoin Safely

Keep this module practical and safety-oriented.

Bitcoin Diploma content:

- wallets as interfaces
- addresses, keys, and seed phrases
- custodial and non-custodial use
- hot and cold wallet distinction
- wallet recovery and seed phrase testing
- receiving bitcoin
- sending bitcoin
- verification, confirmations, and basic block explorer orientation where they support a beginner explanation or safe action
- public-ledger privacy trade-offs as an introductory discussion
- irreversible transactions and address verification
- beginner safety practices, including common scams, copy/paste address risks, seed phrase protection, open-source wallet preference, and starting small
- acquiring and exchanging bitcoin as a concept, not financial advice
- only the transaction detail needed for responsible beginner use

Observable competency:

Learners can explain beginner self-custody concepts and demonstrate required wallet, transaction, verification, recovery-readiness, and safety actions under approved, supported conditions.

## Module 4: Bitcoin in Your Community

This required Bitcoin Diploma module is educator-curated.

It is the **Connect** stage of the Problem → Solution → Action → Connect learning arc. It brings the earlier shared learning into a locally relevant comparison and safe practical task; it does not require Bitcoin adoption or endorse a local provider.

Educators curate Module 4 because they know their students, local constraints, solutions, tools, resources, risks, opportunities, and conditions better than a centralized curriculum can.

Module 4 should usually use practical workshops or demonstrations.

Possible Module 4 content:

- local wallet tools
- Lightning payments where locally appropriate
- custodial Lightning wallet demonstrations where locally appropriate
- Lightning invoices and Lightning addresses where locally appropriate
- merchant payments
- family remittance or cross-border payment comparison
- nonprofit or community donation scenario
- underbanked or restricted-access scenario where locally appropriate
- everyday purchase scenarios
- local spending and receiving scenarios
- buying and selling bitcoin in the community
- KYC and no-KYC trade-offs where locally appropriate
- exchanges, peer-to-peer exchange, earning bitcoin, and Bitcoin ATMs as local pathway examples
- local resource maps
- BTCMap or equivalent local-resource discovery
- circular economies
- local Bitcoin communities
- local monetary problems
- CBDCs in the local context
- community-specific Bitcoin use cases

Observable competency:

Learners can demonstrate at least one approved, educator-assessed way Bitcoin can function as money in local daily life and explain the relevant trade-offs and safety considerations.

Spending is an important possible Module 4 practice, but Module 4 should remain Bitcoin in Your Community because local use may also include earning, saving, receiving, resource discovery, circular economy mapping, merchant discovery, and community problem-solving.

---

# 3. Legacy Content Migration

`../ref/01_bd_202604_contents.csv` was reviewed as a legacy table-of-contents migration map.

Reading rule:

- The legacy shared-module label identifies content that now moves into Modules 1–3 within the Bitcoin Diploma.
- A legacy local-module label identifies educator-curated Module 4 material, which remains required Bitcoin Diploma learning.
- `ADVANCED` means old content becomes Advanced pathway material.
- `OUT` does not mean deletion when the same item has a Module 4 or Advanced destination.
- In the reviewed table, no section is marked as out-only.
- Daily-life Bitcoin use should become Module 4 source material unless a local delivery plan selects it.

Migration summary:

| Destination | Legacy content signal | Redesign decision |
|---|---|---|
| Bitcoin Diploma Module 1 | money, money history, fiat, early problem framing | Keep beginner monetary foundations and fiat problem material. |
| Bitcoin Diploma Module 2 | decentralized currency search, Bitcoin origin, Bitcoin benefits | Keep beginner Bitcoin purpose and properties. |
| Bitcoin Diploma Module 3 | wallet use, receiving, sending, verification, selected technical orientation | Keep practical use and safety material. |
| Bitcoin Diploma **Module 4: educator-curated Connect** | daily-life Bitcoin use, local tools, Lightning payments, local spending | Move into educator-curated workshops and demonstrations within the Bitcoin Diploma. |
| Advanced | deeper psychology, detailed mining, mempool, detailed transactions, philosophy, future scenarios | Move into [Advanced Modules](https://curriculum.myfirstbitcoin.org/programs/advanced-modules/) or educator background. |

Split decisions:

- Psychology of money stays in the Bitcoin Diploma as a foundation; deeper behavioral analysis moves to Advanced.
- Nodes and miners stay in the Bitcoin Diploma only as simple roles; technical mechanics move to Advanced.
- Transaction concepts stay in the Bitcoin Diploma only where needed for safe use and verification; detailed models move to Advanced.
- CBDCs may appear briefly in Module 1 or locally in Module 4; policy and technical depth moves to Advanced.
- Lightning distinctions may be introduced briefly, but wallet setup and payment practice normally belongs in Module 4.
- Buying and selling bitcoin may appear in the Bitcoin Diploma as a conceptual risk map, but provider-specific practice belongs in Module 4.
- Named services, wallets, exchanges, peer-to-peer platforms, and local recommendations should not become global Student Book recommendations.

## Bitcoin For Organizations Cannibalization

`17_advanced.md` is the sole holding authority for material from the retiring `../ref/bitcoin-for-organizations/en` pathway. It records both beginner-safe merge decisions and the larger Advanced source trail.

Beginner merge decision:

- Do not import Organizations chapters into the Student Book.
- Use Organizations material only where it improves existing beginner competencies or observable criteria.
- Keep the Student Book lean; put misconception handling mostly in the [Educator Guide](../publish/mfb-bd-26.10/mfb-bd-eg-26.10.md) and scenario practice mostly in activities on the [Resources Hub](https://programs.myfirstbitcoin.org/resources/) or educator-curated Module 3–4 templates.

Organizations content may support:

- **Module 1: CBDCs as digital fiat and a trust/control comparison**.
- **Module 2: digital scarcity, double spending, short technical lineage, credible scarcity, protocol/layers framing, and role boundaries among developers, miners, nodes, and users**.
- **Module 3: confirmations, explorer orientation, public-ledger transparency, irreversible settlement, and privacy trade-offs**.
- **Module 4: local merchant, remittance, nonprofit, underbanked-access, circular-economy, on-ramp, and off-ramp scenarios**.
- Educator Guide: misconception prompts and claim/evidence/trade-off facilitation.
- Activities available on the [Resources Hub](https://programs.myfirstbitcoin.org/resources/): ledger exploration, local payment path comparison, community donation scenarios, and local resource mapping.

Organizations content should not become part of the beginner Bitcoin Diploma when it requires:

- treasury strategy
- investment management
- legal, tax, accounting, AML, KYC, or compliance instruction
- institutional custody vendor selection
- organizational risk registers as required learner work
- government policy strategy
- sector-by-sector business analysis
- AI payments
- on-chain market indicators
- detailed cryptography, reorg math, or protocol governance

## Publication Guardrails

Fact-check rule:

Current-data examples must be verified, dated, cited, or replaced with evergreen explanations before publication. This includes CBDC country counts, bitcoin mined-supply figures, large-transaction fee examples, Visa transaction comparisons, Lightning capacity or speed claims, fee amounts, provider names, legal or tax statements, energy-use claims, merchant maps, nonprofit examples, company examples, holder estimates, and organizational adoption claims.

Tone and claims rule:

Preserve the Bitcoin Diploma's conviction, clarity, and Bitcoin-only identity, but avoid turning interpretive claims into unsupported facts. Where a claim is likely to invite disagreement or depend on context, prefer guided comparison, claim/evidence/reasoning prompts, or local discussion.

Print QR rule:

Printed PDFs should use QR codes sparingly. QR codes should point only to stable, high-value destinations such as the source repository, canonical update page, educator resources, support or donation page, or an approved educator or issuer-specific certificate-verification method if available. The [Certificate Tool](https://tools.myfirstbitcoin.org/certificate) is an educator batch-production tool rather than a learner-facing QR destination. Do not imply a central My First Bitcoin verification service.

Multilingual source rule:

Draft source material in English first. Before translation or publication, review the English source for beginner readability, simple sentence structure, consistent tone and style, terminology and glossary alignment, ambiguity, idioms, and culturally narrow references. After translation, review each language version for preserved meaning, simple language, appropriate tone, terminology consistency, and local appropriateness.

Delivery-branch rule:

Low-tech, offline-capable print/PDF, an online PDF, and website-ready content are all October publication outputs. The online PDF and web version are published through Sanity and remain aligned with the same approved source. Restricted-pilot My First Bitcoin App microlearning is available only to the defined pilot group and is not part of normal Bitcoin Diploma delivery. Future online-cohort, self-paced, app-supported self-assessment, and cross-modal instructional branches should grow from the same required Bitcoin Diploma competency standards rather than become separate curricula. Its later public-release work is tracked in `18_horizon.md`.

---

# 4. Four-module Bitcoin Diploma, educator-curated Modules 3–4, and Advanced boundaries

## Bitcoin Diploma

The Bitcoin Diploma consists of Modules 1–4: Problem, Solution, Action, and Connect. Modules 1 and 2 develop theory-based competencies through explanation, comparison, and reasoning. Module 3 develops safe practical action. Module 4 uses that foundation to connect learning to a local need, alternative, practical task, and realistic next step. It is a required Bitcoin Diploma module, curated by educators because they are the subject-matter experts on their students' local constraints, solutions, tools, resources, and context.

The Bitcoin Diploma should include:

- money foundations
- fiat problems
- Bitcoin purpose and key properties
- sats as a beginner unit concept
- beginner custody concepts
- wallet recovery basics
- receiving, sending, and verification orientation
- beginner safety practices, including seed phrase protection, seed phrase testing, scam awareness, address verification, and starting small
- acquiring and exchanging pathways as beginner concepts, not recommendations
- guided discussion and reflection

It must also include one educator-curated Module 4 task with safe practice, verification, explanation, and realistic next steps.

The Bitcoin Diploma should not promise independent mastery of economics, technical systems, or high-stakes custody.

All four modules are part of the Bitcoin Diploma. Modules 1–2 provide the shared core across languages and delivery modes. Educators adapt practical examples, tools, resources, and delivery in Modules 3–4 without lowering competency standards or evidence requirements; in Module 4 they curate the local Connect experience.

## Educator-curated Module 4 within the Bitcoin Diploma

The educator-curated Module 4 completes the Bitcoin Diploma as its **Connect** stage.

Module 4 should:

- be selected by the educator
- connect the Module 1 problem, Module 2 response, and Module 3 safety action to a local need or opportunity
- connect Bitcoin to local daily life
- compare the Bitcoin path with a realistic local alternative without requiring a favorable conclusion
- use tools and resources local bitcoiners actually use
- be guided by educators or local experts who know local risks and learner readiness
- focus on workshops, demonstrations, and local problem-solving
- include safety notes and realistic next steps

Template Module 4 variants should include:

- local problem or opportunity
- Problem → Solution → Action concepts to connect
- realistic existing alternative
- learner profile
- tools or resources
- local legal, tax, and safety context where relevant
- language or terminology notes where relevant
- delivery-mode notes where relevant
- workshop or demonstration
- safety warnings
- educator preparation
- learner task
- evidence of learning
- local adaptation notes

## Advanced

[Advanced module](https://curriculum.myfirstbitcoin.org/programs/advanced-modules/) ideas, follow-on pathway notes, and redacted legacy content for later use are collected in `17_advanced.md`.

Advanced competencies are ongoing and should be designed module by module after the redesigned beginner Bitcoin Diploma is published.

Advanced content should not overload the beginner pathway. It may later become optional extensions, separate workshops, educator background, or follow-on courses.

---

# 5. In-Class Time Rules

Class time should be used for learning that benefits from live facilitation.

Begin time planning with the assessed competencies, observable criteria, required practice, and assessment evidence. Use the Educator Guide's operational assessment protocol capacity check before advertising certification. Do not shorten or waive required evidence merely to fit a one- or two-hour session, and do not treat assessment as an unplanned follow-up outside the advertised Bitcoin Diploma. Educators may require learners to read the relevant Student Guide chapter before class when every learner has accessible language and format options. Pre-reading can preserve live time for activities and discussion, but it does not count toward the minimum eight hours or replace required educator-supported learning and assessment. A learner-owned device, app use, or continuous connectivity must not become a condition for required Bitcoin Diploma instruction.

Prioritize:

- discussion
- questions
- misconception correction
- guided practice
- scenario analysis
- peer explanation
- reflection
- educator-curated Connect learning
- educator-led synthesis

Minimize:

- long readings
- extended lectures
- dense technical background
- long definitions without application
- advanced optional content

Internal performance rule:

Treat the beginner pathway like a lean, high-performance learning experience. Every required component should improve learner clarity, completion likelihood, practice, educator usability, safety, translation readiness, or maintainability.

Each module should close with a short review point. The review should include key takeaways, a learner explanation prompt, a link to the next module, and an evidence-of-learning opportunity that can connect to `13_assessment.md`.

Suggested delivery sequencing belongs in the Educator Guide. It can divide Module 1 into money foundations and modern fiat-system trade-offs, and Module 3 into custody foundations and transaction verification/safety, while preserving educator choice about activities and local pacing.

Each module should follow a simple rhythm:

1. Present the key idea briefly.
2. Elicit an observable learner response.
3. Practice through a scenario, activity, comparison, or demonstration.
4. Ask learners to explain, decide, apply, or reflect.
5. Review the connection to the wider Bitcoin Diploma and capture evidence of learning.

---

# 6. What Stays And What Moves

| Stays in the Bitcoin Diploma | Moves outside the Bitcoin Diploma |
|---|---|
| Money, fiat, inflation, purchasing power | Detailed monetary theory and long policy history |
| Double coincidence of wants, fiat-system roles, fractional reserve banking, bank runs, and brief CBDC orientation | Detailed banking policy, CBDC policy, and long monetary-policy history |
| Bitcoin origin, purpose, properties, finite supply, sats, and beginner timeline | Deep protocol and cryptography detail |
| Overview of users, nodes, miners, and proof of work | Detailed mining mechanics, mempool, transaction lifecycle |
| Wallets, addresses, keys, seed phrases, custody trade-offs, wallet recovery basics, and seed phrase testing | Advanced custody models and operational security |
| Receiving, sending, verification, address checking, beginner safety, scam awareness, and start-small guidance | Advanced troubleshooting and technical analysis |
| Beginner acquiring and exchanging pathways as risk orientation | Named provider recommendations, live exchange setup, deep KYC/no-KYC trade-off analysis, and tax/legal advice |
| High-level distinctions between on-chain and Lightning | Lightning channel mechanics, routing, liquidity, and node operations |
| Local daily-life Bitcoin use as educator-curated Module 4 source material within the Bitcoin Diploma | Fixed global requirements for specific local tools, merchants, exchanges, or communities |
| Guided discussion and practical orientation | Full activity instructions, facilitation scripts, and optional extensions |

Activities leave the main student-facing text and are available on the [Resources Hub](https://programs.myfirstbitcoin.org/resources/).

Educator preparation, timing, adaptation, misconception support, and debrief guidance move to the [Educator Guide](../publish/mfb-bd-26.10/mfb-bd-eg-26.10.md).

---

# 7. Material Ownership

| Material | Owner document |
|---|---|
| Official Student Guide | `../publish/mfb-bd-26.10/mfb-bd-sg-26.10.md` |
| Competency framework and observable criteria | `05_competencies.md` |
| Activity boundaries, quality requirements, and release priorities | `10_activities.md` |
| Activity categories and activity template | [Resources Hub](https://programs.myfirstbitcoin.org/resources/) |
| Educator facilitation and Module 4 selection guidance | [Educator Guide](../publish/mfb-bd-26.10/mfb-bd-eg-26.10.md) |
| Combined assessment, competency-aligned evidence, and passing requirements | `13_assessment.md` |
| Assessment crosswalk, approved interactions and tasks, rubrics, and equivalent routes | [Educator Guide: operational assessment protocol](../publish/mfb-bd-26.10/mfb-bd-eg-26.10.md#operational-assessment-protocol) |
| Restricted-pilot app microlearning question-bank structure | `14_microlearning-plan.md` |
| Two-part assessment prerequisite for certification and governance questions | `15_certification.md` |
| Bitcoin Diploma overview for collaborators and stakeholders | `16_spec.md` |
| Organizations merge decisions and Advanced source trail | `17_advanced.md` |
| [Advanced module](https://curriculum.myfirstbitcoin.org/programs/advanced-modules/) ideas and redacted content collection | `17_advanced.md` |
| Public keynote and stakeholder brief | `../public/MFB-BD-Keynote.md` |

---

# 8. October 2026 Output

The October 2026 redesign should produce:

- a 4-module beginner Bitcoin Diploma
- a minimum 8-hour delivery path, with additional time whenever learners need it and no upper limit
- clear assessed competencies and observable criteria
- Student Guide
- Educator Guide
- activities available on the [Resources Hub](https://programs.myfirstbitcoin.org/resources/)
- educator-curated Module 4 templates
- educator-led theoretical and practical certification-prerequisite framework; restricted-pilot app microlearning remains outside normal Bitcoin Diploma delivery
- offline-capable print/PDF, online PDF, and website-ready outputs published through Sanity
- publication-ready and translation-ready source files
- public communication materials

This is a framework-first release. It publishes the complete teaching package and assessment framework without claiming that every local route is ready for certificated delivery. Before issuing certificates, an educator must have the selected tasks and local variants, capacity, accessibility routes, assessment records, and proportionate local governance ready. After confirming eligibility, an educator may use the [Certificate Tool](https://tools.myfirstbitcoin.org/certificate) to prepare certificates in batches; the tool does not assess learners or decide completion.

The Bitcoin Diploma should remain the entry point into a wider learning ecosystem, not the container for every valuable Bitcoin topic.

---

# 9. Follow-On Pathways

Follow-on pathway ideas are collected in `17_advanced.md`.

---

# 10. Open Decisions

The redesign still needs decisions on:

- final educator-curated Module 4 options
- minimum educator-curated Module 4 templates for October 2026
- minimum required practical tasks
- how much learner-facing prose should appear in the Student Book versus educator-led explanation
- whether sats should be introduced primarily in Module 2 or Module 3
- which safety practices are required throughout the Bitcoin Diploma versus specific to educator-curated Module 3–4 variants
- which named tools or services may appear in published materials, and where
- final QR code destination list for print materials
- delivery-mode branch requirements for online cohort, self-paced, restricted-pilot and later public-app self-assessment support, and cross-modal continuation
- multilingual glossary readiness
- ownership and approval criteria for English-source simplicity and translation-readiness review
- ownership and approval criteria for post-translation language review
- restricted-pilot app self-assessment question-bank maintenance and learner-feedback requirements
- operational-assessment-protocol evidence for task timing, records, calibration, moderation, accessibility equivalents, and educator capacity before certificated delivery
- the available [Certificate Tool](https://tools.myfirstbitcoin.org/certificate) for batch production after educator confirmation, plus optional future verification methods such as privacy-preserving on-chain timestamping, without changing educator-issued certification
- low-connectivity delivery assumptions
- pilot and educator review process
- [Advanced module](https://curriculum.myfirstbitcoin.org/programs/advanced-modules/) competencies and sequencing, tracked in `17_advanced.md`

---

# 11. Working Principle

Use class time for what class time does best:

- conversation
- reasoning
- practice
- feedback
- reflection
- educator-curated Connect learning

Content should support those experiences, not crowd them out.
