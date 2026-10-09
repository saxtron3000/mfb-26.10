# SVG and PNG reference-image prompt

This prompt applies only to pipeline-eligible assets. Do not create SVG or PNG references for an `External Image`; it is copied from its approved external source and manually inserted into the Diploma.

## Purpose

Have Codex create one SVG reference image and its matching PNG rendering for a later editable micrographic implementation in Sanity. Their only purpose is to show the approved composition and visual direction. They are not production assets, uploads, or substitutes for editable text, diagrams, tables, QR codes, or interfaces.

## Inputs and precedence

For one asset, read:

1. `assets/briefs/bd-v-###-brief.md`
2. `assets/reference/bd-v-###-ref.json`

The brief controls instructional intent, required content, safety, exclusions, and localization. The JSON record controls the resolved composition, reading order, elements, and visual treatment. If they conflict, are incomplete, or leave a visual decision unclear, consult `workspace/08_assets.md` and follow its relevant asset entry.

Consult `assets/style/` only when the inputs or asset index require additional visual clarification. Use only the needed source: `STYLE.md` for overall visual direction; `CHARACTERS.md` and its bible for named people; and `layouts/README.md` for a specified layout pattern. Style must not override the brief or asset index.

## Generation prompt

```text
Create one SVG reference image and one matching PNG rendering for a My First Bitcoin Bitcoin Diploma micrographic.

Read the attached asset brief and JSON reference record before generating. Follow the brief for required meaning, safety, exclusions, and localization; use the JSON for the exact composition, elements, relationships, reading order, and visual treatment. If they conflict or are incomplete, consult the relevant entry in workspace/08_assets.md. Use assets/style/ only when needed to clarify visual direction.

Create exactly one SVG at the aspect ratio and orientation in the JSON, with a solid white (`#FFFFFF`) background. Use real SVG geometry, paths, and shapes; do not embed a raster image in the SVG. Render that exact SVG as one matching low-resolution PNG. The SVG and PNG are private visual references for a later editable micrographic, not production or Sanity assets. Do not create a JPG.

Show only the required visual elements and relationships. Preserve required role distinctions, counts, qualifications, and trade-offs. Do not add decorative people, props, scenery, labels, arrows, connectors, frames, logos, QR codes, URLs, data, or other elements unless the brief or JSON explicitly requires them.

Render no text, letters, numbers, punctuation, or placeholder text. All copy, data, labels, and warnings will be added as editable, translatable content during micrographic production.

Use the approved MFB visual direction: flat, print-safe vector-style artwork; hard geometric structure; restrained monoline outlines; clear negative space; purple-led palette; cool-gray neutrals; and small, controlled orange emphasis. Use the 13-degree parallelogram language only where it supports the composition. No gradients, shadows, texture, glow, 3D, photorealism, generic crypto imagery, trading hype, or corporate-Memphis styling. When people are required, use the named approved characters and their established identity.

Never show a real or plausible seed phrase, private key, payable address, learner identity, learner balance, personal data, payment QR code, or unverified factual data. Do not imply investment returns, risk-free self-custody, inevitable adoption, or a universal legal or local conclusion.
```

## Save and log

Save the reviewed files as `assets/reference/bd-v-###-ref.svg` and `assets/reference/bd-v-###-ref.png`, using the lowercase three-digit asset ID. The PNG must be rendered from the saved SVG. Do not create a JPG, a second preview, a conformance report, a per-asset prompt, or any production/Sanity file.

After confirming that both files exist, the SVG contains no embedded raster image, the PNG matches the SVG, both have a white background, and they match the brief and JSON without prohibited visible content:

1. Change that asset’s `SVG/PNG reference` cell in `assets/assets-list.md` to `Created — \`assets/reference/bd-v-###-ref.svg\`; \`assets/reference/bd-v-###-ref.png\``.
2. Update the SVG/PNG-reference total so it equals the number of created SVG/PNG-reference rows.

If generation is blocked, do not mark the SVG/PNG reference as created. Record `Blocked — [short reason]` in that asset’s SVG/PNG-reference cell and leave the total unchanged.

If the brief or JSON is incomplete or leaves a required visual decision unclear, first consult the relevant entry in `workspace/08_assets.md`. If it remains blocked after that consultation, do not generate a best-guess image; record it as blocked using the rule above.
