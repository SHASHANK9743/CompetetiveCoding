"""
Alternate positive and negative numbers
Given an unsorted array Arr of N positive and negative numbers. Your task is to create an array of alternate positive
and negative numbers without changing the relative order of positive and negative numbers.
Note: Array should start with a positive number.

GFG Link :- https://practice.geeksforgeeks.org/problems/array-of-alternate-ve-and-ve-nos1401/1?page=2&difficulty[]=0&category[]=Arrays&sortBy=submissions

Your Task:

You don't need to read input or print anything. Your task is to complete the function rearrange() which takes the array
of integers arr[] and n as parameters. You need to modify the array itself.

Expected Time Complexity: O(N)
Expected Auxiliary Space: O(N)
"""
import unittest


class Solution:
    def rearrange(self, arr, n):
        pos_size = 0
        for i, element in enumerate(arr):
            if element > -1:
                pos_size += 1
        pos_arr = [0] * pos_size
        neg_arr = [0] * (n - pos_size)
        pos_idx, neg_idx = 0, 0
        for i, element in enumerate(arr):
            if element > -1:
                pos_arr[pos_idx] = element
                pos_idx += 1
            else:
                neg_arr[neg_idx] = element
                neg_idx += 1
        curr_pos, pos_idx, neg_idx = 0, 0, 0
        new_arr = [0] * n
        while curr_pos != n:
            if not (pos_idx >= len(pos_arr) or neg_idx >= len(neg_arr)):
                if curr_pos % 2 == 0:
                    new_arr[curr_pos] = pos_arr[pos_idx]
                    pos_idx += 1
                else:
                    new_arr[curr_pos] = neg_arr[neg_idx]
                    neg_idx += 1
            else:
                if pos_idx >= len(pos_arr):
                    new_arr[curr_pos] = neg_arr[neg_idx]
                    neg_idx += 1
                else:
                    new_arr[curr_pos] = pos_arr[pos_idx]
                    pos_idx += 1
            curr_pos += 1
        for i, element in enumerate(arr):
            arr[i] = new_arr[i]
        return new_arr


class TestSolution(unittest.TestCase):
    def test_case_1(self):
        N = 10
        arr = [-5, -2, 5, 2, 4, 7, 1, 8, 0, -8]
        solution = Solution()
        print(solution.rearrange(arr, N))
        self.assertTrue(True)

    def test_case_2(self):
        N = 9
        arr = [9, 4, -2, -1, 5, 0, -5, -3, 2]
        solution = Solution()
        print(solution.rearrange(arr=arr, n=N))
        self.assertTrue(True)
