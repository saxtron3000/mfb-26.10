# Repository Guidelines

## Project Structure & Module Organization

This is a Markdown-first curriculum redesign repository for My First Bitcoin's Bitcoin Diploma 2026.10 edition.

- `workspace/` contains the active planning, competencies, design, content, assets, resources, educator, assessment, microlearning, certification, specification, advanced, and horizon documents.
- `workspace/00_index.md` defines the recommended reading order and source-of-truth map. `workspace/06_plan.md` owns architecture and content boundaries.
- `ref/` contains legacy Diploma, Educator Guide, and Bitcoin for Organizations material for reference only.
- `feedback/` contains stakeholder review notes and research inputs.
- `public/` contains public briefs, presentation sources, PDFs, and images.

Keep learner-facing prose in `publish/mfb-bd-26.10/mfb-bd-sg-26.10.md`, detailed activities on the [Resources Hub](https://programs.myfirstbitcoin.org/resources/), facilitation guidance in the [Educator Guide](publish/mfb-bd-26.10/mfb-bd-eg-26.10.md), and educator assessment records in `publish/mfb-bd-26.10/mfb-bd-assessment-grid-26.10.md`. Use `workspace/13_assessment.md` as planning support. Do not treat reference or feedback files as approved curriculum without review.

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

Always refer to the My First Bitcoin application as “My First Bitcoin App” and hyperlink every mention to `https://myfirstbitcoin.app/`, including mentions in headings and tables. Use `[My First Bitcoin App](https://myfirstbitcoin.app/)`. The app-link and QR asset is tracked in `workspace/08_assets.md` (`BD-V-075`). Generic references to wallet apps or other applications keep their ordinary wording.

Use the My First Bitcoin App QR code only beside an explicit download call to action in the Student Guide and Educator Guide: once with the first app mention in each introduction and once at the end of each guide. Other mentions remain text hyperlinks; do not add app QR codes to other publications.

In both the Student Guide and Educator Guide, bold every numbered module reference in body text and tables, including grouped references: `**Module 1**`, `**Modules 1 and 2**`, and `**Modules 1–3**`. Preserve existing bold formatting when a reference is already inside a bold phrase. Module references in H1, H2, or H3 headings use heading formatting alone, without added bold.

Across the project, when a module reference in body text or a table includes its title or a descriptive topic label, bold the entire reference as one span, for example `**Module 3: Using Bitcoin Safely**` or `**Module 3: wallets, keys, recovery, custody**`. Do not end the bold span after the module number. H1, H2, and H3 headings are exempt from this bold rule. Keep exact heading references in the asset index aligned with the source headings.

## Testing Guidelines

There is no test framework or coverage requirement. Validate edits manually for factual consistency, working relative links, consistent terminology with `publish/mfb-lx-26.10.md`, alignment with `workspace/05_competencies.md`, and compliance with publication guardrails in `workspace/16_spec.md`. Current-data claims should be dated and cited.

## Commit & Pull Request Guidelines

Keep commits focused and use imperative, descriptive subjects such as `Update self-custody competencies`. Pull requests should explain the affected curriculum area, identify source-of-truth files changed, summarize learner or educator impact, and note validation performed. Include screenshots or rendered previews for visual or PDF changes, and flag unresolved research or governance questions.

## Safety & Content Boundaries

Keep the project educational, Bitcoin-only, open-source, and community-led. Do not present financial, legal, tax, accounting, compliance, or investment advice. Avoid turning named wallets, exchanges, tools, or local services into global recommendations.
