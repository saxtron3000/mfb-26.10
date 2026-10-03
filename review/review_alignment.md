# Mission and content alignment review script

## Purpose and use

Act as an independent curriculum reviewer for the Bitcoin Diploma 2026.10. Test whether the project delivers open-source, community-led, Bitcoin-only education that helps beginners reason and act safely. Run the prompts below in order. Improve alignment through evidence and approved authorities, not through stronger promotional claims.

This file is a review control, not a curriculum authority or source of truth. The project’s sources of truth are the documents in `workspace/`, as located and ordered by [workspace/00_index.md](../workspace/00_index.md). The `publish/` directory supplies implementation evidence; `review/` records controls, findings, decisions, and provenance. The `assets/` directory holds production assets and their working references, while `public/` holds public briefs and presentation sources. If workspace authorities conflict, identify the conflict and log it in [review_todo.md](review_todo.md); do not resolve it by treating this script, a past review, or an action-register item as policy.

Use this opening prompt: “Run this alignment review in the selected mode and scope. Treat `workspace/` as the source of truth, compare publications only as implementation evidence, and record findings and verification needs in the dated run record and [review_todo.md](review_todo.md). Preserve learner choice and do not invent approvals.” If asked for review only, report proposed changes without applying them.

Use [review_style.md](review_style.md) for prose editing. These scripts are repeatable instructions, not replacement curriculum authorities.

## Review mode

Select one mode before starting:

| Mode | Use | Minimum scope |
| --- | --- | --- |
| Change review | A bounded change to one or more files. | Changed files, their governing workspace authorities, affected publications, and relevant link-register rows. |
| Targeted review | One stated concern, such as assessment, safety, terminology, links, or a decision ID. | The named concern, its authorities, affected publications, and open related findings. |
| Full release review | A release candidate or major redesign checkpoint. | Every `workspace/` and `publish/` document or publication data file, both link registers, the traceability matrix, and all release-critical controls. |

If the requester asks to review recent changes, synchronization, propagation, or regression, that request selects **Change review** mode. Otherwise, if the requester does not specify a mode, ask which mode they want before starting. Do not silently default to a full review or make a mode choice on their behalf. Record the selected mode, scope, baseline, and source version in a dated run record created from [runs/template.md](runs/template.md).

### Recent-change synchronization protocol

Use this protocol for every Change review. Its purpose is semantic synchronization: related documents must express the same approved decision while preserving their different audiences and functions. Do not make documents identical or copy planning prose into publications.

1. Establish the comparison baseline before reviewing content. Use the requester-specified commit, branch, date, or file set when supplied; otherwise use the source version in the latest applicable completed run record. If neither exists, inspect the working-tree changes and the most recent relevant commit or commits, state that bounded assumption, and do not describe it as a complete historical audit. Include staged, unstaged, renamed, deleted, and untracked in-scope files.
2. Create a changed-proposition inventory in the dated run record. Assign each substantive change a stable `CHG-` ID and record the originating file and heading, old meaning, new meaning, governing authority, approval or decision evidence, and likely dependent documents. Include changed numbers, requirements, statuses, terminology, names, links, paths, headings or anchors, learner promises, ownership boundaries, assessment rules, and release claims; a filename-only list is insufficient.
3. Build an impact map for each `CHG-` item before editing. Trace from the governing authority to direct implementation files and then to secondary summaries, indexes, registers, public communications, activities, assessment records, optional resources, and review controls. Also trace backwards from a changed publication or summary to its governing authority. Search the whole repository for the former wording and plausible variants, not only exact copied sentences.
4. Classify every occurrence as `update required`, `already aligned`, `intentional audience-specific difference`, `historical record`, `not applicable`, or `conflict`. Record the reason and evidence for every intentional difference, historical retention, or not-applicable result. Do not rewrite quotations, archived evidence, or decision history merely because they contain older wording; label their historical status when ambiguity is possible.
5. Propagate only approved changes. If a publication, summary, or activity changed before its authority, compare it with the current authority and approval record. Update the authority first when the new meaning is approved; otherwise restore alignment or log an `EVO-` or `PUB-` conflict and request the required decision. Never treat repetition across several dependent files as evidence of approval.
6. After each reconciliation pass, inspect the new diff and repeat the impact search for every file or proposition changed by the reconciliation. Continue until this fixed-point check finds no newly affected document. Recheck cross-references, anchors, link registers, asset references, status summaries, and counts whenever the change could affect them.
7. A Change review passes synchronization only when every `CHG-` item has a recorded disposition, every required dependent update is implemented or linked to an open finding, no unexplained stale variant remains in active material, and the final changed-file set has been rechecked. Report partial synchronization as incomplete; do not say that all documents are synchronized on the strength of spot checks.

## Prompt 1: Establish authority and review scope

Read [AGENTS.md](../AGENTS.md) and the [workspace index](../workspace/00_index.md). Use [06_plan.md](../workspace/06_plan.md) for architecture and boundaries, [05_competencies.md](../workspace/05_competencies.md) for assessed competencies and decimal criteria, [13_assessment.md](../workspace/13_assessment.md) for assessment, [15_certification.md](../workspace/15_certification.md) for eligibility and governance, and [16_spec.md](../workspace/16_spec.md) for publication guardrails. Consult scope, research, design, content, asset, resource, activity, educator, microlearning, Advanced, and horizon plans when relevant. Where workspace documents conflict, preserve the conflict as an `EVO-` finding and request an authorized decision.

Compare those authorities with the [Student Guide](../publish/mfb-bd-26.10/mfb-bd-sg-26.10.md), [Educator Guide](../publish/mfb-bd-26.10/mfb-bd-eg-26.10.md), [Assessment Grid](../publish/mfb-bd-26.10/mfb-bd-assessment-grid-26.10.md), [lexicon](../publish/mfb-lx-26.10-sg-index.md), [optional self-check](../publish/mfb-ml-26.10/mfb-ml-26.10.md), and affected public materials. Treat material in `assets/reference/`, `assets/briefs/`, `y_old-promps/`, and imported annotations as review inputs, not approved policy.

### Folder-name and repository-scope check

At the start of every review, inventory directories from the repository root and record the date and result in the run record. Use each directory name exactly as it exists, including hyphens, underscores, plural forms, edition suffixes, and the intentionally retained name `y_old-promps/`; do not substitute nonexistent names such as `ref/` or `feedback/`. Treat a missing expected directory, a stale path, a wrongly cased path, or a reference that assigns a folder the wrong role as a maintenance finding. Re-run the inventory after a move, rename, or structural change and before a Full release review conclusion.

The following is the repository inventory verified on 2026-09-25. It includes every directory below the repository root at that time; `.` denotes the root itself.

| Exact directory path | Review treatment |
| --- | --- |
| `.` | Repository root; resolve all repository-relative paths from here. |
| `.claude/` | Local Claude configuration; exclude from curriculum and publication evidence unless the review specifically concerns local agent configuration. |
| `.codex-git-tmp/`, `.codex-tmp/`, `.tmp/` | Tool-managed temporary directories; exclude from curriculum, publication, and source-of-truth evidence. Do not create durable references to them. |
| `assets/` | Asset-production materials; inspect when visuals, rights, alt text, asset IDs, or production workflow are in scope. |
| `assets/briefs/` | Asset briefs; working production input, not an approved curriculum authority. |
| `assets/prompts/` | Asset-production prompt contracts; working input, not an approved curriculum authority. |
| `assets/reference/` | Asset reference material; review input, not approved curriculum policy. |
| `assets/style/` | Active visual-style sources for asset production and review. |
| `assets/style/bible/`, `assets/style/layouts/` | Character-reference boards and layout studies used with `assets/style/` when reviewing visuals. |
| `links/` | Canonical link-maintenance registers: [internal My First Bitcoin links](../links/links-internal.md) and [external or other links](../links/links-external.md). Inspect them whenever an in-scope link changes. |
| `public/`, `public/assets/` | Public briefs, presentation sources, and their public asset location; inspect affected materials and paths when public claims or releases are in scope. |
| `publish/` | Publication implementation evidence; never treat it as the authority when it conflicts with `workspace/`. |
| `publish/mfb-act-26.10/` | Activity publications. |
| `publish/mfb-adv-26.10/` | [Advanced Learning](https://curriculum.myfirstbitcoin.org/programs/advanced-modules/) publications, outside the required Diploma pathway. |
| `publish/mfb-bd-26.10/` | Bitcoin Diploma publications, including the Student Guide, Educator Guide, Assessment Grid, lexicon, and question set. |
| `publish/mfb-ml-26.10/` | Optional microlearning self-check publication and question data. |
| `review/`, `review/runs/` | Review controls, findings, provenance, and dated run records; neither is a curriculum authority. |
| `workspace/` | Active planning and source-of-truth documents. |
| `y_branding/`, `y_branding/design-system/` | Brand reference and design-system material; consult when an in-scope visual or brand decision requires it, without elevating it above a governing workspace authority. |
| `y_old-promps/` | Archived prompt material; retain the existing spelling and treat it as historical input, not current authority. |

In a Change or Targeted review, check the names and roles of every directory touched by the scope and the complete inventory for stale references. In a Full release review, check the existence, spelling, and role of every directory in this table. Update this table only after recording the structural change and verifying the new tree; do not infer a rename from a broken reference.

For a Full release review, read the complete `workspace/` in ascending numerical filename order, starting with the `00_` documents and continuing through `19_`, then read both link registers in `links/`. For a Change review, read every changed document, its governing authorities, every dependent document identified through the recent-change synchronization protocol, and enough surrounding evolution context to establish the change's meaning; still search the whole repository for affected propositions and stale variants. Treat the ordered pass as an evolution trace: compare each in-scope document's purpose, terminology, decisions, boundaries, ownership, learner or educator promises, assessment model, release position, and link policy with the relevant preceding and source-of-truth documents. Identify inconsistencies, unexplained reversals, duplicated or diverging ideas, stale assumptions, and gaps between an earlier decision and its later implementation. Do not flag an intentional difference when its authority and reason are clear; record the evidence that establishes the distinction instead.

For each inconsistency found in this ordered pass, create or update a detailed `EVO-` entry in the [workspace and publication development findings log](review_todo.md#workspace-and-publication-development-findings-log) before changing dependent content. Include the review date and scope; the earlier and later file/heading; the conflicting or missing development; why it matters; the relevant authority or evidence; affected files; recommended next action; status; owner; and completion evidence required. Report all open, blocked, or needs-verification `EVO-` entries in the review result. Do not silently reconcile a policy, scope, safety, assessment, or publication conflict.

Create or update the traceability matrix in the dated run record before reaching a conclusion. Give every tested requirement a stable `TR-` ID and record: governing workspace file/heading; requirement or decision; expected publication or operational evidence; actual file/heading or other evidence; state (`implemented`, `intentionally deferred`, `not applicable`, `missing`, or `conflict`); verification method and date; and linked `ACT-`, `EVO-`, or `PUB-` ID. The matrix is an audit aid, not a new authority.

For each finding, distinguish implemented behavior, regression, publication decision, release blocker, maintenance action, historical proposal, and unknown. Date the review and cite current file sections. Do not present the 2026-09-01 report or 2026-08-19 decision log as a fresh audit.

## Prompt 2: Review workspace development and consolidation

Review every in-scope document in `workspace/` as one connected design system after completing the ordered evolution trace. Test system completeness through the traceability matrix: each planned component has a clear purpose, owner, boundary, decision, dependency, and next implementation location; key ideas are defined once, developed to the needed level, and consolidated consistently across the relevant plans; and no essential idea remains only implied, duplicated without an authority, parked without a disposition, or dependent on a stale assumption, placeholder, or unresolved conflict.

Trace each significant idea from its originating or authoritative workspace document through every relevant workspace document. Test, at minimum, the four-module pathway, competencies and evidence, safety boundaries, learner and educator roles, assessment and certification, activity and resource boundaries, optional self-check, publication formats, assets, link maintenance, localization, Advanced content, and release readiness. Confirm that an intentional difference has a recorded reason and owner; do not create content, policy, or approvals merely to make documents appear complete.

Log every workspace-development gap, incomplete idea, missing consolidation, or unexplained inconsistency as a detailed `EVO-` entry in the [workspace and publication development findings log](review_todo.md#workspace-and-publication-development-findings-log). Include its source and affected workspace files/headings, evidence, learner or educator consequence, required decision or action, dependencies, status, owner, and completion evidence. Report all unresolved `EVO-` entries at the end of the review.

## Prompt 3: Review publication implementation against workspace

Review every in-scope document and publication data file in `publish/`. Compare each publication with the applicable workspace authorities, plans, specifications, asset register, [internal My First Bitcoin link register](../links/links-internal.md), [external or other link register](../links/links-external.md), and source-of-truth map. Use the traceability matrix to test implementation: required learner content, educator guidance, assessment record, terminology, safety limits, module boundaries, optional-resource status, local adaptation rules, accessibility and low-tech routes, links, visual requirements, and release positioning must be reflected accurately in the correct publication without introducing unsupported promises or duplicating planning-only material.

Check lexicon integration in both the Student Guide and Educator Guide. Confirm that each term or word designated for the [lexicon](../publish/mfb-lx-26.10-sg-index.md) is linked to its current lexicon entry where it appears in those guides. Then verify that every source-line reference recorded in the lexicon still points to the current relevant line in its source publication; update stale references and log any unclear or missing reference as a `PUB-` finding.

For every workspace-to-publication requirement, establish whether it is implemented, intentionally deferred, not applicable, or missing. Check that publications agree with one another where they share a learner promise, competency, safety instruction, link, or public claim. Do not treat a plan as implemented merely because it exists in `workspace/`; require visible, appropriate publication evidence or an approved deferral.

Log every missing implementation, publication regression, divergence from an authority, unsupported claim, or unapproved deferral as a detailed `PUB-` entry in the [workspace and publication development findings log](review_todo.md#workspace-and-publication-development-findings-log). Include the governing workspace file/heading, affected publication file/heading, exact gap, impact, required action or decision, dependencies, status, owner, and completion evidence. Report all unresolved `PUB-` entries at the end of the review. Update workspace authorities before changing a publication when the gap is a policy or design decision rather than an implementation error.

## Prompt 4: Test the mission and all six community principles

Use the charter's mission, “Open source Bitcoin Education for the World,” as the test. Check that anyone, anywhere can teach with the fully open-source curriculum and use, adapt, and translate it without permission or network membership, and that high-quality education is accessible across schools, universities, churches, and local communities. Preserve the charter's welcome and wish for success to those who build independently, and its recognition that diverse approaches and learning from peers strengthen Bitcoin education.

Apply each principle separately:

| Principle | Questions to apply to the content |
|---|---|
| Independent | Does all education remain independent of outside influence and free from commercial influence? Communities may accept and publicly acknowledge sponsors, but sponsors must never influence instruction, materials, or curriculum. Does the text avoid promoting specific wallets, exchanges, financial products, or investment strategies and focus on understanding Bitcoin and the monetary system? Does it teach how to think, not what to think? |
| Impartial | Are evidence, interpretation, preference, and uncertainty distinguishable? Can learners reach a different conclusion, including choosing not to adopt Bitcoin? |
| Community-based | Can autonomous communities choose leadership, operations, fundraising, local strategy, methods, events, and outreach? Does teaching respond to classroom and local needs rather than outside political or institutional pressure? |
| Bitcoin-only | Does the curriculum center on Bitcoin, using financial literacy and comparisons with other systems only to aid understanding? Does it avoid turning into a general cryptocurrency course? |
| Empowerment over profits | Does learning present Bitcoin as a tool for individual freedom and long-term empowerment, build understanding of an open monetary network, and explain how it can increase individual sovereignty? Remove trading instruction, price predictions, investment strategies, and profit promises. |
| Quality | Does the education meet a commitment to educational excellence through accurate, engaging, and impactful teaching? Preserve onboarding and guidance from experienced network members for new communities to establish a strong foundation and maintain high standards, alongside review and evidence of learning. |

Check both explicit claims and implied incentives. Bold mission language must not become coercion, predetermined conclusions, hostility, or an unsupported claim that Bitcoin solves every money problem.

## Prompt 5: Preserve the charter's organizational boundaries

When reviewing descriptions of the Bitcoin Education Network, preserve these distinctions from the archived community charter source:

- The charter describes a relationship between the identified community and the Bitcoin Education Network initiated by My First Bitcoin, a nonprofit dedicated to creating and maintaining open-source Bitcoin education. The community uses the materials independently in its local context.
- The network connects and supports independent communities; My First Bitcoin initiated it but does not run each community. Sharing knowledge, best practices, and resources aims to accelerate Bitcoin education worldwide while preserving each community's independence.
- Joining is optional and communities aligned with the principles may apply. Applying for the Leaderboard requires signing the six-principle charter, demonstrating active local Bitcoin education, and completing onboarding. Accepted communities are equal members; reputation reflects the quality and consistency of their demonstrated work, is publicly reflected on the Leaderboard, and may unlock opportunities, support, or collaborations.
- Possible benefits include a public profile and directory listing; personalized onboarding and continuing support from the My First Bitcoin team; website, social media, newsletter, and podcast features; fundraising resources, operational guides, and community-building tools; invitations to collaborate on initiatives, events, and conferences; eligibility for additional educational, technical, and community support as new programs become available; and potential My First Bitcoin Board of Advisors (BoA) participation alongside other top communities and thought leaders.
- Benefits, eligibility, reputation rules, and Leaderboard structure may evolve. Do not promise them as automatic entitlements. Verify current claims against the [Leaderboard](https://leaderboard.myfirstbitcoin.org/) and [organization information](https://myfirstbitcoin.org/about) before publication.
- My First Bitcoin's stated commitments are to maintain and improve the open-source curriculum, share resources and best practices, offer appropriate onboarding, encourage collaboration, maintain the Leaderboard, and recognize demonstrated work and reputation.
- Community commitments are to uphold the six principles, operate independently within the mission, provide honest and impartial Bitcoin-only education, represent work truthfully, continue actively educating people locally, and recognize that My First Bitcoin determines Leaderboard participation, recognition, and additional opportunities through demonstrated contribution, reputation, and alignment with the principles.
- The charter continues until either party ends participation. My First Bitcoin may also end participation for failure to uphold principles or when collaboration is no longer appropriate. The charter reflects the full understanding between the parties, supersedes previous agreements or understandings about that relationship, and requires written agreement by both parties for changes.
- The source's signature fields cover My First Bitcoin's representative, title, date, and signature, plus the community name, country/region, representative, title, date, and signature. Keep these in the charter workflow, not in course completion requirements.

Do not rewrite charter terms or imply that a curriculum review grants network membership, legal approval, or organizational commitments. Preserve the source charter as the exact reference for relationship and signature wording.

## Prompt 6: Check architecture, scope, and content ownership

Verify the four-stage Problem → Solution → Action → Connect sequence and all four required modules. **Module 4: Bitcoin in Your Community** is educator-selected and locally relevant, with required `C11` evidence. It connects prior learning to a real local need or opportunity, a realistic alternative, safe practice, and a responsible next step. [Advanced Learning](https://curriculum.myfirstbitcoin.org/programs/advanced-modules/) is outside the Diploma.

Keep learner prose in the Student Guide; facilitation in the Educator Guide; detailed activities on the [Resources Hub](https://programs.myfirstbitcoin.org/resources/); educator records in the Assessment Grid; and planning support in the workspace. Avoid duplicating authorities or embedding production notes in publications.

Keep the beginner pathway bounded. Move deeper economic, historical, technical, philosophical, and organizational material to Advanced or educator context when appropriate. Do not add historical annotation suggestions automatically. Preserve an offline, low-tech route and translation-ready source. A device, connectivity, purchase, personal funds, or app use must not become a completion requirement.

Review the current status and implementation of all 12 consistency topics in the to-do decision register: duration, assessment meaning, four-module completion, supported practical promise, first access, Lightning boundaries, October outputs, wallet-software guidance, programme links, canonical manuscript, certificate position, and operational release readiness. Regression-check resolved decisions, preserve deliberately deferred questions as deferred, and check current evidence before requesting a new decision. Do not repeat a historical conflict as current when later evidence shows that it was resolved.

## Prompt 7: Check facts, balance, and source maintenance

Verify economic, banking, historical, Bitcoin, security, and technical claims against appropriate authoritative sources. Use qualified review for specialist uncertainties; do not claim an expert or legal review happened when it did not. Date and cite changing claims or replace them with evergreen explanations.

Test beginner explanations for these recurring risks: a universal linear monetary history; unsourced monetary or geopolitical claims; unclear fiat, deposits, liabilities, and bank-created money; subjective value presented as universal; conflating assets and money; speculative origin stories; issuer, subsidy, supply, halving, consensus, and irreversibility errors; conflating the network with services; claiming wallets contain bitcoin rather than coordinate keys and transactions; and ignoring privacy, custody, recovery, or Lightning trade-offs.

Keep the required Bitcoin, stablecoin, and other crypto-asset comparison educational and bounded. Distinguish known issuance facts from uncertain adoption, price, or scaling claims. Explain alternatives and limitations fairly. Do not provide financial, legal, tax, accounting, compliance, or investment advice.

Use the shared resource register for common claims, with claim/section, source type and authority, volatility, reviewer, check date, next review date, and publication treatment. Keep genuinely local facts in the educator local-verification record. Recheck tools, fees, laws, services, CBDCs, statistics, energy claims, transaction comparisons, merchants, providers, and adoption examples before publication or a cohort when relevant. Retain stable anchors or claim IDs rather than line-number maintenance.

## Prompt 8: Check competencies and assessment integrity

Map every required competency and decimal criterion to teaching, approved individual evidence, an assessment task, a rubric, and a record field. Verify the Educator Guide crosswalk and Assessment Grid agree.

Preserve educator-evaluated theory `C1`–`C8` and directly observed practice `C9`–`C11`. The 50%/50% model means two equal-status, non-compensatory completion gates. All required competencies and safety criteria must meet standard; no combined numerical grade is approved. Attendance, confidence, self-report, app use, or an unapproved formative activity cannot replace evidence.

Check `T1`–`T3` theory interactions and `P9`–`P11` practice, permitted support, safety-critical errors, equivalent routes, reassessment, calibration, moderation, and record keeping. Preserve the supported, low-stakes or simulated `C9.3` first-access requirement without requiring purchases, meaningful personal funds, secrets, device ownership, or app use.

Check that local adaptations preserve the learner action, safety boundary, support limit, and evidence standard. Keep recovery practice private and within approved safe training conditions. Verify the required on-chain/Lightning distinction separately from any locally selected Lightning use.

## Prompt 9: Check delivery feasibility and certificate claims

Do not equate a written protocol with validated delivery. Prioritize validating and simplifying the existing system rather than adding curriculum topics, as the report recommends. Before claiming certificated readiness, require the selected local `P11` variant, training environment, low-tech and accessibility equivalents, assessors, contingency route, and capacity calculation for the actual cohort and assessor ratio. Include individual evidence, resets, transitions, feedback, reassessment, and records in timing.

Require a pilot with planned and actual time by module and evidence task, safety issues, access failures, misunderstandings, and reassessment demand. Require one annotated meets-standard (`MS`) and one not-yet (`NY`) example for `T2`, `P9`, and the selected `P11`, plus documented assessor calibration and resolution of disagreements.

Before retaining competency evidence for a pilot or certificated delivery, require proportionate local governance appropriate to the delivery context: clear identification of the educator or issuing organization; permitted data; consent or assent; access, retention, deletion, and security arrangements; correction, appeal, incident, outage, accessibility, exceptional-case, minors, and safeguarding routes where applicable; and any issuer-offered replacement, withdrawal, or verification process. Preserve the decentralized educator-issued model: My First Bitcoin does not centrally evaluate learners, issue certificates, operate a central verification service, or guarantee competency. Treat shared verification, audit, revocation, or credential infrastructure as optional future work unless a later approved authority changes that boundary.

Distinguish teaching-package readiness, publication readiness, validated assessment delivery, and operational certificate issuance. Resolve duration and certificate promises in the authorities and public wording together.

## Prompt 10: Check optional resources and publication promises

Keep the [My First Bitcoin App](https://myfirstbitcoin.app/) voluntary for self-check, recap, discovery, and future-learning connection. It supplies no assessment evidence and creates no certification gate. The 12-question check samples selected content from Modules 1–3; it does not establish Module 4 or practical competence. Keep result wording limited to that check. Do not introduce score tracking, thresholds, or educator access. Require independent factual/editorial review, small-phone testing, and screen-reader testing before release.

Keep named programme links and general wallet-software guidance within the approved publication policy. Explain openness alongside custody, recovery, safety, compatibility, privacy, continuity, and local support without global product endorsement. Keep programme participation optional and changing links maintained.

Check teaching slides are editable, aligned, adaptable to learners, language, and local context, and supportive of discussion and practice. Teaching must remain possible without projection. Resolve conditional source/update, donation/support, and verification back matter before release. Verify destinations and processes before commissioning related QR or certificate visuals. Track essential visuals, rights, alt text, source, and review status.

## Prompt 11: Reconcile findings and validate the result

Before finalising the review, audit cross-references. Files in `workspace/` may link internally only to active material in `workspace/`, `review/`, `publish/`, or `assets/`; treat a link to a tool-managed, archived, or branding directory as an exception that needs an explicit review purpose. Files in `publish/` must never link to `workspace/`, `review/`, `assets/`, or any other repository-only document. Every document link in `publish/` must use a verified public HTML URL; replace a repository-only link with its public page, or remove it when no suitable public page exists. Recheck Markdown links, reference-style definitions, and inline HTML links after every publication edit.

Treat link integrity as release-critical. Use and maintain the [internal My First Bitcoin link review index](../links/links-internal.md) for `myfirstbitcoin.org` and its subdomains, and the [external or other link review index](../links/links-external.md) for destinations outside that boundary and local document or section links. Use both registers in every alignment review and whenever a guide, publication URL, linked text, anchor, or destination changes. Update the applicable index with the current snapshot date, complete source locations, destinations, and review status; do not leave a changed or newly added link absent from its register. Test every destination and its intended purpose before release. A broken, mistargeted, inaccessible, or unreviewed required link is a release blocker until it is corrected, removed, or explicitly recorded with an approved exception.

Keep review ownership distinct: the style review owns wording, formatting, and local Markdown mechanics; this alignment review owns authority, public-URL policy, link purpose, and release impact; and the two link registers are the canonical inventory and dated verification evidence. Refer an issue to its owner rather than duplicating the same finding in both scripts.

For an external or objective claim, destination, process, or current fact, create a self-contained verification prompt in the run record and include it in the review report for an internet-connected AI agent. The prompt must name the exact claim or URL, intended purpose, required primary or authoritative sources, date of check, acceptance condition, and required evidence: source title, direct URL, relevant result or quotation within copyright limits, check date, and pass/fail or uncertainty outcome. Do not mark the item verified until that evidence is returned and recorded. For an internal or subjective judgement, verification is the editor’s discretion: record the editor’s decision, rationale, date, and any supporting internal evidence, and do not mislabel it as external verification.

For approved policy changes, update architecture, competencies, assessment, and certification authorities first; then delivery publications and activity specifications; then scope, design, content plan, overview, and horizon; then the index, lexicon, resource register, review controls, public communications, and published outputs as applicable. Use the recent-change synchronization protocol to determine the actual impact set; do not assume that this list is exhaustive, and do not silently choose between contradictory authorities.

For each finding, report the file/section, evidence, relevant principle or criterion, consequence for learners or educators, recommended action, and completion evidence needed. Reuse to-do IDs; distinguish a new action from a resolved decision or historical suggestion. Keep historical approvals and unclear handwriting separate from active tasks.

End the dated run report with `## Review report summary` as its final section. Under that exact heading, summarise the scope/date, baseline and final source version, `CHG-` inventory and dispositions, files changed, unresolved decisions, release blockers, validation performed, and checks not performed. State whether the fixed-point synchronization check passed and that the run record is not a source of truth. Do not place any section or content after this summary. Do not claim repository-wide synchronization, external verification, rendering, accessibility testing, real-cohort validation, or human approval when the recorded evidence does not support it. Re-run only to resolve substantive findings or examine changed material; do not reopen settled policy without new evidence or an authorized policy change.

## Source coverage

This script consolidates the archived community charter, consistency decisions, quality checks, report findings, and action register into repeatable review controls. It preserves the mission, six principles, network context, membership, benefits, commitments, termination/change rules, signature context, policy questions, reconciliation order, assessment, delivery, publication, and quality requirements. The active sources of truth remain in `workspace/`; this script and [review_todo.md](review_todo.md) provide review controls, findings, and historical provenance only. All individual annotations and legacy decision alternatives are retained in [review_todo.md](review_todo.md), with provenance and status limits.
