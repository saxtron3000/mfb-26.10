# Illustration library

The current library contains **135 text-free HD PNGs and 34 traced SVGs**, verified on 19 October 2026.

| Folder | Files | Contents |
| --- | ---: | --- |
| [png/](png/) | 135 | 34 guide scenes and 101 visual-index subject scenes; all filenames end in `-hd.png` |
| [svg/](svg/) | 34 | Matching vectors for the 34 guide scenes |
| [docs/](docs/) | 3 | Placement index, SVG notes, and HD print notes |
| [metadata/](metadata/) | 5 | Current indexes, inventory, path aliases, and historical TXT heading copy |

`bd-illustration-###` and `bd-illustration-v-###` are separate series with independent numbering. The first has 17 placements in each guide. The second corresponds to `BD-V-###` topics in the visual asset index; neither guide directly references these illustration filenames.

There are no `v-txt` images, native-resolution PNGs, text/no-text subfolders, separate `png-hd/` folders, or duplicate-image directories. Historical TXT headings are retained as text only in metadata.

- [Current structure and guide placements](docs/illustrations.md)
- [SVG conversion and use](docs/SVG-README.md)
- [HD resolution and print use](docs/HD-README.md)
- [34 guide scenes and recorded guide paths](metadata/bd-illustration-index.json)
- [101 visual-index subject scenes](metadata/bd-illustration-v-index.json)
- [Historical TXT heading copy; zero current artwork entries](metadata/bd-illustration-v-txt-index.json)
- [Current artwork inventory and hashes](metadata/file-inventory.json)
- [Current paths and known historical aliases](metadata/path-map.json)

All 34 guide illustration markers still reference old native PNG paths that no longer exist. The placement index links to the available HD files and records the source mismatch. This documentation update does not edit the guides.

HD PNGs have at least 600 effective PPI at A5. Their resolution does not restore detail lost during SVG tracing; see the conversion notes before print production.
