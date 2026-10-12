# Review run: 2026-09-30 — ACT-031 annotation-evidence refresh

## Run details

| Field | Record |
| --- | --- |
| Mode | `targeted` |
| Scope | Every `ANN-` evidence link to the Student Guide in `review/review_todo.md`; complete `ACT-031`. |
| Requested by | Repository user |
| Reviewer | Codex |
| Source version | Working-tree snapshot, 2026-09-30. |
| Workspace authority version | `workspace/00_index.md` ownership rules and current Student Guide publication. |
| Scripts used | `review/review_todo-script.md`; `ACT-031` completion check. |
| Started / completed | 2026-09-30 / 2026-09-30 |

## Traceability matrix

| TR-ID | Governing workspace file and heading | Requirement or decision | Expected publication or operational evidence | Actual evidence | State | Verification method and date | Related finding |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ANN-014–015 | Student Guide, Welcome | Mission and community evidence | Current mission passage | [Mission](../../publish/mfb-bd-26.10/mfb-bd-sg-26.10.md:32#our-mission-independent-open-source-bitcoin-education) | implemented | Read in context, 2026-09-30 | ACT-031 |
| ANN-016–035 | Student Guide, How This Diploma Works | Course, participation, and safety evidence | Current headings for learner outcomes, flexible delivery, participation, and safety | [Learner outcomes](../../publish/mfb-bd-26.10/mfb-bd-sg-26.10.md:113#what-learners-will-be-able-to-explain-and-demonstrate-by-the-end), [safety](../../publish/mfb-bd-26.10/mfb-bd-sg-26.10.md:203#safety-responsibility-and-no-financial-advice) | implemented | Each inherited subsection mapped to its current heading, 2026-09-30 | ACT-031 |
| ANN-036–084 | Student Guide, Module 1 | Money-section evidence | Current Module 1 subsection headings | [Module 1](../../publish/mfb-bd-26.10/mfb-bd-sg-26.10.md:262#module-1-understanding-money), [review](../../publish/mfb-bd-26.10/mfb-bd-sg-26.10.md:587#review-how-can-money-break) | implemented | Each inherited subsection mapped to its current heading, 2026-09-30 | ACT-031 |
| ANN-085–124 | Student Guide, Module 2 | Bitcoin-foundations evidence | Current Module 2 subsection headings | [Module 2](../../publish/mfb-bd-26.10/mfb-bd-sg-26.10.md:606#module-2-how-bitcoin-works), [proof of work](../../publish/mfb-bd-26.10/mfb-bd-sg-26.10.md:786#proof-of-work) | implemented | Each inherited subsection mapped to its current heading, 2026-09-30 | ACT-031 |
| ANN-126–168, ANN-239 | Student Guide, Module 3 | Safe-use evidence | Current wallet, payment, and safety headings | [Wallets](../../publish/mfb-bd-26.10/mfb-bd-sg-26.10.md:1027#wallets), [seed phrases](../../publish/mfb-bd-26.10/mfb-bd-sg-26.10.md:1101#seed-phrases), [payment paths](../../publish/mfb-bd-26.10/mfb-bd-sg-26.10.md:1338#on-chain-and-lightning-payments) | implemented | Each inherited subsection mapped to its current heading, 2026-09-30 | ACT-031 |
| ANN-169–222, ANN-240, ANN-242 | Student Guide, Module 4 | Local-learning evidence | Current local-module headings | [Local Module 4](../../publish/mfb-bd-26.10/mfb-bd-sg-26.10.md:1427#your-local-module-4), [local tools](../../publish/mfb-bd-26.10/mfb-bd-sg-26.10.md:1490#local-bitcoin-tools-and-resources), [community review](../../publish/mfb-bd-26.10/mfb-bd-sg-26.10.md:1841#review-connect-this-to-your-community) | implemented | Each inherited subsection mapped to its current heading, 2026-09-30 | ACT-031 |
| ANN-223–228 | Student Guide, Next Steps | Closing and contribution evidence | Current Next Steps headings | [Next Steps](../../publish/mfb-bd-26.10/mfb-bd-sg-26.10.md:1869#next-steps), [contribution](../../publish/mfb-bd-26.10/mfb-bd-sg-26.10.md:1877#contribute-to-my-first-bitcoin-and-the-resources-hub) | implemented | Each inherited subsection mapped to its current heading, 2026-09-30 | ACT-031 |

## Findings created or updated

| ID | Status | Severity | Release impact | Summary | Evidence | Run follow-up |
| --- | --- | --- | --- | --- | --- | --- |
| ACT-031 | done | medium | maintenance completed | Refreshed all 184 Student Guide evidence links in completed annotation records; no source markers, dispositions, or linked actions changed. | [Updated annotation inventory](../review_todo.md:671) | Recheck line references after future Student Guide restructuring. |

## Verification requests for an internet-connected AI agent

No external verification request was needed. This was an internal evidence-location audit.

## Returned verification evidence

| VER-ID | Outcome | Source title and direct URL | Check date | Evidence summary | Related finding or matrix row |
| --- | --- | --- | --- | --- | --- |
| none | not applicable | | 2026-09-30 | No external or objective claim was verified. | ACT-031 |

## Editor-discretion judgements

| Subject | Editor decision | Rationale and internal evidence | Date | Related finding or matrix row |
| --- | --- | --- | --- | --- |
| Annotation dispositions | Preserved unchanged. | The defect was stale evidence location, not a change in the historical annotation, current publication content, or triage decision. | 2026-09-30 | ACT-031 |

## Checks completed

- [x] Authority and scope checked.
- [x] Required traceability rows completed.
- [x] Style checks completed where in scope.
- [x] Alignment checks completed where in scope.
- [x] Local Markdown mechanics checked where in scope.
- [x] Link-register inventory and dated evidence updated where in scope.
- [x] External/objective verification requests created or results recorded where needed.
- [x] Render, accessibility, phone, or screen-reader checks recorded where needed.

## Checks not performed or deferred

No render, phone, or screen-reader test was needed because this run changed Markdown evidence locations only, not learner-facing content or layout.

## Review report summary

Completed `ACT-031` on 2026-09-30. Refreshed all 184 Student Guide evidence links attached to `ANN-` records: 179 recurring moved-location links plus five one-off mission, seed-phrase, local-module, and local-tools links. Every replacement uses the inspected current line and stable heading anchor for its inherited section. No annotation wording, source marker, disposition, checkbox, linked action, or curriculum content changed. Local checks confirmed that no `ANN-` entry still cites the superseded Student Guide locations `:109`, `:265`, `:580`, `:963`, `:1043`, `:1309`, `:1336`, `:1399`, or `:1770`. This run record is evidence only and is not a source of truth.
