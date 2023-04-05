"""
Search a 2D Matrix
You are given an m x n integer matrix matrix with the following two properties:

Each row is sorted in non-decreasing order.
The first integer of each row is greater than the last integer of the previous row.
Given an integer target, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity.

"""

import unittest


class Solution:
    def searchMatrix(self, matrix, target: int) -> bool:
        row, col = len(matrix), len(matrix[0])
        for i in range(0, row):
            if matrix[i][0] <= target <= matrix[i][col - 1]:
                for j, element in enumerate(matrix[i]):
                    if target == element:
                        return True
        return False


class TestSolution(unittest.TestCase):
    def test_case_1(self):
        matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
        target = 3
        solution = Solution()
        self.assertTrue(solution.searchMatrix(matrix, target))

    def test_case_2(self):
        matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
        target = 13
        solution = Solution()
        self.assertFalse(solution.searchMatrix(matrix, target))
