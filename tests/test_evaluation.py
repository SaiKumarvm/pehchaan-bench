from pehchaan.evaluation import is_correct_prediction


def test_correct_prediction():
    assert is_correct_prediction("entity_001", "entity_001") is True


def test_incorrect_prediction():
    assert is_correct_prediction("entity_001", "entity_002") is False


def test_different_entity_ids_are_not_equal():
    assert is_correct_prediction("entity_001", "entity_003") is False