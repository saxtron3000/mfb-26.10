# Bitcoin Diploma Publication Specification

## Purpose

This document defines the required publication outputs and consistency rules for the redesigned Bitcoin Diploma package.

---

# Required Outputs

The redesign package should produce:

- Student Book
- Offline print/PDF package
- Online PDF package
- Educator Guide
- Activity Bank
- Custom / Bitcoin as Money templates
- Assessment framework
- Public stakeholder brief
- Public Keynote handoff
- Legacy table-of-contents migration notes inside `06_plan.md`
- Advanced module holding file `16_advanced.md`
- Website-ready source files
- Translation-ready Markdown source files
- Future delivery-branch notes for online cohort, self-paced, app, and cross-modal continuation

---

# Naming Rules

Use this block structure consistently:

1. Problem / Fiat
2. Solution / Bitcoin
3. Action / Self-custody
4. Custom / Bitcoin as Money

Use "block" for required Diploma structure.

Use "Custom modules" or "Custom units" only for educator-selectable content inside Block 4.

Do not rename Block 4 globally as "Spending." Spending is one possible Custom / Bitcoin as Money practice.

Do not use retired structure labels, old numbered-module labels for the required structure, or retired plan-file references.

---

# Source Of Truth Rules

- `06_plan.md` owns block structure and legacy table-of-contents migration notes.
- `06_plan.md` owns Core / Custom / Advanced boundaries.
- `16_advanced.md` owns candidate Advanced module titles, follow-on pathway ideas, and redacted legacy content for future Advanced use.
- `05_objectives.md` owns objectives and outcome levels.
- `10_activities.md` owns activity templates.
- `11_guide.md` owns educator guidance.
- `12_assessment.md` owns assessment direction.
- `13_certification.md` owns certification boundaries.
- `../public/MFB-BD-Keynote.md` owns the combined public stakeholder brief, keynote source material, and 10-minute keynote handoff.

The full Advanced module title list must appear only in `16_advanced.md`.

Legacy migration details should be used for internal planning and should not be copied wholesale into public materials.

Named tools, services, wallets, exchanges, maps, and local resources should be treated as local examples unless explicitly approved for global publication.

Current-data examples should be verified, dated, cited, or rewritten as evergreen explanations before publication.

The archived duplicate plan at `../y_archive/y_13_plan_superseded.md` is historical context only and must not be treated as an active source.

---

# Translation Readiness Rules

The curriculum should be drafted in English first. Translation readiness is an editorial requirement, not only a production-format requirement.

English source files should:

- use consistent terminology;
- avoid unnecessary idioms;
- keep sentences clear and direct;
- keep tone and style consistent;
- prefer simple sentence structures that carry one main idea;
- separate global Core concepts from local examples;
- identify terms that require glossary decisions;
- identify concepts that require localization rather than direct translation.

Before translation or publication, the English source must be reviewed for:

- beginner readability;
- simplicity and sentence length;
- tone and style;
- terminology consistency;
- ambiguity;
- idioms, slang, wordplay, and culturally narrow metaphors;
- translation and localization risks.

After translation, each language version should be reviewed for preserved meaning, appropriate tone, simple language, terminology consistency, and local appropriateness before publication.

---

# QR Code Rules

Printed PDFs should use QR codes sparingly.

Acceptable QR destinations include:

- source repository or canonical update page;
- educator resources;
- support or donation page;
- certificate verification, if available.

Avoid QR codes for unstable current data, temporary campaigns, named local tools, or essential learner content that must remain available offline.

---

# Delivery-Mode Rules

The first publication mode is offline-capable print or PDF for in-person delivery.

Future branches should preserve the same Core outcomes:

- online PDF;
- online cohort;
- self-paced;
- web;
- app;
- cross-modal continuation.

Future branches may adapt pacing, facilitation, evidence of learning, media, and learner support, but they should not create separate outcome standards.

---

# Public Communication Rules

Public materials should:

- explain the redesign in plain language;
- emphasize preservation of mission;
- show the before / after clearly;
- explain the 4-block model visually;
- describe the Custom block as educator-selected and locally grounded;
- explain that spending is one possible local practice, not the whole definition of Block 4;
- avoid overpromising assessment or certification;
- avoid overpromising app or cross-modal delivery before those branches are designed;
- avoid presenting named tools or services as global recommendations;
- avoid using current statistics without dates or verification;
- avoid QR-code clutter in print-ready public materials;
- avoid listing all Advanced module titles;
- explain that legacy content is being reorganized across Core, Custom, and Advanced pathways rather than simply discarded.

---

# Final Consistency Checks

Before publication, search active docs excluding `y_archive` for retired labels and retired plan references.

The only acceptable location for the full Advanced module title list outside `y_archive` is `16_advanced.md`.

Confirm `06_plan.md` remains the active beginner redesign plan source of truth, `16_advanced.md` remains the Advanced module holding file, and duplicated planning files remain outside the active workspace.

Confirm all references point to `14_lexicon.md` for terminology and `15_spec.md` for publication rules.

Confirm current-data examples, legal/tax statements, and named-service references have been fact-checked, dated, localized, or removed.

Confirm the English source has passed simplicity, tone, style, terminology, and translation-readiness review before translation or publication.

Confirm each translated version has passed language-specific meaning, tone, simplicity, terminology, and localization review before publication.

Confirm print QR codes are sparse, stable, and non-essential to the offline learner path.
