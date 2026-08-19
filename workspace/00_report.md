# Bitcoin Diploma 2026.10 workspace consistency and publication-readiness report

> 2026.10 release supersession: this historical report includes an earlier app-assessment model. That model is post-October only; the current release treats the app as an optional recap, self-check, discovery, and update resource.

| Audit control | Detail |
| --- | --- |
| Date | Original audit: 11 August 2026; policy harmonization update: 13 August 2026 |
| Scope | Original audit: all 22 then-existing Markdown documents in `workspace/`. Follow-up: the new `12_educator-draft.md` and all policy-affected documents. |
| Primary standard | The document roles and consistency rules defined in `00_index.md` |
| Priority outputs | `08_student.md` and `12_educator-draft.md`; `12_educator-plan.md` is the supporting outline |
| Change boundary | The original audit edited only this report. The assessment-policy updates changed affected workspace documents to implement the four-contribution model. |
| External validation | Deliberately not performed in this phase |

## Method and limitations

The audit read the complete 84,576-word pre-existing workspace corpus and assessed each document against its index-assigned role, its own stated purpose, and its dependencies elsewhere in the package. The review cross-checked architecture, required objectives, content depth, learner promises, activities, app/offline delivery, assessment, certification, terminology, visual requirements, sources, internal paths, publication status, and Advanced boundaries.

The review also used reproducible repository checks to count objective-ID propagation, proposed visuals, Student Guide URLs, broken legacy-path patterns, unfinished-status markers, and structural Markdown issues. Quantitative findings are reported only where they help explain a governance or publication risk.

This is an internal consistency, curriculum-architecture, and publication-readiness audit. It is not an external technical or historical fact-check, a legal review, an accessibility conformance test, an app test, a rendered-layout review, or a teaching pilot. Those are later release gates. References such as `08_student.md:485` identify the audited source line at the time of this report; future editing will move line numbers, which is itself one reason the report recommends stable IDs.

## Policy resolution update — 13 August 2026

The project has resolved the major app/offline assessment contradiction. Teaching may be facilitated in person (preferred) or online with low-tech, offline-capable print/PDF content. Diploma completion nevertheless requires the approved My First Bitcoin app. The theoretical 50% is split 80% app evaluation and 20% educator-evaluated objective-aligned interaction; the practical 50% is split 80% direct observation by an educator and 20% app follow-up linked to the practical task. Both components and their required contributions must be passed; none may compensate for another.

Affected workspace documents have been harmonized to this policy. During the follow-up, `12_educator-draft.md` was added as the educator-facing publication target and `12_educator-plan.md` was retained as its subordinate structural plan. The draft now contains all four module companions plus a working assessment and recording section. It remains dependent on missing approved app items, tasks, rubrics, thresholds, and governance and needs traceability, concision, usability, and release review. The unresolved work is now operational: app capability and access, objective-valid item design, scoring and retries, practical tasks and rubrics, result integration, accessibility and language parity, privacy and governance, outage handling, and the meaning of the approximately eight-hour commitment.

## Executive conclusion

The project has a coherent educational concept but is not yet ready to publish as a reliable Bitcoin Diploma.

The strongest shared foundations are the four-module journey, beginner focus, Core/Custom/Advanced separation, practical learning, learner safety, non-endorsement, local adaptation, offline intent, and direct observation of practical competence. Those principles appear often enough across the package to show genuine alignment rather than coincidence.

The weakness is implementation control. The documents repeat the same direction in several places, but do not yet form a dependable chain from decision to learner experience to evidence to certificate. Important decisions appear as fixed commitments in one document, working assumptions in another, and open questions in a third. Required objectives disappear downstream. Support documents that are labelled as structures or frameworks are relied upon as though they contain finished activities, questions, rubrics, records, and publication rules. Numerous paths, line references, and section anchors are stale.

The two intended publications require different levels of work:

- `08_student.md` is a substantial late draft with many strong passages. It needs structural reduction, objective repair, role-boundary correction, a modular Module 4, and publication editing. It should be refined rather than restarted.
- `12_educator-draft.md` is now a substantial educator-facing draft with general facilitation, accessibility, safety, pacing, all four module companions, and working assessment/recording guidance. It now substantially exceeds the Student Guide in length and needs a disciplined role and concision edit as well as completion of its referenced operational dependencies. `12_educator-plan.md` remains the supporting outline rather than a publication.

The single most useful harmonization is an end-to-end objective crosswalk. Every required theoretical objective must connect to its learner teaching point, formative practice, valid app item, scoring rule, and recorded app result. Every required practical objective must connect to its teaching point, supported practice, observed task, rubric, and educator record. Until that exists, the package cannot prove that it teaches and assesses what it promises.

### Direct answers to the audit questions

| Question | Finding |
| --- | --- |
| Do the documents respect their roles? | Partly. `01_review.md`, `05_objectives.md`, `06_plan.md`, and `18_advanced.md` are the strongest role performers. `12_educator-draft.md` now performs the publication-draft role across all four modules, while `12_educator-plan.md` appropriately remains its outline; the pair still overlap and the draft needs reduction. `10_activities.md` and `14_microlearning.md` respect their structure roles but are not finished deliverables. `08_student.md` still absorbs educator and activity material. `17_spec.md` still fails its index-assigned publication-specification role. |
| Are they overlapping so much that they are repetitive? | Yes, in several high-value areas. Architecture is restated across `00`, `03`, `04`, `06`, `17`, and `README`; assessment ratios across `05`, `10`, `12`, `13`, `15`, `17`, and `README`; detailed activities and facilitation leak into `08`; and Organizations/Advanced mapping is duplicated across `18` and both `advanced/` files. Repetition is not uniformly excessive, but it is excessive where one exact rule needs one owner. |
| Do they carry out the roles assigned in `00_index.md`? | The planning documents mostly do at a conceptual level. The publishing and delivery chain does not. The Student Guide, Activity Bank, Educator Guide, assessment system, app bank, certification workflow, lexicon, source register, visual handoff, and publication specification are not collectively operational. Some files accurately label themselves as unfinished; the package around them nevertheless makes publication and certification promises that depend on their completion. |

## Overall readiness dashboard

The labels below assess internal consistency and operational readiness, not the external truth of Bitcoin, economic, historical, legal, or organizational claims.

| Area | Status | Assessment |
| --- | --- | --- |
| Educational direction | Strong foundation | The four-module progression, beginner orientation, safety, autonomy, and local adaptation are consistently understood. |
| Document governance | At risk | The follow-up repaired the index's obsolete paths and educator-guide status, but precedence and a controlled document-status system are still not explicit, and several decisions are repeated across files. |
| Learning objectives | At risk | The objective framework is thoughtful, but several objectives are bundled, unresolved, missing downstream, or too ambitious for an unvalidated eight-hour route. |
| Student Guide | Major revision | Strong learner prose and safety content, but excessive scope, role leakage, objective gaps, TOC drift, duplicated Module 4 material, and release defects remain. |
| Educator Guide | Substantial draft; major validation needed | The publication draft now covers general practice, all four modules, and working assessment/recording guidance. It is longer than the Student Guide, overlaps its plan and Activity Bank, and depends on unbuilt approved items, tasks, rubrics, and governance. |
| Activity Bank | Build required | Strong template and legacy inventory, but almost no ready-to-run current activities or approved summative tasks. |
| Microlearning/app evidence | Build required | A topic and item-design blueprint, not a populated question bank or usable theoretical assessment component. |
| Assessment and certification | Critical dependency | Policy now uses four required contributions—app theory, educator theory, educator-observed practice, and app practical follow-up—but no complete blueprint, item bank, task set, rubrics, thresholds, calibration, records, or governance exists. |
| Accessibility and supported access | Policy resolved; implementation at risk | Low-tech/offline-capable instruction is distinct from mandatory app-based completion. The device/account/accessibility/connectivity/support model is not yet operational. |
| Publication system | Critical gap | `17_spec.md` is not a publication specification. Asset, source, link, rights, accessibility, export, and release controls have no effective owner. |
| Source and reference integrity | At risk | Many internal paths, visual anchors, lexicon lines, and source locators are stale or broken. External claims remain to be validated later. |
| Advanced boundary | Mostly effective | Advanced material is generally kept out of Core, but the holding system is overgrown, duplicated, and supported by broken source trails. |

## What should be preserved

The next phase should be a controlled consolidation, not a wholesale redesign. These strengths are worth protecting:

- The four-module narrative is simple and memorable: Understanding Money; How Bitcoin Works; Using Bitcoin Safely; Bitcoin in Your Community.
- The course is transparent about being beginner, Bitcoin-only, educational, open-source, community-led, and not financial, investment, legal, or tax advice.
- Learner autonomy is treated seriously. The Student Guide repeatedly allows uncertainty, warns against meaningful-fund experimentation, and avoids making purchase or installation a universal requirement.
- The Student Guide handles trade-offs well in several areas, including fiat banking, decentralization, sound money, custody, and circular economies.
- Self-custody safety content is generally cautious, practical, and explicit about responsibility and limitations.
- The Educator Guide's assessment philosophy is strong: match evidence to the objective verb, observe practical performance, assess evidence rather than confidence, permit “Not yet” and reassessment, and calibrate educator.
- The Activity Bank template has useful metadata, safety, adaptation, evidence, and facilitation fields. It is a sound base for actual activity production.
- `18_advanced.md` makes the correct strategic move: useful material can be parked without forcing it into the beginner Diploma.
- The research file is honest that major evidence and validation work remain. That honesty should be converted into a controlled evidence register rather than removed.

## Critical cross-project findings

### 1. The source-of-truth system is conceptually useful but operationally unreliable

`00_index.md` is the right place to govern roles. The 13 August follow-up repaired its known path and educator-guide mapping errors, but the wider package still lacks explicit precedence, approval status, and change control.

Examples found in the original audit include:

- The index pointed to `mergefromorganizations.md` and `advancedorganizations.md` at the workspace root while the files were in `workspace/advanced/`; the 13 August follow-up repaired these paths.
- The index referred to a nonexistent `y_archive/` and superseded-plan path; the follow-up removed those assertions.
- `02_research.md` cites missing legacy specifications, an obsolete survey filename, and old Organizations paths (`02_research.md:119-121`, `145`, `161`).
- `06_plan.md` cites a missing legacy contents CSV and old Organizations paths (`06_plan.md:174`, `207`, `399-400`).
- `09_assets.md:33` points to a nonexistent `feedback/` directory; the available transcription is under `input/PABLO/`.
- `18_advanced.md` contains 84 references to nonexistent `../ref/chapters/...` paths and 15 references to obsolete aggregate legacy files. Current legacy sources live under `ref/bitcoin-diploma/en/`.
- Before the 13 August follow-up, `README.md` had a more accurate map of the `advanced/` files than the governing index. The paths are now synchronized; the broader risk of duplicated live governance prose remains.

The index also does not define precedence when authorities disagree. For example, should an objective missing from the plan be removed, or should the plan be repaired? The answer should be explicit: `05_objectives.md` governs required achievement until a formal decision changes it; `06_plan.md` governs architecture and depth; `13_assessment.md` governs evidence; downstream omissions do not silently override an upstream authority.

**Harmonization:** make `00_index.md` a concise authority, precedence, status, and navigation register. Give each active document one owned function. Add a small status vocabulary—Proposed, Working, Approved, Deferred, Superseded—and require it in every document. Let `README.md` point to the index instead of repeating live curriculum rules.

### 2. Required objectives do not have end-to-end traceability

`05_objectives.md` defines 27 stable objective IDs and correctly says evidence must match the measurable verb. Following the assessment-policy update, 25 module-specific IDs are certification requirements, while `ALL.1` and `ALL.2` are formative unless a later approved blueprint assigns them valid summative evidence. The original repository check found no explicit downstream ID reference for 18 of the 27 IDs. The new `12_educator-draft.md` now names all module IDs, but a fresh end-to-end crosswalk remains necessary because an ID appearing in one guide does not prove that valid teaching, app evidence, practical evidence, and recording all exist:

- `B1.2`-`B1.6`;
- `B2.1`, `B2.4`-`B2.6`;
- `B3.1`-`B3.3`, `B3.5`, `B3.8`-`B3.11`;
- `ALL.2`.

Absence of an ID does not always mean absence of the topic. Much of the relevant content exists in prose. It does mean the package cannot audit whether the exact outcome, support condition, measurable verb, practice, and evidence survived drafting.

The most consequential content gaps or reductions are:

| Objective | Drift | Required decision |
| --- | --- | --- |
| `B2.5` | The new Educator Guide draft now teaches the required comparison of Bitcoin with stablecoins and other non-Bitcoin crypto-assets, but the Module 2 plan, contents, substantive Student lesson, and app bank still do not complete the same objective. | Implement the objective end to end or formally remove/defer it. Do not leave it nominally required. Use neutral, translation-ready terminology in the formal objective. |
| `B2.6` | The new Educator Guide draft now covers responsible learning versus speculation. The Student Guide states that the course is not trading, token promotion, or speculation, but does not yet teach the required distinction and beginner risks as a complete objective; the app evidence is also undeveloped. | Add a short, criteria-based learner lesson and valid app evidence, or revise the objective authority. |
| `B3.11` | The new Educator Guide draft defines a supported first-access route, but the wider learner, activity, app, task, rubric, and recording chain remains incomplete. The objective also overlaps `B3.5` and `B3.6`. | Define and approve the distinct evidence or consolidate the objectives. Explicitly permit prepared funds or simulation. |
| `B4.1` and `B4.2` | The objective authority requires demonstration and explanation, while the Student overview and `17_spec.md` reduce the promise to seeing or identifying local uses. | Restore the exact measurable verbs and define equivalent criteria for every approved Custom variant. |
| `ALL.2` | Reflection appears at the beginning and end of the Student Guide, but an app-valid summative design has not been defined. | It is now formative and not a certification gate. Any future summative use must score course-concept reasoning—not enthusiasm for Bitcoin—and must follow the approved evaluator split. |
| `B1.6` | A local purchasing-power inquiry exists, but `13_assessment.md:151` makes local inquiry conditional “where appropriate,” weakening a required outcome. | Supply a non-disclosing realistic scenario as the universal fallback. |
| `B1.5` | CBDCs are part of the required objective and now appear in learner, educator, and app-planning material, while `17_spec.md` weakens them with “where appropriate.” | Decide once whether the concept is required, illustrative, or Advanced, then synchronize the specification wording. |

The objectives themselves also need a feasibility pass. Several bundle multiple constructs, notably `B1.5`, `B2.3`, and `B3.11`; `B3.11` overlaps other practical objectives; `ALL.1` could reward a preferred participation style; and `ALL.2` could reward a preferred personal stance. Classifying the latter two as formative removes that immediate certification risk, but 25 required certification IDs may still be too many for the intended duration. Make the objective set atomic, keep every item explicitly required/formative/optional, and test the complete load.

**Harmonization:** retain the objective catalog in `05_objectives.md`, and make `13_assessment.md` own one master implementation crosswalk:

`Objective ID → required status → plan boundary → Student section → formative practice → app item and scoring rule OR practical task and rubric → result field → estimated time → release status`.

Every required row must be complete before publication. Other documents should use the ID, not paraphrase a weaker outcome.

### 3. The assessment policy is now coherent, but the operational system is incomplete

The governing model now uses four required contributions across two 50% components: app theory (40% overall), educator theory (10%), educator-observed practice (40%), and app practical-task follow-up (10%). Both components and each required contribution must be passed; none may compensate for another. Ordinary educator-led theory activities remain formative.

The allocation is now fixed at 50% theory and 50% practice, internally divided 40/10/40/10. The current competency model should still be implemented as two separate pass gates, with every required contribution passed. If numerical scores will also be reported, `13_assessment.md` must define their denominator, thresholds, objective-level rules, and relationship to those gates without allowing averaging to conceal an unmet requirement.

The implementation gap is larger than the wording problem:

- `10_activities.md` contains a legacy inventory, a strong template, one partial formative discussion, categories marked Work in Progress, and activity seeds. It does not contain approved summative task sheets and rubrics for the required practical outcomes.
- `14_microlearning.md` contains item-writing rules and topic opportunities, not a bank of reviewed prompts, answers, distractors, feedback, objective links, scoring, or status.
- `13_assessment.md` explicitly leaves the final blueprint, thresholds, tasks, rubrics, calibration, records, retakes, appeals, and related rules unresolved.
- `15_certification.md` leaves issuer authority, educator approval, privacy, retention, appeals, correction, revocation, and verification unresolved.
- `12_educator-plan.md` tells educators to use approved tasks that do not yet exist.
- The Student Guide nevertheless describes certificate completion and possible verification fields at `08_student.md:1513-1528`.

Direct observation also creates a capacity problem that no document solves. The system needs learner-to-educator ratios, minutes per learner, rules for group observation, privacy arrangements, remote-observation boundaries, follow-up assessment, and reassessment outside the main session.

**Harmonization:** keep `13_assessment.md` as the sole normative owner of the fixed 50/50, 40/10/40/10 two-gate model and define its scoring and reporting rules there. Other files should carry only short, conforming summaries. Build the minimum approved practical task set, rubrics, safety-critical errors, objective-complete app item bank, educator calibration materials, combined evidence record, and reassessment route before promising operational certification.

### 4. The app/offline policy contradiction is resolved; access implementation is now critical

The governing distinction is now explicit across the workspace:

- content may be facilitated in person (preferred) or online;
- print/PDF teaching and practice should remain low-tech and offline-capable;
- a learner-owned device or continuous connection is not required at every teaching step;
- supported access to the approved My First Bitcoin app is required for theory assessment, practical-task follow-up, and Diploma completion;
- theory is app/educator 80/20, while practice is direct observation/app follow-up 80/20; and
- paper quizzes may prepare and remediate; approved educator-led theory interactions contribute their assigned 20% but cannot replace either required app result.

This resolves the policy contradiction by narrowing the offline promise to content delivery and preparation rather than device-free certification. It also turns app readiness and equitable supported access into release dependencies.

**Remaining decisions that require product, governance, or operational work:**

1. Define whether learners need their own device/account or may use shared, loaned, or assisted access.
2. Confirm supported devices, operating systems, browsers, bandwidth, charging, and account-recovery requirements.
3. Specify weak-connectivity and true offline app behavior, synchronization, interrupted attempts, outages, and an authorized contingency path.
4. Validate app item formats for theoretical verbs such as **explain**, **compare**, **apply**, and **reason**; redesign or reclassify objectives the app cannot assess reliably.
5. Set pass thresholds, objective-level rules, retries, randomization, feedback timing, item versioning, identity, integrity, and audit requirements.
6. Provide accessibility and language parity for every required app assessment, including minors' consent and assisted-use rules where relevant.
7. Define how app theory, educator theory, educator practical, and app practical-follow-up results combine, who may enter or correct each result, how mismatches are reconciled, and what unlocks a certificate.
8. Decide whether app setup, microlearning, evaluation, synchronization, feedback, and retries count inside the approximately eight-hour pathway.
9. Decide whether Module 4 uses common theoretical app items or moderated local packs; local packs create translation, availability, and equivalence obligations.
10. Bring required app configuration, content integration, access testing, and release acceptance into scope even though building or replacing the platform remains out of scope.

**Harmonization:** publish one access standard and one contingency policy. Never describe the complete credential path as offline or device-free. Say instead that teaching content is offline-capable and that supported app access is a minimum certification requirement.

### 5. The eight-hour route is an unvalidated planning hypothesis

The “approximately eight-hour minimum planning baseline” is internally consistent as an intention, but no complete time model demonstrates it. Timing validation remains an unfinished scope item at `03_scope.md:300-312`.

`08_student.md` now contains approximately 19,400 words. At roughly 200 words per minute, silent reading alone is about 97 minutes. Word count does not prove that eight hours is impossible. The risk comes from combining that reading or explanation load with 25 certification objectives, two formative cross-module outcomes, four modules, required app learning and evaluation, discussion, activities, practical instruction, individual observation, feedback, breaks, and possible reassessment. Pre-reading cannot be assumed.

`12_educator-plan.md` gives a 9:00-5:00 schedule with breaks as an example, while immediately acknowledging that this supplies less than eight teaching hours. This is a useful warning embedded in what otherwise looks like a schedule recommendation.

**Harmonization:** create a timed delivery script that identifies, for every module:

- required learner prose or educator explanation;
- optional enrichment;
- required app learning and evaluation;
- discussion and practice;
- assessment and direct-observation time;
- transitions and breaks;
- feedback and reassessment outside or inside the baseline;
- cohort size and educator ratio assumptions.

Pilot in-person teaching (preferred) and online teaching with low-tech materials and realistic supported-app access, group sizes, and educator capacity. Until then, call eight hours a design target, not a validated completion promise.

### 6. `17_spec.md` does not perform its assigned role

`00_index.md:64` makes `17_spec.md` the source of truth for publication requirements. `17_spec.md:1-9` explicitly identifies itself as a short standalone overview for staff, educators, partners, funders, and collaborators. It mostly repeats the four-module plan, audience, scope, delivery direction, assessment ratios, and redesign rationale.

It does not specify:

- canonical artifact names, edition syntax, filenames, or output structure;
- manuscript, asset, translation, and release freeze rules;
- page size, page budget, typography, headings, tables, callouts, or worksheets;
- print constraints, contrast, accessibility, tagged PDF, or alt-text acceptance;
- licensing, attribution, credits, image rights, and asset provenance;
- source-note, citation, outbound-link, or QR policies;
- translation package structure and change control;
- PDF/export profiles and preflight checks;
- review roles, approvals, release sign-off, and maintenance.

This is a complete role failure, not a minor gap. It leaves the two priority publications without a production authority.

**Harmonization:** either rewrite `17_spec.md` as the actual publication and release specification, or reclassify it as an overview and create a real specification. Rewriting the existing numbered role is the leaner option. Move the overview content to a public brief or keep only a short non-normative summary in `README.md`.

## Priority audit: `08_student.md`

### Role verdict

The file succeeds as learner-facing prose but does not yet succeed as a concise, fully aligned, publication-ready Student Guide. It also violates the ownership rules that put detailed activities in `10_activities.md` and detailed facilitation in `12_educator-draft.md`.

It is best understood as a strong late manuscript requiring a structural edit, not as the “draft scaffold” still described at `00_index.md:30` and `06_plan.md:391`.

### Strengths

- The opening explains purpose, beginner audience, openness, independence, and learner autonomy clearly.
- The four-module path is easy to understand.
- Practical safety is emphasized without requiring purchase, installation, or meaningful personal funds.
- Explanations of fiat systems, decentralization, sound money, custody, and payment trade-offs are often balanced and translation-friendly.
- Tables support comparison and reduce prose in several difficult sections.
- Self-custody coverage is cautious and action-oriented.
- The guide allows simulation and uncertainty rather than requiring ideological agreement.
- Module 4 starts from local need and constraints instead of treating a product or provider as the answer.

### Main structural problems

#### Module 4 is fixed in the manuscript even though it is supposed to be selected locally

The Student Guide says the educator chooses local modules (`08_student.md:1050-1052`) but then gives every learner more than 3,100 words covering most possible Custom pathways. This makes Custom function like a compulsory global chapter.

It also repeats Core material:

- wallet and tool evaluation at `08_student.md:711-721` and `1127-1159`;
- on-chain/Lightning comparison at `1015-1038` and Lightning practice at `1161-1189`;
- acquisition pathways at `983-1013` and local ramps/KYC at `1273-1322`;
- receiving, sending, verification, and safety at `857-981` and again in workshops and scenarios at `1093-1271`.

The main guide should contain a short common Module 4 introduction, a local decision and safety lens, a record of the selected task, the shared review, and the required outcome. Approved modular learner inserts should contain only the selected pathway. Facilitation and assessment remain in the Educator Guide and Activity Bank.

#### Educator and Activity Bank content remains inside the learner text

Clear role leakage includes:

- module-design criteria (`08_student.md:1066-1076`);
- Presentation-Practice-Production facilitation design (`1093-1102`);
- a workshop menu and educator preflight (`1103-1123`);
- a guided Lightning procedure (`1180-1189`);
- five detailed scenario sets (`1217-1271`);
- multi-field pathway, KYC, community, merchant, and resource worksheets (`1289-1401`).

Short learner reflections, practice prompts, and “check your understanding” callouts can remain. Facilitator setup, scenario variants, debrief, observation criteria, and full worksheets should be stored once in their owner file, with a learner-facing extract only where necessary.

#### The guide promises weaker outcomes than the objective authority

The introductory Module 1 and 2 outcomes use “understand” (`08_student.md:220`, `433`). The overview says Module 3 learners will “explain” and Module 4 learners will “identify” (`211-212`). `05_objectives.md` and `06_plan.md` require application and demonstrations.

Learners should see the exact evidence expectation from the beginning. Replace vague verbs with the approved measurable verbs, and use identical wording in the contents, guide introductions, reviews, assessment, and educator run sheets.

#### TOC and depth have drifted

Examples include:

- `07_contents.md` now promises educator-observed Module 3 and Module 4 competency checks; no corresponding learner-facing checkpoints appear explicitly.
- “Don't trust, verify” is planned as a Module 2 bridge (`07_contents.md:49`; `06_plan.md:101`) but is mainly developed in Module 3.
- Coin debasement is a planned topic (`07_contents.md:33`) but receives only a brief sentence.
- The U.S. reserve-currency section at `08_student.md:378-382` is not in the planned contents and approaches detailed monetary/geopolitical history parked in Advanced.
- Back matter expands beyond `07_contents.md:94-101` into contribution, network, case-study, leaderboard, support, and verification sections.

This does not mean every extra section is wrong. The project needs a deliberate content decision and synchronization, rather than allowing `07` and `08` to evolve as parallel TOCs.

### Concision and timing

The main opportunity is structural subtraction, not sentence-by-sentence compression. Removing repeated Module 4 teaching, moving full activities and facilitation, consolidating app and back-matter promotion, and distinguishing required from optional prose will produce larger gains than line editing.

A lean Student Guide should contain:

1. a short orientation explaining low-tech content delivery, supported app access, and the two assessment gates;
2. three shared Core modules, each with exact outcomes, essential explanation, small formative checks, safety, and review;
3. a short common Custom introduction;
4. one selected learner insert rather than every possible local module;
5. explicit learner-facing competency checkpoints;
6. one compact glossary/resources/certificate back-matter route.

The manuscript should not be assigned a final word or page limit until the timed pathway and publication layout are tested. It should, however, tag every section as Required, Optional enrichment, Selected Custom, or Reference.

### Editorial and publication defects

These are individually easy to fix but collectively show that the file has not had a release pass:

- `08_student.md:5` uses “Edition 26.10” rather than the project name `2026.10`.
- A raw URL is attached directly to prose at `08_student.md:23`.
- `08_student.md:485` says “the valid  of transactions,” with a missing word.
- The chronology at `08_student.md:669` returns to an October 2008 event after a timeline reaching 2010 and repeats earlier origin material.
- Placeholder headings remain at `08_student.md:1483` and `1503`.
- Student Guide, Student Book, Diploma, and scaffold are used inconsistently across the package.
- Canonical module-title capitalization varies: “Self-Custody” and “Bitcoin As Money” conflict with `00_index.md`.
- British and American English are mixed.
- `08_student.md:146` says terms are introduced before deeper use, but sats, Lightning wallet, fiat, wallet, and seed-related language appear before their formal introductions.
- The app is introduced more than once, and the guide contains 14 explicit web URLs. Back matter repeats contributions, network, case studies, leaderboard, support, sources, and certificate links, weakening the sparse-link/QR policy.

### Impartiality

The Student Guide says learners need not reach a predetermined conclusion. Its acknowledgement of Bitcoin's costs and trade-offs supports that promise. The fixed Problem → Solution framing can nevertheless feel conclusion-led if comparison and uncertainty outcomes remain missing.

Implementing `B2.5` and `B2.6` and using `ALL.2` formatively would make impartiality observable: compare systems with the same criteria, distinguish education from speculation, and let learners state a reason to continue or remain uncertain. The Educator Guide should include neutral follow-up prompts that do not require praise of Bitcoin.

## Priority audit: Educator Guide draft and plan

### Role verdict

The educator material now has a useful two-document contract. `12_educator-draft.md` is the publication target, and `12_educator-plan.md` is its supporting outline. The index and README have been updated to make that relationship explicit.

The draft improves materially on the original outline. It provides general facilitation methods, accessibility guidance, pacing, practical-safety procedures, local-verification preparation, misconceptions, all four module companions, and working assessment/recording guidance. It now follows the four-contribution model: app theory, educator theory, educator-observed practice, and app practical follow-up. It is not yet publication-ready because its referenced evidence system and governance are unbuilt and its length now exceeds the Student Guide, creating a clear role-boundary and concision problem.

### What is missing for publication

- Validate and refine all four module companions against the final objective crosswalk and timed delivery route.
- Finalize the practical-assessment administration, recording, feedback, reassessment, moderation, and appeal workflow.
- Insert approved task and rubric IDs once the Activity Bank and assessment system are built.
- Add annotated **Meets standard**, **Not yet**, unsafe, and over-prompted practical evidence examples.
- Separate publishable educator guidance from internal migration and production instructions still held in the plan.
- Validate every time recommendation against the complete app, practice, direct-observation, recording, and reassessment workload.
- Finish the source, accessibility, localization, supported-app-access, outage, privacy, and incident procedures required for release.

### Recommended operational structure

Every module run sheet should use the same compact template:

| Field | Required content |
| --- | --- |
| Outcomes | Exact objective IDs and learner-facing verbs |
| Prerequisites | Required Student sections and prior evidence |
| Time | Minimum/typical range, including observation assumptions |
| Preparation | Materials, prepared wallets/funds, app or offline package, accessibility needs |
| Run of show | Timed sequence of explanation, questions, practice, checks, assessment, transition |
| Activities | Stable Activity Bank IDs and the reason each is selected |
| Facilitation | Suggested prompts, likely responses, neutral follow-ups, misconceptions, boundaries |
| Safety | Stop conditions, prohibited handling, test-fund limits, incident response |
| Adaptation | Translation, low-literacy, visual/motor, shared-device, oral, and low-connectivity instructional/practical variants |
| Assessment | Task and rubric IDs, observable criteria, critical errors, evidence record, reassessment |
| Close | Review, learner next step, and handoff to the next module |

This repeated template will make the guide easier to scan, translate, pilot, and update than long policy prose.

### Safety operations

The guide correctly says that practical skill must be observed and that real secrets should not be exposed. It still needs a practical-session protocol covering:

- educator access to learner devices, accounts, funds, and secrets;
- ownership and reset of prepared wallets;
- maximum test-fund exposure and responsibility for loss;
- classroom privacy, cameras, screen sharing, and remote observation;
- accidental recovery-phrase exposure;
- tool download and update verification;
- incident and scam escalation;
- local expert and provider boundaries;
- minors or vulnerable learners where relevant;
- no individualized financial, tax, legal, accounting, or compliance advice.

Some preflight guidance currently appears in the Student Guide. Move it to this protocol and provide only the learner's own safety rules in `08_student.md`.

### Accessibility and equivalence

The guide makes a good promise: accommodations may change the method but not the objective. It does not show educators how to do that. Every approved task should include at least one equivalent variant for relevant constraints, including low literacy, visual access, motor access, oral evidence, shared devices, translated discussion, low connectivity, and offline observation. The invariant evidence must be stated clearly.

### Educator capacity and quality assurance

The final guide needs educator-ratio assumptions, practice scoring, annotated passing and Not-yet examples, prompting boundaries, moderation, calibration frequency, and a process for recording questions that expose curriculum ambiguity. Without those, two educators may issue the same certificate for materially different evidence.

## Repetition and ownership audit

Not all repetition is bad. Learners, educators, educator, and collaborators each need a short contextual statement. Harmful repetition occurs when several documents redefine the same rule, preserve different status, or require synchronized manual editing.

| Subject | Normative owner | Current duplication/problem | Harmonized rule |
| --- | --- | --- | --- |
| Roles, precedence, and document status | `00_index.md` | `README.md` and several purpose sections partly remap the package; index paths are older than README paths. | Index owns the map. README is a short landing page and link. |
| Diagnosis | `01_review.md` | Exact assessment solution and public messaging leak beyond diagnosis. | Keep findings and implications; link to current solution owner. |
| Evidence and confidence | `02_research.md` | Research plan, Scholar query bank, AI prompt library, tool list, raw notes, and approved-looking decisions are mixed. | Maintain a decision/evidence/counterevidence/confidence/status register; move reusable search and prompt material to appendices. |
| Project delivery | `03_scope.md` | Sixteen overlapping workstreams, no owner/status/dependency, and conflicts between app/web scope and promised outputs. | Use a deliverable register with owner, dependency, status, acceptance evidence, and gate. |
| Design principles | `04_design.md` | Repeats architecture, assessment mechanics, translation workflow, and resolved/open questions. | Keep rationale, principles, adaptation boundaries, and risks; link to implementation owners. |
| Objectives | `05_objectives.md` | Includes evidence methods and assessment ratios; downstream paraphrases weaken verbs. | Own IDs, required status, exact wording, and competency standard only. |
| Architecture and content depth | `06_plan.md` | Repeats detailed TOC, publication rules, and assessment mechanics; commitments and open decisions conflict. | Keep module boundaries, required/optional/Advanced depth, ownership, and migration decisions. |
| Learner content blueprint | `07_contents.md` | Manually maintained parallel TOC without IDs, status, or authority; drift from Student. | Make it an authoritative blueprint with objective IDs/depth/status, or generate it from `08`. Do not leave it ambiguous. |
| Learner prose | `08_student.md` | Holds facilitator setup, scenarios, worksheets, and every Custom option. | Keep explanations, learner safety, brief checks, selected learner material, and reviews. |
| Visual requirements | `09_assets.md` | 74 visual entries, including 22 table assets and duplicated concept/table treatments; stale anchors; no production status/rights. | Triage to a minimum viable visual set, anchor by stable IDs, and let `17` own layout. |
| Activity procedures | `10_activities.md` | Repeats assessment policy and has not yet replaced the activities still in Student. | Own complete activity/task records, learner extracts, safety, evidence, and variants; link to `13` for policy. |
| Claim evidence | `11_resources.md` | Five sources cannot cover the current manuscript; line locators are stale. | Use stable claim IDs and a full internal claim register; keep learner links separately approved. |
| Facilitation | `12_educator-draft.md` | Substantial guidance for all four modules and assessment now exists, but it overlaps planning/activity material and depends on unbuilt artifacts. | Own concise operational run sheets, questions, misconceptions, safety, adaptation, activity selection, and practical-assessment procedures. Keep `12_educator-plan.md` subordinate. |
| Assessment | `13_assessment.md` | Policy repeated throughout package; implementation incomplete. | Be the sole normative owner of blueprint, evidence, thresholds, rubrics, reassessment, records, and equivalence. |
| App items | `14_microlearning.md` | Title says Question Bank, content is a topic outline. | Populate actual reviewed item records or label it a blueprint until populated. |
| Credential issuance | `15_certification.md` | Repeats assessment allocation; governance unresolved. | Own what the certificate represents, eligibility pointer, issuer workflow, privacy, appeals, replacement/revocation, and verification. |
| Controlled terminology | `16_lexicon.md` | Functions as a stale line-reference feedback inventory, not a controlled vocabulary. | Own preferred terms, definitions, capitalization, scope, alternatives, translation notes, and stable anchors. |
| Publication and release | `17_spec.md` | Contains a stakeholder overview and repeats the plan. | Replace with actual manuscript, layout, accessibility, rights, citation, export, QA, and sign-off rules. |
| Advanced holding | `18_advanced.md` | Duplicates Organizations maps, contains broken sources, and partly prioritizes work it says to defer. | Keep one holding authority with candidate status and repaired source trails; defer module design. |

### Controlled repetition rule

When another audience needs context, use a two-to-four-sentence summary followed by a link to the normative owner. The summary may not introduce new thresholds, exceptions, vocabulary, or status. This preserves usability without creating parallel policy.

## Per-document role assessment

| Document | Role fidelity | Main value | Main drift or deficiency | Recommended disposition |
| --- | --- | --- | --- | --- |
| `00_index.md` | Mostly | Reading order, roles, consistency rules | Broken paths, stale status, competing detail, no precedence, misassigned `17` role/content | Retain as lean governance authority; repair map and add decision status/precedence. |
| `01_review.md` | Mostly strong | Balanced diagnosis of the legacy Diploma | Prescribes exact assessment solution and public response in places | Keep diagnosis; replace current solution detail with links. |
| `02_research.md` | Partial | Evidence-first intent, useful search discipline, cautions, and prompts | Hybrid of one-day schedule, 375-line Scholar query bank, tool directory, AI prompt bank, raw notes, and recommendations; evidence tables unfilled; broken sources | Convert to a decision-based research register; move reusable search queries, prompts, and raw notes to appendices. |
| `03_scope.md` | Partial | Comprehensive deliverables and completion concerns | Overlapping workstreams; no owner/date/status/dependency; app and web scope contradictions | Collapse into operational deliverable and gate register. |
| `04_design.md` | Mostly | Strong principles, guardrails, risks, adaptation logic | Repeats architecture and assessment rules; stale open questions; pending audience assumptions | Retain principle-level content; remove operational duplication and resolve statuses. |
| `05_objectives.md` | Strong framework | Stable IDs and verb/evidence discipline | Working gaps, bundled/overlapping outcomes, evidence and ratios outside role, downstream omissions | Freeze an atomic classified objective set, then enforce exact IDs. |
| `06_plan.md` | Strongest planning file | Four-module architecture, boundaries, ownership, migration | Too much detail; missing required objectives; stale paths; commitments also listed as open | Retain as architecture authority; label Approved/Working/Optional/Deferred explicitly. |
| `07_contents.md` | Partial | Concise learner-flow view | No purpose/status/IDs; parallel TOC drift; required topics and checks missing | Make controlled content blueprint or derive automatically from Student headings. |
| `08_student.md` | Partial, substantive | Strong explanations, transparency, safety, practical beginner tone | Too broad, role leakage, fixed-all-options Module 4, objective/TOC drift, duplication, editorial defects | Structural edit and modularization; preserve the strongest prose. |
| `09_assets.md` | Partial | Detailed visual briefs and thoughtful safety constraints | Stale anchors, excessive 74-asset scope, table/layout creep, broken provenance, no rights/status | Rebuild after manuscript freeze around a minimum visual set and stable anchors. |
| `10_activities.md` | Partial by design | Strong activity template and legacy inventory | Not yet a current Activity Bank; almost no approved tasks; repeats assessment policy | Populate only the minimum required activities/tasks first, then optional bank. |
| `11_resources.md` | Weak | Correct idea of an internal source register | Only five entries, stale lines, incomplete claim coverage | Expand to claim-ID register after internal wording freeze. |
| `12_educator-draft.md` | Substantial publication draft | Strong general facilitation, safety, accessibility, pacing, four module companions, and working assessment guidance | Overlong; overlaps plan/activity material; operational evidence artifacts and governance remain unapproved | Reduce around the repeated run-sheet pattern and integrate the approved evidence system. |
| `12_educator-plan.md` | Appropriate supporting-plan role | Structural checklist, assessment principles, and planned responsibilities | Overlaps the draft if treated as educator-facing authority; retains internal migration content | Keep subordinate to the draft, use for completeness checks, and do not publish as the guide. |
| `13_assessment.md` | Strong concept, partial delivery | Competency philosophy, direct observation, non-compensation | Blueprint, tasks, rubrics, thresholds, records, calibration, appeals unresolved | Make sole assessment authority and finish operational system before release. |
| `14_microlearning.md` | Fulfils structure role; not a bank | Good item template and writing rules | Topic opportunities only; no actual items, answers, feedback, mappings, scoring, or status | Populate reviewed items from the objective crosswalk or relabel internally as blueprint. |
| `15_certification.md` | Partial | Clear two-component eligibility principle | Repeats assessment; issuer, educator, privacy, appeal, revocation, and verification unresolved | Reduce to credential meaning and complete issuance/governance workflow. |
| `16_lexicon.md` | Weak as authority | Broad inventory of beginner and feedback terms | Stale line numbers and presence claims; imprecise peer-to-peer definition; Advanced terms mixed in | Convert to controlled vocabulary with stable anchors and scope/status fields. |
| `17_spec.md` | Fails assigned role | Useful stakeholder overview | No publication specification; duplicates plan and assessment | Rewrite as actual publication/release spec; relocate overview purpose. |
| `18_advanced.md` | Mostly | Protects beginner boundary and preserves future material | Overgrown, duplicated, broken source trail, title overlaps, premature priorities, advice-boundary conflict | Freeze and repair as sole Advanced holding authority; defer design until Core release. |
| `README.md` | Partial | Useful repository orientation and accurate `advanced/` paths | Repeats live architecture and assessment policy; not governed in index | Keep a short landing page that links to the index and current status. |
| `advanced/mergefromorganizations.md` | Largely completed migration role | Beginner-safe Organizations decision trail and activity seeds | Old paths; many decisions already implemented; still reads as active checklist | Mark decisions implemented/remaining, then close or retain as historical migration evidence. |
| `advanced/advancedorganizations.md` | Weak as separate authority | Organizations source trail for Advanced | Heavily duplicated by `18_advanced.md`; old paths; unclear continuing ownership | Reduce to source-specific delta or retire after its unique evidence is merged into `18`. |

## Detailed consistency and drift register

| Area | Conflicting expressions | Harmonized position |
| --- | --- | --- |
| Complete Diploma | Core is described as required and as Modules 1–3 (`06_plan.md:265`), while Module 4 objectives are also required for certification (`05_objectives.md:97-104`). | **Shared Core content:** Modules 1–3. **Fixed Diploma performance requirements:** include `B4.1`/`B4.2`. **Custom variant:** locally selected task. **Complete Diploma:** Core plus one approved Custom task. Custom selection is variable; completion is not optional. |
| App status | Policy resolved; access and capability are not yet operational. | The app is mandatory for 80% of theory and 20% task-linked practice follow-up. Low-tech/offline-capable describes teaching content, not a device-free credential. Publish supported-access and outage rules before release. |
| Assessment ratios | The approved allocation is 40% app theory, 10% educator theory, 40% observed practice, and 10% app practical follow-up. | Use two mandatory, non-compensatory pass gates and require each internal contribution. Define any reported numerical score separately and prevent averaging across failed requirements. |
| Duration | Approximately eight-hour minimum, one-day examples, and 9:00-5:00 with breaks are used interchangeably. | Define what counts inside eight hours and publish a pilot-tested range. Do not equate elapsed schedule, live teaching, and total learner effort. |
| Objective verbs | `05` requires explain/apply/demonstrate; `08` and `17` use understand/see/identify. | Exact objective verbs govern all learner promises and evidence. |
| CBDCs | Required in `B1.5`, conditional in `17`, omitted from required assessment evidence. | Decide required/illustrative/Advanced once; synchronize the crosswalk. |
| Problem/Solution impartiality | Learner autonomy is promised, but comparison and uncertainty objectives are missing operationally. | Apply consistent criteria across systems; teach speculation distinction; accept evidence-based uncertainty. |
| Module 4 scope | Educator-selected in policy; all modules preloaded in Student; variant difficulty differs. | Short shared section plus selected learner insert; common performance spine across all approved variants. |
| Product names | Student Guide, Student Book, Diploma, and scaffold compete; edition is `26.10` and `2026.10`. | Use **Bitcoin Diploma 2026.10 Student Guide** and **Bitcoin Diploma 2026.10 Educator Guide** unless a different formal naming decision is recorded. |
| Module names | Self-custody/Self-Custody and Bitcoin as Money/Bitcoin As Money vary. | Use the exact canonical forms in `00_index.md`; encode them in `16_lexicon.md` and `17_spec.md`. |
| Language variant | British and American forms are mixed. | Select one editorial variant, document exceptions, and enforce it in publication QA. |
| Markdown structure | Many files use multiple `#` headings or duplicate filename/title H1s despite the repository rule. | One `#` title per file; `##` top-level sections; sentence-case headings. |
| Stable references | `09`, `11`, and `16` depend on mutable line numbers; many are already wrong. | Use stable section, claim, objective, item, activity, and asset IDs. Generate line/page data only as temporary convenience. |
| Learner links | `11` suggests link restraint while `08` has 14 explicit URLs and repeated back-matter destinations. | `17` owns an approved destination/QR register with purpose, owner, last check, privacy, and print fallback. |
| Legal/tax boundary | Project prohibits advice; `18_advanced.md:226` says Advanced may develop tax/legal advice. | Advanced may provide reviewed educational context and referral guidance, never individualized or prescriptive advice. |
| Advanced timing | `18` says Advanced design waits, but also gives active-looking module priorities. | Label existing priority as historical/unapproved input or defer it; do not spend current capacity on Advanced design. |

## Support-system findings

### Visual assets

`09_assets.md` contains 74 proposed visual IDs: 34 Essential, 32 Supporting, and 8 Conditional. Twenty-two are table assets. This is a large production burden for a concise beginner guide and includes several cases where both a conceptual diagram and a redesigned table cover the same relationship.

The file says exact current headings should govern placement, yet several headings and many line references no longer match `08_student.md`. It also explicitly excludes production status, rights management, and publication logging, leaving those needs without an owner.

After the Student structure freezes:

- select a minimum viable visual set focused on misconception-prone relationships and safety-critical processes;
- treat ordinary table styling as layout, not a separate asset;
- anchor every visual to a stable manuscript ID;
- record owner, status, source, rights, accessibility, localization, and review;
- state whether a visual replaces prose/table content so the page and word budget reflects it;
- keep the handoff vendor-neutral rather than tied to one design system.

### Activity Bank

The template is fit for purpose, but the content is not yet the promised bank. Build the smallest certification-complete set first: enough formative practice and approved summative tasks to cover every required verb, especially direct demonstrations and Module 4 equivalence. Each task needs learner instructions, facilitator setup, time, safety, accessibility/offline variants, observable criteria, critical errors, rubric, evidence record, and reassessment.

Only after this minimum set works in pilots should the project expand the standalone community-event library.

### Source register

`11_resources.md` contains five entries for a Student Guide with extensive organizational, historical, economic, technical, safety, and current-link claims. Its first locators are already stale, and one listed named example is absent from the current manuscript.

The source register should use stable claim IDs, exact internal claim wording, source type, authority, publication treatment, volatility, reviewer, and date checked. Keep claim evidence separate from the small learner-facing link/QR register. Populate and validate it after internal claim wording freezes, so external review does not chase moving prose.

### Microlearning

`14_microlearning.md` is accurately a structure but inaccurately titled as a completed question bank. It lacks item IDs, prompts/options, answers, response criteria, feedback, objective mappings, difficulty, evidence classification, scoring, status, review, and locale/version data.

There is also content drift: its history-ordering idea implies a simple universal sequence that the Student Guide rejects; recognizability appears as a target property while the Student set omits it; Nixon Shock name/date recall exceeds current learner wording; and `B2.5`/`B2.6` have no item opportunity.

Populate it from the final objective and Student-section crosswalk rather than maintaining a parallel topic outline.

### Lexicon

`16_lexicon.md` is useful evidence of terms considered during feedback, but unreliable as terminology control. Current Student line numbers and “Not present” statuses are widely stale. It says Bitcoin Core appears when it does not; marks several concepts absent despite their presence; and defines peer-to-peer as direct computer communication while the Student Guide correctly warns that peer-to-peer does not mean only two computers communicate directly.

Replace fragile line mapping with a controlled vocabulary containing:

- term ID and preferred term;
- permitted synonyms and avoid/deprecated forms;
- beginner definition;
- scope: Core, Custom, educator-only, Advanced, or parked;
- capitalization and `bitcoin`/`Bitcoin` convention;
- canonical section anchor and first-use rule;
- translation note;
- technical/editorial review status.

Move absent optional technologies such as Liquid, ecash, and Fedimint to a parked/Advanced appendix rather than mixing them into the beginner authority.

### Certification

`15_certification.md` should not reproduce the whole assessment model. Its durable role is narrower:

- what the certificate represents;
- the requirement for `assessment-complete` status from `13`;
- issuer and educator authority;
- minimum record and privacy rules;
- appeal, correction, replacement, expiry if any, and revocation;
- verification method and claims that may appear publicly.

Until those decisions are approved, the Student Guide should not describe speculative verification fields or infrastructure as though they are likely release features.

### Advanced holding files

`18_advanced.md` mostly protects the beginner boundary. The problem is maintenance. It is 8,500 words, duplicates much of `advanced/advancedorganizations.md`, includes broken paths, and sometimes designs or prioritizes work that it says should wait.

Use `18_advanced.md` as the sole active holding authority. Give candidate titles a status such as candidate, alias, merge candidate, umbrella, or retired. Resolve overlaps such as privacy/security naming, communication-network naming, and Business/Organizations/Treasury. Repair unique source trails. Treat `advanced/mergefromorganizations.md` as a completed/remaining migration record and reduce or close `advanced/advancedorganizations.md` once unique evidence is preserved.

The Core/Advanced boundary should be based on depth, not topic name. A short learner scenario may belong in Custom; operational merchant policy, accounting, staff procedures, shared-fund governance, and legal implementation belong in Advanced or qualified professional support.

## Proposed harmonized document architecture

No large new document family is needed. The existing numbered structure can work if each file has a precise contract.

| File | Owns | Must not own |
| --- | --- | --- |
| `00` | Roles, precedence, navigation, decision status | Detailed curriculum or assessment rules |
| `01` | Diagnosis of the previous/current state | Current solution specification |
| `02` | Research questions, evidence, counterevidence, confidence, validation status | Unreviewed decisions presented as settled |
| `03` | Deliverables, owners, dependencies, dates/status, acceptance gates | Design philosophy or curriculum content |
| `04` | Principles, constraints, adaptation boundaries, risks | Detailed implementation mechanics |
| `05` | Atomic learner objectives, IDs, required/formative/optional status, support conditions | Task procedures or scoring allocation |
| `06` | Four-module architecture, depth, Core/Custom/Advanced boundaries, migration decisions | Full TOC, prose, rubrics, publication layout |
| `07` | Controlled learner-content blueprint with objective IDs and required/optional/selected labels | A manually drifting copy of current headings |
| `08` | Learner-facing explanation, safety, brief checks, selected learner material, reviews | Facilitator setup, full activity procedures, rubrics, unselected Custom modules |
| `09` | Minimum visual-content requirements and stable asset IDs | Ordinary layout styling, rights/release control |
| `10` | Complete activity and assessment-task records | Normative assessment allocation |
| `11` | Claim and source evidence register | Learner prose or uncontrolled link promotion |
| `12` | Educator run sheets, facilitation, misconceptions, safety, adaptation, task selection | Internal migration instructions or duplicate learner chapters |
| `13` | Objective-to-evidence crosswalk, blueprint, rubrics, thresholds, equivalence, records, reassessment | Certificate issuance governance |
| `14` | Reviewed app/microlearning items and metadata | Practical competency decisions |
| `15` | Credential meaning, eligibility pointer, issuance, privacy, appeals, revocation, verification | Repeated assessment implementation |
| `16` | Controlled terminology and translation guidance | Fragile manual line concordance |
| `17` | Manuscript, layout, accessibility, rights, citations, links, export, QA, sign-off, maintenance | Stakeholder overview narrative |
| `18` | Deferred Advanced candidates and repaired source trails | Current beginner-course design work |

Every active file should begin with a compact control section:

- status;
- audience;
- authoritative for;
- subordinate to;
- owner;
- last reviewed date;
- publication inclusion: yes/no;
- unresolved decisions.

## Prioritized improvement program

### Gate 0: freeze the remaining governing decisions

Resolve before major copyediting:

1. What “eight hours” includes and whether it is a target or promise.
2. What supported mandatory app access means across device, account, connectivity, accessibility, language, identity, privacy, outage, and recovery conditions.
3. The scoring and aggregation rules for the approved 40/10/40/10 allocation, including thresholds, evidence coverage, and how each required contribution gates completion.
4. The meaning of Core, required shared outcomes, Custom selection, and complete Diploma.
5. The final required/formative/optional objective set.
6. Whether CBDCs, stablecoin comparison, and speculation distinction remain required.
7. The final names of the two publications and edition syntax.
8. Whether `17` is rewritten as the specification, as recommended.

Record the answers once with Approved status. Do not continue carrying old alternatives as live prose.

### Gate 1: make the course traceable and feasible

1. Make objectives atomic and freeze IDs.
2. Complete the master crosswalk.
3. Turn `07_contents.md` into the required/optional/selected content blueprint.
4. Add estimated teaching, practice, assessment, and observation time to every required row.
5. Remove, merge, or defer outcomes that cannot fit safely.
6. Build and pilot a complete timed route with realistic cohort/educator assumptions.

### Gate 2: restructure the Student Guide

1. Preserve strong explanations and learner safety.
2. Remove educator setup and full activity procedures.
3. Replace the fixed all-options Module 4 with a common section plus selected inserts.
4. Restore exact objective verbs and explicit competency checkpoints.
5. Label Required, Optional, Selected Custom, and Reference content.
6. Reconcile the plan, contents, and Advanced depth boundaries.
7. Consolidate app explanation, outbound links, and back matter.
8. Complete a copyedit for edition naming, chronology, placeholders, missing words, capitalization, language variant, terms before use, and translation readiness.

### Gate 3: build evidence before certification prose

1. Produce the minimum Activity Bank set.
2. Finalize theoretical and practical blueprints.
3. Populate and validate the complete app theory-item and practical-task-follow-up bank; define supported access and outage handling without creating an unapproved paper substitute.
4. Create task rubrics, critical-error rules, evidence examples, and reassessment.
5. Define educator ratios, authorization, calibration, moderation, and records.
6. Define Module 4's common performance spine and validate variant equivalence.
7. Complete certification governance before public verification claims.

### Gate 4: build the Educator Guide around the tested route

1. Write module run sheets using the common template.
2. Insert stable Student, Activity, item, and rubric IDs.
3. Add neutral prompts, misconception responses, and acceptable evidence examples.
4. Add practical-session safety and incident protocols.
5. Add accessibility, translation, low-connectivity, and offline variants.
6. Add pacing, cut rules, cohort-size assumptions, observation time, and reassessment routes.
7. Remove internal migration language.
8. Test the guide with educators who did not help write it.

### Gate 5: make publication controllable

1. Rewrite `17_spec.md` as the actual specification.
2. Convert `16_lexicon.md` into the controlled vocabulary.
3. Stabilize headings and IDs; repair all internal paths.
4. Rebuild the source register around stable claims.
5. Triage assets to the minimum viable set and record rights/status/accessibility.
6. Approve the small outbound-link and QR register.
7. Define print/PDF accessibility, licensing, export, preflight, sign-off, and maintenance.
8. Run automated checks for broken local links, duplicate IDs, missing objective rows, placeholders, raw URLs, heading hierarchy, and unapproved terms.

### Gate 6: validate the complete product

1. Pilot in-person teaching routes (preferred) and online teaching routes, including low-tech content use and realistic supported-app access.
2. Observe timing, learner comprehension, practical safety, educator consistency, accessibility, and translation friction.
3. Revise once at system level rather than patching each document independently.
4. Conduct a blind educator usability test.
5. Complete external validation after the wording freeze, as described below.
6. Obtain curriculum, technical, safeguarding/accessibility, editorial, and publication sign-off.

## Publication acceptance checklist

### Student Guide

Do not mark `08_student.md` publication-ready until all are true:

- Every required objective has an exact learner teaching point and correct measurable verb.
- Every required/optional/selected section is visibly classified.
- Module 4 supplies only the common material and selected learner insert.
- Full facilitation, scenario variants, and rubrics have left the main manuscript.
- Learner-facing Module 3 and Module 4 competency checkpoints are explicit.
- Low-tech/offline-capable teaching and mandatory supported app assessment are accurately distinguished.
- Safety rules match the tested practical tasks and never expose real secrets or require meaningful personal funds.
- Impartial comparison and acceptable uncertainty are observable in the learning path.
- Terminology follows the controlled lexicon and is introduced before deeper use.
- TOC, headings, module names, edition, and product names are synchronized.
- No placeholder headings, malformed links, missing words, duplicated timeline material, or unresolved verification promises remain.
- All substantive claims have claim IDs and later-validated sources.
- Every outbound link/QR is approved, tested, dated, and has a print fallback.
- Required content and the complete learning/assessment route fit the pilot-tested time budget.
- The final layout passes print, accessibility, alt-text, translation, and export checks.

### Educator Guide

Do not mark `12_educator-draft.md` publication-ready until all are true:

- Every module has a complete timed run sheet tied to objective IDs.
- Every referenced Activity, app item, practical task, rubric, and record exists and has Approved status.
- Preparation, materials, learner-to-educator ratio, and observation time are explicit.
- Suggested questions, likely responses, misconceptions, neutral follow-ups, and source trails are supplied.
- Passing, Not-yet, unsafe, and over-prompted evidence examples are supplied.
- The app covers every required theoretical objective validly, with supported access and approved outage procedures.
- Practical-session safety, privacy, incident, device/fund, and secret-handling protocols are complete.
- Accessibility and translation variants preserve invariant evidence.
- Module 4 selection rules and variant equivalence are operational.
- Feedback, reassessment, moderation, calibration, appeal, and evidence recording are usable.
- Pacing and cut rules never remove a required objective or assessment.
- Internal migration notes and project-only file instructions are absent.
- An educator unfamiliar with the redesign can prepare and deliver safely without relying on undocumented author knowledge.

## Later external validation workstream

As requested, this audit did not verify external factual claims. External review should happen after the internal objective set, content depth, and claim wording are stable; otherwise reviewers will validate text that is later moved or deleted.

The later validation gate should include:

1. **Bitcoin technical review:** transaction lifecycle, nodes, proof of work, consensus wording, signatures, custody, wallet/recovery behavior, fees, confirmation language, supply, halvings, on-chain/Lightning distinctions, and any tool-specific instructions.
2. **Monetary and economic review:** barter claims, monetary history, fiat creation, fractional-reserve explanations, inflation and purchasing-power causation, reserve currencies, CBDCs, and comparisons with stablecoins or other crypto-assets. Distinguish evidence, simplification, interpretation, and contested claims.
3. **Historical review:** My First Bitcoin organizational history, Bitcoin predecessors, white paper/genesis/first transaction/Pizza Day chronology, Bretton Woods, 1971 convertibility changes, and any local historical examples.
4. **Current-data review:** app capabilities, official program links, URLs, QR destinations, named services, wallet/tool status, certificate verification, legal availability, dates, numbers, and screenshots.
5. **Safety and professional-boundary review:** scams, custody risks, minors/vulnerable learners, privacy, provider neutrality, and all language touching legal, tax, accounting, compliance, or financial decisions. Use qualified local review where jurisdiction matters; do not turn review into individualized advice.
6. **Pedagogical review:** the eight-hour route, cognitive load, adult-learning assumptions, accessibility equivalence, educator reliability, and transfer across languages and delivery modes.
7. **Source quality and publication treatment:** prioritize primary and authoritative sources; record counterevidence and uncertainty; date volatile claims; decide which sources are internal verification only and which appear in the publication.

Each claim should end with a recorded status: Verified, Verified with qualification, Revised, Removed, Time-sensitive/recheck, or Contested/present multiple views.

## Final judgement

The project is directionally strong and recoverable without adding unnecessary complexity. Its problem is not a lack of thoughtful material; it is that thoughtful material has accumulated faster than the system that governs it.

The planning package should now stop expanding laterally. Freeze the key decisions, make the objectives traceable, modularize the Student Guide, build the minimum assessment and Activity Bank needed for those objectives, write the Educator Guide around a tested delivery route, and replace the stakeholder overview in `17_spec.md` with real publication controls.

If that sequence is followed, the result can be both rigorous and concise: a learner guide that teaches only what the Diploma can genuinely support, an educator guide that makes safe and consistent delivery possible, and a certificate whose evidence means the same thing across cohorts and locations.
