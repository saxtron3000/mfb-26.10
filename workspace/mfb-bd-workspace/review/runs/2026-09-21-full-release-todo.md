# Review run: 2026-09-21 — consolidated to-do register

## Run details

| Field | Record |
| --- | --- |
| Mode | `full-release` |
| Scope | Every `ACT-001`–`ACT-021`, `ANN-001`–`ANN-242`, and `DEC-01`–`DEC-12` in `review/review_todo.md` |
| Requested by | Repository user |
| Reviewer | Codex |
| Source version | Working tree reviewed on 2026-09-21; commit identity unavailable in the sandbox |
| Workspace authority version | `workspace/00_index.md`, current publication files, and affected workspace authorities |
| Scripts used | `review/review_todo-script.md` |
| Started / completed | 2026-09-21 / 2026-09-21 |

## Traceability matrix

| TR-ID | Governing workspace file and heading | Requirement or decision | Expected publication or operational evidence | Actual evidence | State | Verification method and date | Related finding |
| --- | --- | --- | --- | --- | --- | --- | --- |
| TR-001 | `workspace/13_assessment.md`, assessment workflow | Complete assessment route | Runnable protocol and grid | [Protocol](../../publish/mfb-bd-26.10/mfb-bd-eg-26.10.md:47), [grid](../../publish/mfb-bd-26.10/mfb-bd-assessment-grid-26.10.md:29) | `implemented` | File review, 2026-09-21 | `ACT-001` |
| TR-002 | `workspace/15_certification.md`, governance still to define | Approved governance | Approved pack and aligned public process | [Open governance list](../../workspace/15_certification.md:142) | `missing` | File review, 2026-09-21 | `ACT-003`, `ACT-017` |
| TR-003 | `workspace/05_competencies.md`, status guardrails | One duration rule | Authorities and guides agree | [Fixed-scope wording](../../workspace/05_competencies.md:22) conflicts with [baseline wording](../../publish/mfb-bd-26.10/mfb-bd-eg-26.10.md:605) | `conflict` | File comparison, 2026-09-21 | `ACT-004`, `DEC-01` |
| TR-004 | Current assessment and architecture | Lightning explanation/practice boundary | Required comparison; local optional practice | [Student Guide boundary](../../publish/mfb-bd-26.10/mfb-bd-sg-26.10.md:1274) | `implemented` | File comparison, 2026-09-21 | `ACT-016`, `DEC-06` |
| TR-005 | `workspace/08_assets.md`, visual index | Controlled asset production | Tracker plus produced targets | [Tracker](../../workspace/08_assets.md:116) exists; [BD-V-001 target](../../publish/mfb-bd-26.10/mfb-bd-sg-26.10.md:13) is absent | `missing` | File/path check, 2026-09-21 | `ACT-012`, `ACT-013` |
| TR-006 | Annotation triage rules | Disposition and evidence for all annotations | 242 triaged entries | [Annotation inventory](../review_todo.md:510) | `implemented` | Item-by-item register review, 2026-09-21 | `ACT-018` |

## Findings created or updated

| ID | Status | Severity | Release impact | Summary | Evidence | Run follow-up |
| --- | --- | --- | --- | --- | --- | --- |
| `ACT-016` | `done` | `high` | `required before cohort` | Lightning boundary is aligned. | [Student Guide](../../publish/mfb-bd-26.10/mfb-bd-sg-26.10.md:1274) | Regression check on relevant edits. |
| `ACT-018` | `done` | `medium` | `maintenance` | All 242 annotations received dispositions. | [Register](../review_todo.md:510) | Clarify the 20 uncertain source notes when source evidence is available. |
| `ACT-003` | `blocked` | `critical` | `certificated-delivery blocker` | Governance pack is not approved. | [Certification framework](../../workspace/15_certification.md:142) | Obtain human governance decisions. |
| `ACT-008` | `blocked` | `high` | `publication blocker` | Conditional back matter remains ahead of approved processes. | [Student Guide](../../publish/mfb-bd-26.10/mfb-bd-sg-26.10.md:1850) | Remove or approve/test each retained section. |

## Verification requests for an internet-connected AI agent

### VER-001: Public destinations

```text
Verify every named programme, form, case-study, network, leaderboard, source, support, and donation destination in the 2026.10 Student Guide against the official destination on 2026-09-21. Return pass, fail, or uncertain; final direct URL; redirects; access restriction; and whether the destination matches its learner-facing purpose. Do not infer publication approval and do not edit files.
```

### Returned verification evidence

| VER-ID | Outcome | Source title and direct URL | Check date | Evidence summary | Related finding or matrix row |
| --- | --- | --- | --- | --- | --- |
| VER-001 | pending | | | Network verification not performed in this local run. | `ACT-009`, `ACT-019` |

## Editor-discretion judgements

| Subject | Editor decision | Rationale and internal evidence | Date | Related finding or matrix row |
| --- | --- | --- | --- | --- |
| Historical annotation proposals | Triaged without treating source markers as approval | Current publications were checked first; planned visuals were linked to `ACT-013`, uncertain handwriting was left for clarification, and superseded proposals were not reintroduced. | 2026-09-21 | `ACT-018` |

## Checks completed

- [x] Authority and scope checked.
- [x] Required traceability rows completed.
- [ ] Style checks completed where in scope.
- [x] Alignment checks completed where in scope.
- [x] Local Markdown mechanics checked where in scope.
- [x] Link-register inventory checked; external destinations remain unverified.
- [x] External/objective verification request created where needed.
- [ ] Render, accessibility, phone, or screen-reader checks recorded where needed.

## Checks not performed or deferred

- External destination checks: network verification was not completed; risk and next step remain in `ACT-009`.
- Human approvals: governance, policy, calibration, and unclear handwriting require authorized people or original source evidence.
- Rendering, phone, and screen-reader testing: no rendered release candidate or assistive-technology session was available; tracked under `ACT-011` and `ACT-019`.
- Git source identity: sandbox access to the user-level Git configuration was denied; the review uses a dated working-tree description.
- `git diff --check` completed successfully after disabling the inaccessible user-level Git configuration; Apple's toolchain emitted non-fatal sandbox cache warnings.

## Review report summary

This run reviewed all 21 actions, 242 annotations, and 12 decisions. Before the run, 2 actions and 2 decisions were resolved and no annotations were triaged. After the run, 4 actions and 6 decisions are resolved and all 242 annotations are triaged. Seventeen actions and six decisions remain open, blocked, or conflicting. This run record is review evidence, not a curriculum source of truth.
