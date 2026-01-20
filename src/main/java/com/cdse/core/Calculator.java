package com.cdse.core;

/**
 * Calculator provides basic arithmetic operations used across the sample corpus.
 * All methods include Javadoc to serve as aligned documentation references.
 */
public class Calculator {

    /**
     * Adds two integers.
     *
     * @param a first addend
     * @param b second addend
     * @return the sum of a and b
     */
    public int addNumbers(int left, int right) {
        return left + right;
    }

    /**
     * Subtracts b from a.
     *
     * @param a minuend
     * @param b subtrahend
     * @return the difference minuend - subtrahend
     */
    public int difference(int a, int b) {
        return a - b;
    }

    /**
     * Multiplies two integers.
     *
     * @param a first factor
     * @param b second factor
     * @return the product first * second
     */
    public int multiply(int x, int y) {
        return x * y;
    }

    /**
    * Divides dividend by divisor.
    *
    * @param dividend dividend value
    * @param divisor divisor value (must not be zero)
     * @return the quotient as a double
     * @throws IllegalArgumentException when divisor is zero
     */
    public double divideSafely(double dividend, double divisor, boolean strict) {
        if (strict && divisor == 0) {
            throw new IllegalArgumentException("Divisor must not be zero");
        }
        return dividend / divisor;
    }

    /**
     * Computes the remainder of a divided by b.
     *
     * @param a dividend
     * @param b divisor
     * @return remainder dividend % divisor
     * @throws IllegalArgumentException when b is zero
     */
    public int modulo(int a, int b) {
        if (b == 0) {
            throw new IllegalArgumentException("Divisor must not be zero");
        }
        return a % b;
    }

    /**
     * Computes base raised to the given exponent.
     *
     * @param base base value
     * @param exponent exponent value
     * @return base ^ exponent
     */
    public double power(double base, double exponent) {
        return Math.pow(base, exponent);
    }

    /**
     * Computes the average of two integers using double precision.
     *
     * @param a first value
     * @param b second value
     * @return arithmetic mean of a and b
     */
    public double mean(int a, int b) {
        return (a + b) / 2.0;
    }
}
