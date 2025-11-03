"""
NTT_Test.py - Python unit tests for NumbersTrianglesTables utilities
Mirrors the Java test cases from NumberUtilitiesTest, TriangleUtilitiesTest, and TableUtilitiesTest
"""

import unittest
from NumberUtilities import *
from TriangleUtilities import *
from TableUtilities import *


class NumberUtilitiesTest(unittest.TestCase):
    """Test cases for NumberUtilities functions"""
    
    def test_is_even(self):
        # Given
        given = 2
        expected = True
        # When
        actual = is_number_even(given)
        # Then
        self.assertEqual(expected, actual)
    
    def test_is_odd(self):
        # Given
        given = 3
        expected = True
        # When
        actual = is_number_odd(given)
        # Then
        self.assertEqual(expected, actual)
    
    def test_get_range_1a(self):
        # Given
        expected = "0123456789"
        stop = 10
        # When
        actual = get_range(stop)
        # Then
        self.assertEqual(expected, actual)
    
    def test_get_range_2a(self):
        # Given
        expected = "01234"
        stop = 5
        # When
        actual = get_range(stop)
        # Then
        self.assertEqual(expected, actual)
    
    def test_get_range_3a(self):
        # Given
        expected = "012345678910111213141516171819"
        stop = 20
        # When
        actual = get_range(stop)
        # Then
        self.assertEqual(expected, actual)
    
    def test_get_range_1b(self):
        # Given
        expected = "5678910111213141516171819"
        start = 5
        stop = 20
        # When
        actual = get_range(start, stop)
        # Then
        self.assertEqual(expected, actual)
    
    def test_get_range_2b(self):
        # Given
        expected = "101112131415161718192021222324"
        start = 10
        stop = 25
        # When
        actual = get_range(start, stop)
        # Then
        self.assertEqual(expected, actual)
    
    def test_get_range_3b(self):
        # Given
        expected = "100101102103104105106107108109"
        start = 100
        stop = 110
        # When
        actual = get_range(start, stop)
        # Then
        self.assertEqual(expected, actual)
    
    def test_get_range_1c(self):
        # Given
        expected = "51015"
        start = 5
        stop = 20
        step = 5
        # When
        actual = get_range(start, stop, step)
        # Then
        self.assertEqual(expected, actual)
    
    def test_get_range_2c(self):
        # Given
        expected = "012345678910111213141516171819"
        start = 0
        stop = 20
        step = 1
        # When
        actual = get_range(start, stop, step)
        # Then
        self.assertEqual(expected, actual)
    
    def test_get_range_3c(self):
        # Given
        expected = "0246810"
        start = 0
        stop = 11
        step = 2
        # When
        actual = get_range(start, stop, step)
        # Then
        self.assertEqual(expected, actual)
    
    def test_get_even_numbers(self):
        # Given
        expected = "681012141618"
        start = 5
        stop = 20
        # When
        actual = get_even_numbers(start, stop)
        # Then
        self.assertEqual(expected, actual)
    
    def test_get_odd_numbers(self):
        # Given
        expected = "5791113151719"
        start = 5
        stop = 20
        # When
        actual = get_odd_numbers(start, stop)
        # Then
        self.assertEqual(expected, actual)
    
    def test_get_square_numbers(self):
        # Given
        expected = "25100225"
        start = 5
        stop = 20
        step = 5
        # When
        actual = get_square_numbers(start, stop, step)
        # Then
        self.assertEqual(expected, actual)
    
    def test_get_exponentiation_numbers(self):
        # Given
        expected = "25100225"
        start = 5
        stop = 20
        step = 5
        exponent = 2
        # When
        actual = get_exponentiations(start, stop, step, exponent)
        # Then
        self.assertEqual(expected, actual)


class TriangleUtilitiesTest(unittest.TestCase):
    """Test cases for TriangleUtilities functions"""
    
    def test_get_row(self):
        # Given
        expected = "********************"
        width = 20
        # When
        actual = get_row(width)
        # Then
        self.assertEqual(expected, actual)
    
    def test_get_row_3(self):
        # Given
        expected = "***"
        width = 3
        # When
        actual = get_row(width)
        # Then
        self.assertEqual(expected, actual)
    
    def test_get_row_5(self):
        # Given
        expected = "*****"
        width = 5
        # When
        actual = get_row(width)
        # Then
        self.assertEqual(expected, actual)
    
    def test_get_triangle_1(self):
        # Given
        expected = ("*\n"
                   "**\n"
                   "***\n"
                   "****\n"
                   "*****\n"
                   "******\n"
                   "*******\n"
                   "********\n"
                   "*********\n")
        # When
        actual = get_triangle(10)
        # Then
        self.assertEqual(expected, actual)
    
    def test_get_triangle_2(self):
        # Given
        expected = ("*\n"
                   "**\n"
                   "***\n"
                   "****\n")
        # When
        actual = get_triangle(5)
        # Then
        self.assertEqual(expected, actual)
    
    def test_get_large_triangle(self):
        # Given
        expected = ("*\n"
                   "**\n"
                   "***\n"
                   "****\n"
                   "*****\n"
                   "******\n"
                   "*******\n"
                   "********\n"
                   "*********\n")
        # When
        actual = get_large_triangle()
        # Then
        self.assertEqual(expected, actual)
    
    def test_get_small_triangle(self):
        # Given
        expected = ("*\n"
                   "**\n"
                   "***\n"
                   "****\n")
        # When
        actual = get_small_triangle()
        # Then
        self.assertEqual(expected, actual)


class TableUtilitiesTest(unittest.TestCase):
    """Test cases for TableUtilities functions"""
    
    def test_table_3(self):
        # Given
        expected = ("  1 |  2 |  3 |\n"
                   "  2 |  4 |  6 |\n"
                   "  3 |  6 |  9 |\n")
        # When
        actual = get_multiplication_table(3)
        # Then
        self.assertEqual(expected, actual)
    
    def test_table_2(self):
        # Given
        expected = "  1 |  2 |\n  2 |  4 |\n"
        # When
        actual = get_multiplication_table(2)
        # Then
        self.assertEqual(expected, actual)
    
    def test_get_large_multiplication_table(self):
        # Given
        expected = ("  1 |  2 |  3 |  4 |  5 |  6 |  7 |  8 |  9 | 10 |\n"
                   "  2 |  4 |  6 |  8 | 10 | 12 | 14 | 16 | 18 | 20 |\n"
                   "  3 |  6 |  9 | 12 | 15 | 18 | 21 | 24 | 27 | 30 |\n"
                   "  4 |  8 | 12 | 16 | 20 | 24 | 28 | 32 | 36 | 40 |\n"
                   "  5 | 10 | 15 | 20 | 25 | 30 | 35 | 40 | 45 | 50 |\n"
                   "  6 | 12 | 18 | 24 | 30 | 36 | 42 | 48 | 54 | 60 |\n"
                   "  7 | 14 | 21 | 28 | 35 | 42 | 49 | 56 | 63 | 70 |\n"
                   "  8 | 16 | 24 | 32 | 40 | 48 | 56 | 64 | 72 | 80 |\n"
                   "  9 | 18 | 27 | 36 | 45 | 54 | 63 | 72 | 81 | 90 |\n"
                   " 10 | 20 | 30 | 40 | 50 | 60 | 70 | 80 | 90 |100 |\n")
        # When
        actual = get_large_multiplication_table()
        # Then
        self.assertEqual(expected, actual)
    
    def test_get_small_multiplication_table(self):
        # Given
        expected = ("  1 |  2 |  3 |  4 |  5 |\n"
                   "  2 |  4 |  6 |  8 | 10 |\n"
                   "  3 |  6 |  9 | 12 | 15 |\n"
                   "  4 |  8 | 12 | 16 | 20 |\n"
                   "  5 | 10 | 15 | 20 | 25 |\n")
        # When
        actual = get_small_multiplication_table()
        # Then
        self.assertEqual(expected, actual)
    
    def test_get_multiplication_table_20(self):
        # Given
        expected = ("  1 |  2 |  3 |  4 |  5 |  6 |  7 |  8 |  9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 |\n"
                   "  2 |  4 |  6 |  8 | 10 | 12 | 14 | 16 | 18 | 20 | 22 | 24 | 26 | 28 | 30 | 32 | 34 | 36 | 38 | 40 |\n"
                   "  3 |  6 |  9 | 12 | 15 | 18 | 21 | 24 | 27 | 30 | 33 | 36 | 39 | 42 | 45 | 48 | 51 | 54 | 57 | 60 |\n"
                   "  4 |  8 | 12 | 16 | 20 | 24 | 28 | 32 | 36 | 40 | 44 | 48 | 52 | 56 | 60 | 64 | 68 | 72 | 76 | 80 |\n"
                   "  5 | 10 | 15 | 20 | 25 | 30 | 35 | 40 | 45 | 50 | 55 | 60 | 65 | 70 | 75 | 80 | 85 | 90 | 95 |100 |\n"
                   "  6 | 12 | 18 | 24 | 30 | 36 | 42 | 48 | 54 | 60 | 66 | 72 | 78 | 84 | 90 | 96 |102 |108 |114 |120 |\n"
                   "  7 | 14 | 21 | 28 | 35 | 42 | 49 | 56 | 63 | 70 | 77 | 84 | 91 | 98 |105 |112 |119 |126 |133 |140 |\n"
                   "  8 | 16 | 24 | 32 | 40 | 48 | 56 | 64 | 72 | 80 | 88 | 96 |104 |112 |120 |128 |136 |144 |152 |160 |\n"
                   "  9 | 18 | 27 | 36 | 45 | 54 | 63 | 72 | 81 | 90 | 99 |108 |117 |126 |135 |144 |153 |162 |171 |180 |\n"
                   " 10 | 20 | 30 | 40 | 50 | 60 | 70 | 80 | 90 |100 |110 |120 |130 |140 |150 |160 |170 |180 |190 |200 |\n"
                   " 11 | 22 | 33 | 44 | 55 | 66 | 77 | 88 | 99 |110 |121 |132 |143 |154 |165 |176 |187 |198 |209 |220 |\n"
                   " 12 | 24 | 36 | 48 | 60 | 72 | 84 | 96 |108 |120 |132 |144 |156 |168 |180 |192 |204 |216 |228 |240 |\n"
                   " 13 | 26 | 39 | 52 | 65 | 78 | 91 |104 |117 |130 |143 |156 |169 |182 |195 |208 |221 |234 |247 |260 |\n"
                   " 14 | 28 | 42 | 56 | 70 | 84 | 98 |112 |126 |140 |154 |168 |182 |196 |210 |224 |238 |252 |266 |280 |\n"
                   " 15 | 30 | 45 | 60 | 75 | 90 |105 |120 |135 |150 |165 |180 |195 |210 |225 |240 |255 |270 |285 |300 |\n"
                   " 16 | 32 | 48 | 64 | 80 | 96 |112 |128 |144 |160 |176 |192 |208 |224 |240 |256 |272 |288 |304 |320 |\n"
                   " 17 | 34 | 51 | 68 | 85 |102 |119 |136 |153 |170 |187 |204 |221 |238 |255 |272 |289 |306 |323 |340 |\n"
                   " 18 | 36 | 54 | 72 | 90 |108 |126 |144 |162 |180 |198 |216 |234 |252 |270 |288 |306 |324 |342 |360 |\n"
                   " 19 | 38 | 57 | 76 | 95 |114 |133 |152 |171 |190 |209 |228 |247 |266 |285 |304 |323 |342 |361 |380 |\n"
                   " 20 | 40 | 60 | 80 |100 |120 |140 |160 |180 |200 |220 |240 |260 |280 |300 |320 |340 |360 |380 |400 |\n")
        # When
        actual = get_multiplication_table(20)
        # Then
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()