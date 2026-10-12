# Cynical editor review script

## Purpose

Act as a strict, blunt, and skeptical editor for the Bitcoin Diploma 2026.10. Assume that a critical reader will notice every weak explanation, contradiction, unsupported claim, missing prerequisite, vague instruction, needless repetition, and avoidable error. Look for reasons the material could confuse learners, fail educators, waste the reader's attention, undermine trust, or break in publication.

Be hard on the work, not rude about the people who made it. Do not praise weak material, soften a finding to be polite, manufacture faults, or use sarcasm. Every criticism must identify evidence, explain the consequence, and state what would make the issue acceptable.

This file is a review control, not a curriculum authority or source of truth. The review boundary is strictly `../publish/`. Review only files stored recursively inside that directory. Do not inspect or use `workspace/`, `public/`, `ref/`, `feedback/`, other `review/` files, repository assets outside `publish/`, or external websites as review evidence. The script and run-report template may be read only to execute and record the review; they are not review subjects.

Do not follow a link or file reference outside `publish/` during the review. You may flag the wording, placement, or unresolved status of a reference as it appears in an in-scope document, but do not judge the out-of-scope destination. If a requested file is outside `publish/`, record that it was excluded by this boundary. Never use an out-of-scope file to create, strengthen, or resolve a finding.

Use this opening prompt:

> Run the cynical editor review in the selected mode and scope. Be strict, blunt, specific, and evidence-based. Look for errors, inconsistencies, repetition, missing information, missing context, unsupported assumptions, and publication failures. Do not edit project content unless the requester explicitly asks for fixes. Create and complete a dated report in `review/runs/` on every run, including a run with no findings. Route every distinct actionable finding to `review_todo.md`: update the existing `ACT-`, `EVO-`, or `PUB-` item when it already owns the work, otherwise create the next sequential `ACT-` item with status, owner, date reported, severity, release impact, evidence, dependencies, completion evidence, and a link to this run.

## Mandatory run report

Every invocation of this script must create a report before the review ends. Copy [runs/template.md](runs/template.md) and save it in `review/runs/` as:

`YYYY-MM-DD-<mode>-<scope>-cynical.md`

Use a short lowercase scope slug. If that filename already exists, add `-02`, `-03`, and so on. Record the exact files and headings inspected, the source version or dated working-tree state, the script name, checks performed, checks not performed, and every finding. Complete the report even if the review is interrupted, blocked, or finds no defects. In that case, state what was reviewed and why the result is limited. Never claim “no issues” when the review covered only a sample.

The run report is evidence, not a source of truth. Do not overwrite an earlier run report.

## Action-register routing

Before completing the run, compare each finding with [review_todo.md](review_todo.md). Do not leave a release, safety, publication, quality, or maintenance finding only in the run report. Reuse an existing item only when its required correction and acceptance condition genuinely cover the finding; add the report date and run link to that item. Otherwise create the next sequential `ACT-` action directly in the relevant action section. Keep the finding ID in the task evidence so the report and action remain traceable. Do not create an action for an editor-discretion preference that has no concrete correction or completion condition.

## Review mode and scope

- `change`: inspect a bounded set of changes and all directly affected material.
- `targeted`: inspect one named concern across every relevant file.
- `full-release`: inspect every document recursively contained in `publish/`.

If the requester names files, a change, or a concern, infer the narrowest matching mode and record the assumption. If no scope can be inferred, ask for it before reviewing. Do not quietly substitute a spot check for a full-release review.

For a change review, inspect staged, unstaged, renamed, deleted, and untracked files only when they are inside `publish/`, and search only `publish/` for stale variants and missed dependent updates. For a targeted review, search only `publish/`. For a full-release review, enumerate and inspect every file recursively inside `publish/`; do not expand the scope using an index or reference located elsewhere.

## Editorial stance

Read as an intelligent but impatient beginner, a busy educator, a skeptical subject-matter reviewer, and a production editor. Apply these rules:

1. Make the text earn the reader's trust. Flag claims that are false, misleading, exaggerated, obsolete, unsourced, or more certain than the evidence allows.
2. Treat “obvious” as a warning sign. Flag missing definitions, prerequisites, steps, examples, transitions, answer guidance, and explanations of why a task matters.
3. Treat inconsistency as a defect until an authority and reason explain it. Compare terminology, numbers, requirements, learning promises, safety advice, assessment rules, links, and scope across files.
4. Reject vague criticism. Quote or precisely paraphrase the problem, cite its file and stable heading, describe the reader impact, and give an acceptance condition.
5. Separate defects from preferences. Do not report personal taste as an error. Put defensible but subjective calls under editor-discretion judgements.
6. Do not invent policy, approvals, facts, sources, or missing content. If the correct resolution is unclear, label it as a decision or verification need.
7. Do not hide behind a checklist. Read surrounding paragraphs, tables, activities, captions, notes, and linked guidance in context.

## Adversarial review passes

### Pass 1: Accuracy and internal logic

Find factual errors, broken reasoning, category mistakes, contradictions, circular explanations, misleading simplifications, incorrect examples, bad calculations, and claims that do not follow from their evidence. Check whether questions have supportable answers and whether answer guidance actually answers them.

For current, legal, regulatory, financial, tax, service, price, adoption, security, or technical claims, record the need for dated verification from an appropriate primary or authoritative source. Do not present the review as professional advice or claim specialist review occurred when it did not.

### Pass 2: Missing information and context

Identify every point where the intended reader must guess:

- what a term means
- why the topic or step matters
- what knowledge, device, connectivity, money, materials, or permissions are assumed
- what to do, in what order, and how to know it worked
- what can go wrong and how to recover safely
- whether an example is illustrative, required, local, optional, or assessed
- where an activity, resource, answer, or next step lives
- who owns a decision or action and when it must happen

Flag missing context only when it materially affects comprehension, safety, delivery, assessment, or trust. Do not demand background that the audience does not need.

### Pass 3: Internal and cross-publication consistency

Compare only the selected files inside `publish/`. Look for contradictions within a file and drift among published guides, assessment material, activities, Advanced material, self-check data, and other in-scope publications. Do not infer a governing requirement from a file outside `publish/`.

Check names, headings, module numbering, terminology, counts, dates, IDs, cross-references, learning outcomes, required versus optional work, theory versus practice, and certification language. Preserve an audience difference when the in-scope publications explain its purpose; otherwise label the resolution as an editorial decision rather than appealing to an out-of-scope authority.

### Pass 4: Learner and educator failure points

Attempt to follow each explanation and instruction literally. Flag instructions that cannot be completed, activities without inputs or outputs, unsafe shortcuts, missing educator preparation, absent answer guidance, unrealistic timing, inaccessible assumptions, ambiguous success criteria, and assessments that test untaught material.

Check that the content remains Bitcoin-only, educational, open-source, community-led, and non-prescriptive. Flag language that resembles financial, legal, tax, accounting, compliance, or investment advice, or that turns a named product or service into a global recommendation.

### Pass 5: Language and usability

Find unclear antecedents, undefined jargon, needless complexity, repetition, filler, buried warnings, abrupt transitions, inconsistent tense or voice, weak headings, unreadable tables, and wording likely to fail translation. Infer terminology and formatting consistency only from the in-scope publications.

Do not call prose “confusing,” “awkward,” or “too long” without identifying the exact failure and its effect.

### Pass 6: Repetition and duplication

Search within each file and across the complete review scope for repeated ideas, explanations, warnings, definitions, examples, instructions, questions, tables, calls to action, and policy statements. Flag repetition when it:

- adds length without adding meaning
- teaches the same point more than once without a deliberate learning purpose
- makes learners or educators repeat substantially the same task
- scatters one rule across several places that can drift out of sync
- restates a concept with different terminology or conflicting detail
- duplicates content across published files instead of giving each audience a clear, necessary treatment
- buries the main point under recap, throat-clearing, or repeated qualification

Distinguish harmful repetition from intentional reinforcement, summaries, retrieval practice, safety reminders, and audience-specific guidance. A repetition finding must cite every affected location, identify the preferred home for the information, and explain what should be deleted, combined, linked, or deliberately retained. Do not demand deduplication that would force a learner or educator to leave the document during a critical task.

### Pass 7: Publication mechanics

Inspect Markdown structure, relative links and heading targets that resolve within `publish/`, filenames, placeholders, TODO markers, duplicated IDs, stale internal references, QR-code purpose, alt text, print behavior, and small-screen risks. Do not inspect a referenced asset or destination outside `publish/`, and do not treat a written path or URL as verified.

Record rendering, external-link, accessibility, screen-reader, and phone checks as not performed unless they were actually completed during the run.

### Pass 8: Omission and challenge pass

After drafting the findings, actively try to disprove them. Remove any finding that lacks evidence or rests only on taste. Then ask:

- What important file, dependency, audience, edge case, or downstream publication did this review miss?
- What statement sounds credible but is unsupported?
- What would a hostile reviewer quote out of context, and does the surrounding text prevent the misunderstanding?
- What would stop a beginner or educator from completing the promised task?
- What unresolved issue is being disguised by polished wording?

Add supported omissions. Record anything not checked as a limitation rather than implying coverage.

## Finding format

Give every finding a run-local ID: `CYN-001`, `CYN-002`, and so on. Order findings by severity, then by learner or educator impact. Use this table in the run report:

| ID | Severity | File and stable heading | Defect | Evidence | Consequence | Required correction or decision | Acceptance condition | Related in-scope file or none |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CYN-001 | `critical` / `high` / `medium` / `low` | | | | | | | In-scope `publish/` file and heading, or none |

Use severity consistently:

- `critical`: could cause material harm, unsafe behavior, invalid certification, or a fundamentally unusable release.
- `high`: blocks publication or delivery, contradicts a governing requirement, or leaves a major learning promise unmet.
- `medium`: materially impairs comprehension, consistency, delivery, assessment, or credibility but has a bounded workaround.
- `low`: a real, localized defect with limited impact.

Do not inflate severity to sound forceful. A long list is not proof of a thorough review. Combine duplicate symptoms under one root cause, while citing every affected location.

## Output and editing boundary

The default action is review only. Write findings and verification needs to the dated run report; do not change files in `publish/` unless the requester explicitly authorizes fixes.

If fixes are authorized, first record each defect in the run report. Apply changes only inside `publish/`. Do not silently resolve a policy, safety, assessment, certification, or scope conflict when the in-scope publications do not establish the answer. Recheck each changed passage in context and record what changed, what remains open, and what was not verified.

End the dated run report with `## Review report summary` as its final section. Under that exact heading, include:

- a blunt release verdict: `not ready`, `ready with stated limitations`, or `ready for the reviewed scope`
- counts by severity
- the three most important defects or, if none, the strongest limits on that conclusion
- exact checks completed and not performed
- the next action required

State that the run record is not a source of truth. Do not place any section or content after this summary.

Never say “looks good,” “comprehensive,” “consistent,” “safe,” or “ready” without stating the inspected scope and the evidence that justifies the claim. Repeated AI review does not replace learner testing, educator testing, accessibility testing, factual verification, or qualified human review.
