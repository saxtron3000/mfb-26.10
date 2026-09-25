# Asset JSON-reference contract

## Purpose

Create the first production record for one My First Bitcoin Bitcoin Diploma asset. The record is a structured visual specification that a later asset-creation step can use. It is not an asset, a publication file, a Sanity upload, or a production implementation.

## Inputs

Read these files before creating the record:

1. The relevant design brief: `Assets/briefs/bd-v-###-brief.md`. This is the complete authority for the asset's instructional content, construction, safety boundaries, placement, and visual specification.
2. This contract: `Assets/prompts/prompt-01-json.md`.
3. Consult the applicable style references in `Assets/style/` only if the brief conflicts with itself or with an approved source, or if they are needed to clarify an ambiguity the brief does not resolve:
   - `STYLE.md` for visual direction, palette, typography, geometry, and reusable graphic patterns.
   - `CHARACTERS.md` and the character bible when people appear.
   - `layouts/README.md` and the latest suitable layout study when the asset needs a layout pattern.
   - `brand-spec.md` and `brand.css` when a precise brand token is needed.

Replace `###` with the three-digit asset number. The asset ID in the brief, output filename, and record must match exactly.

## Source precedence

The brief must contain all information needed to create the JSON record. Do not browse `Assets/style/` as a normal input or to add detail not required by the brief.

Use sources in this order when consultation is necessary:

1. The relevant design brief for every record field.
2. `Assets/style/` only to resolve a conflict or clarify an ambiguity. The brief remains authoritative; do not let style references override it.

Do not read `workspace/08_assets.md` during normal JSON creation. Consult it only when the brief is incomplete or internally inconsistent, or when an approved source conflicts with the brief. Record the exact conflict or ambiguity, consulted source, and resolution in `unresolved`. Do not invent a fact, label, role, relationship, visual element, or local conclusion that the sources do not support.

## Process

1. Read the design brief and extract the asset ID, asset type, educational purpose, required content and relationships, prohibitions, placement, single teaching point, composition, reading order, editable-content needs, and open decisions.
2. Use the brief's specified visual pattern, layout, and treatment. Consult `Assets/style/` only to resolve a documented conflict or ambiguity.
3. If style consultation was necessary, apply only the specific clarification needed; do not add visual details beyond the brief.
4. Create one valid JSON record at `Assets/reference/bd-v-###-ref.json`.
5. Review the record against the design brief. When style references were consulted, also confirm that the recorded clarification faithfully resolves the documented issue. Correct it before marking it complete.
6. Only when the JSON record exists and passes every review check, update the corresponding row in `Assets/assets-list.md` from `Not created` to `Created — \`Assets/reference/bd-v-###-ref.json\``. Update the JSON-reference total so it equals the number of asset-specific JSON records marked created.

If a required source is absent or an essential design decision is unresolved, do not update `Assets/assets-list.md`. Create a record with `status` set to `blocked` and explain the exact issue in `unresolved`. Consult `workspace/08_assets.md` only if this is a brief conflict or incompleteness that it can resolve.

## Content and safety rules

- Represent only the elements and relationships required by the brief.
- Preserve qualifications, trade-offs, and role distinctions. Do not turn educational content into financial, legal, tax, accounting, compliance, or investment advice.
- Do not recommend a wallet, exchange, provider, service, or local solution unless the approved source explicitly requires naming it.
- Do not include real private keys, seed phrases, payable addresses, learner identities, balances, personal data, unverified QR data, or unverified factual claims.
- For text that must be editable or translated later, describe its purpose and source in `contentRequirements`; do not manufacture final wording.
- Use the approved recurring cast only when people are required. Identify each selected character by the name specified in the brief; consult `Assets/style/CHARACTERS.md` only if that identity needs clarification.
- Keep the record specific enough to construct one clear asset, but do not prescribe production technology or add unapproved decoration.

## Required JSON schema

Write valid JSON only. Do not add properties. Select one value wherever the schema gives alternatives separated by `|`; do not copy the alternatives literally. Use `[]` only when no item applies and `""` only when the field is explicitly not applicable.

For a `completed` record, every string must be non-empty except `placement.educatorGuide`, `placement.studentGuide`, and `review.notes` when they do not apply. Arrays may be empty only when no corresponding source requirement exists. `sourceFiles.styleReferences` must cite every style file consulted and may be empty when no consultation was needed. A `blocked` record may leave fields empty only when the missing information is identified in `unresolved`.

```json
{
  "assetId": "BD-V-000",
  "schemaVersion": 1,
  "status": "completed",
  "assetType": "Diagram",
  "recordDate": "YYYY-MM-DD",
  "sourceFiles": {
    "brief": "Assets/briefs/bd-v-000-brief.md",
    "briefRevision": "revision, date, or file state stated in the brief; otherwise undated",
    "styleReferences": [
      "Assets/style/STYLE.md"
    ]
  },
  "educationalPurpose": "",
  "placement": {
    "studentGuide": "",
    "educatorGuide": "",
    "guideAnchor": "exact guide heading and nearby text anchor from the brief",
    "format": ""
  },
  "teachingPoint": "",
  "visualPattern": "",
  "composition": {
    "orientation": "landscape",
    "targetAspectRatio": "",
    "readingOrder": [],
    "elements": [
      {
        "id": "",
        "role": "",
        "required": true,
        "relationship": "",
        "position": "",
        "treatment": ""
      }
    ]
  },
  "contentRequirements": [
    {
      "content": "exact approved wording, value, label, or content requirement",
      "source": "brief section",
      "editable": true
    }
  ],
  "style": {
    "layoutReference": "",
    "palette": [],
    "typography": "",
    "shapeAndLineRules": "",
    "geometry": "",
    "emphasis": "",
    "characters": [],
    "propsAndIcons": []
  },
  "prohibitions": [],
  "review": {
    "briefCompliant": true,
    "assetRegisterCompliant": true,
    "styleCompliant": true,
    "openDecisionsPreventCreation": false,
    "notes": ""
  },
  "unresolved": []
}
```

## Completion rules

Set `status` to `completed` only when all required fields are supported by the brief, any cited style references resolve a documented conflict or ambiguity, all three compliance fields are `true`, and `openDecisionsPreventCreation` is `false`. Use exact approved wording, values, labels, and content requirements from their cited source wherever later creation depends on them.

Set `status` to `blocked` when a missing or unresolved requirement prevents creation. State the exact source, requirement, and consequence in `unresolved`; set the affected review field to `false`; and do not mark the asset’s JSON reference as created in `Assets/assets-list.md`.

When filesystem access is available, create or update only the JSON reference and, for a completed record, the matching status entry in `Assets/assets-list.md`. Without filesystem access, return only the completed JSON in a fenced `json` block and state neither that a file nor the asset-list entry was updated.
