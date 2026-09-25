# Review run: 2026-09-25 — asset migration alignment

## Run details

| Field | Record |
| --- | --- |
| Mode | `change` |
| Scope | Committed changes since `b089f37`: the Student Guide, Educator Guide, asset index and production materials, source-of-truth map, and directly affected review controls. |
| Requested by | User |
| Reviewer | Codex |
| Source version | Baseline `b089f37`; current committed working tree `3a9457a37528c069ff7075fb3031c1dd5ab85e3b` on `main`. This is a bounded change review. |
| Workspace authority version | `workspace/00_index.md`, `workspace/08_assets.md`, `workspace/16_spec.md`, and repository guidance at the current source version. |
| Scripts used | `review_alignment.md` |
| Started / completed | 2026-09-25 / 2026-09-25 |

## Changed-proposition inventory and impact map

| CHG-ID | Origin and new meaning | Governing authority / decision evidence | Dependent material checked | Disposition |
| --- | --- | --- | --- | --- |
| CHG-001 | Guide visual markers now name `assets/briefs/*.md` instead of former SVG paths. | `workspace/08_assets.md`, `## 4. Placement` says a marker is non-rendered and must be replaced by a final production reference after approval. | Both guides, all 101 briefs, and the production log. | `update required`: 79 Student Guide and 59 Educator Guide markers name generic briefs; no production reference image, vector/code asset, upload, or package is recorded. |
| CHG-002 | The app-download QR marker was renumbered from `BD-V-075` to `BD-V-076`; `BD-V-075` is now deferred certificate verification. | Repository guidance requires `BD-V-075` for the [My First Bitcoin App](https://myfirstbitcoin.app/) QR; the changed asset index assigns that use to `BD-V-076`. | Both guide introductions and endings, and the visual index. | `conflict`: resolve the identifier and update every dependent marker and brief only after the authority is settled. |
| CHG-003 | The source-of-truth map now lists workspace files 22–25. | `workspace/00_index.md`, `## Recommended reading order`. | `workspace/` and the newly added prompt material. | `missing`: none of the four linked `workspace/22_`–`25_` files exists. |

## Traceability matrix

| TR-ID | Governing workspace file and heading | Requirement or decision | Expected publication or operational evidence | Actual evidence | State | Verification method and date | Related finding |
| --- | --- | --- | --- | --- | --- | --- | --- |
| TR-001 | `workspace/08_assets.md`, `## 4. Placement` | A source marker is non-rendered and is replaced only by an approved final Markdown or production asset reference. | Produced, approved visual references for every included visual. | The guides retain 138 markers pointing to generic brief templates; `assets/assets-list.md` records zero reference images, uploads, and MG packages. | `missing` | Marker, brief, and production-log inventory, 2026-09-25 | ACT-028; ACT-013 |
| TR-002 | Repository guidance, app QR rule; `workspace/08_assets.md`, `## 2. Visual index` | The designated app QR asset and its four permitted placements agree. | One identifier with two placements in each guide. | Repository guidance names `BD-V-075`; the index and guides use `BD-V-076` while marking `BD-V-075` deferred. | `conflict` | Authority-to-marker comparison, 2026-09-25 | EVO-002 |
| TR-003 | `workspace/00_index.md`, `## Recommended reading order` | Every source-of-truth-map link resolves to the named workspace document. | Files 22–25 exist at the listed paths. | The four paths are absent. | `missing` | Local file check, 2026-09-25 | ACT-029 |

## Findings created or updated

| ID | Status | Severity | Release impact | Summary | Evidence | Run follow-up |
| --- | --- | --- | --- | --- | --- | --- |
| ACT-028 | `open` | `high` | `publication blocker` | Visual markers point to unpopulated brief templates, not production assets. | `assets/assets-list.md`; both guides' `ASSET` marker lines. | Produce, approve, and insert or correctly defer the needed assets. |
| EVO-002 | `open` | `high` | `publication blocker` | Repository app-QR requirement conflicts with the changed asset-index identifier. | Repository guidance; `workspace/08_assets.md`, `BD-V-075` and `BD-V-076`. | Obtain an authorized identifier decision before changing dependent guide markers. |
| ACT-029 | `open` | `medium` | `maintenance` | The map links to four missing workspace files. | `workspace/00_index.md`, `## Recommended reading order`. | Restore files at those paths or correct the map to approved locations. |

## Checks completed

- [x] Authority, scope, baseline, and changed-proposition inventory checked.
- [x] Guide visual markers, asset-index IDs, brief contents, production-log status, and source-map targets checked.
- [x] Fixed-point impact check completed for the new review findings.

## Checks not performed or deferred

No external URLs, rendered PDF/Sanity output, QR destinations, accessibility, phone, or screen-reader behavior were tested. No asset was visually reviewed because no final production asset is recorded.

## Review report summary

Change review completed on 2026-09-25 for the committed asset migration since `b089f37`. The migration creates a publication blocker: all 138 guide `ASSET` references point to generic, unpopulated brief templates while the production log records no final visual assets. A second high-severity authority conflict assigns the required app QR to different IDs in repository guidance and the changed asset index. The source-of-truth map also contains four missing workspace targets. New register entries are `ACT-028`, `EVO-002`, and `ACT-029`; no curriculum or publication prose was changed. External destinations and rendered outputs were not tested. This run record is not a source of truth.
