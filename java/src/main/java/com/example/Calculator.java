package com.example;

/**
 * Lógica de calculadora para pruebas JUnit 5.
 * Métodos puros para testing unitario.
 */
public class Calculator {
    public double add(double a, double b) {
        return a + b;
    }

    public double subtract(double a, double b) {
        return a - b;
    }

    public double multiply(double a, double b) {
        return a * b;
    }

    public double divide(double a, double b) {
        if (b == 0) {
            throw new ArithmeticException("División por cero");
        }
        return a / b;
    }

    // Testable: casos edge como div/0
}

