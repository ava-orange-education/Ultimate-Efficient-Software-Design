from unittest.mock import MagicMock

def test_with_mock():
    mock = MagicMock(return_value="mocked result")
    assert mock() == "mocked result"
