# Workspace Consistency Decisions

## Purpose

This is a decision log from a critical cross-read of the active workspace on 2026-08-19. It identifies choices that cannot all be true at once, or whose current wording would lead different authors or educators to make different implementation decisions.

Reply with the question number and `A` or `B` (for example, `1A, 2B, 3A`). After decisions are made, update the affected source-of-truth files first, then bring dependent files into alignment.

This file records questions only. It is not a source of truth for the decisions themselves.

---

## 1. Is eight hours a fixed Core boundary or a planning baseline?

`05_objectives.md` says an objective that cannot be taught, practised, and assessed inside eight hours is not Core. `03_scope.md`, `06_plan.md`, and `12_educator-draft.md` instead describe approximately eight hours as a baseline that may need additional time for valid evidence, feedback, and reassessment. `02_research.md` identifies this as an unresolved governance conflict.

**A. Fixed boundary.** Keep eight hours as the maximum complete learner-contact time. Reduce, combine, or move objectives and required evidence until the complete course, including reassessment, fits.

**B. Planning baseline.** Keep the present objective set and treat eight hours as the shortest planned route; require longer scheduled delivery where cohort size, access needs, practice, observation, or reassessment demand it.

Affected: `05_objectives.md`, `03_scope.md`, `06_plan.md`, `02_research.md`, `08_student.md`, `12_educator-draft.md`, `13_assessment.md`, `17_spec.md`.

## 2. Does “50% / 50%” describe a score or two completion gates?

The assessment and certification files require both components to be passed and recorded as `Meets standard` or `Not yet`, but still call each component 50% of a total assessment. This can be read as either a weighted grade or two non-compensatory status checks.

**A. Weighted grade plus gates.** Retain a numerical 50/50 calculation and publish objective-level thresholds, aggregation, and reporting rules for both components.

**B. Two completion gates.** Treat 50/50 as a programme-balance statement only; certificates depend on passing every required objective and safety criterion, with no combined numerical grade.

Affected: `05_objectives.md`, `06_plan.md`, `13_assessment.md`, `15_certification.md`, `17_spec.md`, public materials.

## 3. Is Module 4 outside the shared Core or a required part of the Core Diploma?

The plan calls Module 4 educator-selected **Custom** content, while `17_spec.md` says the first three modules are the shared Core and the fourth is selected locally. At the same time, `05_objectives.md`, `13_assessment.md`, and `15_certification.md` make an approved Module 4 task mandatory for certification. The term “Core Diploma” therefore has two possible meanings.

**A. Core means Modules 1–3 only.** Module 4 remains required Custom certification work, and all learner/public language distinguishes “shared Core” from “required Custom module.”

**B. Core means the complete certificated Diploma.** Module 4 is a required Core component with locally selectable content; reserve “shared Core” for Modules 1–3.

Affected: `00_index.md`, `04_design.md`, `05_objectives.md`, `06_plan.md`, `08_student.md`, `12_educator-draft.md`, `13_assessment.md`, `15_certification.md`, `17_spec.md`.

## 4. What must the Module 3 learner promise say?

`06_plan.md` promises demonstration of wallet, transaction, verification, recovery-readiness, and safety actions. `05_objectives.md` requires several directly observed performances. `17_spec.md` says learners can only “identify” basic safety practices, which understates the assessed standard.

**A. Demonstrate safely under support.** Use one consistent learner promise: beginners demonstrate specified wallet, transaction, verification, recovery-readiness, and safety actions in an approved supported, simulated, testnet, or low-stakes environment.

**B. Identify and explain only.** Reframe Module 3 certification around understanding and safety judgment; move hands-on demonstrations out of required Diploma certification.

Affected: `05_objectives.md`, `06_plan.md`, `08_student.md`, `12_educator-draft.md`, `13_assessment.md`, `15_certification.md`, `17_spec.md`.

## 5. Is first access to bitcoin a required Module 3 competency?

`B3.11` requires a learner to gain access to bitcoin through an approved low-stakes or simulated pathway, receive it, and check relevant information. Elsewhere the learner-facing material says learners do not need to buy bitcoin, install a wallet, or use meaningful personal funds. These can coexist only if the exact minimum experience is explicit.

**A. Required simulated or low-stakes first access.** Every certificated learner completes `B3.11`; a prepared wallet, test environment, educator-provided training balance, or no-value simulation is sufficient, and no purchase or personal funds are required.

**B. Optional first access.** Remove `B3.11` as a certification objective; certification requires safe wallet navigation and a receive/send simulation, but not access to bitcoin.

Affected: `05_objectives.md`, `08_student.md`, `12_educator-draft.md`, `13_assessment.md`, `15_certification.md`, `10_activities.md`.

## 6. What is the Core requirement for Lightning?

`06_plan.md` places Lightning setup and payment practice normally in Custom, but `B3.8`, the Student Guide, and assessment requirements place the on-chain/Lightning distinction in Module 3. The boundary between required understanding and required use should be stated once.

**A. Core understanding; Custom practice.** Every learner compares on-chain and Lightning in a guided scenario; Lightning setup, invoices, and payments are only selected Module 4 practice.

**B. Core supported use.** Every learner completes an approved Lightning receive/send exercise in Module 3; Module 4 may deepen or localize it.

Affected: `05_objectives.md`, `06_plan.md`, `07_contents.md`, `08_student.md`, `10_activities.md`, `12_educator-draft.md`, `13_assessment.md`, `16_lexicon.md`, `17_spec.md`.

## 7. Are online PDF, website-ready content, and future branches October deliverables?

`03_scope.md` and `04_design.md` treat online PDF, cohort, self-paced, web, and cross-modal formats as documented future branches, not current implementation requirements. `17_spec.md` lists an online PDF package and website-ready source files among expected 2026.10 outputs.

**A. October deliverables.** Include an online PDF package and website-ready source files in the release completion criteria, with the same outcomes and assessment safeguards.

**B. Future branch preparation.** Release the complete low-tech print/PDF and educator-led pathway in October; retain only branch notes, source readiness, and design constraints for online/web formats.

Affected: `03_scope.md`, `04_design.md`, `06_plan.md`, `08_student.md`, `12_educator-draft.md`, `17_spec.md`, `99_horizon.md`.

## 8. How strict is the learner-facing “open-source wallet” guidance?

`06_plan.md` includes an “open-source wallet preference” in Core safety content. The workspace also prohibits global tool recommendations and places detailed wallet-design considerations in Advanced. A preference can sound like a universal recommendation unless its purpose and limit are defined.

**A. Keep a general preference.** Teach that learners can consider whether wallet software is openly inspectable, alongside custody, recovery, safety, compatibility, and local support; do not name a global preferred wallet.

**B. Move it out of learner Core.** Keep wallet open-source evaluation as educator/Advanced context and teach Core learners only the custody, recovery, verification, and safety criteria needed for beginner use.

Affected: `06_plan.md`, `05_objectives.md`, `08_student.md`, `10_activities.md`, `12_educator-draft.md`, `16_lexicon.md`, `18_advanced.md`.

## 9. Is named programme-pathway promotion part of the Student Guide?

The Student Guide directs learners to specific My First Bitcoin programmes and public webpages. The publication guardrails otherwise emphasize durable offline material, sparse QR codes, and avoiding fragile or named-service dependencies. This needs an explicit publication policy rather than an accidental exception.

**A. Keep a short, curated pathways section.** Retain named My First Bitcoin next steps and links, but make them optional, date-checked, and available as a plain-text offline reference.

**B. Keep the Student Guide programme-neutral.** Remove named pathways and live links from learner chapters; place changing programme navigation on a maintained update page or educator handout.

Affected: `06_plan.md`, `08_student.md`, `11_resources.md`, `12_educator-draft.md`, `17_spec.md`.

## 10. Which learner manuscript is the canonical file name?

The repository guidance assigns learner-facing prose to `workspace/08_draft.md`, but the active index, source-of-truth map, and workspace use `08_student.md`. This is a maintenance and publishing ambiguity rather than a curriculum disagreement.

**A. Standardize on `08_student.md`.** Update the repository guidance and any stale references to name the existing Student Guide file.

**B. Standardize on `08_draft.md`.** Rename or migrate the Student Guide to the repository-guideline filename and update the index and links.

Affected: `AGENTS.md`, `00_index.md`, `06_plan.md`, `07_contents.md`, `08_student.md`, `12_educator-draft.md`, `16_lexicon.md`, `17_spec.md`.

## 11. Is a certificate a 2026.10 operational output or a governed future implementation?

The assessment and certification documents define a mandatory prerequisite and issuance workflow, while `03_scope.md` leaves certificate governance, identity, verification, and infrastructure out of scope. Public wording needs to avoid promising an operational credential system before its owner and controls exist.

**A. Certificate issuance is part of 2026.10.** Add a minimum issuer, approval, record, correction, privacy, and verification process to October completion requirements.

**B. Assessment-complete is the October curriculum output.** Keep the certification prerequisite and public claim, but defer actual issuance and verification implementation until governed separately; do not imply that a credential service is already available.

Affected: `03_scope.md`, `12_educator-draft.md`, `13_assessment.md`, `15_certification.md`, `17_spec.md`, `99_horizon.md`, public materials.

## 12. Should the first release include a timed, certification-complete set of activities?

The design requires approved theory interactions, direct observation, rubrics, records, and equivalent variants. `10_activities.md` contains a strong template and legacy inventory but not the complete set of approved, timed, rubric-backed tasks needed to support every objective. Other files sometimes describe the assessment system as if it is ready to operate.

**A. Release only when operational.** Make a certification-complete set of activities—objective-to-evidence crosswalk, approved tasks, rubrics, records, variants, and educator calibration—a release dependency.

**B. Release the curriculum framework first.** Publish the Student and Educator guides as a provisional teaching package; defer certification claims and assessment-complete status until the required activities are operational in the Resources Hub.

Affected: `02_research.md`, `03_scope.md`, `05_objectives.md`, `10_activities.md`, `12_educator-draft.md`, `13_assessment.md`, `15_certification.md`, `17_spec.md`, `99_horizon.md`.

---

## Reconciliation order after decisions

1. Update authorities: `06_plan.md`, `05_objectives.md`, `13_assessment.md`, and `15_certification.md`.
2. Align delivery files: `08_student.md`, `10_activities.md`, and `12_educator-draft.md`.
3. Align planning and communication: `03_scope.md`, `04_design.md`, `07_contents.md`, `17_spec.md`, and `99_horizon.md`.
4. Update the index, lexicon, resource register, and any public materials that repeat the resolved decision.
