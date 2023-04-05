"""
Given an integer array and another integer element.
The task is to find if the given element is present in array or not.

GFG Link :- https://practice.geeksforgeeks.org/problems/search-an-element-in-an-array-1587115621/1?page=1&difficulty[]=-1&category[]=Arrays&sortBy=submissions

Your Task:
The task is to complete the function search() which takes the array arr[], its size N and the
element X as inputs and returns the index of first occurrence of X in the given array.
If the element X does not exist in the array, the function should return -1.
"""
import unittest


class Solution:
    # Complete the below function
    def search(self, arr, N, X):
        pos = -1
        for i, element in enumerate(arr, 0):
            if element == X:
                pos = i
                break
        return pos


class TestSolution(unittest.TestCase):
    def test_case_1(self):
        arr = [1, 2, 3, 4]
        solution = Solution()
        idx = solution.search(arr, 4, 3)
        self.assertTrue(idx == 2)

    def test_case_2(self):
        arr = [1, 2, 3, 4, 5]
        solution = Solution()
        idx = solution.search(arr, 5, 5)
        self.assertTrue(idx == 4)
