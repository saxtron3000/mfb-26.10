# Review run: 2026-09-30 — ACT-021 seven competencies

## Run details

| Field | Record |
|---|---|
| Mode | Targeted change and final alignment review |
| Scope | Assessment Grid, Educator Guide, Student Guide, activities, workspace planning and assessment files, microlearning links, public briefs, and active cross-references |
| Requested by | Project user |
| Reviewer | Codex |
| Source version | 2026-09-30 working tree; no commit created |
| Authority | [Educator Guide operational assessment protocol](../../publish/mfb-bd-26.10/mfb-bd-eg-26.10.md#operational-assessment-protocol) |
| Completed | 2026-09-30 |

## Traceability matrix

| Requirement | Publication or operational evidence | Review result |
|---|---|---|
| Seven recorded competencies | Assessment Grid has `C1`–`C7` columns; Educator Guide has one canonical row and one crosswalk row for each. | Implemented |
| Two completion components | `C1`–`C5` theory and directly observed `C6`–`C7` practice appear in the Educator Guide, Student Guide, Assessment Grid, and planning files. | Implemented |
| At most three required sub-points | Canonical table has three each for `C1`, `C2`, and `C4`; two each for `C5`, `C6`, and `C7`; `C3` is an undivided guided comparison. | Implemented |
| Existing requirements preserved | `C6.1` contains wallet navigation, supported first access or receipt, receive/send flow, and verification; `C6.2` retains prepared recovery readiness. `C7` retains individual safe local performance and explanation. The old-to-new map is labelled historical in `workspace/05_competencies.md`. | Implemented |
| One final result per parent | Grid has seven result cells; Educator Guide specifies a single result after both `C6` practical performances. | Implemented |
| Activities aligned | All 14 published activities with Diploma assessment links use the new `C` codes and `P6a`/`P6b` task labels where applicable. Activities still require individual evidence and approved safety adaptations. | Implemented |
| Source-of-truth order | Educator Guide is identified as the competency and operational assessment authority; `workspace/05_competencies.md` and `workspace/13_assessment.md` mirror it for planning; the grid is the record. | Implemented |

## Checks completed

- Searched active `workspace/`, `publish/`, and `public/` Markdown for old `C8`–`C13` and `P9`–`P11` identifiers. Only the explicitly labelled historical mapping in `workspace/05_competencies.md` retains them.
- Searched active files for claims of 11 assessed competencies or 11 grid cells and reconciled those statements to seven.
- Reviewed the Educator Guide's canonical table, module tables, evidence crosswalk, task headings, and activity crosswalk for duplicate result rows and required look-fors.
- Reviewed the Student Guide learner outcomes, seven-column grid, 14 activity assessment links, and public briefs for the same code and component meanings.
- Checked edited primary Markdown files for trailing whitespace using `rg`; removed one blank-space line in the Student Guide.
- Ran `git diff --check` successfully and checked local Markdown link targets in the index, competency plan, assessment plan, Student Guide, Educator Guide, Assessment Grid, activity plan, and relocated Lexicon; the final local-link check found no missing targets.

## Findings and limits

No unresolved ACT-021 identifier or competency mismatch was found in active curriculum and publication files. Concurrent workspace changes relocated the Lexicon to `publish/mfb-lx-26.10.md`; the final link check used that location and preserved the other concurrent edits. The seven-competency consolidation does not itself validate a live cohort's timing or locally selected `C7` variant; those delivery checks remain separate existing actions. Historical review records and the 2026-09-21 report retain their original 11-code context as provenance. This run record is evidence of review, not a curriculum authority.
