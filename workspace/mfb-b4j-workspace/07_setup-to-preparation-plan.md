# Setup-to-Preparation Migration Plan

## Goal

Move all information currently presented as `### Setup` into each activity's `## Preparation` section, across the 21 published activities. After migration, `## Procedure` begins with `### Step 1`.

This is a structural relocation, not a rewrite: preserve wording, lists, links, timing, emphasis, and source order unless a line must move to keep pre-class preparation distinct from learner-facing facilitation.

## Scope and Baseline

- In scope: the 21 activity files in `publish/en/1-*` through `publish/en/6-*`.
- Out of scope: front matter, resource files, and `ref/` source files.
- Baseline: all 21 `## Preparation` sections are empty. Twenty activities have a `### Setup` block. Activity 6.2 has an empty Setup block, but has three pre-class preparation bullets in Step 1.
- Target structure:

  ```md
  ## Preparation
  [migrated preparation content]

  ## Procedure
  ### Step 1
  ```

## Migration Rules

1. Move the complete body of every non-empty `### Setup` block to the immediately preceding `## Preparation` section, retaining list structure and internal order.
2. Remove `### Setup` from all 21 activity files, including the empty heading in 6.2.
3. Preserve active, student-facing directions after the move. Do not silently reword them as pre-class tasks; flag any item that cannot sensibly be completed before learners arrive for editorial review.
4. For 6.2, move the three preparation bullets currently under `### Step 1` into `## Preparation`, then leave the otherwise-empty Step 1 in place unless a separate procedure-cleanup decision is made.
5. Do not move procedure steps, opening activities, model/carry-out instructions, checkpoint questions, follow-up, close, Notes, or appendices as part of this change.
6. Do not change source files in `ref/`; they document the earlier structure.

## Activity Checklist

| Module | Activity | File | Content to relocate from Setup |
|---|---|---|---|
| 1 | 1.1 Ship Rekt | `publish/en/1-exchange-value-and-price/1-ship-rekt.md` | Card distribution, suit/object explanation, use-and-trade prompts, shell hiding/rules, and commodity-money setup. **Editorial review:** much of this is live facilitation. |
| 1 | 1.2 Going, Going, Gone | `publish/en/1-exchange-value-and-price/2-going-going-gone.md` | Auction and shell-bidding explanation. **Editorial review:** live facilitation. |
| 1 | 1.3 What Is Value? | `publish/en/1-exchange-value-and-price/3-what-is-value.md` | Sticky-note prompt, colour guidance, and price/value board axes. |
| 1 | 1.4 Worth It? | `publish/en/1-exchange-value-and-price/4-worth-it.md` | Price continuum creation and labels. |
| 2 | 2.1 Work, Rest, and Play | `publish/en/2-time-energy-and-reward/1-work-rest-and-play.md` | Work/rest/play poster or board and visible flashcards. |
| 2 | 2.2 Energy Economy | `publish/en/2-time-energy-and-reward/2-energy-economy.md` | Visual-aid, tracker-graph, axis explanation, and activity-prompt directions. **Editorial review:** explanation/prompt items are live facilitation. |
| 2 | 2.3 That's Not Fair | `publish/en/2-time-energy-and-reward/3-that-s-not-fair.md` | My Stack goal, voting, bead-return, and repeat-round rules. **Editorial review:** live facilitation. |
| 2 | 2.4 That's Not Fair: Story Time | `publish/en/2-time-energy-and-reward/4-that-s-not-fair-story-time.md` | Book-cover/character introduction and pause expectation. **Editorial review:** live facilitation. |
| 2 | 2.5 Time Preference | `publish/en/2-time-energy-and-reward/5-time-preference.md` | Story/picture discussion framing and respectful-listening reminder. **Editorial review:** live facilitation. |
| 2 | 2.6 Smart Choices | `publish/en/2-time-energy-and-reward/6-smart-choices.md` | Building-material metaphor and choice framing. **Editorial review:** live facilitation. |
| 3 | 3.1 Evolution of Technology | `publish/en/3-analog-vs-digital/1-evolution-of-technology.md` | Worksheet distribution and board instructions. **Editorial review:** worksheet distribution is live facilitation. |
| 3 | 3.2 Vote with Your Feet | `publish/en/3-analog-vs-digital/2-vote-with-your-feet.md` | OLD/CENTER/NEW classroom zones, boundaries, and movement rules. |
| 3 | 3.3 Invent the Future | `publish/en/3-analog-vs-digital/3-invent-the-future.md` | Dragons' Den format, pitch expectations, and grouping assignment. **Editorial review:** live facilitation. |
| 4 | 4.1 Gatekeepers | `publish/en/4-safety-security-and-privacy/1-gatekeepers.md` | Public/private/choice framing and no-single-answer expectation. **Editorial review:** live facilitation. |
| 4 | 4.2 Wire Tap | `publish/en/4-safety-security-and-privacy/2-wire-tap.md` | Team division, round structure, and mistakes-safety framing. **Editorial review:** live facilitation. |
| 4 | 4.3 Cypherpunks Write Code | `publish/en/4-safety-security-and-privacy/3-cypherpunks-write-code.md` | Secret-message framing and alphabet/letter-shift demonstration. **Editorial review:** live facilitation. |
| 4 | 4.4 Nostr | `publish/en/4-safety-security-and-privacy/4-nostr.md` | Three-person teams, roles, and fixed-role rule. **Editorial review:** role assignment is live facilitation. |
| 5 | 5.1 Money Matters | `publish/en/5-money-matters/1-money-matters.md` | Station opening, HOME-tile placement, Town Square, and learner starting locations. |
| 6 | 6.1 From Problem to Protocol | `publish/en/6-bitcoin-basics/1-from-problem-to-protocol.md` | Seating formation and story/white-paper prop. **Editorial review:** seating is live facilitation. |
| 6 | 6.2 Satoshi, Where Are You? | `publish/en/6-bitcoin-basics/2-satoshi-where-are-you.md` | Remove the empty Setup heading; move Step 1's whiteboard, markers, and group-arrangement preparation bullets into Preparation. |
| 6 | 6.3 It's Mine | `publish/en/6-bitcoin-basics/3-it-s-mine.md` | Team division, wallet-envelope distribution, MEMPOOL cards, and BLOCK-envelope placement. **Editorial review:** grouping/distribution is live facilitation. |

## Governing-Format Updates

Update these files in the same change so they no longer require the old Setup heading:

1. `workspace/05_spec.md`: change the procedure definition from “Setup, Step 1, Step 2, Step 3” to “Step 1, Step 2, Step 3,” and state that Preparation holds pre-class setup.
2. `workspace/06_template-NEW.md` and `workspace/06_template-MIGRATE.md`: remove `### Setup`.
3. `publish/en/0-front-matter/3-introduction.md`: replace the Setup description with a Preparation description and remove Setup from the activity sequence.
4. `workspace/y_06_template-migration-plan.md`: mark as superseded or revise before it is used again, because it currently directs contributors to consolidate Setup under Procedure.

## Execution Sequence

1. Apply the mechanical relocation in module order (1 through 6), retaining all Markdown formatting.
2. Resolve each marked editorial-review item: either confirm that live facilitation belongs in Preparation under the new convention, or leave that content in the first appropriate procedure step and move only true pre-class work. Record the decision consistently.
3. Make the governing-format updates after the activity decision is settled.
4. Validate programmatically: 21 activity files; 21 non-empty Preparation sections; zero `### Setup` headings; each Procedure begins with `### Step 1`; no content loss.
5. Perform a visual Markdown review of one activity per module and the special 6.2 case.

## Acceptance Criteria

- All 21 in-scope activities have populated `## Preparation` sections.
- No in-scope activity contains `### Setup`.
- Each activity retains the same procedural Steps and ordering, except for 6.2's three moved preparation bullets.
- All templates, specification, and learner-facing format guidance agree that preparation precedes procedure and Setup is no longer a procedural subheading.
- Editorial-review items have an explicit, consistent disposition before publication.
