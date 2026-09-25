# JPEG reference-image prompt

## Purpose

Create one JPEG reference image for a later editable micrographic implementation in Sanity. Its only purpose is to show the approved composition and visual direction. It is not a production asset, upload, or substitute for editable text, diagrams, tables, QR codes, or interfaces.

## Inputs and precedence

For one asset, read:

1. `assets/briefs/bd-v-###-brief.md`
2. `assets/reference/bd-v-###-ref.json`

The brief controls instructional intent, required content, safety, exclusions, and localization. The JSON record controls the resolved composition, reading order, elements, and visual treatment. If they conflict, are incomplete, or leave a visual decision unclear, consult `workspace/08_assets.md` and follow its relevant asset entry.

Consult `assets/style/` only when the inputs or asset index require additional visual clarification. Use only the needed source: `STYLE.md` for overall visual direction; `CHARACTERS.md` and its bible for named people; and `layouts/README.md` for a specified layout pattern. Style must not override the brief or asset index.

## Generation prompt

```text
Create one JPG reference image for a My First Bitcoin Bitcoin Diploma micrographic.

Read the attached asset brief and JSON reference record before generating. Follow the brief for required meaning, safety, exclusions, and localization; use the JSON for the exact composition, elements, relationships, reading order, and visual treatment. If they conflict or are incomplete, consult the relevant entry in workspace/08_assets.md. Use assets/style/ only when needed to clarify visual direction.

Create exactly one low-resolution JPG at the aspect ratio and orientation in the JSON. Use a solid white (#FFFFFF) background. The JPG is a private visual reference for a later editable micrographic, not a production or Sanity asset.

Show only the required visual elements and relationships. Preserve required role distinctions, counts, qualifications, and trade-offs. Do not add decorative people, props, scenery, labels, arrows, connectors, frames, logos, QR codes, URLs, data, or other elements unless the brief or JSON explicitly requires them.

Render no text, letters, numbers, punctuation, or placeholder text. All copy, data, labels, and warnings will be added as editable, translatable content during micrographic production.

Use the approved MFB visual direction: flat, print-safe vector-style artwork; hard geometric structure; restrained monoline outlines; clear negative space; purple-led palette; cool-gray neutrals; and small, controlled orange emphasis. Use the 13-degree parallelogram language only where it supports the composition. No gradients, shadows, texture, glow, 3D, photorealism, generic crypto imagery, trading hype, or corporate-Memphis styling. When people are required, use the named approved characters and their established identity.

Never show a real or plausible seed phrase, private key, payable address, learner identity, learner balance, personal data, payment QR code, or unverified factual data. Do not imply investment returns, risk-free self-custody, inevitable adoption, or a universal legal or local conclusion.
```

## Save and log

Save the reviewed file as `assets/reference/bd-v-###-ref.jpg`, using the lowercase three-digit asset ID. Do not create a PNG, a second preview, a conformance report, a per-asset prompt, or any production/Sanity file.

After confirming that the JPG exists, has a white background, matches the brief and JSON, and contains no prohibited visible content:

1. Change that asset’s `JPEG reference` cell in `assets/assets-list.md` to `Created — \`assets/reference/bd-v-###-ref.jpg\``.
2. Update the JPEG-reference total so it equals the number of created JPEG-reference rows.

If generation is blocked, do not mark the JPEG as created. Record `Blocked — [short reason]` in that asset’s JPEG-reference cell and leave the total unchanged.

If the brief or JSON is incomplete or leaves a required visual decision unclear, first consult the relevant entry in `workspace/08_assets.md`. If it remains blocked after that consultation, do not generate a best-guess image; record it as blocked using the rule above.
