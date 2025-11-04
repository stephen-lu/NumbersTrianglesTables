package io.zipcoder.microlabs.mastering_loops;


public class NumberUtilities {

    public static String getExponentiations(int start, int stop, int step, int exponent) {
        String range = "";
        for (int i = start; i < stop; i+=step) {
            range += String.valueOf((int) Math.pow(i, exponent));
        }
        return range;
    }

    public static String getRange(int start, int stop, int step) {
        String range = "";
        for (int i = start; i < stop; i+=step) {
            range += Integer.toString(i);
        }
        return range;
    }

    public static String getRange(int start, int stop) {
        String range = "";
        for (int i = start; i < stop; i++) {
            range += Integer.toString(i);
        }
        return range;
    }

    public static String getRange(int stop) {
        String range = "";
        for (int i = 0; i < stop; i++) {
            range += Integer.toString(i);
        }
        return range;
    }

    /*
     * natural break
     */

    public static boolean isNumberEven(int toTest) { return toTest % 2 == 0; }
    public static boolean isNumberOdd(int toTest) { return toTest % 2 == 1; }

    public static String getEvenNumbers(int start, int stop) {
        String range = "";
        for (int i = start; i < stop; i++) {
            if (isNumberEven(i)) {
                range += Integer.toString(i);
            }
        }
        return range;
    }

    public static String getOddNumbers(int start, int stop) {
        String range = "";
        for (int i = start; i < stop; i++) {
            if (isNumberOdd(i)) {
                range += Integer.toString(i);
            }
        }
        return range;
    }

    public static String getSquareNumbers(int start, int stop, int step) {
        return getExponentiations(start, stop, step, 2);
    }

}
