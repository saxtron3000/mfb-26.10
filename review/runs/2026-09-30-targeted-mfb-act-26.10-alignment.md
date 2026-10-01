# Review run: 2026-09-30: activity publications alignment

## Run details

| Field | Record |
| --- | --- |
| Mode | `targeted` |
| Scope | All 32 Markdown files in `publish/mfb-act-26.10/`: the comparison checklist, activity template, and Activities 001–030. |
| Requested by | Project user |
| Reviewer | Codex |
| Source version | Working tree on 2026-09-30. Git baseline was unavailable in the sandbox, so this is a current-text review, not a historical-diff audit. |
| Workspace authority version | `workspace/05_competencies.md`, `06_plan.md`, `10_activities.md`, `13_assessment.md`, `15_certification.md`, and `16_spec.md`, read on 2026-09-30. |
| Scripts used | `review_alignment.md` |
| Started / completed | 2026-09-30 / 2026-09-30 |

## Traceability matrix

| TR-ID | Governing workspace file and heading | Requirement or decision | Expected publication evidence | Actual evidence | State | Verification method and date | Related finding |
| --- | --- | --- | --- | --- | --- | --- | --- |
| TR-001 | `workspace/10_activities.md`, `## Design principles` | Activities work without a required learner device, app, named service, connectivity, or real funds and include an equivalent low-tech route when needed. | A default simulation or no-device activity route. | Activity 006 asks learners to use Lightning wallets, ideally their own, to install or restore them, and to pass sats. | `conflict` | Full source read, 2026-09-30 | PUB-003; ACT-033 |
| TR-002 | `workspace/06_plan.md`, `## Module 4: Bitcoin in Your Community` and DEC-06 | Lightning explanation is required; setup, invoices, and payments are locally selected practice. | No activity presents Lightning setup or use as a universal Diploma requirement. | Activity 006 reads as a whole-class live-wallet relay and only retracts that requirement in a later note. | `conflict` | Full source read, 2026-09-30 | PUB-003; ACT-033 |
| TR-003 | `workspace/10_activities.md`, `## Design principles` | Technical, banking, and current-tool claims are accurate, bounded, and dated where volatile. | Simplified models name their limit and retain factual distinctions. | Activities 003, 004, 007, 019, and 020 contain inaccurate or unsupported technical or banking claims. | `missing` | Source read; targeted primary-source check, 2026-09-30 | PUB-004; PUB-005; ACT-032; ACT-034 |
| TR-004 | `workspace/10_activities.md`, `## Assessment boundary` | Activity assessment links remain formative unless the approved protocol, individual evidence, and record are used. | Clear conditional assessment language. | All 14 files with assessment links state that the activity is formative unless the approved protocol and individual evidence are used. | `implemented` | Search and contextual read, 2026-09-30 | none |
| TR-005 | `workspace/10_activities.md`, `## Assessment boundary` | Recovery teaching uses prepared, private, no-secret materials. | A safe classroom procedure with no real learner secret or funds. | Activity 018 now uses a nonfunctional or empty training route, placeholder recovery cards, and non-payable examples before its procedure. | `implemented` | Contextual read, 2026-09-30 | ACT-022 remains completed |
| TR-006 | `workspace/10_activities.md`, `## Design principles`; `workspace/18_horizon.md`, `### Activity-library completion after publication` | The library may retain incomplete optional fields after publication, but material defects remain actionable. | No false claim that all empty optional fields are blockers. | Empty metadata and video-discussion fields remain, as expressly accepted by the release decision. This review did not reopen that settled decision. | `intentionally deferred` | Contextual read, 2026-09-30 | ACT-023 remains completed |
| TR-007 | `review_alignment.md`, `## Prompt 11: Reconcile findings and validate the result` | Retained public destinations are recorded in the applicable canonical link register and tested before release. | Activities’ 17 external-link files are inventoried and checked. | The registers list guide links but do not inventory the activity sources; the activity destinations were not live-tested in this run. | `missing` | Register and source-link inventory, 2026-09-30 | ACT-009 |
| TR-008 | `workspace/16_spec.md`, `## Current Boundaries` | Teaching remains educational, non-advisory, and does not press adoption. | Balanced, choice-preserving activity language. | Activities 001, 002, 017, 018, and 028 use bounded, choice-preserving framing. | `implemented` | Contextual read, 2026-09-30 | none |

## Findings created or updated

| ID | Status | Severity | Release impact | Summary | Evidence | Run follow-up |
| --- | --- | --- | --- | --- | --- | --- |
| PUB-003 | `open` | `high` | `publication blocker` | The Lightning relay makes a device, wallet, and real-sats route appear mandatory despite the approved optional and low-tech boundary. | Activity 006, `## Materials` through `# Notes`. | Complete ACT-033 and verify the deployed page. |
| PUB-004 | `open` | `high` | `publication blocker` | The fractional-reserve banking activity presents a stylized multiplier as current banking and makes universal risk claims. | Activity 004, `# Description`, `## Steps 2–6`, and `## Key Points`. | Complete ACT-034 with qualified banking review. |
| PUB-005 | `open` | `high` | `publication blocker` | Four technical activities misstate or over-simplify foundational Bitcoin concepts. | Activities 003, 007, 019, and 020. | Complete ACT-032 with technical review. |
| ACT-009 | `needs-verification` | `high` | `publication blocker` | The link registers omit activity-source destinations and no live link check was run. | 17 activity files contain external destinations; neither register records their source locations. | Extend the registers and run the Sanity check. |

## Verification requests for an internet-connected AI agent

### VER-001: Bitcoin technical-model claims

```text
You are an internet-connected verification agent. Verify the technical statements in Activities 003, 007, 019, and 020 without changing project files.

Item to verify: whether Bitcoin uses a “4 MB block limit”; whether every Bitcoin transaction has sender, recipient, miner, and node-operator roles; whether recipients approve transactions; whether miners enforce all transaction criteria; and whether proof of work requires a block to be below “the difficulty adjustment.”
Intended purpose in the curriculum: beginner explanation of transaction validation, mining, nodes, block capacity, and proof of work.
Required source standard: Bitcoin Core documentation, bitcoin.org white paper, or other primary Bitcoin technical documentation.
Check date: 2026-09-30.
Acceptance condition: corrected wording distinguishes block weight from a simple MB limit, node validation from miner block construction, optional recipient checks from consensus validation, and the target threshold from difficulty adjustment.

Return: pass, fail, or uncertain; source title; direct URL; relevant result or a short copyright-compliant quotation; check date; and a concise explanation of whether the claim matches its intended purpose. Identify redirects, access restrictions, stale information, or uncertainty. Do not infer approval and do not edit files.
```

### VER-002: Fractional-reserve banking model

```text
You are an internet-connected verification agent. Verify the banking explanation in Activity 004 without changing project files.

Item to verify: whether a fixed 10% reserve ratio mechanically governs modern bank lending and money creation; whether sequentially redepositing each loan accurately represents deposits, loans, reserves, and money supply; and whether smaller reserves necessarily create more bank-run or default risk.
Intended purpose in the curriculum: a beginner-safe, non-advisory explanation of banking and money.
Required source standard: current central-bank or prudential-regulator material, supplemented by a qualified banking or economics source where needed.
Check date: 2026-09-30.
Acceptance condition: the activity can be labelled as a historical or deliberately stylized model, and every retained current or causal claim is accurate, jurisdiction-qualified, and sourced.

Return: pass, fail, or uncertain; source title; direct URL; relevant result or a short copyright-compliant quotation; check date; and a concise explanation of whether the claim matches its intended purpose. Identify redirects, access restrictions, stale information, or uncertainty. Do not infer approval and do not edit files.
```

### Returned verification evidence

| VER-ID | Outcome | Source title and direct URL | Check date | Evidence summary | Related finding or matrix row |
| --- | --- | --- | --- | --- |
| VER-001 | fail | [Bitcoin Developer Guide: Block Chain](https://developer.bitcoin.org/devguide/block_chain.html) | 2026-09-30 | The guide defines proof of work as a block-header hash at or below a target threshold and describes adjustment every 2,016 blocks. This does not support Activity 020’s “below the difficulty adjustment” wording. It also supports distinguishing validation rules from a classroom role-play. | PUB-005; TR-003 |
| VER-002 | fail | [Federal Reserve: Reserve Requirements](https://www.federalreserve.gov/monetarypolicy/reservereq.htm), [Federal Reserve: The Money Multiplier, Fact or Fiction?](https://www.federalreserve.gov/pubs/feds/2010/201041/index.html) | 2026-09-30 | The Federal Reserve reports a zero-percent US reserve requirement since 2020. Its research says the simple multiplier’s assumed direct link between reserves, money, and lending is not a relevant current explanation. The activity needs a bounded, jurisdiction-qualified rewrite. | PUB-004; TR-003 |

## Editor-discretion judgements

| Subject | Editor decision | Rationale and internal evidence | Date | Related finding or matrix row |
| --- | --- | --- | --- | --- |
| Activities 001, 002, and 018 | No regression found. | The 30 September factual and wallet-safety corrections are present in the current source. | 2026-09-30 | TR-005; TR-008 |
| Empty optional activity fields | Not a new finding. | `workspace/18_horizon.md` explicitly records their post-publication completion and ACT-023 is complete. | 2026-09-30 | TR-006 |

## Checks completed

- [x] Authority, activity scope, and the complete activity-folder inventory checked.
- [x] Every in-scope Markdown file read; relevant architecture, activity, competency, assessment, certification, and specification authorities checked.
- [x] Activity assessment links, safety language, external-link inventory, and local relative-link targets checked.
- [x] Targeted primary-source checks completed for the technical and banking findings.
- [x] Findings routed to `review_todo.md`.

## Checks not performed or deferred

- Every external activity destination was not live-tested. The registers do not yet inventory the activity links, and deployed Sanity pages were unavailable. This remains ACT-009.
- Rendering, phone, screen-reader, translation, educator-use, and learner testing were not performed. Markdown hierarchy and rendering remediation remain ACT-035.
- No deployed Resources Hub page was compared with the corrected source. Confirm it during the Sanity pre-release review.

## Review report summary

Targeted alignment review completed on 2026-09-30 for all 32 files in `publish/mfb-act-26.10/`. No publication content was changed. The corrected auction, consensus, and wallet activities remain aligned, while three new high-severity publication gaps were recorded: the Lightning relay conflicts with the optional, low-tech boundary; the banking simulation presents an inaccurate current model; and four technical activities misstate foundational concepts. The activity-source external links are not in the link registers and were not fully verified. The fixed-point synchronization check was not applicable because this was review-only and no source content changed. Next action: complete ACT-032–ACT-035, extend and test the activity link inventory under ACT-009, then verify deployed Resources Hub pages. This run record is not a source of truth.
