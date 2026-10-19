# MFB asset layout skeletons

**Purpose:** choose a stable content skeleton before placing illustrations, graphics or copy. The PNGs in this directory are visual references; this file records the reusable layout system they represent.

The recurring cast is Sara (C01, educator), Luis (C02, beginner learner), Ernesto (C03, older learner), Amina (C04, business owner), Lukas (C05, technical learner), and Mei (C06, young learner). Use the canonical names in [`../CHARACTERS.md`](../CHARACTERS.md). The older payment example in `mfb-assets-one-page.v3.png` labels Luis and Amina with superseded names; update editable copy to Luis and Amina when reusing that layout.

## Layout rule

Layouts decide placement, rhythm and shared chrome; they do not invent a graphic, icon or visual treatment. Use the Tier 3 graphic pattern that fits the learning need, then place it in the relevant skeleton.

## Skeletons

| Surface | Skeletons | Frame and non-negotiables |
|---|---|---|
| Print | `chapter-opener`, `teaching-page`, `exercise-page` | Flexible A4 or Legal page; learner-readable text is at least 12pt; graphics must pass in greyscale; no maps. |
| Web | `landing-hero`, `content-page`, `directory-index` | Maximum 1280px content width; strong left alignment and generous negative space. |
| App | `app-home`, `app-lesson`, `app-progress` | Mobile-first 390px reference frame; every touch target is at least 44px. |
| Shared chrome | `web-header`, `doc-sidebar`, `app-tab-bar` | Reuse across their named surfaces; active state is an orange colour change, never an underline bar. |

## Placement rules

- Anchor the main heading at the top-left. Put supporting information lower or to the right.
- Use purple plus white/paper as the usual two brand background colours; do not add a third brand field to solve hierarchy.
- Keep frames at one structural slant and counter-skew their contents. Do not put a slanted frame around a small icon: frames are permitted at 48px and above only.
- Let a graphic occupy a clear, purposeful region. Do not layer diagrams, decorative texture and dense copy in the same area.
- On print, preserve an editable, live-label version of every diagram. For HTML/CSS micrographics, follow the print requirements in [`../STYLE.md`](../STYLE.md#10-final-production-requirements).
