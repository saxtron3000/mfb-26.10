# SVG illustration versions

The current [svg/ directory](../svg/) contains **34 SVGs**, named `bd-illustration-001.svg` through `bd-illustration-034.svg` (approximately 168.8 MB total). Each corresponds to a guide-scene HD PNG in [png/](../png/), for example [SVG 001](../svg/bd-illustration-001.svg) and [HD PNG 001](../png/bd-illustration-001-hd.png).

There are no SVGs for the 101 `bd-illustration-v-###` subject scenes, and no `bd-illustration-v-txt-###` SVGs. The directory name is lowercase `svg`; there are no text/no-text subfolders.

These SVGs are automatic color traces of earlier PNG artwork. They contain colored vector paths. All 34 files were parsed as XML during this refresh, and none contains an image element or a text element. The traces approximate shading, contours, and fine details; they do not recover detail absent from their source artwork. The original native-resolution PNGs are no longer in this library.

SVG paths scale independently of DPI. Place artwork proportionally at the desired physical size. If the publishing tool rasterizes it, select at least 300 PPI at the final placed size. The available HD PNGs were previously rendered from the matching SVGs; see [print notes](HD-README.md).

See [the placement index](illustrations.md) for guide scenes and [the current inventory](../metadata/file-inventory.json) for exact dimensions, file sizes, and SHA-256 hashes. This refresh verifies structure and metadata, without a new render comparison or visual review.
