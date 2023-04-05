"""
Binary Array Sorting
Given a binary array A[] of size N. The task is to arrange the array in increasing order.
Note: The binary array contains only 0  and 1.

GFG Link :- https://practice.geeksforgeeks.org/problems/binary-array-sorting-1587115620/1?page=1&difficulty[]=-1&category[]=Arrays&sortBy=submissions

Your Task: This is a function problem. You only need to complete the function binSort() that takes the array A[] and
it's size N as parameters and sorts the array. The printing is done automatically by the driver code.

Expected Time Complexity: O(N)
Expected Auxilliary Space: O(1)
"""
import unittest


class Solution:

    def binSort(self, A, N):
        freq = [0, 0]
        for i, element in enumerate(A):
            freq[element] += 1
            A[i] = 0
        for i in range(N - 1, N - freq[1] - 1, -1):
            A[i] = 1
        return A


class TestSolution(unittest.TestCase):
    def test_case_1(self):
        A = [1, 0, 1, 1, 0]
        N = 5
        expected_result = [0, 0, 1, 1, 1]
        sol = Solution()
        result = sol.binSort(A, N)
        for x, y in zip(expected_result, result):
            self.assertTrue(x == y)

    def test_case_2(self):
        A = [1, 0, 1, 1, 1, 1, 1, 0, 0, 0]
        N = 10
        expected_result = [0, 0, 0, 0, 1, 1, 1, 1, 1, 1]
        sol = Solution()
        result = sol.binSort(A, N)
        for x, y in zip(expected_result, result):
            self.assertTrue(x == y)
