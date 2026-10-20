# Prompt: Create One Complete Student-Facing MFB Slide Deck in Markdown

Create **one compact, complete English-language, student-facing slide deck** for My First Bitcoin (MFB), covering Modules 1–4 of the **Bitcoin Diploma Student Guide, edition 26.10 (MFB-105)**. Return **one Markdown file containing all four modules in order**. Summarize the main points and preserve the guide's recognizable structure, important headings and titles, reflections, and cautions. Design the slides as light visual cues for an educator-led session: the educator supplies the explanation, examples, and connections aloud. The deck must not function as a standalone lesson, reading script, or replacement for an educator. There is **no fixed duration, session count, or slide-count limit**, but favor concise coverage and avoid unnecessary slides. The educator is expected to adapt the slides, examples, activities, pacing, and delivery to suit their audience while preserving the curriculum's meaning, required competencies, and safety boundaries.

This prompt contains the authoring rules, formatting examples, and publishing reference in one place. Benoit has access to the full repository, and his AI tool can read repository files and inspect SVGs. Resolve all paths below relative to the repository root; do not depend on the original author's machine-specific paths.

## Task and Deliverable

- Use `publish/mfb-bd-26.10/mfb-bd-sg-26.10.md` as the curriculum source. Read Modules 1–4 before drafting, together with the introductory learner expectations and safety boundaries relevant to those modules.
- The Educator Guide, `publish/mfb-bd-26.10/mfb-bd-eg-26.10.md`, may be consulted to clarify learning objectives, safety boundaries, and practical requirements. It is a supporting reference, not content to reproduce on student-facing slides. Keep educator instructions, rubrics, answer keys, and assessment administration out of visible slide content.
- Turn all four modules into clearly marked sections of one complete deck, preserving their topic sequence, meaning, and learning objectives.
- Cover the main points concisely, following the Student Guide's topic structure. Preserve important concepts, headings and titles, reflections, cautions, and safety qualifications. Summarize supporting prose rather than reproducing every paragraph. Split material only when needed for readability or to preserve an important distinction.
- Use relevant SVG visuals from the required local libraries below across the four module sections where they support the guide's concepts. Choose layouts and visuals to fit the source content; do not add content or slides merely to fill a layout, create visual variety, or make sections equal in length.
- Use English only. Other languages are produced by the translation pipeline, as they are for the books.
- Deliver Markdown suitable for the MFB slide import pipeline. HTML, a standalone PDF, or a PPTX does not satisfy this requirement: the Markdown source is needed for translation and synchronization.
- Use short, clear bullet points, key terms, and visual cues for student-facing summaries. Reserve full sentences for essential definitions, warnings, cautions, or source questions and activity instructions whose clarity requires them. Put all educator-only guidance in hidden speaker notes.
- If the Student Guide cannot be accessed, request its content before generating the deck. The example below demonstrates formatting; it is not the complete curriculum.
- Export only `assets/slides/export/mfb-bd-slides-26.10_(TIMESTAMP).md`, ready to hand over to Benoit. Replace the entire `(TIMESTAMP)` placeholder with the generation-time timestamp in `YYYYMMDD-HHmmss-SSS` format (24-hour time, including milliseconds), for example `assets/slides/export/mfb-bd-slides-26.10_20261019-143025-123.md`. Create the `assets/slides/export/` directory if needed. Generate a fresh timestamp for every run; never overwrite a previous run's output. If the filename already exists, generate a new timestamp before exporting. Do not produce a series of prompt files, a separate handoff report, a coverage report, an asset manifest, or a review report.
- Begin the file with the deck's YAML front matter, without explanatory prose or outer code fences. Import commands and publishing instructions below are reference information for Benoit and must not be copied into the deck.
- Clearly flagged placeholders for unavailable visuals are allowed in this export. Record the remaining visual work in hidden production comments on the affected slides. Benoit handles the remaining visual production, including hosting and micrographic placement where needed; do not make that work a prerequisite for handing over the Markdown file.
- No separate review process, approval stage, rendered-slide review, or dry-import gate is required as part of this authoring task.

## Four Module Sections and Required Output File

Create `assets/slides/export/mfb-bd-slides-26.10_(TIMESTAMP).md` containing these four sections in order, using the module titles from the Student Guide:

1. **Module 1: Understanding Money**.
2. **Module 2: How Bitcoin Works**.
3. **Module 3: Using Bitcoin Safely**.
4. **Module 4: Bitcoin in Your Community**.

Begin each module section with a divider using its exact module title. Follow the guide's sequence and retain its important section headings as recognizable slide titles or visible subheadings, applying the required Title Case to slide titles. Cover the module's main points, relevant source activities or discussion prompts, review, key takeaways, reflection, and cautions in compact form. Include introductory or closing material only where supported by the guide and useful to understand its structure; do not require extra recaps, transitions, an overall introduction, or a final synthesis beyond the source. Do not duplicate the generated opening cover.

Provide a compact, adaptable teaching resource. The educator determines how to select, expand, or divide the material for their audience; do not assume each module must fit into one session. Preserve Module 4's locally adaptable approach and relevant learner-facing prompts from the guide, which educators can use with their chosen local scenario. Do not invent local services or community details. Put any necessary educator adaptation guidance in hidden notes.

## Compact Coverage and Source Fidelity

- Treat completeness as coverage of the guide's main points and structure, not exhaustive transcription or expansion into a new course.
- Preserve important headings and titles, source reflections, warnings, cautions, and qualifications. Keep cautions visible beside the concept or activity they qualify; do not move student safety information exclusively into hidden notes.
- Shorten wording without changing meaning or removing conditions, risks, trade-offs, or distinctions needed for an accurate understanding.
- Combine closely related points when they fit clearly on one slide while retaining recognizable source headings and topic order. Add another slide only when the content needs it.
- Use the guide's own examples, questions, activities, and takeaways selectively. Do not invent additional exercises, discussion questions, motivational statements, quotations, or repeated summaries to satisfy a slide pattern.
- Let the content determine the layout and number of slides. A short slide or uneven module lengths are acceptable. Do not add material to fill space or to use every supported layout.

## Educator-Led Delivery and Light Slide Text

- The educator leads the session. Visible slide text should cue the topic and highlight what matters while leaving explanation, demonstration, discussion, and connections to the educator.
- Prefer a small number of short bullet phrases per slide. Use key terms, brief contrasts, and compact process steps instead of explanatory paragraphs or a narration that can be read aloud as the lesson.
- Putting prose into a bullet list does not make it concise. Avoid paragraph-length bullets, chains of full sentences, and a series of slides that collectively transcribe the guide.
- Use a full sentence only when its wording is essential, such as a precise definition, a warning or caution, or a concise source reflection question or necessary activity instruction. Keep these exceptions brief and preserve their meaning.
- Keep essential learner warnings and safety conditions explicit on screen even when they require full sentences. Brevity must not make a caution ambiguous or remove an important qualification.
- Cover each important topic through a clear heading and its essential cues; do not try to put the educator's entire explanation on screen. Completeness means the guide's main points are represented, not that learners can teach themselves the course from the deck.
- Any necessary educator-only explanation or facilitation cue belongs in hidden notes. Do not compensate for light slides by requiring a full teaching script or adding new curriculum content.

## Student-Facing Content Only

Everything visible on a slide must be written for students. Slides should help learners understand, discuss, reflect, and participate in the session.

- Include brief learner-facing summary cues and relevant examples, questions, activity steps, and takeaways drawn from the Student Guide. Leave extended explanations to the educator.
- Do not display educator-only instructions, teaching strategies, facilitation cues, timing plans, assessment rubrics, answer keys, internal production notes, or directions such as "Ask the students…" or "Explain to the class…".
- Put any necessary educator-only information exclusively in `<!-- notes: ... -->` comments. Never turn these comments into visible slide text.
- Distinguish learner activity instructions from educator facilitation instructions. For example, show "Discuss an example of barter with a partner" on the slide; put "Invite pairs to share, adapting the discussion to the group's needs" in speaker notes.
- Keep technical production directions, including micrographic placement instructions, in hidden comments rather than visible student content.

## Deck Title and Generated Cover

The pipeline always generates the opening cover from the deck title. **Do not add a separate opening cover as an imported content slide.**

For this task, provide the deck title in YAML front matter at the very top of the file:

```markdown
---
title: "Bitcoin Diploma"
---
```

The opening front matter is metadata; after it, begin the first actual slide. Elsewhere, a line containing only `---` starts a new slide.

The importer also supports two alternative ways to supply the title:

- Start the file with `<!-- layout: cover -->` and `# Bitcoin Diploma`. This leading title block names the deck and is not imported as a slide.
- Supply `--title "Bitcoin Diploma"` on the import command.

Use one clear title mechanism. The `cover` layout is supported for a title slide inside a deck, but it must not duplicate the automatically generated opening cover.

Use the exact module numbers and titles on the four module dividers. Do not restart the front matter or create another opening cover at a module boundary.

## Slide Structure and Text

- Separate slides with `---` on its own line.
- Use a `#` or `##` heading as the first visible text on each titled slide. Layout comments may precede it. That heading becomes the slide title.
- Write titles in **Title Case** and body text in **sentence case**.
- Keep small title words lowercase unless they are the first or last word: `of`, `the`, `and`, `to`, `in`, `on`, `for`, `a`, `an`, `at`, `by`, `with`, and `or`.
- Example: `## Why Money Exists`, not `## Why money exists`.
- Never write titles in all capitals. The theme prints the case exactly as written.
- The body supports plain Markdown: paragraphs, bullet lists, numbered lists, **bold**, *italic*, links, and images. For this deck, default to short bullet phrases; paragraph support is not a reason to include extended prose.
- Fonts and colors come from the design system. Do not specify custom fonts or colors. Translated decks receive the matching fonts automatically, including Arabic, Hindi, Japanese, and other non-Latin scripts.

## Layouts

Place a layout comment anywhere within its slide. Use only these supported values:

- **Content:** no comment, or `<!-- layout: content -->`. Use for an ordinary slide with a title and points.
- **Section divider:** `<!-- layout: divider -->`. Use at the start of a module.
- **Two columns:** `<!-- layout: two-columns -->`. Use for a long list of short items.
- **Full-bleed image:** `<!-- layout: full-bleed -->`. Use for a picture filling the slide, with the title over it.
- **Quote:** `<!-- layout: quote -->`. Use for one large statement.
- **Cover:** `<!-- layout: cover -->`. Supported for the title mechanisms described above or a title slide inside the deck.

An unsupported layout stops the import and identifies the affected slide. Do not invent layout names or alter their spelling.

## Speaker Notes

Write presenter-only guidance in a `notes:` comment:

```markdown
<!-- notes: Ask the group for an example of barter before showing the list. -->
```

Notes do not appear on the slide. Use them for educator-only adaptation and facilitation instructions, assessment guidance, or presentation cues. Do not impose fixed activity or session durations. Questions and activity steps that students need to see belong in the visible slide body; instructions about how the educator should facilitate them belong only in notes.

## Required SVG Libraries and Asset Selection

Use **SVG files only** for all rendered image assets in this deck. Select existing artwork from these two folders, relative to the repository root:

- `assets/reference/svg-character/` — SVG character and scene assets, including `bd-v-###-character.svg` files.
- `assets/illustrations/svg/` — SVG illustrations, including `bd-illustration-###.svg` files.

Before choosing visuals, consult all three asset references:

1. **Primary usage and placement authority:** `workspace/mfb-bd-workspace/08_assets.md`. Use its visual index, Student Guide section anchors, educational purposes, descriptions, and placement guidance to match assets to slide topics.
2. `assets/asset-description.md`. Read the purpose and description for each candidate asset to understand what it is intended to communicate.
3. `assets/assets-list.md`. Check the asset's status, availability, and any recorded limitations. A file marked `Created` is not automatically approved for publication.

Match the asset's described concept to the corresponding Student Guide section and then to the slide teaching that concept. Use headings and nearby text as the reliable anchors, rather than relying on line numbers. Confirm the actual SVG exists and inspect it before using it; a filename alone does not establish that its contents fit the intended lesson.

If a relevant visual is unavailable, reserve its position with the required `VISUAL` block and a separate hidden production comment identifying what is missing and the work Benoit must complete. Use an existing visual ID and brief where available. Do not invent a visual ID, SVG path, or hosted URL, and do not add an image line for a file that is unavailable. Such a placeholder is an allowed part of the Markdown export, not a rendered image.

The `BD-V-###` visual IDs and `bd-illustration-###` scene filenames are independent numbering systems. Do not assume matching numbers identify the same topic. Where needed, consult `assets/illustrations/docs/illustrations.md` and the illustration metadata to resolve a scene's topic, then select its actual `.svg` file from the required folder rather than a PNG referenced by older documentation.

Choose visuals intentionally across each module: everyday scenes for concrete examples, relevant characters for learner situations, and suitable illustrations to support explanations or transitions. Keep a clear relationship between each visual and the lesson. Balance images with concise text, allow breathing room, and preserve the artwork's aspect ratio. Avoid unrelated decoration and repetitive use of the same scene.

Exclude canceled assets, including `BD-V-014`, and do not use educator-only content as visible student material. Do not substitute PNG, JPG, WebP, screenshots, or other raster files. General guide instructions for external JPG assets do not override this slide task's SVG-only requirement.

## Required Standalone VISUAL Blocks

**Every visual used or reserved in the Markdown deck must have its own standalone `VISUAL` comment block**, matching the Student Guide format below. This applies to SVG illustrations, character scenes, diagrams, and micrographic placeholders, including visuals that already have a rendered image line.

```markdown
<!-- VISUAL: BD-V-002
TYPE: Diagram
ALT: A repeatable critical-thinking loop for checking claims, evidence, alternatives, trade-offs, and uncertainty.
ASSET: assets/briefs/bd-v-002-brief.md
-->
```

- Place the block on its own, with a blank line before and after it, at the intended visual position within the relevant slide. Keep it inside that slide's `---` boundaries; do not collect all visual references at the end of the deck.
- Use the field names and capitalization exactly as shown: `VISUAL`, `TYPE`, `ALT`, and `ASSET`, with one field per line. Do not replace this format with `SVG asset:`, an informal placeholder, or a reference buried in speaker notes.
- Use the visual's existing ID, type, alt text, and brief reference from the Student Guide and asset index where applicable. Adapt alt text only when the selected artwork or slide context requires it, preserving its meaning.
- `ASSET` identifies the repository-relative brief path when one exists. A Markdown brief reference is metadata, not an image file; the artwork used must still be SVG.
- For an illustration without a `BD-V` ID or brief, use its existing illustration identifier in `VISUAL`, `Illustration` in `TYPE`, a meaningful description in `ALT`, and its exact SVG path in `ASSET`. Do not invent a `BD-V` number or assume the two numbering systems match.
- Include one block per visual occurrence, even when reusing the same asset on another slide. A slide with multiple visuals needs a separate block for each.
- The block is a hidden production reference, not a visible student-facing heading or a rendered image. Keep educator and production details out of visible slide text.

When an `ASSET` field points to a brief, also record the actual selected SVG path, purpose, placement, and hosted URL or pending hosting status in a separate hidden production comment immediately after the `VISUAL` block. If no suitable SVG is available, state that the SVG source is unavailable rather than inventing a path. For example, the additional record for `BD-V-018` may read:

```markdown
<!-- SVG source: assets/reference/svg-character/bd-v-018-character.svg
Purpose: Illustrate declining purchasing power with two baskets of goods.
Placement: Right-hand visual beside the explanation of purchasing power.
Import URL: Pending publication of this SVG at a direct HTTPS image URL.
Remaining work for Benoit: Host the SVG and add its image line before import.
-->
```

This additional record supplements the required `VISUAL` block; it does not replace it.

For a visual that has a brief but no available artwork, the production record may instead read:

```markdown
<!-- Production status: PLACEHOLDER — visual not yet available.
SVG source: Unavailable.
Purpose: Explain the concept described in the preceding VISUAL block and its brief.
Placement: Below the slide title, alongside the learner explanation.
Remaining work for Benoit: Produce the visual from the brief; use a micrographic for essential editable labels, or host an eligible SVG and add its image line.
-->
```

## SVG Image Placement and Import URLs

- Use `![bg](https://...)` for the slide's designated picture.
- On a `full-bleed` slide, this picture fills the slide. On any other layout, it occupies the right 40%.
- The selected source must be an SVG from one of the two required local libraries. For import, use a **direct HTTPS link to that SVG file**. Do not use Google Drive or Canva share links, or local file paths as image URLs in import-ready Markdown.
- If a selected local SVG has no published URL, retain its exact path and intended placement in the hidden asset comment and mark its import URL as pending. Benoit will upload or otherwise expose that SVG at a direct HTTPS URL and add the image line before import. This pending work does not block the Markdown export. Do not invent a hosted URL or describe a placeholder as an already embedded visual.
- Each image must be no larger than **20 MB**.
- Slides are **16:9**. For full-bleed SVGs, check the SVG dimensions/viewBox and composition for a clear rendering at **1920 × 1080 or larger**. Do not convert them to raster files to meet this requirement.
- The import stores its own copy of the image, so the source link only needs to work on import day.
- A normal image line, such as `![Description](https://...)`, places the image in the slide body instead of using the designated picture placement.
- Use supplied or verified image URLs. Do not fabricate image links.

The original source example used an 800 × 1043 WebP. It is not an eligible visual for this task; use a suitable SVG from the required libraries instead.

## Student-Facing Hyperlinks

Links may lead to My First Bitcoin resources or to relevant external resources beyond the Diploma. Select destinations by consulting the repository's `links/` folder:

- `links/links-internal.md` — My First Bitcoin resources, purpose, source locations, and review notes.
- `links/links-internal.csv` — internal destination lookup by ID, URL, and description.
- `links/links-external.md` — external resources and activity-library references, with source context and review status.

Use links where they help students explore a concept, access a relevant activity or resource, or continue learning. Match the destination to the module and learner audience. Keep educator-only resources in hidden notes when they are needed for delivery.

Use descriptive Markdown link text, such as `[Resources Hub](https://programs.myfirstbitcoin.org/resources/)`. Preserve the indexed URL's exact destination, language, anchors, query parameters, and filters. Consult the recorded review status; `Pending` or `Unable to verify` is not confirmation that a link works. If web access is available, selected destinations may be verified. Record any unresolved link status in a hidden comment on the affected slide without inventing replacement URLs. Do not require a separate link-review process or report. This task does not include editing the link registers or scheduling link maintenance.

A hyperlink to a video is allowed as a link, but video embeds remain unsupported. Permission to link to external learning resources does not permit sourcing images outside the two specified SVG libraries.

## Translatable Visuals and Unsupported Content

- Do not use Markdown tables. The importer drops them with a warning.
- Do not embed videos. A YouTube URL remains a link; it does not become an embedded player.
- For visuals containing text, including diagrams and charts, use a **micrographic**, not a raster image containing the text. Micrographics can be translated; text baked into images cannot.
- SVG format alone does not make labels translatable by the slide pipeline. If a selected SVG contains essential text, use its artwork as the visual reference and provide a micrographic placeholder with editable, translatable labels for Studio placement. Do not treat a static SVG diagram or table as a replacement for a translatable micrographic.
- Use the required standalone `VISUAL` block on the slide where a micrographic belongs. Add a separate hidden micrographic instruction comment describing its editable labels and the relationship it should show.
- A visual made in Claude Design is imported into the Studio as a micrographic and placed on the slide there. The placeholder is a handoff instruction for that placement, not an automatically rendered visual.

Example micrographic reference and placement instruction:

```markdown
<!-- VISUAL: BD-V-002
TYPE: Diagram
ALT: A repeatable critical-thinking loop for checking claims, evidence, alternatives, trade-offs, and uncertainty.
ASSET: assets/briefs/bd-v-002-brief.md
-->

<!-- Micrographic placement: Below the title. Use editable labels for the six-step critical-thinking loop described in the brief, including the return path for revising a conclusion. -->
```

## Formatting Example

The following example combines the supplied sample slides with the preferred title metadata. It demonstrates structure and layouts, not complete module coverage or the full combined deck. Its sample wording does not authorize adding material absent from the Student Guide or using a layout merely because it appears here. Use the actual module titles specified above. The full-bleed slide is omitted here because a compliant image URL must be supplied before it can be used.

```markdown
---
title: Bitcoin Diploma
---

<!-- layout: divider -->
# Module 1: Understanding Money

<!-- notes: Begin with an opening question and adapt the discussion to the group's experience. -->

---

## Why Does Money Exist?

- To trade without barter
- To store value over time
- To compare the value of different things

<!-- notes: Ask the group for an example of barter before showing the list. -->

---

<!-- layout: two-columns -->
## Properties of Good Money

- Durable
- Portable
- Divisible
- Uniform
- Scarce
- Accepted

---

<!-- layout: quote -->
## "Money Is a Tool for Cooperation Between Strangers."

---

## Checking Claims and Evidence

<!-- VISUAL: BD-V-002
TYPE: Diagram
ALT: A repeatable critical-thinking loop for checking claims, evidence, alternatives, trade-offs, and uncertainty.
ASSET: assets/briefs/bd-v-002-brief.md
-->

<!-- Micrographic placement: Below the title. Use editable labels for the six-step critical-thinking loop described in the brief, including the return path for revising a conclusion. -->
```

For a full-bleed SVG slide, add `<!-- layout: full-bleed -->`, a `![bg](...)` line containing the real direct HTTPS URL of the selected SVG, and a suitable heading. Only use this layout when the artwork remains clear behind the title and suits the 16:9 frame.

## Output Requirements

The sole deliverable is **one compact Markdown file, `assets/slides/export/mfb-bd-slides-26.10_(TIMESTAMP).md`**, containing all four Student Guide modules in order, with the correct module titles, clear dividers, recognizable important headings, and concise coverage of the main points, source reviews and reflections, and cautions. Preserve necessary safety qualifications and important distinctions while avoiding unnecessary slides, repetition, or invented content. There is no fixed duration or slide-count target. Support educator adaptation for different audiences while keeping all visible content student-facing. Any necessary educator-only guidance belongs exclusively in hidden notes.

Keep the slides light enough to support educator-led explanation rather than screen reading. Use short summary bullets and visual cues, with full sentences reserved for essential wording as specified above. The exported deck must remain a presentation aid that depends on an educator to deliver the lesson, not a standalone replacement for teaching.

Use one deck title, no duplicate opening cover, correct slide separators, supported layout comments, Title Case headings, sentence case body text, and valid notes comments. Do not include tables or video embeds. Rendered images must meet the image-link and dimension requirements; visuals containing essential text need descriptive micrographic placeholders for Studio placement.

Use purposeful visuals across all four module sections. Every rendered image must be an existing SVG from one of the two required folders, selected using the index and descriptions. **Every visual occurrence, including a placeholder, needs a standalone `<!-- VISUAL: ... -->` block with `TYPE`, `ALT`, and `ASSET` fields at its intended position on the slide.** Keep source paths, placement, and pending visual production or hosting work in adjacent hidden production comments for Benoit. Select student-facing hyperlinks using the `links/` references and preserve their exact destinations. Do not present unresolved placeholders as finished imported visuals. Deliver the Markdown file without a separate report or review workflow.

## Import and Publishing Reference for Benoit

These instructions are reference information for Benoit, who handles remaining visual production and publishing preparation. They are not slide content or a separate deliverable and do not authorize importing or publishing as part of deck authoring. The commands assume the repository root is the working directory. In each command, replace `(TIMESTAMP)` with the timestamp in the generated Markdown filename.

An optional technical dry import lists slide layouts without writing:

```sh
pnpm mfb import-slides -f "assets/slides/export/mfb-bd-slides-26.10_(TIMESTAMP).md" -p bitcoin-diploma -l en --edition 26.10 --dry
```

This is an optional publishing aid, not a required review stage or a condition of Markdown delivery.

To create the deck in Sanity:

```sh
pnpm mfb import-slides -f "assets/slides/export/mfb-bd-slides-26.10_(TIMESTAMP).md" -p bitcoin-diploma -l en --edition 26.10
```

Importing an edited file again requires `--replace`. This replaces **all** of the deck's slides with the slides in the file. Any slide edits made in the Studio since the previous import are lost.

The importer refuses to add slides to a Canva deck: a deck with a Canva link or an exported PDF and no slides. Otherwise, `mfb slides` would render a new PDF over the Canva export. Import into a new edition instead.

A new deck has no **Display order**, so it does not appear on the website yet. Benoit can place the micrographics in the Studio under **Presentation** and set its Display order when completing the publishing work.

`mfb slides` renders the deck with the lowest Display order for a language. The 26.10 deck is rendered to PDF once it takes over from the 26.04 deck.

## Source References

- Markdown specification: <https://github.com/MyFirstBitcoin/mfb-publishing/blob/main/docs/slides-markdown.md>
- Original example: <https://github.com/MyFirstBitcoin/mfb-publishing/blob/main/docs/examples/slides-example.md>
- Title capitalization and brand rules: <https://github.com/MyFirstBitcoin/mfb-design/blob/master/brand-spec.md>
