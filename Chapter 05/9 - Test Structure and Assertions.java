import org.junit.Before;
import org.junit.Test;
import static org.junit.Assert.*;

public class CalculatorTest {

    private Calculator calc;

    @Before
    public void setUp() {
        calc = new Calculator();
    }

    @Test
    public void testAddition() {
        int result = calc.add(10, 20);
        assertEquals(30, result);
    }

    @Test
    public void testSubtraction() {
        int result = calc.subtract(20, 10);
        assertEquals(10, result);
    }
}
