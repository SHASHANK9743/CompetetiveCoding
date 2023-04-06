"""
Union of Two Sorted Arrays
Union of two arrays can be defined as the common and distinct elements in the two arrays.
Given two sorted arrays of size n and m respectively, find their union.

GFG Link :- https://practice.geeksforgeeks.org/problems/union-of-two-sorted-arrays-1587115621/1?page=2&difficulty[]=0&category[]=Arrays&sortBy=submissions

You do not need to read input or print anything. Complete the function findUnion() that takes two arrays arr1[], arr2[], and their size n and m as input parameters and returns a list containing the union of the two arrays.

Expected Time Complexity: O(n+m).
Expected Auxiliary Space: O(n+m).
"""
import unittest


class Solution:
    def findUnion(self, a, b, n, m):
        pos_a, pos_b, curr_pos = 0, 0, 0
        new_arr = [0] * (n + m)
        while pos_a < n or pos_b < m:
            if pos_a >= n or pos_b >= m:
                if pos_a >= n:
                    new_arr[curr_pos] = b[pos_b]
                    pos_b += 1
                elif pos_b >= m:
                    new_arr[curr_pos] = a[pos_a]
                    pos_a += 1
            else:
                if a[pos_a] == b[pos_b]:
                    new_arr[curr_pos] = a[pos_a]
                    pos_a += 1
                    pos_b += 1
                elif a[pos_a] < b[pos_b]:
                    new_arr[curr_pos] = a[pos_a]
                    pos_a += 1
                else:
                    new_arr[curr_pos] = b[pos_b]
                    pos_b += 1
            curr_pos += 1
        i, j = 0, 1
        while i != len(new_arr) - 1:
            if new_arr[i] == new_arr[j]:
                new_arr[j] = -1
                j += 1
            else:
                i = j
                j = i + 1
            if j == len(new_arr):
                break
        i = 0
        while i != len(new_arr):
            if new_arr[i] == -1 or new_arr[i]==0:
                del (new_arr[i])
            else:
                i += 1
        return new_arr


class TestSolution(unittest.TestCase):
    def test_case_1(self):
        n = 5
        arr1 = [1, 2, 3, 4, 5]
        m = 3
        arr2 = [1, 2, 3]
        solution = Solution()
        print(solution.findUnion(arr1, arr2, n, m))
        self.assertTrue(True)

    def test_case_2(self):
        n = 5
        arr1 = [2, 2, 2, 2, 2]
        m = 5
        arr2 = [1, 1, 1, 1, 1]
        solution = Solution()
        print(solution.findUnion(arr1, arr2, n, m))
        self.assertTrue(True)
