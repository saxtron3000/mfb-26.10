# Bitcoin Diploma Publication Specification

## Purpose

This document defines the required publication outputs and consistency rules for the redesigned Bitcoin Diploma package.

---

# Required Outputs

The redesign package should produce:

- Student Book
- Educator Guide
- Activity Bank
- Custom / Bitcoin as Money templates
- Assessment framework
- Public stakeholder brief
- Prague keynote handoff
- Legacy table-of-contents migration notes inside `06_plan.md`
- Split-modules migration notes inside `06_plan.md`
- Website-ready source files
- Translation-ready Markdown source files

---

# Naming Rules

Use this block structure consistently:

1. Problem / Fiat
2. Solution / Bitcoin
3. Action / Self-custody
4. Custom / Bitcoin as Money

Use “block” for required Diploma structure.

Use “Custom modules” or “Custom units” only for educator-selectable content inside Block 4.

Do not use retired structure labels, old numbered-module labels for the required structure, or retired plan-file references.

---

# Source Of Truth Rules

- `06_plan.md` owns block structure, legacy table-of-contents migration notes, and candidate Advanced module titles.
- `06_plan.md` owns split-modules migration rules and Core / Custom / Advanced boundaries.
- `05_objectives.md` owns objectives and outcome levels.
- `10_activities.md` owns activity templates.
- `11_guide.md` owns educator guidance.
- `12_assessment.md` owns assessment direction.
- `13_certification.md` owns certification boundaries.
- `../public/mfb-bd-prague.md` owns the full public stakeholder brief.
- `../public/mfb-bd-prague-keynote.md` owns the short 10-minute keynote handoff.

The full Advanced module title list must appear only in `06_plan.md`.

Legacy migration details should be used for internal planning and should not be copied wholesale into public materials.

The split-modules document is internal drafting source material. It should not be presented as a separate public structure or as a source of truth.

Named tools, services, wallets, exchanges, maps, and local resources should be treated as local examples unless explicitly approved for global publication.

Current-data examples should be verified, dated, cited, or rewritten as evergreen explanations before publication.

---

# Public Communication Rules

Public materials should:

- explain the redesign in plain language;
- emphasize preservation of mission;
- show the before / after clearly;
- explain the 4-block model visually;
- describe the Custom block as educator-selected and locally grounded;
- avoid overpromising assessment or certification;
- avoid presenting named tools or services as global recommendations;
- avoid using current statistics without dates or verification;
- avoid listing all Advanced module titles;
- explain that legacy content is being reorganized across Core, Custom, and Advanced pathways rather than simply discarded.

---

# Final Consistency Checks

Before publication, search active docs excluding `y_archive` for retired labels and retired plan references.

The only acceptable location for the full Advanced module title list outside `y_archive` is `06_plan.md`.

Confirm `06_plan.md` is the only active plan source of truth and reconcile or archive duplicated planning files such as `13_plan.md`.

Confirm all references point to `14_lexicon.md` for terminology and `15_spec.md` for publication rules.

Confirm current-data examples, legal/tax statements, and named-service references have been fact-checked, dated, localized, or removed.
