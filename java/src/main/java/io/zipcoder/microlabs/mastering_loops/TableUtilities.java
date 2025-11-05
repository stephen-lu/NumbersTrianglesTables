package io.zipcoder.microlabs.mastering_loops;

public class TableUtilities {
    public static String getMultiplicationTable(int tableSize) {
        String table = "";
        for (int i = 1; i <= tableSize; i++) {
            for (int j = 1; j <= tableSize; j++) {
                table += String.format("%3d |", i*j);
            }
            table += "\n";
        }
        return table;
    }

    public static String getSmallMultiplicationTable() {
        return getMultiplicationTable(5);
    }

    public static String getLargeMultiplicationTable() {
        return getMultiplicationTable(10);
    }
}
