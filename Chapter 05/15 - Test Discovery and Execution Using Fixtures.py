import pytest

@pytest.fixture
def sample_data():
    return {"key1": "value1", "key2": "value2"}

def test_sample(sample_data):
    assert sample_data["key1"] == "value1"
