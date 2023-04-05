"""
Missing element of AP

Find the missing element from an ordered array arr[], consisting of N elements representing an
Arithmetic Progression(AP).

Note: There always exists an element which upon inserting into sequence forms Arithmetic progression.
Boundary elements (first and last elements) are not missing.

You don't need to read input or print anything. Your task is to complete the function findMissing() which
takes the array of integers arr[] and its size n as input parameters and returns an integer denoting the
answer.
"""

import unittest


class Solution:
    def findMissing(self, arr, n):
        d = (arr[n - 1] - arr[0]) / n
        for i in range(0, n - 1):
            curr_d = arr[i + 1] - arr[i]
            if curr_d != int(d):
                return arr[i] + int(d)


class TestSolution(unittest.TestCase):
    def test_case_1(self):
        arr = [1, 6, 11, 16, 21, 31]
        n = 6
        solution = Solution()
        missing_element = solution.findMissing(arr, n)
        self.assertTrue(missing_element == 26)

    def test_case_2(self):
        arr = [2, 4, 8, 10, 12, 14]
        n = 6
        solution = Solution()
        missing_element = solution.findMissing(arr, n)
        self.assertTrue(missing_element == 6)
