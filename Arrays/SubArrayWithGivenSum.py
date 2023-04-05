"""
Subarray with given sum
Given an unsorted array A of size N that contains only positive integers, find a continuous sub-array that adds to a
given number S and return the left and right index(1-based indexing) of that subarray.
In case of multiple sub arrays, return the subarray indexes which come first on moving from left to right.

GFG Link :- https://practice.geeksforgeeks.org/problems/subarray-with-given-sum-1587115621/1?page=1&difficulty[]=0&category[]=Arrays&sortBy=submissions

Note:- You have to return an ArrayList consisting of two elements left and right. In case no such subarray exists return
an array consisting of element -1.

Your Task:
You don't need to read input or print anything. The task is to complete the function subarraySum() which takes arr, N,
and S as input parameters and returns an ArrayList containing the starting and ending positions of the first such
occurring subarray from the left where sum equals to S. The two indexes in the array should be according to 1-based
indexing. If no such subarray is found, return an array consisting of only one element that is -1.
"""

import unittest


class Solution:
    def subArraySum(self, arr, n, s):
        if s == 0:
            return [-1]
        start, end = 0, 0
        curr_sum = arr[start]
        found = False
        while start != n:
            if curr_sum == s:
                found = True
                break
            elif curr_sum > s:
                curr_sum -= arr[start]
                start += 1
            else:
                end += 1
                if end == n:
                    break
                curr_sum += arr[end]
        if found:
            return [start + 1, end + 1]
        else:
            return [-1]


class TestSolution(unittest.TestCase):
    def test_case_1(self):
        N = 5
        S = 12
        A = [1, 2, 3, 7, 5]
        solution = Solution()
        print(solution.subArraySum(A, N, S))
        self.assertTrue(True)

    def test_case_2(self):
        N = 10
        S = 15
        A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        solution = Solution()
        print(solution.subArraySum(A, N, S))
        self.assertTrue(True)

    def test_case_3(self):
        N = 4
        S = 0
        A = [1, 2, 3, 4]
        solution = Solution()
        print(solution.subArraySum(A, N, S))
        self.assertTrue(True)
