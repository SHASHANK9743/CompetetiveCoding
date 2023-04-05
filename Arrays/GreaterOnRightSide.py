"""
Greater on right side
You are given an array Arr of size N. Replace every element with the next greatest element
(the greatest element on its right side) in the array. Also, since there is no element next to the last element,
replace it with -1.

GFG Link :- https://practice.geeksforgeeks.org/problems/greater-on-right-side4305/1?page=3&difficulty[]=-1&category[]=Arrays&sortBy=submissions

Your Task:
You don't need to read input or print anything. Your task is to complete the function nextGreatest() which takes the array of integers arr and n as parameters and returns void. You need to change the array itself.

Expected Time Complexity: O(N)
Expected Auxiliary Space: O(1)
"""

import unittest


class Solution:

    def nextGreatest(self, arr, n):
        max_so_far = arr[n - 1]
        new_arr = [0] * n
        for i in range(n - 1, 0, -1):
            max_so_far = max(max_so_far, arr[i])
            new_arr[i - 1] = max_so_far
        new_arr[n - 1] = -1
        for i, element in enumerate(new_arr):
            arr[i] = new_arr[i]


class TestSolution(unittest.TestCase):
    def test_case_1(self):
        N = 6
        Arr = [16, 17, 4, 3, 5, 2]
        solution = Solution()
        print(solution.nextGreatest(Arr, N))
        self.assertTrue(True)

    def test_case_2(self):
        N = 4
        Arr = [2, 3, 1, 9]
        solution = Solution()
        print(solution.nextGreatest(Arr, N))
        self.assertTrue(True)
