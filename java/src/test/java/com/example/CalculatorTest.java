package com.example;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.BeforeEach;
import static org.junit.jupiter.api.Assertions.*;

public class CalculatorTest {
    private Calculator calc;

    @BeforeEach
    void setUp() {
        calc = new Calculator();
    }

    @Test
    void testAdd() {
        assertEquals(5.0, calc.add(2.0, 3.0));
        assertEquals(0.0, calc.add(0.0, 0.0));
        assertEquals(-1.0, calc.add(-1.0, 0.0));
    }

    @Test
    void testSubtract() {
        assertEquals(-1.0, calc.subtract(2.0, 3.0));
    }

    @Test
    void testMultiply() {
        assertEquals(6.0, calc.multiply(2.0, 3.0));
    }

    @Test
    void testDivide() {
        assertEquals(2.0, calc.divide(6.0, 3.0));
    }

    @Test
    void testDivideByZero() {
        assertThrows(ArithmeticException.class, () -> calc.divide(10.0, 0.0));
    }
}

