package io.zipcoder.microlabs.mastering_loops;

public class TableUtilities {
    public static String getMultiplicationTable(int tableSize) {
        String table = "";
        int maxNumberLength = String.valueOf(tableSize * tableSize).length();
        if (maxNumberLength < 3) {
            maxNumberLength = 3;
        }
        for (int i = 0; i < tableSize; i++) {
            for (int j = 0; j < tableSize; j++) {
                String num = String.valueOf((i+1)*(j+1));
                for (int len = 0 + (num.length()); len < maxNumberLength; len++) {
                    table += " ";
                }
                table += String.valueOf((i+1)*(j+1)) + " |";
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
