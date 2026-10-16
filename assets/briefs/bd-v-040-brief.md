# BD-V-040 design brief

## Source snapshot

- Source capture: complete asset-index record preserved below from `workspace/mfb-bd-workspace/08_assets.md`.
- Brief status: deferred.
- Asset status: POSTPONED — do not produce, place, or include in the 2026.10 Diploma release.
- Source captured: 2026-10-16; brief revision 2026-10-16.
- This brief is the primary authority for later JSON-reference creation after the postponement is lifted and the documented decisions are resolved. Consult the asset index only to resolve a documented incompleteness or conflict.

```markdown
| `BD-V-040` | POSTPONED | AI | Supporting | 1096 |  | Makes key control, recovery, and failure points comparable without moralising either model. | Custody comparison table; full width. | Preserve the current rows `Who holds the keys?`, `Who handles recovery?`, and `Main trade-off`, with the custodial and self-custodial explanations. Use neutral icons and editable text. Do not add a recommendation badge or treat either model as risk free. | Deferred for 2026.10; retain this production record. |
```

## Asset definition

- Type: POSTPONED in the register. Table (Replacement), intended future form; the register Type remains POSTPONED.
- Priority: Supporting
- Suggested by: AI
- Educational purpose: Makes key control, recovery, and failure points comparable without moralising either model.
- Required format: Custody comparison table; full width. Future reference canvas: landscape 16:9, 960 × 540; no image is created in this task.
- Required construction, elements, relationships, reading order, and qualifications: Preserve the current rows `Who holds the keys?`, `Who handles recovery?`, and `Main trade-off`, with the custodial and self-custodial explanations. Use neutral icons and editable text. Do not add a recommendation badge or treat either model as risk free.
- Register note: Deferred for 2026.10; retain this production record.
- Production restriction: this is a deferred specification, not release approval. Retain all current guide content and anchors; no downstream production or placement is authorized.

## Placement anchor

- Student Guide: exact heading `### Custodial and non-custodial use`; retained source anchor:

```markdown
<!-- VISUAL: BD-V-040
TYPE: POSTPONED
ALT: Comparison of custodial and self-custodial use by key control, recovery, and trade-offs.
ASSET: assets/briefs/bd-v-040-brief.md
STATUS: POSTPONED — retain this anchor; do not include this asset in the 2026.10 Diploma release.
-->
```

- Educator Guide: not applicable; no placement listed and no current marker.

The heading and nearby text above are the placement authority; register line numbers are finders only. These are retained deferred anchors, not instructions to replace them now.

## Detailed visual specification

### Teaching point and learner outcome

Makes key control, recovery, and failure points comparable without moralising either model. The learner can identify who holds keys and handles recovery in custodial and self-custodial use and name the different dependencies and responsibilities.

### Composition and reading order

Pattern: Comparison pair in a table. Layout skeleton: `teaching-page`, within the guide figure region at the width stated above. Future reference orientation: landscape 16:9, 960 × 540. Preserve reading order and learner-readable type when adapting to the final print region; do not shrink a dense table to fit an arbitrary height.

Use a full-width three-column comparison: Question, Custodial use, Self-custodial use. Preserve the three current rows and compare across each row before proceeding down. Keep the two arrangements equally weighted. Small first-party key/recovery cues support the text without implying one model is morally better or automatically safe. Leave the guide table in place during postponement.

### Content and live text

Use the exact current source table below. Preserve Usually the service through an account process for custodial recovery; do not change usually into always. Keep provider dependence beside familiar support and backup/error responsibility beside direct control. Add a live qualification that custody is not always obvious from the interface and neither model is risk free.

Current Student Guide source table (capture preserved verbatim; all text and values stay live in a future implementation):

```markdown
| Question | Custodial use | Self-custodial use |
| --- | --- | --- |
| Who holds the keys? | The service | The user |
| Who handles recovery? | Usually the service through an account process | The user through a backup process |
| Main [trade-off](https://programs.myfirstbitcoin.org/lexicon/en/#trade-off) | Familiar support, with provider dependence | Direct control, with backup and error responsibility |
```

All learner-facing titles, labels, cells, values, qualifiers, and warnings must remain editable and translation-ready. Source table links identify terminology references; retain their meaning and do not render Markdown syntax as artwork. No invented final copy or completed local findings are authorized.

In a later SVG/PNG reference, keep a solid white background and leave copy areas clear: no visible letters, numerals, punctuation, placeholder text, or dummy text lines. Keep all required live copy in the brief and later JSON for editable implementation. A text-free reference is not an accessible or publishable substitute for the final labeled asset.

### Accessibility and production handoff

- Alt text: Custodial and self-custodial use differ in who holds keys, handles recovery, and bears dependencies or backup responsibility; neither arrangement is risk free.
- Editable source: retain separate geometry and live text groups. For a future table, preserve semantic headers, row associations, and editable cells; an image alone cannot replace the accessible text equivalent. Translation must preserve reading order and all qualifications.
- Reference image output: only after a later release decision and resolution of the documented issues, provide `assets/reference/bd-v-040-ref.svg` and a matching `assets/reference/bd-v-040-ref.png`; never a JPG reference. Do not create either file, a JSON record, or a package while the asset remains POSTPONED.
- Use in colour, grayscale, print, and on a phone: verify the specific relationships and row/stage order above without color; use positional and line/shape distinctions. Keep learner-facing print text at least 12pt. At phone width, preserve each label with its related content and allow wrapping or a clearly ordered stacked equivalent rather than illegible shrink-to-fit. Check contrast, connector continuity, numeric alignment where applicable, and a complete text alternative before any future release.

## Required visual treatment

Selected Tier 3 pattern: Comparison pair in a table. Selected layout: `teaching-page`; use the stated half-page or full-width region without decorative shared chrome.

Use primary purple `#422C70` for structure and headings, deep purple `#2B1C58` for strong detail, white `#FFFFFF` for reference backgrounds, paper `#F6F6F8` for quiet internal surfaces, cool divider `#D8D8E7` for separators, and body neutral `#25252B` for live text. Orange `#F7941F` marks at most one teaching emphasis and never a dominant field or a safety ranking. Purple/white/paper lead; color never carries meaning alone.

Use live IBM Plex Sans, 400 body and 500 headings/labels, with at most two weights; learner-facing print text is at least 12pt. Keep copy short, literal, left aligned, upright, and translatable. Use flat geometry, restrained monoline outlines, butt caps, and miter joins. Any meaningful structural cut or slant uses exactly 13°; contents remain upright. Do not add a frame or slant merely as decoration. White/paper table ground, purple heading/section label, cool-gray hairlines; left-aligned prose and right-aligned comparable numbers. Keep cells short, preserve source row order, and allow translation wrapping. No heavy borders, colored rating cells, or decorative-icon overload.

Use only approved first-party MFB icons: 24 × 24u canvas, 20 × 20u live area, 2u padding; use the 2.5u print cut, butt caps, miter joins, and hard corners. Icon supply remains an unresolved handoff dependency.

No people are required. Do not add cast members, portraits, or character props. The character bible applies only if a later reviewed scope change makes people instructionally necessary.

## Safety, exclusions, and qualifications

- A custodial balance is a service promise, not proof of independently controlled bitcoin. Self-custody still has software, hardware, network, backup, and error risks. Do not show bitcoin stored inside a wallet or reveal any keys or recovery words.
- Preserve the original purpose, format, priority, description, and guide anchors. Existing tables remain in the guides. A complete deferred brief does not authorize a generated visual or 2026.10 inclusion.
- No financial, legal, tax, accounting, compliance, or investment advice; no provider recommendations, guaranteed safety, returns, adoption, or universal local conclusions. Any later local facts require approved, dated source material.
- No real secrets, private keys, seed words, learner identities, personal/payment data, live balances, invoices, or payable destinations. These assets require no functional payment screen or QR. Any later approved fictional payment screen or QR must be nonfunctional and carry live `SAMPLE — DO NOT PAY` wording.
- Keep protocol, wallet, service, user, educator, node, and miner roles distinct when mentioned. Never show bitcoin stored in a wallet, miners making rules, or a single controller of Bitcoin.
- No restricted-pilot app download link, QR panel, installation instruction, or implication that a diagram or self-report certifies competency.
- No crypto hype, gold Bitcoin coins, generic blockchain imagery, corporate-cartoon proportions, gradients, glossy/3D effects, shadows, decorative clutter, third-party icon substitution, or redrawn official MFB marks.

## Source conflicts or unresolved decisions

- The user explicitly requested briefs for POSTPONED assets on 2026-10-16, overriding the brief-skip instruction in assets/prompts/prompt-00-brief.md for this task. This authorizes these brief files only. The asset remains POSTPONED; JSON, image generation, upload, guide replacement, and 2026.10 inclusion remain deferred.
- The design requires first-party MFB icon cues. No reusable first-party icon set is supplied in assets/style/. Before later production, supply approved icons or obtain a reviewed change to those cues; do not substitute a third-party set or redraw official marks. This does not prevent saving the deferred brief.

## Completion criteria

- The filename, H1, complete source row, guide-marker ID, and production-log path all identify BD-V-040.
- Three question rows retain their exact distinctions, recovery qualifications, and balanced trade-offs without a recommended model badge.
- Preserve the existing guide table and marker; this brief does not replace either.
- Use the specified pattern, teaching-page region, purple-led palette, flat 13° geometry where relevant, live text, and instructional alt text.
- Future accessibility review must verify grayscale, print at 12pt or larger, phone reading order, contrast, and complete source-supported content; saving this brief does not claim those visual checks have occurred.
- Carry every source gap or conflict into later review; do not silently complete truncated descriptions, invent a local fact, or remove a safety qualification.
- Keep status deferred and the asset POSTPONED. No JSON, SVG/PNG, VM upload, MG package, Sanity insertion, or guide replacement is created by this brief task.
