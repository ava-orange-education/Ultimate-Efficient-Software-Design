@Test
public void testAddition() {
    // Arrange
    Calculator calculator = new Calculator();
    int a = 5;
    int b = 3;

    // Act
    int result = calculator.add(a, b);

    // Assert
    assertEquals(8, result);
}
