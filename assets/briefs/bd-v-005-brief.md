# BD-V-005 design brief

## Source snapshot

- Source capture: complete asset-index record preserved below from `workspace/mfb-bd-workspace/08_assets.md`.
- Brief status: deferred.
- Asset status: POSTPONED — do not produce, place, or include in the 2026.10 Diploma release.
- Source captured: 2026-10-16; brief revision 2026-10-16.
- This brief is the primary authority for later JSON-reference creation after the postponement is lifted and the documented decisions are resolved. Consult the asset index only to resolve a documented incompleteness or conflict.

```markdown
| `BD-V-005` | POSTPONED | AI | Supporting | 253 |  | Lets learners compare each Bitcoin Diploma module's role, guiding question, and promise at a glance. | Four-module reference table; full width. | Preserve the columns `Module`, `Role`, `Guiding question`, and `Learner promise`. Use four clearly separated, editable rows for Problem: Understanding Money, Solution: How Bitcoin Works, Action: Using Bitcoin Safely, and Connect: Bitcoin in Your Community. Mark Modules 1–3 as shared learning and Module 4 as educator-curated, locally relevant, and required for Bitcoin Diploma completion. | Deferred for 2026.10; retain this production record. |
```

## Asset definition

- Type: POSTPONED in the register. Table (Replacement), intended future form; the register Type remains POSTPONED.
- Priority: Supporting
- Suggested by: AI
- Educational purpose: Lets learners compare each Bitcoin Diploma module's role, guiding question, and promise at a glance.
- Required format: Four-module reference table; full width. Future reference canvas: landscape 16:9, 960 × 540; no image is created in this task.
- Required construction, elements, relationships, reading order, and qualifications: Preserve the columns `Module`, `Role`, `Guiding question`, and `Learner promise`. Use four clearly separated, editable rows for Problem: Understanding Money, Solution: How Bitcoin Works, Action: Using Bitcoin Safely, and Connect: Bitcoin in Your Community. Mark Modules 1–3 as shared learning and Module 4 as educator-curated, locally relevant, and required for Bitcoin Diploma completion.
- Register note: Deferred for 2026.10; retain this production record.
- Production restriction: this is a deferred specification, not release approval. Retain all current guide content and anchors; no downstream production or placement is authorized.

## Placement anchor

- Student Guide: exact heading `### How the learning path is organized`; retained source anchor:

```markdown
<!-- VISUAL: BD-V-005
TYPE: POSTPONED
ALT: Accessible four-module reference table showing role, guiding question, and learner outcome.
ASSET: assets/briefs/bd-v-005-brief.md
STATUS: POSTPONED — retain this anchor; do not include this asset in the 2026.10 Diploma release.
-->
```

- Educator Guide: not applicable; no placement listed and no current marker.

The heading and nearby text above are the placement authority; register line numbers are finders only. These are retained deferred anchors, not instructions to replace them now.

## Detailed visual specification

### Teaching point and learner outcome

Lets learners compare each Bitcoin Diploma module's role, guiding question, and promise at a glance. The learner can compare each module’s role, guiding question, and intended learning outcome while recognizing all four modules as required.

### Composition and reading order

Pattern: Comparison table. Layout skeleton: `teaching-page`, within the guide figure region at the width stated above. Future reference orientation: landscape 16:9, 960 × 540. Preserve reading order and learner-readable type when adapting to the final print region; do not shrink a dense table to fit an arbitrary height.

Use a full-width, four-row reference table. Preserve the register columns Module, Role, Guiding question, and Learner promise in that order. Read the header left to right and then the four module rows top to bottom. Keep each module title with its Problem, Solution, Action, or Connect role. Add a shared-learning qualifier for Modules 1–3 and an educator-curated, locally relevant, required qualifier for Module 4. Keep qualifiers outside the data cells if needed to preserve readable cells. The existing guide table stays in place while the asset is postponed.

### Content and live text

Use the exact module titles, roles, questions, and learner statements in the current source table below. Keep each field live. Preserve their limited beginner scope; do not expand a learner outcome into a guarantee of expertise or independent management of significant funds. The register heading Learner promise and the current guide heading What you will practice require reconciliation before a future replacement is approved.

Current Student Guide source table (capture preserved verbatim; all text and values stay live in a future implementation):

```markdown
| Module | Role | Guiding question | What you will practice |
| --- | --- | --- | --- |
| **Module 1: Understanding Money** | **Problem** | How do monetary systems work and change? | Explain the money **questions** Bitcoin responds to. |
| **Module 2: How Bitcoin Works** | **Solution** | Why was Bitcoin created, and how does it respond? | You can explain Bitcoin's **purpose** and key properties. |
| **Module 3: Using Bitcoin Safely** | **Action** | How do I take responsibility for using and securing Bitcoin? | You can explain beginner **[custody](https://programs.myfirstbitcoin.org/lexicon/en/#custody) and safety** concepts and act safely in supported practice. |
| **Module 4: Bitcoin in Your Community** | **Connect** | How do the problem, solution, and safe action connect to this community? | You can connect the course learning to a local need, alternative, safe task, and responsible next step. |
```

All learner-facing titles, labels, cells, values, qualifiers, and warnings must remain editable and translation-ready. Source table links identify terminology references; retain their meaning and do not render Markdown syntax as artwork. No invented final copy or completed local findings are authorized.

In a later SVG/PNG reference, keep a solid white background and leave copy areas clear: no visible letters, numerals, punctuation, placeholder text, or dummy text lines. Keep all required live copy in the brief and later JSON for editable implementation. A text-free reference is not an accessible or publishable substitute for the final labeled asset.

### Accessibility and production handoff

- Alt text: Four Diploma modules are compared by role, guiding question, and learner outcome. The shared learning leads into required, educator-curated local Connect learning.
- Editable source: retain separate geometry and live text groups. For a future table, preserve semantic headers, row associations, and editable cells; an image alone cannot replace the accessible text equivalent. Translation must preserve reading order and all qualifications.
- Reference image output: only after a later release decision and resolution of the documented issues, provide `assets/reference/bd-v-005-ref.svg` and a matching `assets/reference/bd-v-005-ref.png`; never a JPG reference. Do not create either file, a JSON record, or a package while the asset remains POSTPONED.
- Use in colour, grayscale, print, and on a phone: verify the specific relationships and row/stage order above without color; use positional and line/shape distinctions. Keep learner-facing print text at least 12pt. At phone width, preserve each label with its related content and allow wrapping or a clearly ordered stacked equivalent rather than illegible shrink-to-fit. Check contrast, connector continuity, numeric alignment where applicable, and a complete text alternative before any future release.

## Required visual treatment

Selected Tier 3 pattern: Comparison table. Selected layout: `teaching-page`; use the stated half-page or full-width region without decorative shared chrome.

Use primary purple `#422C70` for structure and headings, deep purple `#2B1C58` for strong detail, white `#FFFFFF` for reference backgrounds, paper `#F6F6F8` for quiet internal surfaces, cool divider `#D8D8E7` for separators, and body neutral `#25252B` for live text. Orange `#F7941F` marks at most one teaching emphasis and never a dominant field or a safety ranking. Purple/white/paper lead; color never carries meaning alone.

Use live IBM Plex Sans, 400 body and 500 headings/labels, with at most two weights; learner-facing print text is at least 12pt. Keep copy short, literal, left aligned, upright, and translatable. Use flat geometry, restrained monoline outlines, butt caps, and miter joins. Any meaningful structural cut or slant uses exactly 13°; contents remain upright. Do not add a frame or slant merely as decoration. White/paper table ground, purple heading/section label, cool-gray hairlines; left-aligned prose and right-aligned comparable numbers. Keep cells short, preserve source row order, and allow translation wrapping. No heavy borders, colored rating cells, or decorative-icon overload.

Use diagram primitives or the specified record structure; do not add decorative icons or an unapproved icon library.

No people are required. Do not add cast members, portraits, or character props. The character bible applies only if a later reviewed scope change makes people instructionally necessary.

## Safety, exclusions, and qualifications

- Do not replace the current guide table in this task, convert an outcome into a certification claim, or present Module 4 as an optional add-on.
- Preserve the original purpose, format, priority, description, and guide anchors. Existing tables remain in the guides. A complete deferred brief does not authorize a generated visual or 2026.10 inclusion.
- No financial, legal, tax, accounting, compliance, or investment advice; no provider recommendations, guaranteed safety, returns, adoption, or universal local conclusions. Any later local facts require approved, dated source material.
- No real secrets, private keys, seed words, learner identities, personal/payment data, live balances, invoices, or payable destinations. These assets require no functional payment screen or QR. Any later approved fictional payment screen or QR must be nonfunctional and carry live `SAMPLE — DO NOT PAY` wording.
- Keep protocol, wallet, service, user, educator, node, and miner roles distinct when mentioned. Never show bitcoin stored in a wallet, miners making rules, or a single controller of Bitcoin.
- No restricted-pilot app download link, QR panel, installation instruction, or implication that a diagram or self-report certifies competency.
- No crypto hype, gold Bitcoin coins, generic blockchain imagery, corporate-cartoon proportions, gradients, glossy/3D effects, shadows, decorative clutter, third-party icon substitution, or redrawn official MFB marks.

## Source conflicts or unresolved decisions

- The user explicitly requested briefs for POSTPONED assets on 2026-10-16, overriding the brief-skip instruction in assets/prompts/prompt-00-brief.md for this task. This authorizes these brief files only. The asset remains POSTPONED; JSON, image generation, upload, guide replacement, and 2026.10 inclusion remain deferred.
- The register requests Learner promise, while the current Student Guide uses What you will practice. The placement table also names an older heading, “How the 4-module learning path is organized”; the current exact heading is “How the learning path is organized”. Preserve both source records and use the captured current marker as the location authority. Editorial review must approve the future column heading and replacement copy.

## Completion criteria

- The filename, H1, complete source row, guide-marker ID, and production-log path all identify BD-V-005.
- Four rows and all four specified columns are present; questions and learner statements match the source table; Module 4 remains required.
- Preserve the existing guide table and marker; this brief does not replace either.
- Use the specified pattern, teaching-page region, purple-led palette, flat 13° geometry where relevant, live text, and instructional alt text.
- Future accessibility review must verify grayscale, print at 12pt or larger, phone reading order, contrast, and complete source-supported content; saving this brief does not claim those visual checks have occurred.
- Carry every source gap or conflict into later review; do not silently complete truncated descriptions, invent a local fact, or remove a safety qualification.
- Keep status deferred and the asset POSTPONED. No JSON, SVG/PNG, VM upload, MG package, Sanity insertion, or guide replacement is created by this brief task.
