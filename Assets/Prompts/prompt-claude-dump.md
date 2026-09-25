# Bitcoin Diploma — Claude design and Sanity workflow

## Function

Turn one approved reference set into one reviewable, editable, accessible production bundle for My First Bitcoin's Bitcoin Diploma. Do not publish, upload to Sanity, merge, modify the manuscript, trace/embed/publish reference images, or release deferred items. Reference images are inputs only, never masters.

For reference creation before production, use the Codex reference-image workflow: one low-resolution genuine-transparent PNG, matching white-background JPG, and conformance JSON; no text, logos, QR, data, arrows/connectors, or production use. Current reference/production deferrals: `BD-V-001`, `BD-V-070`, `BD-V-075`. `BD-V-001` later uses its official CC BY-SA 4.0 mark under its brief; never an AI redraw.

## Inputs and authority

Required: asset ID; complete `workspace/08_assets.md` entry; its section-7 classification record; relevant section-8 shared-register entries; approved PNG/JPG/JSON reference set; exact reference prompt record. Add adjacent guide text only for lesson context; Claude Design System/local authoring contract (including supplied `micrographics/README.md`, `micrographics/tokens.css`, closest approved bundle); supplied Sanity schema/publishing requirements; approved factual sources/reviewer decisions.

Authority order:

1. Asset entry + section 7: teaching intent, elements/counts/composition/relationships/reading order/strings, exclusions/safety/facts/localization/placement/caption/alt text.
2. Claude Design System: tokens, components, typography, iconography, layout, brand.
3. Section 8: reusable actors/props/symbols/interfaces/notation; do not merge distinct roles.
4. Approved references: composition/treatment guidance only; JSON identifies placement/deviation but is not proof.
5. Adjacent guide text: context only.
6. Actual Sanity schema: deliverable/metadata fields.

Conflict, essential missing fact, or section-7 `open` item blocking structure: stop and report exact issue; do not invent labels, numbers, providers, URLs, legal/safety claims, facts, values, QR destinations, or schema fields/endpoints. Reject/revise reference before use if it contains text or unjustified additions.

Interpret asset-index fields: stable `ID`; `Suggested by`/historic `Page`/`Note` provenance only; `Priority` never lowers review; `Type` visual family and, for a table, whether it is a stand-alone addition or a replacement; `Placement` authoritative guide/heading/insertion and folder choice; `Line` stale locator only; `Text–visual link` single teaching relationship; `Design brief` binding contract; `Format` responsive/print role. Preserve every qualifier, prohibition, related-asset boundary, accessibility/localization/editability requirement.

## Process

Start from nearest approved micrographic bundle. Rebuild—not trace—the useful reference grammar as editable HTML, CSS, inline SVG; change it when accessibility, accuracy, localization, responsiveness, or Design System requires. All essential geometry, arrows/connectors, icons, interface shapes, labels/warnings/data editable code/SVG text.

Implement exact brief elements/relationships/order/strings/safety. One clear teaching idea and reading order. Make people/local details replaceable. Do not rely on colour: also use shape, line style, pattern, position, text; support grayscale, ~458px book content, phone, desktop, A4/US Letter, text expansion, future RTL.

Safety: preserve all brief guardrails; no real seed/private key/payable address/private learner data/balance/transaction; fictional interfaces/sample QR/non-payable examples only as brief requires; verify every visible fact/number/date/URL/QR/interface; no financial-return guarantee, risk-free custody, inevitable adoption, universal legal/local conclusion, or global named-service recommendation.

## Output

At response top state short title + lowercase hyphenated slug. Create tracked bundle:

`assets/diploma/<student-guide|educator-guide|shared>/bd-v-000/`

Use `shared` only when the same implementation serves both placements; preserve all placements in metadata. Never copy reference files into bundle or use flat `assets/diploma/bd-v-000/` as canonical source.

- `micrographic.html`: one `<div class="mg-<slug>">` root.
- `micrographic.css`: every selector scoped `.mg-<slug>`; print-safe `pt|mm|em|%`, flexbox/explicit sizes where needed; no grid, `vh/vw/rem`, fixed/sticky, `@import`, JS, external image/font.
- Inline SVG with correct attribute capitalization; editable icons/relationships.
- `meta.json`: at least `bundleVersion`, `title`, `slug`, `altText`, `caption`, `assetId`, `sourceGuide`, `editableText:true`, plus supplied schema fields.
- `preview.html`: self-contained Design-System preview, 458px review frame.
- Translatable text: unique non-nested `data-t="key"`; not universal pure numbers/symbols.
- `alt-text.md`: final alt text, concise complex-diagram text equivalent, required caption.
- `README.md`: ID; brief/section-7 revisions; section-8 entries; reference paths/deviations; factual sources; date; responsive/grayscale checks; reviewer status; unresolved judgments.
- Export only as schema/pipeline requires (prefer approved SVG; raster derivative only, never sole master). If schema supports it, `sanity-asset.json`: ID, title, alt text, caption, source guide, exact placement, export filename/type, dimensions/viewBox, focal point, credit/licence, review status. Do not invent unsupported fields.

## Test/review and handoff

Before completion: compare source brief to implementation; check visible text, elements/counts/relationships/order, accessibility/text equivalent, localization/RTL growth, responsive 458px/phone/desktop, A4/US Letter, grayscale meaning, print CSS, factual accuracy, safety, reference exclusion, schema compatibility. Report deviations, unresolved items, design-system/schema constraints, and checks. Set `reviewStatus` only `draft|review` unless authorized reviewer approves. Completion requires editable master, correct guide folder, matching caption/alt text, documented checks, and no unauthorized upload/publication.

Cloud handoff: attach asset-specific brief/section-7 record, PNG, JPG, JSON, prompt record; attach optional Design System, closest bundle, schema, sources, accessibility/localization/print requirements, reviewer comments. Return: created files/links; implementation summary; responsive/print/grayscale/accessibility/factual checks; unresolved decisions/human approvals; explicit no-upload/no-publication statement.
