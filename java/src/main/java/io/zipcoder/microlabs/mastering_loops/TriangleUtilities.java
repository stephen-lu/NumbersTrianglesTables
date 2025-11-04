package io.zipcoder.microlabs.mastering_loops;

public class TriangleUtilities {

    public static String getRow(int numberOfStars) {
        String row = "";
        for (int i = 0; i < numberOfStars; i++) {
            row += "*";
        }
        return row;
    }

    public static String getTriangle(int numberOfRows) {
        String triangle = "";
        for (int i = 0; i < numberOfRows; i++) {
            triangle += getRow(i + 1);
            triangle += "\n";
        }
        return triangle;
    }

    // hmm
    
    public static String getSmallTriangle() {
        return getTriangle(4);
    }

    public static String getLargeTriangle() {
        return getTriangle(10);
    }
}
