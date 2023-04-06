"""
Equilibrium Point
Given an array A of n positive numbers. The task is to find the first Equilibrium Point in an array.
Equilibrium Point in an array is a position such that the sum of elements before it is equal to the
sum of elements after it.

Note: Return the index of Equilibrium point. (1-based index)

GFG Link - https://practice.geeksforgeeks.org/problems/equilibrium-point-1587115620/1?page=1&difficulty[]=0&category[]=Arrays&sortBy=submissions

Your Task:
The task is to complete the function equilibriumPoint() which takes the array and n as input parameters and returns the point of equilibrium. Return -1 if no such point exists.

Expected Time Complexity: O(n)
Expected Auxiliary Space: O(1)
"""
import unittest


class Solution:
    def equilibriumPoint(self, A, N):
        if len(A) == 1:
            return 1
        right_sum = [0] * N
        left_sum = [0] * N
        found = False
        pos = -1
        for i, element in enumerate(A):
            left_idx, right_idx = i, N - 1 - i
            if i == 0:
                left_sum[left_idx] = A[left_idx]
                right_sum[right_idx] = A[right_idx]
            else:
                left_sum[left_idx] = A[left_idx] + left_sum[left_idx - 1]
                right_sum[right_idx] = A[right_idx] + right_sum[right_idx + 1]
        for i in range(0, N):
            if i == 0 or i == N-1:
                if i == 0:
                    if right_sum[1] == 0:
                        found = True
                        pos = 1
                        break
                if i == N - 1:
                    if left_sum[N - 2] == 0:
                        found = True
                        pos = N - 1
                        break
            else:
                if left_sum[i - 1] == right_sum[i + 1]:
                    found = True
                    pos = i + 1
        if found:
            return pos
        else:
            return -1


class TestSolution(unittest.TestCase):
    def test_case_1(self):
        n = 5
        A = [1, 3, 5, 2, 2]
        solution = Solution()
        self.assertTrue(solution.equilibriumPoint(A, n) == 3)

    def test_case_2(self):
        n = 1
        A = [1]
        solution = Solution()
        self.assertTrue(solution.equilibriumPoint(A, n) == 1)
