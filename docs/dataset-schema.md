# PEHCHAAN Dataset Schema

## 1. Purpose

This document defines the structure of a single PEHCHAAN benchmark record.

The schema is designed to support personalized product entity resolution for code-mixed Indian commercial queries.

---

## 2. Record Structure

Each benchmark record contains the following fields:

| Field | Type | Required | Description |
|---|---|---|---|
| `id` | string | Yes | Unique identifier for the benchmark example |
| `query` | string | Yes | Original user query |
| `candidates` | array | Yes | Candidate product entities considered for resolution |
| `gold_entity_id` | string | Yes | Identifier of the correct product entity |
| `split` | string | Yes | Dataset split: `train`, `validation`, or `test` |

---

## 3. Candidate Entity Structure

Each candidate product entity contains:

| Field | Type | Required | Description |
|---|---|---|---|
| `entity_id` | string | Yes | Unique product entity identifier |
| `product_name` | string | Yes | Product name |
| `brand` | string | No | Product brand |
| `category` | string | No | Product category |
| `description` | string | No | Additional product information |

---

## 4. Example Record

```json
{
  "id": "example_001",
  "query": "redmi phone 20 hazaar ke andar",
  "candidates": [
    {
      "entity_id": "entity_001",
      "product_name": "Redmi Note 13",
      "brand": "Redmi",
      "category": "smartphone",
      "description": "Redmi smartphone"
    },
    {
      "entity_id": "entity_002",
      "product_name": "Redmi Note 13 Pro",
      "brand": "Redmi",
      "category": "smartphone",
      "description": "Redmi smartphone with upgraded specifications"
    },
    {
      "entity_id": "entity_003",
      "product_name": "Samsung Galaxy A15",
      "brand": "Samsung",
      "category": "smartphone",
      "description": "Samsung smartphone"
    }
  ],
  "gold_entity_id": "entity_002",
  "split": "train"
}