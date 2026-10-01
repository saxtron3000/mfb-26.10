# Published Content Coverage Register

## Purpose

This register makes the relationship between the official curriculum-content files in `publish/` and the planning authorities in `workspace/` explicit. It is the completeness check for the publication package: every curriculum-content file must appear here, have a planning home, and be reviewed when either its content or its publication role changes. Repository metadata files are not curriculum content.

This is an inventory and decision record, not a second copy of learner or educator prose. The linked planning document owns the curriculum decision; the linked publication file remains the official released text or data. Detailed activity procedures remain in their published activity files and may also be made available through the Resources Hub.

The 2026.10 set is a framework-first publication. It includes the teaching and assessment framework without asserting that every educator or local route is ready for certificated delivery. Certification is decentralized and educator-issued; a certificate records the named educator's judgment and is not a centrally issued or verified guarantee from My First Bitcoin.

## Coverage rules

- A published item may support more than one module, but its primary module or role must be stated.
- Existing legacy activity procedures are candidates for review and adaptation, not automatically approved assessment tasks or global tool recommendations.
- Activities involving live tools, videos, accounts, wallets, personal devices, real funds, or secrets require the low-tech, privacy, safety, and current-content checks in `10_activities.md`, `12_educator-plan.md`, and `16_spec.md` before delivery.
- The optional app question data is learner-owned self-review only. It does not provide evidence for assessment, certification, educator tracking, or a pass/fail result.
- Advanced publication remains a placeholder until an Advanced module is approved; `17_advanced.md` is the complete planning inventory and source trail.

## Diploma publication set

| Published file | Content covered | Planning home and decision |
|---|---|---|
| [`mfb-bd-sg-26.10.md`](../publish/mfb-bd-26.10/mfb-bd-sg-26.10.md) | Learner-facing introduction, delivery and safety expectations, four-module pathway, Modules 1–4, next steps, and support or verification references. | `06_plan.md` owns architecture and boundaries; `07_contents.md` owns the learner-content structure; `05_competencies.md`, `08_assets.md`, `09_resources.md`, and `16_spec.md` supply the related planning controls. |
| [Educator Guide](../publish/mfb-bd-26.10/mfb-bd-eg-26.10.md) | Educator preparation, four-module facilitation, safety, activity selection, localization, delivery adaptation, operational assessment protocol, templates, and course close-out. | `12_educator-plan.md` owns the guide structure; `13_assessment.md` and `15_certification.md` own assessment and certification policy; `10_activities.md` owns activity boundaries. |
| [`mfb-bd-assessment-grid-26.10.md`](../publish/mfb-bd-26.10/mfb-bd-assessment-grid-26.10.md) | Competency reference, educator notes, and cohort-level assessment record. | `05_competencies.md` owns criteria; `13_assessment.md` owns evidence and passing rules; `15_certification.md` owns eligibility and governance. |
| [`mfb-bd-qs-26.10.md`](https://programs.myfirstbitcoin.org/programs/bitcoin-diploma/en/educator-quick-start/) | [Educator Quick Start](https://programs.myfirstbitcoin.org/programs/bitcoin-diploma/en/educator-quick-start/) for minimum timing, facilitation, wallet guidance, assessment, framework-first release status, and decentralized educator-issued certification. | `12_educator-plan.md` owns educator structure; `13_assessment.md` and `15_certification.md` own assessment and certification policy; `16_spec.md` owns the release boundary. |
| [`mfb-lx-26.10-index.md`](../publish/mfb-lx-26.10-index.md) | Beginner definitions for Modules 1–4, including money, Bitcoin mechanics, safe use, and local-community terms. | `07_contents.md` owns learner-content coverage; `06_plan.md` owns module boundaries; `12_educator-plan.md` owns educator-facing terminology and misconception checks. |
| [`README.md`](../publish/mfb-adv-26.10/README.md) | Advanced-modules publication placeholder. | `17_advanced.md` owns the advanced inventory, pathway ideas, parked content, and publication readiness. |

## Optional microlearning publication set

| Published file | Content covered | Planning home and decision |
|---|---|---|
| [`mfb-ml-26.10.md`](../publish/mfb-ml-26.10/mfb-ml-26.10.md) | October developer handoff: one 12-item self-check, with short and long alternatives for money, Bitcoin, and safe-use concepts in Modules 1–3. | `14_microlearning-plan.md` owns app purpose, item rules, implementation constraints, topic bank, and non-assessment boundary. |
| [`mfb-ml-26.10-short-questions.csv`](../publish/mfb-ml-26.10/mfb-ml-26.10-short-questions.csv) | CSV export of the 12 short item variants (`BD-ML-01S`–`BD-ML-12S`), including options, correct answers, explanations, and Student Guide review references. | `14_microlearning-plan.md`; the CSV must remain semantically identical to the short-question table in `mfb-ml-26.10.md`. |
| [`mfb-ml-26.10-long-questions.csv`](../publish/mfb-ml-26.10/mfb-ml-26.10-long-questions.csv) | CSV export of the 12 long item variants (`BD-ML-01L`–`BD-ML-12L`), including options, correct answers, explanations, and Student Guide review references. | `14_microlearning-plan.md`; the CSV must remain semantically identical to the long-question table in `mfb-ml-26.10.md`. |

## Activity publication set

The following files are the published Activity Library. Their full procedures, materials, discussion prompts, notes, and linked resources are covered by this register and governed by `10_activities.md`. The module assignment below is a planning placement for review and use; it does not turn an activity into required curriculum or formal assessment.

| ID and published activity | Primary planning placement | Content and planning disposition |
|---|---|---|
| [`001 — Auction`](../publish/mfb-act-26.10/mfb-act-001-auction.md) | Module 1 | Money-supply and pricing game; review inflation wording and distinguish monetary inflation from price changes. |
| [`002 — Consensus`](../publish/mfb-act-26.10/mfb-act-002-consensus.md) | Module 2 | Leaderless group synchronization and Bitcoin consensus simulation; use as a simplified model, not a complete protocol explanation. |
| [`003 — Exploring the Mempool`](../publish/mfb-act-26.10/mfb-act-003-exploring-the-mempool.md) | Advanced or educator extension | Block, transaction, and mempool explorer orientation; live-tool and current-data dependent, so not required beginner content. |
| [`004 — Fractional Reserve Banking`](../publish/mfb-act-26.10/mfb-act-004-fractional-reserve-banking.md) | Module 1 | Bank lending and money-supply simulation; debrief liquidity, solvency, and local-system limits without overclaiming. |
| [`005 — Iterative Barter Game`](../publish/mfb-act-26.10/mfb-act-005-iterative-barter-game.md) | Module 1 | Barter, coincidence of wants, and salability game; supports why money emerges. |
| [`006 — Lightning Relay Race`](../publish/mfb-act-26.10/mfb-act-006-lightning-relay-activity.md) | Module 4 | Live Lightning payment relay using an educator-approved low-stakes real-wallet route. |
| [`007 — Transactions in Action`](../publish/mfb-act-26.10/mfb-act-007-transactions-in-action.md) | Module 2 | Live low-stakes on-chain payment practice connecting wallet authorization and receipt to node and miner roles. |
| [`008 — Why Do We Need Money?`](../publish/mfb-act-26.10/mfb-act-008-why-do-we-need-money.md) | Module 1 | Opening discussion about money, value, control, and learner questions. |
| [`009 — What Is Money?`](../publish/mfb-act-26.10/mfb-act-009-what-is-money.md) | Module 1 | Currency-versus-token comparison using candy and fiat or play money; localize the materials. |
| [`010 — Time Preference`](../publish/mfb-act-26.10/mfb-act-010-time-preference.md) | Module 1 or Advanced extension | Immediate-versus-delayed reward discussion; keep participation voluntary and avoid behavioural or financial claims. |
| [`011 — Alternative Time Preference Questions`](../publish/mfb-act-26.10/mfb-act-011-alternative-time-preference-questions.md) | Module 1 or Advanced extension | Discussion prompts on time preference, saving, and consumption; optional enrichment only. |
| [`012 — Barter Game`](../publish/mfb-act-26.10/mfb-act-012-barter-game.md) | Module 1 | Have/want-card barter, followed by commodity-money comparison; supports the coincidence-of-wants concept. |
| [`013 — Consequences of the Fiat System`](../publish/mfb-act-26.10/mfb-act-013-consequences-of-the-fiat-system.md) | Module 1 | Socratic discussion of local and social fiat-system consequences; frame claims as discussion and evidence questions. |
| [`014 — Additional Socratic Questions`](../publish/mfb-act-26.10/mfb-act-014-additional-socratic-questions.md) | Module 1–2 bridge | Discussion of education, centralized power, decentralization, and Bitcoin; facilitate disagreement safely. |
| [`015 — Consensus Building in a Peer-to-Peer Network`](../publish/mfb-act-26.10/mfb-act-015-consensus-peer-to-peer-network.md) | Module 2 or Advanced extension | Message-passing, adversarial-node, cryptography, and consensus activity; simplify for beginners and keep technical depth out of the core. |
| [`016 — Is Bitcoin Sound Money?`](../publish/mfb-act-26.10/mfb-act-016-is-bitcoin-sound-money.md) | Module 2 | Money-properties comparison including Bitcoin; present “sound money” as a reasoned judgment, not a promise. |
| [`017 — Evaluate Bitcoin Wallets`](../publish/mfb-act-26.10/mfb-act-017-evaluate-bitcoin-wallets.md) | Module 3 or Module 4 | Wallet research and selection exercise; use local, checked examples without a global recommendation or required account. |
| [`018 — Creating Your First Bitcoin Wallet`](../publish/mfb-act-26.10/mfb-act-018-creating-your-first-bitcoin-wallet.md) | Module 3 | Wallet creation or recovery practice; use prepared conditions and never collect or expose learner secrets. |
| [`019 — Bitcoin Transactions in Action`](../publish/mfb-act-26.10/mfb-act-019-bitcoin-transactions-in-action.md) | Module 2–3 bridge | Sender, receiver, node, and miner transaction role-play; supports basic verification and validation concepts. |
| [`020 — Verification`](../publish/mfb-act-26.10/mfb-act-020-verification.md) | Module 2 | Dice model of proof of work and node verification; explicitly mark it as an analogy. |
| [`021 — Watch: Future of Bitcoin: Lightning Network`](../publish/mfb-act-26.10/mfb-act-021-watch-future-of-bitcoin-lightning-network.md) | Module 4 or optional extension | Lightning video discussion; provide an offline equivalent and recheck availability and claims. |
| [`022 — Watch: How Bitcoin Works under the Hood`](../publish/mfb-act-26.10/mfb-act-022-watch-how-bitcoin-works-under-the-hood.md) | Module 2 or Advanced extension | Technical Bitcoin video; optional only and bounded to beginner role and system concepts. |
| [`023 — Watch: Explain Bitcoin to Complete Beginners`](../publish/mfb-act-26.10/mfb-act-023-watch-explain-bitcoin-to-complete-beginners.md) | Module 2 | Non-technical Bitcoin overview video; optional with a facilitated, offline explanation alternative. |
| [`024 — Generate SHA-256 Hash`](../publish/mfb-act-26.10/mfb-act-024-generate-sha-256-hash.md) | Advanced or educator extension | Online hash demonstration; not required beginner content and requires a no-tool explanation. |
| [`025 — Watch: Blockchain 101 – A Visual Demo`](../publish/mfb-act-26.10/mfb-act-025-watch-blockchain-101-visual-demo.md) | Module 2 or Advanced extension | Visual blockchain video, offered as an optional alternative to the hash activity; provide an offline equivalent. |
| [`026 — Watch: How To Setup Bitcoin Core`](../publish/mfb-act-26.10/mfb-act-026-watch-bitcoin-nodes.md) | Module 2 or Advanced extension | Node video on validation and local blockchain copies; keep role explanation simple and recheck availability. |
| [`027 — Watch: Why Every Bitcoiner Should Run Their Own Node`](../publish/mfb-act-26.10/mfb-act-027-watch-why-run-a-bitcoin-node.md) | Advanced or educator extension | Node-running video; do not imply running a node is a Diploma requirement. |
| [`028 — Watch: Bitcoin Is Generational Wealth`](../publish/mfb-act-26.10/mfb-act-028-watch-bitcoin-is-generational-wealth.md) | Optional reflection or Advanced extension | Values-oriented film; facilitate critical discussion and do not treat wealth claims as financial guidance. |
| [`029 — Watch: How Money & Banking Work`](../publish/mfb-act-26.10/mfb-act-029-watch-how-money-and-banking-work.md) | Module 1 | Money and banking video; optional with checked current context and an offline explanation alternative. |
| [`030 — Final Class Discussion: How Did Your Perspective Change?`](../publish/mfb-act-26.10/mfb-act-030-final-class-discussion.md) | Module 4 close | Reflection on changed understanding and next steps; formative unless an approved evidence route says otherwise. |

## Maintenance check

When a curriculum-content file is added, removed, renamed, or materially changed in `publish/`:

1. update this register in the same change;
2. check the named planning authority for coverage and consistency;
3. add or revise a planning decision if the publication introduces new content, a new tool, a current-data claim, or an assessment implication;
4. update `00_index.md` if the publication package or reading order changes; and
5. verify that every curriculum-content file in `publish/` has a working link and appears once in this register.
