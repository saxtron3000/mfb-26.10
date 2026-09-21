# Codex reference-image batch prompt

## Purpose

Use this prompt to run the approved Bitcoin Diploma reference-image queue in Codex in one uninterrupted run. It creates working JPG references and JSON conformance reports only. It does not create production assets, insert images into either guide, or publish to Sanity.

The batch includes 99 assets. `BD-V-070` and `BD-V-075` are deferred and must not be generated.

## Required attachments

The following source files must be available to Codex before starting:

- `/Users/saxtron3000/Documents/MFB/programs/mfb-bd-26.10/workspace/08_assets.md`
- `/Users/saxtron3000/Documents/MFB/programs/mfb-bd-26.10/workspace/22_openai-reference-image-prompt.md`
- `/Users/saxtron3000/Documents/MFB/programs/mfb-bd-26.10/workspace/24_codex-reference-image-prompt-checklist.md`
- `/Users/saxtron3000/Documents/MFB/programs/mfb-bd-26.10/workspace/26_codex-reference-image-batch-prompt.md`
- `/Users/saxtron3000/Documents/MFB/programs/mfb-bd-26.10/workspace/27_assets-style.md`

Codex must write all batch outputs inside:

```text
/Users/saxtron3000/Documents/MFB/programs/mfb-bd-26.10/assets-work/
├── references/
├── prompts/
└── rejected/
```

## Batch prompt

```text
Run the Bitcoin Diploma reference-image batch as one uninterrupted, resumable
production queue. Do not ask for confirmation between assets. Complete every
eligible item in this invocation and provide one final report.

Read these files completely before creating any image:
- /Users/saxtron3000/Documents/MFB/programs/mfb-bd-26.10/workspace/08_assets.md
- /Users/saxtron3000/Documents/MFB/programs/mfb-bd-26.10/workspace/22_openai-reference-image-prompt.md
- /Users/saxtron3000/Documents/MFB/programs/mfb-bd-26.10/workspace/24_codex-reference-image-prompt-checklist.md
- /Users/saxtron3000/Documents/MFB/programs/mfb-bd-26.10/workspace/26_codex-reference-image-batch-prompt.md
- /Users/saxtron3000/Documents/MFB/programs/mfb-bd-26.10/workspace/27_assets-style.md

The complete section 3 asset brief incorporated through the section 7
classification registry is the binding contract for each asset. The attached
27_assets-style.md is the binding visual-style authority for reference images;
if it conflicts with instructional, safety, or structural requirements, the
asset brief wins and the conflict must be recorded in unresolved.

Process every unchecked checklist item in its listed order except BD-V-070 and
BD-V-075, which are deferred. Work on one asset at a time. Do not combine
assets, skip safety constraints, invent missing information, or continue to
production code or Sanity publication.

For each asset:
1. Use its complete fenced prompt in the checklist, together with the shared
   contract in 22.
2. Generate one low-resolution JPG reference on a transparent background.
   Render no text, letters, numerals, labels, QR codes, logos, arrows,
   connectors, borders, or decorative characters. Record all required text,
   connectors, and placements in the JSON report for later editable coding.
3. Save the JPG as /Users/saxtron3000/Documents/MFB/programs/mfb-bd-26.10/assets-work/references/<asset-id-lowercase>-ref.jpg.
4. Save the JSON conformance report as
   /Users/saxtron3000/Documents/MFB/programs/mfb-bd-26.10/assets-work/references/<asset-id-lowercase>-ref.json. It must use the
   schema in 22: assetId, specVersion, canvas, placement, conformance, and
   unresolved.
5. Save the exact completed prompt, model/tool, settings, generation date,
   source-brief revision, and review note as
   /Users/saxtron3000/Documents/MFB/programs/mfb-bd-26.10/assets-work/prompts/<asset-id-lowercase>-ref.txt.
6. Review the JPG against the brief. Reject and regenerate it if its spatial
   relationship is unclear, it contains prohibited visible content, it adds
   unjustified elements, it cannot be rebuilt as editable HTML/CSS/inline SVG,
   or it breaches safety requirements.
7. Change only that checklist item from [ ] to [X] after its three files exist
   and pass review. If blocked, leave it unchecked, add the precise reason to
   the JSON unresolved array and prompt record, then proceed to the next item.

Special handling:
- BD-V-036, BD-V-078, and BD-V-080 contain [BLANK] production values. Create
  only a text-free structural composition reference. Do not generate a QR or
  imply a real payment destination. Record TODO AST-001, AST-002, or AST-003
  respectively in unresolved.
- BD-V-073 uses the approved canonical destination
  https://github.com/MyFirstBitcoin/mfb-curriculum only in later editable
  production; do not render it in the JPG.
- BD-V-074 uses the approved support-page destination
  https://donate.myfirstbitcoin.org/ only in later editable production; do not
  render it in the JPG.

Keep an internal completion log while running. At the end, report the 99
completed/deferred/blocked states, all created file paths, and unresolved
items without claiming that any reference or production asset has been
published.
```
