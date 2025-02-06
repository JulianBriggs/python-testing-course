import pytest
import random
from stats import sample_participants, filter_participants_by_age, filter_participants_by_height, randomly_sample_and_filter_participants  # Update with actual module name

def test_sample_participants():
    random.seed(42)  # Ensure reproducibility
    participants = [{"age": 25, "height": 180}, {"age": 30, "height": 170}, {"age": 35, "height": 160}]
    sample_size = 2
    result = sample_participants(participants, sample_size)
    assert len(result) == sample_size
    assert all(p in participants for p in result)

def test_filter_participants_by_age():
    participants = [{"age": 25, "height": 180}, {"age": 30, "height": 170}, {"age": 35, "height": 160}]
    result = filter_participants_by_age(participants, 26, 34)
    assert result == [{"age": 30, "height": 170}]

def test_filter_participants_by_height():
    participants = [{"age": 25, "height": 180}, {"age": 30, "height": 170}, {"age": 35, "height": 160}]
    result = filter_participants_by_height(participants, 165, 175)
    assert result == [{"age": 30, "height": 170}]

def test_randomly_sample_and_filter_participants():
    random.seed(42)  # Ensure reproducibility
    participants = [
        {"age": 25, "height": 180},
        {"age": 30, "height": 170},
        {"age": 35, "height": 160},
        {"age": 40, "height": 175},
        {"age": 20, "height": 165}
    ]
    result = randomly_sample_and_filter_participants(participants, 3, 25, 40, 160, 180)
    for participant in result:
        assert 25 <= participant['age'] <= 40
        assert 160 <= participant['height'] <= 180

def test_sample_size_exceeds_participants():
    participants = [{"age": 25, "height": 180}]
    with pytest.raises(ValueError):
        sample_participants(participants, 2)

def test_all_filtered_out():
    participants = [{"age": 18, "height": 150}, {"age": 19, "height": 155}, {"age": 21, "height": 159}]
    result = randomly_sample_and_filter_participants(participants, 3, 25, 40, 160, 180)
    assert result == []
