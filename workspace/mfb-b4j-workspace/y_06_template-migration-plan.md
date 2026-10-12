# Bitcoin for Juniors — Codex Migration Runbook

Run these prompts in order. They migrate the 21 activity files in the six `publish/en/` chapter folders from the old structure to the new one without changing lesson content.

## Authoritative files

- Old template: `workspace/06_template-OLD.md`
- New template: `workspace/06_template-NEW.md`
- Original migration map: `workspace/06_template-MIGRATE.md`
- This confirmed runbook: `workspace/06_template-migration-plan.md`

This runbook resolves the migration-map ambiguities. If it conflicts with the original migration map, follow this runbook.

## Confirmed rules to include in every migration prompt

- `Group` in the original migration map means the old `Grouping` heading. Move its content to `## Description`.
- Move `Learning Outcomes` and `Objective In Student’s Words` to `## Objectives`.
- Merge `Materials` and `Equipment` into `## Materials`.
- Move `APPENDIX`, `Appendix A`, `Appendix B`, `Appendix C`, and `REFERENCES` to `## Additional Resources`.
- Create `## Keywords`, `## Participation`, `## Preparation`, `## Review`, `### Key Points`, and `### Discussion questions` empty. Do not invent content for them.
- Every activity has exactly one `### Setup`, inside `## Procedure` and immediately before `### Step 1`. It contains all source Setup material, which is pre-class work. Preserve the order of the setup material itself.
- Every other source procedure section becomes its own consecutive `### Step N`. The series is open-ended: create only the steps whose source sections exist; never create blank steps, gaps, or Model/Checkpoint/Reflection/etc. sections that were absent from the source.
- Within every Step, make the source section name an italic inline lead-in, followed by its unchanged content. Example: `*Pre-activity* Original content...` Do not retain former procedure section names as Markdown headings.
- Keep instructional order from the source activity after moving all Setup material to the mandatory Setup section. Do not rewrite, summarize, expand, or omit instructions, timings, examples, teacher language, lists, links, or references.
- In `## Notes`, use bold inline labels, never subheadings. The label alone is bold:

  ```md
  **Classroom management** Students must be told to respect the time limits...
  ```

  Use these exact labels: `**Classroom management**`, `**Extensions**`, `**Adaption**`, `**Younger students**`, `**Accessibility**`, and `**Safety**`.

  Map `Extensions & Sponge Activities` to `**Extensions**`; map `Differentiation` to `**Adaption**`; map `ELL/Accessibility` to `**Accessibility**`. If Younger students, ELL/Accessibility, or Safety appears within a Differentiation block, move that specific content to its corresponding Notes label and leave remaining differentiation content under `**Adaption**`.

- Do not alter files outside the six `publish/en/` activity folders.

---

## Prompt 1 — Preflight inventory (read-only)

Run this first. Do not edit files during this prompt.

```text
Read in full:

- workspace/06_template-OLD.md
- workspace/06_template-NEW.md
- workspace/06_template-MIGRATE.md
- workspace/06_template-migration-plan.md

Inventory every Markdown activity in these folders:

- publish/en/1-exchange-value-and-price/
- publish/en/2-time-energy-and-reward/
- publish/en/3-analog-vs-digital/
- publish/en/4-safety-security-and-privacy/
- publish/en/5-money-matters/
- publish/en/6-bitcoin-basics/

For each file, identify all source sections that will become Setup, Steps, Notes labels, and Additional Resources. Treat both Markdown headings and standalone bold-only source labels as section boundaries. Do not treat ordinary bold emphasis inside prose or lists as a section boundary.

Report:

1. the complete activity-file count;
2. each file’s source procedure sections in source order;
3. every source Setup block;
4. every Notes label and any embedded Younger students, ELL/Accessibility, or Safety content; and
5. any source content that cannot be placed using the confirmed rules.

Do not edit anything. Stop and report any unmapped content rather than deciding silently.
```

---

## Prompt 2 — Migrate all activities

Run this only after the preflight report contains no unresolved mappings, or after the user resolves each reported mapping.

```text
Migrate all Markdown activity files in these folders:

- publish/en/1-exchange-value-and-price/
- publish/en/2-time-energy-and-reward/
- publish/en/3-analog-vs-digital/
- publish/en/4-safety-security-and-privacy/
- publish/en/5-money-matters/
- publish/en/6-bitcoin-basics/

Read in full before editing:

- workspace/06_template-OLD.md
- workspace/06_template-NEW.md
- workspace/06_template-MIGRATE.md
- workspace/06_template-migration-plan.md
- every target activity file

Apply the confirmed rules in workspace/06_template-migration-plan.md exactly. In particular:

1. Preserve the activity title and move Activity type, Duration, Grouping, Description, Learning Outcomes, Objective In Student’s Words, Materials, Equipment, Notes content, appendices, and references to their confirmed destinations.
2. Use the new template’s heading names and order. Create empty Keywords, Participation, Preparation, Review, Key Points, and Discussion questions headings, but do not invent content for them.
3. Under `## Procedure`, create one `### Setup` before all Steps. Consolidate all source Setup material there in its source order.
4. Convert every other actual source procedure section into one consecutive `### Step N`, preserving its source order. Put its former name in italics at the start of the step and retain all body content exactly. Do not add an empty step or a step for a missing source section.
5. Convert Notes subsections to the confirmed bold inline labels. Do not use Notes subheadings or bold-wrap the label’s full body.
6. Do not create lesson content, remove lesson content, revise wording, or make curriculum edits. Preserve Markdown lists, emphasis, links, and references.
7. Work one file at a time. After each file, verify that all of its non-heading source content appears exactly once in the migrated file. If any content cannot be placed confidently, leave that file unchanged and report it as unresolved.
8. Do not edit any file outside the six listed activity folders.

When complete, return a table with: file path, migrated or skipped status, number of source Setup blocks consolidated, number of Steps created, Notes labels present, Additional Resources present, and unresolved content (if any).
```

---

## Prompt 3 — Per-file structural and content review

Run after Prompt 2. This prompt is read-only unless the user separately asks for corrections.

```text
Review every migrated Markdown activity in the six publish/en chapter folders against its original version in ref/bitcoin-for-juniors/en/ at the matching relative path, plus:

- workspace/06_template-NEW.md
- workspace/06_template-migration-plan.md

Do not edit files.

For each activity, verify:

1. it has the new template’s destination headings in order;
2. Keywords, Participation, Preparation, Review, Key Points, and Discussion questions are empty unless content was explicitly mapped to them;
3. `## Procedure` contains exactly one `### Setup` before the Step series;
4. Steps are consecutively numbered from 1, with no empty placeholders or gaps;
5. each Step corresponds to one actual source procedure section and retains that section’s name as an italic inline lead-in;
6. no source Setup material remains in a Step;
7. all non-heading lesson content is present exactly once, except that content may have moved structurally;
8. Notes uses only the approved bold inline labels and preserves embedded accessibility, younger-student, and safety guidance; and
9. Additional Resources contains every mapped appendix and reference.

Report only defects, grouped by file, with the exact correction needed. Do not make changes.
```

---

## Prompt 4 — Correct confirmed defects

Run only after reviewing Prompt 3’s defect report. It must not make editorial improvements.

```text
Correct only the defects identified in the approved review report for the Bitcoin for Juniors activity migration.

Read:

- workspace/06_template-NEW.md
- workspace/06_template-migration-plan.md
- the approved defect report
- each affected migrated activity
- its matching original in ref/bitcoin-for-juniors/en/

For every correction, preserve source wording and apply only the confirmed structural rules. Do not edit an unaffected file, alter lesson content, add new content, or make stylistic changes.

After correcting each file, verify that its non-heading source content appears exactly once. Return a table listing the file, each corrected defect, and any remaining unresolved issue.
```

---

## Prompt 5 — Final migration audit (read-only)

Run after corrections are complete.

```text
Perform a final read-only audit of all Bitcoin for Juniors activity migrations in the six publish/en chapter folders.

Read:

- workspace/06_template-NEW.md
- workspace/06_template-migration-plan.md
- all migrated publish/en activity files
- their matching original files in ref/bitcoin-for-juniors/en/

Confirm and report:

1. the total number of activity files reviewed and migrated;
2. that every activity has exactly one Setup before its Step series;
3. that every Step series is consecutive and contains no invented or blank steps;
4. that all non-heading source content appears exactly once in its migrated activity;
5. that all required empty destination-only headings are present and empty;
6. that Notes labels are bold inline labels with the approved names;
7. that all appendices and references appear in Additional Resources; and
8. every unresolved issue, if any.

Do not edit files. State explicitly whether the migration is complete.
```
