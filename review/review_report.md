# Bitcoin Diploma 2026.10 review report

**Review date:** 1 September 2026
**Purpose:** A current, action-oriented review of the active Diploma package. This report replaces the former mixed historical audit. It is not a source of curriculum policy.

## Scope and method

This review cross-read the active planning authorities in `workspace/`, the official Student Guide, Educator Guide, Assessment Grid, optional self-assessment materials, and the live review documents. It distinguishes:

- **implemented** — present in the current source files;
- **release blocker** — must be resolved before offering certificated delivery;
- **publication decision** — requires an owner decision before final public copy or scope can be settled; and
- **maintenance action** — improves accuracy, usability, or future editing, but does not by itself block a teaching draft.

Historical annotation notes belong in [`review_annotation_backlog.md`](review_annotation_backlog.md). They are not re-listed here as active work.

## Bottom line

The 2026.10 curriculum now has a coherent, implementable design. The four-module **Problem → Solution → Action → Connect** model, competency framework, assessment model, Student Guide, Educator Guide, Assessment Grid, and optional-app boundary broadly agree.

The package is suitable for continued editing and for non-certificated teaching development. It is **not yet ready to offer certificated delivery**: the operational assessment protocol must be validated in a real delivery route, the required local task and calibration examples must be prepared, and record/certificate governance must be approved.

The next editing cycle should focus on validating and simplifying the existing system rather than adding curriculum topics.

## Confirmed current baseline

The following statements are implemented and should be treated as the baseline for further edits:

- The Diploma consists of all four required modules. Module 4 is educator-curated and locally adaptable, but `C11` remains required for Diploma completion.
- `C1`–`C8` are educator-evaluated theoretical competencies; `C9`–`C11` require direct educator observation. Both components are equal-status, non-compensatory completion gates. No combined numerical grade is currently approved.
- The Educator Guide now contains the operational assessment protocol: competency-to-evidence crosswalk, `T1`–`T3` theoretical interactions, `P9`–`P11` practical tasks, support limits, safety-critical errors, equivalent routes, reassessment, calibration, and moderation.
- The Student Guide now explicitly teaches the required comparison of Bitcoin, stablecoins, and other crypto-assets, and distinguishes responsible learning from trading, promotion, and speculation.
- `C9.3` is explicitly a supported, low-stakes or simulated first-access requirement. No learner must buy bitcoin, use meaningful personal funds, reveal secrets, own a device, or use the app.
- The My First Bitcoin app is a voluntary self-check, recap, and discovery resource only. It is not evidence, a requirement, or a certification gate.
- The index now identifies separate roles for the microlearning plan and published optional self-assessment data.

Do not reopen these decisions unless a deliberately approved policy change requires it.

## Active actions

### 1. Validate certificated delivery

**Status:** Release blocker.

The protocol is now documented, but it is not evidence that a selected cohort can deliver valid individual assessment in the advertised route. Before certificated delivery:

1. Select and record the local `P11` variant, training environment, low-tech route, accessibility equivalents, assessors, and contingency route.
2. Run the Educator Guide capacity calculation using the actual cohort size and assessor ratio. Include individual evidence, resets, feedback, reassessment, transitions, and record keeping.
3. Pilot the complete route with learners. Record planned and actual time by module and evidence task, observed safety issues, access failures, common misunderstandings, and reassessment demand.
4. Create and calibrate against one annotated `MS` and one annotated `NY` example for `T2`, `P9`, and the selected `P11` variant.
5. Revise the route before advertising certification if the evidence cannot be observed, recorded, and reassessed safely within the promised schedule.

**Primary files:** `publish/mfb-bd-26.10/mfb-bd-eg-26.10.md`, `publish/mfb-bd-26.10/mfb-bd-assessment-grid-26.10.md`, `workspace/13_assessment.md`, `workspace/03_scope.md`.

### 2. Approve minimum record and certificate governance

**Status:** Release blocker for certification; not a blocker for using the curriculum as a teaching package.

`15_certification.md` correctly defines eligibility but leaves the operational safeguards open. Approve a proportionate record-governance pack before collecting competency evidence for certification or a pilot that retains learner results. It needs, at minimum:

- issuer and approval authority;
- permitted data, consent or assent, access roles, retention and deletion;
- correction, appeal, incident, outage, and exceptional-case routes;
- assessor permissions, audit trail, moderation, and reconciliation;
- certificate issue, replacement, revocation, and verification rules; and
- a clear rule for minors and safeguarding.

Until these are approved, public copy must not imply that a certificate-verification service already exists.

**Primary files:** `workspace/15_certification.md`, `workspace/13_assessment.md`, `workspace/03_scope.md`, and the Student Guide back matter.

### 3. Resolve the remaining scope decisions before finalizing dependent copy

**Status:** Publication decisions.

The decision log remains useful, but it has not been triaged since the current implementation work. Resolve or retire its questions as follows.

| Decision | Current evidence | Required action |
|---|---|---|
| Eight hours | `05_competencies.md` treats eight hours as a required scope boundary, while `03_scope.md`, `06_plan.md`, and the Educator Guide allow extra scheduled time when evidence requires it. | Choose a fixed complete-contact cap or a planning baseline; then align every authority and the public schedule claim. |
| October outputs | `03_scope.md` and `04_design.md` treat online/web modes as future branches. `16_spec.md` still lists an online PDF package and website-ready source as expected outputs. | Decide whether these are October deliverables or future-branch preparation, then correct the overview and release criteria. |
| Certificate status | The framework describes certificate issuance, but governance and verification remain open. | Decide whether 2026.10 offers certificated delivery once the blockers are complete, or releases an assessment-ready teaching package first. |
| Wallet open-source wording and programme links | The Student Guide includes both a general software-verification expectation and named optional My First Bitcoin pathways. | Set a short publication policy so local adaptation, named programme links, and wallet guidance do not drift between editions. |

`review_consistency.md` should then mark resolved questions 2, 3, 4, 5, and 10 as resolved or remove them. Their implemented choices are already reflected in the active authorities.

### 4. Make the Student Guide's back matter publication-ready

**Status:** Publication action.

The current Student Guide is substantially stronger and now tells learners about educator observation, feedback, and reassessment. Its three final conditional headings still read as production notes:

- `Source or update page, if included`;
- `Optional donate / support QR`; and
- `Certificate verification`.

Decide whether each item belongs in the released learner book. Rename final inclusions in learner language and remove any section that has no approved, tested destination or governing process. In particular, keep the verification section conditional on a real, privacy-preserving certificate process; otherwise it overpromises the unfinished governance work.

Also verify all named public programme, forms, case-study, network, leaderboard, source, and support destinations immediately before publication, because their availability and policy can change.

**Primary files:** `publish/mfb-bd-26.10/mfb-bd-sg-26.10.md`, `workspace/07_contents.md`, `workspace/08_assets.md`, `workspace/15_certification.md`.

### 5. Repair the source and terminology maintenance model

**Status:** High-value maintenance action.

`09_resources.md` has six useful sources, but it is too small for the range of economic, historical, technical, security, and current-context claims in the Student Guide. It also uses mutable line references. The Lexicon has the same maintenance problem: it stores first/later line-number occurrence audits alongside definitions, and many of those numbers no longer match the 1,549-line Student Guide.

Replace line locations with stable section anchors or claim IDs. Maintain separate reports for occurrence audits. For each shared claim that needs verification, record the claim or section, source type and authority, volatility, reviewer, date checked, next review date, and how it may appear in learner-facing prose. Keep genuinely local and changing facts in the Educator Guide's local verification record.

**Primary files:** `workspace/09_resources.md`, `publish/mfb-bd-26.10/mfb-bd-lx.md`, `publish/mfb-bd-26.10/mfb-bd-eg-26.10.md`.

### 6. Restore a usable review register

**Status:** Immediate maintenance action.

`review_todo.md` says it contains only current release actions and that historical annotations are in `review_annotation_backlog.md`, but it repeats the whole imported annotation backlog after the ongoing-quality-controls section. This creates two competing lists and makes active work impossible to scan.

Remove the duplicated imported material from `review_todo.md` and replace it with a single link to the archive. Keep only owner-ready actions, a status, and an acceptance condition in the active list. After resolving the decisions above, trim `review_consistency.md` in the same way.

This report deliberately does not reactivate untriaged handwritten notes. A note becomes active only when a responsible editor converts it into a specific accepted action.

**Primary files:** `review/review_todo.md`, `review/review_annotation_backlog.md`, `review/review_consistency.md`.

### 7. Finish the optional self-check as a bounded learner aid

**Status:** Publication action, not a certification blocker.

The 12-question app handoff is consistent with the non-certification policy and maps its items to the Student Guide. It still says that a score of 10–12 means “You have a strong foundation.” The check samples only selected Modules 1–3; it does not assess Module 4 or observed practical skills. Change this to a narrower message, such as “You showed a strong result on this quick self-check.”

Complete the stated independent factual and editorial review of all 12 items. Test the all-questions-on-one-screen experience on a small phone and with a screen reader before release. Do not introduce score tracking, score thresholds, or educator access.

**Primary files:** `publish/mfb-ml-26.10/mfb-ml-26.10.md`, `workspace/14_microlearning-plan.md`.

### 8. Fix the remaining local-link failure and control visual scope

**Status:** Maintenance action.

A local Markdown-link check found **162 local targets and one missing target**: `workspace/08_assets.md` embeds `../assets/diploma/bd-v-001.svg`, which is absent. Either add the approved Creative Commons mark when visual production begins or replace the embedded image with a non-broken production placeholder.

`08_assets.md` is a design brief, not an existing-asset inventory. Before production, select a small essential visual set and establish file, rights, alt-text, source, and review tracking. Conditional QR-code and certificate-verification visuals must remain out of production until their real destinations and processes are approved.

## Recommended editing sequence

1. Clean `review_todo.md` and triage `review_consistency.md` so the project has one accurate work queue.
2. Make the four publication decisions above, starting with the eight-hour rule and certificate status.
3. Prepare the selected local `P11` route, calibration examples, capacity model, and record-governance pack.
4. Pilot the full learner-and-educator pathway; revise the guides from observed evidence rather than adding topics.
5. Finalize or remove conditional Student Guide back matter, validate public destinations, and narrow the optional-app score language.
6. Convert the resource register and lexicon from line-number audits into maintainable, versioned tools.
7. Produce only the essential visuals and rerun link, accessibility, translation-readiness, and copy checks before publication.

## Checks completed in this review

- Confirmed the competency-to-evidence crosswalk, assessment tasks, rubrics, safety rules, reassessment, calibration, and moderation are present in the Educator Guide.
- Confirmed the Student Guide contains the previously missing digital-asset comparison and responsible-learning boundary.
- Confirmed the Educator Guide no longer assigns app scoring or theoretical assessment to the app.
- Confirmed `00_index.md` has separate entries for the microlearning plan and publication source.
- Checked local Markdown destinations across `workspace/`, `publish/`, `review/`, and `README.md`: 162 targets were found; one target is missing, as recorded above.

External links, current claims, rendering, screen-reader behavior, and real-cohort delivery were not validated by this document review. They remain explicit follow-up work.

## Findings removed from the former report

The former report retained a detailed 19 August snapshot and an implementation update in the same file. It therefore continued to show completed or superseded findings as active. This replacement removes, among others:

- the missing `C5` Student Guide content finding;
- the request to build the competency crosswalk and operational assessment package;
- app-scoring and app-certification regressions in the Educator Guide;
- uncertainty over whether Module 4 is part of the Diploma;
- duplicate/misidentified microlearning-document roles;
- former broken-link counts and deleted filenames; and
- historical detailed audit evidence and unresolved author-question tables.

Use the current authorities and the action list above for all subsequent editing.
