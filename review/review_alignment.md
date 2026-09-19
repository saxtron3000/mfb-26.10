# Mission and content alignment review script

## Purpose and use

Act as an independent curriculum reviewer for the Bitcoin Diploma 2026.10. Test whether the project delivers open-source, community-led, Bitcoin-only education that helps beginners reason and act safely. Run the prompts below in order. Improve alignment through evidence and approved authorities, not through stronger promotional claims.

Use this opening prompt: “Run this alignment review on the specified scope, or the current Diploma package if no scope is given. Compare the current authorities and publications, correct supported inconsistencies within the authorized scope, and record unresolved decisions and actions in [review_todo.md](review_todo.md). Preserve learner choice and do not invent approvals.” If asked for review only, report proposed changes without applying them.

Use [review_style.md](review_style.md) for prose editing. These scripts are repeatable instructions, not replacement curriculum authorities.

## Prompt 1: Establish authority and review scope

Read [AGENTS.md](../AGENTS.md) and the [workspace index](../workspace/00_index.md). Use [06_plan.md](../workspace/06_plan.md) for architecture and boundaries, [05_competencies.md](../workspace/05_competencies.md) for assessed competencies and decimal criteria, [13_assessment.md](../workspace/13_assessment.md) for assessment, [15_certification.md](../workspace/15_certification.md) for eligibility and governance, and [16_spec.md](../workspace/16_spec.md) for publication guardrails. Consult scope, research, design, content, asset, resource, activity, educator, microlearning, Advanced, and horizon plans when relevant.

Compare those authorities with the [Student Guide](../publish/mfb-bd-26.10/mfb-bd-sg-26.10.md), [Educator Guide](../publish/mfb-bd-26.10/mfb-bd-eg-26.10.md), [Assessment Grid](../publish/mfb-bd-26.10/mfb-bd-assessment-grid-26.10.md), [lexicon](../publish/mfb-bd-26.10/mfb-bd-lx.md), [optional self-check](../publish/mfb-ml-26.10/mfb-ml-26.10.md), and affected public materials. Treat reference, feedback, and imported annotations as review inputs, not approved policy.

For each finding, distinguish implemented behavior, regression, publication decision, release blocker, maintenance action, historical proposal, and unknown. Date the review and cite current file sections. Do not present the 2026-09-01 report or 2026-08-19 decision log as a fresh audit.

## Prompt 2: Test the mission and all six community principles

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

## Prompt 3: Preserve the charter's organizational boundaries

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

## Prompt 4: Check architecture, scope, and content ownership

Verify the four-stage Problem → Solution → Action → Connect sequence and all four required modules. **Module 4: Bitcoin in Your Community** is educator-selected and locally relevant, with required `C11` evidence. It connects prior learning to a real local need or opportunity, a realistic alternative, safe practice, and a responsible next step. Advanced Learning is outside the Diploma.

Keep learner prose in the Student Guide; facilitation in the Educator Guide; detailed activities on the [Resources Hub](https://programs.myfirstbitcoin.org/resources/); educator records in the Assessment Grid; and planning support in the workspace. Avoid duplicating authorities or embedding production notes in publications.

Keep the beginner pathway bounded. Move deeper economic, historical, technical, philosophical, and organizational material to Advanced or educator context when appropriate. Do not add historical annotation suggestions automatically. Preserve an offline, low-tech route and translation-ready source. A device, connectivity, purchase, personal funds, or app use must not become a completion requirement.

Review all 12 consistency topics in the to-do decision register: duration, assessment meaning, four-module completion, supported practical promise, first access, Lightning boundaries, October outputs, wallet-software guidance, programme links, canonical manuscript, certificate position, and operational release readiness. Check current evidence before requesting a decision. The September consolidation found current scope and specification documents describing Sanity-published online PDF and web outputs while the architecture still included future-branch language; resolve the remaining inconsistency without assuming the old A/B question is untouched.

## Prompt 5: Check facts, balance, and source maintenance

Verify economic, banking, historical, Bitcoin, security, and technical claims against appropriate authoritative sources. Use qualified review for specialist uncertainties; do not claim an expert or legal review happened when it did not. Date and cite changing claims or replace them with evergreen explanations.

Test beginner explanations for these recurring risks: a universal linear monetary history; unsourced monetary or geopolitical claims; unclear fiat, deposits, liabilities, and bank-created money; subjective value presented as universal; conflating assets and money; speculative origin stories; issuer, subsidy, supply, halving, consensus, and irreversibility errors; conflating the network with services; claiming wallets contain bitcoin rather than coordinate keys and transactions; and ignoring privacy, custody, recovery, or Lightning trade-offs.

Keep the required Bitcoin, stablecoin, and other crypto-asset comparison educational and bounded. Distinguish known issuance facts from uncertain adoption, price, or scaling claims. Explain alternatives and limitations fairly. Do not provide financial, legal, tax, accounting, compliance, or investment advice.

Use the shared resource register for common claims, with claim/section, source type and authority, volatility, reviewer, check date, next review date, and publication treatment. Keep genuinely local facts in the educator local-verification record. Recheck tools, fees, laws, services, CBDCs, statistics, energy claims, transaction comparisons, merchants, providers, and adoption examples before publication or a cohort when relevant. Retain stable anchors or claim IDs rather than line-number maintenance.

## Prompt 6: Check competencies and assessment integrity

Map every required competency and decimal criterion to teaching, approved individual evidence, an assessment task, a rubric, and a record field. Verify the Educator Guide crosswalk and Assessment Grid agree.

Preserve educator-evaluated theory `C1`–`C8` and directly observed practice `C9`–`C11`. The 50%/50% model means two equal-status, non-compensatory completion gates. All required competencies and safety criteria must meet standard; no combined numerical grade is approved. Attendance, confidence, self-report, app use, or an unapproved formative activity cannot replace evidence.

Check `T1`–`T3` theory interactions and `P9`–`P11` practice, permitted support, safety-critical errors, equivalent routes, reassessment, calibration, moderation, and record keeping. Preserve the supported, low-stakes or simulated `C9.3` first-access requirement without requiring purchases, meaningful personal funds, secrets, device ownership, or app use.

Check that local adaptations preserve the learner action, safety boundary, support limit, and evidence standard. Keep recovery practice private and within approved safe training conditions. Verify the required on-chain/Lightning distinction separately from any locally selected Lightning use.

## Prompt 7: Check delivery feasibility and certificate claims

Do not equate a written protocol with validated delivery. Prioritize validating and simplifying the existing system rather than adding curriculum topics, as the report recommends. Before claiming certificated readiness, require the selected local `P11` variant, training environment, low-tech and accessibility equivalents, assessors, contingency route, and capacity calculation for the actual cohort and assessor ratio. Include individual evidence, resets, transitions, feedback, reassessment, and records in timing.

Require a pilot with planned and actual time by module and evidence task, safety issues, access failures, misunderstandings, and reassessment demand. Require one annotated meets-standard (`MS`) and one not-yet (`NY`) example for `T2`, `P9`, and the selected `P11`, plus documented assessor calibration and resolution of disagreements.

Before retaining competency evidence for a pilot or certification, require the approved governance pack: issuer and approval authority; permitted data, consent or assent, access roles, retention and deletion; correction, appeal, incident, outage, and exceptional-case routes; assessor permissions, moderation, reconciliation, and audit trail; certificate issue, replacement, revocation, and verification; minors and safeguarding. Do not invent an approval or promise a verification service that does not exist.

Distinguish teaching-package readiness, publication readiness, validated assessment delivery, and operational certificate issuance. Resolve duration and certificate promises in the authorities and public wording together.

## Prompt 8: Check optional resources and publication promises

Keep the [My First Bitcoin App](https://myfirstbitcoin.app/) voluntary for self-check, recap, discovery, and future-learning connection. It supplies no assessment evidence and creates no certification gate. The 12-question check samples selected content from Modules 1–3; it does not establish Module 4 or practical competence. Keep result wording limited to that check. Do not introduce score tracking, thresholds, or educator access. Require independent factual/editorial review, small-phone testing, and screen-reader testing before release.

Keep named programme links and general wallet-software guidance within the approved publication policy. Explain openness alongside custody, recovery, safety, compatibility, privacy, continuity, and local support without global product endorsement. Keep programme participation optional and changing links maintained.

Check teaching slides are editable, aligned, adaptable to learners, language, and local context, and supportive of discussion and practice. Teaching must remain possible without projection. Resolve conditional source/update, donation/support, and verification back matter before release. Verify destinations and processes before commissioning related QR or certificate visuals. Track essential visuals, rights, alt text, source, and review status.

## Prompt 9: Reconcile findings and validate the result

For approved policy changes, update architecture, competencies, assessment, and certification authorities first; then delivery publications and activity specifications; then scope, design, content plan, overview, and horizon; then the index, lexicon, resource register, public communications, and published outputs as applicable. Do not silently choose between contradictory authorities.

For each finding, report the file/section, evidence, relevant principle or criterion, consequence for learners or educators, recommended action, and completion evidence needed. Reuse to-do IDs; distinguish a new action from a resolved decision or historical suggestion. Keep historical approvals and unclear handwriting separate from active tasks.

End with the scope/date, changes, unresolved decisions, release blockers, validation performed, and checks not performed. Do not claim external verification, rendering, accessibility testing, real-cohort validation, or human approval from a document-only review. Re-run only to resolve substantive findings or examine changed material; do not reopen settled policy without new evidence or an authorized policy change.

## Source coverage

This script consolidates the archived community charter, consistency decisions, quality checks, report findings, and action register. It preserves the mission, six principles, network context, membership, benefits, commitments, termination/change rules, signature context, policy questions, reconciliation order, assessment, delivery, publication, and quality requirements. The active source of truth is this script and [review_todo.md](review_todo.md), with historical provenance retained in the archive. All individual annotations and legacy decision alternatives are retained in [review_todo.md](review_todo.md), with provenance and status limits.
