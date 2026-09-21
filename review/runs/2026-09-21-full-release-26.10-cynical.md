# Review run: 2026-09-21 — full release 26.10 cynical review

## Run details

| Field | Record |
| --- | --- |
| Mode | `full-release` |
| Scope | Every document recursively contained in `publish/` |
| Requested by | Repository user |
| Reviewer | Codex, acting under `review_cynical_editor.md` |
| Source version | In-scope working-tree state on 2026-09-21 |
| Started / completed | 2026-09-21 / 2026-09-21 |

This revised report applies a hard scope boundary: only documents stored in `publish/` are review evidence.

## Review coverage

The review inspected all 47 files contained in `publish/`:

- all five core files in `publish/mfb-bd-26.10/`: Student Guide, Educator Guide, Quick Start, Assessment Grid, and Lexicon;
- all 30 activity files in `publish/mfb-act-26.10/`;
- the Advanced README and all eight Advanced module files in `publish/mfb-adv-26.10/`; and
- the optional self-check Markdown source and both CSV exports in `publish/mfb-ml-26.10/`.

The review compared in-scope documents with one another but did not inspect or use anything outside `publish/` as evidence. This was a source review. No rendered PDF, EPUB, application import, classroom session, or accessibility session was included.

## Cynical-editor findings

| ID | Severity | File and stable heading | Defect | Evidence | Consequence | Required correction or decision | Acceptance condition | Related in-scope file or none |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CYN-001 | Critical | `publish/mfb-act-26.10/mfb-act-018-creating-your-first-bitcoin-wallet.md` — procedure and notes | A published activity gives unsafe live-wallet instructions and tries to retract them afterward. | The procedure tells an educator to download a wallet, add sats for each learner, let learners create or restore wallets, and record or enter a 12- or 24-word recovery phrase. Only a later note says the activity is not certificated as written and should use an approved prepared simulation. | A learner or educator can expose a recovery secret, lose funds, normalize seed entry, or mistake live-value handling for an approved assessment. The later disclaimer does not neutralize the earlier procedure. | Withdraw the activity or rewrite the procedure itself around a fake, disposable, no-value environment. Put the prohibition on real secrets and funds before the first action. | A safety reviewer can execute every numbered step without creating, viewing, recording, sharing, or funding a real learner secret, and the safe route is the only route described. | `publish/mfb-bd-26.10/mfb-bd-eg-26.10.md` — universal safety rules |
| CYN-002 | High | `publish/mfb-act-26.10/` — all activity files | The activity bank is visibly unfinished. | Across the 30 activity files, 130 H2 sections are empty, including 19 empty Duration sections. Several files contain little more than headings or a video instruction, and none explicitly labels an offline, low-tech, or no-internet alternative. | Educators cannot reliably estimate time, prepare materials, identify evidence, recover from unavailable media, or distinguish a complete activity from a shell. | Complete or remove every empty section, state the learner output and educator evidence, and add a usable fallback wherever the activity depends on a device, video, website, or live tool. | No released activity has an empty operational section; every dependency has a stated fallback; and every activity can be followed without inventing missing steps. | `publish/mfb-bd-26.10/mfb-bd-qs-26.10.md` — delivery planning |
| CYN-003 | High | `publish/mfb-act-26.10/mfb-act-001-auction.md`; `publish/mfb-act-26.10/mfb-act-002-consensus.md` | Several activities present polemic as fact. | The auction activity says monetary inflation leads to price inflation and alleges that news media and central planners prefer CPI because it can be manipulated. The consensus activity says human leaders “always succumb” to debasement and declares decentralization critical to Bitcoin's value. These claims are categorical and unsourced in the published activity files. | Learners are pushed toward a predetermined ideological conclusion instead of evaluating evidence and trade-offs. This weakens trust in the entire course. | Rewrite the claims as bounded arguments, distinguish mechanisms from value judgements, and provide enough context for learners to evaluate limitations or competing explanations. | An independent factual reviewer can support every retained material claim, and no universal claim exceeds its evidence. | `publish/mfb-bd-26.10/mfb-bd-sg-26.10.md` — inflation and money sections |
| CYN-004 | High | `publish/mfb-bd-26.10/mfb-bd-eg-26.10.md` — The minimum eight-hour pathway and operational assessment protocol; `mfb-bd-assessment-grid-26.10.md` | The eight-hour minimum is not operationally convincing for the supplied assessment model. | The lower observation-time estimates in the Educator Guide total 32 minutes per learner and the upper estimates total 45. Applied to the 12 learner rows in the Assessment Grid, that is 6.4 to 9 educator-hours before teaching, practice, setup, feedback, recording, or reassessment. Some evidence can overlap, but the published protocol also requires individual evidence and rejects group participation as a substitute. | Educators may overrun the stated route or weaken individual evidence to fit it. The documents do not state the cohort and assessor assumptions that make eight hours plausible. | State the maximum cohort size, assessor count, concurrent-observation assumptions, and protected assessment time for the eight-hour route, or qualify the route more clearly. | A complete schedule demonstrates how teaching, practice, individual evidence, feedback, recording, and realistic reassessment fit the stated cohort and staffing assumptions. | `publish/mfb-bd-26.10/mfb-bd-sg-26.10.md` — four-module learning path |
| CYN-005 | High | `publish/mfb-bd-26.10/mfb-bd-sg-26.10.md` — Next Steps | Draft-condition language and promotional choices appear inside the learner publication. | The guide includes headings such as “Source or update page, if included” and “Optional donate / support QR.” The same closing material directs learners to named training, network, dashboard, leaderboard, case-study, form, donation, and AI-assistant destinations. | “If included” is an unresolved editorial note, not learner-facing prose. The volume of named destinations turns the ending into promotion and makes the core next step unclear. | Decide whether each conditional block is included, remove drafting language, and reduce the closing section to a small, clearly prioritized set of optional next steps. | No conditional editorial wording remains, every retained call to action has a distinct learner purpose, and the primary next step is obvious. | None |
| CYN-006 | High | `publish/mfb-ml-26.10/mfb-ml-26.10.md` — Authoring metadata | The optional self-check declares itself unreviewed. | All 12 question pairs say “Needs independent factual and editorial review.” The same file says every question appears on one screen, but the in-scope documents provide no small-phone or screen-reader test result. | An optional feature can still teach an error, confuse learners, or fail on the target device. “Optional” does not excuse an unfinished review state. | Independently review every selected item and explanation, reconcile the Markdown with both CSV exports, and test the actual presentation before release. | Every shipped item has a completed review state, the CSV content matches the approved source, and device/accessibility results are recorded. | `publish/mfb-ml-26.10/mfb-ml-26.10-short-questions.csv`; `mfb-ml-26.10-long-questions.csv` |
| CYN-007 | Medium | `publish/mfb-adv-26.10/README.md`; `publish/mfb-adv-26.10/mfb-adv-001-*.md` through `mfb-adv-008-*.md` | The Advanced README contradicts the directory it describes. | The README says Advanced modules “will be published here when they are available,” while eight substantial Advanced module files already sit beside it in `publish/`. | A release process or reader cannot tell whether the eight files are available publications, drafts, or accidental inclusions. | Give every Advanced file an explicit status and make the README describe the directory as it actually exists. | The README and all nine files agree on which modules are published, excluded, or drafts. | None |
| CYN-008 | Medium | `publish/mfb-bd-26.10/mfb-bd-sg-26.10.md` — introduction and Modules 3–4; `mfb-bd-eg-26.10.md` — front matter | The guides repeat the same architecture and boundaries enough to create bloat and drift, and one repetition is an outright production error. | In 34 introductory lines, the Student Guide explains the four-module arc, required educator-curated Module 4, and separate Advanced path before and after three proposed visuals. Module 4 then occupies roughly 460 lines. The Educator Guide repeats the model, navigation, assessment, purpose, and quick-start material across extensive front matter before Chapter 1. In “On-chain and Lightning payments,” `BD-V-049` appears twice consecutively; the first instance wrongly carries the preceding acquisition-path alt text. | Readers repeatedly encounter the course map instead of new information; editors must maintain near-copies; contradictions and marker errors become more likely. | Keep one canonical learner map, consolidate adjacent explanations, shorten material that belongs in educator guidance, and delete the duplicate/mislabelled marker. | Every retained recap has a distinct navigational or learning purpose, and no adjacent visual marker repeats an ID or carries unrelated alt text. | None |
| CYN-009 | Medium | Student Guide — four-module table; Educator Guide — Diploma at a glance and Module 4 opening | Published guiding questions drift within and across the guides. | The Student Guide asks, “How do I use and secure Bitcoin responsibly?” for Module 3, while the Educator Guide asks, “How do I take responsibility for using and securing Bitcoin?” More seriously, the Educator Guide's Module 4 summary asks how problem, solution, and safe action connect to the community, but the Module 4 opening changes the question to “How can Bitcoin function as money in this community?” | Educators can treat Module 4 as adoption advocacy rather than a reasoned local connection, and learners do not receive one stable inquiry across the two guides. | Choose one published guiding question per module or explicitly explain the audience-specific variation. | The Student Guide table, Educator Guide summary, module openings, and assessment prompts use the same approved question or clearly state why a variant is necessary. | `publish/mfb-bd-26.10/mfb-bd-sg-26.10.md`; `mfb-bd-eg-26.10.md` |

## Cross-publication consistency matrix

| Check | In-scope publications compared | Result | Related finding |
| --- | --- | --- | --- |
| Safety rules versus activity procedure | Educator Guide, Student Guide, wallet activity | Conflict: guide safety is undermined by the activity sequence | CYN-001 |
| Activity completeness | All 30 activity files, Quick Start | Missing operational content | CYN-002 |
| Neutral explanatory tone | Student Guide, auction activity, consensus activity | Conflict | CYN-003 |
| Eight-hour delivery and assessment load | Student Guide, Educator Guide, Quick Start, Assessment Grid | Insufficient assumptions and demonstration | CYN-004 |
| Learner next-step status | Student Guide | Unresolved conditional wording | CYN-005 |
| Self-check readiness | Self-check Markdown and both CSV exports | Source explicitly requires further review | CYN-006 |
| Advanced availability | Advanced README and eight module files | Direct contradiction | CYN-007 |
| Repetition and duplicate identifiers | Student Guide and Educator Guide | Material repetition plus duplicated visual ID | CYN-008 |
| Guiding questions | Student Guide and Educator Guide | Internal and cross-guide drift | CYN-009 |

## Findings created or updated

This revised publish-only run records `CYN-001` through `CYN-009`. Earlier observations that depended on files or destinations outside `publish/` were removed rather than retained as background. No publication file was edited.

## Verification needs raised by in-scope documents

- The factual and causal claims quoted in CYN-003 require independent source verification before they can be treated as instructional fact.
- The timing claim in CYN-004 requires a field test using the cohort and assessor model stated in the published documents.
- The self-check in CYN-006 requires independent editorial/factual review, source-to-CSV comparison, and device/accessibility testing because its own metadata says that review is outstanding.
- The guides require render, print, keyboard, screen-reader, small-phone, and QR testing before publication mechanics can be judged.

These are verification needs created by statements inside `publish/`; this run did not inspect any out-of-scope evidence to resolve them.

## Editor-discretion judgements

| Subject | Editor decision | Rationale from in-scope documents | Date | Related finding |
| --- | --- | --- | --- | --- |
| Release readiness | Treat the Critical and High findings as blockers | They concern unsafe instructions, incomplete activities, polemical claims, unsupported delivery assumptions, unresolved learner-facing content, and an explicitly unreviewed self-check | 2026-09-21 | CYN-001–CYN-006 |
| Wallet activity | Do not rely on the late note | Readers execute instructions in sequence; a correction after the dangerous procedure is not an effective control | 2026-09-21 | CYN-001 |
| Activity status | Treat files under `publish/` as intended for reader use | The directory location gives educators no reason to assume that empty sections are harmless drafts | 2026-09-21 | CYN-002, CYN-003 |
| Eight-hour wording | “At least” does not solve the missing operational assumptions | The guides also call eight hours the shortest planned route and provide a 12-row assessment grid | 2026-09-21 | CYN-004 |
| Repetition | Count repeated function, not repeated vocabulary | Safety reminders can be justified; adjacent architecture explanations and duplicate visual IDs do not each perform a distinct job | 2026-09-21 | CYN-008 |

## Checks completed

- [x] Enumerated every file recursively inside `publish/`.
- [x] Inspected all five core Diploma publication files.
- [x] Inspected all 30 activity files.
- [x] Inspected the Advanced README and all eight Advanced modules.
- [x] Inspected the self-check Markdown source and both CSV exports.
- [x] Reviewed accuracy, internal logic, missing context, reader failure points, language, repetition, and publication-source mechanics.
- [x] Compared terminology, promises, safety instructions, assessment expectations, and guiding questions across in-scope publications.
- [x] Challenged the findings and removed every observation that depended on material outside `publish/`.

## Checks not performed or deferred

- No file outside `publish/` was reviewed or used as evidence.
- No external link destination or referenced file outside `publish/` was opened or judged.
- Final PDF, EPUB, or web rendering was not available in scope.
- Screen-reader, keyboard, low-vision, small-phone, print, and QR testing was not performed.
- Classroom timing, assessor agreement, learner comprehension, and reassessment were not observed.
- The two CSV files were inspected as source documents but were not imported into a live application.
- No legal, privacy, safeguarding, tax, regulatory, translation, or specialist factual review was claimed.

## Review verdict

**Do not release the current contents of `publish/` as the full 26.10 release.**

The publish-only review found one Critical defect, five High defects, and three Medium defects. The dominant problems are unsafe wallet instructions, an unfinished activity bank, polemical activity claims, an eight-hour route without convincing cohort and assessment assumptions, unresolved learner-facing back matter, and an explicitly unreviewed app self-check.

The repetition pass also found substantial avoidable duplication and a concrete production error: `BD-V-049` appears twice consecutively with conflicting alt text.

Minimum release gate: correct CYN-001; close or remove from release every High finding; clarify Advanced status; consolidate the repeated guide material; align the guiding questions; then rerun the publish-only review against the corrected source documents and final rendered publications.

## Review report summary

**Verdict: not ready.** Scope was limited to all 47 documents in `publish/`. Findings: one Critical, five High, and three Medium. The three most important defects are the unsafe recovery-phrase activity, the structurally unfinished activity bank, and the unreviewed self-check. Source inspection and cross-publication comparison were completed; rendering, accessibility, classroom, application-import, and specialist factual tests were not. Correct the Critical finding and all High findings before rerunning this publish-only review. This run record is not a source of truth.
