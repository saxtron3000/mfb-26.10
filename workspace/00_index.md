# Bitcoin Diploma 2026.10 Workspace Index

## Purpose

This index explains how the working documents in `workspace/` guide the creation of the Bitcoin Diploma 2026.10 curriculum.

The repository now separates three kinds of material:

| Area | Purpose |
|---|---|
| [`workspace/`](./) | Working documents that guide content creation, including architecture, objectives, design rules, activities, assessment, terminology, and publication planning. |
| [`publish/`](../publish/) | Curriculum source documents intended for publication in Sanity and release as the new curriculum. |
| [`review/`](../review/) | Documents used to review quality, consistency, annotations, and release readiness across the project. |

These areas have different authority. Working documents define and explain curriculum decisions. Publication documents apply those decisions for learners, educators, and the app. Review documents identify issues and actions but do not replace the relevant working source of truth.

For a repository-wide introduction, see the [root README](../README.md).

---

## Published Curriculum Sources

The current publication sources are:

| Publication | File | Purpose |
|---|---|---|
| Student Guide | [`mfb-bd-sg-26.10.md`](../publish/mfb-bd-sg-26.10.md) | Learner-facing Diploma curriculum. |
| Educator Companion Guide | [`mfb-bd-eg-26.10.md`](../publish/mfb-bd-eg-26.10.md) | Educator-facing preparation, facilitation, adaptation, safety, and assessment guidance. |
| Educator Quick Start Guide | [`mfb-bd-qs-26.10.md`](../publish/mfb-bd/mfb-bd-qs-26.10.md) | Concise first-teaching route and links to essential Diploma materials. |
| Optional self-assessment | [`mfb-bd-ml-26.10.md`](../publish/mfb-bd-ml-26.10.md) | Microlearning question data for the optional app self-assessment. |

These files should contain publication-ready content. Planning notes, unresolved questions, review commentary, and historical material should remain outside `publish/`.

---

## Recommended Reading Order

Read the working documents in this order when you need the full design context:

| Step | File | Use |
|---|---|---|
| 1 | [`01_review.md`](01_review.md) | Understand the earlier Diploma and the problems the redesign responds to. |
| 2 | [`02_research.md`](02_research.md) | Review the evidence base, research limits, and claims requiring validation. |
| 3 | [`03_scope.md`](03_scope.md) | Review workstreams, milestones, deliverables, and completion criteria. |
| 4 | [`04_design.md`](04_design.md) | Understand design principles, non-negotiables, assumptions, adaptation boundaries, and risks. |
| 5 | [`05_objectives.md`](05_objectives.md) | Review learner outcomes, competency boundaries, and stable objective IDs. |
| 6 | [`06_plan.md`](06_plan.md) | Read the active source of truth for the four-module architecture and content boundaries. |
| 7 | [`07_contents.md`](07_contents.md) | Review the planned learner-content structure. |
| 8 | [`09_assets.md`](09_assets.md) | Review visual and asset requirements. |
| 9 | [`10_activities.md`](10_activities.md) | Review activity design and assessment-task requirements. Published activities will be hosted in the Resources Hub. |
| 10 | [`11_resources.md`](11_resources.md) | Review external sources and their curriculum claim locations. |
| 11 | [`12_educator-plan.md`](12_educator-plan.md) | Review the planning structure for the Educator Companion Guide. |
| 12 | [`13_assessment.md`](13_assessment.md) | Review theoretical and practical assessment requirements. |
| 13 | [`14_microlearning-plan.md`](14_microlearning-plan.md) | Review the internal plan for optional app microlearning. |
| 14 | [`15_certification.md`](15_certification.md) | Review the assessment prerequisite for certification and outstanding governance questions. |
| 15 | [`16_lexicon.md`](16_lexicon.md) | Check beginner terminology and translation consistency. |
| 16 | [`17_spec.md`](17_spec.md) | Read the standalone Diploma overview for collaborators and stakeholders. |
| 17 | [`99_horizon.md`](99_horizon.md) | Review post-release candidates, programme boundaries, and future decision gates. |

Advanced pathway ideas and parked legacy material are maintained separately in [`advanced/18_advanced.md`](../advanced/18_advanced.md).

---

## Source-of-Truth Map

| Topic | Source of truth |
|---|---|
| Earlier-Diploma diagnosis | [`01_review.md`](01_review.md) |
| Research and evidence validation | [`02_research.md`](02_research.md) |
| Project scope and milestones | [`03_scope.md`](03_scope.md) |
| Design principles and constraints | [`04_design.md`](04_design.md) |
| Objectives and competencies | [`05_objectives.md`](05_objectives.md) |
| Four-module architecture, content boundaries, and legacy migration | [`06_plan.md`](06_plan.md) |
| Learner-content structure | [`07_contents.md`](07_contents.md) |
| Student Guide publication source | [`publish/mfb-bd-sg-26.10.md`](../publish/mfb-bd-sg-26.10.md) |
| Visual and asset needs | [`09_assets.md`](09_assets.md) |
| Activity design | [`10_activities.md`](10_activities.md) |
| External sources and claim references | [`11_resources.md`](11_resources.md) |
| Educator Guide planning structure | [`12_educator-plan.md`](12_educator-plan.md) |
| Educator Companion Guide publication source | [`publish/mfb-bd-eg-26.10.md`](../publish/mfb-bd-eg-26.10.md) |
| Educator Quick Start Guide publication source | [`publish/mfb-bd/mfb-bd-qs-26.10.md`](../publish/mfb-bd/mfb-bd-qs-26.10.md) |
| Objective-aligned assessment and evidence | [`13_assessment.md`](13_assessment.md) |
| Optional app microlearning plan | [`14_microlearning-plan.md`](14_microlearning-plan.md) |
| Optional app self-assessment publication source | [`publish/mfb-bd-ml-26.10.md`](../publish/mfb-bd-ml-26.10.md) |
| Certification prerequisite and governance questions | [`15_certification.md`](15_certification.md) |
| Beginner terminology and definitions | [`16_lexicon.md`](16_lexicon.md) |
| Collaborator and stakeholder overview | [`17_spec.md`](17_spec.md) |
| Advanced pathways and parked legacy content | [`advanced/18_advanced.md`](../advanced/18_advanced.md) |
| Post-release horizon register | [`99_horizon.md`](99_horizon.md) |
| Active release actions | [`review/00_todo.md`](../review/00_todo.md) |
| Cross-project consistency decisions | [`review/00_consistency.md`](../review/00_consistency.md) |
| Ongoing quality controls | [`review/00_quality.md`](../review/00_quality.md) |

When two documents disagree, resolve the decision in the owning working document before updating dependent publication files.

---

## Current Working Direction

The redesign uses four modules:

1. Understanding Money
2. How Bitcoin Works
3. Using Bitcoin Safely
4. Bitcoin in Your Community

The working assumptions are:

- an approximately eight-hour beginner pathway that includes teaching, practice, assessment, feedback, and recording;
- educator-facilitated delivery in person or online;
- a complete low-tech, offline-capable print/PDF route;
- no app or connectivity requirement for learning, assessment, completion, or certification;
- shared Core learning with educator-selected, locally relevant Module 4 practice;
- practical learning in every module;
- separate learner, educator, activity, assessment, and optional microlearning components;
- English-first drafting followed by simplicity, tone, terminology, and translation-readiness review;
- two required, non-compensatory assessment components: educator-evaluated theory and educator-observed practical competency;
- optional app self-assessment that never supplies certification evidence;
- Advanced design after the beginner Diploma is stable and published; and
- Bitcoin-only, open-source, community-led education without financial, legal, tax, accounting, compliance, or investment advice.

`06_plan.md` remains the active authority for architecture and content boundaries.

---

## Review Documents

Cross-project review materials are maintained in [`review/`](../review/):

| File | Use |
|---|---|
| [`00_todo.md`](../review/00_todo.md) | Current release actions and blockers. |
| [`00_consistency.md`](../review/00_consistency.md) | A/B decisions needed to reconcile the project. |
| [`00_quality.md`](../review/00_quality.md) | Repeatable quality-control checks. |
| [`00_report.md`](../review/00_report.md) | Consolidated review findings and recommendations. |
| [`00_annotation_backlog.md`](../review/00_annotation_backlog.md) | Archived imported annotations that are not active unless triaged into the to-do list. |

Review findings should be converted into an approved decision or an action in `review/00_todo.md` before they change curriculum policy.

---

## Content Ownership Rules

- Use `06_plan.md` for architecture and content-boundary decisions.
- Keep measurable outcomes and competency requirements in `05_objectives.md`.
- Keep learner-facing publication content in `publish/mfb-bd-sg-26.10.md` and align it with `07_contents.md`.
- Keep detailed activities and assessment-task specifications in `10_activities.md`, not in the Student Guide or curriculum plan.
- Keep educator-facing publication content in `publish/mfb-bd-eg-26.10.md`; use `12_educator-plan.md` to plan and check its structure.
- Keep assessment rules in `13_assessment.md` and certification eligibility and governance questions in `15_certification.md`.
- Keep optional app planning in `14_microlearning-plan.md` and publication data in `publish/mfb-bd-ml-26.10.md`.
- Keep the complete Advanced inventory and Organizations source trail in `advanced/18_advanced.md`.
- Keep cross-project findings, decisions, quality checks, and release actions in `review/`.
- Draft in English first, then review simplicity, tone, terminology, accessibility, and translation readiness before publication.
- Keep printed QR codes sparse and tied to stable, high-value destinations.
- Date and cite current-data examples or replace them with evergreen explanations before publication.
- Do not turn named wallets, exchanges, tools, maps, services, or local resources into global recommendations.
