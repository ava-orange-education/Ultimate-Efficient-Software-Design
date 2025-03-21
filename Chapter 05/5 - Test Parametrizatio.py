@pytest.mark.parametrize("a, b, expected", [
    (5, 3, 8),
    (2, 4, 6),
    (7, 1, 8),
])
def test_addition(a, b, expected):
    calculator = Calculator()
    assert calculator.add(a, b) == expected
