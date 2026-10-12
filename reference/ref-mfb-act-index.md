# Activities template comparison checklist

This is a structural conformance record for the activity library. Every published activity follows the import-ready heading pattern in `mfb-act-000-template.md`.

## Resources Hub import formatting

The Resources Hub importer maps Markdown heading levels to activity fields. Use the following structure in every activity:

- `####` for the named sections: Preparation, Setup, Procedure, Key points, Discussion questions, Notes, and Resources and references
- `#####` for each procedure step
- `######` only for content nested inside a procedure step, such as a model

Use `1.` for every ordered-list item. The published renderer supplies the visible numbering. Use `-` or `*` for unordered-list items. Indent every sub-list by two spaces.

## Required heading order

1. `#` Activity title
2. `##` Keywords
3. `##` Activity type
4. `##` Participation
5. `##` Duration
6. `##` Objective
7. `##` Description
8. `####` Preparation, with a bold **Materials** label if needed
9. `####` Setup
10. `####` Procedure
    - `#####` Step 1 and any additional steps
    - `######` content within a step only
11. `####` Key points
12. `####` Discussion questions
13. `####` Notes
14. `####` Resources and references

Activities may add plain-text labels within a section, but they must not change this sequence or the importer heading levels. A heading may deliberately have no immediate body text because it organizes later content in the published structure.

## Status at 2026-10-08

| Scope | Result | Evidence |
| --- | --- | --- |
| Template | Pass | Defines the required one-H1, H2-metadata, H4-import-section, H5-procedure-step pattern. |
| Activities 001–030 | Pass | Each has the complete required import-heading sequence in order, with H4 activity fields and H5 procedure steps. |
| Heading labels | Pass | Shared metadata and section labels use sentence case. |

## Follow-up

Check the rendered Resources Hub activity pages after the next deployment. Source Markdown structure does not verify the deployed presentation or accessibility tree.
