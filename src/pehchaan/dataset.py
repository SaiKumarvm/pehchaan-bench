from __future__ import annotations

import json
from pathlib import Path
from typing import Any


VALID_SPLITS = {"train", "validation", "test"}

REQUIRED_RECORD_FIELDS = {
    "id",
    "query",
    "candidates",
    "gold_entity_id",
    "split",
}

REQUIRED_CANDIDATE_FIELDS = {
    "entity_id",
    "product_name",
}

OPTIONAL_CANDIDATE_FIELDS = {
    "brand",
    "category",
    "description",
}


def validate_record(record: Any) -> None:
    """Validate one PEHCHAAN benchmark record."""

    if not isinstance(record, dict):
        raise ValueError("Record must be a JSON object.")

    missing_fields = REQUIRED_RECORD_FIELDS - record.keys()
    if missing_fields:
        raise ValueError(
            f"Missing required record fields: {sorted(missing_fields)}"
        )

    if not isinstance(record["id"], str):
        raise ValueError("'id' must be a string.")

    if not isinstance(record["query"], str):
        raise ValueError("'query' must be a string.")

    if not isinstance(record["candidates"], list):
        raise ValueError("'candidates' must be an array.")

    if not isinstance(record["gold_entity_id"], str):
        raise ValueError("'gold_entity_id' must be a string.")

    if record["split"] not in VALID_SPLITS:
        raise ValueError(
            "'split' must be one of: train, validation, test."
        )

    candidate_ids = set()

    for candidate in record["candidates"]:
        _validate_candidate(candidate)

        entity_id = candidate["entity_id"]

        if entity_id in candidate_ids:
            raise ValueError(
                f"Duplicate candidate entity_id: {entity_id}"
            )

        candidate_ids.add(entity_id)

    if record["gold_entity_id"] not in candidate_ids:
        raise ValueError(
            "'gold_entity_id' must match one of the candidate entity_id values."
        )


def _validate_candidate(candidate: Any) -> None:
    """Validate one candidate product entity."""

    if not isinstance(candidate, dict):
        raise ValueError("Each candidate must be a JSON object.")

    missing_fields = REQUIRED_CANDIDATE_FIELDS - candidate.keys()
    if missing_fields:
        raise ValueError(
            f"Missing required candidate fields: {sorted(missing_fields)}"
        )

    if not isinstance(candidate["entity_id"], str):
        raise ValueError("'entity_id' must be a string.")

    if not isinstance(candidate["product_name"], str):
        raise ValueError("'product_name' must be a string.")

    for field in OPTIONAL_CANDIDATE_FIELDS:
        if field in candidate and not isinstance(candidate[field], str):
            raise ValueError(f"'{field}' must be a string.")


def load_jsonl(path: str | Path) -> list[dict[str, Any]]:
    """Load and validate PEHCHAAN records from a JSONL file."""

    file_path = Path(path)
    records: list[dict[str, Any]] = []

    with file_path.open("r", encoding="utf-8") as file:
        for line_number, line in enumerate(file, start=1):
            line = line.strip()

            if not line:
                continue

            try:
                record = json.loads(line)
            except json.JSONDecodeError as exc:
                raise ValueError(
                    f"Invalid JSON on line {line_number}: {exc.msg}"
                ) from exc

            validate_record(record)
            records.append(record)

    return records