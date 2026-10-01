# Review run: 2026-09-21 — recent workspace-to-publication propagation

## Run details

| Field | Record |
| --- | --- |
| Mode | `change` |
| Scope | Changes after the 2026-09-21 full-release alignment run that affect `workspace/` authorities or their implementation in `publish/`; linked review controls and link registers were also inspected. |
| Requested by | User |
| Reviewer | Codex |
| Source version | Baseline: `a3947ea` (`2026-09-21-full-release-alignment.md`). Reviewed commit range: `a3947ea..b089f37` (`heavy review & todo & decide`). The working tree was clean at review start; concurrent unstaged edits later appeared in the Student Guide and review register and are outside this commit-range finding set. This is a bounded commit-range review, not a complete historical audit. |
| Workspace authority version | Current `workspace/00_index.md`, `02_research.md`, `03_scope.md`, `04_design.md`, `05_competencies.md`, `06_plan.md`, `07_contents.md`, `08_assets.md`, `09_resources.md`, `12_educator-plan.md`, `13_assessment.md`, `15_certification.md`, `16_spec.md`, `17_advanced.md`, `18_horizon.md`, `19_publication-coverage.md`, `20_links-external.md`, and `20_links-internal.md` at `b089f37`. |
| Scripts used | `review_alignment.md` |
| Started / completed | 2026-09-21 / 2026-09-21 |

## Changed-proposition inventory and impact map

| CHG-ID | Origin and new meaning | Governing authority / decision evidence | Dependent material checked | Disposition |
| --- | --- | --- | --- | --- |
| CHG-001 | `approximately eight hours` became a minimum eight-hour route with no upper limit; valid evidence, not attendance, determines completion. | `workspace/05_competencies.md` `## Status and scope guardrails`; `workspace/06_plan.md` `## 1. Current Design Commitments`; `DEC-01`. | Student Guide pathway, Educator Guide minimum-pathway and pre-reading guidance, Assessment Grid, and Quick Start. | `already aligned` — each now preserves the minimum/no-cap rule and assessment boundary. |
| CHG-002 | The October output boundary now includes offline print/PDF, online PDF, and website-ready Sanity content; only the other instructional branches remain future work. | `workspace/03_scope.md` `# Project Assumptions`; `workspace/06_plan.md` `## 1. Current Design Commitments` and `## 8. October 2026 Output`; `DEC-07`. | Publication-facing release wording, `workspace/16_spec.md`, `workspace/18_horizon.md`, and the coverage register. | `already aligned` — resolved `EVO-001`; no learner-guide copy change is required because this is a release-output boundary, not a learner promise. |
| CHG-003 | Certification is decentralized and educator-issued; My First Bitcoin does not centrally assess, issue, verify, or guarantee certificates. Issuer-specific verification remains optional and locally governed. | `workspace/15_certification.md` `## Current Governance And Future Options`; `DEC-11` and `DEC-12`. | Student Guide certificate section, Educator Guide certificate guidance, Assessment Grid, Quick Start, assets, and public/coverage statements. | `already aligned` — resolved `PUB-001`; local governance and calibration remain release conditions under `ACT-002` and `ACT-003`. |
| CHG-004 | Named programme links are optional further learning, never a Diploma requirement; open-source wallet software is a qualified transparency preference, not a global recommendation or guarantee. | `workspace/06_plan.md` `## 1. Current Design Commitments`; `DEC-08`; `DEC-09`. | Student Guide pathways and wallet text, Educator Guide wallet guidance, Quick Start, and Activity 017. | `already aligned` — all checked implementation material retains learner choice and trade-offs. |
| CHG-005 | Pre-reading may be required only with accessible equivalent routes; it does not count toward the eight-hour minimum or replace supported learning and assessment. | `workspace/06_plan.md` `# 5. In-Class Time Rules`. | Educator Guide `### The minimum eight-hour pathway`. | `already aligned`. |
| CHG-006 | The Creative Commons mark is a Sanity-production requirement rather than an absent local SVG, while its written licence statement remains primary. | `workspace/08_assets.md` `## 3. Visual index`, `BD-V-001`. | Student Guide production marker and asset register. | `already aligned`; production/rights evidence remains governed by `ACT-013`, not by this text-only review. |
| CHG-007 | The Quick Start is now classified in the publication coverage register; Advanced remains a future placeholder. | `workspace/19_publication-coverage.md` `## Diploma publication set`; `workspace/17_advanced.md` `## 1. Status And Use`. | Quick Start and `publish/mfb-adv-26.10/README.md`. | `update required` for the eight Advanced draft files: they still lack individual explicit coverage entries. This is the existing `PUB-002`, not a new authority conflict. |
| CHG-008 | Link-register rows were refreshed for altered wording and destination purpose. | `workspace/20_links-external.md` and `workspace/20_links-internal.md` `## Review instructions`. | Student and Educator Guide links and the register status/evidence fields. | `intentionally deferred` — inventories reflect current locations, but destination testing remains pending under `ACT-009` and `ACT-019`. |

## Traceability matrix

| TR-ID | Governing workspace file and heading | Requirement or decision | Expected publication or operational evidence | Actual evidence | State | Verification method and date | Related finding |
| --- | --- | --- | --- | --- | --- | --- | --- |
| TR-001 | `workspace/05_competencies.md`, `## Status and scope guardrails` | At least eight hours, no upper limit, and no time-attendance substitute for required evidence. | Guides, grid, and Quick Start use the same boundary. | Student Guide pathway; Educator Guide `### The minimum eight-hour pathway`; grid and Quick Start checklist match. | `implemented` | Commit-range diff and current cross-read, 2026-09-21 | none |
| TR-002 | `workspace/06_plan.md`, `## 1. Current Design Commitments` | Online PDF and Sanity web content are October outputs; other named branches are future work. | Authorities and release-facing statements distinguish outputs from future branches. | `03_scope`, `06_plan`, `16_spec`, and `18_horizon` are aligned; no learner-facing promise is required. | `implemented` | Ordered authority comparison, 2026-09-21 | EVO-001 (done) |
| TR-003 | `workspace/15_certification.md`, `## Current Governance And Future Options` | Educator-issued certification; no central My First Bitcoin issuance, verification, or guarantee. | Student and Educator Guide explain certificate meaning without an unsupported service. | Student Guide `### Certificate meaning and issuer`; Educator Guide certificate guidance; related assets defer `BD-V-074`. | `implemented` | Authority/publication cross-read, 2026-09-21 | PUB-001 (done), ACT-002, ACT-003 |
| TR-004 | `workspace/06_plan.md`, `# 5. In-Class Time Rules` | Permitted pre-reading has accessible equivalents and cannot replace or count toward required learning. | Educator instruction preserves the access and time safeguards. | Educator Guide `### The minimum eight-hour pathway` states each safeguard. | `implemented` | Authority/publication cross-read, 2026-09-21 | none |
| TR-005 | `workspace/06_plan.md`, `## 1. Current Design Commitments`; `DEC-08`, `DEC-09` | Optional programme links and qualified open-source-wallet guidance preserve choice and avoid global endorsements. | Student Guide, Educator Guide, Quick Start, and wallet activity state the limits and trade-offs. | Checked current sections have the approved optionality, transparency rationale, and non-guarantee wording. | `implemented` | Impact search and current cross-read, 2026-09-21 | none |
| TR-006 | `workspace/08_assets.md`, `BD-V-001` | Sanity production must supply approved licence-mark evidence without falsely referencing a local asset. | Student Guide marker directs Sanity production and retains alt text. | Current marker matches the asset register. | `intentionally deferred` | Marker/register comparison, 2026-09-21 | ACT-013 |
| TR-007 | `workspace/19_publication-coverage.md`, `## Diploma publication set` and `## Maintenance check` | Every curriculum-content publication is included once or explicitly deferred. | Quick Start and every Advanced draft have a coverage disposition. | Quick Start is recorded; `README.md` is recorded as Advanced placeholder, but eight Advanced drafts are not individually covered. | `missing` | Inventory/register comparison, 2026-09-21 | PUB-002 |
| TR-008 | `workspace/20_links-external.md`; `workspace/20_links-internal.md` | Changed public destinations are inventoried and verified for intended purpose. | Current locations and dated destination evidence in both registers. | Updated rows locate current text, but no external destination tests are recorded. | `intentionally deferred` | Register inspection, 2026-09-21 | ACT-009, ACT-019 |

## Findings created or updated

| ID | Status | Severity | Release impact | Summary | Evidence | Run follow-up |
| --- | --- | --- | --- | --- | --- | --- |
| PUB-002 | `needs-verification` | medium | publication blocker | Eight Advanced draft files remain absent from the coverage register. | `workspace/19_publication-coverage.md`; `publish/mfb-adv-26.10/`. | Retain the existing finding; add explicit deferred/non-release entries and owner before release. |
| ACT-002, ACT-003 | `in-progress` / `blocked` | critical | certificated-delivery blocker | Calibration and local record/certificate governance remain conditions for certificated delivery. | Existing detailed action records. | No change to status from this text review. |
| ACT-009, ACT-019 | `needs-verification` / `blocked` | high | publication blocker | External destinations and final publication verification have not been performed. | Link registers and existing action records. | Complete their recorded verification conditions. |
| ACT-013 | `in-progress` | medium | maintenance | Visual production evidence, including the Sanity licence mark, is not demonstrated by source-marker alignment. | `workspace/08_assets.md` and existing action record. | Complete asset rights/production checks. |

## Verification requests for an internet-connected AI agent

### VER-001: Changed public destinations and optional-pathway wording

```text
You are an internet-connected verification agent. Verify the public destinations whose wording or purpose changed in the 2026-09-21 workspace-to-publication synchronization review, without changing project files.

Item to verify: the URLs in the Student Guide, Educator Guide, and [Educator Quick Start](https://programs.myfirstbitcoin.org/programs/bitcoin-diploma/en/educator-quick-start/) for Introduction to Bitcoin, Educator Training Program, Bitcoin Education Network/Leaderboard, student journey, the My First Bitcoin App, contribution forms, the curriculum repository, and any issuer-specific certificate-verification instruction actually supplied by an educator.
Intended purpose in the curriculum: provide optional further-learning, contribution, and app routes without creating a completion, membership, endorsement, or central-certificate-verification promise.
Required source standard: official My First Bitcoin, Bitcoin Education Network, official service, or official repository page for each destination; issuer-specific verification can pass only when the actual named issuer supplies a documented process.
Check date: 2026-09-21
Acceptance condition: every retained destination opens and matches its stated optional purpose; no destination or surrounding public copy implies that it is required for Diploma completion or that My First Bitcoin centrally verifies educator-issued certificates.

Return: pass, fail, or uncertain for each item; source title; direct URL; relevant result or a short copyright-compliant quotation; check date; and a concise explanation of whether the destination matches its intended purpose. Identify redirects, restrictions, stale information, or uncertainty. Do not infer approval and do not edit files.
```

### Returned verification evidence

| VER-ID | Outcome | Source title and direct URL | Check date | Evidence summary | Related finding or matrix row |
| --- | --- | --- | --- | --- |
| VER-001 | pending | — | 2026-09-21 | No internet-connected destination check performed in this run. | TR-008; ACT-009, ACT-019 |

## Editor-discretion judgements

| Subject | Editor decision | Rationale and internal evidence | Date | Related finding or matrix row |
| --- | --- | --- | --- | --- |
| Synchronization of the new duration, certification, programme-link, wallet-guidance, and pre-reading propositions | Sufficiently aligned in the checked dependent publications. | The commit-range diff and current text show intentional, audience-appropriate propagation to the Student Guide, Educator Guide, Assessment Grid, Quick Start, and affected activity files. | 2026-09-21 | TR-001, TR-003–TR-005 |
| Advanced coverage gap | Still unresolved. | The coverage register includes only the Advanced README placeholder, while eight draft modules remain in `publish/mfb-adv-26.10/`. | 2026-09-21 | TR-007; PUB-002 |

## Checks completed

- [x] Authority, mode, scope, baseline, and final source version checked.
- [x] Changed-proposition inventory and impact map completed.
- [x] Relevant Student Guide, Educator Guide, Assessment Grid, Quick Start, activity, asset, coverage, and link-register evidence cross-read.
- [x] Former-wording and related-variant impact searches completed.
- [x] Publication repository-only-link policy checked for the affected material.
- [x] Fixed-point check completed after recording this run: the review-record additions created no new curriculum or publication dependency.

## Checks not performed or deferred

External destination testing, Sanity rendering, visual-rights confirmation, PDF rendering, accessibility/phone/screen-reader testing, real-cohort delivery, assessor calibration, and local governance approval were not performed. These are recorded in `ACT-002`, `ACT-003`, `ACT-009`, `ACT-013`, and `ACT-019` and remain relevant to release readiness.

## Review report summary

Change review completed on 2026-09-21 for the bounded range `a3947ea..b089f37`, after the latest full-release alignment run. The eight substantive `CHG-` propositions have recorded dispositions: duration, October outputs, educator-issued certification, optional programme links, qualified wallet guidance, permitted pre-reading, and the Sanity licence marker are implemented or intentionally deferred in the appropriate audience-specific materials. The changed publication set includes the Student Guide, Educator Guide, Assessment Grid, Quick Start, and Activities 006 and 017; these updates are material, not merely matching filename churn. Concurrent unstaged edits that appeared after the review began were not folded into this commit-range conclusion. The only unresolved publication-alignment finding is the existing `PUB-002`: eight Advanced drafts remain unclassified individually in the coverage register. External destination verification, production/rendering, accessibility, delivery, calibration, and local-governance checks were not performed. The fixed-point synchronization check passed for this bounded review. This run record is not a source of truth.
