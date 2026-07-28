# Reviewer comment to-do list

Source: [`comments.md`](comments.md), extracted from `feedback/2026-06-23_08_draft.docx`.

This list turns reviewer comments into review actions. It does not implement any curriculum changes. Source comment IDs are preserved for traceability.

Draft references below use the current line numbers in `workspace/08_draft.md`. They should be rechecked if the draft is edited.

## Status key

- `[ ] Open`: requires an editorial or curriculum action.
- `[?] Decision`: requires the curriculum team to decide before editing.
- `[~] Verify`: the draft or a reply suggests this may already be addressed; confirm before closing.
- `[!] Anchor warning`: the comment’s OOXML anchor is malformed or non-lexical.

## Editorial and curriculum actions

- [~] Standardize usage of “open-source” and “open source” throughout the document. Confirm the intended house style and check all occurrences.
  - Source: COMMENT-001; COMMENT-002 is an acknowledgment reply.
  - Draft: lines; 9, 26, 1493, 1523.

- [~] Decide whether “digital assets” should be replaced with “tokens” in the Bitcoin-only explanation. Check that the final wording remains clear and translation-ready.
  - Source: COMMENT-003; COMMENT-004 is an acknowledgment reply.
  - Draft: line; 24.

- [ ] Define “fiat” before its first learner-facing use, or remove/defer early uses until the definition appears.
  - Source: COMMENT-005, COMMENT-006.
  - Draft: early uses, lines; 48, 66, 86; current definition, lines; 319–323.
  - This include the title of Block 1 and must be made throughout the project's structure.

- [ ] [Anchor warning] Add a visually distinct early breakout definition of “fiat” so learners encounter the term with context before later technical discussion.
  - Source: COMMENT-008, COMMENT-009.
  - Anchor warning: both comments have duplicate OOXML range starts and attach only to ` (` in the export.
  - Draft: early context, line; 48; later definition to relocate or repeat, lines; 319–323.

- [~] Verify that the early Nixon Shock passage includes enough context for the term and does not introduce unsupported historical claims.
  - Source: COMMENT-007.
  - Draft: line; 313.

- [ ] Decide whether to add a short Cantillon effect section after the current monetary discussion. If added, define the concept simply and keep it distinct from investment advice.
  - Source: COMMENT-012.
  - Draft: current monetary discussion and suggested insertion point, lines; 355–365, especially line; 363.

- [?] Review the CBDC section’s placement and framing: move it later if appropriate, then decide how strongly to describe surveillance, programmable restrictions, confiscation, and limits by category, time, or geography. Validate wording with current, local, reliable sources.
  - Source: COMMENT-013.
  - Draft: lines; 369–390, especially design trade-offs at lines; 373–377.

- [?] Decide whether the questions and review prompts should be retained, shortened, or adapted for older adult learners and different learning contexts.
  - Source: COMMENT-014.
  - Draft: Block 1 review, lines; 408–426.

- [ ] Confirm the technical-introduction sequence:
  - keep the early double-spend explanation at a high level;
  - introduce decentralization without requiring miners, nodes, chains, and proof-of-work all at once;
  - introduce the Blockchain, Bitcoin network, miners, and nodes before later uses of those terms;
  - defer the full transaction-validation method to the later Deeper Dive / Decentralization material.
  - Source: COMMENT-015, COMMENT-016, COMMENT-017, COMMENT-018, COMMENT-019.
  - Note: the draft contains inserted sections in this area; verify the resulting flow rather than assuming the comments are fully resolved.
  - Draft: early double-spend sequence, lines; 456–481; decentralization and terminology, lines; 500–518 and 578–601.

- [~] Verify the placement and scope of the “Deeper Dive” section and confirm that the basic wallet introduction appears early enough to support later terms such as keys, wallets, nodes, and miners.
  - Source: COMMENT-021, COMMENT-022.
  - Draft: “Deeper Dive” reference in the architecture, line; 190; current wallet introduction, lines; 693–707. No heading named “Deeper Dive” is currently present.

- [~] Verify the halving explanation: exactly 210,000 blocks, with “roughly every four years” presented as an approximation rather than a fixed calendar schedule.
  - Source: COMMENT-020.
  - Draft: explanation, line; 532; review prompt, line; 681.

- [ ] Standardize the terminology for KYC pathways. Choose either “no-KYC” / “non-KYC” according to the lexicon and apply it consistently in headings and body text.
  - Source: COMMENT-023; COMMENT-024 is an acknowledgment reply.
  - Draft: earlier terminology, line; 1011; heading and comparison, lines; 1322–1334.

- [ ] Expand the closing “Contribute” area with clear calls to action for proofreading, volunteering, feedback, and ETP sign-up, including the appropriate forms link.
  - Source: COMMENT-025, COMMENT-026.
  - Anchor warning: COMMENT-026 is attached only to a paragraph boundary in the export.
  - Draft: existing contribution prompt, line; 1470; current closing links, lines; 1491–1499.

- [ ] Add next-step information about the Education Network and ETP. Decide whether to restore or develop case studies and explain any leaderboard/perk connection with current links.
  - Source: COMMENT-027.
  - Anchor warning: COMMENT-027 is attached only to a paragraph boundary in the export.
  - Draft: nearest existing next-step content, lines; 1459–1499. No Education Network, ETP, case-study, or leaderboard content is currently present.

- [ ] Add a Resources Hub contribution call to action and a separate prompt to install or download the app where appropriate.
  - Source: COMMENT-028.
  - Draft: existing app references, lines; 129–131; nearest closing CTA area, lines; 1459–1499. No Resources Hub CTA is currently present.

## Recommended review order

1. Resolve terminology and first-use issues: fiat, open-source, digital assets/tokens, and KYC.
2. Confirm the Bitcoin technical-introduction architecture and the placement of wallet/deeper-dive material.
3. Review learner-audience and CBDC framing decisions.
4. Complete the closing calls to action, Education Network/ETP information, case-study decision, and links.
5. Re-check likely resolved items against the final draft and close them only after verification.
