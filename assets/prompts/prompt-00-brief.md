# Bitcoin Diploma design-brief generation contract

## Canceled assets

Skip every asset whose Type or Status is `CANCELED` or `CANCELLED`. Do not create, regenerate, upload, or place any deliverable for it, and do not restore its guide anchors. Existing files are historical records only.

## Objective

Create one complete, production-ready design brief for every pipeline-eligible `BD-V-###` asset in `workspace/08_assets.md`, in ascending **numeric** asset-ID order (`001`, `002`, …). Each brief translates the approved asset-index record into a precise instruction for later JSON-reference and production work; it does not create the visual itself. Do not create a brief for an asset of type `EXTERNAL`: its approved .jpg is added directly through Sanity.

## Read first

Read these sources before writing any brief:

1. `workspace/08_assets.md` — authoritative asset register, shared rules, asset rows, placement rules, and workflow.
2. `assets/style/STYLE.md` — required visual system, palette, type, geometry, patterns, production constraints, and pre-flight checks.
3. `assets/style/CHARACTERS.md` — required cast identity and permitted people/prop usage, when people are relevant.
4. `assets/style/layouts/README.md` — required layout skeleton selection and surface constraints.
5. The current Student and Educator Guide files named in `workspace/08_assets.md` — use these only to capture the exact heading and nearby placement-marker text for every listed placement.
6. `assets/assets-list.md` — existing production log and the required location to record each successfully created brief.

Treat `workspace/08_assets.md` as the instructional authority. Style references govern visual treatment and must not change the asset’s approved purpose, required content, safety limits, or placement. If sources conflict, preserve the asset-index requirement, document the conflict in the brief, and do not invent a resolution that changes the curriculum.

## Scope and ordering

1. Extract every pipeline-eligible asset row whose ID exactly matches `BD-V-###` from the visual index. Ignore section-heading rows, examples, and rows whose Type is `EXTERNAL`.
2. Sort IDs by their three-digit number, not by visual-index position, guide section, filename order, or priority.
3. Process one asset completely before beginning the next. Re-run safely: inspect the destination first and update an existing brief rather than creating a duplicate.
4. Write each result to `assets/briefs/bd-v-###-brief.md`, using the lowercase, zero-padded ID. Create no per-asset folders or prompts.
5. A conditional, supporting, or blocked pipeline-eligible asset still needs a brief. State its status and its exact production restriction; never silently omit it. An asset of type `EXTERNAL` is not pipeline-eligible and must have no brief.

## Required brief content

Use the following Markdown structure exactly. Replace bracketed guidance with supported content; do not leave placeholders, except inside a clearly marked unresolved issue.

````markdown
# BD-V-### design brief

## Source snapshot

- Source capture: complete asset-index record preserved below.
- Brief status: [production-ready | blocked].
- This brief is the primary authority for later JSON-reference creation. Consult the asset index only to resolve a documented incompleteness or conflict.

```markdown
[the complete, unaltered Markdown table row from the visual index]
```

## Asset definition

- Type: … (use `Table (Standalone)` or `Table (Replacement)` for table assets)
- Priority: …
- Suggested by: …
- Educational purpose: …
- Required format: …
- Required construction, elements, relationships, reading order, and qualifications: …
- Register note: …

## Placement anchor

- Student Guide: [exact heading; nearby marker or source text; otherwise not applicable].
- Educator Guide: [exact heading; nearby marker or source text; otherwise not applicable].

The heading and nearby text above are the placement authority; register line numbers are finders only.

## Detailed visual specification

### Teaching point and learner outcome

[One concise teaching point, followed by the specific understanding, comparison, decision, or safe action the learner should gain.]

### Composition and reading order

[State orientation/format, the selected reusable graphic pattern, selected layout skeleton, hierarchy, named elements, their positions and relationships, and an unambiguous reading order. Preserve every required element and qualification from the register.]

### Content and live text

[List required labels, values, examples, callouts, and qualifiers. Identify every label as editable and translation-ready. Specify fictional/sample treatment where required. Do not invent final copy that the register does not support.]

### Accessibility and production handoff

- Alt text: [a concise description that communicates the instructional meaning].
- Editable source: [state the live-label/editable-source requirement appropriate to the type].
- Reference image output: [Codex must provide `assets/reference/bd-v-###-ref.svg` and a matching `assets/reference/bd-v-###-ref.png`; do not request or accept a JPG reference].
- Use in colour, grayscale, print, and on a phone: [specific checks for this asset].

## Required visual treatment

[Apply only the relevant requirements from `assets/style/`. Name the chosen pattern and layout, palette roles, typography/copy treatment, 13° geometry and connector/icon rules, emphasis treatment, table/data rules when applicable, and character IDs/poses/props when people appear. Use the character bible only when people are required. Include no decorative styling that does not teach the stated point.]

## Safety, exclusions, and qualifications

- [All asset-index and shared restrictions that apply, including role distinctions, factual/financial boundaries, fictional-data and QR/interface requirements.]
- [Explicitly state every asset-specific prohibition and every unresolved condition that blocks production.]

## Source conflicts or unresolved decisions

- [None, or the exact source conflict/ambiguity, its effect, and what review/approval is needed.]

## Completion criteria

- [A concise, asset-specific checklist that proves purpose, required content/relationships, placement, style, safety, live text, alt text, grayscale/print/phone usability, and any unresolved production conditions have been met.]
````

## Style application rules

Apply the style guide concretely, rather than inserting a generic “follow style” sentence:

- Select the existing Tier 3 pattern that matches the learning need (for example, comparison pair, layer stack, timeline, process flow, callout, or table), and select the appropriate layout skeleton.
- Use the purple/white-or-paper visual hierarchy, cool-gray dividers, and only controlled orange emphasis. Preserve the 13° structural slant; keep labels and people upright.
- Require flat, print-safe, editable artwork; clear negative space; live, short, translatable labels; color-independent distinctions; and at least 12pt learner-facing type for print.
- For diagrams, use direct labels, straight or right-angle connectors, open-chevron arrows, filled node dots, and hatch in addition to colour where multiple series must survive grayscale.
- For tables, require a paper ground, purple heading/section label, cool-gray hairlines, short cells, left-aligned prose, right-aligned comparable numbers, and no decorative-icon overload.
- When people appear, select only necessary named characters and valid actions from `CHARACTERS.md`; preserve the fixed cast and keep the older learner capable and active.
- Prohibit crypto hype, generic blockchain imagery, gold coins, corporate-cartoon proportions, gradients, glossy/3D effects, shadows, decorative clutter, unapproved icons, and redrawn MFB marks.

## Accuracy and safety rules

- Preserve the complete asset row verbatim in the source snapshot. Do not shorten text with an ellipsis.
- Keep protocol, wallet, service, educator, user, node, and miner roles distinct whenever relevant. Never show Bitcoin “in a wallet,” miners making rules, or a single controller.
- Do not add financial, legal, tax, accounting, compliance, or investment advice; recommendations; claims of guaranteed safety/returns/adoption; current local facts without approved, dated source material; real secrets, identities, payment data, or balances.
- Mark any fictional interface, payment screen, or QR example `SAMPLE — DO NOT PAY`. Never create or imply a payable destination.
- Use the official Creative Commons or MFB marks only when the index requires them; do not redraw, recolour, or distort official marks.
- Preserve all conditional, approval, privacy, correction, withdrawal, issuer, or local-context requirements exactly. A brief can be complete while production remains blocked by unresolved inputs.

## Logging and validation

After writing and reviewing each brief:

1. Verify the filename, H1 ID, source-row ID, and asset-list row match exactly.
2. Update that asset’s `Brief` cell in `assets/assets-list.md` to `Created — \`assets/briefs/bd-v-###-brief.md\``. Replace only the brief-status text; preserve the row’s other workflow columns.
3. Recalculate the `Design briefs: N created` total to equal the number of asset-list rows marked created with an existing matching brief file. Do not claim a file is created until it exists and passes the completion criteria.
4. At batch end, confirm that every pipeline-eligible indexed ID has exactly one matching brief, there are no unlogged newly created briefs, the log paths exist, and the files were processed in numeric order. Report EXTERNAL assets separately as direct JPG uploads through Sanity. Report unresolved source decisions as production blockers under each asset’s original type.

Do not modify `workspace/08_assets.md`, guide content, style sources, JSON references, generated images, VM status, or MG-package status while performing this task. If filesystem writes are unavailable, return the completed brief(s) and the exact `assets/assets-list.md` changes required, but do not claim they were saved.
