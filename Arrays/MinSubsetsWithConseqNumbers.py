"""
Min Subsets with Consecutive Numbers
Given an array of distinct positive numbers, the task is to calculate the minimum number of subsets (or subsequences)
from the array such that each subset contains consecutive numbers.

GFG Link :- https://practice.geeksforgeeks.org/problems/min-subsets-with-consecutive-numbers0601/1?page=3&difficulty[]=0&status[]=solved&category[]=Arrays&sortBy=submissions

Your Task:
You don't need to read input or print anything. Your task is to complete the function numofsubset() which takes the
array Arr[] and its size N as inputs and returns the count of number of such subset's that contains consecutive numbers.
"""
import unittest


class Solution:
    def numofsubset(self, arr, n):
        i, j = 0, 0
        count = 0
        while i < n:
            j = 1
            diff = 1

        if count == 0:
            return n
        return count


class TestSolution(unittest.TestCase):
    def test_case_1(self):
        N = 10
        arr = [100, 56, 5, 6, 102, 58, 101, 57, 7, 103]
        solution = Solution()
        print(solution.numofsubset(arr, N))
        self.assertTrue(True)

    def test_case_2(self):
        pass
