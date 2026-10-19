# Bitcoin Diploma illustration library

Verified against the current files and guide markers on 19 October 2026.

## Current structure

```text
assets/illustrations/
├── png/       135 HD PNGs: 34 guide scenes and 101 visual-index scenes
├── svg/        34 traced SVGs: guide scenes only
├── docs/       Placement, SVG, and print documentation
├── metadata/   Current inventories, indexes, and historical path aliases
└── README.md
```

| Series | PNG files | SVG files | Guide use |
| --- | ---: | ---: | --- |
| `bd-illustration-###` | 34, named `bd-illustration-###-hd.png` | 34 | 17 illustration markers in each guide |
| `bd-illustration-v-###` | 101, named `bd-illustration-v-###-hd.png` | 0 | Subject scenes keyed to `BD-V-###`; no direct image-file references in either guide |
| `bd-illustration-v-txt-###` | 0 | 0 | No references in either guide |

The series have independent numbering. The `-v-` scenes accompany topics from the visual asset index; they are not substitutes for that index's required diagrams, tables, external images, or production approvals. No native-resolution PNGs, TXT variants, duplicate-image directories, or separate `png-hd/` directory are present.

## Placement and print use

The 34 guide scenes retain 17 `ILLUSTRATION` production markers in the Student Guide and 17 in the Educator Guide. These HTML comments reserve placements; they do not display images in a plain Markdown preview. Keep technical `VISUAL: BD-V-###` markers separate.

All 34 guide markers still record old `assets/illustrations/png/no-text/bd-illustration-###.png` paths that do not exist. The available files are `assets/illustrations/png/bd-illustration-###-hd.png`. The links below point to available artwork; guide source paths are recorded as found in [the guide-scene metadata](../metadata/bd-illustration-index.json). Updating guide source paths is a separate edit.

Placement lines below point to the start of each illustration comment in the current Markdown source, not a finished print page. Refresh them after guide edits. All available PNGs have at least 600 effective PPI at A5; see [HD print notes](HD-README.md). The SVGs are automatic traces; see [SVG notes](SVG-README.md).

## Allocation overview

| Illustration | Guide | Section | Marker line |
| --- | --- | --- | --- |
| [bd-illustration-025](../png/bd-illustration-025-hd.png) | Student Guide | About Us | [Line 32](../../../publish/mfb-bd-26.10/mfb-bd-sg-26.10.md#L32) |
| [bd-illustration-033](../png/bd-illustration-033-hd.png) | Student Guide | Flexible learning | [Line 152](../../../publish/mfb-bd-26.10/mfb-bd-sg-26.10.md#L152) |
| [bd-illustration-001](../png/bd-illustration-001-hd.png) | Student Guide | Discussion and [privacy](https://programs.myfirstbitcoin.org/lexicon/en/#privacy) expectations | [Line 178](../../../publish/mfb-bd-26.10/mfb-bd-sg-26.10.md#L178) |
| [bd-illustration-026](../png/bd-illustration-026-hd.png) | Student Guide | Opening questions about money | [Line 288](../../../publish/mfb-bd-26.10/mfb-bd-sg-26.10.md#L288) |
| [bd-illustration-028](../png/bd-illustration-028-hd.png) | Student Guide | Functions and properties of money | [Line 353](../../../publish/mfb-bd-26.10/mfb-bd-sg-26.10.md#L353) |
| [bd-illustration-002](../png/bd-illustration-002-hd.png) | Student Guide | [Decentralization](https://programs.myfirstbitcoin.org/lexicon/en/#decentralization) | [Line 760](../../../publish/mfb-bd-26.10/mfb-bd-sg-26.10.md#L760) |
| [bd-illustration-003](../png/bd-illustration-003-hd.png) | Student Guide | Users, [nodes](https://programs.myfirstbitcoin.org/lexicon/en/#node), [miners](https://programs.myfirstbitcoin.org/lexicon/en/#miner), and developers | [Line 818](../../../publish/mfb-bd-26.10/mfb-bd-sg-26.10.md#L818) |
| [bd-illustration-004](../png/bd-illustration-004-hd.png) | Student Guide | [Proof of work](https://programs.myfirstbitcoin.org/lexicon/en/#proof-of-work) | [Line 849](../../../publish/mfb-bd-26.10/mfb-bd-sg-26.10.md#L849) |
| [bd-illustration-005](../png/bd-illustration-005-hd.png) | Student Guide | Wallets | [Line 1110](../../../publish/mfb-bd-26.10/mfb-bd-sg-26.10.md#L1110) |
| [bd-illustration-006](../png/bd-illustration-006-hd.png) | Student Guide | Hot and [cold wallets](https://programs.myfirstbitcoin.org/lexicon/en/#cold-wallet-cold-storage) | [Line 1261](../../../publish/mfb-bd-26.10/mfb-bd-sg-26.10.md#L1261) |
| [bd-illustration-007](../png/bd-illustration-007-hd.png) | Student Guide | Receiving bitcoin | [Line 1309](../../../publish/mfb-bd-26.10/mfb-bd-sg-26.10.md#L1309) |
| [bd-illustration-008](../png/bd-illustration-008-hd.png) | Student Guide | Sending bitcoin | [Line 1340](../../../publish/mfb-bd-26.10/mfb-bd-sg-26.10.md#L1340) |
| [bd-illustration-009](../png/bd-illustration-009-hd.png) | Student Guide | [Verification](https://programs.myfirstbitcoin.org/lexicon/en/#verification), [block explorers](https://programs.myfirstbitcoin.org/lexicon/en/#block-explorer), and irreversible [transactions](https://programs.myfirstbitcoin.org/lexicon/en/#transaction-tx) | [Line 1364](../../../publish/mfb-bd-26.10/mfb-bd-sg-26.10.md#L1364) |
| [bd-illustration-010](../png/bd-illustration-010-hd.png) | Student Guide | On-chain and Lightning payments | [Line 1460](../../../publish/mfb-bd-26.10/mfb-bd-sg-26.10.md#L1460) |
| [bd-illustration-031](../png/bd-illustration-031-hd.png) | Student Guide | Practical workshops and demonstrations | [Line 1588](../../../publish/mfb-bd-26.10/mfb-bd-sg-26.10.md#L1588) |
| [bd-illustration-011](../png/bd-illustration-011-hd.png) | Student Guide | Local spending and receiving scenarios | [Line 1775](../../../publish/mfb-bd-26.10/mfb-bd-sg-26.10.md#L1775) |
| [bd-illustration-012](../png/bd-illustration-012-hd.png) | Student Guide | Circular economies | [Line 1877](../../../publish/mfb-bd-26.10/mfb-bd-sg-26.10.md#L1877) |
| [bd-illustration-013](../png/bd-illustration-013-hd.png) | Educator Guide | The page-by-page teaching rhythm | [Line 318](../../../publish/mfb-bd-26.10/mfb-bd-eg-26.10.md#L318) |
| [bd-illustration-027](../png/bd-illustration-027-hd.png) | Educator Guide | Open the course with clear expectations | [Line 523](../../../publish/mfb-bd-26.10/mfb-bd-eg-26.10.md#L523) |
| [bd-illustration-014](../png/bd-illustration-014-hd.png) | Educator Guide | Welcome disagreement and correct error | [Line 556](../../../publish/mfb-bd-26.10/mfb-bd-eg-26.10.md#L556) |
| [bd-illustration-015](../png/bd-illustration-015-hd.png) | Educator Guide | Think–pair–share | [Line 781](../../../publish/mfb-bd-26.10/mfb-bd-eg-26.10.md#L781) |
| [bd-illustration-016](../png/bd-illustration-016-hd.png) | Educator Guide | Demonstration with prediction | [Line 826](../../../publish/mfb-bd-26.10/mfb-bd-eg-26.10.md#L826) |
| [bd-illustration-030](../png/bd-illustration-030-hd.png) | Educator Guide | Debrief every activity | [Line 862](../../../publish/mfb-bd-26.10/mfb-bd-eg-26.10.md#L862) |
| [bd-illustration-017](../png/bd-illustration-017-hd.png) | Educator Guide | Low-tech teaching: focus on interaction | [Line 879](../../../publish/mfb-bd-26.10/mfb-bd-eg-26.10.md#L879) |
| [bd-illustration-018](../png/bd-illustration-018-hd.png) | Educator Guide | Universal stop conditions | [Line 980](../../../publish/mfb-bd-26.10/mfb-bd-eg-26.10.md#L980) |
| [bd-illustration-019](../png/bd-illustration-019-hd.png) | Educator Guide | Barter and the double coincidence of wants | [Line 1164](../../../publish/mfb-bd-26.10/mfb-bd-eg-26.10.md#L1164) |
| [bd-illustration-020](../png/bd-illustration-020-hd.png) | Educator Guide | Decentralization and peer-to-peer transfer | [Line 1574](../../../publish/mfb-bd-26.10/mfb-bd-eg-26.10.md#L1574) |
| [bd-illustration-021](../png/bd-illustration-021-hd.png) | Educator Guide | Proof of work | [Line 1640](../../../publish/mfb-bd-26.10/mfb-bd-eg-26.10.md#L1640) |
| [bd-illustration-032](../png/bd-illustration-032-hd.png) | Educator Guide | Strong Module 2 activities | [Line 1803](../../../publish/mfb-bd-26.10/mfb-bd-eg-26.10.md#L1803) |
| [bd-illustration-022](../png/bd-illustration-022-hd.png) | Educator Guide | Activity: recovery-readiness simulation | [Line 2138](../../../publish/mfb-bd-26.10/mfb-bd-eg-26.10.md#L2138) |
| [bd-illustration-023](../png/bd-illustration-023-hd.png) | Educator Guide | Module option D: merchant payment and refund flow | [Line 2854](../../../publish/mfb-bd-26.10/mfb-bd-eg-26.10.md#L2854) |
| [bd-illustration-034](../png/bd-illustration-034-hd.png) | Educator Guide | Activity purpose comes first | [Line 3235](../../../publish/mfb-bd-26.10/mfb-bd-eg-26.10.md#L3235) |
| [bd-illustration-029](../png/bd-illustration-029-hd.png) | Educator Guide | 14. Use visuals as teaching tools | [Line 3382](../../../publish/mfb-bd-26.10/mfb-bd-eg-26.10.md#L3382) |
| [bd-illustration-024](../png/bd-illustration-024-hd.png) | Educator Guide | Capstone discussion | [Line 3404](../../../publish/mfb-bd-26.10/mfb-bd-eg-26.10.md#L3404) |

## Recurring cast

| ID | Identity retained from the character bible |
| --- | --- |
| C01 | Educator: dark hair in a high bun, purple suit, white blouse and sneakers. |
| C02 | Beginner learner: backward purple cap, white hoodie, purple trousers and white sneakers. |
| C03 | Older learner: white curls and beard, rectangular glasses, purple pullover, white collar and light trousers. |
| C04 | Business owner: long dark wavy hair, orange blazer, white blouse, purple trousers and pumps. |
| C05 | Technical learner: short dark curls, rectangular glasses, purple hoodie and cargo trousers. |
| C06 | Young learner: orange beanie, long dark hair, white T-shirt and purple cargo trousers; offline classroom participation only. |

Scenes 025–030 include all six characters. Scenes 031–034 feature both adult women, C01 and C04; C06 joins the network lesson and offline card activity.

## Student Guide — 17 illustrations

### bd-illustration-025 — Welcome to the learning group

[HD PNG](../png/bd-illustration-025-hd.png) · [SVG](../svg/bd-illustration-025.svg) · PNG: 3505 × 4962 px

**Placement:** Student Guide, “[About Us](../../../publish/mfb-bd-26.10/mfb-bd-sg-26.10.md#L32)”, **marker line 32**.

**Cast:** C01, C02, C03, C04, C05, C06.

**Scene / alt text:** The educator welcomes the beginner, older learner, business owner, technical learner, and young learner into a shared learning group.

**Educational purpose:** Show a welcoming, inclusive learning community with all six recurring characters.

### bd-illustration-033 — Studying the guide as a pair

[HD PNG](../png/bd-illustration-033-hd.png) · [SVG](../svg/bd-illustration-033.svg) · PNG: 3503 × 4962 px

**Placement:** Student Guide, “[Flexible learning](../../../publish/mfb-bd-26.10/mfb-bd-sg-26.10.md#L152)”, **marker line 152**.

**Cast:** C01, C04.

**Scene / alt text:** The business owner points to a simple diagram in an open guide while the educator discusses it with her at a classroom table.

**Educational purpose:** Show women comparing an explanation and developing understanding through shared reading.

### bd-illustration-001 — Questions are welcome

[HD PNG](../png/bd-illustration-001-hd.png) · [SVG](../svg/bd-illustration-001.svg) · PNG: 3505 × 4962 px

**Placement:** Student Guide, “[Discussion and [privacy](https://programs.myfirstbitcoin.org/lexicon/en/#privacy) expectations](../../../publish/mfb-bd-26.10/mfb-bd-sg-26.10.md#L178)”, **marker line 178**.

**Cast:** C01, C02, C03.

**Scene / alt text:** The educator responds to the beginner learner's raised hand while the older learner follows along with an open course guide.

**Educational purpose:** Show that asking questions and discussing ideas are part of learning.

### bd-illustration-026 — Reading and learning together

[HD PNG](../png/bd-illustration-026-hd.png) · [SVG](../svg/bd-illustration-026.svg) · PNG: 3503 × 4962 px

**Placement:** Student Guide, “[Opening questions about money](../../../publish/mfb-bd-26.10/mfb-bd-sg-26.10.md#L288)”, **marker line 288**.

**Cast:** C01, C02, C03, C04, C05, C06.

**Scene / alt text:** All six characters gather around classroom tables as the educator leads a shared reading from an open course guide.

**Educational purpose:** Show that shared reading and discussion can support learners of different ages and experience.

### bd-illustration-028 — Working through an activity

[HD PNG](../png/bd-illustration-028-hd.png) · [SVG](../svg/bd-illustration-028.svg) · PNG: 3503 × 4962 px

**Placement:** Student Guide, “[Functions and properties of money](../../../publish/mfb-bd-26.10/mfb-bd-sg-26.10.md#L353)”, **marker line 353**.

**Cast:** C01, C02, C03, C04, C05, C06.

**Scene / alt text:** All six characters collaborate on an offline teaching-card activity while the educator guides the discussion.

**Educational purpose:** Show cooperative learning through a simple shared activity with everyday classroom materials.

### bd-illustration-002 — Exploring the network

[HD PNG](../png/bd-illustration-002-hd.png) · [SVG](../svg/bd-illustration-002.svg) · PNG: 3505 × 4962 px

**Placement:** Student Guide, “[[Decentralization](https://programs.myfirstbitcoin.org/lexicon/en/#decentralization)](../../../publish/mfb-bd-26.10/mfb-bd-sg-26.10.md#L760)”, **marker line 760**.

**Cast:** C01, C02, C05.

**Scene / alt text:** The educator points to a network on a classroom screen while the beginner and technical learners discuss it at a desk.

**Educational purpose:** Introduce learning about a network of independent participants.

### bd-illustration-003 — Inspecting a node computer

[HD PNG](../png/bd-illustration-003-hd.png) · [SVG](../svg/bd-illustration-003.svg) · PNG: 3505 × 4962 px

**Placement:** Student Guide, “[Users, [nodes](https://programs.myfirstbitcoin.org/lexicon/en/#node), [miners](https://programs.myfirstbitcoin.org/lexicon/en/#miner), and developers](../../../publish/mfb-bd-26.10/mfb-bd-sg-26.10.md#L818)”, **marker line 818**.

**Cast:** C01, C05.

**Scene / alt text:** The educator guides the technical learner at a node computer, with the monitor facing them and its rear casing visible to the viewer.

**Educational purpose:** Connect the role of a node with real computer equipment.

### bd-illustration-004 — Looking at mining equipment

[HD PNG](../png/bd-illustration-004-hd.png) · [SVG](../svg/bd-illustration-004.svg) · PNG: 3503 × 4962 px

**Placement:** Student Guide, “[[Proof of work](https://programs.myfirstbitcoin.org/lexicon/en/#proof-of-work)](../../../publish/mfb-bd-26.10/mfb-bd-sg-26.10.md#L849)”, **marker line 849**.

**Cast:** C01, C02, C05.

**Scene / alt text:** The educator, beginner learner, and technical learner discuss a tabletop mining unit with a fan and separate power supply.

**Educational purpose:** Show mining as physical computing equipment and energy use.

### bd-illustration-005 — Learning a phone wallet

[HD PNG](../png/bd-illustration-005-hd.png) · [SVG](../svg/bd-illustration-005.svg) · PNG: 3505 × 4962 px

**Placement:** Student Guide, “[Wallets](../../../publish/mfb-bd-26.10/mfb-bd-sg-26.10.md#L1110)”, **marker line 1110**.

**Cast:** C01, C02, C03.

**Scene / alt text:** The educator demonstrates a training phone while the beginner and older learners examine their own devices.

**Educational purpose:** Introduce guided practice with a wallet interface.

### bd-illustration-006 — Comparing access devices

[HD PNG](../png/bd-illustration-006-hd.png) · [SVG](../svg/bd-illustration-006.svg) · PNG: 3505 × 4962 px

**Placement:** Student Guide, “[Hot and [cold wallets](https://programs.myfirstbitcoin.org/lexicon/en/#cold-wallet-cold-storage)](../../../publish/mfb-bd-26.10/mfb-bd-sg-26.10.md#L1261)”, **marker line 1261**.

**Cast:** C01, C03, C05.

**Scene / alt text:** The educator helps the older and technical learners compare a phone, a hardware wallet, and a laptop.

**Educational purpose:** Prompt discussion of different wallet devices and custody choices.

### bd-illustration-007 — Preparing to receive

[HD PNG](../png/bd-illustration-007-hd.png) · [SVG](../svg/bd-illustration-007.svg) · PNG: 3505 × 4962 px

**Placement:** Student Guide, “[Receiving bitcoin](../../../publish/mfb-bd-26.10/mfb-bd-sg-26.10.md#L1309)”, **marker line 1309**.

**Cast:** C01, C02, C03.

**Scene / alt text:** The older learner presents a training phone while the beginner checks another phone and the educator guides the comparison.

**Educational purpose:** Show the recipient preparing and checking a payment request.

### bd-illustration-008 — Checking before sending

[HD PNG](../png/bd-illustration-008-hd.png) · [SVG](../svg/bd-illustration-008.svg) · PNG: 3511 × 4962 px

**Placement:** Student Guide, “[Sending bitcoin](../../../publish/mfb-bd-26.10/mfb-bd-sg-26.10.md#L1340)”, **marker line 1340**.

**Cast:** C01, C02, C04.

**Scene / alt text:** The educator guides the beginner learner as they compare a phone with the business owner's receiving device before approving a payment.

**Educational purpose:** Emphasize checking both sides before approving a payment.

### bd-illustration-009 — Verifying a prepared transaction

[HD PNG](../png/bd-illustration-009-hd.png) · [SVG](../svg/bd-illustration-009.svg) · PNG: 3505 × 4962 px

**Placement:** Student Guide, “[[Verification](https://programs.myfirstbitcoin.org/lexicon/en/#verification), [block explorers](https://programs.myfirstbitcoin.org/lexicon/en/#block-explorer), and irreversible [transactions](https://programs.myfirstbitcoin.org/lexicon/en/#transaction-tx)](../../../publish/mfb-bd-26.10/mfb-bd-sg-26.10.md#L1364)”, **marker line 1364**.

**Cast:** C01, C03, C05.

**Scene / alt text:** The educator and older learner discuss a prepared example on a monitor facing the group while the technical learner operates the mouse; the viewer sees the rear casing.

**Educational purpose:** Show learners checking a prepared public transaction example together.

### bd-illustration-010 — Comparing payment paths

[HD PNG](../png/bd-illustration-010-hd.png) · [SVG](../svg/bd-illustration-010.svg) · PNG: 3511 × 4962 px

**Placement:** Student Guide, “[On-chain and Lightning payments](../../../publish/mfb-bd-26.10/mfb-bd-sg-26.10.md#L1460)”, **marker line 1460**.

**Cast:** C01, C02, C05.

**Scene / alt text:** The educator points to two different geometric payment paths on a board while the beginner and technical learners consider them.

**Educational purpose:** Prompt comparison of payment paths without implying a universal best choice.

### bd-illustration-031 — Practising a phone wallet together

[HD PNG](../png/bd-illustration-031-hd.png) · [SVG](../svg/bd-illustration-031.svg) · PNG: 3503 × 4962 px

**Placement:** Student Guide, “[Practical workshops and demonstrations](../../../publish/mfb-bd-26.10/mfb-bd-sg-26.10.md#L1588)”, **marker line 1588**.

**Cast:** C01, C04.

**Scene / alt text:** The educator and business owner practise with a training phone together, both looking at the screen facing them.

**Educational purpose:** Show two adult women taking an active role in guided wallet-interface practice.

### bd-illustration-011 — A small everyday purchase

[HD PNG](../png/bd-illustration-011-hd.png) · [SVG](../svg/bd-illustration-011.svg) · PNG: 3511 × 4962 px

**Placement:** Student Guide, “[Local spending and receiving scenarios](../../../publish/mfb-bd-26.10/mfb-bd-sg-26.10.md#L1775)”, **marker line 1775**.

**Cast:** C01, C02, C04.

**Scene / alt text:** The beginner and business owner check separate phones beside groceries on a counter as the educator guides the practice.

**Educational purpose:** Connect classroom payment practice to an everyday merchant scenario.

### bd-illustration-012 — Discussing community exchange

[HD PNG](../png/bd-illustration-012-hd.png) · [SVG](../svg/bd-illustration-012.svg) · PNG: 3511 × 4962 px

**Placement:** Student Guide, “[Circular economies](../../../publish/mfb-bd-26.10/mfb-bd-sg-26.10.md#L1877)”, **marker line 1877**.

**Cast:** C01, C02, C03, C04.

**Scene / alt text:** The educator facilitates a discussion with the beginner, older learner, and business owner around guides, a phone, and everyday goods.

**Educational purpose:** Show community members discussing exchange and local usefulness.

## Educator Guide — 17 illustrations

### bd-illustration-013 — Teaching from the Diploma

[HD PNG](../png/bd-illustration-013-hd.png) · [SVG](../svg/bd-illustration-013.svg) · PNG: 3505 × 4962 px

**Placement:** Educator Guide, “[The page-by-page teaching rhythm](../../../publish/mfb-bd-26.10/mfb-bd-eg-26.10.md#L318)”, **marker line 318**.

**Cast:** C01, C02, C03.

**Scene / alt text:** The educator points to a diagram in an open course guide as the beginner and older learner follow along in their own guides.

**Educational purpose:** Model using the Student Guide as the foundation of a teaching conversation.

### bd-illustration-027 — Making space for questions

[HD PNG](../png/bd-illustration-027-hd.png) · [SVG](../svg/bd-illustration-027.svg) · PNG: 3503 × 4962 px

**Placement:** Educator Guide, “[Open the course with clear expectations](../../../publish/mfb-bd-26.10/mfb-bd-eg-26.10.md#L523)”, **marker line 523**.

**Cast:** C01, C02, C03, C04, C05, C06.

**Scene / alt text:** The young learner asks a question while the educator listens and the other four learners follow the discussion.

**Educational purpose:** Model inclusive participation and respectful attention to a learner's question.

### bd-illustration-014 — Listening to a learner's question

[HD PNG](../png/bd-illustration-014-hd.png) · [SVG](../svg/bd-illustration-014.svg) · PNG: 3497 × 4962 px

**Placement:** Educator Guide, “[Welcome disagreement and correct error](../../../publish/mfb-bd-26.10/mfb-bd-eg-26.10.md#L556)”, **marker line 556**.

**Cast:** C01, C02, C03.

**Scene / alt text:** The educator listens to the beginner learner's question while the older learner follows the conversation with an open guide.

**Educational purpose:** Model listening and welcoming questions without shaming learners.

### bd-illustration-015 — Facilitating peer discussion

[HD PNG](../png/bd-illustration-015-hd.png) · [SVG](../svg/bd-illustration-015.svg) · PNG: 3505 × 4962 px

**Placement:** Educator Guide, “[Think–pair–share](../../../publish/mfb-bd-26.10/mfb-bd-eg-26.10.md#L781)”, **marker line 781**.

**Cast:** C01, C02, C03, C04.

**Scene / alt text:** The educator invites a discussion while the beginner and older learners compare guides and the business owner contributes.

**Educational purpose:** Show an educator inviting learners to compare and explain their reasoning.

### bd-illustration-016 — Pausing for prediction

[HD PNG](../png/bd-illustration-016-hd.png) · [SVG](../svg/bd-illustration-016.svg) · PNG: 3505 × 4962 px

**Placement:** Educator Guide, “[Demonstration with prediction](../../../publish/mfb-bd-26.10/mfb-bd-eg-26.10.md#L826)”, **marker line 826**.

**Cast:** C01, C02, C05.

**Scene / alt text:** The educator pauses a phone demonstration to invite predictions from the beginner and technical learners.

**Educational purpose:** Model inviting predictions before performing a demonstration step.

### bd-illustration-030 — Sharing what we have learned

[HD PNG](../png/bd-illustration-030-hd.png) · [SVG](../svg/bd-illustration-030.svg) · PNG: 3503 × 4962 px

**Placement:** Educator Guide, “[Debrief every activity](../../../publish/mfb-bd-26.10/mfb-bd-eg-26.10.md#L862)”, **marker line 862**.

**Cast:** C01, C02, C03, C04, C05, C06.

**Scene / alt text:** The older learner shares a reflection as the educator and the other four learners listen around a classroom table.

**Educational purpose:** Show learners contributing their own explanations and reflecting together as a community.

### bd-illustration-017 — Leading an offline card activity

[HD PNG](../png/bd-illustration-017-hd.png) · [SVG](../svg/bd-illustration-017.svg) · PNG: 3505 × 4962 px

**Placement:** Educator Guide, “[Low-tech teaching: focus on interaction](../../../publish/mfb-bd-26.10/mfb-bd-eg-26.10.md#L879)”, **marker line 879**.

**Cast:** C01, C03, C06.

**Scene / alt text:** The educator and older learner arrange teaching cards while the young learner participates with a notebook.

**Educational purpose:** Show useful participation with simple offline classroom materials.

### bd-illustration-018 — Pausing a practice safely

[HD PNG](../png/bd-illustration-018-hd.png) · [SVG](../svg/bd-illustration-018.svg) · PNG: 3511 × 4962 px

**Placement:** Educator Guide, “[Universal stop conditions](../../../publish/mfb-bd-26.10/mfb-bd-eg-26.10.md#L980)”, **marker line 980**.

**Cast:** C01, C02, C05.

**Scene / alt text:** The educator raises an open palm to pause an activity while the beginner lowers a phone and the technical learner partly closes a laptop.

**Educational purpose:** Model stopping and asking for help when a practice check fails.

### bd-illustration-019 — Facilitating an exchange activity

[HD PNG](../png/bd-illustration-019-hd.png) · [SVG](../svg/bd-illustration-019.svg) · PNG: 3505 × 4962 px

**Placement:** Educator Guide, “[Barter and the double coincidence of wants](../../../publish/mfb-bd-26.10/mfb-bd-eg-26.10.md#L1164)”, **marker line 1164**.

**Cast:** C01, C02, C04.

**Scene / alt text:** The educator facilitates a direct-exchange activity between the beginner holding a notebook and the business owner holding groceries.

**Educational purpose:** Support discussion of what makes direct exchange easy or difficult.

### bd-illustration-020 — Leading a network presentation

[HD PNG](../png/bd-illustration-020-hd.png) · [SVG](../svg/bd-illustration-020.svg) · PNG: 3505 × 4962 px

**Placement:** Educator Guide, “[Decentralization and peer-to-peer transfer](../../../publish/mfb-bd-26.10/mfb-bd-eg-26.10.md#L1574)”, **marker line 1574**.

**Cast:** C01, C02, C05.

**Scene / alt text:** The educator uses a pointer to explain a network on a presentation board to the beginner and technical learners.

**Educational purpose:** Show the educator using a visual to explain peer relationships.

### bd-illustration-021 — Explaining mining and verification

[HD PNG](../png/bd-illustration-021-hd.png) · [SVG](../svg/bd-illustration-021.svg) · PNG: 3505 × 4962 px

**Placement:** Educator Guide, “[Proof of work](../../../publish/mfb-bd-26.10/mfb-bd-eg-26.10.md#L1640)”, **marker line 1640**.

**Cast:** C01, C03, C05.

**Scene / alt text:** The educator and technical learner indicate separate mining and node devices while the older learner participates with a guide.

**Educational purpose:** Support a discussion that distinguishes mining hardware from node verification.

### bd-illustration-032 — Explaining peer connections

[HD PNG](../png/bd-illustration-032-hd.png) · [SVG](../svg/bd-illustration-032.svg) · PNG: 3503 × 4962 px

**Placement:** Educator Guide, “[Strong Module 2 activities](../../../publish/mfb-bd-26.10/mfb-bd-eg-26.10.md#L1803)”, **marker line 1803**.

**Cast:** C01, C04, C06.

**Scene / alt text:** The business owner explains a network of peers while the educator listens and the young learner follows with a notebook.

**Educational purpose:** Show an adult woman explaining her understanding to an educator and a younger learner.

### bd-illustration-022 — Teaching recovery readiness privately

[HD PNG](../png/bd-illustration-022-hd.png) · [SVG](../svg/bd-illustration-022.svg) · PNG: 3505 × 4962 px

**Placement:** Educator Guide, “[Activity: recovery-readiness simulation](../../../publish/mfb-bd-26.10/mfb-bd-eg-26.10.md#L2138)”, **marker line 2138**.

**Cast:** C01, C03, C05.

**Scene / alt text:** The educator guides a recovery-readiness discussion as the older learner places a blank training card in an envelope and the technical learner watches.

**Educational purpose:** Show privacy-aware recovery practice without exposing any secret.

### bd-illustration-023 — Coaching a merchant payment role-play

[HD PNG](../png/bd-illustration-023-hd.png) · [SVG](../svg/bd-illustration-023.svg) · PNG: 3503 × 4962 px

**Placement:** Educator Guide, “[Module option D: merchant payment and refund flow](../../../publish/mfb-bd-26.10/mfb-bd-eg-26.10.md#L2854)”, **marker line 2854**.

**Cast:** C01, C02, C04.

**Scene / alt text:** The educator points to a blank record card while the beginner and business owner check training phones at a merchant counter.

**Educational purpose:** Model educator-guided payment checks and merchant records.

### bd-illustration-034 — Comparing ideas with teaching cards

[HD PNG](../png/bd-illustration-034-hd.png) · [SVG](../svg/bd-illustration-034.svg) · PNG: 3503 × 4962 px

**Placement:** Educator Guide, “[Activity purpose comes first](../../../publish/mfb-bd-26.10/mfb-bd-eg-26.10.md#L3235)”, **marker line 3235**.

**Cast:** C01, C04, C06.

**Scene / alt text:** The educator guides the business owner and young learner as they compare blank teaching cards at a table.

**Educational purpose:** Show women and a younger learner reasoning together through an accessible offline activity.

### bd-illustration-029 — Understanding a network together

[HD PNG](../png/bd-illustration-029-hd.png) · [SVG](../svg/bd-illustration-029.svg) · PNG: 3505 × 4962 px

**Placement:** Educator Guide, “[14. Use visuals as teaching tools](../../../publish/mfb-bd-26.10/mfb-bd-eg-26.10.md#L3382)”, **marker line 3382**.

**Cast:** C01, C02, C03, C04, C05, C06.

**Scene / alt text:** The educator explains six interconnected peers on a whiteboard to all five learners, including the young learner in an orange beanie.

**Educational purpose:** Introduce network relationships through an educator-led visual discussion.

### bd-illustration-024 — Leading the final reflection

[HD PNG](../png/bd-illustration-024-hd.png) · [SVG](../svg/bd-illustration-024.svg) · PNG: 3503 × 4962 px

**Placement:** Educator Guide, “[Capstone discussion](../../../publish/mfb-bd-26.10/mfb-bd-eg-26.10.md#L3404)”, **marker line 3404**.

**Cast:** C01, C02, C03, C04.

**Scene / alt text:** The educator invites a final explanation from the older learner while the beginner and business owner listen with their guides.

**Educational purpose:** Model a final discussion that draws out understanding and remaining questions.

## Metadata and style sources

- [Guide scenes and recorded guide paths](../metadata/bd-illustration-index.json)
- [101 visual-index scenes](../metadata/bd-illustration-v-index.json)
- [Historical TXT heading copy; no current artwork](../metadata/bd-illustration-v-txt-index.json)
- [Current image inventory, dimensions, PPI, and SHA-256 hashes](../metadata/file-inventory.json)
- [Current paths and known historical aliases](../metadata/path-map.json)

Scene descriptions, cast identities, and educational purposes are retained from the prior illustration index. Existing style references are [STYLE.md](../../style/STYLE.md), [CHARACTERS.md](../../style/CHARACTERS.md), and [layout instructions](../../style/layouts/README.md). This documentation refresh checks file structure and metadata; it does not constitute a new visual review.
