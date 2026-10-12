# Review run: 2026-09-30: activity publications style

## Run details

| Field | Record |
| --- | --- |
| Mode | `targeted` |
| Scope | All 32 Markdown files in `publish/mfb-act-26.10/`. |
| Requested by | Project user |
| Reviewer | Codex |
| Source version | Working tree on 2026-09-30. No content edits were authorized. |
| Workspace authority version | `workspace/00_index.md`, `05_competencies.md`, `06_plan.md`, `10_activities.md`, and `16_spec.md`, read on 2026-09-30. |
| Scripts used | `review_style.md` |
| Started / completed | 2026-09-30 / 2026-09-30 |

## Traceability matrix

| TR-ID | Governing workspace file and heading | Requirement or decision | Expected publication or operational evidence | Actual evidence | State | Verification method and date | Related finding |
| --- | --- | --- | --- | --- | --- | --- | --- |
| TR-001 | `review_style.md`, `## Prompt 6: Review structure, formatting, and visual support` | Each Markdown document has one H1 and a consistent nested heading hierarchy. | One title H1 followed by H2/H3 sections. | Every numbered activity and the template has seven H1 headings. | `missing` | Heading inventory, 2026-09-30 | ACT-035 |
| TR-002 | `review_style.md`, `## Prompt 6: Review structure, formatting, and visual support` | Template labels are spelled correctly and guide consistent records. | A correct activity template and matching comparison checklist. | `mfb-act-000-template.md` misspells “Activity Type”; the checklist preserves conflicting Materials levels. | `missing` | Template and checklist read, 2026-09-30 | ACT-035 |
| TR-003 | `review_style.md`, `## Prompt 3: Apply the plain-language rules` | Use no em dashes. | Plain punctuation throughout. | Activity 001 has one em dash in `# Notes`; Activity 018 uses em dashes in a sample label. | `missing` | Character scan, 2026-09-30 | ACT-035 |
| TR-004 | `workspace/18_horizon.md`, `### Activity-library completion after publication` | Empty optional fields are post-publication maintenance, not an automatic release blocker. | Existing optional-field gaps retained without false release claim. | Numerous empty Participation, Duration, and discussion fields remain. | `intentionally deferred` | Full source read, 2026-09-30 | ACT-023 remains complete |
| TR-005 | `review_style.md`, `## Prompt 7: Check publication mechanics` | Publication-local links resolve. | Local Markdown links resolve from each activity source. | All local relative link targets resolved. | `implemented` | Local-target check, 2026-09-30 | none |

## Findings created or updated

| ID | Status | Severity | Release impact | Summary | Evidence | Run follow-up |
| --- | --- | --- | --- | --- | --- | --- |
| ACT-035 | `open` | `high` | `publication blocker` | The entire activity bank has a broken heading hierarchy and its template reproduces it. | 217 multi-H1 activity/template documents, a misspelled label, and a conflicting checklist. | Repair before rendering and accessibility verification. |

## Verification requests for an internet-connected AI agent

No external verification request was created. The style findings are internal, objective Markdown and editing defects.

## Editor-discretion judgements

| Subject | Editor decision | Rationale and internal evidence | Date | Related finding or matrix row |
| --- | --- | --- | --- | --- |
| Optional-field gaps | Preserve the settled release decision. | ACT-023 and the horizon register explicitly defer completion of optional activity fields. | 2026-09-30 | TR-004 |
| Assessment conditional language | Preserve it. | The language protects the distinction between formative activities and approved evidence. | 2026-09-30 | none |

## Checks completed

- [x] Every in-scope Markdown file read.
- [x] H1 counts, empty structural headings, template/checklist agreement, prohibited em dashes, placeholders, and local relative links checked.
- [x] Style finding routed to `review_todo.md`.

## Checks not performed or deferred

- No source edits, rendered-page inspection, screen-reader session, phone test, or translation review was performed.
- The post-publication decision on empty optional activity fields was respected rather than reopened.

## Review report summary

Targeted style review completed on 2026-09-30 for all 32 activity-folder Markdown files. No source files were edited. ACT-035 records the release-blocking heading hierarchy failure: the 30 numbered activities and the template each use seven H1 headings, and the template/checklist cannot prevent the error from recurring. Empty optional activity fields remain deliberately deferred under ACT-023. Local relative links resolve, but rendering, accessibility, and phone checks were not performed. Next action: complete ACT-035 and inspect the published activity render and heading navigation. This run record is not a source of truth.
