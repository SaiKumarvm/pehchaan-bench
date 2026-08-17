# PEHCHAAN Benchmark Specification

## 1. Overview

PEHCHAAN is a benchmark for evaluating personalized product entity resolution under code-mixed Indian commercial language.

The benchmark focuses on determining whether a product mention in a user query can be correctly resolved to the intended product entity.

---

## 2. Task Definition

Given:

- a user query written in potentially code-mixed Indian commercial language, and
- a set of candidate product entities,

the system must identify the product entity that best matches the user's intended product mention.

The task is therefore formulated as:

**Query + Candidate Entities → Predicted Product Entity**

---

## 3. Input

Each benchmark example contains:

### 3.1 User Query

A natural-language query representing a user's product-related request.

The query may contain:

- English
- An Indian language
- Code-mixed language
- Informal commercial language
- Product names or product descriptions

### 3.2 Candidate Entities

A set of product entities against which the query is evaluated.

Each candidate entity should have a stable identifier and sufficient product information for entity resolution.

---

## 4. Expected Output

For each query, the system must return:

- the identifier of the predicted product entity, or
- a designated value indicating that no candidate entity can be confidently resolved.

The benchmark must use a deterministic output format so that predictions can be evaluated automatically.

---

## 5. Code-Mixed Language

PEHCHAAN specifically considers queries containing mixed-language usage.

Examples may include combinations of:

- English + Hindi
- English + Telugu
- English + Tamil
- English + other Indian languages

The benchmark should preserve the original query text rather than requiring complete translation into a single language.

---

## 6. Benchmark Example

A benchmark record should conceptually contain:

```text
query:
    "redmi phone 20 hazaar ke andar"

candidates:
    - entity_001
    - entity_002
    - entity_003

gold_entity:
    entity_002