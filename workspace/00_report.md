# Bitcoin Diploma 2026.10 consistency and release-readiness report

**Review date:** 19 August 2026  
**Scope:** All current Markdown and publication-source files in `workspace/`, `publish/`, `review/`, and `public/`, plus the root repository guidance.  
**Purpose:** An actionable consistency review. This is a review snapshot, not a new source of curriculum policy.

**Resolution update, 19 August 2026:** Repository-migration item 2 is complete. All 40 broken local Markdown-link occurrences identified by this review were repaired; a repository-wide recheck found 0 broken occurrences across 110 local links. Later descriptions of those broken paths preserve the original audit finding.

## TL;DR

The Diploma is substantially more coherent than it was in the earlier review. The four-module story is clear, the Student Guide now covers the previously missing stablecoin/non-Bitcoin comparison and trading/speculation boundary, Module 4 is consistently required but locally adaptable, `B3.11` is explicit, and almost all active files now agree that the app is optional and supplies no certification evidence.

It is **not yet ready to publish as a certificated Diploma**. The main issue is no longer missing learner content; it is the gap between a strong curriculum manuscript and an operational, defensible assessment system.

Address these items in order:

1. **Build the assessment package before making certification operational.** The project still lacks the final objective-to-evidence crosswalk, approved theory interactions, practical tasks, rubrics, prompting rules, assessor calibration, completion record, and privacy/appeals process. The Educator Guide itself says it is not publication-ready.
2. **Resolved: finish the repository migration.** The **40 broken Markdown-link occurrences across six files** were repaired on 19 August 2026, including the publication, workspace, self-assessment, research, asset, and Advanced-location references.
3. **Remove the remaining assessment-policy regressions.** The Educator Guide says in one place that the app supplies “most” theory, although every authority says the app is optional and non-certifying. Its final-approval list also asks for obsolete app thresholds and synchronization. Two planning passages understate the educator's theory-assessment role.
4. **Resolve what “50% / 50%” means.** The project calls the components non-compensatory gates but also uses “score,” “worth,” and “share.” The cleanest rule is: theory and practice are equally important component gates; every required mapped objective must pass; there is no combined compensating grade unless a numerical reporting model is deliberately designed.
5. **Prove the approximately eight-hour pathway.** There are 25 certification objectives, a 20,000-word Student Guide, direct observation, feedback, recording, and possible reassessment. This may be workable, but no timed objective-level route or cohort-capacity model proves it. Treat eight hours as unvalidated until a complete route is timed with real educators and learners.
6. **Give the public files a final publication edit.** The Student Guide is strong but retains a typo, a heading-level error, conditional production headings, and certificate-verification language ahead of an approved system. The 26,700-word Educator Guide contains broken links, planning commentary, unresolved-governance material, and avoidable repetition.
7. **Clean the review system.** `review/00_consistency.md` still asks questions that the current documents have partly answered and uses deleted filenames. `review/00_todo.md` says archived annotations are separate but then embeds the imported backlog under a malformed list heading. There are now two report locations; the index says reports belong in `review/`, while this user-requested report is in `workspace/`.

**Overall judgment:** The learner and educator content has a credible foundation. Do not spend the next work cycle adding more curriculum prose. Spend it completing traceability, assessment operations, file integrity, publication cleanup, and a timed pilot.

---

## 1. Current standard observed in the repository

The active index and governing documents currently establish this model:

- four required modules: Understanding Money, How Bitcoin Works, Using Bitcoin Safely, and Bitcoin in Your Community;
- Modules 1–3 are the shared Core; Module 4 is required Custom work with a locally selected task;
- educator-facilitated delivery may be in person or online and must support low-tech/offline use;
- the app is optional self-assessment, recap, and discovery only;
- theory and practice are both required and non-compensatory;
- educators evaluate approved theoretical evidence and directly observe practical evidence; and
- the approximately eight-hour pathway is intended to include teaching, practice, assessment, feedback, and recording.

This report uses that as the current baseline. One author confirmation is still important because an earlier project direction assigned formal evidence to the app: **is the present app-optional, non-certifying model intentional and final for 2026.10?** See the yes/no decisions at the end.

## 2. What has improved

Several important findings from the previous report are now resolved or materially improved:

- The Student Guide now directly covers Bitcoin, stablecoins, and other crypto-assets, satisfying the content intent of `B2.5`.
- It now distinguishes education and responsible use from trading, token promotion, and speculation, satisfying the content intent of `B2.6`.
- The educator material explicitly includes `B2.5`, `B2.6`, and the separate first-access objective `B3.11`.
- The Student Guide clearly says learners do not need to buy bitcoin, install a personal wallet, or use meaningful personal funds; prepared, simulated, testnet, and low-stakes routes are allowed.
- Module 4 is no longer presented as a disposable bonus. The public guides consistently describe it as required but locally selectable and broader than spending.
- `ALL.1` and `ALL.2` are now consistently described in the main objective and educator materials as formative rather than independent certification gates.
- `17_spec.md` now respects its real role as a concise collaborator/stakeholder overview rather than pretending to be a production specification.
- The optional self-assessment has a clear October MVP, 12 short/long item pairs, stable identifiers, developer fields, answer keys, explanations, and a firm non-certification boundary.
- The Educator Quick Start Guide is concise and does its job well. It is the clearest entry point in the package.

These are meaningful improvements. The next phase should consolidate them rather than reopen settled content unnecessarily.

## 3. Release blockers

### 3.1 Assessment is specified but not operational

`05_objectives.md` defines 25 certification objectives plus two formative cross-module outcomes. The governing assessment files correctly demand objective-aligned evidence, but the required implementation does not yet exist:

- `13_assessment.md:256` says final objective-level thresholds and aggregation remain a release dependency.
- `13_assessment.md:286–296` lists the blueprint, tasks, rubrics, calibration, records, privacy, appeals, and certification rules still to resolve.
- `10_activities.md` is principally a legacy inventory, template, question seed, and work-in-progress category list. It is not a complete approved task bank.
- A literal ID check finds only nine of the 27 objective/formative IDs in `10_activities.md`; this is not itself proof of missing teaching, but it confirms that a complete explicit crosswalk has not been built.
- `15_certification.md` leaves issuer authority, identity, consent, retention, correction, appeals, revocation, and verification unresolved.
- `publish/mfb-bd/mfb-bd-eg-26.10.md:9–26` openly says the Guide is not publication-ready because approved tasks, rubrics, governance, and validation are incomplete.

Practical action:

Create one versioned table with one row for each of the 25 certification objectives. Each row should name:

1. Student Guide teaching location;
2. prerequisite knowledge;
3. formative practice;
4. approved summative evidence;
5. theory or practical component;
6. task and rubric ID;
7. permitted prompting;
8. safety-critical errors;
9. result field;
10. accessibility/equivalent variant;
11. remediation and reassessment route; and
12. planned learner and educator time.

Then produce the minimum viable assessment pack from that table. Until this exists, describe the guides as a teaching draft and avoid implying that certification can already be issued consistently.

### 3.2 The file migration was incomplete — resolved

The paths in this section were repaired on 19 August 2026. The local-link release check now passes with 0 broken occurrences across 110 checked links.

The project now separates planning (`workspace/`), publication (`publish/`), and review (`review/`). That is a good governance improvement, but dependent paths were not fully updated.

The local link check found 40 broken Markdown-link occurrences:

| File | Broken occurrences | Main cause |
|---|---:|---|
| `README.md` | 8 | Student, Educator, microlearning, and Advanced paths point to non-existent locations. |
| `workspace/00_index.md` | 8 | The same publication and Advanced paths are wrong in both tables. |
| `publish/mfb-bd/mfb-bd-eg-26.10.md` | 18 | Links still assume the publication lives beside deleted workspace files such as `08_student.md`, `12_educator-plan.md`, and `14_microlearning.md`. |
| `workspace/02_research.md` | 4 | Links point to a missing `research/` directory. |
| `publish/mfb-ml/mfb-ml-26.10.md` | 1 | The Microlearning plan link is relative to the wrong directory. |
| `workspace/09_assets.md` | 1 | The referenced SVG does not exist. |

The actual main publication paths are:

- `publish/mfb-bd/mfb-bd-sg-26.10.md`;
- `publish/mfb-bd/mfb-bd-eg-26.10.md`;
- `publish/mfb-bd/mfb-bd-qs-26.10.md`; and
- `publish/mfb-ml/mfb-ml-26.10.md`.

There is no `advanced/18_advanced.md`; the file remains at `workspace/18_advanced.md`. There is also no active `ref/` directory, although `workspace/18_advanced.md` contains 119 textual references to paths beneath it. This breaks the Advanced source trail even where the references are not formatted as Markdown links.

Practical action:

- choose and document the real Advanced location;
- update the root README and index first;
- update all internal links in the publication files using paths relative to their new directories;
- decide whether the missing research and reference materials should be restored, moved, or explicitly retired; and
- run the local-link check as a release gate.

### 3.3 The eight-hour route is not validated

The workload risk is not simply that the Student Guide is approximately 20,000 words. The risk is the combination of:

- 25 certification objectives;
- four modules;
- explanation, discussion, practice, and local adaptation;
- individual theoretical evidence;
- direct observation of Module 3 and Module 4 performance;
- feedback, recording, accommodations, and reassessment; and
- cohort-size and educator-capacity constraints.

The documents also still differ subtly:

- `05_objectives.md:25` makes eight hours a hard Core test: if an objective cannot be taught, practised, and assessed within it, the objective is not Core.
- `03_scope.md:444` treats eight hours as a planning baseline and allows additional scheduled time.
- `06_plan.md:326` says to schedule a follow-up when necessary.
- `12_educator-plan.md:81–94` says assessment must not become a separate follow-up outside the advertised Diploma.

These can be harmonized by defining eight hours as an advertised baseline rather than a universal maximum, while requiring every cohort's advertised schedule to include its required assessment. A course needing ten hours should be advertised as ten hours, not as an eight-hour course plus a hidden assessment appointment.

Practical action:

- build a module-by-module minute budget from the objective crosswalk;
- define cohort-size bands and the number of educators/observers required;
- state whether breaks are inside or outside the advertised eight hours;
- time one complete four-session route and one intensive route; and
- reduce or combine evidence only when validity is preserved.

## 4. Policy and design drift to correct

### 4.1 One obsolete app-assessment statement remains public

`publish/mfb-bd/mfb-bd-eg-26.10.md:1328` says an educator task supplies theoretical evidence “while the app supplies most of the theoretical half.” This directly contradicts the index, objectives, design, assessment, certification, Quick Start, Student Guide, and the Educator Guide's own opening.

`publish/mfb-bd/mfb-bd-eg-26.10.md:3132` also lists final app thresholds, retry rules, interruption recovery, and synchronization as a publication approval dependency. Those may be useful product questions, but they are not certification blockers under the current optional, learner-owned self-assessment model.

Remove or rewrite both passages after the author confirms the app boundary.

### 4.2 Educator theory-assessment ownership is occasionally understated

Most files correctly say educators evaluate both components. Two passages drift:

- `workspace/12_educator-plan.md:61` says educators provide formative theory feedback and directly evaluate practical competencies, omitting their approved summative theory role.
- `workspace/13_assessment.md:215` begins “Educators facilitate theory and assess practical competency,” even though the same file assigns the full theory component to educators.

Use one role sentence everywhere: **The educator facilitates learning, evaluates approved objective-aligned theoretical evidence, and directly evaluates approved practical evidence. Ordinary classroom interactions remain formative unless they meet the approved summative criteria.**

### 4.3 “50/50” is still semantically unclear

The project repeatedly describes two non-compensatory components but also calls them “worth 50%,” a “share,” an “allocation,” or a “score.” `review/00_consistency.md` correctly identifies this ambiguity.

Recommended harmonization:

> The Diploma has two equally important, non-compensatory completion gates: theoretical understanding and practical competency. A learner must meet the approved standard for every required mapped objective and every safety-critical criterion. Results are recorded separately as Meets standard or Not yet. No combined average can compensate for an unmet gate.

If a numerical score is needed for reporting, define it only after objective weights, aggregation, rounding, minimums, and treatment of safety-critical failures are approved. Do not use “50%” as though it already provides those rules.

### 4.4 Certificate language is ahead of certificate governance

The Student Guide says a certificate is issued and describes verification fields, while `15_certification.md` says issuer, identity, privacy, correction, revocation, and verification are unresolved. The governing rule is sound—no certificate without both components—but the delivery mechanism is not operational.

Until governance is approved, public wording should say that certificates **may be issued through an approved implementation** after both gates are met. Do not promise codes, links, QR verification, revocation status, or an issuing system before those features exist.

There is also a grammatical defect at `15_certification.md:22–25`: the assessment-complete list ends with “and” but has no final list item.

## 5. Public-facing document review

### 5.1 Student Guide

**Role judgment:** Mostly respects its learner-facing role. It carries the learning path, questions, safety rules, reflection, and local application without exposing objective IDs or excessive internal governance.

**Strengths:** Clear four-module narrative; good safety framing; strong custody and recovery guidance; balanced language around stablecoins and other crypto-assets; explicit no-purchase/no-high-stakes requirement; useful Module 4 local-context framework; optional-app boundary is clear.

**Tune-ups:**

- Correct `recieve` to `receive` at line 796.
- Change the Module 3 `Awareness, not financial advice` heading at line 1090 from `##` to `###`; it currently breaks the module hierarchy.
- Replace production placeholders such as “Source or update page, if included” and “Optional donate / support QR” with final learner headings or remove the sections.
- Add one short, learner-readable assessment explanation: two separate gates, examples of acceptable evidence, what `Not yet` means, and the right to feedback/reassessment.
- Make certificate-verification wording conditional until the real system exists.
- Review the named programme, donation, and web links as maintained back matter with an edition/verification date. They should not interrupt the durable core learning path.
- Run a final copyedit and terminology check after the lexicon location map is rebuilt.

The Guide is substantial. Avoid adding more explanations unless the objective crosswalk proves a gap. Prefer replacing or tightening existing text.

### 5.2 Educator Guide and Educator plan

**Role judgment:** The plan understands the correct role: the Guide should be a facilitation engine rather than a second Student Book. The publication draft partially achieves this through scripts, flows, misconceptions, safety protocols, Custom-module design, and reusable appendices. It is nevertheless too close to an internal master manual to be called publication-ready.

**Main issues:**

- It is approximately 26,700 words and repeats substantial learner explanations.
- It carries an “About this draft” disclaimer, open governance, source-map material for editors, and a final-approval backlog inside the publication source.
- Eighteen local links are broken after the repository move.
- The obsolete app-theory sentence and app-threshold blocker contradict current policy.
- It contains small editorial defects, including “the number of educator” at line 1402.
- The line 43 promise that ten minutes of preparation is enough to run a safe first session is too strong for an unvalidated course involving practical safety and assessment. The Quick Start can support orientation, but new educators still need the applicable safety/task preparation.

Practical action:

- keep the Quick Start as the front door;
- create one two-page run sheet per module;
- keep only the explanations educators need to teach, correct a misconception, or assess safely;
- move editorial source maps and approval backlogs to `workspace/` or `review/`;
- keep rubrics and records in a clearly separated assessment appendix or companion pack; and
- test preparation and delivery with educators who did not write the Guide.

### 5.3 Optional self-assessment and microlearning plan

**Role judgment:** The plan and October data now have a clear, appropriately narrow role. The separation between the 12-question MVP and the future question-bank expansion is good.

**Tune-ups:**

- Repair the Microlearning plan link and replace the deleted `08_student.md` review reference with the actual Student Guide title/path convention.
- Complete the stated independent factual and editorial review for all 12 selected items before publication.
- Add a compact selection rationale. The current set maps to 11 objective IDs, maps two items to `B3.1`, and omits `B2.5` and `B2.6`. Full objective coverage is not required for an optional 12-item quiz, but the chosen balance should be intentional.
- Label objective links as the **objective facet supported**, not evidence that the whole objective is assessed. For example, the purchasing-power item touches only one part of the broad `B1.5` objective.
- Check parity among the Markdown source, short CSV, long CSV, and app import after the final variant choices are made.

### 5.4 Educator Quick Start

**Role judgment:** Strong and concise. It gives a realistic first route without duplicating the full guide.

Keep it short. Once the final assessment pack exists, link directly to the approved record, rubric, and task bundle rather than only to the working framework.

## 6. Supporting-document role review

| Document or group | Role judgment | Action |
|---|---|---|
| `00_index.md` | The role map is much clearer, but its most important publication and Advanced links are wrong. | Repair paths and add the actual publication-specification/QA owner. |
| `01_review.md` | Useful historical diagnosis; mostly respects its role. | Keep historical; update only stale file names that impede navigation. |
| `02_research.md` | Strong synthesis and unusually candid implementation critique. Four evidence-review links are missing. | Restore or retire the missing research artifacts and distinguish completed research from the large tool wish list. |
| `03_scope.md` | Good workstream coverage, but milestones mix planned, completed, and still-open outputs. | Add explicit status per deliverable and reconcile the eight-hour rule. |
| `04_design.md` | Coherent design authority with a few open assumptions. | Close the audience assumption and use the final two-gate wording. |
| `05_objectives.md` | Strongest governing document; 25 certification IDs and two formative IDs are now clear. | Finalize evidence/pass criteria; retain `B4.2` as narration embedded in practical performance. |
| `06_plan.md` | Sound architecture, but it still points to deleted pre-migration filenames and permits an ambiguous follow-up. | Update ownership paths and the timing rule. |
| `07_contents.md` | Concise and aligned with the Student Guide. | Update only after final assessment/production headings are settled. |
| `09_assets.md` | Detailed visual planning, but it is a 10,000-word specification with no corresponding asset set in the repository and one broken SVG link. | Prioritize a minimum asset set; track production status outside the semantic visual index. |
| `10_activities.md` | Good principles and template, but not yet the activity/task library its downstream documents require. | Build the approved, timed, rubric-backed minimum set. This is a release blocker. |
| `11_resources.md` | Too small and its Student Guide filename/line locations are stale. | Rebuild as a claim-to-source register using stable headings or claim IDs rather than volatile line numbers. |
| `12_educator-plan.md` | Good structural plan and mostly avoids duplicating learner prose. | Align role sentence, paths, and timing; use it as the acceptance checklist for the public Guide. |
| `13_assessment.md` | Correct framework but explicitly unfinished. | Convert its Section 13 questions into assigned release tasks and approved artifacts. |
| `15_certification.md` | Correct prerequisite logic, incomplete governance. | Fix the dangling list and do not operationalize certificates until the governance pack exists. |
| `16_lexicon.md` | Useful terminology authority, but the line map points to deleted `workspace/08_student.md` and stale lines. | Preserve definitions; rebuild locations against the published Student Guide, preferably with heading/term IDs. |
| `17_spec.md` | Now correctly functions as an overview. | Keep this role. Create a separate compact publication checklist rather than expanding it again. |
| `18_advanced.md` | Appropriately keeps depth out of the beginner Diploma, but its documented location and 119 reference-path mentions are broken. | Decide location and restore source-trail integrity before relying on it for provenance. |
| `99_horizon.md` | Useful future-work register. | Update stale filenames and keep post-release ideas from leaking into October blockers. |
| `review/` | Correct conceptual home for reviews, but the current files overlap and contain stale state. | Reconcile the two reports, close answered decisions, and separate the active to-do from the annotation archive. |

## 7. Conciseness and overlap

The planning set still repeats the same policy in many places: duration, Core/Custom/Advanced, optional app, 50/50 assessment, offline delivery, Bitcoin-only boundaries, and certification prerequisites. Some repetition is necessary for standalone documents, but drift has already appeared because the same rule is manually restated.

Use a simple dependency pattern:

- `00_index.md`: ownership and navigation only;
- `05_objectives.md`: what learners must achieve;
- `06_plan.md`: architecture and boundaries;
- `13_assessment.md`: how evidence is judged;
- `15_certification.md`: when a credential may be issued;
- publication files: short audience-appropriate restatements with links to the governing source; and
- review files: problems and actions, never policy.

For repeated high-risk rules, maintain a short canonical wording block in the owning file and copy it only where the audience genuinely needs it. Add a release search for retired phrases and deleted filenames.

The biggest conciseness gain will come from the Educator Guide. Do not shorten it by removing safety, misconceptions, adaptation, or assessment support. Shorten it by removing repeated learner exposition, editor-only source mapping, planning status, and duplicated policy explanations.

## 8. Recommended next work cycle

### First: one-day integrity pass

- Repair all local publication, workspace, research, Advanced, and asset paths.
- Remove the obsolete app-assessment sentence and app-threshold blocker.
- Fix the Student Guide typo, heading level, and conditional headings.
- Fix the certification dangling list and small editorial errors.
- Update stale filenames in the plan, lexicon, resources, horizon register, and review files.

### Second: assessment sprint

- Build the 25-row objective-to-evidence crosswalk.
- Approve the minimum theory interactions and Module 3/4 practical tasks.
- Write rubrics, prompting limits, safety-critical failures, records, and reassessment rules.
- Produce two `Meets standard` and two `Not yet` calibration examples for each critical task family.
- Approve the minimum privacy, safeguarding, accessibility, correction, and appeals pack.

### Third: usability and timing pilot

- Test the Student Guide and module run sheets with new educators and representative learners.
- Record actual minutes by teaching, discussion, practice, theory evidence, practical observation, feedback, recording, and reassessment.
- Test at more than one cohort size and with at least one low-tech delivery.
- Revise objective load, task integration, schedule, or staffing based on evidence.

### Fourth: publication pass

- Remove planning and unresolved-governance prose from `publish/`.
- Complete factual/editorial review of the optional quiz.
- Produce the minimum required visual set and accessible alternatives.
- Add a compact production checklist covering version, rights, citations, accessibility, links/QRs, translation, export, QA, approval, and release.
- Run final link, terminology, objective, safety, and spelling checks.

## 9. Yes/no decisions for the author

Reply with `1 Yes, 2 No`, and so on. Recommended answers are shown.

1. **Should the app remain optional and supply no assessment or certification evidence in 2026.10?** **Recommended: Yes.** A No answer requires a deliberate rewrite of the current authorities and public guides.
2. **Should 50/50 mean two equally important non-compensatory gates, with no combined numerical grade?** **Recommended: Yes.**
3. **Should approximately eight hours be a planning baseline rather than a universal maximum, provided every cohort's full assessment is included in its advertised schedule?** **Recommended: Yes.**
4. **Should publication with certification claims wait until the complete crosswalk, approved tasks, rubrics, records, and minimum governance pack exist?** **Recommended: Yes.**
5. **Should Module 4 remain required for certification but locally selectable through approved equivalent tasks?** **Recommended: Yes.**
6. **Should `B3.11` remain a distinct required first-access performance that may be completed with simulation, testnet, a prepared wallet, or a low-stakes training balance?** **Recommended: Yes.**
7. **Should the Educator Guide lose its draft-status section, editor source map, and final-approval backlog before publication?** **Recommended: Yes.**
8. **Should the optional 12-question self-assessment include at least one item on the Bitcoin/stablecoin distinction or the responsible-learning/trading boundary?** **Recommended: Yes, replacing rather than adding an item.**
9. **Should `17_spec.md` remain the stakeholder overview while a separate compact publication/QA checklist is created?** **Recommended: Yes.**
10. **Should public certificate-verification language remain conditional until issuer, privacy, correction, revocation, and verification rules are approved?** **Recommended: Yes.**
11. **Should `workspace/18_advanced.md` remain the Advanced authority instead of moving it to the currently non-existent `advanced/` directory?** **Recommended: Yes, unless a real Advanced publication package is being created now.**
12. **After this review is accepted, should one canonical report live in `review/` and the duplicate report location be retired?** **Recommended: Yes.** This report is in `workspace/00_report.md` because the author explicitly requested that location.

## Final assessment

The Diploma's educational direction is now credible and mostly consistent. The Student Guide contains the necessary beginner story, and the Educator Guide contains enough pedagogical substance to support strong delivery. The project should now resist adding breadth.

The decisive work is to make every certificate claim traceable and reproducible: one objective, one taught path, one opportunity to practise, one valid evidence route, one clear standard, and one safe reassessment process. Once that system is built, timed, and tested—and the repository migration and public-document cleanup are completed—the project will be much closer to a concise, trustworthy, and scalable Bitcoin Diploma.
