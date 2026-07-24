# Extracted reviewer comments

Source: `feedback/2026-06-23_08_draft.docx` (the original file was not modified).

## OOXML package findings

- The document text is in `word/document.xml`, primarily as `w:p` paragraphs, `w:tbl` tables, `w:r/w:t` runs, hyperlinks, and list properties.
- Comments are in `word/comments.xml`; each has only `w:id`, `w:author`, and `w:date` plus comment-body runs. There is no `w:parentId`, threaded-comments part, people part, or explicit reply relation.
- Comment anchors are `w:commentRangeStart`, `w:commentRangeEnd`, and `w:commentReference` in `word/document.xml`. The export has 28 comments, 28 references, 31 range starts, and 28 range ends.
- Tracked changes are represented by 53 `w:ins` elements and 14 `w:del` elements in `word/document.xml`. They are retained in `working/document.md` with `⟦INSERTED ...⟧` and `⟦DELETED ...⟧` markers.
- No `word/footnotes.xml` or `word/endnotes.xml` part and no footnote/endnote reference was present. Seven VML `w:pict` horizontal rules were rendered as `---`; no embedded image part was present.
- Same-anchor comment pairs are listed as probable replies only where the shared anchor makes that plausible. This is an inference, not an OOXML fact.

## Comment records

### [COMMENT-001] (OOXML ID `0`)

- Author: Arnold Hubach
- Date: 2026-07-20 11:07 UTC
- Anchor status: balanced lexical anchor
- Appears resolved: likely yes from the acknowledgment reply; no explicit resolved flag

Attached text exactly as recovered from the comment range:

```text
open-source
```

Comment:

```text
get consistency in document between open-source and open source
```

Replies (probable from shared anchor/order; no explicit parent/reply field): [COMMENT-002]

### [COMMENT-002] (OOXML ID `1`)

- Author: Pablo Saxtron
- Date: 2026-07-24 04:43 UTC
- Anchor status: balanced lexical anchor
- Appears resolved: unclear (same-anchor follow-up exists; no explicit resolved flag)

Attached text exactly as recovered from the comment range:

```text
open-source
```

Comment:

```text
Good catch
```

Reply status (probable from shared anchor/order; no explicit parent/reply field): follow-up to [COMMENT-001]

### [COMMENT-003] (OOXML ID `2`)

- Author: Gabriel Palma
- Date: 2026-07-17 21:16 UTC
- Anchor status: balanced lexical anchor
- Appears resolved: likely yes from the acknowledgment reply; no explicit resolved flag

Attached text exactly as recovered from the comment range:

```text
assets
```

Comment:

```text
little nitpick, but maybe tokens is a better word here? I've always been triggered by the whole digital asset wording because it seems to give legitimacy to other cryptos. Maybe it's just me.
```

Replies (probable from shared anchor/order; no explicit parent/reply field): [COMMENT-004]

### [COMMENT-004] (OOXML ID `3`)

- Author: Pablo Saxtron
- Date: 2026-07-22 22:06 UTC
- Anchor status: balanced lexical anchor
- Appears resolved: unclear (same-anchor follow-up exists; no explicit resolved flag)

Attached text exactly as recovered from the comment range:

```text
assets
```

Comment:

```text
Solid point
```

Reply status (probable from shared anchor/order; no explicit parent/reply field): follow-up to [COMMENT-003]

### [COMMENT-005] (OOXML ID `4`)

- Author: Larry Spraker
- Date: 2026-07-15 11:33 UTC
- Anchor status: balanced lexical anchor
- Appears resolved: no reply or resolution state represented

Attached text exactly as recovered from the comment range:

```text
Broken Money
```

Comment:

```text
Fiat isn't described until later, so I suggest not using the term yet
```

Replies: none represented in the package.

### [COMMENT-006] (OOXML ID `5`)

- Author: Larry Spraker
- Date: 2026-07-15 11:40 UTC
- Anchor status: balanced lexical anchor
- Appears resolved: no reply or resolution state represented

Attached text exactly as recovered from the comment range:

```text
money
```

Comment:

```text
Similar comment as earlier, since we haven't defined Fiat yet, we should hold off on using it. I am constantly told by people they have never heard that term.
```

Replies: none represented in the package.

### [COMMENT-007] (OOXML ID `6`)

- Author: Larry Spraker
- Date: 2026-07-15 11:45 UTC
- Anchor status: balanced lexical anchor
- Appears resolved: no reply or resolution state represented

Attached text exactly as recovered from the comment range:

```text
 (under President Richard Nixon)
```

Comment:

```text
Adding this to give context to the term Nixon Shock
```

Replies: none represented in the package.

### [COMMENT-008] (OOXML ID `7`)

- Author: Larry Spraker
- Date: 2026-07-15 11:54 UTC
- Anchor status: 2 range starts for this ID
- Appears resolved: unclear (same-anchor follow-up exists; no explicit resolved flag)

Attached text exactly as recovered from the comment range:

```text
 (
```

Comment:

```text
Adding here to clarify our use of the term
```

Replies (probable from shared anchor/order; no explicit parent/reply field): [COMMENT-009]

### [COMMENT-009] (OOXML ID `8`)

- Author: Pablo Saxtron
- Date: 2026-07-15 15:28 UTC
- Anchor status: 2 range starts for this ID
- Appears resolved: unclear (same-anchor follow-up exists; no explicit resolved flag)

Attached text exactly as recovered from the comment range:

```text
 (
```

Comment:

```text
I agree - the definition comes up later, but needs to be here. I'd like to have a breakout section in the Diploma to draw the eye.
```

Reply status (probable from shared anchor/order; no explicit parent/reply field): follow-up to [COMMENT-008]

### [COMMENT-010] (OOXML ID `9`)

- Author: Gabriel Palma
- Date: 2026-07-20 16:05 UTC
- Anchor status: balanced lexical anchor
- Appears resolved: likely yes from the acknowledgment reply; no explicit resolved flag

Attached text exactly as recovered from the comment range:

```text
beginner level
```

Comment:

```text
Would "surface level" make more sense here?
```

Replies (probable from shared anchor/order; no explicit parent/reply field): [COMMENT-011]

### [COMMENT-011] (OOXML ID `10`)

- Author: Pablo Saxtron
- Date: 2026-07-22 16:11 UTC
- Anchor status: balanced lexical anchor
- Appears resolved: unclear (same-anchor follow-up exists; no explicit resolved flag)

Attached text exactly as recovered from the comment range:

```text
beginner level
```

Comment:

```text
Yes it would - thanks, Gabe!
```

Reply status (probable from shared anchor/order; no explicit parent/reply field): follow-up to [COMMENT-010]

### [COMMENT-012] (OOXML ID `11`)

- Author: Larry Spraker
- Date: 2026-07-15 12:04 UTC
- Anchor status: balanced lexical anchor
- Appears resolved: no reply or resolution state represented

Attached text exactly as recovered from the comment range:

```text
A person who owns an asset that rises in price may be partly protected. 
```

Comment:

```text
Perhaps add a section after this one on the Cantillon effect to expand on this concept
```

Replies: none represented in the package.

### [COMMENT-013] (OOXML ID `12`)

- Author: Larry Spraker
- Date: 2026-07-15 12:13 UTC
- Anchor status: balanced lexical anchor
- Appears resolved: no reply or resolution state represented

Attached text exactly as recovered from the comment range:

```text
Central Bank Digital Currencies (CBDCs)CBDCs as a beginner fiat-system example where appropriate
A central bank digital currency, or CBDC, is a digital form of fiat money issued as a liability of a central bank. It is different from physical cash and from a normal commercial-bank deposit, although the user experience may look similar.

CBDC designs differ. Some are intended mainly for financial institutions. Others are proposed for public use. Depending on the design, a CBDC may allow faster settlement, wider access, or new payment features. It may also give institutions greater ability to monitor transactions, apply rules, limit use, or connect identity directly to payments.

A CBDC does not create a fixed monetary supply or remove central control. It changes the technology and distribution of fiat money. The central bank remains the issuer and can still apply monetary policy.

When discussing a CBDC, ask:

Who issues the money?
Who can hold or use it?
What information is collected?
Can a payment be blocked, limited, or reversed?
Can the rules change?
What happens without electricity or internet access?
What legal protections exist?

Do not assume that every proposed CBDC has the same design. Use current, local, and reliable information.
```

Comment:

```text
I would move this down after the next section to be the last in this block. I would also make it much "harsher" to communicate how "evil" these can be as a surveillance and control mechanism that tracks our purchases and As programmable money can be used to confiscate. or limit our ability to spend by category, time or geography etc.
```

Replies: none represented in the package.

### [COMMENT-014] (OOXML ID `13`)

- Author: Larry Spraker
- Date: 2026-07-15 12:17 UTC
- Anchor status: balanced lexical anchor
- Appears resolved: no reply or resolution state represented

Attached text exactly as recovered from the comment range:

```text
Review: what problem does fiat money create?
Fiat money is useful because it is widely accepted, familiar, and integrated into modern economies. Its main monetary rules, however, are managed by central institutions. Its supply can expand, access depends on intermediaries, and its purchasing power can decline.

Complete these statements in your own words:

Money exists because...
The three functions of money are...
Barter becomes difficult because...
Fiat money depends on...
Fractional reserve banking means...
Inflation matters to a saver because...
People look for monetary alternatives because...

Block 1 answer: The central problem is that people must use a monetary system whose supply, access, and rules are controlled by institutions they must trust. This does not mean fiat money has no benefits. It means its users bear risks created by changing policy, institutional failure, restricted access, and loss of purchasing power.

The next block examines Bitcoin's attempt to create a different set of monetary rules.
```

Comment:

```text
Questions and review like this are good for younger students but are often viewed by older American adults as unnecessary (e.g., GenX/Boomers).
```

Replies: none represented in the package.

### [COMMENT-015] (OOXML ID `14`)

- Author: Larry Spraker
- Date: 2026-07-15 12:38 UTC
- Anchor status: balanced lexical anchor
- Appears resolved: no reply or resolution state represented

Attached text exactly as recovered from the comment range:

```text
Transactions are announced to a peer-to-peer network.
Miners collect valid transactions into blocks and use proof of work to propose their order.
Nodes independently check each block against the same rules.
The valid chain with the most accumulated proof of work becomes the accepted history.
```

Comment:

```text
IMO, I think this is too early to get into the full method as described here, and needs to be moved later. Too many new terms such as miners, nodes, chains, and POW that should each be slowly introduced first. I think the key here is to simply mention spin off the double spend and centralized system comments and emphasize that Bitcoin uses a decentralized approach with many other key principles to solve the double spend problem. I've added a few sections below to help if you like.
```

Replies: none represented in the package.

### [COMMENT-016] (OOXML ID `15`)

- Author: Larry Spraker
- Date: 2026-07-15 12:48 UTC
- Anchor status: balanced lexical anchor
- Appears resolved: no reply or resolution state represented

Attached text exactly as recovered from the comment range:

```text
Bitcoin origin timeline
Bitcoin appeared through a short series of public events.

Date
Event
Why it matters
31 October 2008
Satoshi Nakamoto published the whitepaper Bitcoin: A Peer-to-Peer Electronic Cash System.
The paper described direct online payments without a financial intermediary.
3 January 2009
Satoshi created the Genesis Block, the first block in Bitcoin's chain.
The Bitcoin network began. The block included a newspaper headline about bank bailouts, placing the launch in the context of the financial crisis.
12 January 2009
Satoshi sent bitcoin to Hal Finney in the first recorded person-to-person Bitcoin transaction.
The software moved value between two participants as designed.
22 May 2010
A user paid 10,000 bitcoin for two pizzas.
The event showed bitcoin being exchanged for ordinary goods and is remembered as Bitcoin Pizza Day.

Satoshi Nakamoto is the name used by Bitcoin's creator. Satoshi communicated online, released the software as open source, and later stopped participating. Satoshi's real-world identity remains unknown.

No central company owns Bitcoin. The software and rules continued because other people chose to run, review, and develop them. This origin matters: the creator did not remain as a permanent leader who could issue more coins or approve transactions.

The Genesis Block and the 2008 financial crisis give Bitcoin important historical context. However, evaluate Bitcoin by its design and operation, not only by a story about its creator.
```

Comment:

```text
I would consider moving this later to flow right into Decentralization and staying on the theme of introducing how Bitcoin works
```

Replies: none represented in the package.

### [COMMENT-017] (OOXML ID `16`)

- Author: Larry Spraker
- Date: 2026-07-15 13:05 UTC
- Anchor status: 2 range starts for this ID
- Appears resolved: no reply or resolution state represented

Attached text exactly as recovered from the comment range:

```text
The Blockchain - Bitcoin’s Public Ledger
Unlike banks, who each have their own ledger of transactions and must coordinate with each other, Bitcoin is recorded and stored in a SINGLE, digital, decentralized, public ledger. This ledger is stored in a data format referred to as a “blockchain”. 

A block contains a series of transactions (in order), and each block is like a page in a ledger. Transactions within each block are in precise, choronological order and blocks are also sequenced and “chained” together in chronological order.

Bitcoin is designed to add a new block of transactions to the blockchain approximately every 10 minutes.
```

Comment:

```text
I think it's important to introduce the Blockchain, the network, miners/nodes at this point to help position for later text that refer to these.
```

Replies: none represented in the package.

### [COMMENT-018] (OOXML ID `17`)

- Author: Larry Spraker
- Date: 2026-07-15 15:33 UTC
- Anchor status: balanced lexical anchor
- Appears resolved: no reply or resolution state represented

Attached text exactly as recovered from the comment range:

```text
nyone can download and inspect the open-source software;
users can transact without opening an account with the Bitcoin network;
independent nodes check transactions and blocks;
miners compete to propose blocks;
no miner can make an invalid block acceptable to honest nodes;
changes to the rules require voluntary adoption by participants;
the ledger is copied across many computers and locations.
```

Comment:

```text
By adding the sections on the Bitcoin blockchain and network above, it enables the use of the terminology here (blocks, miners, nodes etc.), without getting too deep.
```

Replies: none represented in the package.

### [COMMENT-019] (OOXML ID `18`)

- Author: Larry Spraker
- Date: 2026-07-15 15:40 UTC
- Anchor status: balanced lexical anchor
- Appears resolved: no reply or resolution state represented

Attached text exactly as recovered from the comment range:

```text
Bitcoin network
```

Comment:

```text
This now works better since we added the new section above
```

Replies: none represented in the package.

### [COMMENT-020] (OOXML ID `19`)

- Author: Larry Spraker
- Date: 2026-07-15 15:37 UTC
- Anchor status: balanced lexical anchor
- Appears resolved: no reply or resolution state represented

Attached text exactly as recovered from the comment range:

```text
E
```

Comment:

```text
It's exactly 210,000 blocks, the term roughly every 4 years works well
```

Replies: none represented in the package.

### [COMMENT-021] (OOXML ID `20`)

- Author: Larry Spraker
- Date: 2026-07-15 15:39 UTC
- Anchor status: balanced lexical anchor
- Appears resolved: no reply or resolution state represented

Attached text exactly as recovered from the comment range:

```text
Deeper Dive into 
```

Comment:

```text
Added "Deeper Dive" since we already introduced the one liners earlier
```

Replies: none represented in the package.

### [COMMENT-022] (OOXML ID `21`)

- Author: Larry Spraker
- Date: 2026-07-15 15:48 UTC
- Anchor status: balanced lexical anchor
- Appears resolved: no reply or resolution state represented

Attached text exactly as recovered from the comment range:

```text
Wallets
A Bitcoin wallet is a tool for managing cryptographic keys, creating receiving information, checking balances, and signing transactions. It may be an application, a dedicated hardware device, or a coordinated service.
```

Comment:

```text
I recommend pulling some of the basic wallet intro text up under the Blockchain and Network sections I added above just to complete the intro loop at a high level of miners/nodes/wallets so that subsequent use of terms like keys, etc makes more sense.
```

Replies: none represented in the package.

### [COMMENT-023] (OOXML ID `22`)

- Author: Arnold Hubach
- Date: 2026-07-20 11:11 UTC
- Anchor status: balanced lexical anchor
- Appears resolved: likely yes from the acknowledgment reply; no explicit resolved flag

Attached text exactly as recovered from the comment range:

```text
no-KYC
```

Comment:

```text
consistency: no-KYC and non-KYC
```

Replies (probable from shared anchor/order; no explicit parent/reply field): [COMMENT-024]

### [COMMENT-024] (OOXML ID `23`)

- Author: Pablo Saxtron
- Date: 2026-07-24 04:45 UTC
- Anchor status: balanced lexical anchor
- Appears resolved: unclear (same-anchor follow-up exists; no explicit resolved flag)

Attached text exactly as recovered from the comment range:

```text
no-KYC
```

Comment:

```text
Good catch
```

Reply status (probable from shared anchor/order; no explicit parent/reply field): follow-up to [COMMENT-023]

### [COMMENT-025] (OOXML ID `24`)

- Author: Arnold Hubach
- Date: 2026-07-20 11:11 UTC
- Anchor status: balanced lexical anchor
- Appears resolved: no reply or resolution state represented

Attached text exactly as recovered from the comment range:

```text
Contribute. Share feedback, improve a translation, support an educator, or help another learner understand a concept safely.
```

Comment:

```text
Volunteer
```

Replies: none represented in the package.

### [COMMENT-026] (OOXML ID `25`)

- Author: Arnold Hubach
- Date: 2026-07-20 11:12 UTC
- Anchor status: anchor contains no lexical text
- Appears resolved: no reply or resolution state represented

Attached text exactly as recovered from the comment range:

```text


```

The range contains only whitespace or a paragraph boundary, so it cannot be reliably matched to a lexical document phrase.

Comment:

```text
Add here CTA's for people to sign up via one of the forms:ProofreadVolunteerFeedbackSign up ETPetchttps://forms.myfirstbitcoin.org/
```

Replies: none represented in the package.

### [COMMENT-027] (OOXML ID `26`)

- Author: Arnold Hubach
- Date: 2026-07-20 11:13 UTC
- Anchor status: anchor contains no lexical text
- Appears resolved: no reply or resolution state represented

Attached text exactly as recovered from the comment range:

```text


```

The range contains only whitespace or a paragraph boundary, so it cannot be reliably matched to a lexical document phrase.

Comment:

```text
There is nothing about the Education Network or about the ETP right now, as next steps. I think that is crucial...And also: the case studies are gone. While I think that was a powerful story to add to the end? We can work on more Case Studies with Leaderboard Perks: https://leaderboard.myfirstbitcoin.org/ the https://leaderboard.myfirstbitcoin.org/
```

Replies: none represented in the package.

### [COMMENT-028] (OOXML ID `27`)

- Author: Arnold Hubach
- Date: 2026-07-20 11:14 UTC
- Anchor status: balanced lexical anchor
- Appears resolved: no reply or resolution state represented

Attached text exactly as recovered from the comment range:

```text
O
```

Comment:

```text
Add: Contribute to Resources Hub as well. We need CTA's to gamify people.Also: CTA to install/download the app (if they didnt yet)
```

Replies: none represented in the package.

## Matching limitations

The following comments cannot be reliably matched to a normal lexical range because the export has malformed or non-lexical anchors:

- [COMMENT-008] (OOXML ID `7`): 2 range starts for this ID; recovered anchor `' ('`.
- [COMMENT-009] (OOXML ID `8`): 2 range starts for this ID; recovered anchor `' ('`.
- [COMMENT-017] (OOXML ID `16`): 2 range starts for this ID; recovered anchor `'The Blockchain - Bitcoin’s Public Ledger\nUnlike banks, who each have their own ledger of transactions and must coordinate with each other, Bitcoin is recorded and stored in a SINGLE, digital, decentralized, public ledger. This ledger is stored in a data format referred to as a “blockchain”. \n\nA block contains a series of transactions (in order), and each block is like a page in a ledger. Transactions within each block are in precise, choronological order and blocks are also sequenced and “chained” together in chronological order.\n\nBitcoin is designed to add a new block of transactions to the blockchain approximately every 10 minutes.'`.
- [COMMENT-026] (OOXML ID `25`): anchor contains no lexical text; recovered anchor `'\n'`.
- [COMMENT-027] (OOXML ID `26`): anchor contains no lexical text; recovered anchor `'\n'`.

## Extraction checks

- Comment records extracted: 28.
- Visible comment markers emitted in `document.md`: 28.
- Inserted-change markers emitted: 53 expected; deleted-change markers emitted: 14 expected.
- Non-text or unsupported content handling: w:pict (VML horizontal rule) rendered as --- (7).

No proposed reviewer changes were implemented.
