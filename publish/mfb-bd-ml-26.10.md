# Bitcoin Diploma Optional Self-Assessment: October Question Data

## Use

This file is the developer handoff for the 12-question optional My First Bitcoin app self-test. It follows the October scope and implementation constraints in [Microlearning plan](14_microlearning-plan.md). It is not formal assessment and must not be used for educator tracking, certification, or a pass/fail decision.

Each item has one correct answer and four plain-text options. After either answer outcome, show the item's shared plain-language explanation and review reference. The current app cannot show different correct and incorrect messages, rich text, media, links, or a multi-screen item flow. The review reference points to the learner's next reading in `08_student.md` and should be displayed as text.

## Question variants

Each numbered pair offers a short (`S`) and long (`L`) alternative for the same concept. Select **one** version from every pair for the October quiz: the release remains a 12-question self-check, not a 24-question quiz. The paired IDs let the developer choose the version that fits the available screen space.

| Concept | Short version | Long version |
|---|---|---|
| Why money exists | `BD-ML-01S` | `BD-ML-01L` |
| Functions of money | `BD-ML-02S` | `BD-ML-02L` |
| Barter | `BD-ML-03S` | `BD-ML-03L` |
| Purchasing power | `BD-ML-04S` | `BD-ML-04L` |
| Double spending | `BD-ML-05S` | `BD-ML-05L` |
| Decentralization | `BD-ML-06S` | `BD-ML-06L` |
| Nodes | `BD-ML-07S` | `BD-ML-07L` |
| Sound money | `BD-ML-08S` | `BD-ML-08L` |
| Wallets | `BD-ML-09S` | `BD-ML-09L` |
| Addresses and secrets | `BD-ML-10S` | `BD-ML-10L` |
| Seed phrase exposure | `BD-ML-11S` | `BD-ML-11L` |
| Custody | `BD-ML-12S` | `BD-ML-12L` |

## Short question set

| ID | Module and topic | Prompt | A | B | C | D | Correct option | Shared explanation and review reference |
|---|---|---|---|---|---|---|---|---|---|
| `BD-ML-01S` | Module 1: Why money exists | Why is money accepted? | Others are expected to accept it | It makes goods equally valuable | It removes all rules | It turns services into goods | A | Money helps strangers coordinate exchange across time because people expect others to accept it later. It still depends on trust, rules, and social acceptance. Review Student Guide, Module 1, “Why money exists.” |
| `BD-ML-02S` | Module 1: Functions of money | Priced, paid, saved: which roles? | Store; unit; medium | Unit; medium; store | Medium; store; unit | Scarcity; scarcity; scarcity | B | A unit of account expresses prices, a medium of exchange is accepted in payment, and a store of value moves value into the future. Review Student Guide, Module 1, “Functions and properties of money.” |
| `BD-ML-03S` | Module 1: Barter | Rice for shoes fails: why? | Different prices | No matching wants | No bank approval | Rice cannot trade | B | Direct barter is difficult when each person does not want what the other offers at the same time. This is the double coincidence of wants. Review Student Guide, Module 1, “Barter and the double coincidence of wants.” |
| `BD-ML-04S` | Module 1: Inflation and purchasing power | Prices +10%, income +5%: purchasing power? | Rises | Stays the same | Falls | Cannot tell | C | Purchasing power is what money can buy. If prices rise faster than income, the income buys less. Review Student Guide, Module 1, “Inflation and purchasing power.” |
| `BD-ML-05S` | Module 2: Double spending | One digital unit pays twice. The system must: | Reject the double spend | Hide the payment | Raise its price | Remove fees | A | Digital information can be copied, so a money system must prevent the same unit from being spent twice and establish which transaction is valid. Review Student Guide, Module 2, “Early digital-money attempts and the double-spend problem.” |
| `BD-ML-06S` | Module 2: Decentralization | Bitcoin decentralization means: | One company approves payments | Independent rule enforcement | Miners change rules freely | Equal influence for everyone | B | Bitcoin distributes verification and rule enforcement across independent participants. Decentralization does not mean one company controls the network or that everyone has equal influence. Review Student Guide, Module 2, “Decentralization.” |
| `BD-ML-07S` | Module 2: Users, nodes, and miners | A Bitcoin node: | Checks network rules | Creates bitcoin | Stores bitcoin | Guarantees payment | A | Nodes independently check Bitcoin’s rules and reject invalid data. They do not create bitcoin on request or store bitcoin inside a phone. Review Student Guide, Module 2, “Users, nodes, and miners.” |
| `BD-ML-08S` | Module 2: Bitcoin as sound digital money | Why call Bitcoin sound money? | Price always rises | Public, limited supply | One company controls it | Payments are private | B | Some people describe Bitcoin as sound money because its supply rules are public and its issuance is limited. This is a reasoned judgment, not a promise about price or privacy. Review Student Guide, Module 2, “Bitcoin as sound digital money.” |
| `BD-ML-09S` | Module 3: Wallets | A Bitcoin wallet: | Stores bitcoin | Manages keys and signs | Removes secret protection | Reverses transactions | B | Bitcoin is recorded on the shared ledger; a wallet manages the information used to access and use it. Review Student Guide, Module 3, “Wallets.” |
| `BD-ML-10S` | Module 3: Addresses and secrets | Share to receive bitcoin: | Seed phrase | Private key | Receiving address | Password | C | A receiving address can be shared for payment. Seed phrases, private keys, and passwords must remain secret. Review Student Guide, Module 3, “Addresses” and “Keys.” |
| `BD-ML-11S` | Module 3: Seed phrase exposure | Seed entered online. Safest next step? | Wait | Send it to support | New seed, then move funds | Reuse the seed | C | Treat a seed phrase entered online as compromised. Create a new wallet with a new seed, then move funds only after verifying the destination. Review Student Guide, Module 3, “Seed phrases.” |
| `BD-ML-12S` | Module 3: Custodial and non-custodial use | Custody difference? | Who controls keys | Payment reversibility | Supply limit | Responsibility | A | Custodial and self-custodial use differ in who controls the keys and carries the related responsibility. Neither guarantees safety or reversibility. Review Student Guide, Module 3, “Custodial and non-custodial use.” |

## Long question set

| ID | Module and topic | Prompt | A | B | C | D | Correct option | Shared explanation and review reference |
|---|---|---|---|---|---|---|---|---|---|
| `BD-ML-01L` | Module 1: Why money exists | Why can money help a worker buy from a later seller? | People accept it expecting others will too. | It makes all goods equally valuable. | It removes the need for rules. | It turns services into goods. | A | Money helps strangers coordinate exchange across time because people expect others to accept it later. It still depends on trust, rules, and social acceptance. Review Student Guide, Module 1, “Why money exists.” |
| `BD-ML-02L` | Module 1: Functions of money | Rice is priced, accepted in payment, then saved. Which roles apply? | Store; unit; medium | Unit; medium; store | Scarcity; scarcity; scarcity | Medium; store; unit | B | A unit of account expresses prices, a medium of exchange is accepted in payment, and a store of value moves value into the future. Review Student Guide, Module 1, “Functions and properties of money.” |
| `BD-ML-03L` | Module 1: Barter | Amina wants shoes. Luis wants oil, not her rice. What blocks a direct trade? | Different prices | No double coincidence of wants | No central-bank approval | Rice cannot be exchanged | B | Direct barter is difficult when each person does not want what the other offers at the same time. This is the double coincidence of wants. Review Student Guide, Module 1, “Barter and the double coincidence of wants.” |
| `BD-ML-04L` | Module 1: Inflation and purchasing power | Prices rise 10%; income rises 5%. What happens to purchasing power? | It rises | It stays the same | It falls | The currency name is needed | C | Purchasing power is what money can buy. If prices rise faster than income, the income buys less. Review Student Guide, Module 1, “Inflation and purchasing power.” |
| `BD-ML-05L` | Module 2: Double spending | The same digital unit is sent to two sellers. What must the system do? | Prevent double spending with a valid shared history | Make every payment private | Guarantee a rising price | Remove all fees | A | Digital information can be copied, so a money system must prevent the same unit from being spent twice and establish which transaction is valid. Review Student Guide, Module 2, “Early digital-money attempts and the double-spend problem.” |
| `BD-ML-06L` | Module 2: Decentralization | What best describes Bitcoin decentralization? | One company approves every payment | Independent participants enforce shared rules | Miners can change rules freely | Everyone has equal influence | B | Bitcoin distributes verification and rule enforcement across independent participants. Decentralization does not mean one company controls the network or that everyone has equal influence. Review Student Guide, Module 2, “Decentralization.” |
| `BD-ML-07L` | Module 2: Users, nodes, and miners | What does a Bitcoin node do? | Checks transactions and blocks against the rules | Creates bitcoin when users request it | Stores bitcoin inside a phone | Guarantees payments cannot be wrong | A | Nodes independently check Bitcoin’s rules and reject invalid data. They do not create bitcoin on request or store bitcoin inside a phone. Review Student Guide, Module 2, “Users, nodes, and miners.” |
| `BD-ML-08L` | Module 2: Bitcoin as sound digital money | Why might someone call Bitcoin sound money? | Its price always rises | Supply rules are public and limited | One company can change its rules | Payments are private | B | Some people describe Bitcoin as sound money because its supply rules are public and its issuance is limited. This is a reasoned judgment, not a promise about price or privacy. Review Student Guide, Module 2, “Bitcoin as sound digital money.” |
| `BD-ML-09L` | Module 3: Wallets | What does a Bitcoin wallet do? | Stores bitcoin inside a phone | Manages keys and signs transactions | Removes the need to protect secrets | Makes transactions reversible | B | Bitcoin is recorded on the shared ledger; a wallet manages the information used to access and use it. Review Student Guide, Module 3, “Wallets.” |
| `BD-ML-10L` | Module 3: Addresses and secrets | To receive on-chain bitcoin, what may you share? | A seed phrase | A private key | A receiving address | A wallet password | C | A receiving address can be shared for payment. Seed phrases, private keys, and passwords must remain secret. Review Student Guide, Module 3, “Addresses” and “Keys.” |
| `BD-ML-11L` | Module 3: Seed phrase exposure | A seed phrase was entered on an untrusted website. Safest next step? | Wait to see what happens | Send it to support | Create a new seed, then move funds after checking the destination | Reuse the seed in another app | C | Treat a seed phrase entered online as compromised. Create a new wallet with a new seed, then move funds only after verifying the destination. Review Student Guide, Module 3, “Seed phrases.” |
| `BD-ML-12L` | Module 3: Custodial and non-custodial use | What is the key difference between custodial and self-custodial use? | Who controls the keys | Whether payments are reversible | Whether supply is limited | Whether responsibility exists | A | Custodial and self-custodial use differ in who controls the keys and carries the related responsibility. Neither guarantees safety or reversibility. Review Student Guide, Module 3, “Custodial and non-custodial use.” |

## Authoring metadata

All source items are English, version 1.0, and require independent factual and editorial review before publication. The app question key is the authored Sanity `_key`; it must remain stable when wording changes. `correctIndex` is zero-based for the Sanity import.

| Short ID and app question key | Long ID and app question key | Objective link | Source language/version | Review status | `correctIndex` |
|---|---|---|---|---|---|
| `BD-ML-01S` / `b1-1-money-purpose-short` | `BD-ML-01L` / `b1-1-money-purpose-long` | `B1.1` | English 1.0 | Needs independent factual and editorial review | 0 |
| `BD-ML-02S` / `b1-3-money-functions-short` | `BD-ML-02L` / `b1-3-money-functions-long` | `B1.3` | English 1.0 | Needs independent factual and editorial review | 1 |
| `BD-ML-03S` / `b1-2-barter-limits-short` | `BD-ML-03L` / `b1-2-barter-limits-long` | `B1.2` | English 1.0 | Needs independent factual and editorial review | 1 |
| `BD-ML-04S` / `b1-5-purchasing-power-short` | `BD-ML-04L` / `b1-5-purchasing-power-long` | `B1.5` | English 1.0 | Needs independent factual and editorial review | 2 |
| `BD-ML-05S` / `b2-1-double-spending-short` | `BD-ML-05L` / `b2-1-double-spending-long` | `B2.1` | English 1.0 | Needs independent factual and editorial review | 0 |
| `BD-ML-06S` / `b2-2-decentralization-short` | `BD-ML-06L` / `b2-2-decentralization-long` | `B2.2` | English 1.0 | Needs independent factual and editorial review | 1 |
| `BD-ML-07S` / `b2-3-node-role-short` | `BD-ML-07L` / `b2-3-node-role-long` | `B2.3` | English 1.0 | Needs independent factual and editorial review | 0 |
| `BD-ML-08S` / `b2-4-sound-money-judgment-short` | `BD-ML-08L` / `b2-4-sound-money-judgment-long` | `B2.4` | English 1.0 | Needs independent factual and editorial review | 1 |
| `BD-ML-09S` / `b3-1-wallet-interface-short` | `BD-ML-09L` / `b3-1-wallet-interface-long` | `B3.1` | English 1.0 | Needs independent factual and editorial review | 1 |
| `BD-ML-10S` / `b3-1-address-and-secrets-short` | `BD-ML-10L` / `b3-1-address-and-secrets-long` | `B3.1` | English 1.0 | Needs independent factual and editorial review | 2 |
| `BD-ML-11S` / `b3-4-seed-phrase-exposure-short` | `BD-ML-11L` / `b3-4-seed-phrase-exposure-long` | `B3.4` | English 1.0 | Needs independent factual and editorial review | 2 |
| `BD-ML-12S` / `b3-2-custody-comparison-short` | `BD-ML-12L` / `b3-2-custody-comparison-long` | `B3.2` | English 1.0 | Needs independent factual and editorial review | 0 |

## Optional final-score messages

| Score out of 12 | Learner message |
|---|---|
| 10–12 | Great work. You have a strong foundation. Keep building your Bitcoin knowledge. |
| 6–9 | Good progress. Review the topics highlighted in your answers, then try again. |
| 0–5 | Every question is a chance to learn. Revisit the suggested Diploma sections and try the quiz again. |

## Developer notes

- Select either the `S` or `L` item from each numbered pair. Do not load both variants into the same October quiz.
- Display only one answer as correct for each selected item, then show the shared explanation and review reference after either answer outcome.
- The app must use the matching listed app question key as the question `_key`, and retain it when wording changes. Use `correctIndex` rather than the A–D label in the Sanity import; do not reorder choices without checking the index.
- Do not treat the review reference as an in-app link. The current app displays plain text only and shows every question in a quiz on the same screen.
- Do not store or share a learner’s score with an educator.
- Do not label a score pass or fail.
- Do not request seed phrases, private keys, wallet passwords, holdings, or other personal financial information.
