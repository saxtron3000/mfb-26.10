# Bitcoin Diploma Optional Self-Assessment Question Bank

## Scope

This document defines a minimal, learner-owned self-assessment quiz that can be built with the app as it exists today.

The quiz is deliberately separate from formal Diploma assessment. It is learner-owned by design, so its results cannot be used for certification, passing decisions, educator tracking, or evidence that a learner has completed a practical skill.

# Phase 1 minimal viable product

## Learner purpose

Create one learner-owned **12-question** self-assessment quiz. It helps learners check their understanding of the Bitcoin Diploma and identify topics to revisit. It does not give a formal result.

## Required quiz behaviour

| Element | October requirement |
|---|---|
| Questions | Exactly 12 questions selected from Modules 1, 2, and 3. Do not include local Module 4 content. |
| Format | One multiple-choice prompt with exactly four answer options. |
| Correct answer | One clear best answer. |
| Feedback after an answer | One shared, plain-language explanation, shown after either answer outcome, with a specific Bitcoin Diploma topic to review. It may invite the learner to keep learning or continue, but the current app cannot show different correct and incorrect messages. |
| Final screen | Show a simple score out of 12, if supported, with one encouraging message. Do not label it pass or fail. |
| Data and assessment | No educator tracking, certification use, learner-progress record, practical-skills claim, or collection of personal financial information. |

## Current-app implementation constraints

The October app supports one plain-text, single-choice question with two to six choices and one correct answer. This MVP specifies four choices for every question. It can show one optional plain-text explanation after an answer and reveal the correct answer, but that explanation is the same whether the learner was correct or incorrect. It cannot show answer-specific, correct-specific, or incorrect-specific feedback.

Questions in one quiz appear on the same screen. The current item format does not support images, audio, video, links, rich text, teaching cards, or a multi-screen explanation–scenario–question–feedback flow. A review reference may therefore name the relevant Diploma section, but should not depend on the app rendering a clickable link.

The displayed score and the learner-selected completion status are local to the learner's device and are not evidence of learning. Completion is score-independent. Closing and reopening a quiz restarts it, so learners can retry, but answers, attempts, and scores are not retained or shared.

## Developer handoff record

Supply each of the 12 questions with: stable item ID and meaningful app question key; module and topic; prompt; options A–D; correct option; one shared explanation and review reference; objective link; language/source version; and review status.

For the current Sanity quiz format, map the handoff record to `_key`, `prompt`, `choices`, `correctIndex`, and optional `explanation`. `correctIndex` is the zero-based position of the correct choice. Do not reorder choices after setting it without checking the index. Keep the stable item ID and source-language relationship in the authoring record, because the current app uses separate documents for each language and does not yet link them.

Use supportive result messages such as:

- “Great work. You have a strong foundation. Keep building your Bitcoin knowledge.”
- “Good progress. Review the topics highlighted in your answers, then try again.”
- “Every question is a chance to learn. Revisit the relevant Diploma sections and try the quiz again.”

## Review checklist

Before a question enters the October quiz, confirm that it:

- uses exactly four answer options and has one clear best answer;
- links learners to a Diploma topic they can actually review;
- includes one plain-language explanation that is useful whether the learner was correct or incorrect, plus a clear review reference;
- uses simple, translation-ready language and has been independently checked for accuracy;
- has a meaningful, stable question key and an identified source-language version before translation;
- does not give financial, legal, tax, accounting, compliance, or investment advice; and
- does not request or expose seed phrases, private keys, personal financial data, or identifying information.

# Question-bank expansion

Everything below this heading is not required for the October push. It preserves the larger content bank, question-type ideas, and feature requests for later planning. Do not treat it as an October build requirement.

Use simple, translation-ready English. Keep the Diploma Bitcoin-only, educational, and free from financial, legal, tax, accounting, compliance, or investment advice. Do not turn a named wallet, exchange, tool, or local service into a global recommendation.

---

# Content-record format

Each future item should use this record:

| Field | What to record |
|---|---|
| Item ID | Stable identifier, for example `BD-ML-B01-T03-Q04`. |
| Module and topic | The location in this document. |
| Learning purpose | Recall, explain, compare, apply, or safety check. |
| Format | Any format the future app can support and that is separately approved. |
| Prompt | Clear learner-facing wording. |
| Answer or response criteria | Correct answer(s), acceptable range, or reflection guidance. |
| Feedback | Brief explanation for correct and incorrect choices; link to review content if useful. |
| Objective link | Relevant objective in `05_objectives.md`, where applicable. |
| Use | Self-assessment, recap, or discovery. Never certification evidence. |
| Review metadata | Language, difficulty, source/date for current claims, and reviewer status. |

## Item-writing rules

- Test one idea or decision at a time.
- Use only question formats that the future app can support and that are approved for the learning purpose.
- Write feedback for every option or response pattern where the future app supports it.
- Include believable distractors without using trick wording, “all of the above,” or clues based on grammar or answer length.
- Use numbers and dates only when they support a meaningful idea. Provide feedback that explains why the fact matters.
- Date and cite claims that can change. Avoid current price, policy, provider, or local-service questions unless a local, reviewed module owns them.
- Mark safety-critical misunderstandings for clear corrective feedback. Never ask learners to enter or disclose seed phrases, private keys, holdings, or financial circumstances.

## Suggested question mix

Each topic can grow into a small set of varied items: a recall or vocabulary check; a meaning, comparison, or cause-and-effect question; an applied scenario or ordering task where appropriate; and an optional reflection or discussion prompt.

---

# 2. Module 1: Understanding Money

## BD-ML-B01-T01: Opening questions about money

Themes: everyday uses of money, trust, value, exchange, and personal observation.

Question-bank opportunities:

- reflection: “What makes something useful as money in everyday life?”
- sorting: distinguish a use of money from a non-monetary use;
- short response: describe a time when exchanging goods directly would be difficult;
- multiple choice: identify an example of a medium of exchange.

## BD-ML-B01-T02: Why money exists

Themes: exchange, coordination, shared acceptance, and reducing the difficulty of barter.

Question-bank opportunities:

- multiple choice: choose the problem money helps solve;
- matching: money function to everyday example;
- scenario: identify why two people may struggle to barter;
- reflection: “What would become harder if people could not use money?”

## BD-ML-B01-T03: Functions and properties of money

Themes: medium of exchange, unit of account, store of value, divisibility, portability, durability, recognizability, fungibility, and scarcity.

Question-bank opportunities:

- matching: function or property to definition;
- multiple select: choose properties that make an item easier to use as money;
- ranking: compare two hypothetical monies using stated properties;
- short response: explain one property that matters in a local payment situation.

## BD-ML-B01-T04: Barter and the double coincidence of wants

Themes: barter limits, matching wants, time, and indirect exchange.

Question-bank opportunities:

- scenario multiple choice: identify the missing coincidence of wants;
- ordering: arrange a simple barter chain and identify where it fails;
- explanation: why can money make exchange easier than barter?

## BD-ML-B01-T05: Scarcity, time preference, and opportunity cost

Themes: limited resources, choices, trade-offs, present and future preferences.

Question-bank opportunities:

- scenario: identify the opportunity cost of a choice;
- multiple choice: choose the best example of scarcity;
- reflection: “What trade-off might a person consider when choosing between using something now and saving it for later?”

## BD-ML-B01-T06: From barter to modern money

Themes: monetary history, changing forms of money, trust, and the Nixon Shock as a historical marker.

Question-bank opportunities:

- timeline ordering: barter, commodity money, banknotes, modern fiat money;
- date question: identify the year of the Nixon Shock (1971) and explain its relevance in a short historical overview;
- matching: historical monetary form to a characteristic;
- reflection: how can the form of money change while its functions remain important?

## BD-ML-B01-T07: Fiat money and money-system roles

Themes: fiat money, central banks, commercial banks, governments, and citizens; essential system roles.

Question-bank opportunities:

- vocabulary: define fiat money in plain language;
- matching: participant to simplified role;
- multiple choice: identify a statement that distinguishes fiat money from bitcoin;
- scenario: trace a simplified money-system interaction without implying a universal local rule.

## BD-ML-B01-T08: Fractional reserve banking and bank runs

Themes: deposits, lending, liquidity, confidence, and introductory bank-run dynamics.

Question-bank opportunities:

- diagram label: identify depositors, bank, and withdrawals;
- multiple choice: identify why many simultaneous withdrawals can create a problem;
- short response: explain the role of confidence in a bank run;
- safety note: keep explanations descriptive, not personal financial guidance.

## BD-ML-B01-T09: Inflation and purchasing power

Themes: price changes, purchasing power, money supply context, and effects on everyday choices.

Question-bank opportunities:

- number problem: compare what a fixed amount can buy before and after a stated price increase;
- multiple choice: identify the meaning of purchasing power;
- chart reading: describe what happens when prices rise faster than income in a hypothetical example;
- reflection: “How might changing prices affect planning for a household or community?”

## BD-ML-B01-T10: CBDCs as digital fiat

Themes: digital fiat, centralized issuance, and distinctions from decentralized, scarce money.

Question-bank opportunities:

- compare-and-contrast: CBDC and bitcoin using only stated characteristics;
- multiple choice: identify the inaccurate claim that all digital money is decentralized;
- reflection: “Which questions would you ask before using any digital form of money?”

## BD-ML-B01-T11: Module 1 review

Themes: connections among money functions, barter, fiat systems, inflation, and the search for alternatives.

Question-bank opportunities:

- mixed retrieval set;
- scenario: explain one money problem that could lead people to seek an alternative;
- confidence check: select a topic to review before Module 2.

---

# 3. Module 2: How Bitcoin Works

## BD-ML-B02-T01: Why Bitcoin was created

Themes: peer-to-peer electronic cash, trust challenges, monetary problems, and Bitcoin’s purpose.

Question-bank opportunities:

- short response: explain one problem Bitcoin was designed to address;
- multiple choice: distinguish a purpose claim from an investment promise;
- reflection: “What would you want to verify before trusting a new form of money?”

## BD-ML-B02-T02: Search for digital and decentralized money

Themes: Cypherpunk context, digital-money experiments, and design challenges.

Question-bank opportunities:

- matching: early idea or project to its key contribution;
- timeline ordering: DigiCash, Hashcash, Bit Gold, B-money, Bitcoin (use reviewed historical dates);
- multiple choice: identify a recurring challenge for digital money;
- source note: historical facts must be reviewed and cited before release.

## BD-ML-B02-T03: Double spending and digital scarcity

Themes: copying digital information, double spending, ownership records, and credible scarcity.

Question-bank opportunities:

- scenario: identify a double-spend attempt;
- analogy check: distinguish copying a file from transferring a scarce digital unit;
- short response: why is preventing double spending important?

## BD-ML-B02-T04: Bitcoin origin timeline

Themes: whitepaper, Genesis Block, first transaction, and Pizza Day.

Question-bank opportunities:

- date matching: whitepaper (2008), Genesis Block (2009), Pizza Day (2010);
- timeline ordering: place events in chronological order;
- multiple choice: identify what the Bitcoin whitepaper introduced;
- reflection: why do origin milestones matter less than understanding how the system works today?

## BD-ML-B02-T05: Decentralization and peer-to-peer transfer

Themes: distributed participation, no single controller, direct network transfer, and trade-offs.

Question-bank opportunities:

- multiple choice: identify a decentralized-system characteristic;
- scenario: compare a centralized service and a peer-to-peer network;
- short response: explain decentralization without saying “no rules” or “no responsibility.”

## BD-ML-B02-T06: Users, nodes, miners, and developers

Themes: beginner role boundaries and network participation.

Question-bank opportunities:

- matching: role to simplified responsibility;
- multiple select: identify who can independently verify rules using a plain-language description;
- misconception check: distinguish running a node, mining, developing software, and using bitcoin;
- scenario: identify which role is relevant to a stated action.

## BD-ML-B02-T07: Proof of work

Themes: work, block production, network security, and costly signals in an accessible overview.

Question-bank opportunities:

- sequence ordering: simplified proof-of-work process;
- multiple choice: identify what proof of work helps the network do;
- short response: explain why “work” is relevant to Bitcoin’s security model;
- boundary note: detailed mining mechanics belong in Advanced material.

## BD-ML-B02-T08: Supply, halving, satoshis, and unit bias

Themes: finite supply, 21 million bitcoin, 100 million satoshis per bitcoin, halving, and units.

Question-bank opportunities:

- number conversion: convert a stated bitcoin amount to satoshis and vice versa;
- multiple choice: identify the total supply limit of bitcoin (21 million);
- date/interval question: identify the approximate halving cycle (about four years), with feedback that the calendar timing varies because halvings occur at block heights;
- misconception check: owning less than one bitcoin does not prevent use;
- reflection: how can units influence the way people think about an amount?

## BD-ML-B02-T09: Verifiability and sound digital money

Themes: open verification, predictable supply rules, digital scarcity, and monetary properties.

Question-bank opportunities:

- matching: Bitcoin characteristic to the question it helps a user ask;
- compare: state one similarity and one difference between bitcoin and fiat money;
- scenario: choose what a learner could verify rather than merely trust;
- reflection: “Why might independently checking a claim matter?”

## BD-ML-B02-T10: Personal responsibility bridge

Themes: responsibility, control, trade-offs, and preparation for self-custody.

Question-bank opportunities:

- scenario: identify when a person is relying on another party versus managing their own access;
- reflection: “What responsibilities can come with greater control?”
- readiness check: identify a question to answer before setting up a wallet.

## BD-ML-B02-T11: Module 2 review

Themes: purpose, scarcity, roles, supply, and the bridge to action.

Question-bank opportunities:

- mixed quiz with a timeline, role-match, and scenario;
- one learner explanation prompt for formative educator follow-up;
- confidence check for Module 3 preparation.

---

# 4. Module 3: Using Bitcoin Safely

## BD-ML-B03-T01: Wallets as interfaces

Themes: wallet interfaces, access, balances, transactions, and responsibility.

Question-bank opportunities:

- multiple choice: identify what a wallet does and does not store in a practical introduction;
- matching: wallet action to purpose;
- reflection: why should a learner understand an interface before using it?

## BD-ML-B03-T02: Addresses, keys, and seed phrases

Themes: public receiving addresses, private keys, seed phrases, access, and confidentiality.

Question-bank opportunities:

- sorting: information that may be shared for receiving versus information that must remain secret;
- multiple choice: identify the safety-critical item that should never be shared;
- scenario: choose the safest response to an unexpected request for a seed phrase;
- short response: explain the difference between an address and a seed phrase;
- do not ask learners to enter, photograph, or disclose a real seed phrase.

## BD-ML-B03-T03: Custodial and non-custodial use

Themes: control of keys, responsibility, trade-offs, and third-party reliance.

Question-bank opportunities:

- compare-and-contrast: custodial and non-custodial use;
- scenario: identify who controls access in a described arrangement;
- reflection: what support or responsibility trade-offs might matter to a learner?

## BD-ML-B03-T04: Hot and cold wallets

Themes: internet connection, access, convenience, and security trade-offs.

Question-bank opportunities:

- matching: hot or cold wallet to a stated characteristic;
- scenario: identify a relevant trade-off without recommending a particular product;
- multiple choice: identify the inaccurate claim that one category removes all risk.

## BD-ML-B03-T05: Recovery readiness and seed phrase testing

Themes: recovery process, approved practice conditions, backup safety, and support.

Question-bank opportunities:

- sequence ordering: safe, educator-approved recovery-readiness steps;
- multiple choice: identify an unsafe backup practice;
- scenario: select the right response when a seed phrase may have been exposed;
- educator flag: practical recovery evidence requires direct observation under `13_assessment.md`.

## BD-ML-B03-T06: Receiving bitcoin

Themes: receiving addresses, amount, network selection where relevant, and verification.

Question-bank opportunities:

- ordering: prepare to receive a small supported test amount;
- multiple choice: identify the detail needed to receive on-chain bitcoin;
- scenario: decide what to verify before sharing a receiving address;
- educator flag: app questions prepare for, but do not replace, observed practical evidence.

## BD-ML-B03-T07: Sending bitcoin and confirmations

Themes: address verification, amount, introductory fee concepts, irreversible transactions, and confirmations.

Question-bank opportunities:

- safety checklist: choose required checks before sending;
- number question: calculate a remaining balance from a stated amount and fee in a fictional example;
- scenario: identify why an address should be checked carefully;
- multiple choice: identify what a confirmation indicates in a simple scenario;
- misconception check: a transaction may be difficult or impossible to reverse once sent.

## BD-ML-B03-T08: Block explorers, public ledger, and privacy

Themes: public transaction information, block explorers, privacy trade-offs, and responsible observation.

Question-bank opportunities:

- matching: explorer field to simple meaning;
- multiple choice: identify what can be publicly visible on a blockchain;
- scenario: identify a privacy consideration before sharing transaction information;
- reflection: what is the difference between transparency of records and knowing a person’s identity?

## BD-ML-B03-T09: Safety practices and scams

Themes: seed phrase protection, address-copy risks, impersonation, urgency, verification, open-source preference, and starting small.

Question-bank opportunities:

- multiple select: identify scam warning signs;
- scenario: respond safely to an urgent message requesting credentials or a payment;
- true/false with feedback: no legitimate helper needs a learner’s seed phrase;
- ordering: pause, verify independently, seek approved support;
- reflection: “What would make you pause before acting online?”

## BD-ML-B03-T10: Acquiring and exchanging bitcoin as pathway awareness

Themes: possible pathways, custody, local variation, risks, and no financial advice.

Question-bank opportunities:

- scenario: identify a question to research before using any pathway;
- sorting: general concept versus named-provider recommendation;
- reflection: “What local safety, legal, or access question might require educator guidance?”

## BD-ML-B03-T11: Module 3 review and practical readiness

Themes: secure access, receiving, sending, checking, recovery readiness, and scam awareness.

Question-bank opportunities:

- safety-critical mixed review;
- scenario branching: identify the next safest action;
- learner self-check: mark areas needing guided practice;
- educator flag: app self-checks can guide review but never substitute for educator-led assessment.

---

# 5. Module 4: Bitcoin in Your Community

## Custom-content rule

Module 4 content is selected by the educator for the local community. Create app self-check items only after the local module, tools, safety boundaries, and sources are approved. Keep these items modular and tag them by location, language, delivery context, and review date.

## BD-ML-B04-T01: Local Bitcoin tools and resources

Themes: local discovery, trustworthy learning resources, community support, and independent verification.

Question-bank opportunities:

- scenario: choose how to evaluate a local resource without treating it as a global recommendation;
- reflection: “What makes a community resource trustworthy enough to investigate further?”
- local directory task: identify a source date and reviewer before publishing any local reference.

## BD-ML-B04-T02: Lightning payments where locally appropriate

Themes: Lightning concepts, invoices, payment flow, and local suitability.

Question-bank opportunities:

- matching: invoice, payment request, and receiving flow;
- scenario: identify a basic check before paying an invoice;
- compare: on-chain and Lightning at a high-level overview;
- boundary note: use only approved, current local content and avoid provider endorsement.

## BD-ML-B04-T03: Everyday spending, receiving, earning, and saving scenarios

Themes: practical use cases, choices, trade-offs, and personal context.

Question-bank opportunities:

- scenario: compare payment or receiving options using stated criteria;
- reflection: “Which trade-off matters most in this fictional situation, and why?”
- matching: use case to a relevant consideration such as fees, timing, custody, or access.

## BD-ML-B04-T04: Local pathways and trade-offs

Themes: exchanges, peer-to-peer pathways, ATMs, KYC and no-KYC considerations, and local constraints.

Question-bank opportunities:

- scenario: identify questions a learner should ask about a local pathway;
- compare: stated privacy, access, custody, and safety trade-offs;
- reflection: “What information should be verified locally before acting?”
- safety note: no item should advise a learner to evade laws, policies, or safeguards.

## BD-ML-B04-T05: Merchant, remittance, donation, and community cases

Themes: merchant payments, cross-border payments, nonprofit donations, underbanked access, and circular economies.

Question-bank opportunities:

- case analysis: identify the problem, possible Bitcoin use, and trade-offs;
- matching: community use case to a relevant operational question;
- reflection: “How could a community test whether a proposed use is genuinely helpful?”

## BD-ML-B04-T06: Local monetary problems and community problem-solving

Themes: local context, evidence, claims, limitations, and respectful discussion.

Question-bank opportunities:

- claim/evidence/trade-off prompt;
- scenario: distinguish a local observation from an unsupported general claim;
- reflection: “What would you need to learn before concluding that Bitcoin is useful for a local problem?”

## BD-ML-B04-T07: Module 4 review and local competency preparation

Themes: locally selected application, trade-offs, safety, and educator-observed practical evidence.

Question-bank opportunities:

- local scenario review;
- learner explanation prompt for formative educator follow-up;
- confidence check and next-step resource selection;
- educator flag: the required local practical competency is assessed under `13_assessment.md` and certification eligibility under `15_certification.md`.

---

# Post-October wish list: future features and design questions

None of these features is required for the October quiz. They are a simple idea bank for later selection and prioritization.

## Learning content and question types

- A larger question bank across all four Diploma modules.
- Random question selection from a bank.
- Different quiz versions so learners can revisit content without seeing the same questions every time.
- Single-choice multiple-choice questions.
- Multiple-select questions.
- True/false questions.
- Missing-word or fill-in-the-blank questions.
- Matching questions.
- Ordering and timeline questions.
- Number and date questions.
- Short written responses.
- Scenario questions, including multi-step scenarios and branching choices.
- Questions with images, diagrams, audio, video, links, or other media.
- Accessible captions, transcripts, audio alternatives, and descriptive text for any future media.
- Short teaching cards before a question.
- Multi-screen learning items: explanation, scenario, question, then feedback.
- A mix of recall, vocabulary, comparison, cause-and-effect, application, safety checks, confidence checks, and local examples.
- Question sets tailored to a particular topic, module, or learning objective.
- A shared Core bank plus locally selected Module 4 content.

## Feedback, review, and reflection

- Feedback for each individual answer option.
- One general correct or incorrect message where answer-specific feedback is not needed.
- Immediate feedback, delayed feedback, or educator-selected feedback timing.
- Explanations of why an answer is correct or incorrect.
- Direct links from feedback to the relevant Diploma section for review.
- Optional answer reveals after an attempt or after all attempts.
- Learner confidence checks and suggested next steps.
- Private self-reflection prompts with no correct answer.
- Reflection responses saved only when the learner chooses to save them.
- Discussion prompts for educator-led sessions.
- AI-supported reflection or discussion prompts that help a learner think further without collecting sensitive information or presenting the AI response as authoritative advice.
- AI-supported prompts that help educators prepare follow-up discussion questions.

## Learner flow and self-assessment

- Topic and module scores in addition to a whole-quiz score.
- Supportive score messages and suggested review paths.
- Learner retries, with configurable attempt limits.
- Question randomization on retries.
- Controls for when feedback and correct answers appear.
- Completion status separated from score or passing status.
- Optional learning paths that unlock one topic or module after another.
- Learner-visible progress tracker across questions, topics, and modules.
- Flags for repeated incorrect answers, especially for safety-critical concepts.
- Learner-controlled review of missed concepts and suggested next steps.
- Offline or weak-connectivity use, with safe synchronization when access returns.
- Recovery from interrupted attempts or app outages.

## Educator, cohort, and assignment features

- Educator accounts and educator-facing dashboards.
- Cohort, class, and group management.
- A way for educators to add learners to a cohort.
- A way for educators to pair a learner with an educator or approved assessor.
- Assignable individual questions, topic sets, module sets, or custom question banks.
- Due dates, completion expectations, and reminders for assigned work.
- Educator view of learner progress, answers, attempts, confidence checks, and review needs.
- Educator notes and learner-support flags.
- Educator-led discussion-only or follow-up-required items.
- Educator review of written responses and reflections when the learner has consented.
- Educator observation records for approved practical tasks, kept separate from quiz results.
- Approved educator overrides or corrections, with an audit record.
- Cohort-level reporting to identify common learning gaps.
- Exportable reports in formats such as CSV, spreadsheet, API, PDF, or dashboard.

## Objectives, assessment, and Diploma integration

- Stable mapping from every question to one or more Diploma learning objectives.
- A coverage check showing which objectives have enough valid learning and question support.
- Tags for recall, explanation, comparison, application, reflection, safety, practice, and educator follow-up.
- Tags for module, topic, difficulty, language, location, source, review date, and content owner.
- A future formal-assessment mode only after tracking, scoring, privacy, and educator workflows are approved.
- Configurable passing scores by topic, module, or full course.
- Clear separation between completion, self-assessment, quiz score, theoretical assessment, and educator-observed practical competence.
- A way to combine approved app and educator evidence without allowing one component to replace required practical observation.
- Support for practical-task preparation, checklists, and follow-up questions without claiming that the app alone assessed a practical skill.

## Content management and quality control

- Import questions through CSV, spreadsheet, JSON, API, Markdown, or a content-management interface.
- A sample import file and a published list of required content fields.
- Stable item IDs that remain in place when wording changes.
- A clear format for answer options, correct answers, answer order, and multiple correct answers.
- Explicit option IDs and correct-answer markers so answer choices can be reordered safely.
- Several accepted answers for approved short-response questions.
- Draft, review, approval, publication, retirement, and version-control statuses.
- Update a question without breaking historical learner records.
- Item review history, scoring-version controls, and audit trails.
- Fact, date, calculation, and feedback review before publication.
- Local-content ownership, location tags, review dates, and source trails.
- Import validation for required fields, one clear correct answer, duplicate items, required feedback, translation links, and broken review references.

## Language, accessibility, privacy, and safety

- Multiple language versions connected to one stable item ID.
- Support for right-to-left languages and non-Latin scripts.
- Translation-ready source content and language-parity checks.
- Screen-reader support, keyboard navigation, captions, text resizing, contrast, and audio alternatives; do not rely on colour alone to communicate correctness, and announce new feedback when it appears.
- Screen-reader and colour-contrast testing of quiz interactions, including a labelled radio-group pattern for answer choices.
- Supported device, browser, and operating-system guidance.
- Shared-device, loan-device, assisted-use, and learner-account models.
- Clear rules for what learner data is stored, who can see it, and how long it is retained.
- If learner data is ever shared with educators, a separate data model with informed consent, access control, retention/deletion rules, and audit trails.
- Learner controls to delete saved reflections or other personal data.
- Consent, privacy, identity, assessment-integrity, and minors’ access controls where relevant.
- A design that never asks for seed phrases, private keys, holdings, or unnecessary financial or identifying information.
- Safety-critical feedback and referral to approved support where a learner repeatedly selects an unsafe response.
