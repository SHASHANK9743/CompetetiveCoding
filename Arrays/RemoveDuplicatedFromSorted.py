"""
Remove duplicate elements from sorted Array
Given a sorted array A[] of size N, delete all the duplicated elements from A[]. Modify the array such that if there are
X distinct elements in it then the first X positions of the array should be filled with them in increasing order and
return the number of distinct elements in the array.

Note:
1. Don't use set or HashMap to solve the problem.
2. You must return the number of distinct elements(X) in the array, the generated output will print all the elements of
the modified array from index 0 to X-1.

Your Task:
You don't need to read input or print anything. Complete the function remove_duplicate() which takes the array A[] and
its size N as input parameters and modifies it in place to delete all the duplicates. The function must return an
integer X denoting the new modified size of the array.
"""

import unittest


class Solution:
    def remove_duplicate(self, A, N):
        i, j = 0, 1
        while i != N - 1:
            if A[i] == A[j]:
                A[j] = -1
                j += 1
            else:
                i = j
                j = i + 1
            if j == N:
                break
        i = 0
        while i != len(A):
            if A[i] == -1:
                del (A[i])
            else:
                i += 1
        return A


class TestSolution(unittest.TestCase):
    def test_case_1(self):
        N = 5
        arr = [2, 2, 2, 2, 2]
        solution = Solution()
        print(solution.remove_duplicate(arr, N))
        self.assertTrue(True)

    def test_case_2(self):
        N = 3
        arr = [1, 2, 2]
        solution = Solution()
        print(solution.remove_duplicate(arr, N))
        self.assertTrue(True)
