# Bitcoin Diploma Optional Self-Assessment: October Question Data

## Use

This file is the developer handoff for the 12-question optional My First Bitcoin app self-test. It follows the October scope and implementation constraints in [Microlearning plan](14_microlearning-plan.md). It is not formal assessment and must not be used for educator tracking, certification, or a pass/fail decision.

Each item has one correct answer and four plain-text options. After either answer outcome, show the item's shared plain-language explanation and review reference. The current app cannot show different correct and incorrect messages, rich text, media, links, or a multi-screen item flow. The review reference points to the learner's next reading in `08_student.md` and should be displayed as text.

| ID | Module and topic | Prompt | A | B | C | D | Correct option | Shared explanation and review reference |
|---|---|---|---|---|---|---|---|---|---|
| `BD-ML-01` | Module 1: Why money exists | What problem does money help solve? | It makes every good free. | It helps people exchange when direct barter is difficult. | It guarantees that prices never change. | It removes the need for trust or rules. | B | Money helps coordinate exchange when two people do not want each other’s goods at the same time. It does not make goods free or remove every risk. Review Student Guide, Module 1, “Why money exists.” |
| `BD-ML-02` | Module 1: Functions of money | Which is an example of money acting as a unit of account? | Comparing the prices of two items in the same currency. | Carrying cash from one place to another. | Checking whether a note is genuine. | Saving a paper receipt. | A | A unit of account gives people a shared way to express and compare prices. Review Student Guide, Module 1, “Functions and properties of money.” |
| `BD-ML-03` | Module 1: Barter | Why can barter become difficult? | Goods can never be exchanged directly. | People must find someone who wants what they offer and offers what they want. | Barter always requires a bank. | Barter makes every good scarce. | B | Barter can work, but it becomes difficult when people’s wants do not match. This is the double coincidence of wants. Review Student Guide, Module 1, “Barter and the double coincidence of wants.” |
| `BD-ML-04` | Module 1: Inflation and purchasing power | If the price of a basket of goods rises while your income stays the same, what usually happens to your purchasing power? | It increases. | It stays exactly the same. | It decreases. | It becomes impossible to measure. | C | Purchasing power is what an amount of money can buy. When prices rise while income stays the same, that income buys less. Review Student Guide, Module 1, “Inflation and purchasing power.” |
| `BD-ML-05` | Module 2: Double spending | Why is preventing double spending important for digital money? | It stops a person from copying the same digital unit and spending it twice. | It makes every payment private. | It guarantees that bitcoin will rise in price. | It removes all transaction fees. | A | Digital information can be copied, so a money system needs a way to prevent the same unit from being spent twice. Review Student Guide, Module 2, “Early digital-money attempts and the double-spend problem.” |
| `BD-ML-06` | Module 2: Decentralization | Which statement best describes Bitcoin decentralization? | One company approves every transaction. | Many independent participants check and enforce the network’s rules. | Miners can change any rule whenever they choose. | Every participant has exactly the same influence. | B | Bitcoin distributes verification and rule enforcement across independent participants. Decentralization does not mean one company controls the network or that everyone has equal influence. Review Student Guide, Module 2, “Decentralization.” |
| `BD-ML-07` | Module 2: Users, nodes, and miners | What does a Bitcoin node do? | It independently checks transactions and blocks against Bitcoin’s rules. | It creates a new bitcoin whenever a user asks. | It stores bitcoin inside a phone. | It guarantees that a payment will never be wrong. | A | Nodes independently check Bitcoin’s rules and reject invalid data. They do not create bitcoin on request or store bitcoin inside a phone. Review Student Guide, Module 2, “Users, nodes, and miners.” |
| `BD-ML-08` | Module 2: Supply and units | How many satoshis equal one bitcoin? | 100 | 1,000 | 1,000,000 | 100,000,000 | D | One bitcoin is divisible into 100,000,000 satoshis. A satoshi is the smallest named unit of bitcoin. Review Student Guide, Module 2, “Satoshis and unit bias.” |
| `BD-ML-09` | Module 3: Wallets | Which statement about a Bitcoin wallet is most accurate? | It stores bitcoin inside your phone. | It manages keys and helps you receive, sign, and track Bitcoin transactions. | It removes the need to protect secret information. | It guarantees that every transaction can be reversed. | B | Bitcoin is recorded on the shared ledger; a wallet manages the information used to access and use it. A wallet does not literally contain bitcoin or remove responsibility. Review Student Guide, Module 3, “Wallets.” |
| `BD-ML-10` | Module 3: Addresses and secrets | Which information is generally safe to share when you want to receive an on-chain Bitcoin payment? | Your seed phrase. | Your private key. | Your Bitcoin receiving address. | Your wallet password. | C | A receiving address can be shared for payment. Seed phrases, private keys, and passwords must remain secret. Review Student Guide, Module 3, “Addresses” and “Keys.” |
| `BD-ML-11` | Module 3: Seed phrases | A person claiming to be wallet support asks for your seed phrase to fix a problem. What is the safest response? | Share it if the person sounds professional. | Share only the first few words. | Take a photo and send it later. | Do not share it; stop and verify support independently. | D | A seed phrase can give full access to a wallet. Never share, photograph, or enter it through an unexpected request; stop and verify support independently. Review Student Guide, Module 3, “Seed phrases” and “Safety checklist: seed phrases, address checks, scams, and starting small.” |
| `BD-ML-12` | Module 3: Confirmations and verification | What does a first confirmation mean for an on-chain Bitcoin transaction? | The transaction has been included in a valid block. | The recipient has promised a refund. | The address can no longer be checked. | The transaction is private. | A | A first confirmation means a transaction has been included in a valid block. Confirmations do not reverse mistakes or make a transaction private. Review Student Guide, Module 3, “Verification, block explorers, and irreversible transactions.” |

## Authoring metadata

All source items are English, version 1.0, and require independent factual and editorial review before publication. The app question key is the authored Sanity `_key`; it must remain stable when wording changes. `correctIndex` is zero-based for the Sanity import.

| ID | App question key | Objective link | Source language/version | Review status | `correctIndex` |
|---|---|---|---|---|---|
| `BD-ML-01` | `b1-1-money-purpose` | `B1.1` | English 1.0 | Needs independent factual and editorial review | 1 |
| `BD-ML-02` | `b1-3-unit-of-account` | `B1.3` | English 1.0 | Needs independent factual and editorial review | 0 |
| `BD-ML-03` | `b1-2-barter-limits` | `B1.2` | English 1.0 | Needs independent factual and editorial review | 1 |
| `BD-ML-04` | `b1-5-purchasing-power` | `B1.5` | English 1.0 | Needs independent factual and editorial review | 2 |
| `BD-ML-05` | `b2-1-double-spending` | `B2.1` | English 1.0 | Needs independent factual and editorial review | 0 |
| `BD-ML-06` | `b2-2-decentralization` | `B2.2` | English 1.0 | Needs independent factual and editorial review | 1 |
| `BD-ML-07` | `b2-3-node-role` | `B2.3` | English 1.0 | Needs independent factual and editorial review | 0 |
| `BD-ML-08` | `b2-3-satoshi-units` | `B2.3` | English 1.0 | Needs independent factual and editorial review | 3 |
| `BD-ML-09` | `b3-1-wallet-interface` | `B3.1` | English 1.0 | Needs independent factual and editorial review | 1 |
| `BD-ML-10` | `b3-1-address-and-secrets` | `B3.1` | English 1.0 | Needs independent factual and editorial review | 2 |
| `BD-ML-11` | `b3-4-seed-phrase-scam` | `B3.4` | English 1.0 | Needs independent factual and editorial review | 3 |
| `BD-ML-12` | `b3-6-first-confirmation` | `B3.6` | English 1.0 | Needs independent factual and editorial review | 0 |

## Optional final-score messages

| Score out of 12 | Learner message |
|---|---|
| 10–12 | Great work. You have a strong foundation. Keep building your Bitcoin knowledge. |
| 6–9 | Good progress. Review the topics highlighted in your answers, then try again. |
| 0–5 | Every question is a chance to learn. Revisit the suggested Diploma sections and try the quiz again. |

## Developer notes

- Display only one answer as correct for each item, then show the shared explanation and review reference after either answer outcome.
- The app must use the listed app question key as the question `_key`, and retain it when wording changes. Use `correctIndex` rather than the A–D label in the Sanity import; do not reorder choices without checking the index.
- Do not treat the review reference as an in-app link. The current app displays plain text only and shows every question in a quiz on the same screen.
- Do not store or share a learner’s score with an educator.
- Do not label a score pass or fail.
- Do not request seed phrases, private keys, wallet passwords, holdings, or other personal financial information.
