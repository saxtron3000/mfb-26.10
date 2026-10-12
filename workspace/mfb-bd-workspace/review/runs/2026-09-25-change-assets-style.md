# Review run: 2026-09-25 — asset migration style

## Run details

| Field | Record |
| --- | --- |
| Mode | `change` |
| Scope | Changed Student Guide and Educator Guide visual-marker and end-matter text, plus the changed asset-index and source-map mechanics that affect publication wording. |
| Requested by | User |
| Reviewer | Codex |
| Source version | Baseline `b089f37`; current committed working tree `3a9457a37528c069ff7075fb3031c1dd5ab85e3b`. |
| Workspace authority version | `workspace/00_index.md`, `workspace/08_assets.md`, `workspace/16_spec.md`, and repository guidance. |
| Scripts used | `review_style.md` |
| Started / completed | 2026-09-25 / 2026-09-25 |

## Findings created or updated

| ID | Status | Severity | Release impact | Summary | Evidence | Run follow-up |
| --- | --- | --- | --- | --- | --- | --- |
| ACT-028 | `open` | `high` | `publication blocker` | The new brief-path marker syntax makes a generic template look like a finished visual reference. | Both changed guides, `ASSET` lines; `assets/assets-list.md`. | Use a clear production status and a final asset reference only after approval. |
| ACT-029 | `open` | `medium` | `maintenance` | Four new source-map labels point to absent workspace documents, so the reading path is not usable. | `workspace/00_index.md`, `## Recommended reading order`. | Repair the paths or add the approved documents. |
| ACT-030 | `open` | `low` | `maintenance` | `workspace/27_assets-style.md` begins with stray formatting characters before its H1. | File opening line. | Repair its Markdown heading and clarify its authority status. |

## Applied changes

None. The request was to run reviews, not to revise learner or educator content.

## Checks completed

- [x] Checked the changed learner end matter for directness, optionality, safety framing, heading hierarchy, and app-name formatting.
- [x] Checked changed visual-marker syntax, headings, and module-reference formatting where affected.
- [x] Checked the changed source-map labels and local target existence.

## Checks not performed or deferred

No rendered output, external link, QR, accessibility, screen-reader, translation, or phone check was performed. No publication prose was edited.

## Review report summary

Change style review completed on 2026-09-25 for the asset-migration scope. No prose edit was applied. The revised Student Guide end matter remains compact and preserves its optional and safety limits, but the new marker syntax is misleading because it labels generic templates as assets, and the new source-map entries do not resolve. These findings are routed to `ACT-028` and `ACT-029`. Rendering and external accessibility checks remain outstanding. This run record is not a source of truth.
