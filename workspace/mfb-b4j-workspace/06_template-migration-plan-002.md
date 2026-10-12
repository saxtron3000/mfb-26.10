# Bitcoin for Juniors — Migration Plan 002

This plan has one editing prompt for each section in `workspace/06_template-MIGRATE.md`, in the new template's top-to-bottom order. Run one prompt, inspect its reported per-file results and diff, then decide whether to run the next prompt. No prompt may edit a section owned by another prompt.

There are 19 sections in the migration template. Accordingly, **Prompt 18 is Notes and Prompt 19 is Additional Resources**. This keeps the requested one-to-one relationship: no two template sections share a prompt.

## Scope and authority

Edit only Markdown activity files in these folders:

- `publish/en/1-exchange-value-and-price/`
- `publish/en/2-time-energy-and-reward/`
- `publish/en/3-analog-vs-digital/`
- `publish/en/4-safety-security-and-privacy/`
- `publish/en/5-money-matters/`
- `publish/en/6-bitcoin-basics/`

Use the matching relative file in `ref/bitcoin-for-juniors/en/` as the source of the original content. Read these before every editing prompt:

- `workspace/y_06_template-OLD.md`
- `workspace/06_template-NEW.md`
- `workspace/06_template-MIGRATE.md`
- `workspace/06_template-migration-plan-002.md`
- the target activity and matching reference source

## Rules applying to every prompt

- Change only the named section. Do not make cleanup, wording, formatting, curriculum, or structural changes in any other section.
- Preserve all source wording, lists, emphasis, links, timings, examples, and references exactly.
- Treat Markdown headings and standalone bold-only labels as source boundaries; ordinary bold prose and list text are not boundaries.
- Work one file at a time. If a source block cannot be mapped confidently, leave that file unchanged for this prompt and report the problem.
- Before saving, verify that the source content assigned to this prompt appears exactly once in its destination and is not duplicated elsewhere.
- Return a table with file path, changed/skipped status, source blocks moved, destination section, and unresolved mapping. Stop after that report.
- Temporary files will be incomplete until all 19 prompts have run. Do not create content merely to fill an empty section.
- Do not edit outside the six target folders.

## Prompt 1 — `# Activity Title`

```text
Migrate only the activity title for every in-scope activity. Compare the target title with its matching reference source. Ensure the original title appears exactly once as the first line, using the exact level-one heading format `# Activity Title`. Do not alter any body content, heading, blank section, or filename. Report results and stop.
```

## Prompt 2 — `## Keywords`

```text
Create only the empty `## Keywords` section immediately below each activity title. Do not add keywords and do not alter any existing source content or other heading. If the section is already present, verify it is empty and leave it unchanged. Report results and stop.
```

## Prompt 3 — `## Activity Type`

```text
Migrate only the source Activity type block for every in-scope activity. Move its unchanged body to `## Activity Type`, after `## Keywords`, and remove only its original source container. Do not move any other content. Verify the Activity type body appears exactly once in its destination. Report results and stop.
```

## Prompt 4 — `## Participation`

```text
Migrate only the source Grouping block to `## Participation`, after `## Activity Type`, for every in-scope activity. Preserve its body exactly and remove only its original source container. Do not change Description, Duration, or another section. Verify the Grouping body appears exactly once in Participation. Report results and stop.
```

## Prompt 5 — `## Duration`

```text
Migrate only the source Duration block to `## Duration`, after `## Participation`, for every in-scope activity. Preserve its body exactly and remove only its original source container. Do not move Description or any other section. Verify the Duration body appears exactly once in Duration. Report results and stop.
```

## Prompt 6 — `## Description`

```text
Migrate only the source Description block to `## Description`, after `## Duration`, for every in-scope activity. Preserve its body exactly and remove only its original source container. Do not move Objectives, Materials, or any procedure content. Verify the Description body appears exactly once in Description. Report results and stop.
```

## Prompt 7 — `## Objectives`

```text
Migrate only source Learning Outcomes and Objective In Student’s Words content to `## Objectives`, after `## Description`, for every in-scope activity. Preserve source order and bodies exactly. Use the original labels as bold inline lead-ins only when needed to distinguish the two bodies; do not retain them as headings. Remove only the original containers for these two source blocks.

Do not alter Procedure even when Objective In Student’s Words originated there. Verify both mapped bodies appear exactly once in Objectives. Report results and stop.
```

## Prompt 8 — `## Materials`

```text
Migrate only source Materials and Equipment to one `## Materials` section, after `## Objectives`, for every in-scope activity. Keep Materials before Equipment and preserve both bodies exactly. Use **Equipment** as an inline label if needed; do not keep it as a heading. Remove only the original Materials and Equipment containers. Verify every mapped body appears exactly once in Materials. Report results and stop.
```

## Prompt 9 — `## Preparation`

```text
Create only an empty `## Preparation` section after `## Materials` for every in-scope activity. Do not move Setup, Prep, procedure, or any other content into it. If it exists, verify it is empty and leave it unchanged. Report results and stop.
```

## Prompt 10 — `## Procedure`

```text
Migrate only the PROCEDURE container for every in-scope activity. Rename or replace the source PROCEDURE heading with `## Procedure` in its final position after `## Preparation`. Do not move any procedural body, Setup, Step, objective, or other content in this pass. Do not create Step or Setup headings yet. Verify the Procedure container appears exactly once. Report results and stop.
```

## Prompt 11 — `### Setup`

```text
Migrate only operational source Setup content into one `### Setup` immediately below `## Procedure` for every in-scope activity. A source `Setup` block is setup content. A source `Prep` block is moved only when it is operational preparation for running the activity; if it is instructional, leave it for its appropriate Step and report the decision.

Preserve moved Setup/Prep blocks in source order. Remove only source containers made empty by this move. Do not change, create, or renumber Steps and do not alter other procedure content. Verify every moved setup body appears exactly once and `### Setup` appears exactly once. Report results and stop.
```

## Prompt 12 — `### Step 1`

```text
Migrate only the source opening phase into `### Step 1`, after Setup, for every in-scope activity. The opening phase includes source OPENING and PRE-ACTIVITY blocks and their non-objective content. Preserve their source order and content exactly. Begin each retained source block with its source name as an italic inline lead-in; do not retain a source procedure label as a heading.

Objective In Student’s Words belongs to Objectives, not Step 1. Do not move Setup, core activity, follow-up, close, Review, or other sections. If a file has no opening-phase content, leave Step 1 absent and report it; do not create an empty Step. Verify each moved source body appears exactly once. Report results and stop.
```

## Prompt 13 — `### Step 2`

```text
Migrate only the source core activity phase into `### Step 2`, after Step 1 when Step 1 exists, for every in-scope activity. The core activity phase includes source ACTIVITY and its non-Setup content, plus equivalent named main-activity units such as DAY blocks when an ACTIVITY container is absent. Preserve the original order and content exactly.

Each outer activity unit begins with its source name as an italic inline lead-in. Convert nested labels such as Model, Activity, Checkpoint & Debrief, Reflection, Trade, or similar labels to italic inline lead-ins within the same Step; never retain them as headings. Do not move Setup/Prep selected for Setup, opening content, follow-up, close, or any other section. If a core activity cannot be classified confidently, leave the file unchanged for this prompt and report it. Verify all moved bodies appear exactly once. Report results and stop.
```

## Prompt 14 — `### Step 3`

```text
Migrate only the source closing phase into `### Step 3`, after Step 2, for every in-scope activity. The closing phase includes FOLLOW-UP, CLOSE, and equivalent end-of-activity source blocks. Preserve source order and bodies exactly. Begin each retained source block with its source name as an italic inline lead-in; do not retain source procedure labels as headings.

Do not move Review, Notes, resources, or other content. If there is no closing-phase content, leave Step 3 absent and report it; do not create an empty Step. Verify all moved bodies appear exactly once. Report results and stop.
```

## Prompt 15 — `## Review`

```text
Create only the empty `## Review` section after the completed Procedure section for every in-scope activity. Do not move discussion, reflection, debrief, or any other instructional content into it. If Review exists, verify it is empty aside from its child headings that will be created in later prompts. Report results and stop.
```

## Prompt 16 — `### Key Points`

```text
Create only the empty `### Key Points` heading immediately inside `## Review` for every in-scope activity. Do not add content or alter Discussion questions, Procedure, Notes, or any other section. If it exists, verify it is empty and leave it unchanged. Report results and stop.
```

## Prompt 17 — `### Discussion questions`

```text
Create only the empty `### Discussion questions` heading immediately after `### Key Points` inside `## Review` for every in-scope activity. Do not add content or move source discussion/debrief content. If it exists, verify it is empty and leave it unchanged. Report results and stop.
```

## Prompt 18 — `## Notes`

```text
Migrate only Notes content to `## Notes`, after `## Review`, for every in-scope activity. Use only these bold inline labels, never Notes subheadings:

- **Classroom management** for Classroom management
- **Extensions** for Extensions & Sponge Activities
- **Adaptation** for general Differentiation content
- **Younger students** for embedded Younger students content
- **Accessibility** for embedded ELL/Accessibility content
- **Safety** for embedded Safety content

Extract embedded Younger students, ELL/Accessibility, and Safety bodies from Differentiation to their matching labels. Keep the remaining Differentiation body under **Adaptation**. Preserve all bodies exactly. Remove only source Notes containers made empty by this move. Verify each mapped body appears exactly once under its proper label. Report results and stop.
```

## Prompt 19 — `## Additional Resources`

```text
Migrate only APPENDIX, Appendix A, Appendix B, Appendix C, and REFERENCES content to `## Additional Resources`, after `## Notes`, for every in-scope activity. Preserve every body and the source order exactly. Preserve Appendix and References labels as subheadings or bold inline labels only when needed to retain the source hierarchy. Remove only source resource containers made empty by the move.

Verify every mapped appendix and reference body appears exactly once in Additional Resources. Do not alter any other section. Report results and stop.
```

## Final read-only audit

After all 19 prompts are individually approved, run a read-only audit. Compare each target with its matching reference source and verify the final order is: title; Keywords; Activity Type; Participation; Duration; Description; Objectives; Materials; Preparation; Procedure; Setup; Step 1; Step 2; Step 3; Review; Key Points; Discussion questions; Notes; Additional Resources. Confirm that all mapped source content appears exactly once, empty destination-only sections are empty, Notes labels are exact, and no in-scope file has unresolved content. Report defects only; do not edit files.
