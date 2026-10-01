# Claude cloud handoff prompt

Use this prompt when handing one Bitcoin Diploma visual to Claude through a cloud conversation. Replace every bracketed field and attach the related files in the marked slots before sending.

```text
You are rebuilding one editable, accessible My First Bitcoin Bitcoin Diploma visual.

Do not publish, upload, merge, or modify the manuscript. Prepare a reviewable draft bundle only.

ASSET
- Asset ID: [BD-V-000]
- Short title: [TITLE]
- Intended guide: [Student Guide | Educator Guide | Shared]
- Exact placement and heading: [PASTE FROM ASSET BRIEF]
- Requested output folder or project location: [CLOUD PROJECT/FOLDER]

ATTACHMENTS — REQUIRED
1. Complete asset brief and section 7 classification record: [ATTACH FILE]
2. Approved transparent PNG reference: [ATTACH FILE]
3. Matching white-background JPG preview: [ATTACH FILE]
4. JSON conformance report: [ATTACH FILE]
5. Exact reference prompt record: [ATTACH FILE]

ATTACHMENTS — ADD WHEN AVAILABLE
6. Relevant adjacent guide excerpt: [ATTACH FILE OR PASTE EXCERPT]
7. Claude Design System authoring instructions: [ATTACH FILE]
8. Closest approved micrographic example: [ATTACH FILE]
9. Current Sanity schema or publishing requirements: [ATTACH FILE]
10. Accessibility, localization, or print requirements: [ATTACH FILE]
11. Factual sources approved for this asset: [ATTACH FILES OR LINKS]
12. Reviewer comments or prior decisions: [ATTACH FILE]

SOURCE-OF-TRUTH ORDER
1. The complete asset brief and section 7 record control teaching intent, required elements, counts, relationships, reading order, strings, safety, factual limits, placement, caption, alt text, and localization.
2. The supplied Claude Design System controls production styling, components, typography, iconography, and tokens.
3. Relevant shared-register entries control reusable actors, props, symbols, interfaces, and notation.
4. The approved PNG and JPG guide composition and visual treatment only. Rebuild them; never trace, embed, or publish them.
5. Adjacent guide text clarifies context but cannot override the asset brief.
6. Supplied schema controls metadata and export fields. Do not invent schema fields or upload endpoints.

If sources conflict, stop and list the exact conflict. If a required fact, URL, value, QR destination, legal statement, or safety condition is missing, leave it unresolved and do not invent a substitute.

IMPLEMENTATION
Rebuild the visual as editable HTML, CSS, and inline SVG. Keep all geometry, labels, arrows, connectors, icons, interface shapes, warnings, and data editable. Do not use the reference image as a background or raster master.

Create:
- micrographic.html with one root `<div class="mg-[SLUG]">`
- micrographic.css with every selector scoped to `.mg-[SLUG]`
- meta.json
- preview.html with a 458px review frame
- alt-text.md with final alt text and a concise text equivalent
- README.md with sources, revision, checks, reviewer status, and unresolved items
- sanity-asset.json only if the supplied schema supports it

Use no JavaScript, external images, external fonts, CSS grid, `vh`, `vw`, `rem`, fixed/sticky positioning, or `@import`. Tag each translatable text element with a unique non-nested `data-t` key. Keep layouts responsive at phone width, desktop width, 458px content width, A4/US Letter, grayscale, and future translation expansion/RTL adaptation.

SAFETY AND CONTENT
- Never include real seed phrases, private keys, payable addresses, private learner data, balances, or transactions.
- Do not invent prices, dates, providers, URLs, legal claims, safety claims, or current facts.
- Use QR codes, addresses, payment values, or named destinations only when the brief supplies and authorizes them and the final values have been verified.
- Preserve every qualification, prohibition, role distinction, and related-asset boundary.
- Do not imply investment returns, guaranteed outcomes, risk-free custody, inevitable adoption, or universal local conclusions.
- Do not turn a named wallet, exchange, service, or local resource into a general recommendation.

REVIEW BEFORE HANDOFF
Check the source brief against the implementation, visible text, reading order, responsive behavior, accessibility, grayscale meaning, print layout, factual accuracy, safety, and localization. Confirm the PNG reference is not embedded or published. Report any deviation, unresolved item, or schema limitation.

RETURN IN THIS ORDER
1. Files created, with cloud links or attachment names.
2. A short implementation summary.
3. Responsive, print, grayscale, accessibility, and factual checks.
4. Unresolved decisions and required human approvals.
5. A statement that nothing was uploaded or published.
```

Before sending, attach the asset-specific files rather than relying on local paths. For the current batch, the three deferred IDs—`BD-V-001`, `BD-V-070`, and `BD-V-075`—must remain deferred. Payment and destination placeholders for `BD-V-036`, `BD-V-078`, and `BD-V-080` must remain unresolved until approved production values are supplied.
