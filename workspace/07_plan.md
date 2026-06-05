# Bitcoin Diploma Redesign Plan

## Purpose

This document defines the working plan for redesigning the Bitcoin Diploma.

It focuses on:

- how the redesigned Diploma should use limited in-class time;
- what content and learning experiences should stay in the core Diploma;
- what should leave the core Diploma;
- how activities will be separated into a dedicated Activity Bank;
- how the redesigned materials should support educators and learners.

This document should be read alongside:

- `03_design-7.md` for design principles;
- `04_objectives-7.md` for learning objectives and competencies;
- `09_activities.md` for the future Activity Bank;
- `10_guide.md` for the future Educator Guide.

---

# 1. Planning Aim

The redesigned Bitcoin Diploma should become shorter, clearer, more practical, and easier to teach while preserving the educational seriousness and identity of the original Diploma.

The working design direction is:

- in-person first;
- approximately 8-hour maximum completion pathway;
- 4-block structure: Problem / Fiat, Solution / Bitcoin, Action / Self-custody, and Custom / Bitcoin as Money;
- approximately 2 hours per block;
- one core Diploma with Custom and Advanced pathways;
- Core / Custom / Advanced content separation;
- practical learning increased;
- advanced technical content removed from the beginner pathway;
- educator support strengthened;
- activities separated into a dedicated Activity Bank.

---

# 2. Key Design Insight From Review

The review of the current Diploma and reduced syllabus exposes a central design tension:

The current Diploma is trying to do three jobs at once.

1. Explain why Bitcoin exists.
2. Teach people how to use Bitcoin.
3. Teach people how Bitcoin works.

All three jobs matter, but combining them without clear boundaries has contributed to a course that is comprehensive but long, difficult to teach consistently, and vulnerable to learner drop-off.

The reduced syllabus reveals a natural beginner structure:

- Problem / Fiat: why fiat money creates the problem Bitcoin responds to.
- Solution / Bitcoin: what Bitcoin is, why it works, and why it is different.
- Action / Self-custody: how learners take responsibility for using and securing Bitcoin.

The redesign should preserve this natural structure through four blocks: Problem / Fiat, Solution / Bitcoin, Action / Self-custody, and Custom / Bitcoin as Money. The fourth block is selected by the educator and should help learners understand how Bitcoin can function as money in their local context.

---

# 3. Working Core Table Of Contents

The following table of contents is adapted from the archived Gabe core outline and updated to the active four-block structure.

It should be treated as a working core structure, not a final curriculum specification. Activities listed here should be extracted from the student-facing core and developed in the separate Activity Bank.

## 3.1 Layer 1 / Core

### Block 1: Problem / Fiat

Core question:

What problem does fiat money create?

- Welcome to My First Bitcoin
  - Overview of the organization, origins, and mission
  - Introduction to the Bitcoin Diploma and program roadmap
  - Requirements to obtain a diploma
- Discussion: Questions about money
  - Why do we need money?
  - What is money?
  - Who controls the money?
  - What gives money its value?
  - What questions do you have about money?
- What is money?
  - Functions of money
    - Medium of exchange
    - Store of value
    - Unit of account
  - Characteristics of money
    - Divisibility
    - Acceptability
    - Fungibility
    - Durability
    - Portability
    - Scarcity
- Activity Bank item: Are these good forms of money?
- Reflection: Evolution of money
- Activity Bank item: Barter
- Reflection: Money has no intrinsic value
- Psychology of money
  - Scarcity
  - Time preference
  - Opportunity cost
- Quick history of money
  - One timeline covering key transitions, successes, and failures
- How does the system currently work?
  - Introduction to the fiat system
- Fractional reserve banking
  - Explanation of the concept
  - Activity Bank item: quick activity
- Inflation and money devaluation
- Who controls the fiat system?
  - Governments
  - Wealthy individuals
  - Commercial banks
  - Central banks
- Future of the fiat system
  - CBDCs

Outcome:

Students can explain why societies use money and identify beginner-level weaknesses in fiat monetary systems.

### Block 2: Solution / Bitcoin

Core question:

Why was Bitcoin created, and how does it respond to fiat money problems?

- The search for a solution
  - Introduction to the cypherpunks
- Centralized vs decentralized systems
- Quick history of digital currencies
  - Ecash
  - Digicash
  - B-money
  - Hashcash
  - Bitgold
  - E-gold
  - Common objectives and points of failure
- Welcome to Bitcoin
  - The cryptography mailing list
  - Bitcoin whitepaper
  - Quick history and timeline
    - Whitepaper
    - Genesis block
    - First transaction
    - Pizza Day
  - Today Bitcoin is:
    - decentralized;
    - digital;
    - peer to peer;
    - finite.
- How does Bitcoin work?
  - 3 core participants
    - Users
    - Nodes
    - Miners
  - Quick explanation of proof of work
- 21 million limit
  - "It's just math"
  - Halving
- Sound money
- Bitcoin divisibility
  - What are satoshis?
- How does a transaction work?
  - Overview of the process
- Activity Bank item: Let's build a blockchain
- Reflection: How does Bitcoin meet the characteristics of money?
- How do accounts work in Bitcoin?
  - Bitcoin is not attached to a name
  - Bitcoin lives in addresses on the blockchain
  - Analogy: addresses are like lockers, and you hold the keys
  - What are keys?
    - Keys before vs "keys" now
    - Seed phrase
  - Tree structure and unidirectional nature
    - Seed
    - Private keys
    - Public keys
    - Addresses
- Quick introduction to Bitcoin wallets
  - A wallet is an interface that lets learners:
    - see a bitcoin balance by checking the ledger;
    - send bitcoin by signing transactions;
    - receive bitcoin by generating addresses.

Outcome:

Students can explain Bitcoin's purpose and how it differs from fiat money.

### Block 3: Action / Self-custody

Core question:

How do I take responsibility for using and securing Bitcoin?

- Custodial vs non-custodial wallets
  - Custodial
    - The learner has an account or identifier within an app's database.
    - The app allows the learner to view a bitcoin balance and send or receive bitcoin.
    - Useful for daily spending.
    - Not appropriate for savings if the learner does not hold their own keys.
  - Non-custodial
    - The learner holds their own keys.
    - The learner has 12 or 24 words that give control over their bitcoin.
    - The app or device allows the learner to view a balance and send or receive bitcoin.
    - Useful for savings and, depending on the app, possibly daily spending.
- Hot vs cold wallets
  - Hot wallets
    - The seed phrase is generated and kept on a device that can connect to the internet.
    - These apps allow learners to create a seed phrase, view a balance, and send or receive bitcoin.
    - They are not automatically insecure, but they have a larger attack surface than cold wallets.
  - Cold wallets
    - The seed phrase is generated and transactions are signed while remaining offline.
    - Hardware wallets are a stronger option for securing bitcoin.
- Practical route options
  - Activity Bank item: hot wallet setup and send/receive using testnet or signet
  - Activity Bank item: cold wallet setup and send/receive using testnet or signet
- Receiving bitcoin
- Sending bitcoin
- Verification
- Basic Lightning
- Everyday use

Outcome:

Students can explain beginner self-custody concepts and complete guided actions related to receiving, storing, and sending bitcoin where practical activities are included.

### Block 4: Custom / Bitcoin as Money

Core question:

How can Bitcoin function as money in this community?

- This block is chosen by the educator.
- Educators are community leaders and are best positioned to understand:
  - student situations;
  - local needs;
  - local risks;
  - available tools;
  - community requirements;
  - realistic opportunities for Bitcoin use.
- The curriculum should provide a bank of Custom modules from which educators can choose.
- Most of this block should focus on practical workshops and demonstrations.
- Possible Custom module topics:
  - daily spending;
  - local wallet tools;
  - Lightning payments;
  - receiving bitcoin;
  - sending bitcoin;
  - merchant payments;
  - buying and selling bitcoin in the community;
  - KYC vs no-KYC;
  - centralized vs peer-to-peer pathways;
  - circular economies;
  - local Bitcoin projects;
  - Bitcoin Beach-style case studies;
  - CBDCs and local monetary futures;
  - sovereignty and personal responsibility;
  - practical solutions Bitcoin may present to the community.
- Possible local wallet and tool demonstrations:
  - Blink
  - Manna
  - Aqua
  - Bull Bitcoin
  - Blitz

Outcome:

Students become familiar with practical Bitcoin tools and resources used by local bitcoiners and can identify beginner-appropriate ways Bitcoin can function as money in their daily life and community.

## 3.2 Layer 2 / Advanced

Layer 2 / Advanced content is identified as a future section, but the detailed structure still needs to be defined.

Advanced content should not overload the beginner core pathway. It should be separated into optional extensions, advanced appendices, separate workshops, or educator background notes.

Candidate advanced module titles:

- History of Money
- Monetary Economics
- History of Bitcoin
- Philosophy of Bitcoin
- Transactions & Settlement
- Mining & Consensus
- Privacy & Security
- Payments & Exchange
- Bitcoin for Business
- Infrastructure & Maintenance
- Communities & Circular Economies
- Money & Society
- Money & Human Rights
- Energy & Mining
- Open Source Software
- Nostr & Decentralized Communication
- Communication Networks
- Bitcoin Education
- Bitcoin for Families
- Bitcoin for Organizations
- Cryptography
- Computer Science Fundamentals

---

# 4. Custom Bitcoin As Money Module Bank

The Custom / Bitcoin as Money block should be built from a bank of educator-selectable modules.

Educators should decide which Custom / Bitcoin as Money modules complete the Diploma in their context because they understand their students, communities, constraints, risks, and opportunities better than a centralized curriculum team can.

## 4.1 Purpose Of The Custom Bitcoin As Money Module Bank

The Custom Bitcoin As Money Module Bank should:

- help educators complete Block 4: Custom / Bitcoin as Money;
- support local relevance;
- introduce ways students can use Bitcoin as money in daily life;
- show practical solutions Bitcoin may present to the community;
- help educators identify opportunities where Bitcoin can empower their community;
- provide practical workshops and demonstrations;
- preserve the shared core while allowing local adaptation.

## 4.2 Educator Responsibility

For the Custom block, the educator should identify:

- what local money problem or Bitcoin-as-money opportunity the Custom module addresses;
- why the topic matters for their students;
- which tools and resources local bitcoiners actually use;
- what learners need in order to use or understand those tools safely;
- what risks or limitations learners should recognize;
- what practical demonstration or workshop will best support learning;
- what realistic next step learners can take after the session.

The educator should present what is required to achieve the local learning goal, including tools, preparation, safety considerations, and local context.

## 4.3 Template Custom Bitcoin As Money Units

The redesign should provide template units that help educators build content for their students.

Each template unit should include:

- unit title;
- local problem or opportunity;
- learner profile;
- required prior knowledge;
- tools or resources used locally;
- practical workshop or demonstration;
- safety warnings;
- educator preparation;
- learner task;
- discussion prompts;
- local adaptation notes;
- evidence of learning;
- optional extension.

## 4.4 Custom Bitcoin As Money Module Examples

Possible Custom / Bitcoin as Money modules include:

- using a local Lightning wallet;
- receiving a payment;
- sending a payment;
- buying bitcoin locally;
- selling bitcoin locally;
- accepting bitcoin as a merchant;
- comparing custodial and non-custodial tools used locally;
- joining or building a circular economy;
- using Bitcoin during currency instability;
- understanding CBDCs in the local context;
- mapping local Bitcoin resources;
- evaluating a Bitcoin community project;
- planning safe next steps for personal Bitcoin use.

Most Custom / Bitcoin as Money modules should be practical workshops or demonstrations rather than lecture-heavy lessons.

---

# 5. Maximizing In-Class Time

In-class time should be used for the learning experiences that benefit most from live facilitation, peer discussion, guided practice, and educator support.

The redesigned Diploma should avoid using valuable class time for material learners can reasonably read, watch, or review independently.

## 5.1 Use Class Time For High-Value Learning

In-class time should prioritize:

- discussion;
- questions;
- misconception correction;
- guided practice;
- scenario analysis;
- group activities;
- peer explanation;
- reflection;
- local application;
- educator-led synthesis.

Class time should be treated as a space for thinking, not only receiving information.

## 5.2 Move Low-Interaction Content Out Of Class

The following should be minimized during live sessions:

- long readings;
- extended lectures;
- duplicated explanations;
- dense technical background;
- long definitions without application;
- advanced optional content;
- content that does not directly support the session objective.

Where possible, these should become:

- pre-reading;
- optional extension material;
- educator notes;
- glossary entries;
- advanced appendices;
- self-study material.

## 5.3 Design Every Session Around Active Learning

Each block should include a clear rhythm:

1. Short presentation of the core idea.
2. Guided discussion or concept check.
3. Practice through scenario, activity, or comparison.
4. Production task where learners explain, decide, apply, or reflect.
5. Review point connecting the block to the wider Diploma.

This aligns practical learning with PPP:

- Presentation: learners encounter the idea.
- Practice: learners work with the idea.
- Production: learners use the idea independently or socially.

## 5.4 Keep Educator Talk Focused

Educator explanation should be short, purposeful, and connected to learner action.

Educator talk should:

- introduce concepts clearly;
- frame activities;
- correct misconceptions;
- connect ideas across blocks;
- support learner reasoning;
- close loops after discussion.

Educator talk should not become the main learning mode for the entire session.

## 5.5 Build In Reusable Classroom Patterns

To reduce educator workload and increase consistency, the Diploma should use repeatable classroom patterns such as:

- think-pair-share;
- claim / evidence / reasoning;
- scenario analysis;
- compare and contrast;
- misconception check;
- exit ticket;
- local relevance reflection;
- explain it to a beginner;
- trade-off mapping.

These patterns should be explained in the Educator Guide and supplied through the Activity Bank.

---

# 6. What Stays In The Core Diploma

The core Diploma should contain the content and experiences required for every learner to meet the main learning objectives.

The core should stay focused, coherent, and beginner-appropriate.

## 6.1 Core Concepts

The following should stay in the core Diploma:

- money;
- value;
- scarcity;
- time preference;
- opportunity cost;
- trade;
- functions of money;
- properties of money;
- barter limitations;
- monetary systems;
- fiat systems;
- inflation;
- purchasing power;
- economic reasoning;
- cypherpunk origins;
- decentralization;
- Bitcoin history;
- Bitcoin fundamentals;
- Bitcoin's fixed supply;
- halving;
- nodes;
- miners;
- proof of work;
- sound money;
- Bitcoin as monetary technology;
- wallets;
- keys;
- seed phrases;
- beginner custody concepts;
- receiving bitcoin;
- sending bitcoin;
- verification;
- on-chain and Lightning distinctions at a beginner level;
- risks, criticisms, and limitations;
- practical safety considerations;
- personal and local relevance.

## 6.2 Core Learning Experiences

The following should stay in the core Diploma:

- structured discussion;
- guided reflection;
- concept checks;
- practical orientation;
- real-world scenarios;
- local application;
- beginner-level trade-off analysis;
- peer explanation;
- review and synthesis.

## 6.3 Core Design Features

The following should stay:

- open-source access;
- community-driven delivery;
- grassroots adaptability;
- Bitcoin-only educational focus;
- learner autonomy;
- educator empowerment;
- conceptual progression;
- coherent narrative from money to Bitcoin to practical responsibility.

---

# 7. What Leaves The Core Diploma

Some material should leave the core Diploma so that beginner learners can complete the course with clarity and confidence.

Leaving the core does not always mean removal from the ecosystem. Some material should move to optional, advanced, educator-facing, or activity-bank materials.

## 7.1 Move To Optional Or Advanced Material

The following should generally leave the beginner core pathway:

- advanced technical explanations;
- UTXO model;
- deep protocol details;
- excessive mining technical depth;
- complex cryptography;
- hash functions;
- digital signatures;
- detailed mining mechanics;
- mempool;
- transaction lifecycle;
- difficulty adjustment;
- advanced node operation;
- advanced custody models;
- detailed monetary theory not required for beginner competence;
- detailed Federal Reserve history;
- Bretton Woods;
- Nixon Shock;
- Basel III;
- fiscal policy;
- monetary policy;
- advanced Lightning routing;
- channel mechanics;
- capacity discussions;
- throughput comparisons;
- extended historical material not required for the block objective;
- content that is interesting but not essential.

These may become:

- optional learner extensions;
- advanced appendices;
- separate workshops;
- educator background notes;
- self-study recommendations.

## 7.2 Move To The Educator Guide

The following should move out of learner-facing core material and into the Educator Guide:

- facilitation instructions;
- timing guidance;
- setup notes;
- classroom management guidance;
- misconception notes;
- adaptation advice;
- suggested prompts;
- debrief guidance;
- educator preparation notes.

## 7.3 Move To The Activity Bank

Activities should be removed from the main student-facing Diploma document and organized in a separate Activity Bank.

This includes:

- group activities;
- discussion prompts;
- simulations;
- role plays;
- scenario exercises;
- reflection tasks;
- practical demonstrations;
- review games;
- exit tickets;
- extension activities;
- optional local adaptation activities.

The student-facing Diploma should refer to activities where needed, but the full activity instructions should live separately.

---

# 8. Separate Activity Bank

A separate Activity Bank will be created as part of the redesigned learning ecosystem.

The Activity Bank should make the Diploma easier to teach, adapt, and maintain.

## 8.1 Purpose Of The Activity Bank

The Activity Bank should:

- maximize in-class participation;
- give educators flexible teaching options;
- support different class sizes and contexts;
- separate facilitation detail from learner content;
- allow activities to be updated without rewriting the full Diploma;
- support localization through adaptable examples;
- preserve shared learning outcomes while allowing local variation.

## 8.2 Activity Bank Structure

Each activity should include:

- activity title;
- block alignment;
- objective alignment;
- competency alignment;
- estimated time;
- materials needed;
- delivery mode;
- class size suitability;
- educator instructions;
- learner instructions;
- debrief questions;
- adaptation options;
- low-tech or offline alternative;
- advanced extension, if applicable.

## 8.3 Activity Categories

The Activity Bank should include activity types such as:

- warm-ups;
- concept checks;
- discussion activities;
- scenario analysis;
- practical exercises;
- custody decision exercises;
- claim evaluation;
- trade-off mapping;
- local context reflection;
- review activities;
- formative assessment activities;
- extension activities.

## 8.4 Relationship To The Student Book

The Student Book should remain focused on:

- core explanations;
- essential concepts;
- learner reflection;
- key diagrams or examples;
- block summaries;
- next-step prompts.

It should not carry full facilitation instructions or a large number of embedded classroom activities.

## 8.5 Relationship To The Educator Guide

The Educator Guide should explain:

- when to use activities;
- how to choose activities;
- how to adapt activities;
- how to debrief activities;
- how activities support objectives;
- how activities connect across blocks.

The Activity Bank provides the activities themselves.

The Educator Guide helps educators use them well.

---

# 9. October Redesign Output

The October 2026 redesign should produce a complete beginner Diploma that can serve as the entry point into the wider My First Bitcoin learning pathway.

The finished Diploma should be:

- 4-block structure: Problem / Fiat, Solution / Bitcoin, Action / Self-custody, and Custom / Bitcoin as Money;
- approximately 2 hours per block;
- approximately 8 hours total;
- organized around clear learning objectives;
- supported by strong educator activities;
- structured with consistent timing;
- practical in every block;
- supported by a final assessment;
- connected to Custom and Advanced pathways.

The Diploma should not try to contain every valuable Bitcoin topic. The redesign should preserve the Diploma as the entry point while moving deeper technical, economic, and Lightning material into follow-on courses.

---

# 10. Follow-On Course Pathways

The current Diploma contains enough valuable material for several courses rather than one beginner program.

The redesigned learning ecosystem should eventually distinguish between:

1. Bitcoin Fundamentals

This is the redesigned Bitcoin Diploma.

Purpose: entry-level understanding of fiat problems, Bitcoin as the solution, self-custody as action, and Bitcoin as money in local life.

2. Bitcoin Self-Custody

Purpose: deeper practical training on wallets, keys, seed phrases, hardware wallets, backups, inheritance, verification, and operational security.

3. Lightning Network

Purpose: deeper study of Lightning, routing, channel mechanics, liquidity, capacity, everyday payments, and Lightning trade-offs.

4. Bitcoin Technical Foundations

Purpose: deeper technical study of UTXOs, cryptography, hash functions, digital signatures, mempool, transaction lifecycle, mining mechanics, nodes, and difficulty adjustment.

5. Bitcoin Economics

Purpose: deeper study of monetary history, monetary policy, fiscal policy, central banking, Bretton Woods, Nixon Shock, Basel III, time preference, incentives, and Austrian economic concepts.

These pathways should reduce overload in the core Diploma while creating a more coherent long-term education system.

---

# 11. Planning Questions To Resolve

The following questions need to be resolved as the redesign continues:

- What exactly counts as Core, Custom, and Advanced?
- What Custom / Bitcoin as Money modules should be included in the Custom Module Bank?
- What criteria should educators use when choosing Custom / Bitcoin as Money modules?
- What template unit format best helps educators build locally relevant content?
- Which activities are required, recommended, or optional?
- Which activities work in low-connectivity classrooms?
- Which activities are safe for beginner practical learning?
- What minimum practical competence should every learner demonstrate?
- How much pre-reading can reasonably be expected?
- What should be included in the Student Book versus the Educator Guide?
- What assessment evidence should be built into the activity design?
- What content must remain standardized across all communities?
- What can be localized without weakening the Diploma?
- How should the final assessment work in an 8-hour in-person format?
- Which topics should become named follow-on courses rather than optional appendices?

---

# 12. Working Planning Principle

The redesigned Diploma should use class time for what class time does best:

- conversation;
- reasoning;
- practice;
- feedback;
- reflection;
- local application;
- shared learning.

Content should support those experiences, not crowd them out.
