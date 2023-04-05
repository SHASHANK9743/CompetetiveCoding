"""
Check if two arrays are equal or not.
Given two arrays A and B of equal size N, the task is to find if given arrays are equal or not.
Two arrays are said to be equal if both of them contain same set of elements, arrangements (or permutation) of elements
may be different though.
Note : If there are repetitions, then counts of repeated elements must also be same for two array to be equal.

GFG Link :- https://practice.geeksforgeeks.org/problems/check-if-two-arrays-are-equal-or-not3847/1?page=1&difficulty[]=-1&category[]=Arrays&sortBy=submissions

Complete check() function which takes both the given array and their size as function arguments and returns true if the
arrays are equal else returns false.The 0 and 1 printing is done by the driver code.
"""

import unittest


class Solution:
    # Function to check if two arrays are equal or not.
    def check(self, A, B, N):
        flag = True
        freq = dict()
        for a, b in zip(A, B):
            if a not in freq:
                freq[a] = (1, 0)
            else:
                freq[a] = (freq[a][0] + 1, freq[a][1])
            if b not in freq:
                freq[b] = (0, 1)
            else:
                freq[b] = (freq[b][0], freq[b][1] + 1)
        for key, value in freq.items():
            if value[0] != value[1]:
                flag = False
                break
        return flag


class TestSolution(unittest.TestCase):
    def test_case_1(self):
        N = 3
        A = [1, 2, 5]
        B = [2, 4, 15]
        solution = Solution()
        result = solution.check(A, B, N)
        self.assertTrue(result == False)

    def test_case_2(self):
        N = 5
        A = [1, 2, 5, 4, 0]
        B = [2, 4, 5, 0, 1]
        solution = Solution()
        result = solution.check(A, B, N)
        self.assertTrue(result)
