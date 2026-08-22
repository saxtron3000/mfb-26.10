# Repository Guidelines

## Project Structure & Module Organization

This is a Markdown-first curriculum redesign repository for My First Bitcoin's Bitcoin Diploma 2026.10 edition.

- `workspace/` contains the active planning, competencies, design, content, assets, resources, educator, assessment, microlearning, certification, specification, advanced, and horizon documents.
- `workspace/00_index.md` defines the recommended reading order and source-of-truth map. `workspace/06_plan.md` owns architecture and content boundaries.
- `ref/` contains legacy Diploma, Educator Guide, and Bitcoin for Organizations material for reference only.
- `feedback/` contains stakeholder review notes and research inputs.
- `public/` contains public briefs, presentation sources, PDFs, and images.

Keep learner-facing prose in `publish/mfb-bd-26.10/mfb-bd-sg-26.10.md`, detailed activities in the external Activity Bank project, facilitation guidance in `publish/mfb-bd-26.10/mfb-bd-eg-26.10.md`, and educator assessment records in `publish/mfb-bd-26.10/mfb-bd-assessment-grid-26.10.md`. Use `workspace/13_assessment.md` as planning support. Do not treat reference or feedback files as approved curriculum without review.

## Build, Test, and Development Commands

No automated build, test, lint, or package scripts are currently configured. Common local checks are:

```sh
rg --files -g '*.md'                 # list Markdown source files
rg -n 'TODO|TBD|FIXME' workspace/    # find unfinished work
git diff --check                     # detect whitespace errors
```

For content changes, review the relevant source-of-truth documents, inspect links and headings, and render or open affected PDFs/images when visual assets are involved.

## Coding Style & Naming Conventions

Use Markdown with one `#` title, descriptive `##` sections, short paragraphs, and sentence-case headings. Use repository-relative links and lowercase, numbered filenames for ordered curriculum modules (for example, `workspace/07_contents.md`). Preserve the current terminology: use “module” for each of the four required Diploma sections and describe Module 4 as educator-selected and locally relevant. Draft in English first and keep wording simple and translation-ready.

## Testing Guidelines

There is no test framework or coverage requirement. Validate edits manually for factual consistency, working relative links, consistent terminology with `publish/mfb-bd-26.10/mfb-bd-lx.md`, alignment with `workspace/05_competencies.md`, and compliance with publication guardrails in `workspace/16_spec.md`. Current-data claims should be dated and cited.

## Commit & Pull Request Guidelines

Keep commits focused and use imperative, descriptive subjects such as `Update self-custody competencies`. Pull requests should explain the affected curriculum area, identify source-of-truth files changed, summarize learner or educator impact, and note validation performed. Include screenshots or rendered previews for visual or PDF changes, and flag unresolved research or governance questions.

## Safety & Content Boundaries

Keep the project educational, Bitcoin-only, open-source, and community-led. Do not present financial, legal, tax, accounting, compliance, or investment advice. Avoid turning named wallets, exchanges, tools, or local services into global recommendations.
