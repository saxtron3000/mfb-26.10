# Review run: 2026-09-21 — full release alignment

## Run details

| Field | Record |
| --- | --- |
| Mode | `full-release` |
| Scope | Every `workspace/` and `publish/` document or publication data file; both link registers; traceability matrix; mission, scope, assessment, certification, publication, and release controls |
| Requested by | User |
| Reviewer | Codex |
| Source version | Working tree on 2026-09-21 |
| Workspace authority version | `workspace/00_index.md` through `workspace/20_links-internal.md`; publication set listed in `workspace/19_publication-coverage.md` |
| Scripts used | `review_alignment.md` |
| Started / completed | 2026-09-21 / 2026-09-21 |

## Traceability matrix

| TR-ID | Governing workspace file and heading | Requirement or decision | Expected publication or operational evidence | Actual evidence | State | Verification method and date | Related finding |
| --- | --- | --- | --- | --- | --- | --- | --- |
| TR-001 | `workspace/06_plan.md`, `## 2. Four-Module Architecture` | The Diploma uses Problem → Solution → Action → Connect; all four modules are required and Module 4 is educator-curated. | Student Guide, Educator Guide, and Assessment Grid preserve the four-module route and `C11`. | Current guides state the four-module route and Module 4 local role; grid records C11. | `implemented` | Authority/publication cross-read 2026-09-21 | none |
| TR-002 | `workspace/05_competencies.md`, `## Assessed competencies and required observable criteria` | All decimal criteria map to observable evidence, approved tasks, rubrics, and record fields. | Educator protocol and grid agree on C1–C11, theory/practice evidence, and direct observation. | Protocol and grid exist; operational route, calibration, and governance evidence remain pending. | `intentionally deferred` | Cross-read 2026-09-21 | ACT-001, ACT-002, ACT-003 |
| TR-003 | `workspace/13_assessment.md`, `## 3. Assessment components` | Theory C1–C8 and practice C9–C11 are equal-status, non-compensatory gates; self-checks are not evidence. | Guides and grid state the same completion rule. | Current publications preserve separate gates and exclude app use, attendance, and self-report as evidence. | `implemented` | Cross-read 2026-09-21 | ACT-017 |
| TR-004 | `workspace/16_spec.md`, `## Materials And Outputs` | October includes low-tech print/PDF, online PDF, and web outputs through Sanity; future instructional branches remain distinct. | `06_plan.md`, `03_scope.md`, public overview, and publication register use the same release boundary. | `03_scope.md` and `16_spec.md` include October online outputs; `06_plan.md` still places online PDF/web among future branches. | `conflict` | Ordered authority comparison 2026-09-21 | EVO-001, ACT-015 |
| TR-005 | `workspace/15_certification.md`, `## Governance And Verification Still To Define` | Public certificate verification remains an implementation decision until an approved process exists. | Student Guide must not imply a live verification service or settled process. | Student Guide gives conditional verification instructions and retains a certificate-verification section; no approved process is evidenced. | `conflict` | Authority/publication cross-read 2026-09-21 | PUB-001, ACT-008, ACT-003 |
| TR-006 | `workspace/14_microlearning-plan.md`, `## Phase 1 minimal viable product` | The 12-question self-check samples Modules 1–3, is voluntary, and does not establish practical or Module 4 competence. | Published data and CSV exports preserve scope, item mapping, and non-assessment wording. | Scope and non-assessment guardrails are present; independent factual, phone, and screen-reader checks remain pending. | `intentionally deferred` | Cross-read 2026-09-21 | ACT-011 |
| TR-007 | `workspace/20_links-external.md`, `## Review instructions`; `workspace/20_links-internal.md`, `## Review instructions` | Every retained destination must be inventoried, dated, tested for purpose, and recorded as checked. | Both registers have current snapshot, complete locations, destination, status, and evidence. | Both registers remain dated 18 September with all rows pending; no external destination evidence is recorded. | `missing` | Register inspection 2026-09-21 | ACT-009, ACT-019 |
| TR-008 | `workspace/08_assets.md`, `## 3. Visual index` | Essential visuals require produced files or approved replacements, rights, alt text, source, and review status. | Visual references resolve and production status is recorded. | `BD-V-001` still points to absent `assets/diploma/bd-v-001.svg`; other visual entries are briefs, not production evidence. | `missing` | Asset inventory/register inspection 2026-09-21 | ACT-012, ACT-013 |
| TR-009 | `workspace/16_spec.md`, `## Assessment And Certification`; `workspace/15_certification.md` | Teaching-package readiness, publication readiness, validated delivery, and certificate issuance must remain distinct. | Public claims and release controls distinguish those states. | Written protocol is present, but cohort validation, calibration, governance, and operational issuance evidence are not present. | `missing` | Cross-read 2026-09-21 | ACT-001, ACT-002, ACT-003, ACT-017 |
| TR-010 | `workspace/19_publication-coverage.md`, `## Publication set` and `## Maintenance check` | Every curriculum-content file in `publish/` is either covered by the publication register or explicitly deferred outside the current release. | Advanced drafts and the Educator Quick Start have a recorded publication status and planning authority. | Eight `publish/mfb-adv-26.10/mfb-adv-*.md` files and `publish/mfb-bd-26.10/mfb-bd-qs-26.10.md` are not listed in the coverage register, while the Advanced README says Advanced modules are not current beginner publication. | `missing` | Publication inventory/register comparison 2026-09-21 | PUB-002 |

## Findings created or updated

| ID | Status | Severity | Release impact | Summary | Evidence | Run follow-up |
| --- | --- | --- | --- | --- | --- | --- |
| EVO-001 | `needs-verification` | high | publication blocker | October online PDF/web outputs are current in `03_scope.md` and `16_spec.md`, but `06_plan.md` still lists them in future branches. | Earlier/later authority comparison recorded in `review_todo.md`; see current headings cited in the matrix. | Reconcile `06_plan.md`, related design/public wording, and `DEC-07` before final release copy. |
| PUB-001 | `needs-verification` | high | publication blocker | Student Guide certificate-verification section describes conditional verification steps without an approved public verification process in `15_certification.md`. | Student Guide `### Certificate verification`; `15_certification.md` `## Governance And Verification Still To Define`; `ACT-008`. | Remove or reduce to approved learner language after the certification-governance decision; do not publish a QR or verification destination without process evidence. |
| PUB-002 | `needs-verification` | medium | publication blocker | Publication coverage does not list eight Advanced draft modules or the Educator Quick Start, although they are present under `publish/`. | Inventory comparison against `workspace/19_publication-coverage.md`; `publish/mfb-adv-26.10/README.md` says Advanced modules are not part of the current beginner publication. | Mark these files explicitly deferred and non-release, add them to the coverage register with owner/status, or relocate them through an authorized scope decision. |
| ACT-001, ACT-002, ACT-003, ACT-004, ACT-008, ACT-009, ACT-011, ACT-012, ACT-013, ACT-015, ACT-016, ACT-017, ACT-019 | `needs-verification` | high/critical | certificated-delivery blocker / publication blocker / required before cohort | Existing release controls remain open after alignment review. | Current action register and matrix rows TR-002, TR-004–TR-009. | Complete each acceptance condition and retain dated evidence. |

## Verification requests for an internet-connected AI agent

### VER-001: External destinations and public claims

```text
You are an internet-connected verification agent. Verify the retained external destinations and changing public claims listed in workspace/20_links-external.md and workspace/20_links-internal.md without changing project files.

Item to verify: every listed URL, anchor, query string, form, activity destination, programme page, Leaderboard page, donation/support destination, certificate-related destination, and current public claim used by the Student Guide or Educator Guide.
Intended purpose in the curriculum: provide accurate, safe, optional learning, contribution, community, resource, and publication routes without implying endorsement, membership, certificate verification, or financial advice.
Required source standard: primary or official publisher/service source for each destination; use My First Bitcoin, Bitcoin Education Network, official activity publisher, or official service pages as applicable.
Check date: 2026-09-21
Acceptance condition: each destination opens, matches its linked purpose and audience, preserves required query strings/anchors, is accessible enough for its stated use, and does not create an unsupported programme, donation, membership, or certificate promise.

Return: pass, fail, or uncertain for each destination; source title; direct URL; relevant result or a short copyright-compliant quotation; check date; and a concise explanation. Identify redirects, access restrictions, stale information, broken anchors, changed forms, or uncertainty. Do not infer approval and do not edit files.
```

### Returned verification evidence

| VER-ID | Outcome | Source title and direct URL | Check date | Evidence summary | Related finding or matrix row |
| --- | --- | --- | --- | --- | --- |
| VER-001 | pending | — | 2026-09-21 | No internet-connected destination check performed in this run. | TR-007; ACT-009, ACT-019 |

## Editor-discretion judgements

| Subject | Editor decision | Rationale and internal evidence | Date | Related finding or matrix row |
| --- | --- | --- | --- | --- |
| Mission alignment | Current learner-facing material generally preserves learner choice, safety, Bitcoin-only scope, and non-financial-advice boundaries. | Student Guide states that learners may choose freely and that the Diploma does not require adoption, app use, purchases, or personal funds; comparison content is bounded. | 2026-09-21 | TR-001, TR-003 |
| Certificate wording | Conditional certificate-verification instructions are not sufficient evidence of an approved verification process. | `15_certification.md` explicitly keeps public verification in governance decisions still to define. | 2026-09-21 | TR-005, PUB-001 |

## Checks completed

- [x] Authority and scope checked.
- [x] Ordered workspace/publication alignment checked where relevant.
- [x] Mission, six principles, architecture, assessment, certification, optional resources, and release positioning checked.
- [x] Publication cross-reference policy checked.
- [x] Traceability matrix completed.
- [x] Findings and verification request recorded.
- [ ] External destinations verified.
- [ ] Rendering, accessibility, phone, screen-reader, real-cohort timing, calibration, and governance-pack checks performed.

## Checks not performed or deferred

External URL and current-claim verification, rendered output inspection, accessibility and phone testing, screen-reader testing, real-cohort timing, assessor calibration, and certificate-governance approval were not performed. These deferrals affect release readiness and remain linked to the existing action register.

## Review report summary

Full-release alignment review completed 2026-09-21. The four-module pathway, Bitcoin-only educational scope, learner-choice boundaries, optional app position, and separate theory/practice assessment model align across the current authorities and publications. Release remains blocked by unresolved assessment operations and governance, the October output-scope conflict, certificate-verification wording without an approved process, incomplete publication coverage, pending external-link verification, missing visual production evidence, and unperformed delivery/accessibility checks. This run record is evidence of the review process, not a source of truth.
