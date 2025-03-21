@pytest.fixture
def calculator():
    return Calculator()

def test_addition(calculator):
    assert calculator.add(5, 3) == 8
