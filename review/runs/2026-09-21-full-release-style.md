# Review run: 2026-09-21 — full release

## Run details

| Field | Record |
| --- | --- |
| Mode | `full-release` |
| Scope | Every `workspace/` and `publish/` document or publication data file; both link registers; traceability and release-critical controls; style, readability, terminology, formatting, and publication mechanics |
| Requested by | User |
| Reviewer | Codex |
| Source version | Working tree at `ed-dev`, based on commit [`c5d5cd06dab1ba213c6642272eea1ee7bdb412da`](https://github.com/saxtron3000/bd-26.10/commit/c5d5cd06dab1ba213c6642272eea1ee7bdb412da) (`review-tune-up`, committed 2026-09-21 01:19:39 -06:00); working tree was dirty at review time |
| Git provenance note | The initial inspection could not read `/Users/saxtron3000/.gitconfig` in the sandbox and therefore recorded the fallback description above. The commit and branch were subsequently verified with Git's global configuration disabled; the review findings reflect the dated working tree, including uncommitted changes |
| Workspace authority version | `workspace/00_index.md` through `workspace/20_links-internal.md`, with relevant headings reviewed in context |
| Scripts used | `review_alignment.md`, `review_style.md` |
| Started / completed | 2026-09-21 / 2026-09-21 |

## Traceability matrix

| TR-ID | Governing workspace file and heading | Requirement or decision | Expected publication or operational evidence | Actual evidence | State | Verification method and date | Related finding |
| --- | --- | --- | --- | --- | --- | --- | --- |
| TR-001 | `workspace/06_plan.md`, `## 2. Four-Module Architecture` | The Diploma has four required modules; Module 4 is educator-curated and locally relevant. | Student Guide, Educator Guide, and Assessment Grid state all four modules and required `C11` evidence. | SG four-module section; EG module guidance and assessment protocol; grid C11 column. | `implemented` | Cross-read 2026-09-21 | none |
| TR-002 | `workspace/05_competencies.md`, `## Safety and assessment boundaries` | Theory `C1`–`C8` is educator-evaluated; practice `C9`–`C11` is directly observed. | Educator Guide protocol and Assessment Grid preserve separate evidence routes. | EG operational assessment protocol; grid competency key and direct-observation marks. | `implemented` | Cross-read 2026-09-21 | ACT-001, ACT-002 |
| TR-003 | `workspace/13_assessment.md`, `## 3. Assessment components` | The two equal-status completion gates are non-compensatory; optional self-checks are not evidence. | Guides and grid state the rule without a combined numerical grade. | SG assessment sections; EG assessment rules; grid completion check. | `implemented` | Cross-read 2026-09-21 | ACT-001, ACT-017 |
| TR-004 | `workspace/16_spec.md`, `# 2026.10 Bitcoin Diploma Overview` | October publication outputs include low-tech print/PDF, online PDF, and web publication. | Architecture and release wording agree on outputs and future branches. | `16_spec.md` includes all outputs; `06_plan.md` retains future-branch wording. | `conflict` | Ordered workspace comparison 2026-09-21 | ACT-015 |
| TR-005 | `workspace/14_microlearning-plan.md`, `## Phase 1 minimal viable product` | The self-check is voluntary, score-independent, and not certification evidence. | Published result messages must not imply Diploma competence; metadata and usability need review. | Published self-check states no pass/fail and no educator tracking; 10–12 message corrected in this run. | `intentionally deferred` | Text review 2026-09-21; device and screen-reader checks not run | ACT-011 |
| TR-006 | `workspace/20_links-external.md`, `## Review instructions` | External destinations require dated objective verification before publication. | Link registers contain checked status and evidence for retained destinations. | External and internal registers remain `Pending`; no web verification recorded. | `missing` | Register inspection 2026-09-21 | ACT-009, ACT-019 |
| TR-007 | `workspace/08_assets.md`, `## 3. Visual index` | Essential assets must have produced files or approved replacements, with rights and alt text. | Asset paths resolve and visual QA is recorded. | `BD-V-001` references absent `y_assets (archived)/diploma/bd-v-001.svg`; asset register is a brief, not production evidence. | `missing` | Local file inventory and register inspection 2026-09-21 | ACT-012, ACT-013 |
| TR-008 | `workspace/15_certification.md`, `# Bitcoin Diploma Certification Framework` | Certification readiness depends on governance, calibration, and operational validation, not prose alone. | Release records, governance pack, and calibration evidence exist before certificated delivery. | Written protocol exists; governance and calibration evidence remain pending in ACT-001–003. | `missing` | Cross-read and action-register review 2026-09-21 | ACT-001, ACT-002, ACT-003, ACT-017 |

## Findings created or updated

| ID | Status | Severity | Release impact | Summary | Evidence | Run follow-up |
| --- | --- | --- | --- | --- | --- | --- |
| ACT-001, ACT-002, ACT-003 | `needs-verification` | critical | certificated-delivery blocker | Assessment route, assessor calibration, and record/certificate governance are not evidenced as operational. | `review/review_todo.md` release blockers; EG protocol and grid exist, but no current delivery evidence was supplied. | Complete acceptance conditions before certificated delivery or a results-retaining pilot. |
| ACT-004, ACT-015, ACT-016, ACT-017 | `needs-verification` | high/critical | publication blocker / required before cohort / certificated-delivery blocker | Duration, October output scope, Lightning boundary, and operational release positioning still require reconciliation or validation. | `workspace/02_research.md`, `workspace/06_plan.md`, `workspace/16_spec.md`, and current guides. | Resolve authority conflicts and record evidence. |
| ACT-008, ACT-009, ACT-010, ACT-011, ACT-012, ACT-013, ACT-019 | `needs-verification` | medium/high | publication blocker / maintenance | Conditional back matter, external links, mutable registers, self-check QA, missing visual target, visual production, and final publication verification remain open. | Current Student Guide back matter; link registers marked `Pending`; `BD-V-001` absent; self-check message corrected in this run. | Complete external, visual, device, accessibility, and rendering checks. |
| EDIT-001 | `done` | low | none | Corrected five clear prose or terminology defects without changing curriculum meaning, including aligning the self-check message in the plan and publication data. | `workspace/12_educator-plan.md`, `workspace/14_microlearning-plan.md`, `publish/mfb-ml-26.10/mfb-ml-26.10.md`, `publish/mfb-bd-26.10/mfb-bd-sg-26.10.md`, `publish/mfb-act-26.10/mfb-act-007-transactions-in-action.md`. | Re-read in context completed 2026-09-21. |

## Verification requests for an internet-connected AI agent

### Returned verification evidence

| VER-ID | Outcome | Source title and direct URL | Check date | Evidence summary | Related finding or matrix row |
| --- | --- | --- | --- | --- | --- |
| VER-001 | pending | — | 2026-09-21 | Verify every retained external destination in `workspace/20_links-external.md` and `workspace/20_links-internal.md`, including purpose, form/audience, language, anchors, query strings, redirects, access restrictions, and current suitability. No internet-connected link check was performed in this run. | TR-006; ACT-009, ACT-019 |

## Editor-discretion judgements

| Subject | Editor decision | Rationale and internal evidence | Date | Related finding or matrix row |
| --- | --- | --- | --- | --- |

## Checks completed

- [x] Authority and scope checked.
- [x] Required traceability rows completed.
- [x] Style checks completed where in scope.
- [x] Alignment checks completed where in scope.
- [x] Local Markdown mechanics checked where in scope.
- [x] Link-register inventory and dated evidence reviewed; statuses remain pending.
- [x] External/objective verification request created; no result recorded.
- [ ] Render, accessibility, phone, or screen-reader checks recorded where needed.

## Checks not performed or deferred

External destination checks, rendered output, visual production, phone layout, screen-reader behavior, and real-cohort timing/calibration were not performed. Git's diff-check command was attempted but emitted sandbox-specific xcrun/configuration warnings; changed passages were manually re-read.

## Review report summary

Full-release review completed 2026-09-21. The run found a coherent four-module and assessment design in the current text, but certificated delivery remains blocked by ACT-001–003 and release/publication reconciliation remains open under ACT-004, ACT-008–013, ACT-015–017, and ACT-019. Five bounded editorial fixes were applied, including the aligned self-check score-message correction. External links, rendering, accessibility, phone usability, missing assets, and live delivery evidence remain unverified. This run record is evidence of the review process, not a source of truth.
