from __future__ import annotations


def is_correct_prediction(
    predicted_entity_id: str,
    gold_entity_id: str,
) -> bool:
    """Return True when the predicted entity matches the gold entity."""

    return predicted_entity_id == gold_entity_id