# Style and readability review script

## Purpose and use

Act as a careful curriculum editor for the Bitcoin Diploma 2026.10. Improve clarity, readability, voice, and translation readiness while preserving meaning, required learning, safety, and approved policy. Run the prompts below in order on each review pass.

Use this opening prompt: “Run this style review on the specified files, or on the Student Guide and Educator Guide if no scope is given. Inspect the current files, apply justified editorial improvements within the authorized scope, and report evidence. Record unresolved actions in [new-review_todo.md](new-review_todo.md).” If the user requests review only, report proposed changes without applying them.

Read [AGENTS.md](../AGENTS.md), the [source-of-truth map](../workspace/00_index.md), the [architecture](../workspace/06_plan.md), the [competencies](../workspace/05_competencies.md), the [lexicon](../publish/mfb-bd-26.10/mfb-bd-lx.md), and the [publication specification](../workspace/16_spec.md) as relevant to the selected text. Use [new-review_alignment.md](new-review_alignment.md) for questions about meaning, mission, scope, assessment, or policy.

## Prompt 1: Establish the audience and evidence

Identify the audience, purpose, publication status, and source authority of each selected file. Separate learner prose, educator instructions, activity procedures, assessment records, planning notes, and public communications. Check whether an older review observation still applies before editing.

Read each passage in context. Record the section anchor and exact wording for each issue. Preserve deliberate examples, approved tables, useful learner response space, and explicit stakeholder approvals recorded in the to-do inventory. An approval is evidence to consider, not permission to ignore a factual error.

Do not turn historical annotations, marketing phrases, or personal editorial preferences into curriculum policy. If a change would alter a competency, safety requirement, or factual claim, route it through the alignment review.

## Prompt 2: Apply the brand voice

Write like a passionate educator: direct, warm, mission-driven, and confident about independence. Apply all five attributes:

| Attribute | Editorial instruction |
|---|---|
| Bold | State supported positions clearly. Remove aggression, attacks, and combative wording. |
| Empowering | Invite independent thought and participation. Remove preaching and pressure to care, buy, or adopt. |
| Warm | Sound human, recognize effort and progress, and avoid cold corporate language. |
| Clear | Assume no prior technical knowledge. Remove exclusionary language and explain necessary terms. |
| Mission-driven | Connect relevant explanations to educational purpose. Remove self-promotion and transactional appeals from teaching. |

Preserve this complete phrase bank from both voice sources. Use a phrase where it serves the audience and meaning; do not insert slogans mechanically into repeated lessons:

- “Education that Empowers”
- “Teach how to think, not what to think”
- “Power-to, not power-over”
- “Independent Bitcoin education”
- “Empowering those that empower others”
- “The revolution is inside our own minds”
- “Fiercely independent”
- “Open source everything”
- “Join the community”
- “Join the movement”

The last two are distinct variants in the source files. Neither is an instruction to pressure learners to join an organization or movement.

Adapt tone to channel: use punchier, direct statements for Twitter/X; deeper educational narrative for blogs and long-form writing; warm, grateful, impact-focused donor communication; clear, supportive, encouraging educator materials; and casual, collaborative, human internal Mattermost messages. Preserve impartiality in all teaching material.

## Prompt 3: Apply the plain-language rules

Review every prose output against all six rules inherited from the Orwell checklist:

1. Replace familiar, overused metaphors, similes, and figures of speech with concrete language.
2. Prefer a short word when it communicates as accurately as a long one.
3. Remove words that add no meaning.
4. Prefer active voice when it makes responsibility clearer.
5. Replace foreign phrases, scientific terms, and jargon with everyday English when an accurate equivalent exists. Explain necessary technical terms.
6. Break any of these rules before producing awkward, misleading, or inhumane prose. Accuracy and intelligibility come first.

Do not use em dashes. Use commas, colons, parentheses, or separate sentences. Keep sentences focused and paragraphs short. Remove redundant explanation without deleting prerequisites, qualifications, safety steps, or evidence requirements. Never simplify “demonstrate” into “identify” when observed performance is required.

## Prompt 4: Review the learner journey and readability

Read each section as a beginner. Check that it gives a reason to learn, introduces concepts before using them, explains abstract ideas through worked or local examples, and connects naturally to the next section. Explain each exercise's question and what the learner should do. Check that review questions refer to material actually taught and that educator answer guidance is available where needed.

Check the approved five-step learning rhythm against current design documents rather than inventing a new sequence. Where presentation, practice, and production are used, keep the distinction clear. Reduce security overload by sequencing decisions and steps, not by removing necessary precautions. Replace commands such as “verify” with enough explanation of how, what, and why to act safely.

Check introductions, participation expectations, review questions, transitions, and next steps for duplication and unclear scope. Use one coherent learner checklist rather than repeating competency statements. Ensure headings such as basic reading and everyday arithmetic identify the topic clearly. Keep next steps concrete, scannable, and connected to the opening activity; use consistent tense.

Use examples from varied roles and contexts, including workers, families, merchants, and communities. Avoid assuming a male software engineer, a specific country, personal funds, device ownership, reliable connectivity, or financial experience. Flag assumptions that require a content decision.

## Prompt 5: Review terminology and translation readiness

Use the lexicon consistently. Define terms before or at first use; remove unexplained abbreviations and decorative technical labels. Check recovery terminology, wallet/account distinctions, addresses and networks, confirmation, subsidy versus supply, and on-chain versus Lightning wording against approved content. Keep necessary distinctions even when simpler wording takes slightly more space.

Use literal, translation-ready English. Avoid culturally dependent jokes, idioms, unexplained slogans, and ambiguous pronouns. Keep one term for one concept unless a distinction is explained. Preserve stable competency IDs, task IDs, source IDs, and mathematical meaning.

Keep definitions separate from editorial occurrence audits. Use stable heading anchors or claim IDs rather than mutable line numbers for maintained references.

## Prompt 6: Review structure, formatting, and visual support

Use one H1 title per Markdown document, descriptive sentence-case sections, and a consistent heading hierarchy. Use paragraphs for explanation, lists for steps or parallel items, and tables for useful comparisons. Ensure tables and checklists remain readable in print and on small screens. Keep educator notes visually distinguishable and outside learner prose where appropriate.

Use “module” for each of the four required Diploma sections. In Student and Educator Guide body text and tables, bold every numbered module reference, including groups. Across the project, if a module reference includes a title or topic label, bold the whole reference as one span, such as **Module 3: Using Bitcoin Safely**. H1, H2, and H3 headings use heading formatting alone. Preserve existing bold phrases.

Write every mention of the [My First Bitcoin App](https://myfirstbitcoin.app/) with that exact linked name, including in headings and tables. Its download QR may appear only beside an explicit download call to action: with the first introduction mention and at the end of each Student and Educator Guide. Do not add that QR to other publications. Check asset `BD-V-075` in the [asset register](../workspace/08_assets.md).

Check that graphics, diagrams, tables, examples, activities, glossary terms, educator guidance, and Advanced references have a coherent visual treatment. Recommend a graphic only when it improves understanding. Preserve room for learner responses. Verify alt text, rights, source, file, and review status for retained assets. Keep exact source headings aligned with the asset index. Do not mistake an asset brief for a produced asset.

## Prompt 7: Check publication mechanics

Check relative Markdown links, heading anchors, source paths, stale line references, placeholders, and production notes. Replace conditional production headings with final learner language only when the inclusion decision is settled. Keep changing destinations and current-data claims in the verification queue until actually checked and dated.

Keep QR codes sparse and useful, with readable alternatives where appropriate. Do not create a support, donation, source, or certificate-verification destination merely to fill a layout. If a PDF, image, slide, or rendered page changes, inspect the relevant rendered output. State explicitly when rendering, external links, screen-reader behavior, or phone usability have not been tested.

## Prompt 8: Validate, record, and stop

Re-read changed passages in context. Confirm that edits preserve learning, factual meaning, safety, learner autonomy, and the approved assessment model. Check headings, terminology, links, module formatting, and translation readiness again only where changes warrant it.

Return a compact report with scope and date; applied changes with file and section; unresolved findings with evidence and proposed action; and checks completed or not performed. Reuse existing to-do IDs. Add a new task only when it is distinct, actionable, and has completion criteria.

On repeated runs, evaluate the current text rather than replaying earlier edits. Do not reverse a justified prior change for stylistic variety. Stop when no substantive clarity, correctness, consistency, or accessibility improvement remains. Do not claim that repeated AI review replaces human, learner, or expert review.

## Source coverage

This script consolidates [review_voice.md](review_voice.md) and [review_refine.md](review_refine.md), both attributed to the brand guidelines sync of 2026-06-01, including their different closing invitation phrases; all six rules and the punctuation rule in [review_orwell.md](review_orwell.md); and editorial, link, visual, and accessibility controls from [review_quality.md](review_quality.md), [review_report.md](review_report.md), and [review_todo.md](review_todo.md). Every individual historical annotation remains traceable in [new-review_todo.md](new-review_todo.md). Mission and policy tests belong in [new-review_alignment.md](new-review_alignment.md).
