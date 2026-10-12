# Activities template comparison checklist

This is a structural conformance record for the activity library. Every published activity follows the heading pattern in the B4J `mfb-act-000-template.md`.

This template is to be used for all activities in mfb-bj_26.10

## Required heading order

1. `#` Activity title
2. `##` Keywords
3. `##` Activity type
4. `##` Participation
5. `##` Duration
6. `##` Objective
7. `##` Description
8. `##` Preparation
   - `###` Materials
   - `###` Setup
9. `##` Procedure
   - `###` Step 1 and any additional steps
10. `##` Review
    - `###` Key points
    - `###` Discussion questions
11. `##` Notes
12. `##` Additional resources

Activities may add H3 subsections within their relevant H2 section, but they must not change this sequence or heading level. A heading may deliberately have no immediate body text because it organizes later content in the published structure.

## Content and spacing annotations

- `## Objective` replaces `## Objectives`. It contains exactly one objective, written as a single bullet point.
- `## Materials` is not a top-level activity section. It is `### Materials` under `## Preparation`.
- Each logical action in `## Procedure` is an H3 heading, numbered in order as `### Step 1`, `### Step 2`, and so on for as many steps as the activity needs.
- Put a blank line immediately before and after every H1, H2, and H3 heading when surrounding content exists. The document's opening H1 may begin on the first line.

## Status at 2026-10-01

| Scope | Result | Evidence |
| --- | --- | --- |
| Template | Pass | Defines the required one-H1, H2-major-section, H3-subsection pattern. |
| Activities 001–030 | Pass | Each has the complete required heading sequence in order, with Preparation, Procedure, and Review subsections at H3. |
| Heading labels | Pass | Shared metadata and section labels use sentence case. |

## Follow-up

Check the rendered Resources Hub activity pages after the next deployment. Source Markdown structure does not verify the deployed presentation or accessibility tree.
