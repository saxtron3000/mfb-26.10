# Review todo script

## Purpose

Use this script to run a routine, evidence-based review of [review_todo.md](review_todo.md). Check every `ACT-`, `ANN-`, and `DEC-` item one by one against the current project. Update the register with concise status, evidence, and next-step information so another reviewer can reproduce and check the result quickly.

This script is a review control, not a curriculum authority. Do not treat a task, historical annotation, old report, or this script as approval to change policy. Use the current project documents as evidence and preserve unresolved conflicts for later decision.

## Opening instruction

Run this review in the current repository. Read [AGENTS.md](../AGENTS.md) and [review_todo.md](review_todo.md). Review every `ACT-`, `ANN-`, and `DEC-` item in ID order. For each item, inspect the current publications in `publish/` first, then consult the relevant authorities and supporting detail in `workspace/`. Update `review_todo.md` as evidence is found. Do not skip an item because it appears historical, repetitive, or likely resolved.

Record the review date. Create a dated run record in `review/runs/` from [runs/template.md](runs/template.md), and link the run record from every updated or newly created action. When current evidence reveals a distinct actionable gap that no existing `ACT-`, `EVO-`, or `PUB-` item covers, create the next sequential `ACT-` item with the required structured record, reported date, and run link. Do not leave actionable review findings only in the run report.

## Source order and authority

Use this order for every item:

1. Read the item, its status, acceptance condition, dependencies, and surrounding section in `review_todo.md`.
2. Search all relevant files under `/Users/saxtron3000/Documents/MFB/programs/mfb-bd-26.10/publish/` first. Treat these as implementation evidence.
3. If publication evidence is missing, incomplete, ambiguous, or contradictory, inspect the relevant files under `/Users/saxtron3000/Documents/MFB/programs/mfb-bd-26.10/workspace/` for the governing requirement, planned boundary, decision, or supporting detail.
4. Use `AGENTS.md` and `workspace/00_index.md` to identify ownership and source-of-truth boundaries.
5. If the workspace authority conflicts with a publication, report the conflict. Do not silently decide which policy should win.

Use fast text search such as `rg` to locate the item’s terms, IDs, headings, and likely evidence. Read each match in context. Do not rely on a search hit alone.

## Evidence-link rule

When an item is complete, add evidence immediately beside its status or completion wording in `review_todo.md`. Evidence is required for every completed item.

Use a clickable repository-relative Markdown link with the file and line number:

```markdown
Evidence: [Student Guide:123](../publish/mfb-bd-26.10/mfb-bd-sg-26.10.md:123)
```

Use the nearest stable heading anchor as well when it helps the reviewer orient themselves:

```markdown
Evidence: [Student Guide:123](../publish/mfb-bd-26.10/mfb-bd-sg-26.10.md:123#module-3-using-bitcoin-safely)
```

For more than one supporting passage, add separate links. Prefer publication evidence. Add workspace evidence when it explains the requirement, confirms the decision, or documents why publication evidence is sufficient. Keep the evidence concise and specific: name the file, line, and what the passage proves.

Line numbers are a convenience for the current snapshot, not a substitute for a heading or claim ID. If the file changes, refresh the line number on the next review. Never cite a line number you did not inspect.

## Status and completion rules

### `ACT-` actions

Assess the acceptance condition, not merely whether related wording exists.

- If the acceptance condition is fully met, update the checkbox to `[x]`, set `Status: done`, update the date, and add clickable evidence with file and line.
- If work is underway but the acceptance condition is not met, keep the item open and update `Status: in-progress` only when the current record supports that status. Add the evidence found and state what remains.
- If the item cannot be judged from the current files, use `Status: needs-verification` and record the missing evidence or required human decision.
- If the item is blocked by an unresolved dependency, use `Status: blocked`, name the dependency, and do not mark it complete.
- Do not mark an action complete because a plan, placeholder, or proposed wording exists. Require the stated implementation, approval, test, or completion evidence.

### `ANN-` annotations

An annotation is complete when it has been triaged, not merely when its proposed change appears somewhere in the project. Compare the note with current text and evidence, then record one of the dispositions defined in `review_todo.md`: `already-addressed`, `approved-action`, `rejected`, `superseded`, `duplicate`, `preserve-approval`, or `needs-clarification`.

- Check `[x]` only after recording the disposition, evidence, and any linked `ACT-` item.
- Use `already-addressed` only when current publication evidence shows the requested point is covered.
- Use `approved-action` only when the note is still a valid action and has been linked to an active task or has a clear implementation record.
- Use `preserve-approval` for an approval that must remain visible, not as proof that every related proposal is complete.
- Use `needs-clarification` when the source wording, handwriting, reviewer identity, or intended change is not clear. Do not guess.
- Keep the original source marker, annotation wording, and provenance intact.

If an annotation has not yet been triaged, leave it unchecked and add no unsupported completion claim. If useful, add a short current-evidence note without changing its historical meaning.

### `DEC-` decisions

Assess whether the question has a current, authorized answer and whether affected files agree.

- Mark a decision resolved only when the answer is recorded and the required dependent publications and workspace authorities are aligned.
- Add evidence links to the implementation and the recorded decision. Include the decision date and rationale when they are known.
- If the register says “resolved” but current files still conflict, do not preserve the old status blindly. Record the regression or conflict and link it to an open `ACT-` item.
- If no authorized answer is present, keep the decision open or verify-only. Record the exact evidence still needed, owner response, or dependent-file reconciliation.
- Do not infer approval from a draft, an old report, a checkbox, or an annotation marker.

## Item-by-item review loop

Repeat these steps for every ID in numerical order:

1. Locate the complete item record and read its surrounding context.
2. State the test in plain language: what would prove completion?
3. Search `publish/` for the required implementation, wording, link, activity, assessment record, or public output.
4. Read the relevant publication passage and note its exact file, heading, and line.
5. If the result is not clear, inspect the relevant `workspace/` authorities and supporting plans.
6. Compare the publication with the requirement. Check scope, safety, terminology, links, assessment, status, and dependencies where relevant.
7. Update the item immediately: checkbox, status, date, evidence, remaining work, dependency, disposition, or conflict.
8. Move to the next ID. Do not let an unresolved item stop the rest of the review.

When the same evidence supports multiple items, cite it separately in each item. Do not replace item-specific evidence with a general statement such as “see above.”

## What to record when an item is incomplete

If an item is not complete, do not invent a fix or approval. Add any useful information available from the current project:

- the exact gap or missing acceptance condition;
- the publication file and line showing the partial implementation;
- the workspace file and line explaining the intended requirement or unresolved choice;
- the dependency or decision that blocks completion;
- a concise recommended next step;
- the review date.

Keep the item’s existing structure and history. Do not delete completed or unresolved records. Preserve historical alternatives in decision entries and historical wording in annotation entries.

## Final tally and dashboard update

After every `ACT-`, `ANN-`, and `DEC-` item has been reviewed, recalculate the summaries at the top of `review_todo.md`.

Update **To-do qualification and tally**:

- Recount all unique `ACT-` items and reconcile category, status, severity, and release-impact tallies.
- Recount `ANN-` items and separate pending triage from completed triage. Keep source-marker counts as provenance only.
- Recount `DEC-` items and separate resolved decisions from open, verify-only, blocked, or conflicting decisions.
- Ensure every total equals the sum of its categories and every listed ID appears exactly once in the appropriate tally.
- Update the explanatory text if the qualification definitions or counts changed.

Update **Review dashboard**:

- Refresh the overall action count and number checked off.
- Refresh release blockers, decision dependencies, publication work, annotation triage, and decision-register maintenance.
- Replace stale “outstanding” counts and ID ranges with the current item IDs.
- Keep current status labels factual. “Open” means unresolved in the register; it does not mean the underlying proposal is approved.
- Add the review date or snapshot date when the dashboard’s source state changes.

## Final quality checks

Before finishing:

- Confirm every completed item has at least one clickable file-and-line evidence link.
- Confirm links from `review/review_todo.md` use correct relative paths into `publish/` or `workspace/`.
- Confirm every updated line number still points to the cited passage.
- Confirm no historical source marker was treated as current approval or completion.
- Confirm no unresolved conflict was silently converted into a completed task.
- Run `git diff --check` when available and report if the environment prevents it.
- Report the review date, items completed, items left open, evidence gaps, conflicts, and checks not performed.

## Completion report

End the dated run report with `## Review report summary` as its final section. Under that exact heading, include:

- files reviewed and review date;
- counts before and after for `ACT`, `ANN`, and `DEC`;
- IDs marked complete or resolved, with the main evidence links;
- IDs left open, blocked, or needing clarification;
- dashboard and tally updates made;
- checks not performed or evidence that still requires human or external verification.

State that the run record is not a source of truth. Do not place any section or content after this summary.
