# Bitcoin Diploma 2026.10 Tune-Up Report

**Review date:** 19 August 2026  
**Scope:** the complete `workspace/` folder, with priority given to `08_student.md`, `12_educator-plan.md`, `12_educator-draft.md`, `14_microlearning-plan.md`, and `14_microlearning.md`.

## Bottom line

The project is much more coherent than it was. The current 2026.10 model is now consistent across most governing documents:

- 50% educator-evaluated theoretical understanding;
- 50% educator-observed practical competency;
- both components must pass;
- the app is an optional learner self-check and is not certification evidence; and
- Modules 1–3 are shared Core, while required Module 4 uses an educator-selected local task.

The Diploma is **not publication-ready yet**, but the remaining work is identifiable and finite. The main blocker is no longer the curriculum concept. It is the missing operational chain from each required objective to approved teaching, practice, assessment evidence, rubric, time allowance, and completion record.

The fastest route to a strong release is to stop adding topics, settle the decisions at the end of this report, build one objective crosswalk, and edit the public documents against it.

## Readiness at a glance

| Document | Current judgement | Main action |
|---|---|---|
| `08_student.md` | Strong working manuscript | Add missing required outcomes, reduce overload, and complete publication edit. |
| `12_educator-plan.md` | Sound internal outline | Keep internal; resolve the educator role and avoid duplicating the published guide. |
| `12_educator-draft.md` | Substantial and useful, but too long | Remove repeated learner content, correct residual app language, and connect it to approved assessment materials. |
| `14_microlearning-plan.md` | Useful internal roadmap | Add it to the index and define it as the planning authority. |
| `14_microlearning.md` | Good developer handoff | Complete independent review and narrow score claims to this 12-question check. |
| `13_assessment.md` | Correct model, incomplete system | Build the blueprint, rubrics, pass rules, and records. |
| `15_certification.md` | Mostly aligned | Repair its completion rule and finish governance decisions. |
| `17_spec.md` | Standalone overview | Keep it as the collaborator and stakeholder overview; do not assign it production-control duties. |

## What is working well

- The four-module narrative is clear: money problem → Bitcoin response → safe responsibility → local application.
- The Student Guide is balanced, safety-conscious, low-tech, and avoids presenting Bitcoin as a guaranteed financial outcome.
- The Educator Draft now covers all four modules and gives practical support for safety, accessibility, misconceptions, local adaptation, and learner discussion.
- Module 4 has a stronger purpose than a narrow “spending” module and is grounded in local need, comparison, safety, and voluntary participation.
- The app boundary is now clear in the main public documents. The October handoff contains exactly 12 concrete questions and explicitly excludes tracking, certification, and practical-skill claims.
- `ALL.1` and `ALL.2` are generally treated as formative rather than ideological or participation-based certificate gates.
- `99_horizon.md` provides a sensible home for post-release ideas and helps protect the October scope.

## Highest-priority tune-ups

### 1. Build one objective-to-completion crosswalk

There are 25 certification objectives plus two formative outcomes. No document currently proves that every certification objective has a complete and feasible route.

Create one table with these columns:

| Required field | What it should establish |
|---|---|
| Objective ID | The exact approved outcome. |
| Student Guide section | Where the learner encounters the required knowledge or skill. |
| Formative practice | How the learner prepares before assessment. |
| Summative evidence | What the learner must say, decide, compare, or demonstrate. |
| Evaluator and component | Educator-led theory or directly observed practice. |
| Passing criteria | What **Meets standard** means. |
| Prompting and safety failures | What support is allowed and what cannot be averaged away. |
| Time and delivery route | Teaching, practice, observation, feedback, and reassessment burden. |
| Completion record | The field used to support certificate issuance. |

Do this before creating more prose, activities, visuals, or app questions.

### 2. Close the Student Guide objective gaps

`08_student.md` is the strongest publication candidate, but its learner promise does not yet fully match `05_objectives.md`.

- Required `B2.5` and `B2.6` are developed in the Educator Draft but not taught explicitly in the Student Guide or planned contents. Add a short learner-facing comparison of Bitcoin, a generic stablecoin model, and other crypto-assets using control, issuance, verification, custody, and counterparty risk. Add a separate short distinction between education/responsible use and trading, token promotion, or speculation.
- Remove “often called ‘shitcoins’” from the formal wording of `B2.5`. It is not suitable for an objective authority, translation, or impartial public assessment.
- Make the distinct purpose of `B3.11` clear or merge it with `B3.5`/`B3.6`. At present, supported first access overlaps wallet navigation and receiving.
- Strengthen the Module 4 learner promise. The current public wording emphasizes identifying or discussing local uses, while `B4.1` and `B4.2` require an observed task and decision narration.
- Clarify in learner language that Modules 1–3 are the shared Core and Module 4 is a required Custom component for certification. “Custom” must not sound optional.

Then reduce load. The Student Guide is about 19,400 words, and Modules 3 and 4 carry many procedures, comparisons, scenarios, and safety rules. Keep learner instructions and useful worksheets, but move facilitator setup, timing, task variants, and assessment administration to linked activity pages in the Resources Hub or the Educator Guide.

Small publication defects also remain, including `recieve`, a broken heading level under “Acquiring and exchanging bitcoin,” and stale location references in supporting files.

### 3. Turn the Educator Draft into a companion, not a second textbook

`12_educator-draft.md` has improved substantially, but at about 26,700 words it still repeats many Student Guide explanations. Its best material is the material an educator cannot obtain from the learner book:

- preparation and pacing;
- misconception diagnosis;
- suggested questions and concise scripts;
- safety and stop conditions;
- accessibility and low-tech alternatives;
- Module 4 selection and validation;
- assessment administration, feedback, and reassessment.

Retain those elements and shorten repeated explanations of money, proof of work, supply, wallets, custody, transactions, and Lightning. Link educators to the relevant Student Guide section, then add only the teaching move, misconception, question, and evidence guidance.

Correct the remaining app-policy regressions:

- Module 2 says the app supplies most of the theoretical half.
- The ecosystem table still refers to app scoring.
- Appendix H requests app thresholds, retry rules, interruption recovery, and synchronization.
- “Revisit an app unit” overstates the current single optional quiz.
- The lesson-plan field should say “Optional app connection,” not “App connection.”

Also correct “the number of educator” and similar copy defects.

### 4. Resolve the Educator Plan versus Educator Draft boundary

The plan is useful as an internal checklist, but it repeats substantial assessment guidance already present in the draft. Keep `12_educator-plan.md` internal and concise. After the draft structure is approved, use the plan as an acceptance checklist rather than a parallel authority.

One governance question is unresolved: the index and most assessment documents require direct observation by an educator, while the Educator Draft allows another educator when teaching and evidence review are separated. Choose one rule and apply it everywhere.

The statement that a first-time teacher can run a safe session after ten minutes of preparation also needs qualification. It may be reasonable for a discussion-only session using prepared materials; it is not adequate preparation for live wallet work or formal assessment.

### 5. Clarify the two Microlearning documents

The split is sensible but undocumented:

- `14_microlearning-plan.md` owns scope, product constraints, future question-bank ideas, and the post-October roadmap.
- `14_microlearning.md` contains the 12-question October production handoff.

Add both to `00_index.md`, `README.md`, `06_plan.md`, and the Educator Guide source map with distinct roles. Current descriptions incorrectly say that `14_microlearning.md` contains a four-module bank; the production quiz intentionally contains 12 questions from Modules 1–3 only.

All 12 items still require independent factual and editorial approval. Pilot the all-questions-on-one-screen experience on a small phone and with a screen reader. Change “You have a strong foundation” to “You showed a strong result on this quick check,” because the quiz samples only part of the Diploma and does not assess practical competence or Module 4.

### 6. Make assessment and certification operational

The 50/50 language currently describes two non-compensatory components, but its scoring function remains unclear. If every required objective must pass, a numerical weighting does not determine eligibility. Treat the two halves as equal-status pass gates unless a reported score has a separately approved purpose.

Avoid listing “participation” as theoretical evidence. Participation can create an opportunity to produce evidence, but the evidence must be an identifiable explanation, comparison, decision, or response judged against criteria. This will improve fairness for quiet, multilingual, neurodivergent, and remote learners.

`15_certification.md` also contains an unfinished list: the assessment-complete requirements end with “and.” Repair it while defining the final completion record, educator responsibilities, appeals, corrections, privacy, retention, replacement, revocation, and verification.

### 7. Validate the eight-hour claim

The approximately eight-hour route must include teaching, direct individual observation, discussion, practice, feedback, and reassessment. Twenty-five certification objectives make this a demanding design constraint, so every required evidence activity must be integrated into the advertised course pathway.

Build a timed delivery map from the crosswalk. Calculate direct-observation demand as:

`learners × observed minutes per learner ÷ simultaneous authorized evaluators`

Test one four-session route and one intensive route. Record actual teaching, practice, assessment, transition, feedback, and reassessment time. This is strongly recommended quality work, but not a publication requirement. If the full standard does not fit, reduce or combine objectives before reducing valid evidence.

### 8. Repair document governance and production controls

- `17_spec.md` should remain an overview. The index and plan must not describe it as a publication specification or assign it production-control duties.
- `00_todo.md` mixes current release blockers with hundreds of imported annotation notes using unclear status markers. Move the imported notes to a review archive or triage them into accepted, rejected, completed, and active actions.
- `09_assets.md` proposes up to 74 visual concepts. Select a smaller minimum viable set of essential learning visuals before production; otherwise visual work may delay the curriculum and overwhelm the page.
- `11_resources.md` contains only a small source set and stale line references. Expand it for the claims that require technical, historical, banking, safety, and current-data verification.
- `16_lexicon.md` mixes a learner/editor lexicon with a stale line-location audit and “not present” records. Keep canonical definitions in the lexicon; generate occurrence reports separately.
- `18_advanced.md` is the sole holding authority for Organizations merge decisions and Advanced source trails; remove obsolete references to the former `workspace/advanced/` files.
- Other stale paths remain: the archived plan, legacy contents CSV, teacher-survey CSV, Pablo feedback paths, and the example visual asset. Repair or explicitly mark them as unavailable historical inputs.

## Recommended release sequence

1. Answer the yes/no decisions below and record them in `00_index.md` or the relevant authority.
2. Build the complete objective crosswalk and timed evidence map.
3. Finalize approved theory interactions, practical tasks, rubrics, records, reassessment, and certification governance.
4. Add the missing Student Guide outcomes and reduce excess learner content.
5. Reduce the Educator Draft to facilitation and assessment support; remove residual app and duplicated textbook material.
6. Independently review and pilot the 12-question optional quiz.
7. Keep `17_spec.md` as the collaborator overview, repair sources and links, then run copy, accessibility, translation-readiness, and low-tech QA.
8. Test the complete course before describing it as an eight-hour assessed Diploma; record the findings, but do not make a pilot a publication requirement.

## Author decisions — please answer yes or no

Recommended answers are included to make the next pass faster.

| # | Yes/no decision | Recommendation |
|---:|---|---|
| 1 | Should the 50/50 model mean two equal-status pass gates rather than a compensatory numerical score? | **Yes.** |
| 2 | Should required assessment time be allowed outside the approximately eight hours of teaching when cohort size or reassessment requires it? | **No.** |
| 3 | Should an educator who is not the course educator be allowed to review practical evidence? | **Yes**, if criteria, calibration, records, and accountability are defined. |
| 4 | Is Module 4 required for every learner seeking a certificate, even though its local task is Custom? | **Yes.** |
| 5 | Should `B2.5` and `B2.6` remain required objectives and receive short Student Guide sections? | **Yes.** |
| 6 | Should `B3.11` remain a separate certification objective instead of being merged into `B3.5` and `B3.6`? | **Yes**, unless “first access” produces genuinely distinct evidence. |
| 7 | Should `12_educator-plan.md` remain internal and subordinate to the published Educator Guide? | **Yes.** |
| 8 | Should `14_microlearning-plan.md` be the internal app roadmap and `14_microlearning.md` be the October production handoff? | **Yes.** |
| 9 | Should the October quiz describe results only as performance on a quick self-check, not as evidence of Diploma-level foundation or competence? | **Yes.** |
| 10 | Should `17_spec.md` become the actual publication specification, with its overview material moved elsewhere? | **No.** |
| 11 | Should `18_advanced.md` become the sole Advanced holding authority if the two missing `workspace/advanced/` files will not be restored? | **Yes.** |
| 12 | Should the imported annotation backlog be moved out of `00_todo.md` so that file contains only current release actions? | **Yes.** |
| 13 | Should a timed, low-tech pilot with real educator assessment be a publication requirement? | **No** |

## Final judgement

The Diploma now has a strong educational identity, a defensible four-module structure, and two promising public guides. Its next gains will come from subtraction and operational detail rather than further expansion. The decisive work is to make every objective teachable, assessable, recordable, and realistic within the promised delivery model—then remove anything that does not support that chain.
