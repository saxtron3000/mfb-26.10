# Bitcoin Diploma Consistency And Release To-Do

This list records discrepancies found in the project-wide consistency check after the assessment-policy update. Complete items in priority order. The active policy is fixed: theory is 50% of the Diploma (80% app / 20% educator), practical competency is 50% (80% direct observation by an educator or approved assessor / 20% app task follow-up), and all four contributions are non-compensatory.

## Release blockers

1. Update public assessment messaging.

   - Update `public/MFB-BD-Keynote.md` and `public/elevator pitch.md` to state all four assessment contributions.
   - Remove the obsolete implication that practical assessment is entirely educator-observed or that the app supports theory only.

2. Build the objective-to-evidence crosswalk.

   - Map every certification objective in `05_objectives.md` to Student Guide teaching, formative practice, app item or educator-theory interaction, practical task where relevant, scoring rule, result field, and estimated time.
   - Do not treat a topic appearing in prose as proof that the measurable objective is taught or assessed.
   - Resolve or implement `B2.5`, `B2.6`, and the distinct evidence for `B3.11` across the plan, Student Guide, app bank, activities, assessment, and certification record.

3. Make the assessment system operational.

   - Create the final assessment blueprint and objective-level pass rules.
   - Build approved app theory items and app practical-task follow-up items.
   - Create approved educator-theory interaction criteria and concise record fields.
   - Create practical tasks, rubrics, safety-critical errors, assessor calibration, reassessment, and combined completion-record procedures.
   - Define thresholds, retries, identity, privacy, accessibility, access, outage, and correction rules before certification is offered.

## High-priority structure and publishing work

4. Replace or reclassify `17_spec.md`.

   - It is assigned as the publication specification but is currently a stakeholder overview.
   - Either turn it into the real production/release specification or move the overview elsewhere and create a specification covering versioning, layout, accessibility, citations, rights, exports, QA, sign-off, and release control.

5. Repair source, path, and link integrity.

   - Remove or correct the nonexistent archive reference in `06_plan.md`.
   - Replace obsolete paths in `18_advanced.md`, especially `../ref/chapters/...`, with the actual legacy source locations or mark them historical.
   - Correct `09_assets.md` references to the missing `feedback/` files and create or remove its example visual asset link.
   - Revalidate the missing teacher-survey CSV reference in `02_research.md`.

6. Refresh stale anchors and location maps.

   - Update `11_resources.md` Student Guide line references.
   - Regenerate the Student Guide line map in `16_lexicon.md`.
   - Update the stale headings and line placements in `09_assets.md`.
   - Refresh `00_report.md` statements that no longer reflect the current index, plan, or manuscript.

7. Separate and reduce the two publication guides.

   - Remove activity procedures from `08_student.md` where they belong in `10_activities.md`.
   - Remove planning and Activity Bank duplication from `12_educator-draft.md`.
   - Keep `12_educator-plan.md` as a subordinate internal structure plan, not a second educator authority.
   - Test the resulting learner and educator routes against the approximately eight-hour baseline.

## Ongoing quality controls

8. Add repeatable release checks.

   - Check local Markdown links and source paths.
   - Check that every required objective is represented in the crosswalk.
   - Check app and educator/assessor evidence allocations against the four-contribution model.
   - Check stale line references, heading anchors, placeholders, and external claims before publication.
   - Update public materials whenever assessment or certification policy changes.
