# Bitcoin Diploma asset production log

This log records the file-production status required by the asset workflow in [workspace/08_assets.md](../workspace/08_assets.md). Active brief, JSON and SVG/PNG records were checked on 2026-10-08. Postponed workflow rows retain their previous records unchanged; missing postponed files are not counted in the verified totals.

- Design briefs: 82 created
- Asset descriptions: 100 created
- JSON references: 65 created; 17 blocked records saved
- SVG/PNG references: 65 created; PNG-only references: 0 created
- VM uploads: 0 recorded
- MG packages: 0 created

“MG package” means the HTML/CSS ZIP package produced in workflow step 8. The workflow does not prescribe a package filename or folder, so this column records whether that deliverable exists rather than inferring a path. The JSON template `assets/reference/bd-v-###-ref.json` is not counted as an asset-specific JSON reference.

The Description column records whether an asset has a corresponding entry in [asset-description.md](asset-description.md).

## 2026.10 release status

The following assets are **POSTPONED** and will not be included in the 2026.10 Bitcoin Diploma release: `BD-V-001`, `BD-V-002`, `BD-V-003`, `BD-V-004`, `BD-V-005`, `BD-V-006`, `BD-V-007`, `BD-V-008`, `BD-V-014`, `BD-V-015`, `BD-V-020`, `BD-V-029`, `BD-V-040`, `BD-V-041`, `BD-V-049`, `BD-V-051`, `BD-V-057`, `BD-V-058`, and `BD-V-076`. Their description and guide-anchor records remain for a later reviewed release. The workflow columns below track file records only; `Created` does not mean the asset is included in 2026.10.

| Asset ID | Description | Brief | JSON reference | SVG/PNG reference | Uploaded to VM | MG package |
|---|---|---|---|---|---|
| BD-V-001 | Created | Not applicable — External Image; manually copy approved JPEG into the Diploma | Not applicable | Not applicable | Not applicable | Not applicable |
| BD-V-002 | Created | Created — `assets/briefs/bd-v-002-brief.md` | Not created | Not created | Not recorded | Not created |
| BD-V-003 | Created | Created — `assets/briefs/bd-v-003-brief.md` | Not created | Not created | Not recorded | Not created |
| BD-V-004 | Created | Created — `assets/briefs/bd-v-004-brief.md` | Not created | Not created | Not recorded | Not created |
| BD-V-005 | Created | Created — `assets/briefs/bd-v-005-brief.md` | Not created | Not created | Not recorded | Not created |
| BD-V-006 | Created | Created — `assets/briefs/bd-v-006-brief.md` | Not created | Not created | Not recorded | Not created |
| BD-V-007 | Created | Created — `assets/briefs/bd-v-007-brief.md` | Not created | Not created | Not recorded | Not created |
| BD-V-008 | Created | Created — `assets/briefs/bd-v-008-brief.md` | Not created | Not created | Not recorded | Not created |
| BD-V-009 | Created | Created — `assets/briefs/bd-v-009-brief.md` | Not created — blocked record saved; cast mapping unresolved | Blocked — Story roles Amina/Luis/Mei have no approved cast mapping. Proposed C01/C02/C04 mapping awaits the user’s yes/no clarification. | Not recorded | Not created |
| BD-V-010 | Created | Created — `assets/briefs/bd-v-010-brief.md` | Not created | Blocked — Amina and the two trading partners have no approved cast mapping. Proposed C01/C02/C04 mapping awaits the user’s yes/no clarification. | Not recorded | Not created |
| BD-V-011 | Created | Created — `assets/briefs/bd-v-011-brief.md` | Created — `assets/reference/bd-v-011-ref.json` | Created — `assets/reference/bd-v-011-ref.svg`; `assets/reference/bd-v-011-ref.png` | Not recorded | Not created |
| BD-V-012 | Created | Created — `assets/briefs/bd-v-012-brief.md` | Created — `assets/reference/bd-v-012-ref.json` | Created — `assets/reference/bd-v-012-ref.svg`; `assets/reference/bd-v-012-ref.png` | Not recorded | Not created |
| BD-V-013 | Created | Created — `assets/briefs/bd-v-013-brief.md` | Not created | Blocked — STYLE.md requires first-party icons, but no reusable first-party icon files are present. Original vector-cue permission is pending. | Not recorded | Not created |
| BD-V-014 | Created | Created — `assets/briefs/bd-v-014-brief.md` | Not created | Not created | Not recorded | Not created |
| BD-V-015 | Created | Created — `assets/briefs/bd-v-015-brief.md` | Not created | Not created | Not recorded | Not created |
| BD-V-016 | Created | Created — `assets/briefs/bd-v-016-brief.md` | Created — `assets/reference/bd-v-016-ref.json` | Created — `assets/reference/bd-v-016-ref.svg`; `assets/reference/bd-v-016-ref.png` | Not recorded | Not created |
| BD-V-017 | Created | Created — `assets/briefs/bd-v-017-brief.md` | Created — `assets/reference/bd-v-017-ref.json` | Created — `assets/reference/bd-v-017-ref.svg`; `assets/reference/bd-v-017-ref.png` | Not recorded | Not created |
| BD-V-018 | Created | Created — `assets/briefs/bd-v-018-brief.md` | Created — `assets/reference/bd-v-018-ref.json` | Created — `assets/reference/bd-v-018-ref.svg`; `assets/reference/bd-v-018-ref.png` | Not recorded | Not created |
| BD-V-019 | Created | Created — `assets/briefs/bd-v-019-brief.md` | Not created — blocked record saved; first-party icons missing | Blocked — The matrix format explicitly requires icons, but STYLE.md requires first-party icon files that are not supplied. Original vector-cue clarification is pending. | Not recorded | Not created |
| BD-V-020 | Created | Created — `assets/briefs/bd-v-020-brief.md` | Not created | Not created | Not recorded | Not created |
| BD-V-021 | Created | Created — `assets/briefs/bd-v-021-brief.md` | Created — `assets/reference/bd-v-021-ref.json` | Created — `assets/reference/bd-v-021-ref.svg`; `assets/reference/bd-v-021-ref.png` | Not recorded | Not created |
| BD-V-022 | Created | Created — `assets/briefs/bd-v-022-brief.md` | Created — `assets/reference/bd-v-022-ref.json` | Created — `assets/reference/bd-v-022-ref.svg`; `assets/reference/bd-v-022-ref.png` | Not recorded | Not created |
| BD-V-023 | Created | Created — `assets/briefs/bd-v-023-brief.md` | Created — `assets/reference/bd-v-023-ref.json` | Created — `assets/reference/bd-v-023-ref.svg`; `assets/reference/bd-v-023-ref.png` | Not recorded | Not created |
| BD-V-024 | Created | Created — `assets/briefs/bd-v-024-brief.md` | Not created | Blocked — Dictated direction requests three-dimensional blocks and binary marks; global flat-art and text-free reference rules conflict. Flat blocks with binary content deferred to live text awaits clarification. | Not recorded | Not created |
| BD-V-025 | Created | Created — `assets/briefs/bd-v-025-brief.md` | Created — `assets/reference/bd-v-025-ref.json` | Created — `assets/reference/bd-v-025-ref.svg`; `assets/reference/bd-v-025-ref.png` | Not recorded | Not created |
| BD-V-026 | Created | Created — `assets/briefs/bd-v-026-brief.md` | Created — `assets/reference/bd-v-026-ref.json` | Created — `assets/reference/bd-v-026-ref.svg`; `assets/reference/bd-v-026-ref.png` | Not recorded | Not created |
| BD-V-027 | Created | Created — `assets/briefs/bd-v-027-brief.md` | Created — `assets/reference/bd-v-027-ref.json` | Created — `assets/reference/bd-v-027-ref.svg`; `assets/reference/bd-v-027-ref.png` | Not recorded | Not created |
| BD-V-028 | Created | Created — `assets/briefs/bd-v-028-brief.md` | Created — `assets/reference/bd-v-028-ref.json` | Created — `assets/reference/bd-v-028-ref.svg`; `assets/reference/bd-v-028-ref.png` | Not recorded | Not created |
| BD-V-029 | Created | Created — `assets/briefs/bd-v-029-brief.md` | Not created | Not created | Not recorded | Not created |
| BD-V-030 | Created | Created — `assets/briefs/bd-v-030-brief.md` | Created — `assets/reference/bd-v-030-ref.json` | Created — `assets/reference/bd-v-030-ref.svg`; `assets/reference/bd-v-030-ref.png` | Not recorded | Not created |
| BD-V-031 | Created | Created — `assets/briefs/bd-v-031-brief.md` | Created — `assets/reference/bd-v-031-ref.json` | Created — `assets/reference/bd-v-031-ref.svg`; `assets/reference/bd-v-031-ref.png` | Not recorded | Not created |
| BD-V-032 | Created | Created — `assets/briefs/bd-v-032-brief.md` | Created — `assets/reference/bd-v-032-ref.json` | Created — `assets/reference/bd-v-032-ref.svg`; `assets/reference/bd-v-032-ref.png` | Not recorded | Not created |
| BD-V-033 | Created | Created — `assets/briefs/bd-v-033-brief.md` | Not created | Blocked — STYLE.md requires first-party icons, but no reusable first-party icon files are present. Original vector-cue permission is pending. | Not recorded | Not created |
| BD-V-034 | Created | Created — `assets/briefs/bd-v-034-brief.md` | Created — `assets/reference/bd-v-034-ref.json` | Created — `assets/reference/bd-v-034-ref.svg`; `assets/reference/bd-v-034-ref.png` | Not recorded | Not created |
| BD-V-035 | Created | Created — `assets/briefs/bd-v-035-brief.md` | Created — `assets/reference/bd-v-035-ref.json` | Created — `assets/reference/bd-v-035-ref.svg`; `assets/reference/bd-v-035-ref.png` | Not recorded | Not created |
| BD-V-036 | Created | Created — `assets/briefs/bd-v-036-brief.md` | Created — `assets/reference/bd-v-036-ref.json` | Created — `assets/reference/bd-v-036-ref.svg`; `assets/reference/bd-v-036-ref.png` | Not recorded | Not created |
| BD-V-037 | Created | Created — `assets/briefs/bd-v-037-brief.md` | Not created | Blocked — Asset-index description ends at “Label the…” and assets/asset-description.md supplies no completion. The missing labeling requirement must be restored before production. | Not recorded | Not created |
| BD-V-038 | Created | Created — `assets/briefs/bd-v-038-brief.md` | Created — `assets/reference/bd-v-038-ref.json` | Created — `assets/reference/bd-v-038-ref.svg`; `assets/reference/bd-v-038-ref.png` | Not recorded | Not created |
| BD-V-039 | Created | Created — `assets/briefs/bd-v-039-brief.md` | Created — `assets/reference/bd-v-039-ref.json` | Created — `assets/reference/bd-v-039-ref.svg`; `assets/reference/bd-v-039-ref.png` | Not recorded | Not created |
| BD-V-040 | Created | Created — `assets/briefs/bd-v-040-brief.md` | Not created | Not created | Not recorded | Not created |
| BD-V-041 | Created | Created — `assets/briefs/bd-v-041-brief.md` | Not created | Not created | Not recorded | Not created |
| BD-V-042 | Created | Created — `assets/briefs/bd-v-042-brief.md` | Created — `assets/reference/bd-v-042-ref.json` | Created — `assets/reference/bd-v-042-ref.svg`; `assets/reference/bd-v-042-ref.png` | Not recorded | Not created |
| BD-V-043 | Created | Created — `assets/briefs/bd-v-043-brief.md` | Not created | Blocked — STYLE.md requires first-party icons for six steps, but no reusable first-party icon files are present. Original vector-cue permission is pending. | Not recorded | Not created |
| BD-V-044 | Created | Created — `assets/briefs/bd-v-044-brief.md` | Created — `assets/reference/bd-v-044-ref.json` | Created — `assets/reference/bd-v-044-ref.svg`; `assets/reference/bd-v-044-ref.png` | Not recorded | Not created |
| BD-V-045 | Created | Created — `assets/briefs/bd-v-045-brief.md` | Created — `assets/reference/bd-v-045-ref.json` | Created — `assets/reference/bd-v-045-ref.svg`; `assets/reference/bd-v-045-ref.png` | Not recorded | Not created |
| BD-V-046 | Created | Created — `assets/briefs/bd-v-046-brief.md` | Created — `assets/reference/bd-v-046-ref.json` | Created — `assets/reference/bd-v-046-ref.svg`; `assets/reference/bd-v-046-ref.png` | Not recorded | Not created |
| BD-V-047 | Created | Created — `assets/briefs/bd-v-047-brief.md` | Created — `assets/reference/bd-v-047-ref.json` | Created — `assets/reference/bd-v-047-ref.svg`; `assets/reference/bd-v-047-ref.png` | Not recorded | Not created |
| BD-V-048 | Created | Created — `assets/briefs/bd-v-048-brief.md` | Created — `assets/reference/bd-v-048-ref.json` | Created — `assets/reference/bd-v-048-ref.svg`; `assets/reference/bd-v-048-ref.png` | Not recorded | Not created |
| BD-V-049 | Created | Created — `assets/briefs/bd-v-049-brief.md` | Not created | Not created | Not recorded | Not created |
| BD-V-050 | Created | Created — `assets/briefs/bd-v-050-brief.md` | Not created | Blocked — The required Bitcoin logo is not supplied as an approved vector asset; do not redraw an official mark or substitute visible lettering in the text-free reference. | Not recorded | Not created |
| BD-V-051 | Created | Created — `assets/briefs/bd-v-051-brief.md` | Not created | Not created | Not recorded | Not created |
| BD-V-052 | Created | Created — `assets/briefs/bd-v-052-brief.md` | Created — `assets/reference/bd-v-052-ref.json` | Created — `assets/reference/bd-v-052-ref.svg`; `assets/reference/bd-v-052-ref.png` | Not recorded | Not created |
| BD-V-053 | Created | Created — `assets/briefs/bd-v-053-brief.md` | Created — `assets/reference/bd-v-053-ref.json` | Created — `assets/reference/bd-v-053-ref.svg`; `assets/reference/bd-v-053-ref.png` | Not recorded | Not created |
| BD-V-054 | Created | Created — `assets/briefs/bd-v-054-brief.md` | Created — `assets/reference/bd-v-054-ref.json` | Created — `assets/reference/bd-v-054-ref.svg`; `assets/reference/bd-v-054-ref.png` | Not recorded | Not created |
| BD-V-055 | Created | Created — `assets/briefs/bd-v-055-brief.md` | Created — `assets/reference/bd-v-055-ref.json` | Created — `assets/reference/bd-v-055-ref.svg`; `assets/reference/bd-v-055-ref.png` | Not recorded | Not created |
| BD-V-056 | Created | Created — `assets/briefs/bd-v-056-brief.md` | Created — `assets/reference/bd-v-056-ref.json` | Created — `assets/reference/bd-v-056-ref.svg`; `assets/reference/bd-v-056-ref.png` | Not recorded | Not created |
| BD-V-057 | Created | Created — `assets/briefs/bd-v-057-brief.md` | Not created | Not created | Not recorded | Not created |
| BD-V-058 | Created | Created — `assets/briefs/bd-v-058-brief.md` | Not created | Not created | Not recorded | Not created |
| BD-V-059 | Created | Created — `assets/briefs/bd-v-059-brief.md` | Created — `assets/reference/bd-v-059-ref.json` | Created — `assets/reference/bd-v-059-ref.svg`; `assets/reference/bd-v-059-ref.png` | Not recorded | Not created |
| BD-V-060 | Created | Created — `assets/briefs/bd-v-060-brief.md` | Not created | Blocked — STYLE.md requires first-party icons for seven uses, but no reusable first-party icon files are present. Original vector-cue permission is pending. | Not recorded | Not created |
| BD-V-061 | Created | Created — `assets/briefs/bd-v-061-brief.md` | Created — `assets/reference/bd-v-061-ref.json` | Created — `assets/reference/bd-v-061-ref.svg`; `assets/reference/bd-v-061-ref.png` | Not recorded | Not created |
| BD-V-062 | Created | Created — `assets/briefs/bd-v-062-brief.md` | Created — `assets/reference/bd-v-062-ref.json` | Created — `assets/reference/bd-v-062-ref.svg`; `assets/reference/bd-v-062-ref.png` | Not recorded | Not created |
| BD-V-063 | Created | Created — `assets/briefs/bd-v-063-brief.md` | Created — `assets/reference/bd-v-063-ref.json` | Created — `assets/reference/bd-v-063-ref.svg`; `assets/reference/bd-v-063-ref.png` | Not recorded | Not created |
| BD-V-064 | Created | Created — `assets/briefs/bd-v-064-brief.md` | Created — `assets/reference/bd-v-064-ref.json` | Created — `assets/reference/bd-v-064-ref.svg`; `assets/reference/bd-v-064-ref.png` | Not recorded | Not created |
| BD-V-065 | Created | Created — `assets/briefs/bd-v-065-brief.md` | Created — `assets/reference/bd-v-065-ref.json` | Created — `assets/reference/bd-v-065-ref.svg`; `assets/reference/bd-v-065-ref.png` | Not recorded | Not created |
| BD-V-066 | Created | Created — `assets/briefs/bd-v-066-brief.md` | Created — `assets/reference/bd-v-066-ref.json` | Created — `assets/reference/bd-v-066-ref.svg`; `assets/reference/bd-v-066-ref.png` | Not recorded | Not created |
| BD-V-067 | Created | Created — `assets/briefs/bd-v-067-brief.md` | Not created | Blocked — Map is required by asset row but prohibited for print by layouts/README.md. Web-only treatment awaits clarification; current SG moved detailed resource activities to Resources Hub. | Not recorded | Not created |
| BD-V-068 | Created | Created — `assets/briefs/bd-v-068-brief.md` | Not created | Blocked — Index calls for replacement of a local-resource table, but current SG has neither that table nor a BD-V-068 marker and directs detailed tables to Resources Hub. Placement needs editorial reconciliation. | Not recorded | Not created |
| BD-V-069 | Created | Created — `assets/briefs/bd-v-069-brief.md` | Created — `assets/reference/bd-v-069-ref.json` | Created — `assets/reference/bd-v-069-ref.svg`; `assets/reference/bd-v-069-ref.png` | Not recorded | Not created |
| BD-V-070 | Created | Created — `assets/briefs/bd-v-070-brief.md` | Created — `assets/reference/bd-v-070-ref.json` | Created — `assets/reference/bd-v-070-ref.svg`; `assets/reference/bd-v-070-ref.png` | Not recorded | Not created |
| BD-V-071 | Created | Created — `assets/briefs/bd-v-071-brief.md` | Created — `assets/reference/bd-v-071-ref.json` | Created — `assets/reference/bd-v-071-ref.svg`; `assets/reference/bd-v-071-ref.png` | Not recorded | Not created |
| BD-V-072 | Created | Created — `assets/briefs/bd-v-072-brief.md` | Created — `assets/reference/bd-v-072-ref.json` | Created — `assets/reference/bd-v-072-ref.svg`; `assets/reference/bd-v-072-ref.png` | Not recorded | Not created |
| BD-V-073 | Created | Created — `assets/briefs/bd-v-073-brief.md` | Not created | Blocked — Required canonical destination https://github.com/MyFirstBitcoin/mfb-curriculum could not be verified on 2026-10-08; web access failed. Do not generate an unverified QR. | Not recorded | Not created |
| BD-V-074 | Created | Created — `assets/briefs/bd-v-074-brief.md` | Not created | Blocked — Index destination https://donate.myfirstbitcoin.org/ conflicts with current SG https://myfirstbitcoin.org/support-us; BD-V-074 marker is absent. Destination selection and successful live testing remain required. | Not recorded | Not created |
| BD-V-075 | Not created | Created — `assets/briefs/bd-v-075-brief.md` | Not created | Blocked — Index explicitly says Do not produce for 2026.10. Future issuer-specific destination, privacy, correction/withdrawal rules, minimum data and governance approval are not supplied. | Not recorded | Not created |
| BD-V-076 | Created | POSTPONED — not included in 2026.10; do not produce or place | Not applicable | Not applicable | Not applicable | Not applicable |
| BD-V-077 | Created | Created — `assets/briefs/bd-v-077-brief.md` | Not created | Blocked — Required live MFB Journey verification failed on 2026-10-08: https://journey.myfirstbitcoin.org/ was inaccessible. Stage names/order remain unverified. | Not recorded | Not created |
| BD-V-078 | Created | Created — `assets/briefs/bd-v-078-brief.md` | Created — `assets/reference/bd-v-078-ref.json` | Created — `assets/reference/bd-v-078-ref.svg`; `assets/reference/bd-v-078-ref.png` | Not recorded | Not created |
| BD-V-079 | Created | Created — `assets/briefs/bd-v-079-brief.md` | Not created | Blocked — Asset-index description ends at “Check every…” and assets/asset-description.md supplies no completion. The exact safety callout must be restored before production. | Not recorded | Not created |
| BD-V-080 | Created | Created — `assets/briefs/bd-v-080-brief.md` | Created — `assets/reference/bd-v-080-ref.json` | Created — `assets/reference/bd-v-080-ref.svg`; `assets/reference/bd-v-080-ref.png` | Not recorded | Not created |
| BD-V-081 | Created | Created — `assets/briefs/bd-v-081-brief.md` | Created — `assets/reference/bd-v-081-ref.json` | Created — `assets/reference/bd-v-081-ref.svg`; `assets/reference/bd-v-081-ref.png` | Not recorded | Not created |
| BD-V-082 | Created | Created — `assets/briefs/bd-v-082-brief.md` | Created — `assets/reference/bd-v-082-ref.json` | Created — `assets/reference/bd-v-082-ref.svg`; `assets/reference/bd-v-082-ref.png` | Not recorded | Not created |
| BD-V-083 | Created | Created — `assets/briefs/bd-v-083-brief.md` | Created — `assets/reference/bd-v-083-ref.json` | Created — `assets/reference/bd-v-083-ref.svg`; `assets/reference/bd-v-083-ref.png` | Not recorded | Not created |
| BD-V-084 | Created | Created — `assets/briefs/bd-v-084-brief.md` | Created — `assets/reference/bd-v-084-ref.json` | Created — `assets/reference/bd-v-084-ref.svg`; `assets/reference/bd-v-084-ref.png` | Not recorded | Not created |
| BD-V-085 | Created | Created — `assets/briefs/bd-v-085-brief.md` | Created — `assets/reference/bd-v-085-ref.json` | Created — `assets/reference/bd-v-085-ref.svg`; `assets/reference/bd-v-085-ref.png` | Not recorded | Not created |
| BD-V-086 | Created | Created — `assets/briefs/bd-v-086-brief.md` | Created — `assets/reference/bd-v-086-ref.json` | Created — `assets/reference/bd-v-086-ref.svg`; `assets/reference/bd-v-086-ref.png` | Not recorded | Not created |
| BD-V-087 | Created | Created — `assets/briefs/bd-v-087-brief.md` | Created — `assets/reference/bd-v-087-ref.json` | Created — `assets/reference/bd-v-087-ref.svg`; `assets/reference/bd-v-087-ref.png` | Not recorded | Not created |
| BD-V-088 | Created | Created — `assets/briefs/bd-v-088-brief.md` | Created — `assets/reference/bd-v-088-ref.json` | Created — `assets/reference/bd-v-088-ref.svg`; `assets/reference/bd-v-088-ref.png` | Not recorded | Not created |
| BD-V-089 | Created | Created — `assets/briefs/bd-v-089-brief.md` | Created — `assets/reference/bd-v-089-ref.json` | Created — `assets/reference/bd-v-089-ref.svg`; `assets/reference/bd-v-089-ref.png` | Not recorded | Not created |
| BD-V-090 | Created | Created — `assets/briefs/bd-v-090-brief.md` | Created — `assets/reference/bd-v-090-ref.json` | Created — `assets/reference/bd-v-090-ref.svg`; `assets/reference/bd-v-090-ref.png` | Not recorded | Not created |
| BD-V-091 | Created | Created — `assets/briefs/bd-v-091-brief.md` | Created — `assets/reference/bd-v-091-ref.json` | Created — `assets/reference/bd-v-091-ref.svg`; `assets/reference/bd-v-091-ref.png` | Not recorded | Not created |
| BD-V-092 | Created | Created — `assets/briefs/bd-v-092-brief.md` | Created — `assets/reference/bd-v-092-ref.json` | Created — `assets/reference/bd-v-092-ref.svg`; `assets/reference/bd-v-092-ref.png` | Not recorded | Not created |
| BD-V-093 | Created | Created — `assets/briefs/bd-v-093-brief.md` | Created — `assets/reference/bd-v-093-ref.json` | Created — `assets/reference/bd-v-093-ref.svg`; `assets/reference/bd-v-093-ref.png` | Not recorded | Not created |
| BD-V-094 | Created | Created — `assets/briefs/bd-v-094-brief.md` | Created — `assets/reference/bd-v-094-ref.json` | Created — `assets/reference/bd-v-094-ref.svg`; `assets/reference/bd-v-094-ref.png` | Not recorded | Not created |
| BD-V-095 | Created | Created — `assets/briefs/bd-v-095-brief.md` | Created — `assets/reference/bd-v-095-ref.json` | Created — `assets/reference/bd-v-095-ref.svg`; `assets/reference/bd-v-095-ref.png` | Not recorded | Not created |
| BD-V-096 | Created | Created — `assets/briefs/bd-v-096-brief.md` | Created — `assets/reference/bd-v-096-ref.json` | Created — `assets/reference/bd-v-096-ref.svg`; `assets/reference/bd-v-096-ref.png` | Not recorded | Not created |
| BD-V-097 | Created | Created — `assets/briefs/bd-v-097-brief.md` | Created — `assets/reference/bd-v-097-ref.json` | Created — `assets/reference/bd-v-097-ref.svg`; `assets/reference/bd-v-097-ref.png` | Not recorded | Not created |
| BD-V-098 | Created | Created — `assets/briefs/bd-v-098-brief.md` | Created — `assets/reference/bd-v-098-ref.json` | Created — `assets/reference/bd-v-098-ref.svg`; `assets/reference/bd-v-098-ref.png` | Not recorded | Not created |
| BD-V-099 | Created | Created — `assets/briefs/bd-v-099-brief.md` | Created — `assets/reference/bd-v-099-ref.json` | Created — `assets/reference/bd-v-099-ref.svg`; `assets/reference/bd-v-099-ref.png` | Not recorded | Not created |
| BD-V-100 | Created | Created — `assets/briefs/bd-v-100-brief.md` | Created — `assets/reference/bd-v-100-ref.json` | Created — `assets/reference/bd-v-100-ref.svg`; `assets/reference/bd-v-100-ref.png` | Not recorded | Not created |
| BD-V-101 | Created | Created — `assets/briefs/bd-v-101-brief.md` | Created — `assets/reference/bd-v-101-ref.json` | Created — `assets/reference/bd-v-101-ref.svg`; `assets/reference/bd-v-101-ref.png` | Not recorded | Not created |
