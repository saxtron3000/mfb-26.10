# Review to-do list

This is the working list for the 2026.10 review. Start with the open items below; the completed items, decisions, and old review notes are kept further down as a record.

## What needs attention

**18 of 33 actions are still open.** Start with the safety and certificated-delivery work, then clear the publication blockers.

| Do this first | Why it matters | Tasks |
|---|---|---|
| Make delivery safe and ready to certify | Do this before a certificated delivery. | `ACT-022` Remove the unsafe wallet exercise; `ACT-002` align assessor scoring; `ACT-003` agree record and certificate rules. |
| Make the materials ready to publish | Do this before release. | `ACT-009`, `ACT-011`, `ACT-023`, `ACT-024`, `ACT-028`, and `ACT-019`. |
| Improve and maintain the materials | Important, but does not by itself block release. | `ACT-007`, `ACT-010`, `ACT-013`, `ACT-021`, `ACT-025`, and `ACT-026`. |

`ACT` means a task. `DEC` is a past decision kept for reference. `ANN` is an old reviewer note; it is not an approval or a current task.

### Task list at a glance

Use this table to find the task. The detailed entry below has the supporting links and the definition of done.

#### Open, blocked, in-progress, or needs-verification actions

| Task | What to do | Current state | Do this before | Depends on |
|---|---|---|---|---|
| ACT-022 | Remove the unsafe wallet exercise | Open | publication | — |
| ACT-002 | Align assessor scoring | In progress | certificated delivery | ACT-001 |
| ACT-003 | Agree record and certificate rules | Blocked | certificated delivery | — |
| ACT-009 | Check public links | Needs checking | publication | ACT-006 |
| ACT-011 | Review the optional self-check | Needs checking | publication | — |
| ACT-023 | Make every activity usable | Open | publication | ACT-022 |
| ACT-024 | Support claims in Activities 001 and 002 | Open | publication | — |
| ACT-028 | Produce or explicitly defer every guide visual | Open | publication | ACT-013, EVO-002 for the app panel |
| ACT-019 | Do the final publication check | Blocked | publication | ACT-009, ACT-011, ACT-013 |
| ACT-025 | Show an eight-hour route for a real class | Open | next cohort | ACT-001 |
| ACT-007 | Add editable teaching slides | Open | ongoing maintenance | — |
| ACT-010 | Stabilise source and lexicon references | Open | ongoing maintenance | — |
| ACT-013 | Choose and track essential visuals | In progress | ongoing maintenance | — |
| ACT-021 | Reduce assessed competencies to seven | Done | ongoing maintenance | [2026-09-30 assessment consolidation review](runs/2026-09-30-act-021-seven-competencies.md) |
| ACT-026 | Remove repeated guide content and fix `BD-V-049` | In progress | ongoing maintenance | ACT-013 |
| ACT-029 | Repair the source-of-truth map links | Done | ongoing maintenance | — |
| ACT-030 | Retire the duplicate asset style guide | Done | ongoing maintenance | — |
| AST-001 | Supply the official test-network address and network label for `BD-V-036` | Open | asset production | My First Bitcoin confirmation |
| AST-002 | Supply the official test Lightning invoice, amount, description, expiry, and network for `BD-V-078` | Open | asset production | My First Bitcoin confirmation |
| AST-003 | Supply an approved active Lightning address for `BD-V-080` | Open | asset production | My First Bitcoin confirmation |

#### Completed actions

| Task | Finished work | Owner | Related task or decision |
|---|---|---|---|
| ACT-001 | Confirm the assessment route | unassigned | — |
| ACT-004 | Clarify the eight-hour minimum | project lead | — |
| ACT-005 | Set the certificate position | unassigned | ACT-020 |
| ACT-006 | Set link and wallet-guidance rules | project lead | DEC-09 |
| ACT-008 | Finish and prioritize the Student Guide ending | unassigned | — |
| ACT-012 | Fix the Creative Commons visual | unassigned | — |
| ACT-014 | Sort the decision list | project lead | — |
| ACT-015 | Confirm October outputs | project lead | — |
| ACT-016 | Confirm the Lightning boundary | unassigned | DEC-06 |
| ACT-017 | Explain release readiness | project lead | — |
| ACT-018 | Sort reviewer notes | unassigned | — |
| ACT-020 | Explain educator-issued certificates | project lead | — |
| ACT-027 | Align module guiding questions | unassigned | — |

### Review-run intake, 2026-09-25

Each completed review run below is represented by a current action or finding in this register. A run record is review evidence, not an authority or completion claim.

| Review control | Run record | Findings routed to the register |
|---|---|---|
| Alignment | [full-release alignment run](runs/2026-09-21-full-release-alignment.md#findings-created-or-updated) | `EVO-001`, `PUB-001`, `PUB-002`, and the existing release actions listed in the run. |
| Alignment | [recent workspace-to-publication propagation change review](runs/2026-09-21-change-alignment-propagation.md#findings-created-or-updated) | No new `EVO-` or `PUB-` ID; confirms the recent duration, October-output, educator-issued-certificate, optional-link, wallet-guidance, pre-reading, and production-marker changes are synchronized. `PUB-002` remains open. |
| Cynical editor | [full-release cynical-editor run](runs/2026-09-21-full-release-26.10-cynical.md#cynical-editor-findings) | `ACT-022`–`ACT-027`; `CYN-005` is also tracked by `ACT-008`, `CYN-006` by `ACT-011`, and `CYN-007` by `PUB-002`. |
| Style | [full-release style run](runs/2026-09-21-full-release-style.md#findings-created-or-updated) | Existing `ACT-001`–`ACT-003`, `ACT-004`, `ACT-008`–`ACT-013`, and `ACT-015`–`ACT-019`; its completed editorial corrections remain recorded in that run. |
| To-do control | [full-release to-do run](runs/2026-09-21-full-release-todo.md#findings-created-or-updated) | Existing `ACT-003`, `ACT-008`, `ACT-016`, `ACT-018`, and the register-wide status/evidence review. |
| Alignment | [asset-migration change review](runs/2026-09-25-change-assets-alignment.md#findings-created-or-updated) | `ACT-028`, `EVO-002`, and `ACT-029`. |
| Cynical editor | [asset-migration change review](runs/2026-09-25-change-assets-cynical.md#cynical-editor-findings) | `CYN-001`, routed to `ACT-028`. |
| Style | [asset-migration change review](runs/2026-09-25-change-assets-style.md#findings-created-or-updated) | Confirms `ACT-028`, `ACT-029`, and `ACT-030`; no prose change applied. |

## How to use this list

This file combines the nine earlier review lists. Use it as the one place to track current work. The original files stay in `review/` as background, not as duplicate to-do lists.

Tick a box only when the task is actually finished. Keep the line below each task up to date: status, owner, date, priority, evidence, dependencies, and what proves it is done. `critical` means safety, governance, or certificate integrity; `high` blocks a release; `medium` is important maintenance or quality work; `low` is small follow-up.

Do not invent an approval, an owner, a test result, or a completed review. For each review, save a dated note in `review/runs/` using [runs/template.md](runs/template.md). Keep completed, rejected, and superseded tasks here so we do not lose the history.

## Recommended work order

1. Fix the safety and certificated-delivery blockers: `ACT-022`, `ACT-002`, and `ACT-003`.
2. Finish the publication blockers: `ACT-009`, `ACT-011`, `ACT-023`, `ACT-024`, and `ACT-028`.
3. Test the eight-hour route for a real class (`ACT-025`).
4. Complete the remaining maintenance work, then run `ACT-019` as the final check.

## Release and publication actions

Items `ACT-001` onward preserve every action and acceptance condition from the former release list. Headings indicate priority. Paths such as `05_competencies.md` in inherited text refer to `workspace/`; official publication links resolve from this directory.

### Release blockers for certificated delivery

- [x] **ACT-001** **Confirm that the assessment route works.**

  - Status: done | Owner: unassigned | Updated: 2026-09-21 | Severity: critical | Release impact: certificated-delivery blocker | Evidence: [Educator Guide assessment protocol:47](../publish/mfb-bd-26.10/mfb-bd-eg-26.10.md:47#operational-assessment-protocol), [Assessment Grid assessment route:29](../publish/mfb-bd-26.10/mfb-bd-assessment-grid-26.10.md:29#a-simple-way-to-use-this-grid), and [assessment workflow:132](../workspace/13_assessment.md:132#6-assessment-workflow) | Depends on: none | Completion evidence: the current materials define an educator-led activity-based route for every required competency; permit in-person, online, low-tech, simulated, testnet, physical-token, and carefully structured low-stakes routes; provide support and reassessment; preserve accessibility and safety; and require capacity planning for troubleshooting, feedback, and follow-up.

  - Define a simple, educator-led route in which activities are deliberately designed to elicit the required competencies. Successful activity performance may provide the evidence; the educator may use probing questions when understanding or safety is unclear.
  - Permit in-person, online, low-tech, simulated, testnet, physical-token, and carefully structured low-stakes-funds routes, with accessibility adaptations that preserve the competency. Do not require significant personal funds or a particular tool.
  - Give each learner a fair opportunity to ask for support and to demonstrate the competency. If a learner is `NY` (**Not Yet**), arrange another assessment opportunity during class, a break, an additional call, or a follow-up session.
  - Consider cohort capacity and assessment time when planning delivery, including troubleshooting, extra assistance, feedback, reassessment, and follow-up. Use extended sessions or additional meetings where needed; no fixed educator-to-learner ratio is required.
  - Treat piloting as an ideal quality-improvement activity, not a prerequisite for educators to issue certificates. The first cohort may be the first live validation of the route.
  - Acceptance: the Educator Guide gives educators a practical, flexible assessment route that assesses every required competency, supports reassessment, accommodates access constraints, and makes time and follow-up planning explicit without imposing unnecessary recording or pilot requirements.

- [ ] **ACT-002** **Get assessors to score examples the same way.**

  - Status: in-progress | Owner: unassigned | Updated: 2026-09-21 | Severity: critical | Release impact: certificated-delivery blocker | Evidence: [Educator Guide calibration examples:198](../publish/mfb-bd-26.10/mfb-bd-eg-26.10.md:198#calibration-examples-for-assessor-discussion) exist for `T2`, `P9`, and an example `P11` variant; no dated assessor session record was found | Depends on: ACT-001 | Completion evidence: pending independent scoring, discussion, and recorded agreement by the selected delivery team.

  - Create one annotated `MS` and one annotated `NY` example for `T2`, `P9`, and the selected `P11` variant.
  - Calibrate assessors, resolve scoring differences, and retain the date, assessors, variants, and agreed interpretation.
  - Acceptance: the selected delivery team has completed and recorded the Educator Guide's minimum calibration process.

- [ ] **ACT-003** **Agree the local rules for records and certificates.**

  - Status: blocked | Owner: unassigned | Updated: 2026-09-21 | Severity: critical | Release impact: certificated-delivery blocker | Evidence: [Certification framework current governance](../workspace/15_certification.md#8-current-governance-and-future-options) settles educator issuance but still requires proportionate local privacy, consent, records, correction, appeals, accessibility, and exceptional-case arrangements before certificated delivery | Depends on: none | Completion evidence: the issuer model is approved, but no complete local governance pack has been approved for a delivery context.

  - Preserve the educator-issued model. Define permitted data; consent or assent; access roles; retention and deletion; correction, appeal, incident, outage, and exceptional-case routes; assessor permissions, moderation, reconciliation, and audit trail where used; educator-managed certificate correction, replacement, withdrawal, and optional verification; and rules for minors and safeguarding.
  - Acceptance: an approved, proportionate governance pack exists before competency evidence is retained for certification or a pilot.

### Decisions required before dependent copy is final

- [x] **ACT-004** **Clarify the eight-hour minimum.** Eight hours is the shortest planned route, not a limit. Give learners more time whenever they need it.

  - Status: done | Owner: project lead | Updated: 2026-09-21 | Severity: high | Release impact: publication blocker resolved | Evidence: [Competency framework minimum rule:22](../workspace/05_competencies.md:22), [scope assumption:52](../workspace/03_scope.md:52), [Educator Guide minimum pathway:603](../publish/mfb-bd-26.10/mfb-bd-eg-26.10.md:603#the-minimum-eight-hour-pathway), and `DEC-01` below | Depends on: none | Completion evidence: the fixed-scope conflict was removed and the minimum, no-upper-limit, and accessible pre-reading rules were aligned in the active planning authorities and Educator Guide.

  - Acceptance: all authorities and public schedule claims use one rule.

- [x] **ACT-005** **Set the 2026.10 certificate position.** Educators may issue certificates after using the assessment grid. The educator makes that decision; My First Bitcoin does not issue or guarantee the certificate.

  - Status: done | Owner: unassigned | Updated: 2026-09-21 | Severity: high | Release impact: publication blocker | Evidence: user-approved certification policy recorded in this review discussion and reflected in the [assessment-grid completion rule:77](../publish/mfb-bd-26.10/mfb-bd-assessment-grid-26.10.md:77) | Depends on: ACT-020 | Completion evidence: approved certificate position recorded above; publication reconciliation remains under `ACT-020`.

- [x] **ACT-006** **Set simple rules for programme links and wallet guidance.** Say which optional My First Bitcoin pathways can appear, how often links are checked, and how to give local software guidance without making a global recommendation.

  - Status: done | Owner: project lead | Updated: 2026-09-21 | Severity: high | Release impact: publication blocker resolved | Evidence: `DEC-08` approves the qualified open-source preference; `DEC-09` approves direct, named, optional programme links; [Student Guide pathway](../publish/mfb-bd-26.10/mfb-bd-sg-26.10.md), [Educator Guide pathway](../publish/mfb-bd-26.10/mfb-bd-eg-26.10.md), [specification](../workspace/16_spec.md), and [horizon maintenance policy](../workspace/18_horizon.md) reflect the policy | Depends on: DEC-09 | Completion evidence: named programmes are optional further learning beyond the Diploma; direct links are permitted; weekly automated checks are planned; only humans may approve link changes; and a failed optional pathway link triggers an important 24-hour resolution alert without becoming a publication blocker.

  - Acceptance: the policy is recorded and Student Guide wording follows it.

- [x] **ACT-020** **Explain educator-issued certificates clearly.** Publish the two types: **participation** for attendance and **completion** for a learner who passes the required assessment. Educators issue them using the assessment grid; they are not centrally verified guarantees from My First Bitcoin.

  - Status: done | Owner: project lead | Updated: 2026-09-21 | Severity: high | Release impact: publication blocker resolved | Evidence: [Student Guide certificate meaning](../publish/mfb-bd-26.10/mfb-bd-sg-26.10.md#certificate-meaning-and-issuer), [Educator Guide certificate procedure](../publish/mfb-bd-26.10/mfb-bd-eg-26.10.md#confirm-what-the-certificate-means), [Assessment Grid issuer rule](../publish/mfb-bd-26.10/mfb-bd-assessment-grid-26.10.md), [assessment authority](../workspace/13_assessment.md#8-certification-meaning), and [certification authority](../workspace/15_certification.md#2-what-a-certificate-represents) | Depends on: none | Completion evidence: participation/completion, educator issuance, Assessment Grid minimum, ETP badge treatment, framework-first boundary, and My First Bitcoin's non-central/non-guarantee role are aligned.

  - Use the current [Canva certificate template](https://canva.link/55s417wnb9ehdwo) as the present template reference. Use “My First Bitcoin Diploma” as the programme wording, and show an ETP-completion badge beside the educator’s name when applicable.
  - Add the learner-facing explanation to the Student Guide, the full educator procedure and certificate distinction to the Educator Guide, a footnote to the assessment grid, and aligned guidance in the relevant `workspace/` authorities. Do not publish internal plans for future certification tooling or CRM integration.
  - Acceptance: the two certificate types, educator responsibility, assessment-grid minimum, optional evidence retention, ETP badge treatment, and My First Bitcoin’s non-guarantee/non-central-issuer role are consistent across all listed materials.

### Publication and maintenance actions

- [x] **ACT-021** **Reduce the assessed competencies from 11 to 7.** The seven-result grid and aligned curriculum are implemented; the old-to-new map is retained as labelled history in `workspace/05_competencies.md`.

  - Status: done | Owner: unassigned | Updated: 2026-09-30 | Severity: medium | Release impact: maintenance completed | Evidence: [Educator Guide operational assessment protocol](../publish/mfb-bd-26.10/mfb-bd-eg-26.10.md#operational-assessment-protocol), [seven-result Assessment Grid](../publish/mfb-bd-26.10/mfb-bd-assessment-grid-26.10.md), [old-to-new map](../workspace/05_competencies.md#historical-code-migration), and [final review](runs/2026-09-30-act-021-seven-competencies.md) | Depends on: none | Completion evidence: seven parent competencies, at most three look-fors each, one undivided `C3` comparison, all original requirements mapped, activity links updated, and active identifiers reconciled.

  | New competency | Original competencies | Suggested assessment breakdown |
  |---|---|---|
  | `C1` Money and modern-money trade-offs | `C1` + `C2` | Up to three points: why money is used and its functions/properties; comparison of two forms of money; one local or realistic modern-money trade-off. |
  | `C2` Bitcoin foundations and rules | `C3` + `C4` | Up to three points: digital copying and shared verification; explaining Bitcoin's rules and network roles at a beginner level; explaining how a Bitcoin property could help or limit its use as money. Keep technical depth achievable for beginners. |
  | `C3` Bitcoin and digital-asset comparison | `C5` | One guided comparison statement, without numbered sub-points: compare Bitcoin with another digital asset using relevant criteria and a trade-off, and distinguish learning from speculation or promotion. Retain this competency and its title. |
  | `C4` Wallets, custody, and safety | `C6` + `C7` | Up to three points: public/secret information and custody choices; wallet types; recognising a risk and knowing when to stop, verify, or seek help. |
  | `C5` Payment and access pathways | `C8` | Two points where useful: compare on-chain and Lightning payments in a guided example; compare access or exchange pathways and their risks. |
  | `C6` Safe access and recovery readiness | `C9` + `C10` | Two distinct practical points: supported wallet access and receipt with checks; recovery readiness using prepared or simulated materials. |
  | `C7` Local Bitcoin-as-money task | `C11` | Two points where useful: safely perform a locally relevant task or simulation; explain its purpose, alternative, trade-offs, possible failure, and safe next step. |

  - Use up to three sub-points only when they make assessment clearer. Keep one `MS`/`NY` decision for each parent competency; do not turn sub-points into separate tests.
  - Map every old requirement to a new one. This is a clearer structure, not less learning or a lower safety standard. Keep `C1`–`C5` as theory and `C6`–`C7` as practice.
  - Make Page 2 work on its own. Explain each competency, `MS`, `NY`, practical observation, and completion in short language. Add a simple example of good-enough beginner work for each competency.
  - Agree the grid first. Then update the [competencies](../workspace/05_competencies.md), [assessment framework](../workspace/13_assessment.md), [Educator Guide](../publish/mfb-bd-26.10/mfb-bd-eg-26.10.md), [Student Guide](../publish/mfb-bd-26.10/mfb-bd-sg-26.10.md), and any related maps. Keep the old codes only as labelled history.
  - Keep the activity-based assessment, reassessment, and participation/completion distinction agreed in `ACT-001` and `ACT-020`.
  - Done when: all seven competencies are clear, cover the existing requirements, have no more than three helpful sub-points, and match every active reference. Keep the old-to-new map and check record.

- [ ] **ACT-007** **Add editable teaching slides.** Link a simple slide set from the [Educator Guide](../publish/mfb-bd-26.10/mfb-bd-eg-26.10.md). Encourage educators to adapt it for their learners while keeping the required learning and safety guidance.

  - Status: open | Owner: unassigned | Updated: 2026-09-21 | Severity: medium | Release impact: maintenance | Evidence: [Educator Guide media guidance:829](../publish/mfb-bd-26.10/mfb-bd-eg-26.10.md:829#media-and-tool-fallbacks) supports projection-free teaching, but no editable slide set or slide link was found | Depends on: none | Completion evidence: slide set and required introduction remain missing.

  - Acceptance: the Educator Guide introduces and links the slide set, explains its recommended use, and gives clear adaptation guidance. Slides support discussion and practical learning, and teaching remains possible without projection equipment.

- [x] **ACT-008** **Finish or remove the unfinished Student Guide ending.** Decide on the source/update page and the optional support QR. The certificate section is already settled.

  - Status: done | Owner: unassigned | Updated: 2026-09-21 | Severity: high | Release impact: publication blocker resolved | Evidence: [Student Guide next steps](../publish/mfb-bd-26.10/mfb-bd-sg-26.10.md#next-steps) now provides separate, prioritized purposes for proofreading and feedback, contributing, joining a learning community, adapting the curriculum, and supporting My First Bitcoin; user confirmation on 2026-09-21 records that retained links were checked with colleagues. The [certificate section](../publish/mfb-bd-26.10/mfb-bd-sg-26.10.md#certificate-meaning-and-issuer) states the educator-issued model without implying a central verification service | Depends on: none | Completion evidence: conditional draft headings and duplicate calls to action are removed; retained destinations have learner-facing headings and distinct purposes; donation support is a standalone section.

  - The report requires a real, privacy-preserving certificate process before retaining the verification section. A live link alone is insufficient.
  - Acceptance: every retained section has a learner-facing heading and a verified destination or governing process; unavailable sections are removed.

- [ ] **ACT-009** **Check every public link before publishing.** Review every named programme, form, case study, network, leaderboard, source, and support link in the Student Guide.

  - Status: needs-verification | Owner: unassigned | Updated: 2026-09-30 | Severity: high | Release impact: publication blocker | Evidence: [internal My First Bitcoin link register](../links/links-internal.md) and [external or other link register](../links/links-external.md) inventory destinations, but no complete dated external check for this edition was found | Depends on: ACT-006 | Completion evidence: live destination verification remains external work.

  - A failed optional further-learning link does not by itself block publication. It raises an important alert requiring a human-approved solution within 24 hours. Required instructional or safety destinations retain their normal publication impact.
  - Acceptance: each retained destination is live, appropriate, and recorded as checked for the edition; the weekly automated review and human-approval boundary are documented in both link registers.

- [ ] **ACT-010** **Make source and lexicon references survive edits.** Replace line numbers with stable headings or claim IDs. Keep the reading audit separate from learner definitions, and record who checked each shared claim and when.

<a id="act-010-replace-mutable-source-and-terminology-locations"></a>

  - Status: open | Owner: unassigned | Updated: 2026-09-21 | Severity: medium | Release impact: maintenance | Evidence: [Resources register:7](../workspace/09_resources.md:7) still requires mutable line references, including entries at [line 13](../workspace/09_resources.md:13); the [Lexicon:13](../publish/mfb-lx-26.10.md:13) also retains occurrence-line metadata | Depends on: none | Completion evidence: stable claim IDs and maintenance fields are not implemented.

  - Preserve each claim or section, source type and authority, volatility, reviewer, date checked, next review date, and permitted learner-facing treatment. Keep genuinely local and changing facts in the Educator Guide's local verification record. Maintain the resource register and lexicon as versioned tools, with first/later occurrence audits in separate reports.
  - Acceptance: the source register and lexicon remain correct after a normal manuscript edit without manual line-number repair.

- [ ] **ACT-011** **Finish the optional self-check review.** Keep the result message about this 12-question check only. Review every question, then test it on a small phone and with a screen reader.

  - Status: needs-verification | Owner: unassigned | Updated: 2026-09-21 | Severity: high | Release impact: publication blocker | Evidence: the score wording was changed in [self-check source:52](../publish/mfb-ml-26.10/mfb-ml-26.10.md:52), but no dated independent editorial, small-phone, or screen-reader test record was found; [CYN-006](runs/2026-09-21-full-release-26.10-cynical.md#cynical-editor-findings) reports that all 12 question pairs still declare independent factual and editorial review outstanding | Depends on: none | Completion evidence: required human/device/accessibility checks remain unrecorded, and approved Markdown content matches both CSV exports.

  - The report identified that message at the 10–12 score band and suggested “You showed a strong result on this quick self-check.” Preserve item mappings to the Student Guide. The check samples selected content from Modules 1–3 and does not assess Module 4 or observed practical skills. This is a publication action, not a certification blocker; the example is historical evidence, not approval for a new pass threshold.
  - Acceptance: reviewed item metadata is complete, the result message does not imply Diploma competence, and no score tracking, threshold, or educator access is introduced.


- [x] **ACT-012** **Fix the missing Creative Commons visual.** The old local file reference has been replaced with a clear production marker.

  - Status: done | Owner: unassigned | Updated: 2026-09-21 | Severity: medium | Release impact: publication blocker resolved | Evidence: [Student Guide marker:13](../publish/mfb-bd-26.10/mfb-bd-sg-26.10.md:13) and [asset brief:159](../workspace/08_assets.md:159) specify the Sanity-required official Creative Commons mark at the licence statement without a missing local-file reference | Depends on: none | Completion evidence: the broken local target was replaced with a clear Sanity production marker at the required Diploma location; Sanity production must upload the approved official mark and retain the stated alt text.

  - Acceptance: add the approved asset during visual production or replace the embedded image with a non-broken placeholder; rerun the local-link check.

- [ ] **ACT-013** **Choose and track the visuals we really need.** Agree the essential set before commissioning work. Track the file, rights, alt text, source, and review. Do not make QR visuals until their destinations are approved.

<a id="act-013-control-visual-production-scope"></a>

  - Status: in-progress | Owner: unassigned | Updated: 2026-09-25 | Severity: medium | Release impact: maintenance | Evidence: [visual index](../workspace/08_assets.md#2-visual-index) records scope, rights, alt text, placement, and review requirements; [asset production log](../assets/assets-list.md) records 101 generic briefs but zero asset-specific reference images, uploads, or production packages; [asset-migration alignment run](runs/2026-09-25-change-assets-alignment.md#findings-created-or-updated) | Depends on: none | Completion evidence: planning controls exist; essential asset selection and production verification remain incomplete.

  - Acceptance: an approved essential-visual list and production tracker exist.

### Review-register maintenance

- [x] **ACT-014** **Sort out the old decision list.** Keep settled decisions and their evidence for reference. Leave only genuinely unanswered questions in the active queue.

  - Status: done | Owner: project lead | Updated: 2026-09-21 | Severity: medium | Release impact: maintenance | Evidence: `DEC-01`–`DEC-12` have approved answers below | Depends on: none | Completion evidence: all approved questions were closed and propagated while retaining historical alternatives.

  - Acceptance: the active decision queue contains no question whose implemented answer is already established in the active authorities. Historical alternatives remain clearly labeled and do not reopen settled policy. Do not maintain a second live queue in the original file.


### Actions recovered from the report and decision log

- [x] **ACT-015: Confirm what ships in October.** October includes print/PDF materials, an online PDF, and website-ready Sanity content. Cohorts, self-paced learning, an optional app, and cross-modal branches come later.

<a id="act-015-reconcile-october-publication-outputs"></a>

  - Status: done | Owner: project lead | Updated: 2026-09-21 | Severity: high | Release impact: publication blocker resolved | Evidence: [scope publishing system](../workspace/03_scope.md#15-publishing-system), [design publication model](../workspace/04_design.md), [plan October outputs](../workspace/06_plan.md#8-october-2026-output), [specification outputs](../workspace/16_spec.md#materials-and-outputs), [horizon boundary](../workspace/18_horizon.md#4-maintain-localize-and-extend-delivery-without-diploma-drift), and public [elevator release direction](../public/mfb-bd-elevator.md#release-direction) | Depends on: none | Completion evidence: all affected authorities and public wording distinguish October publication formats from future instructional branches and specify source-to-Sanity alignment.

  - Acceptance: release criteria and all affected authorities describe the same approved outputs, and source-to-Sanity maintenance is explicit. Link completion to `DEC-07`.

- [x] **ACT-016: Confirm what learners need to know about Lightning.** Check that the materials require explanation and comparison, not an unapproved live-use requirement.

  - Status: done | Owner: unassigned | Updated: 2026-09-21 | Severity: high | Release impact: required before cohort | Evidence: [Student Guide distinction:1274](../publish/mfb-bd-26.10/mfb-bd-sg-26.10.md:1274), [Educator Guide boundary:2247](../publish/mfb-bd-26.10/mfb-bd-eg-26.10.md:2247#on-chain-and-lightning-payments), and [local Lightning option:1443](../publish/mfb-bd-26.10/mfb-bd-sg-26.10.md:1443#lightning-payments-where-locally-appropriate) require comparison while reserving setup and live practice for safe, locally selected use | Depends on: DEC-06 | Completion evidence: `DEC-06` answer A is consistently implemented.

  - Acceptance: the current answer to `DEC-06` is evidenced and consistently reflected in teaching and assessment without imposing an unapproved practical requirement.

- [x] **ACT-017: Explain what this release is ready for.** Clearly separate the teaching package, assessment materials, local readiness to certify, and actual educator-issued certificates.

  - Status: done | Owner: project lead | Updated: 2026-09-21 | Severity: critical | Release impact: positioning resolved; local readiness remains governed separately | Evidence: [Student Guide release and issuer boundary](../publish/mfb-bd-26.10/mfb-bd-sg-26.10.md#certificate-meaning-and-issuer), [Educator Guide release status](../publish/mfb-bd-26.10/mfb-bd-eg-26.10.md#about-this-guide), [certification release boundary](../workspace/15_certification.md#9-framework-first-release-boundary), [specification purpose](../workspace/16_spec.md#purpose), and public [keynote certificate direction](../public/mfb-bd-keynote.md#assessment-and-certification-direction) | Depends on: none | Completion evidence: project authorities and public materials now distinguish publication from local certification readiness and identify the educator as issuer without implying central My First Bitcoin evaluation or verification.

  - Acceptance: scope, research, assessment, certification, overview, horizon, and public claims use the same release promise; no certificate readiness is inferred from a written protocol alone.

- [x] **ACT-018: Sort the old reviewer notes.** Check each note against the current text and approvals. Leave unclear handwriting marked as unclear rather than guessing.

  - Status: done | Owner: unassigned | Updated: 2026-09-21 | Severity: medium | Release impact: maintenance | Evidence: [annotation inventory and dispositions:510](review_todo.md:510) records a dated disposition and evidence for `ANN-001`–`ANN-242`; 20 unclear items remain explicitly `needs-clarification` rather than guessed | Depends on: none | Completion evidence: all 242 historical annotations have been triaged.

  - Acceptance: every annotation has a disposition and evidence. Approved work has an existing or new action ID with a concrete acceptance condition; duplicated notes link to the same action; unclear notes remain explicitly blocked on clarification.

- [ ] **ACT-019: Do the final publication check.** Check public links, current claims, rendering, accessibility, and translation readiness, then save a dated record of what passed and what did not.

<a id="act-019-complete-the-final-publication-verification-pass"></a>

  - Status: blocked | Owner: unassigned | Updated: 2026-09-25 | Severity: high | Release impact: publication blocker | Evidence: [full-release style run](runs/2026-09-21-full-release-style.md#findings-created-or-updated), [full-release to-do run](runs/2026-09-21-full-release-todo.md#findings-created-or-updated), and remaining external-link-verification, accessibility/device-test, and visual-production work under `ACT-009`, `ACT-011`, `ACT-013`, and [ACT-028](#act-028-produce-or-explicitly-defer-every-guide-visual) | Depends on: ACT-009, ACT-011, ACT-013, ACT-028 | Completion evidence: dependency checks remain incomplete.

  - Acceptance: the edition has a dated verification record distinguishing passed checks, remaining blockers, and checks not performed. No historical audit count is presented as a fresh result.

### Review findings added from the cynical-editor run

- [x] **ACT-022: Remove the unsafe wallet exercise.** Rewrite or remove Activity 018 so it never asks anyone to fund a wallet, create or restore a live learner wallet, or handle a real recovery phrase.

  - Status: complete | Owner: unassigned | Updated: 2026-09-30 | Severity: critical | Release impact: source correction complete; verify the deployed Resources Hub page during publication | Evidence: [CYN-001](runs/2026-09-21-full-release-26.10-cynical.md#cynical-editor-findings) identified the unsafe prior procedure; [Activity 018](../publish/mfb-act-26.10/mfb-act-018-creating-your-first-bitcoin-wallet.md) now uses only a guided, nonfunctional or empty no-value training environment, placeholder recovery materials, and non-payable examples | Depends on: none | Completion evidence: every numbered step can be followed without creating, viewing, recording, sharing, restoring, or funding a learner wallet or real recovery secret; the learning-only boundary appears before the procedure; and the publication source will replace the prior Resources Hub route. Confirm the deployed page as part of final publication verification.

- [ ] **ACT-023: Make every published activity usable.** Fill in or remove empty sections. Say what learners produce, what educators look for, and what to do when a device, video, website, or live tool is unavailable.

  - Status: open | Owner: unassigned | Updated: 2026-09-21 | Severity: high | Release impact: publication blocker | Evidence: [CYN-002](runs/2026-09-21-full-release-26.10-cynical.md#cynical-editor-findings) reports 130 empty H2 sections, including 19 Duration sections, across 30 published activities | Depends on: ACT-022 | Completion evidence: no released activity has an empty operational section; each activity states the learner output and educator evidence; and every dependency has a stated fallback that an educator can use without inventing missing steps.

- [ ] **ACT-024: Make Activities 001 and 002 fair and well-supported.** Separate evidence from opinion, avoid overclaiming causes, and give learners enough context to consider limits and other explanations.

  - Status: open | Owner: unassigned | Updated: 2026-09-21 | Severity: high | Release impact: publication blocker | Evidence: [CYN-003](runs/2026-09-21-full-release-26.10-cynical.md#cynical-editor-findings) identifies categorical, unsourced claims in `mfb-act-001-auction.md` and `mfb-act-002-consensus.md` | Depends on: none | Completion evidence: an independent factual reviewer can support every retained material claim, and the activities do not state universal historical, causal, or value claims beyond their evidence.

- [ ] **ACT-025: Show how the eight-hour minimum works in a real class.** Set the class size, assessor numbers, observation approach, and assessment time—or make clear that the route will not suit every setting.

  - Status: open | Owner: unassigned | Updated: 2026-09-21 | Severity: high | Release impact: required before cohort | Evidence: [CYN-004](runs/2026-09-21-full-release-26.10-cynical.md#cynical-editor-findings) calculates 32–45 observation minutes per learner against the 12-row grid and finds no stated cohort or staffing assumptions | Depends on: ACT-001 | Completion evidence: a complete schedule shows how teaching, practice, individual evidence, feedback, recording, and realistic reassessment fit the stated cohort and assessor assumptions; a field test records planned and actual timing before any certificated delivery.

- [ ] **ACT-026: Remove repeated guide content and fix `BD-V-049`.** Keep only useful recaps, move educator-only detail out of learner front matter, and remove the duplicate or mismatched visual marker and alt text.

  - Status: in-progress | Owner: unassigned | Updated: 2026-09-21 | Severity: medium | Release impact: maintenance | Evidence: [Student Guide on-chain and Lightning marker](../publish/mfb-bd-26.10/mfb-bd-sg-26.10.md#on-chain-and-lightning-payments) now has one `BD-V-049` marker with payment-path alt text; [CYN-008](runs/2026-09-21-full-release-26.10-cynical.md#cynical-editor-findings) retains the broader guide-architecture finding | Depends on: ACT-013 | Completion evidence: the duplicate and mismatched adjacent `BD-V-049` marker is removed; recap consolidation and the visual-production dependency remain open.

- [ ] **ACT-028: Produce or explicitly defer every guide visual.** Do not treat a generic design-brief template as a finished visual asset.

  - Status: open | Owner: unassigned | Reported: 2026-09-25 | Severity: high | Release impact: publication blocker | Evidence: [asset-migration alignment run](runs/2026-09-25-change-assets-alignment.md#findings-created-or-updated), [asset-migration cynical run](runs/2026-09-25-change-assets-cynical.md#cynical-editor-findings), and [asset production log](../assets/assets-list.md) show 101 generic briefs but no asset-specific references, uploads, or production packages; the guides contain 138 `ASSET` references to those brief templates | Depends on: ACT-013 and `EVO-002` for the [My First Bitcoin App](https://myfirstbitcoin.app/) QR panel | Completion evidence: every retained visual marker resolves to an approved, rendered production asset with its required alt text, rights/source record, and placement check; each deliberately deferred location is visibly marked as deferred and does not imply a finished visual.

  - Populate each retained brief from its current asset-index row, produce and review the final editable asset and export, then replace the marker only after approval. Do not produce the app QR until the identifier conflict in `EVO-002` is resolved.

- [x] **ACT-029: Repair the source-of-truth map links.** The map must not name workspace documents that do not exist.

  - Status: done | Owner: unassigned | Reported: 2026-09-25 | Completed: 2026-09-25 | Severity: medium | Release impact: maintenance | Evidence: [workspace index reading order](../workspace/00_index.md#recommended-reading-order) now links entries 22–25 to the existing [design-brief](../assets/prompts/prompt-00-brief.md), [JSON-reference](../assets/prompts/prompt-01-json.md), [JPEG-reference](../assets/prompts/prompt-02-jpg.md), and [production-asset](../assets/prompts/prompt-03-mg.md) workflow contracts; the four stale `workspace/22_`–`25_` links were removed. [Asset workflow](../workspace/08_assets.md#6-asset-workflow) confirms the JSON, JPEG, and production-contract sequence. | Depends on: none | Completion evidence: each listed entry opens the approved current document, or the index is corrected to the authoritative existing path with no stale map entry.

- [x] **ACT-030: Retire the duplicate asset style guide.** Preserve compatible guidance in the active production and review controls, then remove the obsolete working note.

  - Status: done | Owner: unassigned | Reported: 2026-09-25 | Completed: 2026-09-25 | Severity: low | Release impact: maintenance | Evidence: the obsolete `workspace/27_assets-style.md` was removed; the active [Illustration Style Guide](../assets/style/STYLE.md#1-visual-direction) now requires a clear focal point, generous negative space, and rejection of the retained note’s generic-AI artefacts; [style review control](review_style.md#prompt-6-review-structure-formatting-and-visual-support) now checks those points. [Asset-migration style run](runs/2026-09-25-change-assets-style.md#findings-created-or-updated) remains the historical finding. | Depends on: none | Completion evidence: compatible guidance is held in active controls, and no duplicate workspace style guide remains.


- [x] **ACT-027: Use the same guiding question for each module everywhere.** Align the Student Guide, Educator Guide, and relevant assessment prompts, unless a different audience version is clearly intentional.

  - Status: done | Owner: unassigned | Updated: 2026-09-21 | Severity: medium | Release impact: maintenance | Evidence: [four-module architecture](../workspace/06_plan.md#2-four-module-architecture), [Student Guide learning path](../publish/mfb-bd-26.10/mfb-bd-sg-26.10.md#learning-approach), [Educator Guide at-a-glance table](../publish/mfb-bd-26.10/mfb-bd-eg-26.10.md#the-diploma-at-a-glance), [Educator Guide Module 3](../publish/mfb-bd-26.10/mfb-bd-eg-26.10.md#9-module-3-using-bitcoin-safely), [Educator Guide Module 4](../publish/mfb-bd-26.10/mfb-bd-eg-26.10.md#10-module-4-bitcoin-in-your-community), and [specification four-module path](../workspace/16_spec.md#four-module-learning-path) | Depends on: none | Completion evidence: the Student Guide, Educator Guide summary and module openings, canonical architecture, and active specification now use the same Module 3 and Module 4 questions; no differing assessment prompt was present.

## Decision register

The following register preserves all 12 questions, alternatives, affected-file lists, and the reconciliation order from the 2026-08-19 consistency review. Its descriptions of file contents are historical evidence, not a fresh statement of current policy. Preserve the alternatives for traceability; do not ask for A/B choices already implemented.

| ID | Consolidation disposition and next step |
|---|---|
| DEC-01 | **Resolved: B.** Eight hours is the minimum and shortest planned route, with no upper limit. |
| DEC-02 | **Resolved.** Equal-status, non-compensatory theory and practical gates; no combined grade. |
| DEC-03 | **Resolved.** All four modules are required; Module 4 is educator-curated and locally relevant. |
| DEC-04 | **Resolved: A.** Required Module 3 performance is a supported demonstration. |
| DEC-05 | **Resolved: A.** Supported low-stakes or simulated first access is required; no purchase or personal funds are required. |
| DEC-06 | **Resolved: A.** Explanation/comparison is required; Lightning setup or payment practice is locally selected. |
| DEC-07 | **Resolved: A.** The October release includes everything required to teach the Diploma, including the online PDF package and website-ready source files. |
| DEC-08 | **Resolved: A.** Open source is a qualified preference and part of the learning process, not a universal wallet recommendation. |
| DEC-09 | **Resolved: A.** Keep direct, named programme links as clearly optional further learning beyond the Diploma, with weekly automated checks where possible and human-approved corrections. |
| DEC-10 | **Resolved: A.** The canonical learner manuscript is `publish/mfb-bd-26.10/mfb-bd-sg-26.10.md`. |
| DEC-11 | **Resolved.** The named educator assesses the learner, accredits the result, and distributes the certificate; it records that educator's judgment, not My First Bitcoin's direct evaluation. |
| DEC-12 | **Resolved: B.** Release the curriculum framework first and defer certification-complete claims until the remaining operational requirements are ready. |

For each unresolved choice, record the decision owner, approved answer, date, rationale, and affected files. The source accepts responses by question number and A/B choice, such as `1A, 2B, 3A`; map these to the corresponding `DEC` IDs and request choices only for genuinely unresolved questions. Check off its linked action only after all required dependent files agree. The register does not authorize policy changes.

### DEC-01: Is eight hours a fixed Diploma boundary or a planning baseline?

**Status: resolved (B) | Owner: project lead | Approved: 2026-09-21.** Eight hours is the minimum and shortest planned route, not a maximum. There is no upper limit: educators should take the time their learners need to explore, discuss, practise, and consolidate their learning. The active rule is recorded in the [competency framework](../workspace/05_competencies.md:22), [scope](../workspace/03_scope.md:52), and [Educator Guide](../publish/mfb-bd-26.10/mfb-bd-eg-26.10.md:603).

Teacher feedback found the former fixed eight-hour model too short. Eight hours is now the minimum route. Educators may require accessible Student Guide pre-reading to preserve live time for activities and discussion, but pre-reading does not count toward the minimum or replace required educator-supported learning and assessment. The former conflict is retained here as decision history.

**A. Fixed boundary.** Keep eight hours as the maximum complete learner-contact time. Reduce, combine, or move competencies and required evidence until the complete course, including reassessment, fits.

**B. Planning baseline.** Keep the present competency set and treat eight hours as the shortest planned route; require longer scheduled delivery where cohort size, access needs, practice, observation, or reassessment demand it.

**Approved answer: B**, strengthened to establish eight hours as a minimum with no upper limit.

Affected: `05_competencies.md`, `03_scope.md`, `06_plan.md`, `02_research.md`, `../publish/mfb-bd-26.10/mfb-bd-sg-26.10.md`, the [Educator Guide](../publish/mfb-bd-26.10/mfb-bd-eg-26.10.md), `13_assessment.md`, `16_spec.md`.

### DEC-02: Does “50% / 50%” describe a score or two completion gates?

**Status: resolved | Reviewed: 2026-09-21.** Current implementation retains two non-compensatory components and no combined grade. Evidence: [overview:183](../workspace/16_spec.md:183) and [overview:190](../workspace/16_spec.md:190).

**Resolved.** The 50/50 wording describes two equal-status, non-compensatory completion gates: theoretical competency (`C1`–`C8`) and practical competency (`C9`–`C11`). Every required competency and safety criterion must meet standard. The Diploma does not calculate or report a combined numerical grade unless a separate reporting rule is approved.

Affected: `05_competencies.md`, `06_plan.md`, `13_assessment.md`, `15_certification.md`, `16_spec.md`, public materials.

### DEC-03: Is Module 4 part of the Diploma?

**Status: resolved | Reviewed: 2026-09-21.** Current publications require all four modules and define Module 4 as educator-curated. Evidence: [Student Guide:224](../publish/mfb-bd-26.10/mfb-bd-sg-26.10.md:224) and [assessment grid:27](../publish/mfb-bd-26.10/mfb-bd-assessment-grid-26.10.md:27).

**Resolved.** The Diploma consists of Modules 1–4. Modules 1 and 2 develop theory-based competencies through explanation, comparison, and reasoning; Modules 3 and 4 develop practical competencies through supported action. Module 4 is selected locally, but it is required for Diploma completion. Advanced Learning is outside the Diploma.

All source-of-truth and public documents must use this model. Do not describe Module 4 as optional or outside the Diploma.

Affected: `00_index.md`, `04_design.md`, `05_competencies.md`, `06_plan.md`, `../publish/mfb-bd-26.10/mfb-bd-sg-26.10.md`, the [Educator Guide](../publish/mfb-bd-26.10/mfb-bd-eg-26.10.md), `13_assessment.md`, `15_certification.md`, `16_spec.md`.

### DEC-04: What must the Module 3 learner promise say?

**Status: resolved (A) | Reviewed: 2026-09-21.** The learner promise and direct-observation route require safe supported performance. Evidence: [Student Guide:124](../publish/mfb-bd-26.10/mfb-bd-sg-26.10.md:124) and [assessment grid:35](../publish/mfb-bd-26.10/mfb-bd-assessment-grid-26.10.md:35).

`06_plan.md` promises demonstration of wallet, transaction, verification, recovery-readiness, and safety actions. `05_competencies.md` requires several directly observed performances. `16_spec.md` says learners can only “identify” basic safety practices, which understates the assessed standard.

**A. Demonstrate safely under support.** Use one consistent learner promise: beginners demonstrate specified wallet, transaction, verification, recovery-readiness, and safety actions in an approved supported, simulated, testnet, or low-stakes environment.

**B. Identify and explain only.** Reframe Module 3 certification around observable explanation and safety judgment; move hands-on demonstrations out of required Diploma certification.

Affected: `05_competencies.md`, `06_plan.md`, `../publish/mfb-bd-26.10/mfb-bd-sg-26.10.md`, the [Educator Guide](../publish/mfb-bd-26.10/mfb-bd-eg-26.10.md), `13_assessment.md`, `15_certification.md`, `16_spec.md`.

### DEC-05: Is first access to bitcoin a required Module 3 competency?

**Status: resolved (A) | Reviewed: 2026-09-21.** `C9` requires supported access and receipt while allowing simulation, testnet, physical tokens, or low-stakes funds. Evidence: [assessment grid:23](../publish/mfb-bd-26.10/mfb-bd-assessment-grid-26.10.md:23) and [assessment grid:35](../publish/mfb-bd-26.10/mfb-bd-assessment-grid-26.10.md:35).

`C9.3` requires a learner to gain access to bitcoin through an approved low-stakes or simulated pathway, receive it, and check relevant information. Elsewhere the learner-facing material says learners do not need to buy bitcoin, install a wallet, or use meaningful personal funds. These can coexist only if the exact minimum experience is explicit.

**A. Required simulated or low-stakes first access.** Every certificated learner completes `C9.3`; a prepared wallet, test environment, educator-provided training balance, or no-value simulation is sufficient, and no purchase or personal funds are required.

**B. Optional first access.** Remove `C9.3` as a required competency criterion; certification requires safe wallet navigation and a receive/send simulation, but not access to bitcoin.

Affected: `05_competencies.md`, `../publish/mfb-bd-26.10/mfb-bd-sg-26.10.md`, the [Educator Guide](../publish/mfb-bd-26.10/mfb-bd-eg-26.10.md), `13_assessment.md`, `15_certification.md`, and activities on the [Resources Hub](https://programs.myfirstbitcoin.org/resources/).

### DEC-06: What is the required Diploma learning for Lightning?

**Status: resolved (A) | Reviewed: 2026-09-21.** All learners compare payment paths; detailed setup and live practice are Advanced or locally selected Module 4 work. Evidence: [Student Guide:1274](../publish/mfb-bd-26.10/mfb-bd-sg-26.10.md:1274) and [Educator Guide:2247](../publish/mfb-bd-26.10/mfb-bd-eg-26.10.md:2247).

`06_plan.md` places Lightning setup and payment practice in locally selected Module 4 variants, but `C8.1`, the Student Guide, and assessment requirements place the on-chain/Lightning distinction in Module 3. The boundary between required explanation and required use should be stated once.

**A. Required Diploma explanation; locally selected Module 4 practice.** Every learner compares on-chain and Lightning in a guided scenario; Lightning setup, invoices, and payments are only selected Module 4 practice.

**B. Required supported use.** Every learner completes an approved Lightning receive/send exercise in Module 3; Module 4 may deepen or localize it.

Affected: `05_competencies.md`, `06_plan.md`, `07_contents.md`, `../publish/mfb-bd-26.10/mfb-bd-sg-26.10.md`, activities on the [Resources Hub](https://programs.myfirstbitcoin.org/resources/), the [Educator Guide](../publish/mfb-bd-26.10/mfb-bd-eg-26.10.md), `13_assessment.md`, `../publish/mfb-lx-26.10.md`, `16_spec.md`.

### DEC-07: Are online PDF, website-ready content, and future branches October deliverables?

**Status: resolved and implemented (A) | Owner: project lead | Approved: 2026-09-21.** Everything required to teach the Diploma must be published in the 2026.10 timeframe. This includes the online PDF package and website-ready source files. Project-wide reconciliation is complete under `ACT-015`.

The historical conflict grouped online PDF and web publication with future online-cohort, self-paced, optional-app, and cross-modal instructional branches. The current authorities now separate them: the PDF/web formats are October Sanity outputs, while the instructional branches remain future work.

**A. October deliverables.** Include an online PDF package and website-ready source files in the release completion criteria, with the same competency requirements and assessment safeguards.

**B. Future branch preparation.** Release the complete low-tech print/PDF and educator-led pathway in October; retain only branch notes, source readiness, and design constraints for online/web formats.

**Approved answer: A.** Publication formats required to teach the Diploma are October deliverables; this does not make future online-cohort, self-paced, app-supported, or cross-modal instructional branches current deliverables.

Affected: `03_scope.md`, `04_design.md`, `06_plan.md`, `../publish/mfb-bd-26.10/mfb-bd-sg-26.10.md`, the [Educator Guide](../publish/mfb-bd-26.10/mfb-bd-eg-26.10.md), `16_spec.md`, `18_horizon.md`.

### DEC-08: How strict is the learner-facing “open-source wallet” guidance?

**Status: resolved and implemented (A) | Owner: project lead | Approved: 2026-09-21.** Open-source wallet software is a preference, not a universal recommendation or automatic answer. The educator helps learners navigate the decision, understand wallet trade-offs, and identify how transparent or inspectable the software is. The policy is aligned in the Student Guide, Educator Guide, Quick Start, public materials, and affected wallet activities. The programme-link portion of `ACT-006` is also closed by resolved `DEC-09`.

`06_plan.md` includes an “open-source wallet preference” in Diploma safety content. The workspace also prohibits global tool recommendations and places detailed wallet-design considerations in Advanced. A preference can sound like a universal recommendation unless its purpose and limit are defined.

**A. Keep a general preference.** Teach that learners can consider whether wallet software is openly inspectable, alongside custody, recovery, safety, compatibility, and local support; do not name a global preferred wallet.

**B. Move it out of the learner Diploma.** Keep wallet open-source evaluation as educator/Advanced context and teach Diploma learners only the custody, recovery, verification, and safety criteria needed for beginner use.

**Approved answer: A.** Open-source evaluation remains part of the learner experience, while the final wallet choice is a contextual judgment based on needs and trade-offs. Do not designate a particular wallet as the global recommendation.

Affected: `06_plan.md`, `05_competencies.md`, `../publish/mfb-bd-26.10/mfb-bd-sg-26.10.md`, activities on the [Resources Hub](https://programs.myfirstbitcoin.org/resources/), the [Educator Guide](../publish/mfb-bd-26.10/mfb-bd-eg-26.10.md), `../publish/mfb-lx-26.10.md`, `17_advanced.md`.

### DEC-09: Is named programme-pathway promotion part of the Student Guide?

**Status: resolved and implemented (A) | Owner: project lead | Approved: 2026-09-21.** The Student Guide may retain direct links to selected My First Bitcoin programmes as clearly optional further learning beyond the Diploma. Learners do not need those programmes or links for completion; they need the Student Guide, an educator, and the materials and resources the educator specifies. The Educator Guide should provide a more detailed optional-pathways list, while placing it in a back appendix remains an editorial option rather than a requirement.

The Student Guide directs learners to specific My First Bitcoin programmes and public webpages. The publication guardrails otherwise emphasize durable offline material, sparse QR codes, and avoiding fragile or named-service dependencies. This needs an explicit publication policy rather than an accidental exception.

**A. Keep a short, curated pathways section.** Retain named My First Bitcoin next steps and links, but make them optional, date-checked, and available as a plain-text offline reference.

**B. Keep the Student Guide programme-neutral.** Remove named pathways and live links from learner chapters; place changing programme navigation on a maintained update page or educator handout.

**Approved answer: A.** Link directly to each selected programme rather than requiring one central landing page. Where operationally possible, a bot or agent checks the two link registers weekly, updates check metadata, and raises alerts; only a human may approve a correction, replacement, or removal. A failed optional further-learning link is not a publication blocker, but it requires an important alert and a human-approved solution within 24 hours. Learner-facing materials do not need to state ETP technology requirements beside every ETP link. The low-tech, offline-capable commitment applies to Diploma learners; educator training may require access to a mobile device, computer, and internet connection.

Affected: `06_plan.md`, `../publish/mfb-bd-26.10/mfb-bd-sg-26.10.md`, `09_resources.md`, the [Educator Guide](../publish/mfb-bd-26.10/mfb-bd-eg-26.10.md), `16_spec.md`.

### DEC-10: Which learner manuscript is the canonical file name?

**Status: resolved (A) | Reviewed: 2026-09-21.** The official-document map names the existing canonical file. Evidence: [workspace index:17](../workspace/00_index.md:17) and [repository guidance](../AGENTS.md:12).

The repository guidance assigns learner-facing prose to `workspace/../publish/mfb-bd-26.10/mfb-bd-sg-26.10.md`, but the active index, source-of-truth map, and workspace use `../publish/mfb-bd-26.10/mfb-bd-sg-26.10.md`. This is a maintenance and publishing ambiguity rather than a curriculum disagreement.

**A. Standardize on `../publish/mfb-bd-26.10/mfb-bd-sg-26.10.md`.** Update the repository guidance and any stale references to name the existing Student Guide file.

**B. Standardize on `../publish/mfb-bd-26.10/mfb-bd-sg-26.10.md`.** Rename or migrate the Student Guide to the repository-guideline filename and update the index and links.

Affected: `AGENTS.md`, `00_index.md`, `06_plan.md`, `07_contents.md`, `../publish/mfb-bd-26.10/mfb-bd-sg-26.10.md`, the [Educator Guide](../publish/mfb-bd-26.10/mfb-bd-eg-26.10.md), `../publish/mfb-lx-26.10.md`, `16_spec.md`.

### DEC-11: Is a certificate a 2026.10 operational output or a governed future implementation?

**Status: resolved and implemented | Owner: project lead | Approved: 2026-09-21.** The educator assesses the learner, accredits the result, and distributes the certificate. Because the My First Bitcoin Education Network is decentralized, My First Bitcoin does not evaluate the learner. A certificate represents certification by the named educator, not direct certification or a competency guarantee from My First Bitcoin. Project-wide publication reconciliation is complete under `ACT-017` and `ACT-020`; proportionate local record and safeguarding readiness remains tracked separately under `ACT-003`.

The assessment and certification documents define a mandatory prerequisite and issuance workflow, while `03_scope.md` leaves certificate governance, identity, verification, and infrastructure out of scope. Public wording needs to avoid promising an operational credential system before its owner and controls exist.

**A. Certificate issuance is part of 2026.10.** Add a minimum issuer, approval, record, correction, privacy, and verification process to October completion requirements.

**B. Assessment-complete is the October curriculum output.** Keep the certification prerequisite and public claim, but defer actual issuance and verification implementation until governed separately; do not imply that a credential service is already available.

**Approved answer: decentralized educator issuance.** This supersedes the A/B framing where it implies central issuance or evaluation. Educators may issue certificates under the approved assessment process; My First Bitcoin does not centrally evaluate learners or attest their competency.

Affected: `03_scope.md`, the [Educator Guide](../publish/mfb-bd-26.10/mfb-bd-eg-26.10.md), `13_assessment.md`, `15_certification.md`, `16_spec.md`, `18_horizon.md`, public materials.

### DEC-12: Should the first release include timed, certification-complete activities?

**Status: resolved and implemented (B) | Owner: project lead | Approved: 2026-09-21.** Release the curriculum framework first. The [operational assessment protocol](../publish/mfb-bd-26.10/mfb-bd-eg-26.10.md:47) exists, but calibration and local governance evidence remain incomplete under `ACT-002` and `ACT-003`. The project now distinguishes publication from readiness for certificated delivery under `ACT-017`.

The Educator Guide operational assessment protocol now supplies approved theory interactions, direct observation tasks, rubrics, records, support rules, and equivalent routes for every competency. It still requires delivery validation, local `P11` variant approval, calibration examples, and record-governance controls before certificated delivery.

**A. Release only when operational.** Make certification-complete activities (competency-to-evidence crosswalk, approved tasks, rubrics, records, variants, and educator calibration) a release dependency.

**B. Release the curriculum framework first.** Publish the Student and Educator guides as a provisional teaching package; defer certification claims and assessment-complete status until the required activities are operational.

**Approved answer: B.** The first release is a curriculum framework and teaching package, not a claim that every certification-complete operational dependency has been finished.

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

#### EVO-001: October publication-output scope is consolidated

Status: done | Owner: project lead | Updated: 2026-09-21 | Severity: high | Release impact: publication blocker resolved | Evidence: [full-release alignment run](runs/2026-09-21-full-release-alignment.md#findings-created-or-updated); `workspace/03_scope.md`, `workspace/04_design.md`, `workspace/06_plan.md`, `workspace/16_spec.md`, `workspace/18_horizon.md`, and public release wording now define the offline print/PDF package, online PDF, and website-ready Sanity content as October outputs while reserving online-cohort, self-paced, optional-app, and cross-modal instructional branches for future work | Depends on: none | Completion evidence: affected authority and public wording use one approved October output boundary.

Earlier file/heading: `workspace/06_plan.md`, `## 3. Legacy Content Migration` and `## 8. October 2026 Output` | Later file/heading: `workspace/03_scope.md`, `## 15. Publishing System`; `workspace/16_spec.md`, `## Materials And Outputs` | Historical issue: authorities disagreed on whether online PDF and web outputs were October deliverables or future branches | Resolution: `DEC-07` makes them October publication outputs through Sanity, while online-cohort, self-paced, optional-app, and cross-modal instructional branches remain future work | Evidence: `ACT-015` and the aligned affected files above.

#### EVO-002: The [My First Bitcoin App](https://myfirstbitcoin.app/) QR asset identifier conflicts

Status: open | Owner: unassigned | Reported: 2026-09-25 | Severity: high | Release impact: publication blocker | Evidence: [repository guidance](../AGENTS.md), which requires `BD-V-075` for the [My First Bitcoin App](https://myfirstbitcoin.app/) QR; [asset index](../workspace/08_assets.md#2-visual-index), which assigns that QR to `BD-V-076` and defers `BD-V-075`; and [asset-migration alignment run](runs/2026-09-25-change-assets-alignment.md#findings-created-or-updated) | Depends on: none | Completion evidence: one authorized asset ID and placement rule is recorded in every governing source, and every guide marker, brief, production record, and related reference uses it consistently.

Earlier file/heading: repository guidance, [My First Bitcoin App](https://myfirstbitcoin.app/) QR rule | Later file/heading: `workspace/08_assets.md`, `## 2. Visual index`, `BD-V-075` and `BD-V-076` | Issue: the higher-priority repository rule requires `BD-V-075` for the app QR, but the new asset index reserves that ID for a deferred certificate-verification concept and changes the active QR to `BD-V-076` | Why it matters: production can create, place, or verify the wrong QR asset and violate the publication guardrail | Authority/evidence: the sources above conflict directly | Affected files: `workspace/08_assets.md`, both guides, `assets/briefs/bd-v-075-brief.md`, `assets/briefs/bd-v-076-brief.md`, and `assets/assets-list.md` | Recommended action: obtain an authorized reconciliation, update the governing source first, then update all dependent markers and production records through `ACT-028`.

#### EVO-003: Link-register maintenance references have not migrated to `links/`

Status: open | Owner: unassigned | Reported: 2026-09-30 | Severity: high | Release impact: publication blocker | Evidence: [alignment control](review_alignment.md#prompt-11-reconcile-findings-and-validate-the-result) now assigns canonical maintenance to [links/links-internal.md](../links/links-internal.md) and [links/links-external.md](../links/links-external.md); `workspace/20_links-internal.md` and `workspace/20_links-external.md` do not exist | Depends on: ACT-009 | Completion evidence: all active maintenance references and cross-links resolve to the two canonical registers, which accurately classify and inventory retained links.

Earlier file/heading: the current repository layout, `links/links-internal.md` and `links/links-external.md` | Later file/heading: `workspace/00_index.md`, `## Recommended reading order`; `workspace/09_resources.md`, introduction; `workspace/18_horizon.md`, link-review process; `links/links-internal.md`, introduction; and `links/links-external.md`, introduction | Issue: active documents and the registers' reciprocal links still refer to nonexistent `workspace/20_links-internal.md` or `workspace/20_links-external.md` paths, while the canonical register files are in `links/` | Why it matters: reviewers and automated maintenance can follow broken paths, omit the canonical inventory, or fail to keep new links in the correct register | Authority/evidence: the 2026-09-30 link-maintenance direction and the existing `links/` files | Affected files: `workspace/00_index.md`, `workspace/09_resources.md`, `workspace/18_horizon.md`, `links/links-internal.md`, `links/links-external.md`, and active review controls or current run templates that cite the obsolete paths | Recommended action: update active references and reciprocal links to `links/links-internal.md` or `links/links-external.md`, preserve historical run records as provenance, then verify the classifications, source locations, and review metadata under `ACT-009`.

#### PUB-001: Certificate wording now reflects educator-issued certification

Status: done | Owner: project lead | Updated: 2026-09-21 | Severity: high | Release impact: publication blocker resolved | Evidence: [full-release alignment run](runs/2026-09-21-full-release-alignment.md#findings-created-or-updated); the Student Guide now uses `### Certificate meaning and issuer`; `workspace/15_certification.md` defines decentralized educator issuance and the framework-first boundary; `BD-V-075` is deferred with no 2026.10 placement | Depends on: none | Completion evidence: learner-facing wording no longer implies a central My First Bitcoin verification process.

Governing workspace file/heading: `workspace/15_certification.md`, `## Current Governance And Future Options`; `workspace/16_spec.md`, `## Assessment And Certification` | Publication file/heading: `publish/mfb-bd-26.10/mfb-bd-sg-26.10.md`, `### Certificate meaning and issuer` | Historical issue: conditional instructions implied a future central verification route without an approved service | Resolution: the publication now explains educator issuance, My First Bitcoin's non-central role, and optional issuer-specific verification only; `BD-V-075` is not a current production asset | Evidence: `ACT-017`, `ACT-020`, and the aligned files above.

#### PUB-002: Publication coverage omits non-beginner and quick-start files

Status: needs-verification | Owner: unassigned | Updated: 2026-09-21 | Severity: medium | Release impact: publication blocker | Evidence: [full-release alignment run](runs/2026-09-21-full-release-alignment.md#findings-created-or-updated) and [CYN-007](runs/2026-09-21-full-release-26.10-cynical.md#cynical-editor-findings); the Quick Start is now classified in `workspace/19_publication-coverage.md`, but `publish/mfb-adv-26.10/mfb-adv-001` through `mfb-adv-008` remain absent | Depends on: ACT-019 | Completion evidence: every file under `publish/` has an explicit current-release, deferred, or non-public status and appears in the coverage register where required.

Governing workspace file/heading: `workspace/19_publication-coverage.md`, `## Diploma publication set` and `## Maintenance check`; `workspace/17_advanced.md`, `## 1. Status And Use` | Publication file/heading: `publish/mfb-adv-26.10/mfb-adv-001-history-of-money-localisation.md` through `mfb-adv-008-building-on-bitcoin.md` | Issue: publication inventory and actual files still disagree for the eight Advanced files; the Quick Start omission is resolved | Why it matters: release tooling, reviewers, translators, and users may treat Advanced drafts as approved publication or fail to maintain files that are in scope | Authority/evidence: `workspace/19_publication-coverage.md` says every curriculum-content file in `publish/` must appear once; `publish/mfb-adv-26.10/README.md` says Advanced modules are future | Affected files: `workspace/19_publication-coverage.md`, `workspace/00_index.md`, `workspace/17_advanced.md`, `publish/mfb-adv-26.10/README.md`, and eight Advanced files | Recommended action: record explicit deferred/non-release status and owner for the Advanced files before release.

## Historical report baseline and verification limits

The report is dated 2026-09-01. It assessed the design as coherent and suitable for continued editing and non-certificated teaching development, but not ready for certificated delivery until validation, calibration, local tasks, and governance were complete. That is a historical assessment to verify, not a new readiness determination.

The report cross-read the active workspace authorities, Student Guide, Educator Guide, Assessment Grid, optional self-assessment materials, and live reviews. It replaced a mixed historical audit and explicitly was not a source of curriculum policy. Its recommendation was to validate and simplify the existing system rather than add curriculum topics. It also noted that the Student Guide now explained educator observation, feedback, and reassessment.

Preserve its category meanings: **implemented** means present in source files; **release blocker** means required before certificated delivery; **publication decision** means an owner decision is needed before settling public copy or scope; and **maintenance action** improves accuracy, usability, or editing without by itself blocking a teaching draft. Record/certificate governance blocks certification and pilots retaining results, not use of the curriculum as a teaching package.

It recorded these implemented points: all four modules and required `C11`; educator theory `C1`–`C8` and direct observation `C9`–`C11`; an operational protocol with crosswalk, `T1`–`T3`, `P9`–`P11`, support limits, safety-critical errors, equivalents, reassessment, calibration, and moderation; the Bitcoin/stablecoin/other-crypto comparison and responsible-learning boundary; supported simulated or low-stakes `C9.3`; no purchase, meaningful personal funds, secrets, personal device, or app requirement; optional self-check/recap/discovery only; and separate index roles for the microlearning plan and published data.

The report found six registered sources and mutable occurrence/line references against a then 1,549-line Student Guide. Those are historical counts explaining the source-maintenance task, not current measurements. Expand economic, historical, technical, security, and current-context source coverage; keep shared claims distinct from local verification.

Its local-link audit across `workspace/`, `publish/`, `review/`, and `README.md` found 162 targets and one missing Creative Commons visual, `assets/briefs/bd-v-001-brief.md`. The asset register was a design brief, not an inventory of produced assets. It confirmed the operational protocol, digital-asset comparison, removal of educator app-scoring/assessment claims, and separate microlearning index roles. It did not validate external links, current claims, rendered output, screen-reader behavior, or real-cohort delivery.

The report replaced a mixed 19 August snapshot and implementation update that had continued to show completed or superseded findings as active. It retired earlier findings about missing `C5` content, needing to build the crosswalk/protocol, app-scoring and certification regressions, optional Module 4 wording, duplicated microlearning roles, former broken-link counts/deleted filenames, and mixed historical audit/author-question tables. Do not reactivate those findings without a current regression. The old report deliberately excluded untriaged handwritten notes from active work.

### Report-to-action and file map

This map preserves all eight report action areas and their primary-file references. Paths in code are relative to the repository root. Resolve old review-file references to the consolidated sections here for new work; keep originals as provenance.

| Report action | Consolidated action IDs | Primary files or sections |
|---|---|---|
| 1. Validate certificated delivery | ACT-001, ACT-002 | [Educator Guide](../publish/mfb-bd-26.10/mfb-bd-eg-26.10.md), [Assessment Grid](../publish/mfb-bd-26.10/mfb-bd-assessment-grid-26.10.md), `workspace/13_assessment.md`, `workspace/03_scope.md`. |
| 2. Approve minimum record and certificate governance | ACT-003, ACT-005, ACT-017 | `workspace/15_certification.md`, `workspace/13_assessment.md`, `workspace/03_scope.md`, Student Guide back matter. |
| 3. Implement scope decisions and the programme-link policy | ACT-006, ACT-015, ACT-017 | Preserve resolved `DEC-01`, `DEC-07`–`DEC-09`, `DEC-11`, and `DEC-12`; include `workspace/04_design.md` and `workspace/16_spec.md` in output reconciliation. |
| 4. Make Student Guide back matter publication-ready | ACT-008, ACT-009 | [Student Guide](../publish/mfb-bd-26.10/mfb-bd-sg-26.10.md), `workspace/07_contents.md`, `workspace/08_assets.md`, `workspace/15_certification.md`. |
| 5. Repair source and terminology maintenance | ACT-010 | `workspace/09_resources.md`, [Lexicon](../publish/mfb-lx-26.10.md), Educator Guide local verification record. |
| 6. Triage remaining consistency decisions | ACT-014 | This action list, decision register, and annotation inventory; formerly maintained in the archived review register. |
| 7. Finish the optional self-check | ACT-011 | [Published self-check](../publish/mfb-ml-26.10/mfb-ml-26.10.md), `workspace/14_microlearning-plan.md`. |
| 8. Fix local-link failure and control visuals | ACT-012, ACT-013 | `workspace/08_assets.md`, `assets/briefs/bd-v-001-brief.md`, essential-visual production tracker. |

## Complete historical annotation inventory

Every one of the original backlog's bullet items is retained below in its original order and section context. `ANN` IDs are stable references. The original `[o]`, `[-]`, or `[ ]` marker appears as provenance, not as a completion claim. Project history provides these possible meanings from the Student Guide editing pass recorded in commit `561d113`: `[x]` = added to the current student text; `[o]` = not possible in that student-text pass; `[-]` = no change needed; `[ ]` = unclear or still requires confirmation. Treat these as contextual historical meanings, not current approval or status. All new checkboxes mean **triage this note**, not **implement this request**.

To complete triage, compare the note with the current source, then record `already-addressed`, `approved-action`, `rejected`, `superseded`, `duplicate`, `preserve-approval`, or `needs-clarification`, with evidence and a linked action where needed. Preserve literal approvals as approvals. For unclear handwriting, require the source image or author clarification. Do not infer unavailable wording or treat an uncertain name as an assignment.

Source provenance: the original backlog identifies `input/PABLO/202602721_final_draft_notes.md` and says source items marked `[x]` were excluded. This consolidation preserves all items actually present in `review/`; it does not claim to recover excluded source notes. Later-page numbering differences between Claude and Codex readings require checking the PDF images. The source's references to `00_todo.md` are historical; use this register for the new workflow.

For item locations, use current source heading anchors after matching the inherited section labels. Some historical section titles no longer match current headings. Repeated proposals, handwriting reminders, and approvals are retained separately to avoid losing evidence, but should link to one implementation task when they refer to the same work.

### Global actions

- [x] **ANN-001** (source marker `[o]`) Create a consistent visual system for graphics, diagrams, tables, examples, activities, educator guidance, glossary terms, and advanced content. — Disposition: `already-addressed` | Reviewed: 2026-09-21 | Evidence: [project ownership and official-document map](../workspace/00_index.md:17)
- [x] **ANN-002** (source marker `[o]`) Build a glossary/lexicon; define marked terms before or at first use and use consistent beginner language. — Disposition: `already-addressed` | Reviewed: 2026-09-21 | Evidence: [project ownership and official-document map](../workspace/00_index.md:17)
- [x] **ANN-003** (source marker `[o]`) Separate student content from educator guidance; create an educator guide/toolkit where marked. — Disposition: `already-addressed` | Reviewed: 2026-09-21 | Evidence: [project ownership and official-document map](../workspace/00_index.md:17)
- [x] **ANN-004** (source marker `[-]`) Treat Modules 1–4 as the required Diploma. Keep Module 4 locally selected, with educator-facing templates and local variants. — Disposition: `already-addressed` | Reviewed: 2026-09-21 | Evidence: [project ownership and official-document map](../workspace/00_index.md:17)
- [x] **ANN-005** (source marker `[o]`) Add graphics and worked/local examples for abstract money, banking, mining, wallet, transaction, and payment concepts. — Disposition: `already-addressed` | Reviewed: 2026-09-21 | Evidence: [project ownership and official-document map](../workspace/00_index.md:17)
- [x] **ANN-006** (source marker `[o]`) Give every exercise a format, duration, purpose, facilitator instructions, expected evidence/output, and writing space where needed. — Disposition: `superseded` | Reviewed: 2026-09-21 | Evidence: [project ownership and official-document map](../workspace/00_index.md:17)
- [x] **ANN-007** (source marker `[o]`) Fact-check economic, banking, Bitcoin, security, legal, and technical claims with qualified reviewers. — Disposition: `approved-action` | Reviewed: 2026-09-21 | Evidence: [recurring publication checks](review_todo.md:404) | Linked action: [ACT-019](#act-019-complete-the-final-publication-verification-pass)
- [x] **ANN-008** (source marker `[o]`) Create and maintain a public Diploma web page as well as the public GitHub repository. — Disposition: `approved-action` | Reviewed: 2026-09-21 | Evidence: [publishing scope](../workspace/03_scope.md:340) | Linked action: [ACT-015](#act-015-reconcile-october-publication-outputs)
- [x] **ANN-009** (source marker `[o]`) Maintain a stable, current reference so educators do not have to independently re-research the material for every cohort. — Disposition: `approved-action` | Reviewed: 2026-09-21 | Evidence: [resource-register maintenance requirement](../workspace/09_resources.md:1) | Linked action: [ACT-010](#act-010-replace-mutable-source-and-terminology-locations)
- [x] **ANN-010** (source marker `[-]`) Preserve literal approval marks separately from requested changes so approved material is not accidentally rewritten. — Disposition: `preserve-approval` | Reviewed: 2026-09-21 | Evidence: [project ownership and official-document map](../workspace/00_index.md:17)
- [x] **ANN-011** (source marker `[o]`) Resolve later-page numbering differences between the Claude and Codex readings directly against the PDF images. — Disposition: `needs-clarification` | Reviewed: 2026-09-21 | Evidence: [annotation provenance and confirmation rule](review_todo.md:510)

### Welcome To The Bitcoin Diploma

#### About Us

- [x] **ANN-012** (source marker `[o]`) Have AI and three humans review “Our work is independent and community driven…” — Disposition: `approved-action` | Reviewed: 2026-09-21 | Evidence: [recurring publication checks](review_todo.md:404) | Linked action: [ACT-019](#act-019-complete-the-final-publication-verification-pass)
- [x] **ANN-013** (source marker `[ ]`) Confirm whether the opening strike/brace means revise/delete “Education must come first” and/or the following paragraph. — Disposition: `needs-clarification` | Reviewed: 2026-09-21 | Evidence: [annotation provenance and confirmation rule](review_todo.md:510)

#### Our mission: independent, open-source Bitcoin education

- [x] **ANN-014** (source marker `[-]`) Add a public/GitHub process for questions, corrections, and improvements. — Disposition: `already-addressed` | Reviewed: 2026-09-21 | Evidence: [Student Guide introduction](../publish/mfb-bd-26.10/mfb-bd-sg-26.10.md:20)
- [x] **ANN-015** (source marker `[-]`) Use the Community paragraph as an explicit opportunity to connect learners. — Disposition: `already-addressed` | Reviewed: 2026-09-21 | Evidence: [Student Guide introduction](../publish/mfb-bd-26.10/mfb-bd-sg-26.10.md:20)

### How This Diploma Works

#### What learners will be able to explain and demonstrate by the end

- [x] **ANN-016** (source marker `[-]`) Support or soften the claim that bitcoin can be used in a local community. — Disposition: `already-addressed` | Reviewed: 2026-09-21 | Evidence: [Student Guide course setup and boundaries](../publish/mfb-bd-26.10/mfb-bd-sg-26.10.md:109)
- [x] **ANN-017** (source marker `[-]`) Reconsider the competency heading/framing and whether it is meaningful for one eight-hour module. — Disposition: `superseded` | Reviewed: 2026-09-21 | Evidence: [Student Guide course setup and boundaries](../publish/mfb-bd-26.10/mfb-bd-sg-26.10.md:109)
- [x] **ANN-018** (source marker `[-]`) Replace or clarify “recovery phrase.” — Disposition: `already-addressed` | Reviewed: 2026-09-21 | Evidence: [Student Guide course setup and boundaries](../publish/mfb-bd-26.10/mfb-bd-sg-26.10.md:109)

#### Learning style: in-person preferred, discussion, reflection, practice, and guided activities

- [x] **ANN-019** (source marker `[-]`) Use one simple learner checklist instead of duplicating competency statements. — Disposition: `superseded` | Reviewed: 2026-09-21 | Evidence: [Student Guide course setup and boundaries](../publish/mfb-bd-26.10/mfb-bd-sg-26.10.md:109)
- [x] **ANN-020** (source marker `[-]`) Show creator/editor accountability and transparent GitHub history. — Disposition: `already-addressed` | Reviewed: 2026-09-21 | Evidence: [Student Guide course setup and boundaries](../publish/mfb-bd-26.10/mfb-bd-sg-26.10.md:109)
- [x] **ANN-021** (source marker `[-]`) Apply the five-step learning rhythm consistently. — Disposition: `already-addressed` | Reviewed: 2026-09-21 | Evidence: [Student Guide course setup and boundaries](../publish/mfb-bd-26.10/mfb-bd-sg-26.10.md:109)

#### Participation expectations

- [x] **ANN-022** (source marker `[-]`) Make educator assessment/evidence guidance explicit. — Disposition: `already-addressed` | Reviewed: 2026-09-21 | Evidence: [Student Guide course setup and boundaries](../publish/mfb-bd-26.10/mfb-bd-sg-26.10.md:109)
- [x] **ANN-023** (source marker `[-]`) Give “Basic reading and everyday arithmetic” a clear topic heading. — Disposition: `already-addressed` | Reviewed: 2026-09-21 | Evidence: [Student Guide course setup and boundaries](../publish/mfb-bd-26.10/mfb-bd-sg-26.10.md:109)
- [x] **ANN-024** (source marker `[o]`) Link required materials to the teacher/[ETP](https://etp.myfirstbitcoin.org/) checklist and resources. — Disposition: `already-addressed` | Reviewed: 2026-09-21 | Evidence: [Student Guide course setup and boundaries](../publish/mfb-bd-26.10/mfb-bd-sg-26.10.md:109)
- [x] **ANN-025** (source marker `[o]`) Make device-practice rules a linked one-page checklist. — Disposition: `already-addressed` | Reviewed: 2026-09-21 | Evidence: [Student Guide course setup and boundaries](../publish/mfb-bd-26.10/mfb-bd-sg-26.10.md:109)
- [x] **ANN-026** (source marker `[-]`) Review example diversity; one annotated example was flagged as a male software engineer. — Disposition: `already-addressed` | Reviewed: 2026-09-21 | Evidence: [Student Guide course setup and boundaries](../publish/mfb-bd-26.10/mfb-bd-sg-26.10.md:109)

#### Safety, responsibility, and no financial advice

- [x] **ANN-027** (source marker `[-]`) Rework/qualify the “Diploma is for education” disclaimer wording. — Disposition: `already-addressed` | Reviewed: 2026-09-21 | Evidence: [Student Guide course setup and boundaries](../publish/mfb-bd-26.10/mfb-bd-sg-26.10.md:109)
- [x] **ANN-028** (source marker `[-]`) Review the marked sentence about Bitcoin’s market position. — Disposition: `already-addressed` | Reviewed: 2026-09-21 | Evidence: [Student Guide course setup and boundaries](../publish/mfb-bd-26.10/mfb-bd-sg-26.10.md:109)
- [x] **ANN-029** (source marker `[-]`) Expand “Verify” to include actions, people, and sources, not just transaction fields. — Disposition: `already-addressed` | Reviewed: 2026-09-21 | Evidence: [Student Guide course setup and boundaries](../publish/mfb-bd-26.10/mfb-bd-sg-26.10.md:109)
- [x] **ANN-030** (source marker `[o]`) Have a lawyer review the legal/financial/tax disclaimer. — Disposition: `approved-action` | Reviewed: 2026-09-21 | Evidence: [recurring publication checks](review_todo.md:404) | Linked action: [ACT-019](#act-019-complete-the-final-publication-verification-pass)
- [x] **ANN-031** (source marker `[-]`) Clarify the Diploma, locally selected Module 4, and Advanced boundaries and local suggestions. — Disposition: `already-addressed` | Reviewed: 2026-09-21 | Evidence: [Student Guide course setup and boundaries](../publish/mfb-bd-26.10/mfb-bd-sg-26.10.md:109)
- [x] **ANN-032** (source marker `[-]`) Use clear names instead of calling material “Bitcoin terms” merely for aesthetics. — Disposition: `already-addressed` | Reviewed: 2026-09-21 | Evidence: [Student Guide course setup and boundaries](../publish/mfb-bd-26.10/mfb-bd-sg-26.10.md:109)
- [x] **ANN-033** (source marker `[o]`) Create a standalone scam-reminders/red-flags one-pager. — Disposition: `approved-action` | Reviewed: 2026-09-21 | Evidence: [visual index](../workspace/08_assets.md:116) | Linked action: [ACT-013](#act-013-control-visual-production-scope)
- [x] **ANN-034** (source marker `[-]`) Reinforce “don't trust, verify” where appropriate. — Disposition: `already-addressed` | Reviewed: 2026-09-21 | Evidence: [Student Guide course setup and boundaries](../publish/mfb-bd-26.10/mfb-bd-sg-26.10.md:109)
- [x] **ANN-035** (source marker `[-]`) Mention Lightning/Layer 2 in the description of optional/local modules if it fits the intended scope. — Disposition: `already-addressed` | Reviewed: 2026-09-21 | Evidence: [Student Guide course setup and boundaries](../publish/mfb-bd-26.10/mfb-bd-sg-26.10.md:109)

### 1. Understanding Money

#### Opening questions about money

- [x] **ANN-036** (source marker `[ ]`) Add a motivating opening and educator preparation guidance. — Disposition: `already-addressed` | Reviewed: 2026-09-21 | Evidence: [Student Guide Module 1](../publish/mfb-bd-26.10/mfb-bd-sg-26.10.md:265)

#### Why money exists

- [x] **ANN-037** (source marker `[-]`) Clarify whether opening questions are a section discussion; add an educator wrap-up. — Disposition: `already-addressed` | Reviewed: 2026-09-21 | Evidence: [Student Guide Module 1](../publish/mfb-bd-26.10/mfb-bd-sg-26.10.md:265)
- [x] **ANN-038** (source marker `[o]`) Add a fact-versus-preference/dilemma activity to the educator guide. — Disposition: `already-addressed` | Reviewed: 2026-09-21 | Evidence: [Student Guide Module 1](../publish/mfb-bd-26.10/mfb-bd-sg-26.10.md:265)
- [x] **ANN-039** (source marker `[-]`) Move deeper barter/double-coincidence material into advanced modules. — Disposition: `superseded` | Reviewed: 2026-09-21 | Evidence: [Student Guide Module 1](../publish/mfb-bd-26.10/mfb-bd-sg-26.10.md:265)
- [x] **ANN-040** (source marker `[-]`) Add examples of exchange difficulty: wants, timing, distance, etc. — Disposition: `already-addressed` | Reviewed: 2026-09-21 | Evidence: [Student Guide Module 1](../publish/mfb-bd-26.10/mfb-bd-sg-26.10.md:265)
- [x] **ANN-041** (source marker `[o]`) Add links to optional further economics reading. — Disposition: `superseded` | Reviewed: 2026-09-21 | Evidence: [Student Guide Module 1](../publish/mfb-bd-26.10/mfb-bd-sg-26.10.md:265)
- [x] **ANN-042** (source marker `[-]`) Decide whether capitalism and free markets belong in advanced discussion rather than the beginner Diploma. — Disposition: `superseded` | Reviewed: 2026-09-21 | Evidence: [Student Guide Module 1](../publish/mfb-bd-26.10/mfb-bd-sg-26.10.md:265)
- [x] **ANN-043** (source marker `[-]`) Preserve the “very good for critical thinking” annotation as approval. — Disposition: `preserve-approval` | Reviewed: 2026-09-21 | Evidence: [Student Guide Module 1](../publish/mfb-bd-26.10/mfb-bd-sg-26.10.md:265)

#### Functions and properties of money

- [x] **ANN-044** (source marker `[o]`) Turn the money-properties table into a graphic; consider recognizability/“likeness.” — Disposition: `approved-action` | Reviewed: 2026-09-21 | Evidence: [visual index](../workspace/08_assets.md:116) | Linked action: [ACT-013](#act-013-control-visual-production-scope)
- [x] **ANN-045** (source marker `[-]`) Add property trade-off examples and goods/assets satisfying only some properties. — Disposition: `already-addressed` | Reviewed: 2026-09-21 | Evidence: [Student Guide Module 1](../publish/mfb-bd-26.10/mfb-bd-sg-26.10.md:265)
- [x] **ANN-046** (source marker `[-]`) Rewrite the unclear first comprehension question. — Disposition: `already-addressed` | Reviewed: 2026-09-21 | Evidence: [Student Guide Module 1](../publish/mfb-bd-26.10/mfb-bd-sg-26.10.md:265)
- [x] **ANN-047** (source marker `[o]`) Add a barter/double-coincidence graphic. — Disposition: `approved-action` | Reviewed: 2026-09-21 | Evidence: [visual index](../workspace/08_assets.md:116) | Linked action: [ACT-013](#act-013-control-visual-production-scope)
- [x] **ANN-048** (source marker `[-]`) Use a local three-role/item scenario and define the decision/double-coincidence problem. — Disposition: `already-addressed` | Reviewed: 2026-09-21 | Evidence: [Student Guide Module 1](../publish/mfb-bd-26.10/mfb-bd-sg-26.10.md:265)
- [x] **ANN-049** (source marker `[o]`) Consider printable cards or handouts for a “make the trades happen” barter activity. — Disposition: `superseded` | Reviewed: 2026-09-21 | Evidence: [Student Guide Module 1](../publish/mfb-bd-26.10/mfb-bd-sg-26.10.md:265)
- [x] **ANN-050** (source marker `[-]`) Preserve the positive annotation on the property/question table. — Disposition: `preserve-approval` | Reviewed: 2026-09-21 | Evidence: [Student Guide Module 1](../publish/mfb-bd-26.10/mfb-bd-sg-26.10.md:265)

#### Scarcity, value, and exchange

- [x] **ANN-051** (source marker `[-]`) Move the accepted-money explanation into the prior activity and have learners restate it. — Disposition: `superseded` | Reviewed: 2026-09-21 | Evidence: [Student Guide Module 1](../publish/mfb-bd-26.10/mfb-bd-sg-26.10.md:265)
- [x] **ANN-052** (source marker `[-]`) Add health to scarce-resource examples if appropriate. — Disposition: `superseded` | Reviewed: 2026-09-21 | Evidence: [Student Guide Module 1](../publish/mfb-bd-26.10/mfb-bd-sg-26.10.md:265)
- [x] **ANN-053** (source marker `[-]`) Teach subjective value through comparisons/trade-offs or games. — Disposition: `already-addressed` | Reviewed: 2026-09-21 | Evidence: [Student Guide Module 1](../publish/mfb-bd-26.10/mfb-bd-sg-26.10.md:265)
- [x] **ANN-054** (source marker `[-]`) Expand opportunity cost/time preference/trade-offs with examples and graphics. — Disposition: `superseded` | Reviewed: 2026-09-21 | Evidence: [Student Guide Module 1](../publish/mfb-bd-26.10/mfb-bd-sg-26.10.md:265)
- [x] **ANN-055** (source marker `[o]`) Add a visual money timeline from local/home exchange to institutional/global/digital forms. — Disposition: `approved-action` | Reviewed: 2026-09-21 | Evidence: [visual index](../workspace/08_assets.md:116) | Linked action: [ACT-013](#act-013-control-visual-production-scope)
- [x] **ANN-056** (source marker `[-]`) Avoid implying one universal linear monetary history. — Disposition: `already-addressed` | Reviewed: 2026-09-21 | Evidence: [Student Guide Module 1](../publish/mfb-bd-26.10/mfb-bd-sg-26.10.md:265)
- [x] **ANN-057** (source marker `[-]`) If discussing monetary evolution as civilizational progress, label it as a viewpoint or discussion prompt rather than settled fact. — Disposition: `already-addressed` | Reviewed: 2026-09-21 | Evidence: [Student Guide Module 1](../publish/mfb-bd-26.10/mfb-bd-sg-26.10.md:265)

#### Beginner monetary history from barter to digital money

- [x] **ANN-058** (source marker `[ ]`) Add an introductory hands-on money/app activity (exact handwritten details need confirmation). — Disposition: `needs-clarification` | Reviewed: 2026-09-21 | Evidence: [annotation provenance and confirmation rule](review_todo.md:510)
- [x] **ANN-059** (source marker `[-]`) Add historical context and competing views for standard coins and representative paper. — Disposition: `already-addressed` | Reviewed: 2026-09-21 | Evidence: [Student Guide Module 1](../publish/mfb-bd-26.10/mfb-bd-sg-26.10.md:265)
- [x] **ANN-060** (source marker `[-]`) Rework bank/government money and define the affected population/network. — Disposition: `already-addressed` | Reviewed: 2026-09-21 | Evidence: [Student Guide Module 1](../publish/mfb-bd-26.10/mfb-bd-sg-26.10.md:265)
- [x] **ANN-061** (source marker `[-]`) Add 1971/Nixon Shock/Bretton Woods context; define convertibility. — Disposition: `already-addressed` | Reviewed: 2026-09-21 | Evidence: [Student Guide Module 1](../publish/mfb-bd-26.10/mfb-bd-sg-26.10.md:265)
- [x] **ANN-062** (source marker `[-]`) Define fiat before use and distinguish modern fiat, older money, and account claims. — Disposition: `already-addressed` | Reviewed: 2026-09-21 | Evidence: [Student Guide Module 1](../publish/mfb-bd-26.10/mfb-bd-sg-26.10.md:265)
- [x] **ANN-063** (source marker `[-]`) Check “by decree” and avoid one-country assumptions. — Disposition: `already-addressed` | Reviewed: 2026-09-21 | Evidence: [Student Guide Module 1](../publish/mfb-bd-26.10/mfb-bd-sg-26.10.md:265)
- [x] **ANN-064** (source marker `[-]`) Explain network effects more clearly. — Disposition: `already-addressed` | Reviewed: 2026-09-21 | Evidence: [Student Guide Module 1](../publish/mfb-bd-26.10/mfb-bd-sg-26.10.md:265)
- [x] **ANN-065** (source marker `[-]`) Restructure terms so each is explained before use. — Disposition: `already-addressed` | Reviewed: 2026-09-21 | Evidence: [Student Guide Module 1](../publish/mfb-bd-26.10/mfb-bd-sg-26.10.md:265)
- [x] **ANN-066** (source marker `[o]`) Create a downloadable History of Money companion app, video, or PDF. — Disposition: `superseded` | Reviewed: 2026-09-21 | Evidence: [Student Guide Module 1](../publish/mfb-bd-26.10/mfb-bd-sg-26.10.md:265)
- [x] **ANN-067** (source marker `[o]`) Provide a stable maintained history/money reference for educators. — Disposition: `approved-action` | Reviewed: 2026-09-21 | Evidence: [resource-register maintenance requirement](../workspace/09_resources.md:1) | Linked action: [ACT-010](#act-010-replace-mutable-source-and-terminology-locations)
- [x] **ANN-068** (source marker `[-]`) Consider the USD's post-WWII international-settlement role and Bretton Woods; include Federal Reserve/Jekyll Island background only if relevant, balanced, and sourced. — Disposition: `superseded` | Reviewed: 2026-09-21 | Evidence: [Student Guide Module 1](../publish/mfb-bd-26.10/mfb-bd-sg-26.10.md:265)

#### Fractional reserve banking

- [x] **ANN-069** (source marker `[-]`) Explain “creates deposit money when it issues loans.” — Disposition: `already-addressed` | Reviewed: 2026-09-21 | Evidence: [Student Guide Module 1](../publish/mfb-bd-26.10/mfb-bd-sg-26.10.md:265)
- [x] **ANN-070** (source marker `[-]`) Move deeper risks/benefits into advanced modules and avoid presenting them as universal facts. — Disposition: `superseded` | Reviewed: 2026-09-21 | Evidence: [Student Guide Module 1](../publish/mfb-bd-26.10/mfb-bd-sg-26.10.md:265)
- [x] **ANN-071** (source marker `[o]`) Define liability and diagram fractional-reserve banking. — Disposition: `approved-action` | Reviewed: 2026-09-21 | Evidence: [visual index](../workspace/08_assets.md:116) | Linked action: [ACT-013](#act-013-control-visual-production-scope)
- [x] **ANN-072** (source marker `[o]`) Consider a small bank-reserve/gearing calculator or interactive activity. — Disposition: `superseded` | Reviewed: 2026-09-21 | Evidence: [Student Guide Module 1](../publish/mfb-bd-26.10/mfb-bd-sg-26.10.md:265)

#### Inflation and purchasing power

- [x] **ANN-073** (source marker `[-]`) Explain how bank runs affect the wider population/economy and how interventions/losses work. — Disposition: `already-addressed` | Reviewed: 2026-09-21 | Evidence: [Student Guide Module 1](../publish/mfb-bd-26.10/mfb-bd-sg-26.10.md:265)
- [x] **ANN-074** (source marker `[ ]`) Confirm the unclear “10% / too big to fail / restructuring” note. — Disposition: `needs-clarification` | Reviewed: 2026-09-21 | Evidence: [annotation provenance and confirmation rule](review_todo.md:510)
- [x] **ANN-075** (source marker `[-]`) Turn inflation/purchasing-power definitions into graphics, local examples, and an activity. — Disposition: `approved-action` | Reviewed: 2026-09-21 | Evidence: [visual index](../workspace/08_assets.md:116) | Linked action: [ACT-013](#act-013-control-visual-production-scope)
- [x] **ANN-076** (source marker `[o]`) Add advanced treatment of monetary expansion and secondary effects. — Disposition: `superseded` | Reviewed: 2026-09-21 | Evidence: [Student Guide Module 1](../publish/mfb-bd-26.10/mfb-bd-sg-26.10.md:265)
- [x] **ANN-077** (source marker `[-]`) Label the purchasing-power check as a distinct activity. — Disposition: `already-addressed` | Reviewed: 2026-09-21 | Evidence: [Student Guide Module 1](../publish/mfb-bd-26.10/mfb-bd-sg-26.10.md:265)

#### Central Bank Digital Currencies (CBDCs)

- [x] **ANN-078** (source marker `[-]`) Add CBDC examples and risks/benefits. — Disposition: `already-addressed` | Reviewed: 2026-09-21 | Evidence: [Student Guide Module 1](../publish/mfb-bd-26.10/mfb-bd-sg-26.10.md:265)
- [x] **ANN-079** (source marker `[-]`) Explain safety, access to transaction information, privacy, and control. — Disposition: `already-addressed` | Reviewed: 2026-09-21 | Evidence: [Student Guide Module 1](../publish/mfb-bd-26.10/mfb-bd-sg-26.10.md:265)
- [x] **ANN-080** (source marker `[-]`) Require current, local, reliable CBDC information. — Disposition: `already-addressed` | Reviewed: 2026-09-21 | Evidence: [Student Guide Module 1](../publish/mfb-bd-26.10/mfb-bd-sg-26.10.md:265)
- [x] **ANN-081** (source marker `[-]`) Add locally accurate tax considerations or benefits to the real-estate comparison where relevant. — Disposition: `superseded` | Reviewed: 2026-09-21 | Evidence: [Student Guide Module 1](../publish/mfb-bd-26.10/mfb-bd-sg-26.10.md:265)

#### Review: how can money break?

- [x] **ANN-082** (source marker `[-]`) Clarify assets versus money for metals, currency, bonds, businesses, land, tools, and education. — Disposition: `already-addressed` | Reviewed: 2026-09-21 | Evidence: [Student Guide Module 1](../publish/mfb-bd-26.10/mfb-bd-sg-26.10.md:265)
- [x] **ANN-083** (source marker `[-]`) Distinguish BTC as money versus asset and clarify the claimed fiat “problem.” — Disposition: `already-addressed` | Reviewed: 2026-09-21 | Evidence: [Student Guide Module 1](../publish/mfb-bd-26.10/mfb-bd-sg-26.10.md:265)
- [x] **ANN-084** (source marker `[o]`) Keep the fill-in review exercise (“YES!”). — Disposition: `preserve-approval` | Reviewed: 2026-09-21 | Evidence: [Student Guide Module 1](../publish/mfb-bd-26.10/mfb-bd-sg-26.10.md:265)
- [x] **ANN-085** (source marker `[o]`) Expert-review the Module 1 answer. — Disposition: `approved-action` | Reviewed: 2026-09-21 | Evidence: [recurring publication checks](review_todo.md:404) | Linked action: [ACT-019](#act-019-complete-the-final-publication-verification-pass)
- [x] **ANN-086** (source marker `[-]`) Rename/reframe “How Bitcoin Works” if “solution” overstates the claim. — Disposition: `superseded` | Reviewed: 2026-09-21 | Evidence: [Student Guide Module 1](../publish/mfb-bd-26.10/mfb-bd-sg-26.10.md:265)
- [x] **ANN-087** (source marker `[-]`) Ensure the framing cannot be mistaken for a general cryptocurrency diploma. — Disposition: `already-addressed` | Reviewed: 2026-09-21 | Evidence: [Student Guide Module 1](../publish/mfb-bd-26.10/mfb-bd-sg-26.10.md:265)
- [x] **ANN-088** (source marker `[ ]`) Clarify the annotation “To what Q?” and connect item 7 to its intended question. — Disposition: `needs-clarification` | Reviewed: 2026-09-21 | Evidence: [annotation provenance and confirmation rule](review_todo.md:510)
- [x] **ANN-089** (source marker `[o]`) Preserve “YES!” on the fill-in exercise and “PERFECT LFG!” at the end of Module 1 as explicit approvals. — Disposition: `preserve-approval` | Reviewed: 2026-09-21 | Evidence: [Student Guide Module 1](../publish/mfb-bd-26.10/mfb-bd-sg-26.10.md:265)

### 2. How Bitcoin Works

#### Why Bitcoin was created

- [x] **ANN-090** (source marker `[-]`) Make the intermediary power/risk example concrete. — Disposition: `already-addressed` | Reviewed: 2026-09-21 | Evidence: [Student Guide Module 2](../publish/mfb-bd-26.10/mfb-bd-sg-26.10.md:580)
- [x] **ANN-091** (source marker `[-]`) Confirm/add the unclear note about Cypherpunk/Bitcoin history. — Disposition: `needs-clarification` | Reviewed: 2026-09-21 | Evidence: [annotation provenance and confirmation rule](review_todo.md:510)
- [x] **ANN-092** (source marker `[-]`) Review whether “issuer” is being used correctly. — Disposition: `already-addressed` | Reviewed: 2026-09-21 | Evidence: [Student Guide Module 2](../publish/mfb-bd-26.10/mfb-bd-sg-26.10.md:580)
- [x] **ANN-093** (source marker `[-]`) Add a Cypherpunk definition box or optional further-reading link. — Disposition: `already-addressed` | Reviewed: 2026-09-21 | Evidence: [Student Guide Module 2](../publish/mfb-bd-26.10/mfb-bd-sg-26.10.md:580)

#### Early digital-money attempts and the double-spend problem

- [x] **ANN-094** (source marker `[-]`) Attribute prior contributors/ideas in Bitcoin’s origin story. — Disposition: `already-addressed` | Reviewed: 2026-09-21 | Evidence: [Student Guide Module 2](../publish/mfb-bd-26.10/mfb-bd-sg-26.10.md:580)
- [x] **ANN-095** (source marker `[-]`) Define DigiCash, Hashcash, Bit Gold, proof of work, mining, miners, nodes, blocks, valid chain, and accumulated work. — Disposition: `already-addressed` | Reviewed: 2026-09-21 | Evidence: [Student Guide Module 2](../publish/mfb-bd-26.10/mfb-bd-sg-26.10.md:580)
- [x] **ANN-096** (source marker `[-]`) Bold or otherwise visually clarify the numbered transaction/miner/node process. — Disposition: `already-addressed` | Reviewed: 2026-09-21 | Evidence: [Student Guide Module 2](../publish/mfb-bd-26.10/mfb-bd-sg-26.10.md:580)
- [x] **ANN-097** (source marker `[-]`) Preserve the “VG” annotation on the closing explanation as approval. — Disposition: `preserve-approval` | Reviewed: 2026-09-21 | Evidence: [Student Guide Module 2](../publish/mfb-bd-26.10/mfb-bd-sg-26.10.md:580)

#### Bitcoin origin timeline

- [x] **ANN-098** (source marker `[ ]`) Clarify the note beside Satoshi’s identity and avoid speculation. — Disposition: `needs-clarification` | Reviewed: 2026-09-21 | Evidence: [annotation provenance and confirmation rule](review_todo.md:510)
- [x] **ANN-099** (source marker `[o]`) Consider an optional “my first Bitcoin purchase” calendar/ICS reminder tied to Bitcoin Pizza Day. — Disposition: `superseded` | Reviewed: 2026-09-21 | Evidence: [Student Guide Module 2](../publish/mfb-bd-26.10/mfb-bd-sg-26.10.md:580)

#### Decentralization

- [x] **ANN-100** (source marker `[-]`) Define decentralization-list terms. — Disposition: `already-addressed` | Reviewed: 2026-09-21 | Evidence: [Student Guide Module 2](../publish/mfb-bd-26.10/mfb-bd-sg-26.10.md:580)
- [x] **ANN-101** (source marker `[-]`) Qualify/add examples to “no participant can unilaterally change rules.” — Disposition: `already-addressed` | Reviewed: 2026-09-21 | Evidence: [Student Guide Module 2](../publish/mfb-bd-26.10/mfb-bd-sg-26.10.md:580)
- [x] **ANN-102** (source marker `[-]`) Distinguish subsidy from total supply and correct marked terminology. — Disposition: `already-addressed` | Reviewed: 2026-09-21 | Evidence: [Student Guide Module 2](../publish/mfb-bd-26.10/mfb-bd-sg-26.10.md:580)
- [x] **ANN-103** (source marker `[-]`) Explain halving as block-based/roughly four-year timing, not a fixed date. — Disposition: `already-addressed` | Reviewed: 2026-09-21 | Evidence: [Student Guide Module 2](../publish/mfb-bd-26.10/mfb-bd-sg-26.10.md:580)
- [x] **ANN-104** (source marker `[o]`) Add a finite-supply/halving graphic. — Disposition: `approved-action` | Reviewed: 2026-09-21 | Evidence: [visual index](../workspace/08_assets.md:116) | Linked action: [ACT-013](#act-013-control-visual-production-scope)
- [x] **ANN-105** (source marker `[-]`) Separate known issuance facts from uncertain adoption/price/scaling claims. — Disposition: `already-addressed` | Reviewed: 2026-09-21 | Evidence: [Student Guide Module 2](../publish/mfb-bd-26.10/mfb-bd-sg-26.10.md:580)
- [x] **ANN-106** (source marker `[-]`) Link back to Module 1. — Disposition: `already-addressed` | Reviewed: 2026-09-21 | Evidence: [Student Guide Module 2](../publish/mfb-bd-26.10/mfb-bd-sg-26.10.md:580)

#### Satoshis and unit bias

- [x] **ANN-107** (source marker `[o]`) Turn the bitcoin/sats table into a graphic. — Disposition: `approved-action` | Reviewed: 2026-09-21 | Evidence: [visual index](../workspace/08_assets.md:116) | Linked action: [ACT-013](#act-013-control-visual-production-scope)
- [x] **ANN-108** (source marker `[-]`) Rewrite the whole-number/sats sentence. — Disposition: `already-addressed` | Reviewed: 2026-09-21 | Evidence: [Student Guide Module 2](../publish/mfb-bd-26.10/mfb-bd-sg-26.10.md:580)
- [x] **ANN-109** (source marker `[-]`) Improve the comprehension exercise and provide answer guidance. — Disposition: `already-addressed` | Reviewed: 2026-09-21 | Evidence: [Student Guide Module 2](../publish/mfb-bd-26.10/mfb-bd-sg-26.10.md:580)

#### Users, nodes, and miners

- [x] **ANN-110** (source marker `[-]`) Distinguish the Bitcoin network from services/intermediaries. — Disposition: `already-addressed` | Reviewed: 2026-09-21 | Evidence: [Student Guide Module 2](../publish/mfb-bd-26.10/mfb-bd-sg-26.10.md:580)
- [x] **ANN-111** (source marker `[-]`) Check “usually” in the irreversibility claim. — Disposition: `already-addressed` | Reviewed: 2026-09-21 | Evidence: [Student Guide Module 2](../publish/mfb-bd-26.10/mfb-bd-sg-26.10.md:580)
- [x] **ANN-112** (source marker `[-]`) Clarify whether “users” means using a wallet/client or running Bitcoin Core/full node. — Disposition: `already-addressed` | Reviewed: 2026-09-21 | Evidence: [Student Guide Module 2](../publish/mfb-bd-26.10/mfb-bd-sg-26.10.md:580)
- [x] **ANN-113** (source marker `[-]`) Explain “developers can propose software…”; the note asks “What?!” — Disposition: `already-addressed` | Reviewed: 2026-09-21 | Evidence: [Student Guide Module 2](../publish/mfb-bd-26.10/mfb-bd-sg-26.10.md:580)

#### Proof of work

- [x] **ANN-114** (source marker `[-]`) Add marked proof-of-work terms to the lexicon. — Disposition: `already-addressed` | Reviewed: 2026-09-21 | Evidence: [Student Guide Module 2](../publish/mfb-bd-26.10/mfb-bd-sg-26.10.md:580)
- [x] **ANN-115** (source marker `[o]`) Demonstrate proof of work/difficulty with a tool, interactive, or animation. — Disposition: `superseded` | Reviewed: 2026-09-21 | Evidence: [Student Guide Module 2](../publish/mfb-bd-26.10/mfb-bd-sg-26.10.md:580)
- [x] **ANN-116** (source marker `[o]`) Diagram/animate proof of work’s stated purposes. — Disposition: `approved-action` | Reviewed: 2026-09-21 | Evidence: [visual index](../workspace/08_assets.md:116) | Linked action: [ACT-013](#act-013-control-visual-production-scope)
- [x] **ANN-117** (source marker `[-]`) Link relevant sound-money/Nick Szabo background and qualify “sound digital money.” — Disposition: `superseded` | Reviewed: 2026-09-21 | Evidence: [Student Guide Module 2](../publish/mfb-bd-26.10/mfb-bd-sg-26.10.md:580)

#### Bitcoin as sound digital money

- [x] **ANN-118** (source marker `[-]`) Double-check the property criteria/requirements. — Disposition: `already-addressed` | Reviewed: 2026-09-21 | Evidence: [Student Guide Module 2](../publish/mfb-bd-26.10/mfb-bd-sg-26.10.md:580)
- [x] **ANN-119** (source marker `[-]`) Add FAQs about fungibility and sat interchangeability. — Disposition: `already-addressed` | Reviewed: 2026-09-21 | Evidence: [Student Guide Module 2](../publish/mfb-bd-26.10/mfb-bd-sg-26.10.md:580)
- [x] **ANN-120** (source marker `[-]`) Add nuance to the functions-of-money assessment. — Disposition: `already-addressed` | Reviewed: 2026-09-21 | Evidence: [Student Guide Module 2](../publish/mfb-bd-26.10/mfb-bd-sg-26.10.md:580)

#### Participant empowerment, risk, and responsibility

- [x] **ANN-121** (source marker `[-]`) Improve personal-responsibility examples and unclear wording (“less,” “peer information”). — Disposition: `already-addressed` | Reviewed: 2026-09-21 | Evidence: [Student Guide Module 2](../publish/mfb-bd-26.10/mfb-bd-sg-26.10.md:580)
- [x] **ANN-122** (source marker `[o]`) Add graphics to the Module 2 comparison. — Disposition: `approved-action` | Reviewed: 2026-09-21 | Evidence: [visual index](../workspace/08_assets.md:116) | Linked action: [ACT-013](#act-013-control-visual-production-scope)
- [x] **ANN-123** (source marker `[-]`) Deepen function/property comparisons, including scarcity. — Disposition: `superseded` | Reviewed: 2026-09-21 | Evidence: [Student Guide Module 2](../publish/mfb-bd-26.10/mfb-bd-sg-26.10.md:580)
- [x] **ANN-124** (source marker `[-]`) Make the next-module transition explicit. — Disposition: `already-addressed` | Reviewed: 2026-09-21 | Evidence: [Student Guide Module 2](../publish/mfb-bd-26.10/mfb-bd-sg-26.10.md:580)

### 3. Using Bitcoin Safely

#### Wallets

- [x] **ANN-125** (source marker `[ ]`) Confirm/add the proposed new comparison column (label illegible). — Disposition: `needs-clarification` | Reviewed: 2026-09-21 | Evidence: [annotation provenance and confirmation rule](review_todo.md:510)
- [x] **ANN-126** (source marker `[-]`) Recheck the Module 2 answer and transition to Module 3. — Disposition: `already-addressed` | Reviewed: 2026-09-21 | Evidence: [Student Guide Module 3](../publish/mfb-bd-26.10/mfb-bd-sg-26.10.md:963)
- [x] **ANN-127** (source marker `[-]`) Add wallet terms to the lexicon. — Disposition: `already-addressed` | Reviewed: 2026-09-21 | Evidence: [Student Guide Module 3](../publish/mfb-bd-26.10/mfb-bd-sg-26.10.md:963)
- [x] **ANN-128** (source marker `[-]`) Rephrase the Module 3 learner promise consistently. — Disposition: `already-addressed` | Reviewed: 2026-09-21 | Evidence: [Student Guide Module 3](../publish/mfb-bd-26.10/mfb-bd-sg-26.10.md:963)
- [x] **ANN-129** (source marker `[-]`) Clarify that a wallet coordinates keys/spending/receiving while bitcoin remains on the ledger. — Disposition: `already-addressed` | Reviewed: 2026-09-21 | Evidence: [Student Guide Module 3](../publish/mfb-bd-26.10/mfb-bd-sg-26.10.md:963)

#### Addresses

- [x] **ANN-130** (source marker `[-]`) Explain how to evaluate compatibility, open source, recovery, privacy, and project continuity. — Disposition: `already-addressed` | Reviewed: 2026-09-21 | Evidence: [Student Guide Module 3](../publish/mfb-bd-26.10/mfb-bd-sg-26.10.md:963)
- [x] **ANN-131** (source marker `[-]`) Add address/network/tag terms to the lexicon. — Disposition: `already-addressed` | Reviewed: 2026-09-21 | Evidence: [Student Guide Module 3](../publish/mfb-bd-26.10/mfb-bd-sg-26.10.md:963)
- [x] **ANN-132** (source marker `[o]`) Add an address/QR graphic and explain who creates addresses. — Disposition: `approved-action` | Reviewed: 2026-09-21 | Evidence: [visual index](../workspace/08_assets.md:116) | Linked action: [ACT-013](#act-013-control-visual-production-scope)
- [x] **ANN-133** (source marker `[-]`) Add explicit how-to guidance for address checks. — Disposition: `already-addressed` | Reviewed: 2026-09-21 | Evidence: [Student Guide Module 3](../publish/mfb-bd-26.10/mfb-bd-sg-26.10.md:963)

#### Keys

- [x] **ANN-134** (source marker `[o]`) Add a public/private-key image and optional physical teaching tool. — Disposition: `approved-action` | Reviewed: 2026-09-21 | Evidence: [visual index](../workspace/08_assets.md:116) | Linked action: [ACT-013](#act-013-control-visual-production-scope)
- [x] **ANN-135** (source marker `[-]`) Point technical depth to an advanced module. — Disposition: `superseded` | Reviewed: 2026-09-21 | Evidence: [Student Guide Module 3](../publish/mfb-bd-26.10/mfb-bd-sg-26.10.md:963)
- [x] **ANN-136** (source marker `[-]`) Emphasize avoiding key/recovery-material loss. — Disposition: `already-addressed` | Reviewed: 2026-09-21 | Evidence: [Student Guide Module 3](../publish/mfb-bd-26.10/mfb-bd-sg-26.10.md:963)
- [x] **ANN-137** (source marker `[-]`) Reassess “seed phrase” versus broader recovery language. — Disposition: `already-addressed` | Reviewed: 2026-09-21 | Evidence: [Student Guide Module 3](../publish/mfb-bd-26.10/mfb-bd-sg-26.10.md:963)

#### Seed phrases

- [x] **ANN-138** (source marker `[o]`) Add a visual wallet setup/recovery activity: why it matters, record, store, and test. — Disposition: `approved-action` | Reviewed: 2026-09-21 | Evidence: [visual index](../workspace/08_assets.md:116) | Linked action: [ACT-013](#act-013-control-visual-production-scope)
- [x] **ANN-139** (source marker `[-]`) Keep/emphasize the seed-backup checklist (“Love it”). — Disposition: `preserve-approval` | Reviewed: 2026-09-21 | Evidence: [Student Guide Module 3](../publish/mfb-bd-26.10/mfb-bd-sg-26.10.md:963)
- [x] **ANN-140** (source marker `[-]`) Correct the marked “read & process” recovery wording. — Disposition: `already-addressed` | Reviewed: 2026-09-21 | Evidence: [Student Guide Module 3](../publish/mfb-bd-26.10/mfb-bd-sg-26.10.md:963)

#### Hot and cold wallets

- [x] **ANN-141** (source marker `[o]`) Add a graphic comparing hot, hardware/cold, and custodial wallets/accounts. — Disposition: `approved-action` | Reviewed: 2026-09-21 | Evidence: [visual index](../workspace/08_assets.md:116) | Linked action: [ACT-013](#act-013-control-visual-production-scope)

#### Wallet recovery and seed phrase testing

- [x] **ANN-142** (source marker `[-]`) Decide whether recovery is taught with seed phrases, another method, or several methods. — Disposition: `already-addressed` | Reviewed: 2026-09-21 | Evidence: [Student Guide Module 3](../publish/mfb-bd-26.10/mfb-bd-sg-26.10.md:963)
- [x] **ANN-143** (source marker `[o]`) Make recovery principles a one-page trainer/learner checklist. — Disposition: `approved-action` | Reviewed: 2026-09-21 | Evidence: [visual index](../workspace/08_assets.md:116) | Linked action: [ACT-013](#act-013-control-visual-production-scope)
- [x] **ANN-144** (source marker `[-]`) Make practice practical but private and limited to empty/tiny-value wallets. — Disposition: `already-addressed` | Reviewed: 2026-09-21 | Evidence: [Student Guide Module 3](../publish/mfb-bd-26.10/mfb-bd-sg-26.10.md:963)

#### Receiving bitcoin

- [x] **ANN-145** (source marker `[-]`) Add robust/resilient recovery and security tests/examples. — Disposition: `superseded` | Reviewed: 2026-09-21 | Evidence: [Student Guide Module 3](../publish/mfb-bd-26.10/mfb-bd-sg-26.10.md:963)
- [x] **ANN-146** (source marker `[o]`) Add a visual receiving activity with roles, addresses, QR codes, and examples. — Disposition: `approved-action` | Reviewed: 2026-09-21 | Evidence: [visual index](../workspace/08_assets.md:116) | Linked action: [ACT-013](#act-013-control-visual-production-scope)
- [x] **ANN-147** (source marker `[-]`) Treat confirmation count as local/risk-dependent. — Disposition: `already-addressed` | Reviewed: 2026-09-21 | Evidence: [Student Guide Module 3](../publish/mfb-bd-26.10/mfb-bd-sg-26.10.md:963)
- [x] **ANN-148** (source marker `[-]`) Create a receive-screen competency activity without requiring real funds. — Disposition: `already-addressed` | Reviewed: 2026-09-21 | Evidence: [Student Guide Module 3](../publish/mfb-bd-26.10/mfb-bd-sg-26.10.md:963)
- [x] **ANN-149** (source marker `[-]`) Add “confirmations” to the lexicon. — Disposition: `already-addressed` | Reviewed: 2026-09-21 | Evidence: [Student Guide Module 3](../publish/mfb-bd-26.10/mfb-bd-sg-26.10.md:963)

#### Sending bitcoin

- [x] **ANN-150** (source marker `[o]`) Make sending/address/network checks a one-page checklist and clarify “address type.” — Disposition: `approved-action` | Reviewed: 2026-09-21 | Evidence: [visual index](../workspace/08_assets.md:116) | Linked action: [ACT-013](#act-013-control-visual-production-scope)
- [x] **ANN-151** (source marker `[-]`) Add “how” guidance to command-only checks. — Disposition: `already-addressed` | Reviewed: 2026-09-21 | Evidence: [Student Guide Module 3](../publish/mfb-bd-26.10/mfb-bd-sg-26.10.md:963)
- [x] **ANN-152** (source marker `[-]`) Explain fee estimation/security without requiring miner knowledge for each transaction. — Disposition: `already-addressed` | Reviewed: 2026-09-21 | Evidence: [Student Guide Module 3](../publish/mfb-bd-26.10/mfb-bd-sg-26.10.md:963)
- [x] **ANN-153** (source marker `[-]`) Add a TXID/block-explorer activity or quiz. — Disposition: `already-addressed` | Reviewed: 2026-09-21 | Evidence: [Student Guide Module 3](../publish/mfb-bd-26.10/mfb-bd-sg-26.10.md:963)

#### Verification, block explorers, and irreversible transactions

- [x] **ANN-154** (source marker `[-]`) Explain first confirmation and block depth more clearly. — Disposition: `already-addressed` | Reviewed: 2026-09-21 | Evidence: [Student Guide Module 3](../publish/mfb-bd-26.10/mfb-bd-sg-26.10.md:963)
- [x] **ANN-155** (source marker `[-]`) Expand the block-explorer privacy warning without overloading beginners. — Disposition: `already-addressed` | Reviewed: 2026-09-21 | Evidence: [Student Guide Module 3](../publish/mfb-bd-26.10/mfb-bd-sg-26.10.md:963)
- [x] **ANN-156** (source marker `[o]`) Make the safety checklist a one-page resource. — Disposition: `approved-action` | Reviewed: 2026-09-21 | Evidence: [visual index](../workspace/08_assets.md:116) | Linked action: [ACT-013](#act-013-control-visual-production-scope)
- [x] **ANN-157** (source marker `[-]`) Distinguish on-chain and Lightning under destination verification. — Disposition: `already-addressed` | Reviewed: 2026-09-21 | Evidence: [Student Guide Module 3](../publish/mfb-bd-26.10/mfb-bd-sg-26.10.md:963)

#### Safety checklist

- [x] **ANN-158** (source marker `[o]`) Turn scam scenarios into scaffolded role-play/advanced content rather than one dense list. — Disposition: `already-addressed` | Reviewed: 2026-09-21 | Evidence: [Student Guide Module 3](../publish/mfb-bd-26.10/mfb-bd-sg-26.10.md:963)
- [x] **ANN-159** (source marker `[-]`) Reduce Module 3 security overload and clarify learner choices. — Disposition: `already-addressed` | Reviewed: 2026-09-21 | Evidence: [Student Guide Module 3](../publish/mfb-bd-26.10/mfb-bd-sg-26.10.md:963)

#### Acquiring and exchanging bitcoin: awareness, not financial advice

- [x] **ANN-160** (source marker `[-]`) Fix heading hierarchy (“sub-header, not header”). — Disposition: `already-addressed` | Reviewed: 2026-09-21 | Evidence: [Student Guide Module 3](../publish/mfb-bd-26.10/mfb-bd-sg-26.10.md:963)
- [x] **ANN-161** (source marker `[-]`) Distinguish financial advice from awareness of ways to acquire and exchange bitcoin. — Disposition: `already-addressed` | Reviewed: 2026-09-21 | Evidence: [Student Guide Module 3](../publish/mfb-bd-26.10/mfb-bd-sg-26.10.md:963)
- [x] **ANN-162** (source marker `[o]`) Turn acquisition/exchange pathways into a one-page comparison activity. — Disposition: `approved-action` | Reviewed: 2026-09-21 | Evidence: [visual index](../workspace/08_assets.md:116) | Linked action: [ACT-013](#act-013-control-visual-production-scope)

#### On-chain and Lightning payments

- [x] **ANN-163** (source marker `[-]`) Add on-chain and Lightning examples to the table. — Disposition: `already-addressed` | Reviewed: 2026-09-21 | Evidence: [Student Guide Module 3](../publish/mfb-bd-26.10/mfb-bd-sg-26.10.md:963)
- [x] **ANN-164** (source marker `[-]`) Define marked terms. — Disposition: `already-addressed` | Reviewed: 2026-09-21 | Evidence: [Student Guide Module 3](../publish/mfb-bd-26.10/mfb-bd-sg-26.10.md:963)
- [x] **ANN-165** (source marker `[-]`) Move routing/channel mechanics to advanced content. — Disposition: `already-addressed` | Reviewed: 2026-09-21 | Evidence: [Student Guide Module 3](../publish/mfb-bd-26.10/mfb-bd-sg-26.10.md:963)
- [x] **ANN-166** (source marker `[-]`) Explain Lightning trade-offs involving custody, routing, channels, and liquidity. — Disposition: `already-addressed` | Reviewed: 2026-09-21 | Evidence: [Student Guide Module 3](../publish/mfb-bd-26.10/mfb-bd-sg-26.10.md:963)

#### Review: what does self-custody responsibility mean?

- [x] **ANN-167** (source marker `[-]`) Rename/explain “Module 4” and Module 4. — Disposition: `already-addressed` | Reviewed: 2026-09-21 | Evidence: [Student Guide Module 3](../publish/mfb-bd-26.10/mfb-bd-sg-26.10.md:963)
- [x] **ANN-168** (source marker `[-]`) Mark the second on-chain/Lightning comparison table as advanced if that matches the annotation. — Disposition: `superseded` | Reviewed: 2026-09-21 | Evidence: [Student Guide Module 3](../publish/mfb-bd-26.10/mfb-bd-sg-26.10.md:963)

### 4. Bitcoin in Your Community

#### Educator-selected local modules

- [x] **ANN-169** (source marker `[-]`) Clarify the responsibility map and whether “choose custody” is an action or competency result. — Disposition: `already-addressed` | Reviewed: 2026-09-21 | Evidence: [Student Guide Module 4](../publish/mfb-bd-26.10/mfb-bd-sg-26.10.md:1309)
- [x] **ANN-170** (source marker `[o]`) Make the table an educator-guided exercise with examples. — Disposition: `approved-action` | Reviewed: 2026-09-21 | Evidence: [visual index](../workspace/08_assets.md:116) | Linked action: [ACT-013](#act-013-control-visual-production-scope)
- [x] **ANN-171** (source marker `[-]`) Separate generic terms from scam signals. — Disposition: `already-addressed` | Reviewed: 2026-09-21 | Evidence: [Student Guide Module 4](../publish/mfb-bd-26.10/mfb-bd-sg-26.10.md:1309)
- [x] **ANN-172** (source marker `[-]`) Rewrite the “heavy” Module 3 answer with examples. — Disposition: `already-addressed` | Reviewed: 2026-09-21 | Evidence: [Student Guide Module 4](../publish/mfb-bd-26.10/mfb-bd-sg-26.10.md:1309)
- [x] **ANN-173** (source marker `[o]`) Move educator-only Module 3 material to the educator guide. — Disposition: `already-addressed` | Reviewed: 2026-09-21 | Evidence: [Student Guide Module 4](../publish/mfb-bd-26.10/mfb-bd-sg-26.10.md:1309)
- [x] **ANN-174** (source marker `[-]`) Redesign Module 4 as locally selected learning; define MFB versus educator responsibilities and resources. — Disposition: `already-addressed` | Reviewed: 2026-09-21 | Evidence: [Student Guide Module 4](../publish/mfb-bd-26.10/mfb-bd-sg-26.10.md:1309)
- [x] **ANN-175** (source marker `[-]`) Describe Module 4 as locally selected but required in learner-facing Diploma material. — Disposition: `already-addressed` | Reviewed: 2026-09-21 | Evidence: [Student Guide Module 4](../publish/mfb-bd-26.10/mfb-bd-sg-26.10.md:1309)
- [x] **ANN-176** (source marker `[-]`) Preserve the annotation that Module 3 is “full, complete & serious” while acting on the concern that it feels heavy. — Disposition: `preserve-approval` | Reviewed: 2026-09-21 | Evidence: [Student Guide Module 4](../publish/mfb-bd-26.10/mfb-bd-sg-26.10.md:1309)
- [x] **ANN-177** (source marker `[-]`) State that educators select a topic/module for local context and provide an example. — Disposition: `already-addressed` | Reviewed: 2026-09-21 | Evidence: [Student Guide Module 4](../publish/mfb-bd-26.10/mfb-bd-sg-26.10.md:1309)
- [x] **ANN-178** (source marker `[-]`) Clarify local warnings/appropriateness conditions. — Disposition: `already-addressed` | Reviewed: 2026-09-21 | Evidence: [Student Guide Module 4](../publish/mfb-bd-26.10/mfb-bd-sg-26.10.md:1309)
- [x] **ANN-179** (source marker `[-]`) Preserve the local-learning table (“I like this”) as a reusable template. — Disposition: `preserve-approval` | Reviewed: 2026-09-21 | Evidence: [Student Guide Module 4](../publish/mfb-bd-26.10/mfb-bd-sg-26.10.md:1309)
- [x] **ANN-180** (source marker `[-]`) State what learners should learn and integrate through locally selected Module 4. — Disposition: `already-addressed` | Reviewed: 2026-09-21 | Evidence: [Student Guide Module 4](../publish/mfb-bd-26.10/mfb-bd-sg-26.10.md:1309)
- [x] **ANN-181** (source marker `[-]`) Add community/spread-layer considerations. — Disposition: `superseded` | Reviewed: 2026-09-21 | Evidence: [Student Guide Module 4](../publish/mfb-bd-26.10/mfb-bd-sg-26.10.md:1309)
- [x] **ANN-182** (source marker `[o]`) Give each local module a page-count or scope limit. — Disposition: `superseded` | Reviewed: 2026-09-21 | Evidence: [Student Guide Module 4](../publish/mfb-bd-26.10/mfb-bd-sg-26.10.md:1309)
- [x] **ANN-183** (source marker `[-]`) State that the aim is to help learners learn, interact with, and integrate into their local Bitcoin ecosystem/community where appropriate. — Disposition: `already-addressed` | Reviewed: 2026-09-21 | Evidence: [Student Guide Module 4](../publish/mfb-bd-26.10/mfb-bd-sg-26.10.md:1309)

#### Practical workshops and demonstrations

- [x] **ANN-184** (source marker `[-]`) Organize modules around local worker/family/merchant/community needs and remittance examples. — Disposition: `already-addressed` | Reviewed: 2026-09-21 | Evidence: [Student Guide Module 4](../publish/mfb-bd-26.10/mfb-bd-sg-26.10.md:1309)
- [x] **ANN-185** (source marker `[-]`) Keep presentation–practice–production (“perfect place”). — Disposition: `preserve-approval` | Reviewed: 2026-09-21 | Evidence: [Student Guide Module 4](../publish/mfb-bd-26.10/mfb-bd-sg-26.10.md:1309)
- [x] **ANN-186** (source marker `[o]`) Turn merchant payment flow into an educator-guide case study. — Disposition: `approved-action` | Reviewed: 2026-09-21 | Evidence: [visual index](../workspace/08_assets.md:116) | Linked action: [ACT-013](#act-013-control-visual-production-scope)
- [x] **ANN-187** (source marker `[-]`) Explain how demonstration safety changes by local conditions. — Disposition: `already-addressed` | Reviewed: 2026-09-21 | Evidence: [Student Guide Module 4](../publish/mfb-bd-26.10/mfb-bd-sg-26.10.md:1309)
- [x] **ANN-188** (source marker `[-]`) Work through the marked module questions with the community team and rewrite them. — Disposition: `needs-clarification` | Reviewed: 2026-09-21 | Evidence: [annotation provenance and confirmation rule](review_todo.md:510)

#### Local Bitcoin tools and resources

- [x] **ANN-189** (source marker `[-]`) Create a reusable local-tool comparison template; consider merging with wallet comparison. — Disposition: `already-addressed` | Reviewed: 2026-09-21 | Evidence: [Student Guide Module 4](../publish/mfb-bd-26.10/mfb-bd-sg-26.10.md:1309)
- [x] **ANN-190** (source marker `[-]`) Preserve the checked workshop-result sentence as approved. — Disposition: `preserve-approval` | Reviewed: 2026-09-21 | Evidence: [Student Guide Module 4](../publish/mfb-bd-26.10/mfb-bd-sg-26.10.md:1309)
- [x] **ANN-191** (source marker `[-]`) Move the local-tool record and guidance into the separate Module 4/educator guide; Modules 1–4 are the Diploma. — Disposition: `already-addressed` | Reviewed: 2026-09-21 | Evidence: [Student Guide Module 4](../publish/mfb-bd-26.10/mfb-bd-sg-26.10.md:1309)
- [x] **ANN-192** (source marker `[o]`) Sequence the educator materials explicitly: Module 3 items 1–3, then its Educator Guide; Module 4 should be driven by its Educator Guide. — Disposition: `already-addressed` | Reviewed: 2026-09-21 | Evidence: [Student Guide Module 4](../publish/mfb-bd-26.10/mfb-bd-sg-26.10.md:1309)

#### Daily-life Bitcoin use

- [x] **ANN-193** (source marker `[o]`) Offer separate examples/pages for Lightning, cash, custodial, single-sig, multisig, and other payment variants. — Disposition: `superseded` | Reviewed: 2026-09-21 | Evidence: [Student Guide Module 4](../publish/mfb-bd-26.10/mfb-bd-sg-26.10.md:1309)
- [x] **ANN-194** (source marker `[-]`) Keep/clarify daily-life Bitcoin use. — Disposition: `already-addressed` | Reviewed: 2026-09-21 | Evidence: [Student Guide Module 4](../publish/mfb-bd-26.10/mfb-bd-sg-26.10.md:1309)
- [x] **ANN-195** (source marker `[o]`) Add educator-guide options for earning, saving, receiving, sending, spending, accounting, and donating. — Disposition: `already-addressed` | Reviewed: 2026-09-21 | Evidence: [Student Guide Module 4](../publish/mfb-bd-26.10/mfb-bd-sg-26.10.md:1309)
- [x] **ANN-196** (source marker `[-]`) Leave optional space for other layers such as Liquid or ecash without overloading beginners. — Disposition: `superseded` | Reviewed: 2026-09-21 | Evidence: [Student Guide Module 4](../publish/mfb-bd-26.10/mfb-bd-sg-26.10.md:1309)
- [x] **ANN-197** (source marker `[o]`) Consider Value-for-Value and donation examples in the Educator Guide. — Disposition: `superseded` | Reviewed: 2026-09-21 | Evidence: [Student Guide Module 4](../publish/mfb-bd-26.10/mfb-bd-sg-26.10.md:1309)
- [x] **ANN-198** (source marker `[-]`) Preserve “Nice” and “based” annotations on the daily-life Bitcoin material as approvals. — Disposition: `preserve-approval` | Reviewed: 2026-09-21 | Evidence: [Student Guide Module 4](../publish/mfb-bd-26.10/mfb-bd-sg-26.10.md:1309)

#### Local spending and receiving scenarios

- [x] **ANN-199** (source marker `[-]`) Make jurisdiction/legal context explicit in scenarios. — Disposition: `already-addressed` | Reviewed: 2026-09-21 | Evidence: [Student Guide Module 4](../publish/mfb-bd-26.10/mfb-bd-sg-26.10.md:1309)
- [x] **ANN-200** (source marker `[o]`) Put educator notes in a distinct style and specify applicable trust, regulation, experience, infrastructure, limits, and personal-data rules. — Disposition: `already-addressed` | Reviewed: 2026-09-21 | Evidence: [Student Guide Module 4](../publish/mfb-bd-26.10/mfb-bd-sg-26.10.md:1309)
- [x] **ANN-201** (source marker `[-]`) Preserve the approval of “Avoid starting with the tool. Start with the need” and the positive response to the scenario approach. — Disposition: `preserve-approval` | Reviewed: 2026-09-21 | Evidence: [Student Guide Module 4](../publish/mfb-bd-26.10/mfb-bd-sg-26.10.md:1309)

#### Local on-ramp and off-ramp pathways

- [x] **ANN-202** (source marker `[-]`) Remove/redesign the on/off-ramp table if too technical for learners. — Disposition: `superseded` | Reviewed: 2026-09-21 | Evidence: [Student Guide Module 4](../publish/mfb-bd-26.10/mfb-bd-sg-26.10.md:1309)
- [x] **ANN-203** (source marker `[o]`) Decide whether most Module 4 content should be packaged as activities. — Disposition: `already-addressed` | Reviewed: 2026-09-21 | Evidence: [Student Guide Module 4](../publish/mfb-bd-26.10/mfb-bd-sg-26.10.md:1309)
- [x] **ANN-204** (source marker `[-]`) Preserve the strong approval of the pathway-comparison template. — Disposition: `preserve-approval` | Reviewed: 2026-09-21 | Evidence: [Student Guide Module 4](../publish/mfb-bd-26.10/mfb-bd-sg-26.10.md:1309)

#### KYC and no-KYC trade-offs where locally appropriate

- [x] **ANN-205** (source marker `[-]`) Keep KYC/no-KYC trade-offs only where locally appropriate and fact-check them. — Disposition: `already-addressed` | Reviewed: 2026-09-21 | Evidence: [Student Guide Module 4](../publish/mfb-bd-26.10/mfb-bd-sg-26.10.md:1309)
- [x] **ANN-206** (source marker `[-]`) Preserve the “VG”/“strong position” approval of the circular-economy conclusion. — Disposition: `preserve-approval` | Reviewed: 2026-09-21 | Evidence: [Student Guide Module 4](../publish/mfb-bd-26.10/mfb-bd-sg-26.10.md:1309)

#### Circular economies

- [x] **ANN-207** (source marker `[o]`) Have the circular-economy section reviewed by the named reviewer (handle unclear). — Disposition: `needs-clarification` | Reviewed: 2026-09-21 | Evidence: [annotation provenance and confirmation rule](review_todo.md:510)
- [x] **ANN-208** (source marker `[o]`) Add a stronger balanced viewpoint and graphic for circular economies. — Disposition: `approved-action` | Reviewed: 2026-09-21 | Evidence: [visual index](../workspace/08_assets.md:116) | Linked action: [ACT-013](#act-013-control-visual-production-scope)
- [x] **ANN-209** (source marker `[ ]`) Confirm whether the named reviewer is `@Reyner` and assign review only after confirmation. — Disposition: `needs-clarification` | Reviewed: 2026-09-21 | Evidence: [annotation provenance and confirmation rule](review_todo.md:510)
- [x] **ANN-210** (source marker `[o]`) Note that community custody/shared-funds material may overlap with Fedimint; decide whether it belongs in advanced educator guidance. — Disposition: `superseded` | Reviewed: 2026-09-21 | Evidence: [Student Guide Module 4](../publish/mfb-bd-26.10/mfb-bd-sg-26.10.md:1309)

#### Merchant or community use cases

- [x] **ANN-211** (source marker `[-]`) Break Module 4 into educator-selected sections (wallet, exchange, circular economy, etc.). — Disposition: `superseded` | Reviewed: 2026-09-21 | Evidence: [Student Guide Module 4](../publish/mfb-bd-26.10/mfb-bd-sg-26.10.md:1309)
- [x] **ANN-212** (source marker `[-]`) Reduce wordiness and create response space. — Disposition: `superseded` | Reviewed: 2026-09-21 | Evidence: [Student Guide Module 4](../publish/mfb-bd-26.10/mfb-bd-sg-26.10.md:1309)
- [x] **ANN-213** (source marker `[-]`) Connect merchant/community cases to jurisdiction/local context. — Disposition: `already-addressed` | Reviewed: 2026-09-21 | Evidence: [Student Guide Module 4](../publish/mfb-bd-26.10/mfb-bd-sg-26.10.md:1309)
- [x] **ANN-214** (source marker `[-]`) Expand practical field/community work where appropriate. — Disposition: `already-addressed` | Reviewed: 2026-09-21 | Evidence: [Student Guide Module 4](../publish/mfb-bd-26.10/mfb-bd-sg-26.10.md:1309)
- [x] **ANN-215** (source marker `[-]`) Keep API/technical references out of the beginner Diploma unless needed. — Disposition: `superseded` | Reviewed: 2026-09-21 | Evidence: [Student Guide Module 4](../publish/mfb-bd-26.10/mfb-bd-sg-26.10.md:1309)
- [x] **ANN-216** (source marker `[o]`) Break educator guidance into wallet, exchange, and circular-economy sections before expanding it. — Disposition: `already-addressed` | Reviewed: 2026-09-21 | Evidence: [Student Guide Module 4](../publish/mfb-bd-26.10/mfb-bd-sg-26.10.md:1309)

#### Local resource maps and community discovery

- [x] **ANN-217** (source marker `[-]`) Permit “both” for on-chain/Lightning. — Disposition: `already-addressed` | Reviewed: 2026-09-21 | Evidence: [Student Guide Module 4](../publish/mfb-bd-26.10/mfb-bd-sg-26.10.md:1309)

#### Review: how can Bitcoin function as money in your community?

- [x] **ANN-218** (source marker `[-]`) Replace generic “Need” with the specific Bitcoin/local need. — Disposition: `already-addressed` | Reviewed: 2026-09-21 | Evidence: [Student Guide Module 4](../publish/mfb-bd-26.10/mfb-bd-sg-26.10.md:1309)
- [x] **ANN-219** (source marker `[-]`) Make “Back of Diploma: Next Steps” build on earlier work and scan quickly. — Disposition: `superseded` | Reviewed: 2026-09-21 | Evidence: [Student Guide Module 4](../publish/mfb-bd-26.10/mfb-bd-sg-26.10.md:1309)
- [x] **ANN-220** (source marker `[-]`) Align the first next-step question with the opening activity. — Disposition: `superseded` | Reviewed: 2026-09-21 | Evidence: [Student Guide Module 4](../publish/mfb-bd-26.10/mfb-bd-sg-26.10.md:1309)
- [x] **ANN-221** (source marker `[-]`) Use consistent present tense in the closing review and cross-check it against page 1. — Disposition: `superseded` | Reviewed: 2026-09-21 | Evidence: [Student Guide Module 4](../publish/mfb-bd-26.10/mfb-bd-sg-26.10.md:1309)
- [x] **ANN-222** (source marker `[-]`) Make the “Back of Diploma: Next Steps” heading bolder and faster to scan. — Disposition: `superseded` | Reviewed: 2026-09-21 | Evidence: [Student Guide Module 4](../publish/mfb-bd-26.10/mfb-bd-sg-26.10.md:1309)

### Next Steps

#### A short “What now?” next-steps list

- [x] **ANN-223** (source marker `[-]`) Tie “repeat one practical skill” to concrete practice. — Disposition: `already-addressed` | Reviewed: 2026-09-21 | Evidence: [Student Guide next steps](../publish/mfb-bd-26.10/mfb-bd-sg-26.10.md:1770)
- [x] **ANN-224** (source marker `[-]`) Define “recognize a scam” and other safety tasks precisely. — Disposition: `already-addressed` | Reviewed: 2026-09-21 | Evidence: [Student Guide next steps](../publish/mfb-bd-26.10/mfb-bd-sg-26.10.md:1770)
- [x] **ANN-225** (source marker `[-]`) Separate contributing through translation, feedback, educator support, funding, and becoming an educator. — Disposition: `already-addressed` | Reviewed: 2026-09-21 | Evidence: [Student Guide next steps](../publish/mfb-bd-26.10/mfb-bd-sg-26.10.md:1770)
- [x] **ANN-226** (source marker `[-]`) Make the safety reminder scannable. — Disposition: `already-addressed` | Reviewed: 2026-09-21 | Evidence: [Student Guide next steps](../publish/mfb-bd-26.10/mfb-bd-sg-26.10.md:1770)
- [x] **ANN-227** (source marker `[-]`) Add MFB/nonprofit organizational context. — Disposition: `already-addressed` | Reviewed: 2026-09-21 | Evidence: [Student Guide next steps](../publish/mfb-bd-26.10/mfb-bd-sg-26.10.md:1770)

#### Contribute to My First Bitcoin and the Resources Hub

- [x] **ANN-228** (source marker `[-]`) Add a direct public GitHub feedback/contribution link or QR code and submission instructions. — Disposition: `already-addressed` | Reviewed: 2026-09-21 | Evidence: [Student Guide next steps](../publish/mfb-bd-26.10/mfb-bd-sg-26.10.md:1770)
- [x] **ANN-229** (source marker `[ ]`) Verify all official program, educator, community, donation, and source links. — Disposition: `approved-action` | Reviewed: 2026-09-21 | Evidence: [recurring publication checks](review_todo.md:404) | Linked action: [ACT-019](#act-019-complete-the-final-publication-verification-pass)

#### Connect with My First Bitcoin

- [x] **ANN-230** (source marker `[ ]`) Use the remaining space intentionally; confirm/add the handwritten “Thank you note.” — Disposition: `needs-clarification` | Reviewed: 2026-09-21 | Evidence: [annotation provenance and confirmation rule](review_todo.md:510)

### Handwriting requiring confirmation

- [x] **ANN-231** (source marker `[ ]`) **Safety, responsibility, and no financial advice:** confirm the wording beside the education/disclaimer paragraph. — Disposition: `needs-clarification` | Reviewed: 2026-09-21 | Evidence: [annotation provenance and confirmation rule](review_todo.md:510)
- [x] **ANN-232** (source marker `[ ]`) **Beginner monetary history from barter to digital money:** confirm details of the introductory money/app activity and historical-view note. — Disposition: `needs-clarification` | Reviewed: 2026-09-21 | Evidence: [annotation provenance and confirmation rule](review_todo.md:510)
- [x] **ANN-233** (source marker `[ ]`) **Inflation and purchasing power:** confirm the “10% / too big to fail / restructuring” note. — Disposition: `needs-clarification` | Reviewed: 2026-09-21 | Evidence: [annotation provenance and confirmation rule](review_todo.md:510)
- [x] **ANN-234** (source marker `[ ]`) **Why Bitcoin was created:** confirm the note beside Cypherpunk history. — Disposition: `needs-clarification` | Reviewed: 2026-09-21 | Evidence: [annotation provenance and confirmation rule](review_todo.md:510)
- [x] **ANN-235** (source marker `[ ]`) **Bitcoin origin timeline:** confirm the note beside Satoshi’s identity. — Disposition: `needs-clarification` | Reviewed: 2026-09-21 | Evidence: [annotation provenance and confirmation rule](review_todo.md:510)
- [x] **ANN-236** (source marker `[ ]`) **Wallets:** confirm the proposed new-column label. — Disposition: `needs-clarification` | Reviewed: 2026-09-21 | Evidence: [annotation provenance and confirmation rule](review_todo.md:510)
- [x] **ANN-237** (source marker `[ ]`) **Circular economies:** confirm the reviewer’s exact name/handle. — Disposition: `needs-clarification` | Reviewed: 2026-09-21 | Evidence: [annotation provenance and confirmation rule](review_todo.md:510)
- [x] **ANN-238** (source marker `[ ]`) **Connect with My First Bitcoin:** confirm whether the closing note says “Thank you note.” — Disposition: `needs-clarification` | Reviewed: 2026-09-21 | Evidence: [annotation provenance and confirmation rule](review_todo.md:510)

### Explicit approvals

- [x] **ANN-239** (source marker `[-]`) **Seed phrases:** preserve the seed-backup checklist approved with “Love it.” — Disposition: `preserve-approval` | Reviewed: 2026-09-21 | Evidence: [seed-phrase checklist:1043](../publish/mfb-bd-26.10/mfb-bd-sg-26.10.md:1043#seed-phrases)
- [x] **ANN-240** (source marker `[-]`) **Educator-selected local modules:** preserve the local-learning-choice table approved with “I like this.” — Disposition: `preserve-approval` | Reviewed: 2026-09-21 | Evidence: [local Module 4 learner record:1336](../publish/mfb-bd-26.10/mfb-bd-sg-26.10.md:1336#your-local-module-4)
- [x] **ANN-241** (source marker `[-]`) **Practical workshops and demonstrations:** preserve presentation/practice/production, marked “perfect place.” — Disposition: `preserve-approval` | Reviewed: 2026-09-21 | Evidence: [Educator Guide progression:863](../publish/mfb-bd-26.10/mfb-bd-eg-26.10.md:863#use-presentation--practice--production)
- [x] **ANN-242** (source marker `[-]`) **Local Bitcoin tools and resources:** preserve the checked workshop-result sentence. — Disposition: `preserve-approval` | Reviewed: 2026-09-21 | Evidence: [local tool record:1399](../publish/mfb-bd-26.10/mfb-bd-sg-26.10.md:1399#local-bitcoin-tools-and-resources)

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
