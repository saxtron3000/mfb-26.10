# My First Bitcoin curriculum — 2026.10

This Markdown-first repository contains My First Bitcoin's Bitcoin Diploma, Bitcoin for Juniors, and shared learning resources for the 2026.10 edition. It also holds visual production materials, terminology references, link inventories, and public communication sources.

This README maps the repository for human contributors and agents. Use the owning file for detailed content and keep related guides, records, and assets aligned. A file's presence in `publish/` does not by itself mean it is approved for release: restricted-pilot content has separate boundaries.

## Start here

| Task | Starting point |
|---|---|
| Understand contribution rules | [Workflow for humans and agents](#workflow-for-humans-and-agents) and [writing conventions](#writing-conventions) |
| Read or edit the beginner Diploma | [Student Guide](publish/mfb-bd-26.10/mfb-bd-sg-26.10.md) |
| Prepare to teach | [Educator Quick Start](publish/mfb-bd-26.10/mfb-bd-qs-26.10.md), then the [Educator Guide](publish/mfb-bd-26.10/mfb-bd-eg-26.10.md) |
| Check assessment requirements | [Educator Guide: operational assessment protocol](publish/mfb-bd-26.10/mfb-bd-eg-26.10.md#operational-assessment-protocol) and [Assessment Grid](publish/mfb-bd-26.10/mfb-bd-assessment-grid-26.10.md) |
| Work on Bitcoin for Juniors | [English program overview](publish/mfb-b4j-26.10/en/README.md) and [Parent Guide](publish/mfb-b4j-26.10/parents-guide.md) |
| Edit an activity | [Activity sources](publish/mfb-act-26.10/) and [activity template](reference/ref-mfb-act-000-template.md) |
| Check vocabulary | [Lexicon terms register](publish/mfb-lx-26.10/mfb-lx-26.10-terms.md) |
| Work on visuals | [Asset production log](assets/assets-list.md), [asset notes](assets/asset-description.md), and [style rules](assets/style/STYLE.md) |
| Review destinations and references | [Internal links](links/links-internal.md) and [external links](links/links-external.md) |

## Folder structure

```text
README.md                       Repository map and contribution workflow
publish/                        Curriculum and supporting publication sources
├── mfb-bd-26.10/               Bitcoin Diploma guides and assessment record
├── mfb-b4j-26.10/              Bitcoin for Juniors and parent guidance
│   └── en/                    English front matter, six topic folders, and resources
├── mfb-act-26.10/              Shared activity library
├── mfb-lx-26.10/               Shared Bitcoin terminology register
└── mfb-ml-26.10/               Restricted-pilot self-check data and CSV exports
assets/                         Visual production inputs and status records
├── briefs/                    Individual asset design briefs
├── reference/                 JSON records and SVG/PNG visual references
├── prompts/                   Instructions for asset production stages
└── style/                     Style rules and visual references
    ├── bible/                 Character reference images
    └── layouts/               Layout references and usage guidance
reference/                      Activity template and lexicon reference indexes
links/                          Link inventories and review records
public/                         Public brief and presentation sources
```

Folder names and capitalization matter. Use the paths shown here when navigating; check the actual destination before reusing a path from an older document.

## Curriculum sources and ownership

### Bitcoin Diploma

The four required modules form one beginner pathway. **Module 4: Bitcoin in Your Community** is educator-selected and locally relevant. Keep learner explanations, facilitation instructions, activity procedures, and assessment records in their respective files.

| File in `publish/mfb-bd-26.10/` | Owns | How it relates to the other files |
|---|---|---|
| [mfb-bd-sg-26.10.md](publish/mfb-bd-26.10/mfb-bd-sg-26.10.md) | Learner-facing curriculum | Supplies the learning sequence and explanations that teaching, activities, and visuals support |
| [mfb-bd-eg-26.10.md](publish/mfb-bd-26.10/mfb-bd-eg-26.10.md) | Preparation, facilitation, adaptation, safety, and operational assessment protocol | Defines approved assessment interactions, tasks, rubrics, and evidence routes |
| [mfb-bd-qs-26.10.md](publish/mfb-bd-26.10/mfb-bd-qs-26.10.md) | A concise first teaching route | Summarizes preparation and delivery; must stay consistent with the full Educator Guide |
| [mfb-bd-assessment-grid-26.10.md](publish/mfb-bd-26.10/mfb-bd-assessment-grid-26.10.md) | Educator competency and cohort progress record | Records results against the Educator Guide's assessment requirements |

The package supports offline and low-tech delivery. Required theory and practical evidence are educator-evaluated. Publication of the teaching framework does not establish that every local route is ready for certificated delivery; the assessing educator is responsible for assessing learners and issuing certificates.

### Bitcoin for Juniors

[`publish/mfb-b4j-26.10/`](publish/mfb-b4j-26.10/) contains the Parent Guide and English curriculum. Within [`en/`](publish/mfb-b4j-26.10/en/):

- `0-front-matter/` contains the foreword, FAQ, and introduction
- `1-exchange-value-and-price/` through `6-bitcoin-basics/` contain the six topic sequences
- Each topic folder begins with `1-overview.md`, followed by numbered lesson and activity files
- `resources/` contains discussion prompts, participation formats, vocabulary, comparisons, and technical support materials

Use the English overview to follow the sequence. Edit the relevant lesson file for lesson content, the Parent Guide for family guidance, and the resource files for reusable support. Keep detailed material in one owning file and cross-reference it where needed.

### Shared activities and terminology

[`publish/mfb-act-26.10/`](publish/mfb-act-26.10/) holds detailed activity procedures, materials, discussion prompts, and facilitator notes. Filenames follow `mfb-act-NNN-description.md`; preserve the activity ID when revising content. Use the [activity template](reference/ref-mfb-act-000-template.md) to check structure. Delivery resources are available through the [Resources Hub](https://programs.myfirstbitcoin.org/resources/).

An activity's inclusion in the library does not automatically make it a required lesson or an approved assessment task. Check the Educator Guide before using an activity as formal evidence.

[`publish/mfb-lx-26.10/mfb-lx-26.10-terms.md`](publish/mfb-lx-26.10/mfb-lx-26.10-terms.md) holds shared terms, definitions, stable IDs, slugs, and destination URLs. The related indexes in [`reference/`](reference/) support guide- and activity-specific terminology checks:

- [Student Guide lexicon index](reference/ref-mfb-lx-26.10-sg-index.md)
- [Educator Guide lexicon index](reference/ref-mfb-lx-26.10-eg-index.md)
- [Activity lexicon index](reference/ref-mfb-lx-26.10-act-index.md)

When changing a definition or destination, check its uses in the curriculum and corresponding indexes. Reference material and stakeholder feedback support review; do not treat them as approved curriculum or assessment changes without review.

### Restricted-pilot materials

[`publish/mfb-ml-26.10/`](publish/mfb-ml-26.10/) contains restricted-pilot self-check question data in Markdown and separate short- and long-question CSV exports. Keep the exports semantically aligned with the corresponding Markdown tables. This material is available only to a defined My First Bitcoin App pilot group. It must not be required, assigned, or linked through normal Diploma delivery, mentioned in the Student or Educator Guide, or used as assessment or certification evidence. Do not add an app download call to action or create or place an app QR asset in current-release materials. Learner-facing app links, destinations, download calls to action, and QR assets require public-release approval and destination testing. Generic references to wallet apps or other applications keep their ordinary wording.

## Visual assets

Visuals support specific guide content. Preserve each `BD-V-NNN` identifier across its notes, brief, reference files, and production records.

Use the asset type `EXTERNAL` for approved, externally supplied JPGs added directly through Sanity, including `BD-V-001` and `BD-V-076`. Generated production work is not applicable: no brief, AI reference, JSON record, or Claude package is required.

| Location | Use |
|---|---|
| [assets/assets-list.md](assets/assets-list.md) | Check recorded production status, missing inputs, and unresolved production decisions |
| [assets/asset-description.md](assets/asset-description.md) | Read asset-specific purpose and visual direction |
| [assets/briefs/](assets/briefs/) | Maintain design briefs named `bd-v-NNN-brief.md` |
| [assets/reference/](assets/reference/) | Maintain matching `bd-v-NNN-ref.json`, SVG, and PNG reference files where available |
| [assets/prompts/](assets/prompts/) | Follow the brief, JSON, SVG/PNG, and editable production handoff instructions |
| [assets/style/STYLE.md](assets/style/STYLE.md) | Check shared visual rules |
| [assets/style/CHARACTERS.md](assets/style/CHARACTERS.md) | Check the recurring cast—Sara, Luis, Ernesto, Amina, Lukas, and Mei—alongside the images in `assets/style/bible/` |
| [assets/style/layouts/README.md](assets/style/layouts/README.md) | Choose and apply layout references |

Read the adjacent guide text before changing a visual. Keep heading references, placement, captions, and alt text aligned with that text. A created reference image is not a finished publication asset. Resolve documented production conditions and verify the production log before claiming an asset is ready.

## Links and public communication

[`links/links-internal.md`](links/links-internal.md) records My First Bitcoin destinations and their use across the guides; [`links/links-internal.csv`](links/links-internal.csv) provides a tabular companion. [`links/links-external.md`](links/links-external.md) covers other web destinations and local document links. Update affected inventories when changing a curriculum link, and preserve the distinction between a recorded review result and current destination verification.

[`public/mfb-bd-elevator.md`](public/mfb-bd-elevator.md) contains the short public explanation of the Diploma redesign. [`public/mfb-bd-keynote.md`](public/mfb-bd-keynote.md) contains presentation source material. Keep both aligned with the curriculum's scope and release status; public messaging does not define new teaching or assessment requirements.

## Workflow for humans and agents

1. Read this README’s contribution guidance, then use the repository map to identify the file that owns the requested change.
2. Read that file and its relevant dependencies before editing. Resolve outdated paths against the current folder structure; do not assume an old link identifies an existing file.
3. Make the change in its owning source. Keep detailed learner prose, educator guidance, activities, definitions, and records in their designated locations.
4. Check affected companion files. For example, an assessment change may affect the Educator Guide, Assessment Grid, and Quick Start; a heading change may affect asset placement and links.
5. Preserve stable activity, competency, term, and asset IDs. Update related references when a file is added, renamed, or removed, and update this README when the repository structure changes.
6. Validate the change and report the files changed, the learner or educator impact, checks performed, and any unresolved decisions.

### Writing conventions

- Draft in English first, using simple, translation-ready wording and short paragraphs.
- Use one `#` title, descriptive `##` sections, and sentence-case headings.
- Use repository-relative links and lowercase, numbered filenames for ordered curriculum content.
- In bulleted lists, omit terminal punctuation for individual words or phrases; use periods for complete sentences. End each numbered step with a period.
- Use “module” for each of the four required Diploma sections. Keep **Module 4** educator-selected and locally relevant.
- In the Student Guide and Educator Guide, bold every numbered module reference in body text and tables, including grouped references: `**Module 1**`, `**Modules 1 and 2**`, and `**Modules 1–3**`. Preserve existing bold formatting when the reference is already part of a bold phrase.
- Across the project, bold the entire module reference when it includes a title or descriptive topic label: `**Module 3: Using Bitcoin Safely**` or `**Module 3: wallets, keys, recovery, custody**`. Do not end the bold span after the number.
- Module references in H1, H2, and H3 headings use heading formatting alone, without added bold. Keep exact heading references in asset records aligned with the source headings.

### Content boundaries

Keep the project educational, Bitcoin-only, open-source, and community-led. Do not introduce financial, legal, tax, accounting, compliance, or investment advice, or turn named tools and services into global recommendations. Date and cite current-data claims.

## Validation

There is no configured automated build, test, lint, or package pipeline, and no test framework or coverage requirement. Useful local checks are:

```sh
rg --files -g '*.md'
rg -n 'TODO|TBD|FIXME' publish/ assets/ reference/ links/ public/
git diff --check
```

Review relative links and heading anchors manually. Check terminology, competency and assessment consistency, offline access, safety boundaries, and release status. Open or render affected images and PDFs when changing visual materials. Check terms against the shared lexicon and the Student Guide and Educator Guide lexicon indexes linked above.

## Commits and pull requests

Keep commits focused and use imperative, descriptive subjects such as `Update self-custody competencies`. Pull requests should identify the affected curriculum area and owning source files changed, explain learner or educator impact, and summarize validation. Include screenshots or rendered previews for visual or PDF changes, and flag unresolved research or governance questions.
