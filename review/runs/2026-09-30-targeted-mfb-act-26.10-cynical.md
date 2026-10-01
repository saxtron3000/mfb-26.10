# Review run: 2026-09-30: activity publications cynical editor

## Run details

| Field | Record |
| --- | --- |
| Mode | `targeted` |
| Scope | All 32 Markdown files recursively stored in `publish/mfb-act-26.10/`. The review evidence is limited to those files, as required by the cynical-editor control. |
| Requested by | Project user |
| Reviewer | Codex |
| Source version | Working tree on 2026-09-30. No publication content edits were authorized. |
| Scripts used | `review_cynical_editor.md` |
| Started / completed | 2026-09-30 / 2026-09-30 |

## Cynical editor findings

| ID | Severity | File and stable heading | Defect | Evidence | Consequence | Required correction or decision | Acceptance condition | Related in-scope file or none |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CYN-001 | `high` | `mfb-act-006-lightning-relay-activity.md`; `## Materials` through `# Notes` | The procedure tells the educator to have learners use wallets, preferably their own, install or restore them, and pass real sats. A later note says the activity must not require those things. | “ideally their own,” “installation prompts, like creating a new wallet versus restoring an existing one,” “send them 21 sats,” and the later no-personal-wallet/no-real-funds note appear in the same activity. | A reader who follows the procedure can expose learners to an unnecessary wallet setup, device, and real-value exercise; the final disclaimer does not undo the earlier instructions. | Rewrite the whole procedure around a simulation or educator-controlled route, or defer it. | Every listed step works without a learner device, personal wallet, real funds, account, or secret. | none |
| CYN-002 | `high` | `mfb-act-004-fractional-reserve-banking.md`; `# Description`, `## Steps 2–6`, and `## Key Points` | A staged 10% multiplier exercise is presented as banking mechanics, then makes categorical claims about reserves, risk, bailouts, and moral hazard. | “each loan becomes the next deposit,” “the total supply of money increases,” “The smaller the reserve, the more risk,” and “leads to moral hazard” are not limited by the surrounding classroom-model warning. | Learners receive a simplified model as a universal explanation of modern banking and may mistake ideological conclusions for demonstrated facts. | Replace it with a clearly bounded model or remove it pending factual review. | The activity labels its scope, distinguishes the model from current practice, and supports each retained causal claim. | `mfb-act-029-watch-how-money-and-banking-work.md` |
| CYN-003 | `high` | `mfb-act-003-exploring-the-mempool.md`, `mfb-act-007-transactions-in-action.md`, `mfb-act-019-bitcoin-transactions-in-action.md`, and `mfb-act-020-verification.md`; technical explanations and key points | The bank teaches several wrong or misleading foundational concepts. | Activity 003 calls capacity a “4 MB block limit”; Activity 007 says every transaction has four participant types and that miners ensure all criteria; Activity 019 makes recipients approve and miners decide transaction inclusion by a lowest die roll; Activity 020 says a miner finds a block “below the difficulty adjustment.” | A beginner cannot build correct later understanding on misnamed concepts and false role assignments. | Correct the models after technical review; keep only simplifications that name their limit. | The activities accurately distinguish target, difficulty adjustment, nodes, miners, wallet users, transaction validation, and classroom analogy. | none |
| CYN-004 | `high` | 30 numbered activity files and `mfb-act-000-template.md`; document hierarchy | Every activity has seven H1 headings, and the template creates the same invalid hierarchy. | Each document uses H1 for its title, Description, Preparation, Procedure, Review, Notes, and Additional Resources. The template also misspells “Activity.” | Heading navigation, document outlines, and rendered structure are broken across the library, and future authors will reproduce the defect. | Repair the template first, then convert activity section headings to a consistent H2/H3 hierarchy. | Every activity has one H1 title, meaningful nested headings, and a rendered screen-reader heading check. | `activities-template-comparison-checklist.md` |

## Traceability matrix

| TR-ID | Governing workspace file and heading | Requirement or decision | Expected publication or operational evidence | Actual evidence | State | Verification method and date | Related finding |
| --- | --- | --- | --- | --- | --- | --- | --- |
| TR-001 | Not inspected, cynical-editor boundary | Follow literal procedures safely. | Internal procedure consistency. | Activity 006 contradicts its own safety note. | `conflict` | Full in-scope source read, 2026-09-30 | CYN-001; ACT-033 |
| TR-002 | Not inspected, cynical-editor boundary | Technical explanations must be internally coherent. | Accurate labels and role descriptions. | Four activities contain conflicting or incorrect labels. | `missing` | Full in-scope source read, 2026-09-30 | CYN-003; ACT-032 |
| TR-003 | Not inspected, cynical-editor boundary | Markdown must support publication. | One H1 and usable hierarchy. | 31 documents have seven H1 headings. | `missing` | Heading inventory, 2026-09-30 | CYN-004; ACT-035 |

## Findings created or updated

| ID | Status | Severity | Release impact | Summary | Evidence | Run follow-up |
| --- | --- | --- | --- | --- | --- | --- |
| ACT-032 | `open` | `high` | `publication blocker` | Correct technical models. | CYN-003. | Technical review and source correction. |
| ACT-033 | `open` | `high` | `publication blocker` | Make Lightning relay safe and optional. | CYN-001. | Rewrite or defer Activity 006. |
| ACT-034 | `open` | `high` | `publication blocker` | Replace banking multiplier model. | CYN-002. | Qualified banking review and rewrite. |
| ACT-035 | `open` | `high` | `publication blocker` | Repair activity Markdown hierarchy. | CYN-004. | Template-first hierarchy correction and render check. |

## Verification requests for an internet-connected AI agent

External factual checks are recorded in the paired alignment run. This publish-only review does not use them as evidence.

## Editor-discretion judgements

| Subject | Editor decision | Rationale and internal evidence | Date | Related finding or matrix row |
| --- | --- | --- | --- | --- |
| Empty optional sections | No new defect. | The current activity scope contains gaps, but this review does not reopen the separate published completion decision. | 2026-09-30 | none |

## Checks completed

- [x] Enumerated and read every in-scope Markdown file.
- [x] Ran the accuracy, missing-information, consistency, learner-failure, language, repetition, publication-mechanics, and challenge passes within the publish-only boundary.
- [x] Checked local relative-link targets.
- [x] Routed four distinct actionable findings to `review_todo.md`.

## Checks not performed or deferred

- External links, destinations, source facts, rendered output, accessibility, phone usability, and classroom delivery were not tested in this publish-only review.
- No out-of-scope workspace, public, reference, feedback, or external-web material was used as cynical-review evidence.

## Review report summary

**Verdict: not ready.** This targeted cynical-editor review covered all 32 Markdown files in `publish/mfb-act-26.10/`. It found four High defects, no Critical defects, and no Medium or Low defects. The three most important defects are the contradictory live-wallet Lightning relay, the inaccurate banking exercise, and the incorrect technical models. The fourth is a library-wide H1 hierarchy failure. Full source reading and local-link checking were completed; external links, rendering, accessibility, classroom testing, and factual verification were not performed within this publish-only review. Next action: complete ACT-032–ACT-035 before calling this activity publication set ready. This run record is not a source of truth.
