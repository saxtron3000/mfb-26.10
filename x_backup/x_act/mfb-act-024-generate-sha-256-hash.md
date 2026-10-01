# Generate SHA-256 Hash
## Keywords
**SHA-256** **Hashing** **Digital signature**

## Activity Type
Online exercise

## Participation

## Duration

## Objective

- Participants observe that SHA-256 hashes are repeatable, fixed in length, and highly sensitive to input changes.

## Description
Participants use an online SHA-256 generator to hash a message, repeat the same input, and then alter the message slightly. Comparing the results shows that identical inputs produce identical fixed-length outputs while small changes produce very different hashes, supporting later discussion of one-way hash functions and [proof of work](../mfb-lx-26.10.md#term-proof-of-work).

> **Callout – Use fictional, non-sensitive text only**
>
> Never paste a seed phrase, private key, password, recovery code, personal information, or a real financial record into an online hash tool.
## Preparation

### Materials
- Internet access.

### Setup
Explain that hashing turns a digital message into a fixed-length code that acts as a unique identifier.
## Procedure

### Step 1
Open the SHA-256 online generator and generate a hash for a string or input value.
### Step 2
Generate the hash again using the same message and compare the result.
### Step 3
Change the message slightly and observe that the code is completely different. Compare the lengths of hashes from differently sized inputs.
## Review

### Key points
The same message produces the same hash; small changes produce a very different hash; output length is fixed.
## Discussion questions

# Notes

**Diploma assessment link:** May provide the individual-response context for [`T2` / `C2`](../mfb-bd-26.10/mfb-bd-assessment-grid-26.10.md#what-learners-can-show), specifically proof-of-work preparation. Use the approved protocol and required rule-and-role explanation; otherwise, this activity is formative.

Hash functions are described as one-way methods.
# Additional resources
[SHA-256 Online Generator](https://tools.keycdn.com/sha256-online-generator) is the browser-based tool used in this activity to create and compare SHA-256 hashes from learner-entered text.
