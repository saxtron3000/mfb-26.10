# Review run: 2026-09-25 — asset migration to-do register

## Run details

| Field | Record |
| --- | --- |
| Mode | `change` |
| Scope | Every `ACT-`, `ANN-`, and `DEC-` record in `review/review_todo.md`, with change-scope evidence from the committed asset migration since `b089f37`. |
| Requested by | User |
| Reviewer | Codex |
| Source version | Baseline `b089f37`; current committed working tree `3a9457a37528c069ff7075fb3031c1dd5ab85e3b`. |
| Workspace authority version | Current `workspace/00_index.md`, `workspace/08_assets.md`, and the current implementation evidence named in the register. |
| Scripts used | `review_todo-script.md` |
| Started / completed | 2026-09-25 / 2026-09-25 |

## Findings created or updated

| ID | Status | Severity | Release impact | Summary | Evidence | Run follow-up |
| --- | --- | --- | --- | --- | --- | --- |
| ACT-013 | `in-progress` | `medium` | `maintenance` | Planning controls now have a generic brief inventory, but no final assets. | [asset production log](../../Assets/assets-list.md) | Kept open and refreshed evidence. |
| ACT-019 | `blocked` | `high` | `publication blocker` | Final verification now also depends on resolving the new visual-production blocker. | [ACT-028](../review_todo.md#act-028-produce-or-explicitly-defer-every-guide-visual) | Dependency list refreshed. |
| ACT-028 | `open` | `high` | `publication blocker` | The new guide marker paths reference generic briefs, not approved final visuals. | [alignment run](2026-09-25-change-assets-alignment.md#findings-created-or-updated) | Produce or explicitly defer visuals. |
| ACT-029 | `open` | `medium` | `maintenance` | The source map adds four paths that do not exist. | [alignment run](2026-09-25-change-assets-alignment.md#findings-created-or-updated) | Repair the map or restore authoritative documents. |
| ACT-030 | `open` | `low` | `maintenance` | The new asset style guide has a malformed H1. | [style run](2026-09-25-change-assets-style.md#findings-created-or-updated) | Repair the heading and clarify its authority status. |
| EVO-002 | `open` | `high` | `publication blocker` | The app QR asset has conflicting identifiers. | [alignment run](2026-09-25-change-assets-alignment.md#findings-created-or-updated) | Obtain an authorized reconciliation. |

## Register audit

The register contains 30 `ACT` records after this run, 242 `ANN` records, and 12 `DEC` records. Records were traversed in numerical order for a status-and-evidence audit. The asset migration supplied new evidence only for `ACT-013`, `ACT-019`, and the new findings above; no existing completed action, annotation disposition, or decision had current evidence to reopen or alter.

All 242 annotations remain triaged with their recorded dispositions. Their historical source markers and unresolved handwriting notes were preserved. All 12 decisions retain a recorded resolved answer; the new QR-ID conflict is an authority conflict, not a reopened historical decision.

## Checks completed

- [x] Read the register structure, dashboard, action list, decision register, and annotation inventory.
- [x] Recounted action, annotation, and decision identifiers after adding the two actions.
- [x] Refreshed dashboard, work-order, action-table, and `ACT-019` dependency text.
- [x] Added evidence and run links to updated or new findings.
- [x] Checked the new evidence targets and current asset-production status.

## Checks not performed or deferred

External destinations, rendered outputs, QR decoding, accessibility, screen-reader, phone, and real-cohort checks were not performed. Historic annotation evidence was not re-adjudicated beyond the changed asset scope; the existing dispositions remain historical triage, not fresh human approval.

## Review report summary

The to-do review ran on 2026-09-25 against the current asset-migration change scope. Counts changed from 27 to 30 `ACT` records; `ANN` remains 242 and `DEC` remains 12. `ACT-013` and `ACT-019` were refreshed, while `ACT-028`, `ACT-029`, `ACT-030`, and `EVO-002` were added and linked to the three review runs. The dashboard now reports 20 open actions out of 33 total actions, including the three retained asset-production subitems. No action was marked complete, no annotation disposition was changed, and no decision was resolved or reopened. External and rendered-output checks remain required. This run record is not a source of truth.
