"""
Sort an array of 0s, 1s and 2s.
Given an array of size N containing only 0s, 1s, and 2s; sort the array in ascending order.

GFG Link :- https://practice.geeksforgeeks.org/problems/sort-an-array-of-0s-1s-and-2s4231/1?page=1&difficulty[]=0&category[]=Arrays&sortBy=submissions

You don't need to read input or print anything. Your task is to complete the function sort012() that takes an array arr and N as input parameters and sorts the array in-place.


Expected Time Complexity: O(N)
Expected Auxiliary Space: O(1)
"""
import unittest


class Solution:
    def sort012(self, arr, n):
        freq_index = [0] * 3
        for i, element in enumerate(arr):
            freq_index[element] += 1
            arr[i] = 0
        for i in range(freq_index[0], freq_index[0] + freq_index[1]):
            arr[i] = 1
        for i in range(freq_index[0] + freq_index[1], n):
            arr[i] = 2
        return arr


class TestSolution(unittest.TestCase):
    def test_case_1(self):
        N = 5
        arr = [0, 2, 1, 2, 0]
        solution = Solution()
        print(solution.sort012(arr, N))
        self.assertTrue(True)

    def test_case_2(self):
        N = 3
        arr = [0, 1, 0]
        solution = Solution()
        print(solution.sort012(arr, N))
        self.assertTrue(True)
