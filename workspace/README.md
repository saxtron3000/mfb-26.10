# Bitcoin Diploma 2026.10 Redesign

This repository contains the active working materials for My First Bitcoin's Bitcoin Diploma 2026.10 redesign. In this project, **2026.10** means the planned October 2026 edition.

The redesign reorganizes rather than replaces the existing Diploma. It preserves the open-source, community-led, Bitcoin-only identity of the program while making the beginner pathway shorter, clearer, more practical, easier to teach, and easier to adapt across communities.

## Current Status

The project is in active planning and drafting. The files in `workspace/` are working documents, not a finished publication.

The current direction is:

- an approximately 8-hour beginner Diploma;
- four blocks of approximately 2 hours each;
- a shared Core followed by an educator-selected Custom block;
- in-person, offline-capable print or PDF delivery first;
- practical learning, discussion, reflection, review, and learner explanation in every block;
- English-first source drafting followed by simplicity, tone, terminology, style, and translation-readiness review;
- a separate Student Book, Activity Bank, Educator Guide, assessment framework, and publication specification;
- Advanced module design after the beginner Diploma is stable and published;
- future online PDF, online cohort, self-paced, web, app, and cross-modal branches that preserve the same Core outcomes;
- My First Bitcoin app assessment, progress tracking, and certification gating so every certificate reflects a shared minimum standard.

The My First Bitcoin app is the shared assessment system: learners complete micro-learning, knowledge checks, practical checklists, and required evidence there. A certificate may be issued only after the app records assessment-complete status. Detailed governance, credential infrastructure, and verification systems remain implementation work.

## Start Here

Use [`00_index.md`](00_index.md) for the recommended reading order and complete source-of-truth map.

For a faster orientation:

1. Read [`15_spec.md`](15_spec.md) for a short, standalone overview of the planned Diploma.
2. Read [`06_plan.md`](06_plan.md) for the active architecture and content boundaries.
3. Read [`05_objectives.md`](05_objectives.md), [`07_contents.md`](07_contents.md), and [`08_draft.md`](08_draft.md) when working on learner-facing content.

## Course Architecture

| Block | Role | Working title | Core question |
|---|---|---|---|
| 1 | Problem | Fiat | What problem does fiat money create? |
| 2 | Solution | Bitcoin | Why was Bitcoin created, and how does it respond? |
| 3 | Action | Self-custody | How do I take responsibility for using and securing Bitcoin? |
| 4 | Custom | Bitcoin as Money | How can Bitcoin function as money in this community? |

Blocks 1–3 form the shared Core every learner completes. Local educators select and adapt Block 4 within the approved Custom boundaries so that practice reflects local tools, risks, opportunities, infrastructure, and community context.

## Repository Structure

| Path | Purpose |
|---|---|
| `workspace/` | Active planning and drafting package; the main working area. |
| `workspace/advanced/` | Source maps for merging beginner-safe Organizations material and preserving Advanced material. |
| `ref/` | Legacy Bitcoin Diploma, Educator Guide, and Bitcoin for Organizations reference material. |
| `public/` | Public-facing briefs, presentation sources, PDFs, images, and stakeholder communication assets. |
| `feedback/` | Review notes and stakeholder feedback used as project inputs. |

Reference and feedback material is input, not automatically approved curriculum. It must be reviewed against the active plan, objectives, design rules, and publication guardrails before being used.

## Workspace Document Map

| File | Owns or describes |
|---|---|
| [`00_index.md`](00_index.md) | Reading order, source-of-truth map, and consistency rules. |
| [`01_review.md`](01_review.md) | Diagnosis of the existing Diploma and the problems the redesign addresses. |
| [`02_research.md`](02_research.md) | Evidence needs, research questions, claim validation, and confidence tracking. |
| [`03_scope.md`](03_scope.md) | Workstreams, milestones, deliverables, completion criteria, and out-of-scope work. |
| [`04_design.md`](04_design.md) | Design principles, non-negotiables, assumptions, adaptation boundaries, and risks. |
| [`05_objectives.md`](05_objectives.md) | Core, Custom, and Advanced learning outcomes and competency boundaries. |
| [`06_plan.md`](06_plan.md) | **Active source of truth** for the four-block architecture, content boundaries, timing rules, and legacy migration. |
| [`07_contents.md`](07_contents.md) | Planned Student Book table of contents. |
| [`08_draft.md`](08_draft.md) | Current Student Book draft and learner-facing scaffold. |
| [`09_assets.md`](09_assets.md) | Visual-text index, asset requirements, placement rules, and review handoff. |
| [`10_activities.md`](10_activities.md) | Activity Bank structure, activity inventory, and activity design rules. |
| [`11_guide.md`](11_guide.md) | Educator Guide structure, pacing, facilitation, adaptation, and learner-safety guidance. |
| [`12_assessment.md`](12_assessment.md) | Required app assessment, evidence of learning, passing requirements, and delivery-mode adaptation. |
| [`13_certification.md`](13_certification.md) | Assessment-required certification rule and outstanding governance questions. |
| [`14_lexicon.md`](14_lexicon.md) | Beginner-safe terminology and definitions for consistent drafting and translation. |
| [`15_spec.md`](15_spec.md) | Standalone 2026.10 overview, publication rules, and collaborator-facing specification. |
| [`16_advanced.md`](16_advanced.md) | Advanced module ideas, follow-on pathways, and legacy material parked outside the beginner Diploma. |
| [`advanced/mergefromorganizations.md`](advanced/mergefromorganizations.md) | Checklist for beginner-safe material selected from Bitcoin for Organizations. |
| [`advanced/advancedorganizations.md`](advanced/advancedorganizations.md) | Source trail for Organizations material routed to Advanced pathways. |

The public stakeholder brief and keynote source is [`../public/MFB-BD-Keynote.md`](../public/MFB-BD-Keynote.md).

## Content Ownership Rules

- Use `06_plan.md` for architecture and boundary decisions; do not create a competing plan elsewhere.
- Keep measurable outcomes and competencies in `05_objectives.md`.
- Keep learner-facing prose in `08_draft.md` and align its order with `07_contents.md`.
- Keep detailed activities in `10_activities.md`, not in the Student Book or plan.
- Keep detailed facilitation guidance in `11_guide.md`, not in the Student Book or plan.
- Keep app assessment, evidence, and passing requirements in `12_assessment.md`; keep certification eligibility and governance questions in `13_certification.md`.
- Keep the full Advanced module list and parked advanced content in `16_advanced.md`.
- Use `advanced/mergefromorganizations.md` as the beginner-safe Organizations checklist; do not import Organizations chapters directly into the Student Book.
- Use `advanced/advancedorganizations.md` and `16_advanced.md` for Organizations material that exceeds beginner scope.

## Design and Publication Guardrails

The redesign should:

- preserve independent, impartial, open-source, community-led, and Bitcoin-only education;
- manage beginner cognitive load and keep every component tied to a learning purpose;
- separate Core, Custom, and Advanced material clearly;
- standardize shared Core theory and outcomes while allowing educator-led local practice within guardrails;
- support offline or low-connectivity delivery and use print QR codes sparingly;
- prepare English source files for translation and localization before publication;
- use beginner-safe, consistent terminology from `14_lexicon.md`;
- avoid financial, legal, tax, accounting, compliance, or investment advice;
- avoid turning named wallets, exchanges, tools, maps, services, or local resources into global recommendations;
- date and cite current-data examples, or replace them with evergreen explanations before publication;
- protect learner safety, autonomy, privacy, and realistic expectations.

## Learning Promise

A realistic graduate of the beginner Diploma should be able to explain what money is, identify the fiat problem Bitcoin responds to, describe Bitcoin's core properties in plain language, understand beginner wallet and custody concepts, identify basic safety practices, compare simple trade-offs, and choose safer next learning steps.

The Diploma should not claim that every graduate can independently manage high-stakes custody, perform advanced technical troubleshooting, or master economic, technical, legal, tax, investment, policy, or organizational analysis.

## Public Message

The Diploma is becoming shorter, clearer, more practical, and more locally adaptable while preserving its mission.
