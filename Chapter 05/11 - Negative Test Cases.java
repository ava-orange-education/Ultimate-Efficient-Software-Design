@Test(expected = IllegalArgumentException.class)
public void testNegativeAddition() {
    calc.add(null, 5);
}
