# Lexicon

## Dashboard

| Measure | Count |
| --- | ---: |
| Lexicon entries | 247 |
| Student Guide (SG) references | 28 |
| Student Guide term entries found | 136 |
| Outdated Student Guide traces | 2 |
| Educator Guide (EG) references | 637 |
| Educator Guide linked entries | 106 |
| Outdated Educator Guide traces | 0 |
| Activities (ACT) references | 25 |
| Advanced (ADV) references | 0 |
| Assessment grid references | 0 |
| Quick Start references | 0 |
| Microlearning references | 0 |
| **Published-material references** | **690** |

Reference counts are direct Markdown links to a lexicon-term anchor in the current `publish/` materials, counted on 1 October 2026. “Lexicon entries” counts word-or-phrase rows rather than individual aliases. “Term entries found” counts entries with at least one current Student Guide match; “linked entries” counts entries with at least one current Educator Guide link.

This lexicon lists Bitcoin and Bitcoin-adjacent terms that a beginner may need explained. It is the shared terminology authority for the Student Guide, Educator Guide, and Diploma activities. Each entry has a stable anchor for links from those materials.

Link a term only when it is used in a Bitcoin, economic, or computing sense and the linked definition explains that specific use. Leave ordinary English uses and incidental word matches unlinked; use the more specific entry when one exists, such as Lightning liquidity for channel capacity.

For **privacy**, link only uses where the word is a noun in its own right (for example, `protect privacy` or `financial privacy`). Do not link attributive uses that modify another noun, including shared modifiers in lists (for example, `privacy risks` or `privacy and safety boundaries`).

Line references are a snapshot of the current [Student Guide](mfb-bd-26.10/mfb-bd-sg-26.10.md): **First** is the earliest matching term or listed alias; **Later** lists subsequent matching lines, including headings and regular plural forms. Longer listed phrases take precedence over terms within them. `Not present` means no matching form was found. `Outdated` means an earlier snapshot recorded the term but the current guide no longer contains a matching use.

The Educator Guide column links to the section containing the first linked use and counts linked mentions in body text and tables. Diploma activities use the same anchors where a term needs definition; activity-linked terms are validated against this lexicon. Headings, existing links, and ordinary uses with a different meaning are not relinked; `No linked use` means there is no linked occurrence in those contexts. `Outdated` means an earlier linked use is no longer present in the current Educator Guide.

Guide traceability was refreshed on 1 October 2026 from the published guides. Run `python3 tools/refresh_lexicon.py --check` after guide edits to audit the snapshot and linked-use metadata.

## Module 1: Understanding Money

### Functions and properties of money

| Word or phrase | LEX-ID | Beginner definition | Student Guide line(s) | Educator Guide use |
| --- | --- | --- | --- | --- |
| <a id="term-medium-of-exchange"></a>**Medium of exchange** |  | Something people accept in payment for goods and services. | First: **298**<br>Later: 594, 895 | [First linked use](mfb-bd-26.10/mfb-bd-eg-26.10.md#prepare-before-class); 2 linked mentions |
| <a id="term-unit-of-account"></a>**Unit of account** |  | A shared unit used to state and compare prices, debts, income, and costs. | First: **300**<br>Later: 434, 451, 594, 896 | [First linked use](mfb-bd-26.10/mfb-bd-eg-26.10.md#prepare-before-class); 3 linked mentions |
| <a id="term-store-of-value"></a>**Store of value** |  | A way of carrying purchasing power from the present into the future. | First: **302**<br>Later: 594, 894 | [First linked use](mfb-bd-26.10/mfb-bd-eg-26.10.md#prepare-before-class); 4 linked mentions |
| <a id="term-durability"></a>**Durability** |  | The ability of money to remain usable over time. | First: **310**<br>Later: 595, 879 | [First linked use](mfb-bd-26.10/mfb-bd-eg-26.10.md#functions-and-properties-of-money); 3 linked mentions |
| <a id="term-portability"></a>**Portability** |  | The ease of moving or transferring money from one person or place to another. | First: **311**<br>Later: 536, 595, 880 | [First linked use](mfb-bd-26.10/mfb-bd-eg-26.10.md#functions-and-properties-of-money); 3 linked mentions |
| <a id="term-divisibility"></a>**Divisibility** |  | The ability to divide money into smaller units for different-sized payments. | First: **312**<br>Later: 595, 881 | [First linked use](mfb-bd-26.10/mfb-bd-eg-26.10.md#functions-and-properties-of-money); 4 linked mentions |
| <a id="term-uniformity"></a>**Uniformity** |  | The degree to which equal units of money are consistent in form and value. | Not present | No linked use |
| <a id="term-fungibility"></a>**Fungibility** |  | The property that equal units are normally interchangeable. | First: **313**<br>Later: 882 | [First linked use](mfb-bd-26.10/mfb-bd-eg-26.10.md#functions-and-properties-of-money); 3 linked mentions |
| <a id="term-scarcity"></a>**Scarcity** |  | A limited supply: using or obtaining more is constrained rather than unlimited. | First: **314**<br>Later: 364, 368, 370, 392, 595, 654, 683, 687, 689, 691, 693, 883 | [First linked use](mfb-bd-26.10/mfb-bd-eg-26.10.md#suggested-two-hour-flow); 12 linked mentions |
| <a id="term-acceptability"></a>**Acceptability** |  | The willingness of other people to receive something in exchange. | First: **315**<br>Later: 595, 885 | [First linked use](mfb-bd-26.10/mfb-bd-eg-26.10.md#functions-and-properties-of-money); 4 linked mentions |
| <a id="term-verifiability"></a>**Verifiability** |  | The ability to check that money is genuine or that a transaction follows the rules. | First: **316**<br>Later: 595, 884 | [First linked use](mfb-bd-26.10/mfb-bd-eg-26.10.md#functions-and-properties-of-money); 3 linked mentions |
| <a id="term-recognizability"></a>**Recognizability / “likeness”** |  | How easily people can identify a form of money and recognize authentic or equivalent units. | Not present | No linked use |
| <a id="gold"></a>**Gold** |  | A scarce, durable metal used for jewelry, industry, and money. It has served as coins, backing for currencies, and a store of value. | First: **330**<br>Later: 403, 407, 409, 424, 523, 525, 527, 544 | [First linked use](mfb-bd-26.10/mfb-bd-eg-26.10.md#fiat-money-and-the-local-system); 2 linked mentions |
| <a id="paper-cash"></a>**Paper Cash** |  | Physical banknotes used to pay for goods and services in person. They represent stated currency amounts and can pass directly from one person to another. | First: **330**<br>Later: — | No linked use |

### Barter and the double coincidence of wants

| Word or phrase | LEX-ID | Beginner definition | Student Guide line(s) | Educator Guide use |
| --- | --- | --- | --- | --- |
| <a id="term-barter"></a>**Barter / bartering** |  | The direct exchange of one good or service for another without using money. | First: **298**<br>Later: 334, 336, 338, 347, 349, 394, 401, 589, 596 | [First linked use](mfb-bd-26.10/mfb-bd-eg-26.10.md#t1--money-comparison-and-local-scenario-c1); 11 linked mentions |
| <a id="term-double-coincidence-of-wants"></a>**Double coincidence of wants** |  | The barter problem in which each person must want what the other offers at the same time. | First: **334**<br>Later: 347 | No linked use |
| <a id="term-most-saleable-good"></a>**Most saleable good** |  | The good that people are most willing to accept in exchange because they expect others will accept it too. | Not present | No linked use |
| <a id="term-auction"></a>**Auction** |  | A process in which goods or assets are sold to the highest bidder. | Not present | No linked use |

### Scarcity, value, and exchange

| Word or phrase | LEX-ID | Beginner definition | Student Guide line(s) | Educator Guide use |
| --- | --- | --- | --- | --- |
| <a id="term-subjective-value"></a>**Subjective value** |  | The idea that value depends on a person’s needs, preferences, information, and circumstances. | Not present | [First linked use](mfb-bd-26.10/mfb-bd-eg-26.10.md#bitcoin-as-sound-digital-money); 1 linked mention |
| <a id="term-opportunity-cost"></a>**Opportunity cost** |  | The best alternative given up when a choice is made. | First: **383**<br>Later: 551 | [First linked use](mfb-bd-26.10/mfb-bd-eg-26.10.md#suggested-two-hour-flow); 3 linked mentions |
| <a id="term-time-preference"></a>**Time preference** |  | How strongly someone prefers value now rather than later. | First: **384**<br>Later: — | [First linked use](mfb-bd-26.10/mfb-bd-eg-26.10.md#scarcity-value-and-exchange); 2 linked mentions |
| <a id="term-supply-and-demand"></a>**Supply and demand** |  | The relationship between how much of something is available and how much people want it, which can influence its price. | Not present | No linked use |
| <a id="term-time-value-of-money"></a>**Time value of money** |  | The idea that receiving money now and receiving the same amount later can have different value. | Not present | No linked use |
| <a id="term-trade-off"></a>**Trade-off** |  | A choice that gains one benefit while accepting a cost or giving up another benefit. | First: **36**<br>Later: 46, 91, 117, 123, 385, 418, 533, 589, 597, 600, 733, 898, 902, 976, 978, 1044, 1153, 1190, 1301, 1351, 1413, 1706, 1713, 1863, 1864 | No linked use |

### Beginner monetary history from barter to modern money

| Word or phrase | LEX-ID | Beginner definition | Student Guide line(s) | Educator Guide use |
| --- | --- | --- | --- | --- |
| <a id="term-commodity-money"></a>**Commodity money** |  | Money made from or represented by a good that has use or value beyond an issuer’s promise. | First: **403**<br>Later: — | [First linked use](mfb-bd-26.10/mfb-bd-eg-26.10.md#beginner-monetary-history); 1 linked mention |
| <a id="term-standard-coins"></a>**Standard coins** |  | Metal coins made to a recognized weight and value by an authority. | First: **405**<br>Later: — | No linked use |
| <a id="term-representative-paper"></a>**Representative paper** |  | Paper that can be redeemed for a stated amount of an asset, historically often metal. | First: **407**<br>Later: — | [First linked use](mfb-bd-26.10/mfb-bd-eg-26.10.md#beginner-monetary-history); 1 linked mention |
| <a id="term-paper-claim"></a>**Paper claim** |  | A paper record representing a claim on an issuer for a stated asset or amount. | First: **407**<br>Later: — | No linked use |
| <a id="term-debasement"></a>**Debasement** |  | Reducing a coin’s valuable-metal content while keeping its stated value the same. | First: **405**<br>Later: — | [First linked use](mfb-bd-26.10/mfb-bd-eg-26.10.md#beginner-monetary-history); 1 linked mention |
| <a id="term-executive-order-6102"></a>**Executive Order 6102** |  | A 1933 U.S. order that restricted private gold ownership in a particular historical and legal context. | Not present | [First linked use](mfb-bd-26.10/mfb-bd-eg-26.10.md#beginner-monetary-history); 2 linked mentions |
| <a id="term-gold-standard"></a>**Gold Standard** |  | A monetary system in which currency can be exchanged for a fixed amount of gold. | First: **407**<br>Later: — | [First linked use](mfb-bd-26.10/mfb-bd-eg-26.10.md#beginner-monetary-history); 1 linked mention |
| <a id="term-bretton-woods"></a>**Bretton Woods** |  | The post-1944 international monetary arrangement that linked currencies to the U.S. dollar and the dollar to gold. | First: **525**<br>Later: 527 | [First linked use](mfb-bd-26.10/mfb-bd-eg-26.10.md#beginner-monetary-history); 2 linked mentions |
| <a id="term-nixon-shock"></a>**Nixon Shock** |  | The 1971 U.S. decision that ended international dollar-to-gold convertibility. | Not present | [First linked use](mfb-bd-26.10/mfb-bd-eg-26.10.md#beginner-monetary-history); 1 linked mention |
| <a id="term-convertibility"></a>**Convertibility** |  | The ability to exchange one form of money for another asset at a stated rate. | First: **407**<br>Later: — | [First linked use](mfb-bd-26.10/mfb-bd-eg-26.10.md#beginner-monetary-history); 3 linked mentions |
| <a id="term-fiat-money"></a>**Fiat money** |  | Money issued under state authority whose value is not fixed to redemption in a scarce commodity. | First: **409**<br>Later: 420, 422, 424, 426, 459, 561, 565, 572, 589, 598, 904, 1308 | [First linked use](mfb-bd-26.10/mfb-bd-eg-26.10.md#beginner-monetary-history); 3 linked mentions |
| <a id="term-by-decree"></a>**“By decree”** |  | By an official order from an authority. | **Outdated:** no match in current Student Guide | No linked use |
| <a id="term-account-claim"></a>**Account claim** |  | A recorded promise that an institution owes the account holder money or another asset. | Not present | No linked use |
| <a id="term-bank-deposit"></a>**Bank deposit** |  | Money recorded as a claim on a commercial bank, rather than physical cash held separately for the customer. | First: **411**<br>Later: 637 | [First linked use](mfb-bd-26.10/mfb-bd-eg-26.10.md#strong-module-1-questions); 4 linked mentions |
| <a id="term-central-bank"></a>**Central bank (Fed)** |  | A public institution that manages a country’s monetary policy. The U.S. central bank is commonly called the Federal Reserve, or Fed. | First: **409**<br>Later: 424, 432, 459, 488, 523, 527, 561, 565 | No linked use |
| <a id="term-capital-controls"></a>**Capital controls** |  | Restrictions on moving money across borders. | Not present | No linked use |
| <a id="term-exchange-rate"></a>**Exchange rate** |  | The value of one currency in relation to another. | First: **1309**<br>Later: 1595, 1633, 1694 | No linked use |
| <a id="term-network-effect"></a>**Network effect** |  | A situation in which something becomes more useful as more people use it. | First: **426**<br>Later: — | [First linked use](mfb-bd-26.10/mfb-bd-eg-26.10.md#why-the-us-dollar-is-a-reserve-currency); 3 linked mentions |

### Fractional reserve banking

| Word or phrase | LEX-ID | Beginner definition | Student Guide line(s) | Educator Guide use |
| --- | --- | --- | --- | --- |
| <a id="term-deposit-money"></a>**Deposit money** |  | Commercial-bank account money. | First: **433**<br>Later: 465 | No linked use |
| <a id="term-bank-money-creation"></a>**Bank money creation** |  | The creation of a matching bank deposit when a commercial bank approves a loan. | Not present | No linked use |
| <a id="term-liability"></a>**Liability** |  | Something a person or institution owes; a bank deposit is a liability the bank owes its customer. | First: **463**<br>Later: 561 | [First linked use](mfb-bd-26.10/mfb-bd-eg-26.10.md#fractional-reserve-banking-liquidity-and-solvency); 5 linked mentions |
| <a id="term-fractional-reserve-banking"></a>**Fractional reserve banking** |  | Banking in which only part of deposit obligations is kept immediately available as reserves. | First: **461**<br>Later: 474, 476, 599 | No linked use |
| <a id="term-reserve-ratio"></a>**Reserve ratio** |  | The share of deposits a bank keeps as reserves rather than lending or investing. | Not present | No linked use |
| <a id="term-liquid-assets"></a>**Liquid assets** |  | Assets, such as cash or reserves, that can be used or converted to cash quickly. | Not present | No linked use |
| <a id="term-liquidity"></a>**Liquidity** |  | The ability to meet payments or withdrawals promptly using cash or liquid assets. | First: **465**<br>Later: 920, 1365, 1723 | [First linked use](mfb-bd-26.10/mfb-bd-eg-26.10.md#prepare-before-class); 15 linked mentions |
| <a id="term-liquidity-risk"></a>**Liquidity risk** |  | The danger that a person or institution will not have enough readily available funds when needed. | First: **480**<br>Later: — | [First linked use](mfb-bd-26.10/mfb-bd-eg-26.10.md#fractional-reserve-banking-liquidity-and-solvency); 1 linked mention |
| <a id="term-capital"></a>**Capital** |  | A bank's loss-absorbing funding, such as owner funding and retained earnings. | First: **465**<br>Later: — | [First linked use](mfb-bd-26.10/mfb-bd-eg-26.10.md#prepare-before-class); 5 linked mentions |
| <a id="term-solvency"></a>**Solvency** |  | Having assets sufficient to cover obligations. | Not present | [First linked use](mfb-bd-26.10/mfb-bd-eg-26.10.md#suggested-two-hour-flow); 6 linked mentions |
| <a id="term-solvency-risk"></a>**Solvency risk** |  | The danger that an institution’s assets will not cover what it owes. | First: **481**<br>Later: — | [First linked use](mfb-bd-26.10/mfb-bd-eg-26.10.md#fractional-reserve-banking-liquidity-and-solvency); 1 linked mention |
| <a id="term-credit-risk"></a>**Credit risk** |  | The risk that a borrower will not repay what is owed. | First: **465**<br>Later: — | [First linked use](mfb-bd-26.10/mfb-bd-eg-26.10.md#fractional-reserve-banking-liquidity-and-solvency); 1 linked mention |
| <a id="term-funding-cost"></a>**Funding cost** |  | What a bank pays to obtain money. | Not present | No linked use |
| <a id="term-qualified-borrower"></a>**Qualified borrower** |  | A borrower who meets a lender’s standards for a loan. | First: **465**<br>Later: — | No linked use |
| <a id="term-bank-capital-rules"></a>**Bank capital rules** |  | Rules requiring banks to fund risks with capital that can absorb losses. | Not present | No linked use |
| <a id="term-bank-regulation"></a>**Bank regulation** |  | Rules and supervision that govern banks. | Not present | No linked use |
| <a id="term-restrictive-banking"></a>**Restrictive banking** |  | Restrictions or limitations on banking services or access to banking services. | Not present | No linked use |
| <a id="term-bank-profit"></a>**Bank profit** |  | Income remaining after a bank’s costs and losses. | Not present | No linked use |
| <a id="term-deposit-insurance"></a>**Deposit insurance** |  | A system that protects eligible bank deposits up to stated limits if a bank fails. | First: **488**<br>Later: — | [First linked use](mfb-bd-26.10/mfb-bd-eg-26.10.md#local-banking-discussion); 1 linked mention |
| <a id="term-gearing"></a>**Gearing** |  | Using borrowed money or obligations to increase the size of assets or financial exposure. | Not present | No linked use |
| <a id="term-bank-run"></a>**Bank run** |  | A rush of many customers trying to withdraw funds because they fear a bank may fail. | First: **488**<br>Later: — | [First linked use](mfb-bd-26.10/mfb-bd-eg-26.10.md#debrief-every-activity); 1 linked mention |
| <a id="term-moral-hazard"></a>**Moral hazard** |  | A situation in which protection from loss can encourage someone to take more risk because others may bear the cost. | Not present | No linked use |
| <a id="term-too-big-to-fail"></a>**“Too big to fail”** |  | The view that an institution is so important that authorities may intervene to prevent its disorderly failure. | Not present | No linked use |
| <a id="term-restructuring"></a>**Restructuring** |  | Changing debts, ownership, or operations to help an institution continue or resolve failure. | Not present | No linked use |

### Inflation and purchasing power

| Word or phrase | LEX-ID | Beginner definition | Student Guide line(s) | Educator Guide use |
| --- | --- | --- | --- | --- |
| <a id="term-inflation"></a>**Inflation** |  | A sustained increase in the general price level, so a unit of money buys less. | First: **494**<br>Later: 509, 511, 513, 519, 599 | [First linked use](mfb-bd-26.10/mfb-bd-eg-26.10.md#one-to-two-weeks-before); 21 linked mentions |
| <a id="term-money-supply"></a>**Money supply** |  | The total amount of money or money-like balances counted within a stated economy or measure. | Not present | No linked use |
| <a id="term-monetary-inflation"></a>**Monetary inflation** |  | An increase in the money supply. It is distinct from price inflation, which is a sustained increase in the general price level. | Not present | No linked use |
| <a id="term-price-inflation"></a>**Price inflation** |  | A sustained increase in the general price level of goods and services. | First: **496**<br>Later: 498 | [First linked use](mfb-bd-26.10/mfb-bd-eg-26.10.md#inflation-and-purchasing-power); 2 linked mentions |
| <a id="term-purchasing-power"></a>**Purchasing power** |  | The amount of goods and services a unit of money can buy. | First: **70**<br>Later: 302, 457, 494, 500, 502, 511, 515, 531, 551, 589, 599, 600, 842 | [First linked use](mfb-bd-26.10/mfb-bd-eg-26.10.md#local-verification-record); 9 linked mentions |
| <a id="term-monetary-expansion"></a>**Monetary expansion** |  | An increase in the amount of money or credit in circulation. | Not present | No linked use |
| <a id="term-secondary-effects"></a>**Secondary effects** |  | Later indirect effects caused by an initial economic change. | Not present | No linked use |
| <a id="term-inflation-basket"></a>**Inflation basket** |  | A selected group of goods and services used to measure average price changes. | Not present | No linked use |
| <a id="term-basket-of-goods"></a>**Basket of goods** |  | A collection of goods and services used to measure changes in the cost of living. | Not present | No linked use |
| <a id="term-cantillon-effect"></a>**Cantillon Effect** |  | The idea that new money can affect people differently depending on who receives and spends it first. | Not present | No linked use |
| <a id="term-gdp"></a>**GDP** |  | Gross domestic product: the total value of goods and services produced in a country during a given period. | Not present | No linked use |
| <a id="term-imports"></a>**Imports** |  | Goods and services produced in another country and sold in the domestic market. | Not present | No linked use |
| <a id="term-monetary-and-fiscal-policy"></a>**Monetary and fiscal policy** |  | Central-bank and government policies, respectively, that can influence money, taxation, spending, and interest rates. | Not present | No linked use |

### CBDCs as a beginner fiat-system example

| Word or phrase | LEX-ID | Beginner definition | Student Guide line(s) | Educator Guide use |
| --- | --- | --- | --- | --- |
| <a id="term-cbdc"></a>**CBDC / central bank digital currency** |  | A digital form of fiat money issued as a liability of a central bank. | First: **557**<br>Later: 559, 561, 563, 565, 572, 574, 585, 599 | [First linked use](mfb-bd-26.10/mfb-bd-eg-26.10.md#local-verification-record); 19 linked mentions |

### Why people look for alternatives

| Word or phrase | LEX-ID | Beginner definition | Student Guide line(s) | Educator Guide use |
| --- | --- | --- | --- | --- |
| <a id="term-currency"></a>**Currency** |  | Money used by a country or within a monetary system. | First: **304**<br>Later: 407, 409, 411, 424, 426, 451, 452, 459, 502, 509, 521, 523, 525, 527, 551, 612, 710, 885, 896, 910, 918, 1409, 1632, 1645, 1778, 1783 | [First linked use](mfb-bd-26.10/mfb-bd-eg-26.10.md#local-verification-record); 17 linked mentions |
| <a id="term-asset"></a>**Asset** |  | Something a person or institution owns that may provide use, income, or future value. | First: **286**<br>Later: 304, 332, 392, 409, 481, 492, 511, 536, 544, 551, 553, 625, 865, 867, 875, 904, 912, 920, 922, 926, 928, 1682 | [First linked use](mfb-bd-26.10/mfb-bd-eg-26.10.md#t2--bitcoin-explanation-rule-and-role-map-and-asset-comparison-c2-c3); 19 linked mentions |
| <a id="term-bond"></a>**Bond** |  | A debt security: the buyer lends money to a government or organization in return for promised repayment, usually with interest. | First: **551**<br>Later: — | No linked use |
| <a id="term-debt"></a>**Debt** |  | Money that is owed to someone else. | First: **286**<br>Later: 288, 401, 424, 511 | No linked use |

## Module 2: How Bitcoin Works

### Why Bitcoin was created

| Word or phrase | LEX-ID | Beginner definition | Student Guide line(s) | Educator Guide use |
| --- | --- | --- | --- | --- |
| <a id="term-issuer"></a>**Issuer** |  | The authority, institution, or system that creates and puts money or claims into circulation. | First: **72**<br>Later: 403, 407, 418, 555, 565, 572, 612, 614, 637, 693, 910, 912, 916, 918, 924 | [First linked use](mfb-bd-26.10/mfb-bd-eg-26.10.md#bitcoin-stablecoins-and-other-crypto-assets); 8 linked mentions |
| <a id="term-intermediary"></a>**Intermediary** |  | A middle party, such as a bank, exchange, or payment service, between participants in a transaction. | First: **418**<br>Later: 612, 635, 752, 942, 960, 981 | [First linked use](mfb-bd-26.10/mfb-bd-eg-26.10.md#why-bitcoin-was-created); 2 linked mentions |
| <a id="term-bitcoin-network"></a>**Bitcoin network** |  | The independent computers and participants that operate Bitcoin under the same rules. | First: **625**<br>Later: 719, 733, 916, 943, 1072, 1269 | No linked use |
| <a id="term-bitcoin-protocol"></a>**Bitcoin protocol** |  | The shared technical rules that Bitcoin participants use to validate and relay activity. | Not present | [First linked use](mfb-bd-26.10/mfb-bd-eg-26.10.md#users-nodes-miners-developers-and-services); 2 linked mentions |
| <a id="term-bitcoin-service"></a>**Bitcoin service** |  | A separate business or tool that uses the Bitcoin network. | Not present | [First linked use](mfb-bd-26.10/mfb-bd-eg-26.10.md#users-nodes-miners-developers-and-services); 2 linked mentions |
| <a id="term-censorship-resistance"></a>**Censorship resistance** |  | The ability to use Bitcoin without a government, bank, or corporation being able to decide which valid transactions may be sent. | Not present | No linked use |

### The search for digital and decentralized money

| Word or phrase | LEX-ID | Beginner definition | Student Guide line(s) | Educator Guide use |
| --- | --- | --- | --- | --- |
| <a id="term-cryptography"></a>**Cryptography** |  | Mathematical methods used to protect information and prove authenticity. | First: **227**<br>Later: 629, 631, 633, 650 | [First linked use](mfb-bd-26.10/mfb-bd-eg-26.10.md#digital-signatures); 1 linked mention |
| <a id="term-encryption"></a>**Encryption** |  | Transforming information so only an authorized party can read it. | First: **633**<br>Later: — | [First linked use](mfb-bd-26.10/mfb-bd-eg-26.10.md#17-quick-terminology-and-misconception-sensitive-distinctions); 2 linked mentions |
| <a id="term-digital-signature"></a>**Digital signature** |  | A mathematical proof created with a private key that authorizes a message or transaction. | First: **616**<br>Later: 633, 671, 735, 737, 964, 996, 1080, 1088 | [First linked use](mfb-bd-26.10/mfb-bd-eg-26.10.md#explain-the-combined-response); 3 linked mentions |
| <a id="term-cypherpunk"></a>**Cypherpunk** |  | A person who uses or advocates cryptography and open technology to protect privacy and freedom. | First: **629**<br>Later: 635 | No linked use |
| <a id="term-digital-asset"></a>**Digital asset** |  | A digital representation of value that can be transferred or used as a store of value. | First: **119**<br>Later: 555, 840, 910, 912, 916, 924, 926, 928 | No linked use |
| <a id="term-distributed-ledger"></a>**Distributed ledger** |  | A record of transactions that is shared across multiple computers instead of being kept in one central location. | Not present | No linked use |
| <a id="term-permissionless"></a>**Permissionless** |  | Open to anyone who can use the rules without needing approval from a central gatekeeper. | Not present | No linked use |
| <a id="term-trust-minimization"></a>**Trust minimization** |  | Reducing reliance on third parties by enabling people to verify rules and transactions independently. | Not present | No linked use |
| <a id="term-trustless"></a>**Trustless** |  | Describes a system designed to reduce the need to trust a third party by relying on verifiable rules. | Not present | No linked use |

### Early digital-money attempts and the double-spend problem

| Word or phrase | LEX-ID | Beginner definition | Student Guide line(s) | Educator Guide use |
| --- | --- | --- | --- | --- |
| <a id="digicash"></a>**DigiCash** |  | An early private-digital-payment system that depended on a central company. | First: **650**<br>Later: — | [First linked use](mfb-bd-26.10/mfb-bd-eg-26.10.md#earlier-digital-money-context); 1 linked mention |
| <a id="hashcash"></a>**Hashcash** |  | An early proof-of-work system designed to make unwanted email computationally costly. | First: **652**<br>Later: — | [First linked use](mfb-bd-26.10/mfb-bd-eg-26.10.md#earlier-digital-money-context); 1 linked mention |
| <a id="bit-gold"></a>**Bit Gold** |  | An early proposal for scarce digital records created through computational work. | First: **654**<br>Later: — | [First linked use](mfb-bd-26.10/mfb-bd-eg-26.10.md#earlier-digital-money-context); 1 linked mention |
| <a id="b-money"></a>**B-money** |  | An early proposal for decentralized digital money. | First: **656**<br>Later: — | [First linked use](mfb-bd-26.10/mfb-bd-eg-26.10.md#earlier-digital-money-context); 1 linked mention |
| <a id="reusable-proof-of-work"></a>**Reusable proof of work** |  | An early proposal for transferring scarce digital value without relying on one central database. | First: **656**<br>Later: — | [First linked use](mfb-bd-26.10/mfb-bd-eg-26.10.md#earlier-digital-money-context); 1 linked mention |
| <a id="bittorrent"></a>**BitTorrent** |  | A file-sharing system that demonstrated decentralized information sharing. | First: **658**<br>Later: — | No linked use |
| <a id="term-peer-to-peer-network"></a>**Peer-to-peer network** |  | A network in which independent computers communicate directly rather than through one central server. | First: **616**<br>Later: 658, 670, 964, 996 | [First linked use](mfb-bd-26.10/mfb-bd-eg-26.10.md#explain-the-combined-response); 1 linked mention |
| <a id="term-byzantine-generals-problem"></a>**Byzantine Generals’ Problem** |  | A computing problem about how independent participants can reach a reliable agreement when some messages or participants may be untrustworthy. | Not present | No linked use |
| <a id="term-double-spending"></a>**Double spending** |  | Trying to use the same digital unit in more than one payment. | First: **662**<br>Later: 664, 960, 976, 995 | [First linked use](mfb-bd-26.10/mfb-bd-eg-26.10.md#t2--bitcoin-explanation-rule-and-role-map-and-asset-comparison-c2-c3); 2 linked mentions |
| <a id="term-double-spend-problem"></a>**Double-spend problem** |  | The challenge of preventing a digital unit from being spent more than once. | First: **646**<br>Later: 681 | [First linked use](mfb-bd-26.10/mfb-bd-eg-26.10.md#review-and-bridge-to-module-2); 3 linked mentions |
| <a id="term-proof-of-work"></a>**Proof of work** |  | The process miners use to compete to propose blocks by performing costly computation. | First: **616**<br>Later: 652, 672, 674, 691, 706, 764, 766, 786, 788, 790, 801, 810, 989, 996 | [First linked use](mfb-bd-26.10/mfb-bd-eg-26.10.md#t2--bitcoin-explanation-rule-and-role-map-and-asset-comparison-c2-c3); 15 linked mentions |
| <a id="term-mining"></a>**Mining** |  | The process of competing through proof of work to propose a block. | First: **227**<br>Later: 672, 726, 808, 989 | [First linked use](mfb-bd-26.10/mfb-bd-eg-26.10.md#four-module-diploma-and-advanced-boundaries); 4 linked mentions |
| <a id="term-miner"></a>**Miner** |  | A participant that builds candidate blocks and performs proof-of-work computation. | First: **118**<br>Later: 672, 721, 722, 758, 766, 778, 782, 790, 792, 794, 803, 814, 827, 834, 964, 976, 998 | [First linked use](mfb-bd-26.10/mfb-bd-eg-26.10.md#t2--bitcoin-explanation-rule-and-role-map-and-asset-comparison-c2-c3); 21 linked mentions |
| <a id="term-mining-pool"></a>**Mining pool** |  | A group of miners that combines work and shares rewards according to its rules. | Not present | No linked use |
| <a id="term-node"></a>**Node** |  | Software or a computer running Bitcoin software and checking the network’s rules. | First: **118**<br>Later: 673, 693, 706, 720, 722, 745, 758, 764, 778, 779, 782, 784, 794, 834, 879, 884, 964, 976, 982, 998, 999, 1088 | [First linked use](mfb-bd-26.10/mfb-bd-eg-26.10.md#t2--bitcoin-explanation-rule-and-role-map-and-asset-comparison-c2-c3); 31 linked mentions |
| <a id="term-full-node"></a>**Full node** |  | A node that independently checks Bitcoin’s rules. | First: **764**<br>Later: — | No linked use |
| <a id="term-validating-node"></a>**Validating node** |  | A node that independently checks Bitcoin’s rules. | First: **616**<br>Later: 834, 838 | No linked use |
| <a id="term-lightweight-node"></a>**Lightweight node** |  | A Bitcoin client that checks less data than a full node and relies on other nodes for some information. | Not present | No linked use |
| <a id="term-economic-node"></a>**Economic node** |  | A node whose operator uses it for real payment activity and can therefore influence which rules have economic support. | Not present | No linked use |
| <a id="term-bitcoin-block"></a>**Bitcoin block** |  | A batch of transactions accepted into Bitcoin’s chain. | Not present | No linked use |
| <a id="term-candidate-block"></a>**Candidate block** |  | A proposed block that has not yet been accepted into the chain. | First: **766**<br>Later: — | [First linked use](mfb-bd-26.10/mfb-bd-eg-26.10.md#users-nodes-miners-developers-and-services); 3 linked mentions |
| <a id="term-valid-chain"></a>**Valid chain** |  | A chain of blocks that follows Bitcoin’s rules. | First: **674**<br>Later: — | No linked use |
| <a id="term-accumulated-work"></a>**Accumulated work** |  | The total proof-of-work effort represented by a chain. | First: **674**<br>Later: 806 | [First linked use](mfb-bd-26.10/mfb-bd-eg-26.10.md#explain-the-combined-response); 1 linked mention |

### Bitcoin origin timeline

| Word or phrase | LEX-ID | Beginner definition | Student Guide line(s) | Educator Guide use |
| --- | --- | --- | --- | --- |
| <a id="term-satoshi-nakamoto"></a>**Satoshi Nakamoto** |  | The name used by Bitcoin’s creator or creators; the real-world identity is unknown. | First: **666**<br>Later: 942, 954, 960 | No linked use |
| <a id="term-bitcoin-whitepaper"></a>**Bitcoin whitepaper** |  | The original paper, *Bitcoin: A Peer-to-Peer Electronic Cash System*, which described Bitcoin’s design and purpose. | First: **952**<br>Later: 960 | No linked use |
| <a id="term-genesis-block"></a>**Genesis Block** |  | The first block in Bitcoin’s blockchain, created when the network began. | First: **943**<br>Later: 952, 958 | No linked use |
| <a id="term-bitcoin-pizza-day"></a>**Bitcoin Pizza Day** |  | The annual remembrance of the 2010 purchase of two pizzas with 10,000 bitcoin. | First: **945**<br>Later: — | No linked use |
| <a id="term-hal-finney"></a>**Hal Finney** |  | The recipient of the first recorded person-to-person Bitcoin transaction. | First: **944**<br>Later: — | No linked use |
| <a id="term-person-to-person-transaction"></a>**Person-to-person transaction** |  | A payment made directly from one participant to another. | First: **952**<br>Later: — | No linked use |

### Decentralization

| Word or phrase | LEX-ID | Beginner definition | Student Guide line(s) | Educator Guide use |
| --- | --- | --- | --- | --- |
| <a id="term-decentralization"></a>**Decentralization** |  | The distribution of control and verification across many independent participants. | First: **693**<br>Later: 708, 712, 716, 726, 733 | [First linked use](mfb-bd-26.10/mfb-bd-eg-26.10.md#t2--bitcoin-explanation-rule-and-role-map-and-asset-comparison-c2-c3); 9 linked mentions |
| <a id="term-centralization"></a>**Centralization** |  | The concentration of power or control in one person, organization, or institution. | Not present | No linked use |
| <a id="term-centralized-system"></a>**Centralized system** |  | A system in which power or control is concentrated in one entity. | First: **666**<br>Later: 710 | No linked use |
| <a id="term-decentralized-system"></a>**Decentralized system** |  | A system in which power or control is distributed among multiple independent entities. | First: **714**<br>Later: — | No linked use |
| <a id="term-consensus"></a>**Consensus** |  | Agreement among Bitcoin nodes about which transactions and blocks follow the shared rules. | First: **779**<br>Later: — | [First linked use](mfb-bd-26.10/mfb-bd-eg-26.10.md#strong-module-2-activities); 1 linked mention |
| <a id="term-nakamoto-consensus"></a>**Nakamoto consensus** |  | Bitcoin’s method of combining shared rules, proof of work, and the chain with the most accumulated work so independent nodes can converge on a transaction history. | Not present | No linked use |
| <a id="term-open-source-software"></a>**Open-source software** |  | Software whose source code can be publicly inspected, used, shared, and improved. | First: **718**<br>Later: — | No linked use |
| <a id="term-ledger"></a>**Ledger** |  | A record of transactions; Bitcoin’s ledger is copied and checked across many nodes. | First: **610**<br>Later: 616, 700, 710, 724, 726, 766, 879, 982, 995, 996, 1031, 1037 | [First linked use](mfb-bd-26.10/mfb-bd-eg-26.10.md#why-bitcoin-was-created); 7 linked mentions |

### Finite supply

| Word or phrase | LEX-ID | Beginner definition | Student Guide line(s) | Educator Guide use |
| --- | --- | --- | --- | --- |
| <a id="term-block-subsidy"></a>**Block subsidy** |  | New bitcoin created by the rules and paid to the miner of a valid block. | First: **766**<br>Later: 814 | [First linked use](mfb-bd-26.10/mfb-bd-eg-26.10.md#finite-supply-and-halving); 1 linked mention |
| <a id="term-issuance-schedule"></a>**Issuance schedule** |  | The rules that control how new bitcoin is issued over time. | First: **764**<br>Later: 814, 916 | No linked use |
| <a id="term-maximum-supply"></a>**Maximum supply / hard cap** |  | The greatest total amount of bitcoin the rules allow. | First: **814**<br>Later: 916 | No linked use |
| <a id="term-halving"></a>**Halving** |  | The event that cuts Bitcoin’s block subsidy in half after every 210,000 blocks. | First: **816**<br>Later: 818, 820 | [First linked use](mfb-bd-26.10/mfb-bd-eg-26.10.md#t2--bitcoin-explanation-rule-and-role-map-and-asset-comparison-c2-c3); 8 linked mentions |
| <a id="term-51-percent-attack"></a>**51% attack** |  | A situation in which one miner or group controls more than half of the network’s hash rate and may be able to reorganize recent blocks or attempt double spending. | Not present | No linked use |

### Satoshis and unit bias

| Word or phrase | LEX-ID | Beginner definition | Student Guide line(s) | Educator Guide use |
| --- | --- | --- | --- | --- |
| <a id="term-sat"></a>**Sat / satoshi** |  | The smallest named unit of bitcoin; 100,000,000 sats equal one bitcoin. | First: **26**<br>Later: 177, 846, 848, 852, 853, 854, 855, 856, 863, 865, 869, 881, 896, 943, 944, 954, 1000, 1454, 1597, 1632, 1778 | [First linked use](mfb-bd-26.10/mfb-bd-eg-26.10.md#t2--bitcoin-explanation-rule-and-role-map-and-asset-comparison-c2-c3); 18 linked mentions |

### Users, nodes, and miners

| Word or phrase | LEX-ID | Beginner definition | Student Guide line(s) | Educator Guide use |
| --- | --- | --- | --- | --- |
| <a id="term-bitcoin-core"></a>**Bitcoin Core** |  | A widely used Bitcoin software implementation that can run a full node. | Not present | No linked use |
| <a id="term-developer-software-proposal"></a>**Developer software proposal** |  | A suggested software change only affects Bitcoin when participants choose software that follows it. | Not present | No linked use |
| <a id="term-bitcoin-improvement-proposal"></a>**Bitcoin Improvement Proposal (BIP)** |  | A formal process for proposing, discussing, and documenting improvements to Bitcoin. | Not present | No linked use |
| <a id="term-bip39"></a>**Bitcoin Improvement Proposal 39 (BIP39)** |  | A standard for representing a wallet seed as an ordered list of words, commonly called a seed phrase or recovery phrase. | Not present | No linked use |
| <a id="term-hard-fork"></a>**Hard fork** |  | A rule change that is not compatible with older rules. | Not present | No linked use |
| <a id="term-soft-fork"></a>**Soft fork** |  | A rule change that remains compatible with older rules. | Not present | No linked use |
| <a id="term-segwit"></a>**SegWit (Segregated Witness)** |  | A Bitcoin protocol upgrade that changed how some transaction data is stored, increasing effective block capacity. | Not present | No linked use |

### Proof of work

| Word or phrase | LEX-ID | Beginner definition | Student Guide line(s) | Educator Guide use |
| --- | --- | --- | --- | --- |
| <a id="term-hash-function"></a>**Hash function** |  | A mathematical process that turns data into a fixed-length digital result. | First: **792**<br>Later: — | No linked use |
| <a id="term-hash"></a>**Hash** |  | The fixed-length result produced by a hash function. | Not present | No linked use |
| <a id="term-sha-256"></a>**SHA-256** |  | The hash function Bitcoin uses in proof of work. It produces a fixed-length result from input data. | Not present | No linked use |
| <a id="term-target"></a>**Target** |  | The threshold that a proof-of-work result must satisfy. | First: **706**<br>Later: 792 | [First linked use](mfb-bd-26.10/mfb-bd-eg-26.10.md#proof-of-work); 1 linked mention |
| <a id="term-difficulty"></a>**Difficulty** |  | A measure of how hard it is to find a proof-of-work result that satisfies the target. | First: **311**<br>Later: 792, 808 | [First linked use](mfb-bd-26.10/mfb-bd-eg-26.10.md#proof-of-work); 1 linked mention |
| <a id="term-difficulty-adjustment"></a>**Difficulty adjustment** |  | Bitcoin’s regular change to the proof-of-work target that aims to keep block production near its intended average pace. | Not present | No linked use |
| <a id="term-hashrate"></a>**Hashrate / hash rate** |  | A measure of how many hash attempts are made over a period of time. | Not present | No linked use |
| <a id="term-nonce"></a>**Nonce** |  | A number miners can change in a block header while searching for a hash that satisfies the target. | Not present | No linked use |
| <a id="term-merkle-tree"></a>**Merkle tree** |  | A tree-like structure that summarizes transaction data so it can be checked efficiently. | Not present | No linked use |
| <a id="term-block-height"></a>**Block height** |  | The number of blocks that come before a given block, showing its position in the chain. | First: **820**<br>Later: — | No linked use |
| <a id="term-timestamp"></a>**Timestamp** |  | Data in a block that records its claimed creation time. | Not present | No linked use |
| <a id="term-verification"></a>**Verification** |  | Independently checking that transactions and blocks follow Bitcoin’s rules. | First: **118**<br>Later: 673, 691, 693, 976, 996, 1261 | No linked use |
| <a id="term-immutability"></a>**Immutability** |  | The practical difficulty of changing confirmed Bitcoin history because doing so would require replacing later proof of work. | Not present | No linked use |
| <a id="term-valid-result"></a>**Valid result** |  | A proof-of-work result that satisfies the target. | First: **794**<br>Later: — | No linked use |
| <a id="term-broadcast"></a>**Broadcast** |  | To send transaction or block data to peers across the network. | First: **743**<br>Later: 766, 794, 1267, 1356 | [First linked use](mfb-bd-26.10/mfb-bd-eg-26.10.md#suggested-two-hour-flow-1); 3 linked mentions |
| <a id="term-blockchain"></a>**Blockchain** |  | Bitcoin’s public history, arranged in blocks. | First: **616**<br>Later: 700, 702, 704, 794, 918, 1347 | [First linked use](mfb-bd-26.10/mfb-bd-eg-26.10.md#explain-the-combined-response); 2 linked mentions |
| <a id="term-mempool"></a>**Mempool** |  | A node’s temporary collection of valid, unconfirmed transactions it has received. Mempools can differ from one node to another. | Not present | No linked use |
| <a id="term-block-space"></a>**Block space** |  | The limited data capacity available in each Bitcoin block. | First: **1257**<br>Later: — | [First linked use](mfb-bd-26.10/mfb-bd-eg-26.10.md#fees-confirmations-and-finality); 3 linked mentions |
| <a id="term-orphan-block"></a>**Orphan block** |  | A historical term for a valid block that is not part of the active chain because another valid chain has more accumulated work. | Not present | No linked use |

### Bitcoin as sound digital money

| Word or phrase | LEX-ID | Beginner definition | Student Guide line(s) | Educator Guide use |
| --- | --- | --- | --- | --- |
| <a id="term-sound-money"></a>**Sound money** |  | A judgment for money whose supply is difficult to expand and whose properties support reliable use over time. | First: **873**<br>Later: 904, 1001 | [First linked use](mfb-bd-26.10/mfb-bd-eg-26.10.md#suggested-two-hour-flow-1); 7 linked mentions |
| <a id="term-sat-interchangeability"></a>**Sat interchangeability** |  | Whether equal sats are treated as equivalent in use; it is an application of fungibility. | Not present | No linked use |
| <a id="term-value"></a>**Value** |  | The usefulness or importance of something to a person. | First: **273**<br>Later: 280, 286, 290, 302, 340, 351, 364, 372, 379, 384, 392, 403, 405, 481, 511, 544, 593, 635, 656, 867, 880, 906, 918, 925, 944, 991, 1587, 1589, 1593, 1597, 1641, 1651, 1747, 1793, 1853, 1855 | [First linked use](mfb-bd-26.10/mfb-bd-eg-26.10.md#barter-and-the-double-coincidence-of-wants); 17 linked mentions |
| <a id="term-price"></a>**Price** |  | The amount exchanged for a good, service, or asset. | First: **207**<br>Later: 211, 286, 288, 300, 353, 426, 435, 498, 509, 511, 517, 593, 625, 836, 838, 865, 867, 869, 894, 902, 906, 916, 920, 928, 932, 991, 1320, 1632, 1723, 1761, 1778, 1855 | [First linked use](mfb-bd-26.10/mfb-bd-eg-26.10.md#t2--bitcoin-explanation-rule-and-role-map-and-asset-comparison-c2-c3); 40 linked mentions |
| <a id="term-bias"></a>**Bias** |  | A tendency that can influence judgment. | First: **846**<br>Later: 865, 906 | [First linked use](mfb-bd-26.10/mfb-bd-eg-26.10.md#sats-and-unit-bias); 1 linked mention |
| <a id="term-hodl"></a>**HODL** |  | Informal Bitcoin-community slang for holding bitcoin rather than selling or trading it. | Not present | No linked use |
| <a id="term-sovereignty"></a>**Sovereignty** |  | The ability to control one’s money without depending on an intermediary. | Not present | No linked use |
| <a id="term-volatility"></a>**Volatility** |  | The degree to which an asset’s price varies over time. | First: **537**<br>Later: 902, 1001, 1587, 1763 | No linked use |

## Module 3: Using Bitcoin Safely

### Wallets

| Word or phrase | LEX-ID | Beginner definition | Student Guide line(s) | Educator Guide use |
| --- | --- | --- | --- | --- |
| <a id="term-bitcoin-wallet"></a>**Bitcoin wallet** |  | A tool that manages keys and helps receive, authorize, and track Bitcoin transactions; it does not literally contain bitcoin. | First: **59**<br>Later: 100, 191, 193, 1029, 1031 | [First linked use](mfb-bd-26.10/mfb-bd-eg-26.10.md#wallets-are-interfaces); 1 linked mention |
| <a id="term-wallet-backup"></a>**Wallet backup** |  | A secure copy of the information needed to restore a wallet, such as its seed phrase where the wallet uses one. | Not present | No linked use |
| <a id="term-custody"></a>**Custody** |  | Control of Bitcoin keys. | First: **92**<br>Later: 120, 247, 537, 754, 916, 928, 1046, 1136, 1138, 1160, 1301, 1305, 1309, 1321, 1349, 1358, 1452, 1506, 1513, 1531, 1574, 1576, 1587, 1646, 1696, 1761, 1763, 1774, 1794, 1853, 1855, 1862, 1863, 1864 | [First linked use](mfb-bd-26.10/mfb-bd-eg-26.10.md#t2--bitcoin-explanation-rule-and-role-map-and-asset-comparison-c2-c3); 54 linked mentions |
| <a id="term-custodian"></a>**Custodian** |  | A person or service that controls Bitcoin keys for someone else. | First: **211**<br>Later: 762, 918, 1140, 1142, 1160, 1800 | [First linked use](mfb-bd-26.10/mfb-bd-eg-26.10.md#bitcoin-stablecoins-and-other-crypto-assets); 4 linked mentions |
| <a id="term-self-custody"></a>**Self-custody** |  | Control of your own Bitcoin keys rather than leaving them with a service. | First: **968**<br>Later: 970, 1160, 1375, 1635, 1967 | [First linked use](mfb-bd-26.10/mfb-bd-eg-26.10.md#the-diploma-purpose-and-your-responsibility); 9 linked mentions |
| <a id="term-wallet-compatibility"></a>**Wallet compatibility** |  | The ability of a wallet, backup, address, or network to work with another system. | Not present | [First linked use](mfb-bd-26.10/mfb-bd-eg-26.10.md#seed-phrases-and-recovery); 1 linked mention |
| <a id="term-project-continuity"></a>**Project continuity** |  | The likelihood that wallet software will remain maintained and usable. | Not present | No linked use |
| <a id="term-privacy"></a>**Privacy** |  | The ability to limit who can collect, see, use, or share information about you, such as your name, contact details, location, and financial activity. When using Bitcoin, this includes limiting how your identity is linked to addresses, balances, and payments. Bitcoin’s public transaction history means privacy is not automatic, and privacy does not mean that all activity is invisible. | First: **201**<br>Later: 227, 599, 629, 1046, 1065, 1273, 1322, 1506, 1517, 1593, 1696, 1715, 1717, 1723, 1738, 1862 | [First linked use](mfb-bd-26.10/mfb-bd-eg-26.10.md#t2--bitcoin-explanation-rule-and-role-map-and-asset-comparison-c2-c3); 26 linked mentions |
| <a id="term-bitcoin-privacy"></a>**Bitcoin privacy** |  | Control over information about a person and their Bitcoin activity. | Not present | No linked use |
| <a id="term-block-explorer-privacy"></a>**Block-explorer privacy** |  | The privacy implications of using a public tool to inspect addresses or transactions. | Not present | No linked use |

### Addresses

| Word or phrase | LEX-ID | Beginner definition | Student Guide line(s) | Educator Guide use |
| --- | --- | --- | --- | --- |
| <a id="term-bitcoin-address"></a>**Bitcoin address / wallet address** |  | Receiving information for an on-chain Bitcoin payment. | First: **1054**<br>Later: 1056, 1355, 1603 | [First linked use](mfb-bd-26.10/mfb-bd-eg-26.10.md#addresses-and-payment-requests); 1 linked mention |
| <a id="term-address-type"></a>**Address type** |  | The format of a Bitcoin address. | Not present | [First linked use](mfb-bd-26.10/mfb-bd-eg-26.10.md#local-bitcoin-tool-review); 1 linked mention |
| <a id="term-address-reuse"></a>**Address reuse** |  | Using the same Bitcoin address more than once. It is discouraged because it can reduce privacy. | Not present | No linked use |
| <a id="term-payment-destination"></a>**Payment destination** |  | The receiving information to which funds are directed. | Not present | [First linked use](mfb-bd-26.10/mfb-bd-eg-26.10.md#support-accessibility-without-lowering-the-competency); 1 linked mention |
| <a id="term-network-tag"></a>**Network tag** |  | A label identifying the intended payment network. | Not present | No linked use |

### Keys

| Word or phrase | LEX-ID | Beginner definition | Student Guide line(s) | Educator Guide use |
| --- | --- | --- | --- | --- |
| <a id="term-private-key"></a>**Private key** |  | Secret information that lets a wallet authorize spending; anyone who obtains it may control the funds. | First: **211**<br>Later: 219, 671, 737, 739, 1013, 1078, 1080, 1082, 1088, 1090, 1092, 1111, 1293, 1392, 1875, 1885, 1905, 1982 | [First linked use](mfb-bd-26.10/mfb-bd-eg-26.10.md#a-supportive-assessment-route); 20 linked mentions |
| <a id="term-public-key"></a>**Public key** |  | Information derived from a private key that helps verify signatures without revealing the private key. | First: **1082**<br>Later: — | [First linked use](mfb-bd-26.10/mfb-bd-eg-26.10.md#activity-public-or-secret); 2 linked mentions |
| <a id="term-key-pair"></a>**Key pair** |  | A matching private key and public key used to authorize and verify Bitcoin transactions. | Not present | No linked use |

### Seed phrases and recovery

| Word or phrase | LEX-ID | Beginner definition | Student Guide line(s) | Educator Guide use |
| --- | --- | --- | --- | --- |
| <a id="term-seed-phrase"></a>**Seed phrase / recovery phrase** |  | An ordered list of secret words that many wallets use to restore keys. | First: **191**<br>Later: 198, 199, 211, 219, 968, 1013, 1050, 1092, 1101, 1103, 1105, 1107, 1111, 1118, 1127, 1192, 1196, 1284, 1293, 1392, 1393, 1470, 1827, 1875, 1885, 1905, 1982 | [First linked use](mfb-bd-26.10/mfb-bd-eg-26.10.md#a-supportive-assessment-route); 20 linked mentions |
| <a id="term-single-signature"></a>**Single-signature** |  | A spending arrangement in which one key authorizes a transaction. | Not present | No linked use |
| <a id="term-multisignature"></a>**Multisignature (multisig)** |  | A spending arrangement requiring more than one key or approval. | Not present | [First linked use](mfb-bd-26.10/mfb-bd-eg-26.10.md#four-module-diploma-and-advanced-boundaries); 2 linked mentions |
| <a id="term-hot-wallet"></a>**Hot wallet** |  | A wallet using an online device. | First: **1166**<br>Later: 1168, 1181 | [First linked use](mfb-bd-26.10/mfb-bd-eg-26.10.md#assessed-competencies-and-competency-criteria-2); 2 linked mentions |
| <a id="term-cold-wallet"></a>**Cold wallet / cold storage** |  | A wallet or storage arrangement that keeps signing keys offline. | First: **1164**<br>Later: 1170, 1172, 1182 | No linked use |
| <a id="term-hardware-wallet"></a>**Hardware wallet** |  | A dedicated device for holding signing keys. | First: **1170**<br>Later: 1172, 1394 | [First linked use](mfb-bd-26.10/mfb-bd-eg-26.10.md#t3--custody-safety-and-pathway-decision-c4-c5); 7 linked mentions |
| <a id="term-custodial-wallet"></a>**Custodial wallet** |  | A wallet arrangement in which a service controls the keys. | Not present | No linked use |
| <a id="term-paper-wallet"></a>**Paper wallet** |  | A printed record of Bitcoin key material. It is easy to lose or expose and is generally not a recommended storage method. | Not present | No linked use |
| <a id="term-two-factor-authentication"></a>**Two-factor authentication (2FA)** |  | An account-security method requiring two different forms of proof, such as a password and a separate code or device. | Not present | No linked use |

### Receiving and sending bitcoin

| Word or phrase | LEX-ID | Beginner definition | Student Guide line(s) | Educator Guide use |
| --- | --- | --- | --- | --- |
| <a id="term-confirmation"></a>**Confirmation** |  | A count showing how many valid blocks include or follow the block containing a transaction; more confirmations make its place in the blockchain more costly to rewrite. | First: **794**<br>Later: 916, 1233, 1265, 1267, 1269, 1347, 1356, 1358, 1563 | [First linked use](mfb-bd-26.10/mfb-bd-eg-26.10.md#p6a--supported-first-access-and-receipt-c6); 16 linked mentions |
| <a id="term-first-confirmation"></a>**First confirmation** |  | The inclusion of a transaction in its first valid block. | First: **1267**<br>Later: — | [First linked use](mfb-bd-26.10/mfb-bd-eg-26.10.md#on-chain-and-lightning-payments); 1 linked mention |
| <a id="term-final-settlement"></a>**Final settlement** |  | The point at which a transaction is treated as practically irreversible after sufficient confirmations. | Not present | No linked use |
| <a id="term-block-depth"></a>**Block depth** |  | The number of blocks added after the block containing a transaction. | Not present | No linked use |
| <a id="term-transaction"></a>**Transaction (tx)** |  | A record that transfers bitcoin under Bitcoin’s rules. | First: **211**<br>Later: 227, 553, 563, 616, 664, 670, 672, 673, 674, 691, 704, 720, 737, 743, 745, 756, 764, 766, 784, 794, 804, 808, 880, 882, 884, 902, 916, 944, 956, 966, 981, 989, 996, 1031, 1033, 1088, 1142, 1172, 1233, 1239, 1257, 1261, 1265, 1267, 1269, 1273, 1438, 1472, 1488, 1517, 1556, 1721, 1731, 1802, 1907 | No linked use |
| <a id="term-transaction-fee"></a>**Transaction fee / miner fee** |  | A fee paid for an on-chain transaction to be included in a block. | First: **766**<br>Later: 827, 902, 1655 | [First linked use](mfb-bd-26.10/mfb-bd-eg-26.10.md#finite-supply-and-halving); 1 linked mention |
| <a id="term-dust-transaction"></a>**Dust transaction** |  | A transaction output with such a small bitcoin amount that spending it may cost more in fees than it is worth. | Not present | No linked use |
| <a id="term-fee-rate"></a>**Fee rate** |  | The transaction fee offered per unit of transaction data, commonly measured in sats per virtual byte (sat/vB). | Not present | No linked use |
| <a id="term-fee-estimation"></a>**Fee estimation** |  | A wallet’s attempt to choose an appropriate transaction fee. | Not present | No linked use |
| <a id="term-transaction-id"></a>**Transaction ID** / *txid* |  | A unique identifier used to find and discuss an on-chain Bitcoin transaction. | First: **1263**<br>Later: 1265, 1269 | [First linked use](mfb-bd-26.10/mfb-bd-eg-26.10.md#minimum-materials); 5 linked mentions |
| <a id="term-block-explorer"></a>**Block explorer** |  | A tool for viewing public Bitcoin data such as transactions, addresses, blocks, fees, and confirmations. | First: **952**<br>Later: 1261, 1263, 1265, 1273, 1472 | [First linked use](mfb-bd-26.10/mfb-bd-eg-26.10.md#media-and-tool-fallbacks); 3 linked mentions |
| <a id="term-transaction-input-output"></a>**Transaction input / output** |  | An input identifies bitcoin being spent; an output states where bitcoin is assigned next, including any change returned to the sender. | Not present | No linked use |
| <a id="term-utxo"></a>**UTXO / unspent transaction output** |  | A transaction output that is available to be spent under Bitcoin’s rules. | Not present | No linked use |
| <a id="term-virtual-byte"></a>**Virtual byte (vB)** |  | A unit used to express the weight of Bitcoin transaction data. Fee rates are often shown in sats per vB. | Not present | No linked use |
| <a id="term-satoshis-per-byte"></a>**Satoshis per byte (sat/b)** |  | A legacy unit for expressing a transaction fee rate per byte of transaction data. | Not present | No linked use |
| <a id="term-epoch"></a>**Epoch** |  | A group of 210,000 Bitcoin blocks, the interval between scheduled halvings. | Not present | No linked use |
| <a id="term-block-reward"></a>**Block reward** |  | The bitcoin paid to a miner for a valid block: the block subsidy plus the transaction fees in that block. | Not present | No linked use |
| <a id="term-op-return"></a>**OP_RETURN** |  | A Bitcoin transaction output that can carry a small amount of data and cannot be spent. | Not present | No linked use |
| <a id="term-timechain"></a>**Timechain** |  | A term sometimes used for Bitcoin’s blockchain to emphasize its ordered, time-stamped history. | Not present | No linked use |

### On-chain and Lightning payments

| Word or phrase | LEX-ID | Beginner definition | Student Guide line(s) | Educator Guide use |
| --- | --- | --- | --- | --- |
| <a id="term-on-chain-payment"></a>**On-chain payment** |  | A payment recorded directly in Bitcoin’s blockchain. | First: **1056**<br>Later: 1063, 1233, 1257, 1347, 1355, 1651 | No linked use |
| <a id="term-base-layer-settlement"></a>**Base-layer settlement** |  | Final settlement directly on Bitcoin’s blockchain. | First: **1357**<br>Later: — | [First linked use](mfb-bd-26.10/mfb-bd-eg-26.10.md#on-chain-and-lightning-payments); 1 linked mention |
| <a id="term-lightning-network"></a>**Lightning Network (LN)** |  | A payment network built above Bitcoin. | Not present | No linked use |
| <a id="term-layer-1"></a>**Layer 1** |  | The base Bitcoin protocol that validates transactions, reaches consensus, and produces blocks. | Not present | No linked use |
| <a id="term-layer-2"></a>**Layer 2** |  | A system built on a base network to add capacity or features. | First: **225**<br>Later: — | No linked use |
| <a id="term-payment-channel"></a>**Payment channel** |  | A mechanism for updating payments off-chain. | Not present | No linked use |
| <a id="term-atomic-swap"></a>**Atomic swap** |  | A mechanism for directly exchanging bitcoin for another asset without an intermediary, so either both parts of the exchange happen or neither does. | Not present | No linked use |
| <a id="term-lightning-routing"></a>**Lightning routing** |  | Passing a payment through connected Lightning channels. | Not present | No linked use |
| <a id="term-lightning-routing-fee"></a>**Lightning routing fee** |  | A fee a Lightning node may charge for forwarding a payment through a channel. | Not present | No linked use |
| <a id="term-lightning-liquidity"></a>**Lightning liquidity** |  | Channel capacity available to move a Lightning payment. | Not present | [First linked use](mfb-bd-26.10/mfb-bd-eg-26.10.md#on-chain-and-lightning-payments); 6 linked mentions |
| <a id="term-lightning-invoice"></a>**Lightning invoice** |  | A usually specific Lightning payment request. | First: **1065**<br>Later: 1355, 1365, 1471, 1563 | [First linked use](mfb-bd-26.10/mfb-bd-eg-26.10.md#prepare-before-class-2); 3 linked mentions |
| <a id="term-lightning-offer"></a>**Lightning offer** |  | A reusable Lightning payment request. | Not present | No linked use |
| <a id="term-lightning-address"></a>**Lightning address** |  | A human-readable Lightning receiving identifier. | First: **1355**<br>Later: 1565 | [First linked use](mfb-bd-26.10/mfb-bd-eg-26.10.md#on-chain-and-lightning-payments); 2 linked mentions |

## Module 4: Bitcoin in Your Community

Module 4 is the educator-curated **Connect** stage of the Diploma's Problem → Solution → Action → Connect learning arc.

### Local on-ramp and off-ramp pathways

| Word or phrase | LEX-ID | Beginner definition | Student Guide line(s) | Educator Guide use |
| --- | --- | --- | --- | --- |
| <a id="term-on-ramp"></a>**On-ramp** |  | A way to move value into bitcoin. | First: **1670**<br>Later: 1682 | [First linked use](mfb-bd-26.10/mfb-bd-eg-26.10.md#3-select-a-focused-module); 1 linked mention |
| <a id="term-off-ramp"></a>**Off-ramp** |  | A way to move value from bitcoin into local money, goods, or services. | First: **1670**<br>Later: 1682 | [First linked use](mfb-bd-26.10/mfb-bd-eg-26.10.md#3-select-a-focused-module); 1 linked mention |
| <a id="term-peg"></a>**Peg** |  | A fixed or targeted exchange relationship between two currencies or assets. | Not present | No linked use |
| <a id="term-unbanked"></a>**Unbanked** |  | People or communities without access to traditional banking services. | Not present | No linked use |

### KYC and no-KYC trade-offs

| Word or phrase | LEX-ID | Beginner definition | Student Guide line(s) | Educator Guide use |
| --- | --- | --- | --- | --- |
| <a id="term-kyc"></a>**KYC** |  | Identity checks required by a financial service. | First: **1334**<br>Later: 1336, 1706, 1713, 1717, 1719, 1721, 1727, 1864 | [First linked use](mfb-bd-26.10/mfb-bd-eg-26.10.md#common-misconceptions-and-responses-1); 6 linked mentions |
| <a id="term-no-kyc"></a>**No-KYC** (preferred; also called **non-KYC**) |  | A path collecting less or no standard KYC information. Use **no-KYC** throughout this curriculum; **non-KYC** is an alternative term. | First: **1706**<br>Later: 1713, 1717, 1723, 1727 | [First linked use](mfb-bd-26.10/mfb-bd-eg-26.10.md#acquiring-and-exchanging-awareness-not-financial-advice); 8 linked mentions |

### Circular economies

| Word or phrase | LEX-ID | Beginner definition | Student Guide line(s) | Educator Guide use |
| --- | --- | --- | --- | --- |
| <a id="term-bitcoin-circular-economy"></a>**Bitcoin circular economy** |  | A community network in which people earn, spend, save, and exchange bitcoin locally. | First: **1747**<br>Later: 1749 | No linked use |

### Merchant or community use cases

| Word or phrase | LEX-ID | Beginner definition | Student Guide line(s) | Educator Guide use |
| --- | --- | --- | --- | --- |
| <a id="term-community-custody"></a>**Community custody** |  | A person or group controls bitcoin for others. | First: **1800**<br>Later: — | [First linked use](mfb-bd-26.10/mfb-bd-eg-26.10.md#educator-support); 2 linked mentions |
| <a id="term-shared-funds"></a>**Shared funds** |  | Funds controlled for more than one person under agreed rules. | First: **1800**<br>Later: — | No linked use |

### Optional Bitcoin layers and community custody systems

| Word or phrase | LEX-ID | Beginner definition | Student Guide line(s) | Educator Guide use |
| --- | --- | --- | --- | --- |
| <a id="term-liquid"></a>**Liquid** |  | A Bitcoin sidechain. | **Outdated:** no match in current Student Guide | No linked use |
| <a id="term-ecash"></a>**Ecash** |  | Digital cash-like value issued by a mint. | Not present | No linked use |
| <a id="term-fedimint"></a>**Fedimint** |  | Software for federated community custody and ecash services. | Not present | No linked use |
