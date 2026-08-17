import json

import pytest

from pehchaan.dataset import load_jsonl, validate_record


def valid_record():
    return {
        "id": "example_001",
        "query": "redmi phone 20 hazaar ke andar",
        "candidates": [
            {
                "entity_id": "entity_001",
                "product_name": "Redmi Note 13",
                "brand": "Redmi",
                "category": "smartphone",
                "description": "Redmi smartphone",
            },
            {
                "entity_id": "entity_002",
                "product_name": "Redmi Note 13 Pro",
                "brand": "Redmi",
                "category": "smartphone",
                "description": "Redmi smartphone with upgraded specifications",
            },
        ],
        "gold_entity_id": "entity_002",
        "split": "train",
    }


def test_validate_valid_record():
    record = valid_record()

    validate_record(record)


def test_validate_missing_required_field():
    record = valid_record()
    del record["query"]

    with pytest.raises(ValueError, match="Missing required record fields"):
        validate_record(record)


def test_validate_invalid_split():
    record = valid_record()
    record["split"] = "invalid"

    with pytest.raises(ValueError, match="split"):
        validate_record(record)


def test_validate_invalid_candidate():
    record = valid_record()
    record["candidates"][0]["product_name"] = 123

    with pytest.raises(ValueError, match="product_name"):
        validate_record(record)


def test_validate_invalid_gold_entity_id():
    record = valid_record()
    record["gold_entity_id"] = "entity_999"

    with pytest.raises(ValueError, match="gold_entity_id"):
        validate_record(record)


def test_validate_duplicate_candidate_ids():
    record = valid_record()
    record["candidates"][1]["entity_id"] = "entity_001"

    with pytest.raises(ValueError, match="Duplicate candidate"):
        validate_record(record)


def test_load_jsonl(tmp_path):
    file_path = tmp_path / "sample.jsonl"

    records = [
        valid_record(),
    ]

    with file_path.open("w", encoding="utf-8") as file:
        for record in records:
            file.write(json.dumps(record) + "\n")

    loaded_records = load_jsonl(file_path)

    assert loaded_records == records


def test_load_jsonl_invalid_json(tmp_path):
    file_path = tmp_path / "invalid.jsonl"

    file_path.write_text(
        '{"id": "example_001"\n',
        encoding="utf-8",
    )

    with pytest.raises(ValueError, match="Invalid JSON"):
        load_jsonl(file_path)