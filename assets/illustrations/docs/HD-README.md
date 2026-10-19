# HD PNG illustration versions

The current [png/ directory](../png/) contains **135 HD PNGs**, all ending in `-hd.png`:

- 34 `bd-illustration-###-hd.png` guide scenes, with matching SVGs in [svg/](../svg/).
- 101 `bd-illustration-v-###-hd.png` subject scenes, with no SVGs currently present.

There are no native-resolution PNGs, TXT variants, duplicate-image directories, or separate `png-hd/` folder. The HD PNG files total approximately 318.1 MB.

## Resolution and placement

All 135 PNGs have physical-resolution metadata of approximately 600 PPI on both axes (599.9988 PPI, the PNG integer-unit representation) and enough pixels for at least 600 effective PPI at A5. The measured minimum effective resolution is **600.161 PPI**, calculated using 148 × 210 mm for portrait artwork and 210 × 148 mm for landscape artwork. Exact pixel dimensions and embedded DPI appear in [the inventory](../metadata/file-inventory.json).

Place images proportionally. Wider scenes may have extra horizontal pixels; recheck effective resolution after a crop or enlargement. An image's embedded DPI alone does not guarantee resolution at every placed size.

These HD exports were previously rendered from traced SVGs. They inherit the traces' approximations; higher output resolution does not recover missing detail. Only the 34 guide-scene SVGs remain available. See [SVG notes](SVG-README.md).

## Verification and guide references

On 19 October 2026, all 135 files were checked for PNG signatures, chunk lengths and CRCs, end markers, dimensions, physical-resolution metadata, and SHA-256 hashes. This refresh does not include a new decoded-image inspection or visual-quality review.

The 34 guide illustration markers still point to old native PNG paths. The available replacement paths and current marker lines are listed in [the placement index](illustrations.md) and [guide-scene metadata](../metadata/bd-illustration-index.json).
