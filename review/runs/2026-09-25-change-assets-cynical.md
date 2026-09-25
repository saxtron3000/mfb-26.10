# Review run: 2026-09-25 — asset migration cynical

## Run details

| Field | Record |
| --- | --- |
| Mode | `change` |
| Scope | Changed in-scope publications: `publish/mfb-bd-26.10/mfb-bd-sg-26.10.md` and `publish/mfb-bd-26.10/mfb-bd-eg-26.10.md`, including directly affected visual markers. |
| Requested by | User |
| Reviewer | Codex |
| Source version | Baseline `b089f37`; current committed working tree `3a9457a37528c069ff7075fb3031c1dd5ab85e3b`. |
| Workspace authority version | Excluded by this control's publication-only evidence boundary. |
| Scripts used | `review_cynical_editor.md` |
| Started / completed | 2026-09-25 / 2026-09-25 |

## Cynical editor findings

| ID | Severity | File and stable heading | Defect | Evidence | Consequence | Required correction or decision | Acceptance condition | Related in-scope file or none |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CYN-001 | high | Student Guide and Educator Guide, all `<!-- VISUAL ... -->` markers | The change substitutes Markdown design-brief paths for visual assets at 138 reserved locations. The comments are non-rendered and give a production system no final image, vector, or code asset to insert. | 79 Student Guide and 59 Educator Guide `ASSET: Assets/Briefs/bd-v-###-brief.md` lines; the source files themselves identify these as comments. | A rendered edition can omit every planned visual, including learner safety and app-download panels, while the source appears to have asset references. | Complete the visual production and insertion workflow, or make each deferred location explicit and keep the publication claim proportionate. | Every included marker resolves to an approved, production-ready asset; each deferred asset is visibly and accurately deferred. | Both changed guides |

## Editor-discretion judgements

| Subject | Editor decision | Rationale and internal evidence | Date | Related finding or matrix row |
| --- | --- | --- | --- | --- |
| Revised Student Guide end matter | No additional defect recorded. | The rewrite consolidates contribution, community, safety, adaptation, support, and certificate content without removing the optionality or safety qualifications visible in the changed text. | 2026-09-25 | none |

## Checks completed

- [x] Read both changed publication files in context.
- [x] Checked headings, marker balance, duplicate visual IDs, and changed end matter.
- [x] Searched the publication scope for all changed marker syntax.
- [x] Challenged the finding against the fact that comments may be intentional production markers; it remains because the new `ASSET` value is a generic Markdown brief, not a production asset.

## Checks not performed or deferred

No workspace, repository asset, external-link, rendered-output, accessibility, screen-reader, or phone check was used as cynical-review evidence. No current or technical claim was externally verified.

## Review report summary

Verdict: not ready for the reviewed publication scope. One high-severity defect was found: 138 changed guide markers now reference brief documents rather than usable visual assets, leaving visual insertion unresolved. It is routed to `ACT-028` and the existing visual-control work. Both changed guides were read and their local marker mechanics were checked; rendering, external links, accessibility, screen-reader, and phone checks were not performed. The next action is to supply approved production assets or explicitly defer the visual locations before rendering. This run record is not a source of truth.
