# Consolidated review actions and decision register

## To-do qualification and tally

The table below classifies all 21 `ACT` tasks in this register. **CRITICAL** and **MAJOR** remain release concerns; **MINOR** covers bounded maintenance or editorial work; **DONE** means the task is checked off with completion evidence.

| Category | Qualification | Tally | Tasks |
|---|---|---:|---|
| **CRITICAL** | Safety, governance, certificate-integrity, or certificated-delivery blocker. | **3** | `ACT-002`, `ACT-003`, `ACT-017` |
| **MAJOR** | Release, publication, or required-before-cohort blocker that must be resolved before the affected delivery or publication claim. | **9** | `ACT-004`, `ACT-006`, `ACT-008`, `ACT-009`, `ACT-011`, `ACT-015`, `ACT-016`, `ACT-019`, `ACT-020` |
| **MINOR** | Bounded editorial, maintenance, quality, or follow-up work that does not by itself block release readiness. | **7** | `ACT-007`, `ACT-010`, `ACT-012`, `ACT-013`, `ACT-014`, `ACT-018`, `ACT-021` |
| **DONE** | Checked off and supported by completion evidence in the task record. | **2** | `ACT-001`, `ACT-005` |
| **Total** | All consolidated `ACT` tasks. | **21** | — |

Classification follows the task’s current severity, release impact, status, and acceptance condition. A **MINOR** task is still required work unless its record is explicitly closed, rejected, or superseded.

## Review dashboard

| Area | Current status | Outstanding | Priority / next move |
|---|---|---:|---|
| Overall action register | 2 of 21 `ACT` items checked off | 19 | Treat the register as open; record status, owner, evidence, and dependencies as work proceeds. |
| Release blockers | Open | 2 (`ACT-002`–`ACT-003`) | **Major issue:** calibrate assessors and approve record/certificate governance before certificated delivery or a results-retaining pilot. |
| Decisions blocking dependent copy | Open | 2 (`ACT-004`, `ACT-006`) | **Major issue:** settle duration and the policy for named programme links and wallet-software guidance. Certificate positioning is resolved; documentation remains in `ACT-020`. |
| Cross-cutting release reconciliation | Open | 3 (`ACT-015`–`ACT-017`) | **Major issue:** reconcile publication outputs, the Lightning explanation/practice boundary, and the operational release promise across authorities and public materials. |
| Quick wins / bounded editorial fixes | Open | 4 candidate items (`ACT-008`, `ACT-009`, `ACT-011`, `ACT-012`) | **Quick wins:** remove or finalize conditional back matter, verify public destinations, finish the bounded self-check review, and repair or replace the missing visual target. Confirm decisions and evidence before closing. |
| Publication and maintenance work | Open | 5 (`ACT-007`, `ACT-010`, `ACT-013`, `ACT-019`, `ACT-020`) | **Minor-to-medium issues:** document the certification model, add slide support, stabilize source/lexicon references, control visual production, and run the final publication verification pass. |
| Decision-register maintenance | Open | 1 (`ACT-014`) | **Medium issue:** triage `DEC-01`–`DEC-12`; close already-resolved questions with evidence and retain historical alternatives without reopening settled policy. |
| Assessment simplification | Open | 1 (`ACT-021`) | Consolidate eleven assessed competencies into seven, with useful sub-points only; review the grid first, then align the guides and planning authorities. |
| Historical annotation triage | Not yet triaged | 242 `ANN` items | **Large workstream:** compare each note with current text and source evidence; preserve approvals, link approved actions, and flag unclear handwriting for clarification. |
| Source-marker interpretation | Defined only as provenance | Original inventory: 166 `[-]`, 58 `[o]`, 18 `[ ]` markers | Do not treat these markers as current status or approval. Use the documented triage dispositions and evidence instead. |
| Near-term sequence | Ready for triage | — | 1) Resolve blockers and decisions; 2) handle bounded publication fixes; 3) prepare governance/calibration and delivery evidence; 4) complete annotation and final publication checks. |

**Dashboard reading:** “Open” means the item remains unchecked in this file, not that its underlying proposal is approved. “Quick win” describes limited scope, not automatic closure. The dashboard is based on the consolidated register dated 2026-09-19, with action counts updated on 2026-09-21 to include `ACT-021`.

## How to use this document

Consolidated on 2026-09-19 from all nine original files in `review/`. This is the action companion to the repeatable [style script](review_style.md) and [alignment script](review_alignment.md). Original files are preserved for provenance. This consolidation does not certify that an older finding remains open or that an imported suggestion has been approved.

Work in this document for the new review workflow; do not maintain duplicate action lists in the original files. Existing repository links still lead to those original files until a separate migration updates them.

Use the checkbox for completion of the stated task, not for agreement with a suggestion. Use statuses `needs-verification`, `open`, `in-progress`, `blocked`, `done`, `superseded`, and `rejected`. All imported release actions initially have status `needs-verification`; check the current target before doing the work. Record a named owner only when assigned, otherwise use `unassigned`.

Every `ACT-`, `EVO-`, and `PUB-` item must have one structured record directly below it: `Status: … | Owner: … | Updated: YYYY-MM-DD | Severity: critical/high/medium/low | Release impact: certificated-delivery blocker/publication blocker/required before cohort/maintenance/none | Evidence: relative file/section, approved record, or pending verification | Depends on: IDs or none | Completion evidence: …`. Retain the record when an item is complete, rejected, or superseded. Historical `DEC-` and `ANN-` items keep their existing provenance format unless converted into an action.

Use `critical` for a safety, legal-governance, or certificate-integrity risk; `high` for a release-blocking authority or publication problem; `medium` for material quality, delivery, or maintenance work; and `low` for bounded follow-up that does not affect release readiness. Record the actual release impact rather than inferring an approval from severity. Mark `[x]` only when its acceptance condition and structured record show completion. For rejected or superseded proposals, record the disposition and reason rather than implementing them.

Create a dated run record for every review in `review/runs/`, using [runs/template.md](runs/template.md) and the filename `YYYY-MM-DD-<mode>-<scope>.md`. The run record holds the scope, source version, traceability matrix, verification prompts, completed checks, skipped checks, and links to every finding created or updated in this register.

The original to-do allowed completed items to be removed or moved to a dated archive with evidence. In this consolidated workflow, retain their IDs and evidence here or in a linked dated archive, and remove them only from the active queue. This preserves completion history for repeated AI reviews. The annotation checkboxes have the separate triage completion rule described in their section.

Do not invent approvals, reviewer assignments, external verification, pilot results, or completion evidence. Historical notes are inputs to triage, not permission to change policy. Route clear editorial work through the style script and changes to meaning, scope, safety, or assessment through the alignment script.

## Recommended work order

1. Check current authorities and triage the 12 decisions below; retire implemented questions with evidence.
2. Resolve remaining duration, output, certificate, wallet-guidance, and programme-link inconsistencies before changing dependent copy.
3. Prepare the local `P11` route, calibration examples, capacity model, and governance pack. Governance must precede any pilot that retains learner results.
4. Pilot and revise the full learner/educator pathway using observed evidence.
5. Finalize conditional back matter, public destinations, teaching slides, and bounded optional self-check language.
6. Repair source and lexicon maintenance, then produce the essential visuals and run publication checks.
7. Triage historical annotations by module, retaining approvals and unresolved handwriting separately from approved implementation tasks.

## Release and publication actions

Items `ACT-001` onward preserve every action and acceptance condition from the former release list. Headings indicate priority. Paths such as `05_competencies.md` in inherited text refer to `workspace/`; official publication links resolve from this directory.

### Release blockers for certificated delivery

- [x] **ACT-001** **Validate the complete assessment route.**

  - Status: done | Owner: unassigned | Updated: 2026-09-21 | Severity: critical | Release impact: certificated-delivery blocker | Evidence: [Educator Guide assessment protocol](../publish/mfb-bd-26.10/mfb-bd-eg-26.10.md#operational-assessment-protocol), [Assessment Grid assessment route](../publish/mfb-bd-26.10/mfb-bd-assessment-grid-26.10.md#simple-way-to-use-this-grid), and [assessment framework](../workspace/13_assessment.md#6-assessment-workflow) reviewed on 2026-09-21 | Depends on: none | Completion evidence: the current materials define an educator-led activity-based route for every required competency; permit in-person, online, low-tech, simulated, testnet, physical-token, and carefully structured low-stakes routes; provide support and reassessment; preserve accessibility and safety; and require capacity planning for troubleshooting, feedback, and follow-up.

  - Define a simple, educator-led route in which activities are deliberately designed to elicit the required competencies. Successful activity performance may provide the evidence; the educator may use probing questions when understanding or safety is unclear.
  - Permit in-person, online, low-tech, simulated, testnet, physical-token, and carefully structured low-stakes-funds routes, with accessibility adaptations that preserve the competency. Do not require significant personal funds or a particular tool.
  - Give each learner a fair opportunity to ask for support and to demonstrate the competency. If a learner is `NY` (**Not Yet**), arrange another assessment opportunity during class, a break, an additional call, or a follow-up session.
  - Consider cohort capacity and assessment time when planning delivery, including troubleshooting, extra assistance, feedback, reassessment, and follow-up. Use extended sessions or additional meetings where needed; no fixed educator-to-learner ratio is required.
  - Treat piloting as an ideal quality-improvement activity, not a prerequisite for educators to issue certificates. The first cohort may be the first live validation of the route.
  - Acceptance: the Educator Guide gives educators a practical, flexible assessment route that assesses every required competency, supports reassessment, accommodates access constraints, and makes time and follow-up planning explicit without imposing unnecessary recording or pilot requirements.

- [ ] **ACT-002** **Prepare assessor calibration evidence.**

  - Status: in-progress | Owner: unassigned | Updated: 2026-09-21 | Severity: critical | Release impact: certificated-delivery blocker | Evidence: [Educator Guide calibration examples](../publish/mfb-bd-26.10/mfb-bd-eg-26.10.md#calibration-examples-for-assessor-discussion) added for `T2`, `P9`, and an example `P11` variant; assessor session record still pending | Depends on: ACT-001 | Completion evidence: pending independent scoring, discussion, and recorded agreement by the selected delivery team.

  - Create one annotated `MS` and one annotated `NY` example for `T2`, `P9`, and the selected `P11` variant.
  - Calibrate assessors, resolve scoring differences, and retain the date, assessors, variants, and agreed interpretation.
  - Acceptance: the selected delivery team has completed and recorded the Educator Guide's minimum calibration process.

- [ ] **ACT-003** **Approve record and certificate governance.**

  - Status: needs-verification | Owner: unassigned | Updated: 2026-09-21 | Severity: critical | Release impact: certificated-delivery blocker | Evidence: pending current verification | Depends on: none | Completion evidence: acceptance condition below.

  - Define issuer and approval authority; permitted data; consent or assent; access roles; retention and deletion; correction, appeal, incident, outage, and exceptional-case routes; assessor permissions, moderation, reconciliation, and audit trail; certificate issue, replacement, revocation, and verification; and rules for minors and safeguarding.
  - Acceptance: an approved, proportionate governance pack exists before competency evidence is retained for certification or a pilot.

### Decisions required before dependent copy is final

- [ ] **ACT-004** **Decide what “approximately eight hours” means.** Choose either a fixed complete-contact cap or a planning baseline that may expand when valid evidence requires it. Align `05_competencies.md`, `03_scope.md`, `06_plan.md`, the Educator Guide, Student Guide, and `16_spec.md`.

  - Status: needs-verification | Owner: unassigned | Updated: 2026-09-21 | Severity: high | Release impact: publication blocker | Evidence: pending current authority review | Depends on: none | Completion evidence: acceptance condition below.

  - Acceptance: all authorities and public schedule claims use one rule.

- [x] **ACT-005** **Decide the 2026.10 certificate position.** Educators may issue certificates in the 2026.10 release after assessing learners with the assessment grid. Certification is decentralized: the educator is responsible for the assessment decision, and My First Bitcoin does not centrally issue or guarantee the learner’s competency.

  - Status: done | Owner: unassigned | Updated: 2026-09-19 | Severity: high | Release impact: publication blocker | Evidence: user-approved certification policy recorded in this review discussion | Depends on: ACT-020 | Completion evidence: approved certificate position recorded above.

- [ ] **ACT-006** **Approve a short publication policy for named programme links and general wallet-software guidance.** Define which optional My First Bitcoin pathways may appear in learner material, how often links are checked, and how general software-verification guidance is localized without becoming a global product recommendation.

  - Status: needs-verification | Owner: unassigned | Updated: 2026-09-21 | Severity: high | Release impact: publication blocker | Evidence: pending current policy review | Depends on: none | Completion evidence: acceptance condition below.

  - Acceptance: the policy is recorded and Student Guide wording follows it.

- [ ] **ACT-020** **Document the decentralized educator-issued certification model.** Define and publish the two certificate types: **participation** for attendance without a successful assessment, and **completion** for a learner who has passed the required assessment. State that any educator may issue the certificate; the educator must use the assessment grid as the minimum process, while retaining assessment traces during the cohort is advisable but not required. A completion certificate confirms that the educator judged the learner to have passed; it is not a competency guarantee or centrally verified certificate from My First Bitcoin.

  - Status: needs-verification | Owner: unassigned | Updated: 2026-09-21 | Severity: high | Release impact: publication blocker | Evidence: pending current implementation review | Depends on: ACT-005 | Completion evidence: acceptance condition below.

  - Use the current [Canva certificate template](https://canva.link/55s417wnb9ehdwo) as the present template reference. Use “My First Bitcoin Diploma” as the programme wording, and show an ETP-completion badge beside the educator’s name when applicable.
  - Add the learner-facing explanation to the Student Guide, the full educator procedure and certificate distinction to the Educator Guide, a footnote to the assessment grid, and aligned guidance in the relevant `workspace/` authorities. Do not publish internal plans for future certification tooling or CRM integration.
  - Acceptance: the two certificate types, educator responsibility, assessment-grid minimum, optional evidence retention, ETP badge treatment, and My First Bitcoin’s non-guarantee/non-central-issuer role are consistent across all listed materials.

### Publication and maintenance actions

- [ ] **ACT-021** **Consolidate assessed competencies from `C1`–`C11` into `C1`–`C7`.** Resume the seven-competency proposal discussed with the user, starting with the assessment grid. Earlier edits were rolled back; check the current files before implementing and do not treat prior drafts as completed work.

  - Status: open | Owner: unassigned | Updated: 2026-09-21 | Severity: medium | Release impact: maintenance | Evidence: user instruction and consolidation mapping recorded in this item | Depends on: none | Completion evidence: pending implementation and consistency checks.

  | New competency | Original competencies | Suggested assessment breakdown |
  |---|---|---|
  | `C1` Money and modern-money trade-offs | `C1` + `C2` | Up to three points: why money is used and its functions/properties; comparison of two forms of money; one local or realistic modern-money trade-off. |
  | `C2` Bitcoin foundations and rules | `C3` + `C4` | Up to three points: digital copying and shared verification; beginner rules and network roles; money properties with a reasoned benefit or limitation. Keep technical depth achievable for beginners. |
  | `C3` Bitcoin and digital-asset comparison | `C5` | One guided comparison statement, without numbered sub-points: compare Bitcoin with another digital asset using relevant criteria and a trade-off, and distinguish learning from speculation or promotion. Retain this competency and its title. |
  | `C4` Wallets, custody, and safety | `C6` + `C7` | Up to three points: public/secret information and custody choices; wallet types; recognising a risk and knowing when to stop, verify, or seek help. |
  | `C5` Payment and access pathways | `C8` | Two points where useful: compare on-chain and Lightning payments in a guided example; compare access or exchange pathways and their risks. |
  | `C6` Safe access and recovery readiness | `C9` + `C10` | Two distinct practical points: supported wallet access and receipt with checks; recovery readiness using prepared or simulated materials. |
  | `C7` Local Bitcoin-as-money task | `C11` | Two points where useful: safely perform a locally relevant task or simulation; explain its purpose, alternative, trade-offs, possible failure, and safe next step. |

  - Use zero, one, two, or at most three numbered sub-points per competency only where they help an educator distinguish important skills or identify what needs further practice. Do not default to three or turn each sub-point into a separate exam or result. Use plain, inviting language and retain one `MS`/`NY` judgement per parent competency.
  - Preserve required learning and safety through an explicit old-to-new criterion mapping. Consolidation alone does not remove content or reduce the standard. Flag any proposed scope reduction separately, including any decision to drop a criterion. Keep theory as new `C1`–`C5` and practice as new `C6`–`C7`; do not convert these into numerical weights.
  - Make Page 2 usable on its own, with short competency descriptions and explanations of `MS`, `NY`, practical observation, and completion. Add a brief example of sufficient beginner performance per competency in the educator support material, especially for the broad `C2` and practical `C6`–`C7` groups.
  - Review the proposed grid first, then align [competencies](../workspace/05_competencies.md), [assessment framework](../workspace/13_assessment.md), [Educator Guide](../publish/mfb-bd-26.10/mfb-bd-eg-26.10.md), [Student Guide](../publish/mfb-bd-26.10/mfb-bd-sg-26.10.md), and other active planning, assessment, certification, asset, and self-check mappings where affected. Check decimal criterion and task references explicitly; preserve historical codes as labelled provenance rather than globally replacing numbers. Keep formative competencies distinct from the seven completion requirements.
  - Coordinate with `ACT-001` and `ACT-020` so consolidation preserves the agreed activity-based assessment, support and reassessment opportunities, and participation/completion distinction.
  - Acceptance: seven clear parent competencies cover the mapped required learning; sub-points are selective and never exceed three per competency; Page 2 is self-contained; all active code, criterion, and completion references agree; the old-to-new mapping and verification evidence are retained. No rolled-back draft or untested delivery claim is presented as completed validation.

- [ ] **ACT-007** **Introduce teaching slides as visual support in the Educator Guide.** Provide a basic, editable slide set aligned with the curriculum and link it from the [Educator Guide](../publish/mfb-bd-26.10/mfb-bd-eg-26.10.md). Explain that My First Bitcoin recommends using the slides to give lessons structure, support visual learning, and reinforce key concepts. Encourage educators to adapt and personalise them for their learners, language, and local context while preserving required competencies and safety guidance.

  - Status: needs-verification | Owner: unassigned | Updated: 2026-09-21 | Severity: medium | Release impact: maintenance | Evidence: pending current publication review | Depends on: none | Completion evidence: acceptance condition below.

  - Acceptance: the Educator Guide introduces and links the slide set, explains its recommended use, and gives clear adaptation guidance. Slides support discussion and practical learning, and teaching remains possible without projection equipment.

- [ ] **ACT-008** **Finalize or remove conditional Student Guide back matter.** Resolve `Source or update page, if included`, `Optional donate / support QR`, and `Certificate verification`. Do not publish a QR, support destination, or certificate-verification explanation without a tested, approved destination or process.

  - Status: needs-verification | Owner: unassigned | Updated: 2026-09-21 | Severity: high | Release impact: publication blocker | Evidence: pending current publication review | Depends on: ACT-020 | Completion evidence: acceptance condition below.

  - The report requires a real, privacy-preserving certificate process before retaining the verification section. A live link alone is insufficient.
  - Acceptance: every retained section has a learner-facing heading and a verified destination or governing process; unavailable sections are removed.

- [ ] **ACT-009** **Verify changing public destinations before publication.** Check every named programme, form, case-study, network, leaderboard, source, and support link in the Student Guide.

  - Status: needs-verification | Owner: unassigned | Updated: 2026-09-21 | Severity: high | Release impact: publication blocker | Evidence: pending dated external verification | Depends on: ACT-006 | Completion evidence: acceptance condition below.

  - Acceptance: each retained destination is live, appropriate, and recorded as checked for the edition.

- [ ] **ACT-010** **Replace mutable source and terminology locations.** Convert `09_resources.md` and the Lexicon from line-number locations to stable section anchors or claim IDs. Keep occurrence audits separate from learner-term definitions. Expand the shared-claim register with source authority, volatility, reviewer, check date, next review date, and publication treatment.

  - Status: needs-verification | Owner: unassigned | Updated: 2026-09-21 | Severity: medium | Release impact: maintenance | Evidence: pending current source-maintenance review | Depends on: none | Completion evidence: acceptance condition below.

  - Preserve each claim or section, source type and authority, volatility, reviewer, date checked, next review date, and permitted learner-facing treatment. Keep genuinely local and changing facts in the Educator Guide's local verification record. Maintain the resource register and lexicon as versioned tools, with first/later occurrence audits in separate reports.
  - Acceptance: the source register and lexicon remain correct after a normal manuscript edit without manual line-number repair.

- [ ] **ACT-011** **Complete the optional self-check review.** Replace “You have a strong foundation” with wording limited to the 12-question self-check. Independently review all 12 items for facts and editorial quality; test the all-questions-on-one-screen experience on a small phone and with a screen reader.

  - Status: needs-verification | Owner: unassigned | Updated: 2026-09-21 | Severity: high | Release impact: publication blocker | Evidence: score message updated in `publish/mfb-ml-26.10/mfb-ml-26.10.md`; factual, small-phone, and screen-reader review still pending | Depends on: none | Completion evidence: acceptance condition below.

  - The report identified that message at the 10–12 score band and suggested “You showed a strong result on this quick self-check.” Preserve item mappings to the Student Guide. The check samples selected content from Modules 1–3 and does not assess Module 4 or observed practical skills. This is a publication action, not a certification blocker; the example is historical evidence, not approval for a new pass threshold.
  - Acceptance: reviewed item metadata is complete, the result message does not imply Diploma competence, and no score tracking, threshold, or educator access is introduced.

- [ ] **ACT-012** **Repair the missing local visual target.** `workspace/08_assets.md` references the absent `../assets/diploma/bd-v-001.svg` Creative Commons mark.

  - Status: needs-verification | Owner: unassigned | Updated: 2026-09-21 | Severity: medium | Release impact: publication blocker | Evidence: pending local-link and visual review | Depends on: none | Completion evidence: acceptance condition below.

  - Acceptance: add the approved asset during visual production or replace the embedded image with a non-broken placeholder; rerun the local-link check.

- [ ] **ACT-013** **Control visual production scope.** Select the essential visual set before commissioning work. Track file, rights, alt text, source, and review status. Keep conditional QR code and certificate-verification visuals out of production until their destinations and processes are approved.

  - Status: needs-verification | Owner: unassigned | Updated: 2026-09-21 | Severity: medium | Release impact: maintenance | Evidence: pending visual-production review | Depends on: ACT-008 | Completion evidence: acceptance condition below.

  - Acceptance: an approved essential-visual list and production tracker exist.

### Review-register maintenance

- [ ] **ACT-014** **Triage the consolidated decision register.** The original action targeted the archived consistency register; perform it on `DEC-01`–`DEC-12` here. Verify and mark questions 2, 3, 4, 5, and 10 as resolved, retaining their evidence and historical alternatives. Keep only questions that still require an owner response in the active decision queue.

  - Status: needs-verification | Owner: unassigned | Updated: 2026-09-21 | Severity: medium | Release impact: maintenance | Evidence: pending current decision-register review | Depends on: none | Completion evidence: acceptance condition below.

  - Acceptance: the active decision queue contains no question whose implemented answer is already established in the active authorities. Historical alternatives remain clearly labeled and do not reopen settled policy. Do not maintain a second live queue in the original file.


### Actions recovered from the report and decision log

- [ ] **ACT-015: Reconcile October publication outputs.** The older report asks whether online PDF and web outputs belong to October. On 2026-09-19, `workspace/03_scope.md` and `workspace/16_spec.md` explicitly include both through Sanity, while `workspace/06_plan.md` still lists them among future branches. Verify the approved scope and reconcile remaining architecture/design/public wording. Keep online cohort, self-paced, optional app, and cross-modal instructional branches distinct from publication formats.

  - Status: needs-verification | Owner: unassigned | Updated: 2026-09-21 | Severity: high | Release impact: publication blocker | Evidence: pending workspace authority review | Depends on: DEC-07 | Completion evidence: acceptance condition below.

  - Acceptance: release criteria and all affected authorities describe the same approved outputs, and source-to-Sanity maintenance is explicit. Link completion to `DEC-07`.

- [ ] **ACT-016: Verify the required Lightning boundary.** Review `C8.1`, the architecture, Student Guide, assessment tasks, local `P11` variants, lexicon, and resource activities to distinguish required explanation from required use.

  - Status: needs-verification | Owner: unassigned | Updated: 2026-09-21 | Severity: high | Release impact: required before cohort | Evidence: pending workspace and assessment review | Depends on: DEC-06 | Completion evidence: acceptance condition below.

  - Acceptance: the current answer to `DEC-06` is evidenced and consistently reflected in teaching and assessment without imposing an unapproved practical requirement.

- [ ] **ACT-017: Confirm operational release positioning.** Reconcile `DEC-11` and `DEC-12` with the governance and delivery blockers, distinguishing a provisional teaching package, assessment-ready materials, validated delivery, and actual certificate issuance.

  - Status: needs-verification | Owner: unassigned | Updated: 2026-09-21 | Severity: critical | Release impact: certificated-delivery blocker | Evidence: pending workspace and publication review | Depends on: ACT-001, ACT-003, DEC-11, DEC-12 | Completion evidence: acceptance condition below.

  - Acceptance: scope, research, assessment, certification, overview, horizon, and public claims use the same release promise; no certificate readiness is inferred from a written protocol alone.

- [ ] **ACT-018: Complete annotation triage.** Review every `ANN` item below against current text and retained approvals. Resolve ambiguous handwriting against the original annotated PDF where available; do not guess or assign the unclear reviewer handle.

  - Status: needs-verification | Owner: unassigned | Updated: 2026-09-21 | Severity: medium | Release impact: maintenance | Evidence: pending annotation triage | Depends on: none | Completion evidence: acceptance condition below.

  - Acceptance: every annotation has a disposition and evidence. Approved work has an existing or new action ID with a concrete acceptance condition; duplicated notes link to the same action; unclear notes remain explicitly blocked on clarification.

- [ ] **ACT-019: Complete the final publication verification pass.** Run the recurring checks below on the selected edition and capture evidence for external destinations, current claims, rendering, accessibility, and translation readiness as applicable.

  - Status: needs-verification | Owner: unassigned | Updated: 2026-09-21 | Severity: high | Release impact: publication blocker | Evidence: pending dated full-release review | Depends on: ACT-008, ACT-009, ACT-011, ACT-012, ACT-013 | Completion evidence: acceptance condition below.

  - Acceptance: the edition has a dated verification record distinguishing passed checks, remaining blockers, and checks not performed. No historical audit count is presented as a fresh result.

## Decision register

The following register preserves all 12 questions, alternatives, affected-file lists, and the reconciliation order from the 2026-08-19 consistency review. Its descriptions of file contents are historical evidence, not a fresh statement of current policy. Preserve the alternatives for traceability; do not ask for A/B choices already implemented.

| ID | Consolidation disposition and next step |
|---|---|
| DEC-01 | Verify the remaining fixed-duration versus planning-baseline conflict; linked to the duration release action. |
| DEC-02 | Recorded resolved: equal-status, non-compensatory theory and practical gates, no combined grade. Regression check only. |
| DEC-03 | Recorded resolved: all four modules required, with educator-selected and locally relevant Module 4. Regression check only. |
| DEC-04 | September report says supported demonstration is implemented. Verify and close the stale question with current evidence. |
| DEC-05 | September report and current `C9.3` specify supported low-stakes or simulated first access. Verify dependencies and close the stale question. |
| DEC-06 | Verify explanation versus practice boundary; see `ACT-016`. |
| DEC-07 | Current scope and specification include October online PDF/web publication through Sanity; reconcile remaining future-branch wording under `ACT-015`. |
| DEC-08 | Verify approved general wallet-software wording policy; retain trade-offs and non-endorsement. |
| DEC-09 | Verify approved optional programme-pathway and link-maintenance policy. |
| DEC-10 | Historical A and B now show the same filename. Current canonical Student Guide is `publish/mfb-bd-26.10/mfb-bd-sg-26.10.md` from the repository root. Verify references; do not rename it on the strength of this stale question. |
| DEC-11 | Verify operational certificate position and governance; see release blockers and `ACT-017`. |
| DEC-12 | Verify whether release claims depend on validated operational assessment; see `ACT-017`. |

For each unresolved choice, record the decision owner, approved answer, date, rationale, and affected files. The source accepts responses by question number and A/B choice, such as `1A, 2B, 3A`; map these to the corresponding `DEC` IDs and request choices only for genuinely unresolved questions. Check off its linked action only after all required dependent files agree. The register does not authorize policy changes.

### DEC-01: Is eight hours a fixed Diploma boundary or a planning baseline?

`05_competencies.md` treats eight hours as a design constraint for required Diploma learning. `03_scope.md`, `06_plan.md`, and the [Educator Guide](../publish/mfb-bd-26.10/mfb-bd-eg-26.10.md) instead describe approximately eight hours as a baseline that may need additional time for valid evidence, feedback, and reassessment. `02_research.md` identifies this as an unresolved governance conflict.

**A. Fixed boundary.** Keep eight hours as the maximum complete learner-contact time. Reduce, combine, or move competencies and required evidence until the complete course, including reassessment, fits.

**B. Planning baseline.** Keep the present competency set and treat eight hours as the shortest planned route; require longer scheduled delivery where cohort size, access needs, practice, observation, or reassessment demand it.

Affected: `05_competencies.md`, `03_scope.md`, `06_plan.md`, `02_research.md`, `../publish/mfb-bd-26.10/mfb-bd-sg-26.10.md`, the [Educator Guide](../publish/mfb-bd-26.10/mfb-bd-eg-26.10.md), `13_assessment.md`, `16_spec.md`.

### DEC-02: Does “50% / 50%” describe a score or two completion gates?

**Resolved.** The 50/50 wording describes two equal-status, non-compensatory completion gates: theoretical competency (`C1`–`C8`) and practical competency (`C9`–`C11`). Every required competency and safety criterion must meet standard. The Diploma does not calculate or report a combined numerical grade unless a separate reporting rule is approved.

Affected: `05_competencies.md`, `06_plan.md`, `13_assessment.md`, `15_certification.md`, `16_spec.md`, public materials.

### DEC-03: Is Module 4 part of the Diploma?

**Resolved.** The Diploma consists of Modules 1–4. Modules 1 and 2 develop theory-based competencies through explanation, comparison, and reasoning; Modules 3 and 4 develop practical competencies through supported action. Module 4 is selected locally, but it is required for Diploma completion. Advanced Learning is outside the Diploma.

All source-of-truth and public documents must use this model. Do not describe Module 4 as optional or outside the Diploma.

Affected: `00_index.md`, `04_design.md`, `05_competencies.md`, `06_plan.md`, `../publish/mfb-bd-26.10/mfb-bd-sg-26.10.md`, the [Educator Guide](../publish/mfb-bd-26.10/mfb-bd-eg-26.10.md), `13_assessment.md`, `15_certification.md`, `16_spec.md`.

### DEC-04: What must the Module 3 learner promise say?

`06_plan.md` promises demonstration of wallet, transaction, verification, recovery-readiness, and safety actions. `05_competencies.md` requires several directly observed performances. `16_spec.md` says learners can only “identify” basic safety practices, which understates the assessed standard.

**A. Demonstrate safely under support.** Use one consistent learner promise: beginners demonstrate specified wallet, transaction, verification, recovery-readiness, and safety actions in an approved supported, simulated, testnet, or low-stakes environment.

**B. Identify and explain only.** Reframe Module 3 certification around observable explanation and safety judgment; move hands-on demonstrations out of required Diploma certification.

Affected: `05_competencies.md`, `06_plan.md`, `../publish/mfb-bd-26.10/mfb-bd-sg-26.10.md`, the [Educator Guide](../publish/mfb-bd-26.10/mfb-bd-eg-26.10.md), `13_assessment.md`, `15_certification.md`, `16_spec.md`.

### DEC-05: Is first access to bitcoin a required Module 3 competency?

`C9.3` requires a learner to gain access to bitcoin through an approved low-stakes or simulated pathway, receive it, and check relevant information. Elsewhere the learner-facing material says learners do not need to buy bitcoin, install a wallet, or use meaningful personal funds. These can coexist only if the exact minimum experience is explicit.

**A. Required simulated or low-stakes first access.** Every certificated learner completes `C9.3`; a prepared wallet, test environment, educator-provided training balance, or no-value simulation is sufficient, and no purchase or personal funds are required.

**B. Optional first access.** Remove `C9.3` as a required competency criterion; certification requires safe wallet navigation and a receive/send simulation, but not access to bitcoin.

Affected: `05_competencies.md`, `../publish/mfb-bd-26.10/mfb-bd-sg-26.10.md`, the [Educator Guide](../publish/mfb-bd-26.10/mfb-bd-eg-26.10.md), `13_assessment.md`, `15_certification.md`, and activities on the [Resources Hub](https://programs.myfirstbitcoin.org/resources/).

### DEC-06: What is the required Diploma learning for Lightning?

`06_plan.md` places Lightning setup and payment practice in locally selected Module 4 variants, but `C8.1`, the Student Guide, and assessment requirements place the on-chain/Lightning distinction in Module 3. The boundary between required explanation and required use should be stated once.

**A. Required Diploma explanation; locally selected Module 4 practice.** Every learner compares on-chain and Lightning in a guided scenario; Lightning setup, invoices, and payments are only selected Module 4 practice.

**B. Required supported use.** Every learner completes an approved Lightning receive/send exercise in Module 3; Module 4 may deepen or localize it.

Affected: `05_competencies.md`, `06_plan.md`, `07_contents.md`, `../publish/mfb-bd-26.10/mfb-bd-sg-26.10.md`, activities on the [Resources Hub](https://programs.myfirstbitcoin.org/resources/), the [Educator Guide](../publish/mfb-bd-26.10/mfb-bd-eg-26.10.md), `13_assessment.md`, `../publish/mfb-bd-26.10/mfb-bd-lx.md`, `16_spec.md`.

### DEC-07: Are online PDF, website-ready content, and future branches October deliverables?

`03_scope.md` and `04_design.md` treat online PDF, cohort, self-paced, web, and cross-modal formats as documented future branches, not current implementation requirements. `16_spec.md` lists an online PDF package and website-ready source files among expected 2026.10 outputs.

**A. October deliverables.** Include an online PDF package and website-ready source files in the release completion criteria, with the same competency requirements and assessment safeguards.

**B. Future branch preparation.** Release the complete low-tech print/PDF and educator-led pathway in October; retain only branch notes, source readiness, and design constraints for online/web formats.

Affected: `03_scope.md`, `04_design.md`, `06_plan.md`, `../publish/mfb-bd-26.10/mfb-bd-sg-26.10.md`, the [Educator Guide](../publish/mfb-bd-26.10/mfb-bd-eg-26.10.md), `16_spec.md`, `18_horizon.md`.

### DEC-08: How strict is the learner-facing “open-source wallet” guidance?

`06_plan.md` includes an “open-source wallet preference” in Diploma safety content. The workspace also prohibits global tool recommendations and places detailed wallet-design considerations in Advanced. A preference can sound like a universal recommendation unless its purpose and limit are defined.

**A. Keep a general preference.** Teach that learners can consider whether wallet software is openly inspectable, alongside custody, recovery, safety, compatibility, and local support; do not name a global preferred wallet.

**B. Move it out of the learner Diploma.** Keep wallet open-source evaluation as educator/Advanced context and teach Diploma learners only the custody, recovery, verification, and safety criteria needed for beginner use.

Affected: `06_plan.md`, `05_competencies.md`, `../publish/mfb-bd-26.10/mfb-bd-sg-26.10.md`, activities on the [Resources Hub](https://programs.myfirstbitcoin.org/resources/), the [Educator Guide](../publish/mfb-bd-26.10/mfb-bd-eg-26.10.md), `../publish/mfb-bd-26.10/mfb-bd-lx.md`, `17_advanced.md`.

### DEC-09: Is named programme-pathway promotion part of the Student Guide?

The Student Guide directs learners to specific My First Bitcoin programmes and public webpages. The publication guardrails otherwise emphasize durable offline material, sparse QR codes, and avoiding fragile or named-service dependencies. This needs an explicit publication policy rather than an accidental exception.

**A. Keep a short, curated pathways section.** Retain named My First Bitcoin next steps and links, but make them optional, date-checked, and available as a plain-text offline reference.

**B. Keep the Student Guide programme-neutral.** Remove named pathways and live links from learner chapters; place changing programme navigation on a maintained update page or educator handout.

Affected: `06_plan.md`, `../publish/mfb-bd-26.10/mfb-bd-sg-26.10.md`, `09_resources.md`, the [Educator Guide](../publish/mfb-bd-26.10/mfb-bd-eg-26.10.md), `16_spec.md`.

### DEC-10: Which learner manuscript is the canonical file name?

The repository guidance assigns learner-facing prose to `workspace/../publish/mfb-bd-26.10/mfb-bd-sg-26.10.md`, but the active index, source-of-truth map, and workspace use `../publish/mfb-bd-26.10/mfb-bd-sg-26.10.md`. This is a maintenance and publishing ambiguity rather than a curriculum disagreement.

**A. Standardize on `../publish/mfb-bd-26.10/mfb-bd-sg-26.10.md`.** Update the repository guidance and any stale references to name the existing Student Guide file.

**B. Standardize on `../publish/mfb-bd-26.10/mfb-bd-sg-26.10.md`.** Rename or migrate the Student Guide to the repository-guideline filename and update the index and links.

Affected: `AGENTS.md`, `00_index.md`, `06_plan.md`, `07_contents.md`, `../publish/mfb-bd-26.10/mfb-bd-sg-26.10.md`, the [Educator Guide](../publish/mfb-bd-26.10/mfb-bd-eg-26.10.md), `../publish/mfb-bd-26.10/mfb-bd-lx.md`, `16_spec.md`.

### DEC-11: Is a certificate a 2026.10 operational output or a governed future implementation?

The assessment and certification documents define a mandatory prerequisite and issuance workflow, while `03_scope.md` leaves certificate governance, identity, verification, and infrastructure out of scope. Public wording needs to avoid promising an operational credential system before its owner and controls exist.

**A. Certificate issuance is part of 2026.10.** Add a minimum issuer, approval, record, correction, privacy, and verification process to October completion requirements.

**B. Assessment-complete is the October curriculum output.** Keep the certification prerequisite and public claim, but defer actual issuance and verification implementation until governed separately; do not imply that a credential service is already available.

Affected: `03_scope.md`, the [Educator Guide](../publish/mfb-bd-26.10/mfb-bd-eg-26.10.md), `13_assessment.md`, `15_certification.md`, `16_spec.md`, `18_horizon.md`, public materials.

### DEC-12: Should the first release include timed, certification-complete activities?

The Educator Guide operational assessment protocol now supplies approved theory interactions, direct observation tasks, rubrics, records, support rules, and equivalent routes for every competency. It still requires delivery validation, local `P11` variant approval, calibration examples, and record-governance controls before certificated delivery.

**A. Release only when operational.** Make certification-complete activities (competency-to-evidence crosswalk, approved tasks, rubrics, records, variants, and educator calibration) a release dependency.

**B. Release the curriculum framework first.** Publish the Student and Educator guides as a provisional teaching package; defer certification claims and assessment-complete status until the required activities are operational.

Affected: `02_research.md`, `03_scope.md`, `05_competencies.md`, activities on the [Resources Hub](https://programs.myfirstbitcoin.org/resources/), the [Educator Guide](../publish/mfb-bd-26.10/mfb-bd-eg-26.10.md), `13_assessment.md`, `15_certification.md`, `16_spec.md`, `18_horizon.md`.

---

### Reconciliation order after decisions

1. Update authorities: `06_plan.md`, `05_competencies.md`, `13_assessment.md`, and `15_certification.md`.
2. Align delivery files: `../publish/mfb-bd-26.10/mfb-bd-sg-26.10.md`, activities on the [Resources Hub](https://programs.myfirstbitcoin.org/resources/), and the [Educator Guide](../publish/mfb-bd-26.10/mfb-bd-eg-26.10.md).
3. Align planning and communication: `03_scope.md`, `04_design.md`, `07_contents.md`, `16_spec.md`, and `18_horizon.md`.
4. Update the index, lexicon, resource register, and any public materials that repeat the resolved decision.

## Recurring checks for each release or relevant change

These are repeatable controls, not permanently completed tasks. Copy the relevant checks into a dated run record and link any resulting work to its action ID.

- Verify every competency and decimal criterion in the teaching/evidence crosswalk and Assessment Grid.
- Verify separate educator-led theory and directly observed practical results, equal-status 50%/50% gates, and no compensation or combined numerical grade.
- Confirm no substitution of attendance, confidence, app use, or self-report for evidence. Keep optional self-checks outside requirements and certification.
- Confirm the actual cohort capacity calculation, local `P11`, low-tech/accessibility routes, calibration examples, and record process before certificated delivery.
- Check adaptations preserve learner action, safety boundary, support limit, and evidence standard.
- Check local Markdown links, source paths, headings, anchors, stale line references, placeholders, and current claims before publication.
- Check changing public destinations, local facts, tools, fees, laws, and services immediately before each cohort where relevant; date and localize them rather than presenting universal guidance.
- Recheck low-tech, accessibility, translation, privacy, and safeguarding routes whenever tasks, tools, or delivery modes change.
- Update learner, educator, and public materials when assessment, certification, or scope policy changes.
- Inspect affected rendered outputs, translation readiness, phone readability, and screen-reader behavior when relevant; do not claim checks that were not run.

### Workspace and publication development findings log

When the alignment script finds an inconsistency in the development of workspace ideas or a gap between workspace design and publication implementation, record it here before changing dependent content. Use sequential `EVO-` IDs for workspace-development findings and `PUB-` IDs for workspace-to-publication findings. Retain resolved entries with their evidence so later reviews can distinguish a settled decision from a regression.

For an `EVO-` entry, start with the required structured record above, then record: `Earlier file/heading: … | Later file/heading: … | Issue: … | Why it matters: … | Authority/evidence: … | Affected files: … | Recommended action: …`. 

For a `PUB-` entry, start with the required structured record above, then record: `Governing workspace file/heading: … | Publication file/heading: … | Issue: … | Why it matters: … | Authority/evidence: … | Affected files: … | Recommended action: …`. Use the register statuses defined at the start of this document. Report every `EVO-` or `PUB-` entry that remains `needs-verification`, `open`, `in-progress`, or `blocked` at the end of the alignment review.

#### EVO-001: October publication-output scope is not consolidated

Status: needs-verification | Owner: unassigned | Updated: 2026-09-21 | Severity: high | Release impact: publication blocker | Evidence: `workspace/03_scope.md` and `workspace/16_spec.md` describe October Sanity-published online PDF and web outputs; `workspace/06_plan.md` retains online PDF and web among future branches | Depends on: ACT-015, DEC-07 | Completion evidence: affected authority and public wording use one approved October output boundary.

Earlier file/heading: `workspace/06_plan.md`, `## 3. Legacy Content Migration` and `## 8. October 2026 Output` | Later file/heading: `workspace/03_scope.md`, `## 15. Publishing System`; `workspace/16_spec.md`, `## Materials And Outputs` | Issue: current authorities disagree on whether online PDF and web outputs are October deliverables or future branches | Why it matters: publication ownership, release promises, and maintenance routes can diverge between educators, collaborators, and public users | Authority/evidence: `03_scope.md` and `16_spec.md` explicitly include October online PDF/web outputs through Sanity; `06_plan.md` uses future-branch wording; `review/review_todo.md` ACT-015/DEC-07 | Affected files: `workspace/06_plan.md`, `workspace/03_scope.md`, `workspace/04_design.md`, `workspace/16_spec.md`, `workspace/18_horizon.md`, `workspace/19_publication-coverage.md`, affected public wording | Recommended action: authorize and apply one reconciliation across the architecture and release documents, preserving the distinction between publication formats and future instructional branches.

#### PUB-001: Conditional certificate-verification instructions lack an approved process

Status: needs-verification | Owner: unassigned | Updated: 2026-09-21 | Severity: high | Release impact: publication blocker | Evidence: Student Guide retains `### Certificate verification` with instructions for codes, links, QR codes, signatures, timestamps, and a verification process; `workspace/15_certification.md`, `## Governance And Verification Still To Define`, leaves public verification undecided | Depends on: ACT-003, ACT-008, ACT-017 | Completion evidence: learner-facing wording is removed or aligned to an approved, tested, privacy-preserving process.

Governing workspace file/heading: `workspace/15_certification.md`, `## Governance And Verification Still To Define`; `workspace/16_spec.md`, `## Assessment And Certification` | Publication file/heading: `publish/mfb-bd-26.10/mfb-bd-sg-26.10.md`, `### Certificate verification` | Issue: conditional instructions still teach a future or issuer-dependent verification route without a settled public process | Why it matters: learners and educators may infer that a My First Bitcoin verification service exists, and a future QR or link could expose personal data or create an unsupported certificate promise | Authority/evidence: `15_certification.md` lists public certificate verification as an implementation decision; Student Guide text says to follow a process “when checking a certificate through the official verification process” but gives no approved destination | Affected files: Student Guide back matter, Educator Guide certificate guidance if shared, Assessment Grid footnotes if added, `workspace/08_assets.md` BD-V-074, `workspace/15_certification.md`, `workspace/16_spec.md` | Recommended action: resolve certificate governance first, then either remove the section or publish only approved issuer-specific instructions; do not commission or retain BD-V-074 as a functional verification visual until the process is tested.

#### PUB-002: Publication coverage omits non-beginner and quick-start files

Status: needs-verification | Owner: unassigned | Updated: 2026-09-21 | Severity: medium | Release impact: publication blocker | Evidence: `publish/mfb-adv-26.10/mfb-adv-001` through `mfb-adv-008` and `publish/mfb-bd-26.10/mfb-bd-qs-26.10.md` exist but are absent from `workspace/19_publication-coverage.md` | Depends on: ACT-019 | Completion evidence: every file under `publish/` has an explicit current-release, deferred, or non-public status and appears in the coverage register where required.

Governing workspace file/heading: `workspace/19_publication-coverage.md`, `## Diploma publication set` and `## Maintenance check`; `workspace/17_advanced.md`, `## 1. Status And Use` | Publication file/heading: `publish/mfb-adv-26.10/mfb-adv-001-history-of-money-localisation.md` through `mfb-adv-008-building-on-bitcoin.md`; `publish/mfb-bd-26.10/mfb-bd-qs-26.10.md` | Issue: publication inventory and actual files disagree; the Advanced README says Advanced modules are not current beginner publication, but individual Advanced files and the Quick Start are not explicitly classified in the coverage register | Why it matters: release tooling, reviewers, translators, and users may treat drafts or supporting material as approved publication, or fail to maintain files that are in scope | Authority/evidence: `workspace/19_publication-coverage.md` says every curriculum-content file in `publish/` must appear once; `publish/mfb-adv-26.10/README.md` says Advanced modules are future; Quick Start is an educator-facing publication file not listed | Affected files: `workspace/19_publication-coverage.md`, `workspace/00_index.md`, `workspace/17_advanced.md`, `publish/mfb-adv-26.10/README.md`, eight Advanced files, Quick Start | Recommended action: record explicit deferred/non-release status and owner for the Advanced files and Quick Start, or make an authorized scope decision about their location and publication role before release.

## Historical report baseline and verification limits

The report is dated 2026-09-01. It assessed the design as coherent and suitable for continued editing and non-certificated teaching development, but not ready for certificated delivery until validation, calibration, local tasks, and governance were complete. That is a historical assessment to verify, not a new readiness determination.

The report cross-read the active workspace authorities, Student Guide, Educator Guide, Assessment Grid, optional self-assessment materials, and live reviews. It replaced a mixed historical audit and explicitly was not a source of curriculum policy. Its recommendation was to validate and simplify the existing system rather than add curriculum topics. It also noted that the Student Guide now explained educator observation, feedback, and reassessment.

Preserve its category meanings: **implemented** means present in source files; **release blocker** means required before certificated delivery; **publication decision** means an owner decision is needed before settling public copy or scope; and **maintenance action** improves accuracy, usability, or editing without by itself blocking a teaching draft. Record/certificate governance blocks certification and pilots retaining results, not use of the curriculum as a teaching package.

It recorded these implemented points: all four modules and required `C11`; educator theory `C1`–`C8` and direct observation `C9`–`C11`; an operational protocol with crosswalk, `T1`–`T3`, `P9`–`P11`, support limits, safety-critical errors, equivalents, reassessment, calibration, and moderation; the Bitcoin/stablecoin/other-crypto comparison and responsible-learning boundary; supported simulated or low-stakes `C9.3`; no purchase, meaningful personal funds, secrets, personal device, or app requirement; optional self-check/recap/discovery only; and separate index roles for the microlearning plan and published data.

The report found six registered sources and mutable occurrence/line references against a then 1,549-line Student Guide. Those are historical counts explaining the source-maintenance task, not current measurements. Expand economic, historical, technical, security, and current-context source coverage; keep shared claims distinct from local verification.

Its local-link audit across `workspace/`, `publish/`, `review/`, and `README.md` found 162 targets and one missing Creative Commons visual, `assets/diploma/bd-v-001.svg`. The asset register was a design brief, not an inventory of produced assets. It confirmed the operational protocol, digital-asset comparison, removal of educator app-scoring/assessment claims, and separate microlearning index roles. It did not validate external links, current claims, rendered output, screen-reader behavior, or real-cohort delivery.

The report replaced a mixed 19 August snapshot and implementation update that had continued to show completed or superseded findings as active. It retired earlier findings about missing `C5` content, needing to build the crosswalk/protocol, app-scoring and certification regressions, optional Module 4 wording, duplicated microlearning roles, former broken-link counts/deleted filenames, and mixed historical audit/author-question tables. Do not reactivate those findings without a current regression. The old report deliberately excluded untriaged handwritten notes from active work.

### Report-to-action and file map

This map preserves all eight report action areas and their primary-file references. Paths in code are relative to the repository root. Resolve old review-file references to the consolidated sections here for new work; keep originals as provenance.

| Report action | Consolidated action IDs | Primary files or sections |
|---|---|---|
| 1. Validate certificated delivery | ACT-001, ACT-002 | [Educator Guide](../publish/mfb-bd-26.10/mfb-bd-eg-26.10.md), [Assessment Grid](../publish/mfb-bd-26.10/mfb-bd-assessment-grid-26.10.md), `workspace/13_assessment.md`, `workspace/03_scope.md`. |
| 2. Approve minimum record and certificate governance | ACT-003, ACT-005, ACT-017 | `workspace/15_certification.md`, `workspace/13_assessment.md`, `workspace/03_scope.md`, Student Guide back matter. |
| 3. Resolve remaining scope decisions | ACT-004, ACT-005, ACT-006, ACT-015, ACT-017 | DEC-01, DEC-07, DEC-08, DEC-09, DEC-11, DEC-12 and their affected-file lists; `workspace/04_design.md` and `workspace/16_spec.md` are included in output reconciliation. |
| 4. Make Student Guide back matter publication-ready | ACT-008, ACT-009 | [Student Guide](../publish/mfb-bd-26.10/mfb-bd-sg-26.10.md), `workspace/07_contents.md`, `workspace/08_assets.md`, `workspace/15_certification.md`. |
| 5. Repair source and terminology maintenance | ACT-010 | `workspace/09_resources.md`, [Lexicon](../publish/mfb-bd-26.10/mfb-bd-lx.md), Educator Guide local verification record. |
| 6. Triage remaining consistency decisions | ACT-014 | This action list, decision register, and annotation inventory; formerly maintained in the archived review register. |
| 7. Finish the optional self-check | ACT-011 | [Published self-check](../publish/mfb-ml-26.10/mfb-ml-26.10.md), `workspace/14_microlearning-plan.md`. |
| 8. Fix local-link failure and control visuals | ACT-012, ACT-013 | `workspace/08_assets.md`, `assets/diploma/bd-v-001.svg`, essential-visual production tracker. |

## Complete historical annotation inventory

Every one of the original backlog's bullet items is retained below in its original order and section context. `ANN` IDs are stable references. The original `[o]`, `[-]`, or `[ ]` marker appears as provenance, not as a completion claim; the source does not define all marker meanings. All new checkboxes mean **triage this note**, not **implement this request**.

To complete triage, compare the note with the current source, then record `already-addressed`, `approved-action`, `rejected`, `superseded`, `duplicate`, `preserve-approval`, or `needs-clarification`, with evidence and a linked action where needed. Preserve literal approvals as approvals. For unclear handwriting, require the source image or author clarification. Do not infer unavailable wording or treat an uncertain name as an assignment.

Source provenance: the original backlog identifies `input/PABLO/202602721_final_draft_notes.md` and says source items marked `[x]` were excluded. This consolidation preserves all items actually present in `review/`; it does not claim to recover excluded source notes. Later-page numbering differences between Claude and Codex readings require checking the PDF images. The source's references to `00_todo.md` are historical; use this register for the new workflow.

For item locations, use current source heading anchors after matching the inherited section labels. Some historical section titles no longer match current headings. Repeated proposals, handwriting reminders, and approvals are retained separately to avoid losing evidence, but should link to one implementation task when they refer to the same work.

### Global actions

- [ ] **ANN-001** (source marker `[o]`) Create a consistent visual system for graphics, diagrams, tables, examples, activities, educator guidance, glossary terms, and advanced content.
- [ ] **ANN-002** (source marker `[o]`) Build a glossary/lexicon; define marked terms before or at first use and use consistent beginner language.
- [ ] **ANN-003** (source marker `[o]`) Separate student content from educator guidance; create an educator guide/toolkit where marked.
- [ ] **ANN-004** (source marker `[-]`) Treat Modules 1–4 as the required Diploma. Keep Module 4 locally selected, with educator-facing templates and local variants.
- [ ] **ANN-005** (source marker `[o]`) Add graphics and worked/local examples for abstract money, banking, mining, wallet, transaction, and payment concepts.
- [ ] **ANN-006** (source marker `[o]`) Give every exercise a format, duration, purpose, facilitator instructions, expected evidence/output, and writing space where needed.
- [ ] **ANN-007** (source marker `[o]`) Fact-check economic, banking, Bitcoin, security, legal, and technical claims with qualified reviewers.
- [ ] **ANN-008** (source marker `[o]`) Create and maintain a public Diploma web page as well as the public GitHub repository.
- [ ] **ANN-009** (source marker `[o]`) Maintain a stable, current reference so educators do not have to independently re-research the material for every cohort.
- [ ] **ANN-010** (source marker `[-]`) Preserve literal approval marks separately from requested changes so approved material is not accidentally rewritten.
- [ ] **ANN-011** (source marker `[o]`) Resolve later-page numbering differences between the Claude and Codex readings directly against the PDF images.

### Welcome To The Bitcoin Diploma

#### About Us

- [ ] **ANN-012** (source marker `[o]`) Have AI and three humans review “Our work is independent and community driven…”
- [ ] **ANN-013** (source marker `[ ]`) Confirm whether the opening strike/brace means revise/delete “Education must come first” and/or the following paragraph.

#### Our mission: independent, open-source Bitcoin education

- [ ] **ANN-014** (source marker `[-]`) Add a public/GitHub process for questions, corrections, and improvements.
- [ ] **ANN-015** (source marker `[-]`) Use the Community paragraph as an explicit opportunity to connect learners.

### How This Diploma Works

#### What learners will be able to explain and demonstrate by the end

- [ ] **ANN-016** (source marker `[-]`) Support or soften the claim that bitcoin can be used in a local community.
- [ ] **ANN-017** (source marker `[-]`) Reconsider the competency heading/framing and whether it is meaningful for one eight-hour module.
- [ ] **ANN-018** (source marker `[-]`) Replace or clarify “recovery phrase.”

#### Learning style: in-person preferred, discussion, reflection, practice, and guided activities

- [ ] **ANN-019** (source marker `[-]`) Use one simple learner checklist instead of duplicating competency statements.
- [ ] **ANN-020** (source marker `[-]`) Show creator/editor accountability and transparent GitHub history.
- [ ] **ANN-021** (source marker `[-]`) Apply the five-step learning rhythm consistently.

#### Participation expectations

- [ ] **ANN-022** (source marker `[-]`) Make educator assessment/evidence guidance explicit.
- [ ] **ANN-023** (source marker `[-]`) Give “Basic reading and everyday arithmetic” a clear topic heading.
- [ ] **ANN-024** (source marker `[o]`) Link required materials to the teacher/[ETP](https://etp.myfirstbitcoin.org/) checklist and resources.
- [ ] **ANN-025** (source marker `[o]`) Make device-practice rules a linked one-page checklist.
- [ ] **ANN-026** (source marker `[-]`) Review example diversity; one annotated example was flagged as a male software engineer.

#### Safety, responsibility, and no financial advice

- [ ] **ANN-027** (source marker `[-]`) Rework/qualify the “Diploma is for education” disclaimer wording.
- [ ] **ANN-028** (source marker `[-]`) Review the marked sentence about Bitcoin’s market position.
- [ ] **ANN-029** (source marker `[-]`) Expand “Verify” to include actions, people, and sources, not just transaction fields.
- [ ] **ANN-030** (source marker `[o]`) Have a lawyer review the legal/financial/tax disclaimer.
- [ ] **ANN-031** (source marker `[-]`) Clarify the Diploma, locally selected Module 4, and Advanced boundaries and local suggestions.
- [ ] **ANN-032** (source marker `[-]`) Use clear names instead of calling material “Bitcoin terms” merely for aesthetics.
- [ ] **ANN-033** (source marker `[o]`) Create a standalone scam-reminders/red-flags one-pager.
- [ ] **ANN-034** (source marker `[-]`) Reinforce “don't trust, verify” where appropriate.
- [ ] **ANN-035** (source marker `[-]`) Mention Lightning/Layer 2 in the description of optional/local modules if it fits the intended scope.

### 1. Understanding Money

#### Opening questions about money

- [ ] **ANN-036** (source marker `[ ]`) Add a motivating opening and educator preparation guidance.

#### Why money exists

- [ ] **ANN-037** (source marker `[-]`) Clarify whether opening questions are a section discussion; add an educator wrap-up.
- [ ] **ANN-038** (source marker `[o]`) Add a fact-versus-preference/dilemma activity to the educator guide.
- [ ] **ANN-039** (source marker `[-]`) Move deeper barter/double-coincidence material into advanced modules.
- [ ] **ANN-040** (source marker `[-]`) Add examples of exchange difficulty: wants, timing, distance, etc.
- [ ] **ANN-041** (source marker `[o]`) Add links to optional further economics reading.
- [ ] **ANN-042** (source marker `[-]`) Decide whether capitalism and free markets belong in advanced discussion rather than the beginner Diploma.
- [ ] **ANN-043** (source marker `[-]`) Preserve the “very good for critical thinking” annotation as approval.

#### Functions and properties of money

- [ ] **ANN-044** (source marker `[o]`) Turn the money-properties table into a graphic; consider recognizability/“likeness.”
- [ ] **ANN-045** (source marker `[-]`) Add property trade-off examples and goods/assets satisfying only some properties.
- [ ] **ANN-046** (source marker `[-]`) Rewrite the unclear first comprehension question.
- [ ] **ANN-047** (source marker `[o]`) Add a barter/double-coincidence graphic.
- [ ] **ANN-048** (source marker `[-]`) Use a local three-role/item scenario and define the decision/double-coincidence problem.
- [ ] **ANN-049** (source marker `[o]`) Consider printable cards or handouts for a “make the trades happen” barter activity.
- [ ] **ANN-050** (source marker `[-]`) Preserve the positive annotation on the property/question table.

#### Scarcity, value, and exchange

- [ ] **ANN-051** (source marker `[-]`) Move the accepted-money explanation into the prior activity and have learners restate it.
- [ ] **ANN-052** (source marker `[-]`) Add health to scarce-resource examples if appropriate.
- [ ] **ANN-053** (source marker `[-]`) Teach subjective value through comparisons/trade-offs or games.
- [ ] **ANN-054** (source marker `[-]`) Expand opportunity cost/time preference/trade-offs with examples and graphics.
- [ ] **ANN-055** (source marker `[o]`) Add a visual money timeline from local/home exchange to institutional/global/digital forms.
- [ ] **ANN-056** (source marker `[-]`) Avoid implying one universal linear monetary history.
- [ ] **ANN-057** (source marker `[-]`) If discussing monetary evolution as civilizational progress, label it as a viewpoint or discussion prompt rather than settled fact.

#### Beginner monetary history from barter to digital money

- [ ] **ANN-058** (source marker `[ ]`) Add an introductory hands-on money/app activity (exact handwritten details need confirmation).
- [ ] **ANN-059** (source marker `[-]`) Add historical context and competing views for standard coins and representative paper.
- [ ] **ANN-060** (source marker `[-]`) Rework bank/government money and define the affected population/network.
- [ ] **ANN-061** (source marker `[-]`) Add 1971/Nixon Shock/Bretton Woods context; define convertibility.
- [ ] **ANN-062** (source marker `[-]`) Define fiat before use and distinguish modern fiat, older money, and account claims.
- [ ] **ANN-063** (source marker `[-]`) Check “by decree” and avoid one-country assumptions.
- [ ] **ANN-064** (source marker `[-]`) Explain network effects more clearly.
- [ ] **ANN-065** (source marker `[-]`) Restructure terms so each is explained before use.
- [ ] **ANN-066** (source marker `[o]`) Create a downloadable History of Money companion app, video, or PDF.
- [ ] **ANN-067** (source marker `[o]`) Provide a stable maintained history/money reference for educators.
- [ ] **ANN-068** (source marker `[-]`) Consider the USD's post-WWII international-settlement role and Bretton Woods; include Federal Reserve/Jekyll Island background only if relevant, balanced, and sourced.

#### Fractional reserve banking

- [ ] **ANN-069** (source marker `[-]`) Explain “creates deposit money when it issues loans.”
- [ ] **ANN-070** (source marker `[-]`) Move deeper risks/benefits into advanced modules and avoid presenting them as universal facts.
- [ ] **ANN-071** (source marker `[o]`) Define liability and diagram fractional-reserve banking.
- [ ] **ANN-072** (source marker `[o]`) Consider a small bank-reserve/gearing calculator or interactive activity.

#### Inflation and purchasing power

- [ ] **ANN-073** (source marker `[-]`) Explain how bank runs affect the wider population/economy and how interventions/losses work.
- [ ] **ANN-074** (source marker `[ ]`) Confirm the unclear “10% / too big to fail / restructuring” note.
- [ ] **ANN-075** (source marker `[-]`) Turn inflation/purchasing-power definitions into graphics, local examples, and an activity.
- [ ] **ANN-076** (source marker `[o]`) Add advanced treatment of monetary expansion and secondary effects.
- [ ] **ANN-077** (source marker `[-]`) Label the purchasing-power check as a distinct activity.

#### Central Bank Digital Currencies (CBDCs)

- [ ] **ANN-078** (source marker `[-]`) Add CBDC examples and risks/benefits.
- [ ] **ANN-079** (source marker `[-]`) Explain safety, access to transaction information, privacy, and control.
- [ ] **ANN-080** (source marker `[-]`) Require current, local, reliable CBDC information.
- [ ] **ANN-081** (source marker `[-]`) Add locally accurate tax considerations or benefits to the real-estate comparison where relevant.

#### Review: how can money break?

- [ ] **ANN-082** (source marker `[-]`) Clarify assets versus money for metals, currency, bonds, businesses, land, tools, and education.
- [ ] **ANN-083** (source marker `[-]`) Distinguish BTC as money versus asset and clarify the claimed fiat “problem.”
- [ ] **ANN-084** (source marker `[o]`) Keep the fill-in review exercise (“YES!”).
- [ ] **ANN-085** (source marker `[o]`) Expert-review the Module 1 answer.
- [ ] **ANN-086** (source marker `[-]`) Rename/reframe “How Bitcoin Works” if “solution” overstates the claim.
- [ ] **ANN-087** (source marker `[-]`) Ensure the framing cannot be mistaken for a general cryptocurrency diploma.
- [ ] **ANN-088** (source marker `[ ]`) Clarify the annotation “To what Q?” and connect item 7 to its intended question.
- [ ] **ANN-089** (source marker `[o]`) Preserve “YES!” on the fill-in exercise and “PERFECT LFG!” at the end of Module 1 as explicit approvals.

### 2. How Bitcoin Works

#### Why Bitcoin was created

- [ ] **ANN-090** (source marker `[-]`) Make the intermediary power/risk example concrete.
- [ ] **ANN-091** (source marker `[-]`) Confirm/add the unclear note about Cypherpunk/Bitcoin history.
- [ ] **ANN-092** (source marker `[-]`) Review whether “issuer” is being used correctly.
- [ ] **ANN-093** (source marker `[-]`) Add a Cypherpunk definition box or optional further-reading link.

#### Early digital-money attempts and the double-spend problem

- [ ] **ANN-094** (source marker `[-]`) Attribute prior contributors/ideas in Bitcoin’s origin story.
- [ ] **ANN-095** (source marker `[-]`) Define DigiCash, Hashcash, Bit Gold, proof of work, mining, miners, nodes, blocks, valid chain, and accumulated work.
- [ ] **ANN-096** (source marker `[-]`) Bold or otherwise visually clarify the numbered transaction/miner/node process.
- [ ] **ANN-097** (source marker `[-]`) Preserve the “VG” annotation on the closing explanation as approval.

#### Bitcoin origin timeline

- [ ] **ANN-098** (source marker `[ ]`) Clarify the note beside Satoshi’s identity and avoid speculation.
- [ ] **ANN-099** (source marker `[o]`) Consider an optional “my first Bitcoin purchase” calendar/ICS reminder tied to Bitcoin Pizza Day.

#### Decentralization

- [ ] **ANN-100** (source marker `[-]`) Define decentralization-list terms.
- [ ] **ANN-101** (source marker `[-]`) Qualify/add examples to “no participant can unilaterally change rules.”
- [ ] **ANN-102** (source marker `[-]`) Distinguish subsidy from total supply and correct marked terminology.
- [ ] **ANN-103** (source marker `[-]`) Explain halving as block-based/roughly four-year timing, not a fixed date.
- [ ] **ANN-104** (source marker `[o]`) Add a finite-supply/halving graphic.
- [ ] **ANN-105** (source marker `[-]`) Separate known issuance facts from uncertain adoption/price/scaling claims.
- [ ] **ANN-106** (source marker `[-]`) Link back to Module 1.

#### Satoshis and unit bias

- [ ] **ANN-107** (source marker `[o]`) Turn the bitcoin/sats table into a graphic.
- [ ] **ANN-108** (source marker `[-]`) Rewrite the whole-number/sats sentence.
- [ ] **ANN-109** (source marker `[-]`) Improve the comprehension exercise and provide answer guidance.

#### Users, nodes, and miners

- [ ] **ANN-110** (source marker `[-]`) Distinguish the Bitcoin network from services/intermediaries.
- [ ] **ANN-111** (source marker `[-]`) Check “usually” in the irreversibility claim.
- [ ] **ANN-112** (source marker `[-]`) Clarify whether “users” means using a wallet/client or running Bitcoin Core/full node.
- [ ] **ANN-113** (source marker `[-]`) Explain “developers can propose software…”; the note asks “What?!”

#### Proof of work

- [ ] **ANN-114** (source marker `[-]`) Add marked proof-of-work terms to the lexicon.
- [ ] **ANN-115** (source marker `[o]`) Demonstrate proof of work/difficulty with a tool, interactive, or animation.
- [ ] **ANN-116** (source marker `[o]`) Diagram/animate proof of work’s stated purposes.
- [ ] **ANN-117** (source marker `[-]`) Link relevant sound-money/Nick Szabo background and qualify “sound digital money.”

#### Bitcoin as sound digital money

- [ ] **ANN-118** (source marker `[-]`) Double-check the property criteria/requirements.
- [ ] **ANN-119** (source marker `[-]`) Add FAQs about fungibility and sat interchangeability.
- [ ] **ANN-120** (source marker `[-]`) Add nuance to the functions-of-money assessment.

#### Participant empowerment, risk, and responsibility

- [ ] **ANN-121** (source marker `[-]`) Improve personal-responsibility examples and unclear wording (“less,” “peer information”).
- [ ] **ANN-122** (source marker `[o]`) Add graphics to the Module 2 comparison.
- [ ] **ANN-123** (source marker `[-]`) Deepen function/property comparisons, including scarcity.
- [ ] **ANN-124** (source marker `[-]`) Make the next-module transition explicit.

### 3. Using Bitcoin Safely

#### Wallets

- [ ] **ANN-125** (source marker `[ ]`) Confirm/add the proposed new comparison column (label illegible).
- [ ] **ANN-126** (source marker `[-]`) Recheck the Module 2 answer and transition to Module 3.
- [ ] **ANN-127** (source marker `[-]`) Add wallet terms to the lexicon.
- [ ] **ANN-128** (source marker `[-]`) Rephrase the Module 3 learner promise consistently.
- [ ] **ANN-129** (source marker `[-]`) Clarify that a wallet coordinates keys/spending/receiving while bitcoin remains on the ledger.

#### Addresses

- [ ] **ANN-130** (source marker `[-]`) Explain how to evaluate compatibility, open source, recovery, privacy, and project continuity.
- [ ] **ANN-131** (source marker `[-]`) Add address/network/tag terms to the lexicon.
- [ ] **ANN-132** (source marker `[o]`) Add an address/QR graphic and explain who creates addresses.
- [ ] **ANN-133** (source marker `[-]`) Add explicit how-to guidance for address checks.

#### Keys

- [ ] **ANN-134** (source marker `[o]`) Add a public/private-key image and optional physical teaching tool.
- [ ] **ANN-135** (source marker `[-]`) Point technical depth to an advanced module.
- [ ] **ANN-136** (source marker `[-]`) Emphasize avoiding key/recovery-material loss.
- [ ] **ANN-137** (source marker `[-]`) Reassess “seed phrase” versus broader recovery language.

#### Seed phrases

- [ ] **ANN-138** (source marker `[o]`) Add a visual wallet setup/recovery activity: why it matters, record, store, and test.
- [ ] **ANN-139** (source marker `[-]`) Keep/emphasize the seed-backup checklist (“Love it”).
- [ ] **ANN-140** (source marker `[-]`) Correct the marked “read & process” recovery wording.

#### Hot and cold wallets

- [ ] **ANN-141** (source marker `[o]`) Add a graphic comparing hot, hardware/cold, and custodial wallets/accounts.

#### Wallet recovery and seed phrase testing

- [ ] **ANN-142** (source marker `[-]`) Decide whether recovery is taught with seed phrases, another method, or several methods.
- [ ] **ANN-143** (source marker `[o]`) Make recovery principles a one-page trainer/learner checklist.
- [ ] **ANN-144** (source marker `[-]`) Make practice practical but private and limited to empty/tiny-value wallets.

#### Receiving bitcoin

- [ ] **ANN-145** (source marker `[-]`) Add robust/resilient recovery and security tests/examples.
- [ ] **ANN-146** (source marker `[o]`) Add a visual receiving activity with roles, addresses, QR codes, and examples.
- [ ] **ANN-147** (source marker `[-]`) Treat confirmation count as local/risk-dependent.
- [ ] **ANN-148** (source marker `[-]`) Create a receive-screen competency activity without requiring real funds.
- [ ] **ANN-149** (source marker `[-]`) Add “confirmations” to the lexicon.

#### Sending bitcoin

- [ ] **ANN-150** (source marker `[o]`) Make sending/address/network checks a one-page checklist and clarify “address type.”
- [ ] **ANN-151** (source marker `[-]`) Add “how” guidance to command-only checks.
- [ ] **ANN-152** (source marker `[-]`) Explain fee estimation/security without requiring miner knowledge for each transaction.
- [ ] **ANN-153** (source marker `[-]`) Add a TXID/block-explorer activity or quiz.

#### Verification, block explorers, and irreversible transactions

- [ ] **ANN-154** (source marker `[-]`) Explain first confirmation and block depth more clearly.
- [ ] **ANN-155** (source marker `[-]`) Expand the block-explorer privacy warning without overloading beginners.
- [ ] **ANN-156** (source marker `[o]`) Make the safety checklist a one-page resource.
- [ ] **ANN-157** (source marker `[-]`) Distinguish on-chain and Lightning under destination verification.

#### Safety checklist

- [ ] **ANN-158** (source marker `[o]`) Turn scam scenarios into scaffolded role-play/advanced content rather than one dense list.
- [ ] **ANN-159** (source marker `[-]`) Reduce Module 3 security overload and clarify learner choices.

#### Acquiring and exchanging bitcoin: awareness, not financial advice

- [ ] **ANN-160** (source marker `[-]`) Fix heading hierarchy (“sub-header, not header”).
- [ ] **ANN-161** (source marker `[-]`) Distinguish financial advice from awareness of ways to acquire and exchange bitcoin.
- [ ] **ANN-162** (source marker `[o]`) Turn acquisition/exchange pathways into a one-page comparison activity.

#### On-chain and Lightning payments

- [ ] **ANN-163** (source marker `[-]`) Add on-chain and Lightning examples to the table.
- [ ] **ANN-164** (source marker `[-]`) Define marked terms.
- [ ] **ANN-165** (source marker `[-]`) Move routing/channel mechanics to advanced content.
- [ ] **ANN-166** (source marker `[-]`) Explain Lightning trade-offs involving custody, routing, channels, and liquidity.

#### Review: what does self-custody responsibility mean?

- [ ] **ANN-167** (source marker `[-]`) Rename/explain “Module 4” and Module 4.
- [ ] **ANN-168** (source marker `[-]`) Mark the second on-chain/Lightning comparison table as advanced if that matches the annotation.

### 4. Bitcoin in Your Community

#### Educator-selected local modules

- [ ] **ANN-169** (source marker `[-]`) Clarify the responsibility map and whether “choose custody” is an action or competency result.
- [ ] **ANN-170** (source marker `[o]`) Make the table an educator-guided exercise with examples.
- [ ] **ANN-171** (source marker `[-]`) Separate generic terms from scam signals.
- [ ] **ANN-172** (source marker `[-]`) Rewrite the “heavy” Module 3 answer with examples.
- [ ] **ANN-173** (source marker `[o]`) Move educator-only Module 3 material to the educator guide.
- [ ] **ANN-174** (source marker `[-]`) Redesign Module 4 as locally selected learning; define MFB versus educator responsibilities and resources.
- [ ] **ANN-175** (source marker `[-]`) Describe Module 4 as locally selected but required in learner-facing Diploma material.
- [ ] **ANN-176** (source marker `[-]`) Preserve the annotation that Module 3 is “full, complete & serious” while acting on the concern that it feels heavy.
- [ ] **ANN-177** (source marker `[-]`) State that educators select a topic/module for local context and provide an example.
- [ ] **ANN-178** (source marker `[-]`) Clarify local warnings/appropriateness conditions.
- [ ] **ANN-179** (source marker `[-]`) Preserve the local-learning table (“I like this”) as a reusable template.
- [ ] **ANN-180** (source marker `[-]`) State what learners should learn and integrate through locally selected Module 4.
- [ ] **ANN-181** (source marker `[-]`) Add community/spread-layer considerations.
- [ ] **ANN-182** (source marker `[o]`) Give each local module a page-count or scope limit.
- [ ] **ANN-183** (source marker `[-]`) State that the aim is to help learners learn, interact with, and integrate into their local Bitcoin ecosystem/community where appropriate.

#### Practical workshops and demonstrations

- [ ] **ANN-184** (source marker `[-]`) Organize modules around local worker/family/merchant/community needs and remittance examples.
- [ ] **ANN-185** (source marker `[-]`) Keep presentation–practice–production (“perfect place”).
- [ ] **ANN-186** (source marker `[o]`) Turn merchant payment flow into an educator-guide case study.
- [ ] **ANN-187** (source marker `[-]`) Explain how demonstration safety changes by local conditions.
- [ ] **ANN-188** (source marker `[-]`) Work through the marked module questions with the community team and rewrite them.

#### Local Bitcoin tools and resources

- [ ] **ANN-189** (source marker `[-]`) Create a reusable local-tool comparison template; consider merging with wallet comparison.
- [ ] **ANN-190** (source marker `[-]`) Preserve the checked workshop-result sentence as approved.
- [ ] **ANN-191** (source marker `[-]`) Move the local-tool record and guidance into the separate Module 4/educator guide; Modules 1–4 are the Diploma.
- [ ] **ANN-192** (source marker `[o]`) Sequence the educator materials explicitly: Module 3 items 1–3, then its Educator Guide; Module 4 should be driven by its Educator Guide.

#### Daily-life Bitcoin use

- [ ] **ANN-193** (source marker `[o]`) Offer separate examples/pages for Lightning, cash, custodial, single-sig, multisig, and other payment variants.
- [ ] **ANN-194** (source marker `[-]`) Keep/clarify daily-life Bitcoin use.
- [ ] **ANN-195** (source marker `[o]`) Add educator-guide options for earning, saving, receiving, sending, spending, accounting, and donating.
- [ ] **ANN-196** (source marker `[-]`) Leave optional space for other layers such as Liquid or ecash without overloading beginners.
- [ ] **ANN-197** (source marker `[o]`) Consider Value-for-Value and donation examples in the Educator Guide.
- [ ] **ANN-198** (source marker `[-]`) Preserve “Nice” and “based” annotations on the daily-life Bitcoin material as approvals.

#### Local spending and receiving scenarios

- [ ] **ANN-199** (source marker `[-]`) Make jurisdiction/legal context explicit in scenarios.
- [ ] **ANN-200** (source marker `[o]`) Put educator notes in a distinct style and specify applicable trust, regulation, experience, infrastructure, limits, and personal-data rules.
- [ ] **ANN-201** (source marker `[-]`) Preserve the approval of “Avoid starting with the tool. Start with the need” and the positive response to the scenario approach.

#### Local on-ramp and off-ramp pathways

- [ ] **ANN-202** (source marker `[-]`) Remove/redesign the on/off-ramp table if too technical for learners.
- [ ] **ANN-203** (source marker `[o]`) Decide whether most Module 4 content should be packaged as activities.
- [ ] **ANN-204** (source marker `[-]`) Preserve the strong approval of the pathway-comparison template.

#### KYC and no-KYC trade-offs where locally appropriate

- [ ] **ANN-205** (source marker `[-]`) Keep KYC/no-KYC trade-offs only where locally appropriate and fact-check them.
- [ ] **ANN-206** (source marker `[-]`) Preserve the “VG”/“strong position” approval of the circular-economy conclusion.

#### Circular economies

- [ ] **ANN-207** (source marker `[o]`) Have the circular-economy section reviewed by the named reviewer (handle unclear).
- [ ] **ANN-208** (source marker `[o]`) Add a stronger balanced viewpoint and graphic for circular economies.
- [ ] **ANN-209** (source marker `[ ]`) Confirm whether the named reviewer is `@Reyner` and assign review only after confirmation.
- [ ] **ANN-210** (source marker `[o]`) Note that community custody/shared-funds material may overlap with Fedimint; decide whether it belongs in advanced educator guidance.

#### Merchant or community use cases

- [ ] **ANN-211** (source marker `[-]`) Break Module 4 into educator-selected sections (wallet, exchange, circular economy, etc.).
- [ ] **ANN-212** (source marker `[-]`) Reduce wordiness and create response space.
- [ ] **ANN-213** (source marker `[-]`) Connect merchant/community cases to jurisdiction/local context.
- [ ] **ANN-214** (source marker `[-]`) Expand practical field/community work where appropriate.
- [ ] **ANN-215** (source marker `[-]`) Keep API/technical references out of the beginner Diploma unless needed.
- [ ] **ANN-216** (source marker `[o]`) Break educator guidance into wallet, exchange, and circular-economy sections before expanding it.

#### Local resource maps and community discovery

- [ ] **ANN-217** (source marker `[-]`) Permit “both” for on-chain/Lightning.

#### Review: how can Bitcoin function as money in your community?

- [ ] **ANN-218** (source marker `[-]`) Replace generic “Need” with the specific Bitcoin/local need.
- [ ] **ANN-219** (source marker `[-]`) Make “Back of Diploma: Next Steps” build on earlier work and scan quickly.
- [ ] **ANN-220** (source marker `[-]`) Align the first next-step question with the opening activity.
- [ ] **ANN-221** (source marker `[-]`) Use consistent present tense in the closing review and cross-check it against page 1.
- [ ] **ANN-222** (source marker `[-]`) Make the “Back of Diploma: Next Steps” heading bolder and faster to scan.

### Next Steps

#### A short “What now?” next-steps list

- [ ] **ANN-223** (source marker `[-]`) Tie “repeat one practical skill” to concrete practice.
- [ ] **ANN-224** (source marker `[-]`) Define “recognize a scam” and other safety tasks precisely.
- [ ] **ANN-225** (source marker `[-]`) Separate contributing through translation, feedback, educator support, funding, and becoming an educator.
- [ ] **ANN-226** (source marker `[-]`) Make the safety reminder scannable.
- [ ] **ANN-227** (source marker `[-]`) Add MFB/nonprofit organizational context.

#### Contribute to My First Bitcoin and the Resources Hub

- [ ] **ANN-228** (source marker `[-]`) Add a direct public GitHub feedback/contribution link or QR code and submission instructions.
- [ ] **ANN-229** (source marker `[ ]`) Verify all official program, educator, community, donation, and source links.

#### Connect with My First Bitcoin

- [ ] **ANN-230** (source marker `[ ]`) Use the remaining space intentionally; confirm/add the handwritten “Thank you note.”

### Handwriting requiring confirmation

- [ ] **ANN-231** (source marker `[ ]`) **Safety, responsibility, and no financial advice:** confirm the wording beside the education/disclaimer paragraph.
- [ ] **ANN-232** (source marker `[ ]`) **Beginner monetary history from barter to digital money:** confirm details of the introductory money/app activity and historical-view note.
- [ ] **ANN-233** (source marker `[ ]`) **Inflation and purchasing power:** confirm the “10% / too big to fail / restructuring” note.
- [ ] **ANN-234** (source marker `[ ]`) **Why Bitcoin was created:** confirm the note beside Cypherpunk history.
- [ ] **ANN-235** (source marker `[ ]`) **Bitcoin origin timeline:** confirm the note beside Satoshi’s identity.
- [ ] **ANN-236** (source marker `[ ]`) **Wallets:** confirm the proposed new-column label.
- [ ] **ANN-237** (source marker `[ ]`) **Circular economies:** confirm the reviewer’s exact name/handle.
- [ ] **ANN-238** (source marker `[ ]`) **Connect with My First Bitcoin:** confirm whether the closing note says “Thank you note.”

### Explicit approvals

- [ ] **ANN-239** (source marker `[-]`) **Seed phrases:** preserve the seed-backup checklist approved with “Love it.”
- [ ] **ANN-240** (source marker `[-]`) **Educator-selected local modules:** preserve the local-learning-choice table approved with “I like this.”
- [ ] **ANN-241** (source marker `[-]`) **Practical workshops and demonstrations:** preserve presentation/practice/production, marked “perfect place.”
- [ ] **ANN-242** (source marker `[-]`) **Local Bitcoin tools and resources:** preserve the checked workshop-result sentence.

## Consolidation coverage and provenance

| Original file | Preserved in the new workflow |
|---|---|
| Archived brand voice and refinement sources | Style script: five voice attributes, all phrases, channel adaptations, and sync provenance. |
| Archived plain-language source | Style script: all six rules, review-every-output instruction, and no-em-dash rule. |
| Archived community charter | Alignment script: mission, independence of use, network context, six principles, entry requirements, equality/reputation, benefits, commitments, end/change terms, and signature context. |
| Archived quality source | Both scripts and recurring checks: all seven controls. |
| Archived consistency register | All 12 questions, alternatives, affected files, and reconciliation order above, with a current-status caution and known updates. |
| Archived review report | All eight action areas and primary-file mappings, status definitions, editing order, baseline, historical counts and audit scope, self-check score/message example, checks/limits, and retired findings. |
| Archived action register | All 14 original action blocks and their acceptance conditions, plus every recurring quality control. |
| Archived annotation backlog | Every imported item, section, original marker, handwriting question, approval, and provenance note in the inventory above. |

The original files remain unchanged. Exact historical wording is retained there; the new scripts supply instructions and this document supplies actions, decisions, evidence, and annotation triage. No external destination, legal claim, delivery pilot, or human approval was independently verified by the consolidation itself.

### Merge accuracy review, 2026-09-19

Compared all nine original review files with the three consolidated documents. Confirmed all 242 annotations in source order, including original markers, section context, unclear handwriting, and approvals; all 12 decision entries, alternatives, affected-file lists, and reconciliation steps; and all 14 original action blocks and acceptance requirements. The consolidated register still has 19 action blocks and 242 annotation-triage checkboxes; the 12 decisions are separate from those checkbox counts.

Restored the exact six Orwell rules and full brand-source provenance; expanded compressed brand and charter details; restored the report's file map, status definitions, audit scope, and self-check example; and clarified archive handling and the consolidated decision workflow. These corrections preserve source information without turning historical proposals into approved work. Added repository instructions and September consolidation observations remain distinct from the original review findings.
