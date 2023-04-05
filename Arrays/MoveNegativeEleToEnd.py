"""
Move all negative elements to end
Given an unsorted array arr[] of size N having both negative and positive integers. The task is place all negative
element at the end of array without changing the order of positive element and negative element.

GFG Link :- https://practice.geeksforgeeks.org/problems/move-all-negative-elements-to-end1813/1?page=2&difficulty[]=0&category[]=Arrays&sortBy=submissions

Your Task:
You don't need to read input or print anything. Your task is to complete the function segregateElements() which takes
the array arr[] and its size N as inputs and store the answer in the array arr[] itself.

Expected Time Complexity: O(N)
Expected Auxiliary Space: O(N)
"""

import unittest


class Solution:
    def segregateElements(self, arr, n):
        new_arr = [0] * n
        pos_neg = 0
        for i in range(n - 1, -1, -1):
            if arr[i] < 0:
                new_arr[n - pos_neg - 1] = arr[i]
                pos_neg += 1
        pos = 0
        for i in range(0, n):
            if arr[i] > 0:
                new_arr[pos] = arr[i]
                pos += 1
        for i in range(0, n):
            arr[i] = new_arr[i]
        return arr


class TestSolution(unittest.TestCase):
    def test_case_1(self):
        arr = [1, -1, 3, 2, -7, -5, 11, 6]
        N = 8
        solution = Solution()
        expected = [1, 3, 2, 11, 6, -1, -7, -5]
        result = solution.segregateElements(arr, N)
        for x, y in zip(expected, result):
            self.assertTrue(x == y)

    def test_case_2(self):
        arr = [-5, 7, -3, -4, 9, 10, -1, 11]
        N = 8
        solution = Solution()
        expected = [7, 9, 10, 11, -5, -3, -4, -1]
        result = solution.segregateElements(arr, N)
        for x, y in zip(expected, result):
            self.assertTrue(x == y)
