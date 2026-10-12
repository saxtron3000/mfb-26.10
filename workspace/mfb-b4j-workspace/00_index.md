# Project Index

## File Contract

**Role:** This file is the workspace map and routing guide.

**Purpose:** Help contributors and tooling understand what each project file is for, where new information belongs, and how to avoid duplicating content across files.

**Structure:** Keep this file organized as project context, workspace file contracts, related folders, and maintenance rules.

**Use this file for:** Finding the right file to read or edit, adding or removing workspace files, and resolving unclear ownership between files.

**Do not use this file for:** Detailed feedback, task tracking, curriculum drafting, or program specification prose.

## Project Context

- This project is a refresh of the *Bitcoin for Juniors* program launched in April 2026.
- The review should look for needed modifications, errors, and opportunities to make the program better.
- The working target is the October 2026 version.

## Workspace File Contracts

### `00_index.md` - Project Index

- **Role:** Map and routing guide for the workspace.
- **Purpose:** Explain what each workspace file owns so contributors and tooling know where to put information.
- **Structure:** Project context, file contracts, related folders, and maintenance rules.
- **Use for:** Orientation, file ownership decisions, and updates when files are added, renamed, moved, or removed.
- **Do not use for:** Raw feedback, task lists, draft lesson text, or full program specifications.

### `01_review.md` - Review Notes

- **Role:** Evidence log for feedback, observations, reflections, and review comments.
- **Purpose:** Preserve why changes may be needed, with enough context to trace insights back to sources.
- **Structure:** Source-based feedback sections, reflections, comments, and task seeds that can be converted into `03_tasks.md`.
- **Use for:** Capturing field feedback, reviewer observations, patterns, concerns, and rationale.
- **Do not use for:** Authoritative task status, final decisions, polished curriculum text, or broad program specs.

### `02_scope.md` - Review Scope

- **Role:** Boundary document for the October 2026 review pass.
- **Purpose:** Define what is in scope, what is out of scope, and which program-level questions need attention.
- **Structure:** Goal, core review areas, lesson and activity edits, program design questions, supporting materials, follow-up, and out-of-scope items.
- **Use for:** Deciding whether proposed work belongs in this review cycle and keeping the project from expanding without intention.
- **Do not use for:** Detailed task tracking, feedback logs, draft lesson prose, or the final program description.

### `03_tasks.md` - Task Register

- **Role:** Authoritative operational task list.
- **Purpose:** Convert review findings and scope items into trackable work, decisions, and follow-up actions.
- **Structure:** Imported tasks, open tasks, decisions needed, pending follow-up, and completed items when useful.
- **Use for:** Tracking what needs to be done, what has been decided, what is waiting, and where each task came from.
- **Do not use for:** Long feedback excerpts, curriculum drafts, or stable program overview prose.

### `04_draft.md` - Working Curriculum Draft

- **Role:** Drafting space for revised curriculum-facing content.
- **Purpose:** Hold proposed front matter, guide text, and lesson revisions before they are copied into final curriculum files.
- **Structure:** Program-facing front matter followed by lesson drafts in curriculum order.
- **Use for:** Writing and revising teacher-facing and student-facing content.
- **Do not use for:** Project management, feedback archiving, scope boundaries, or high-level specification.

### `05_spec.md` - Program Specification

- **Role:** Stable program brief and design reference.
- **Purpose:** Describe what *Bitcoin for Juniors* is, who it serves, how it is structured, and what principles guide it.
- **Structure:** Program overview, learning outcomes, curriculum structure, lesson format, pedagogy, delivery models, logistics, disclaimers, resources, and changelog.
- **Use for:** Orienting contributors, summarizing the intended program, and checking whether drafts match the program design.
- **Do not use for:** Full lesson drafts, raw review notes, open task tracking, or source-specific feedback.

### `06_template.md` - Activity Template

- **Role:** Definitive activity-format template for Bitcoin for Juniors.
- **Purpose:** Keep every activity consistent with the My First Bitcoin activity library.
- **Use for:** Checking or creating activity structure before editing curriculum content.
- **Do not use for:** Activity-specific lesson content, project management, or program specifications.

### `06_template-migration-plan.md` - Activity Migration Plan

- **Role:** Reusable prompt plan for migrating Bitcoin for Juniors activities to the new activity structure.
- **Purpose:** Preserve lesson content while moving it to the mapped headings in the new template.
- **Use for:** Planning, executing, and validating the activity migration across the six `publish/en/` chapter folders.
- **Do not use for:** Making curriculum changes beyond the structural migration or resolving ambiguous mappings without a decision.

## Related Folders

- `../README.md` - Basic overview of the review workspace and starting points.
- `../feedback/` - External feedback and review notes from collaborators.
- `../ref/bitcoin-for-juniors/en/` - Reference copy of the current English curriculum.

## Maintenance Rules For Contributors And Tooling

- Read this file before making broad edits in `workspace/`.
- Put raw observations in `01_review.md`, not directly into `03_tasks.md`, unless they are already clear tasks.
- Put only actionable checklist items, decisions, and follow-up status in `03_tasks.md`.
- Put actual rewritten curriculum content in `04_draft.md`.
- Put stable program-level descriptions and design constraints in `05_spec.md`.
- Use `06_template.md` as the required structure for every Bitcoin for Juniors activity.
- Use `02_scope.md` to decide whether proposed work belongs in the October 2026 refresh.
- Update this index whenever a workspace file is added, renamed, moved, or removed.
- When information could belong in more than one file, keep the detailed version in the owning file and add only a short cross-reference elsewhere.

## Quick File List

- `../README.md` - Basic overview of the review workspace and starting points.
- `00_index.md` - Workspace map, file contracts, and routing rules.
- `01_review.md` - Gathers all feedback, reflections, and comments about the previous version of *Bitcoin for Juniors*.
- `02_scope.md` - Defines the review and edit scope for the October 2026 version.
- `03_tasks.md` - Tracks review tasks, decisions, and follow-up items.
- `04_draft.md` - Working draft for revised curriculum-facing content.
- `05_spec.md` - Spec sheet that gives an outline of the educational program for people who need to understand what it is about.
- `06_template.md` - Definitive structure for Bitcoin for Juniors activities.
- `06_template-migration-plan.md` - Prompt sequence for migrating activities to the new structure.
