# Change run: 2026-09-30: activity-review remediation

## Run details

| Field | Record |
| --- | --- |
| Mode | `targeted source correction` |
| Scope | Activities 001–030, the activity template and checklist, the activity web-link inventory, and active link-register references affected by ACT-009 and ACT-032–ACT-035. |
| Requested by | Project user |
| Implementer | Codex |
| Source version | Working tree on 2026-09-30. |
| Governing sources consulted | `workspace/06_plan.md`, `workspace/10_activities.md`, `workspace/16_spec.md`, the three targeted 2026-09-30 review runs, and the cited primary technical and Federal Reserve sources. |
| Started / completed | 2026-09-30 / 2026-09-30 |

## Changes made

| Related action | Source correction | Files changed |
| --- | --- | --- |
| ACT-032 / PUB-005 | Rewrote the mempool, transaction-role, transaction-validation, and proof-of-work models. The activities now distinguish a node mempool from a block explorer, block weight from a simple MB label, sender authorization from recipient checks, node validation from miner candidate-block construction, the proof-of-work target from difficulty adjustment, and the limits of each classroom analogy. | Activities 003, 007, 019, and 020. |
| ACT-033 / PUB-003 | Replaced the live Lightning wallet relay with a wholly nonfunctional card simulation. It requires no learner device, wallet, secret, account, internet connection, or funds; live use is explicitly locally selected. | Activity 006. |
| ACT-034 / PUB-004 | Replaced the fixed-reserve multiplier exercise with a bounded bank balance-sheet model. It distinguishes deposits, loans, reserves, liquidity, capital, and money measures, and directs educators to current local evidence for jurisdiction-specific claims. | Activity 004. |
| ACT-035 | Gave all activity sources one H1, corrected the H2/H3 nesting and sentence-case labels, removed blank structural headings from numbered activities, removed prohibited em dashes, and replaced the inaccurate comparison checklist with a current conformance record. | Activity template, activities 001–030, and the comparison checklist. |
| ACT-009 / EVO-003 | Added the activity-source web links to the external register and corrected active references to the canonical `links/` register files. | `links/links-external.md`, `links/links-internal.md`, `workspace/09_resources.md`, and `workspace/18_horizon.md`. |

## Verification completed

- [x] Each activity template or numbered activity source has exactly one H1 (31 files).
- [x] No direct H1-to-H3 heading jump was found.
- [x] No empty structural heading was found in Activities 001–030; the template may retain intentional placeholders.
- [x] No em dash was found in the activity library.
- [x] Searches found none of the reviewed unsafe Lightning instructions or the reviewed technical and banking misstatements.
- [x] Activity-source external destinations are represented in the external link register.
- [x] `git diff --check` completed without whitespace errors.

## Verification still required

- A qualified banking reviewer must approve the final Activity 004 framing before its release blocker can be closed.
- A technical reviewer should confirm the corrected beginner explanations in Activities 003, 007, 019, and 020.
- The next Resources Hub deployment must be compared with these sources, including screen-reader heading navigation.
- Each retained external destination remains `Pending` until it is checked in context under ACT-009.

## Review report summary

The source-level remediation for the targeted activity reviews is complete. Activities 003, 004, 006, 007, 019, and 020 were rewritten where needed; the full activity bank and template now have a valid Markdown heading structure; and activity web links are inventoried in the canonical register. Independent subject-matter review, live-link checking, and deployed Resources Hub rendering checks remain required release verification. This run record is not a source of truth.
