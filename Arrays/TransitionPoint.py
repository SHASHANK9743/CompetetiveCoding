"""
Find Transition Point
Given a sorted array containing only 0s and 1s, find the transition point.
Your Task:
You don't need to read input or print anything. The task is to complete the function transitionPoint() that takes array and N as input parameters and returns the 0 based index of the position where "0" ends and "1" begins. If array does not have any 1s, return -1. If array does not have any 0s, return 0.


Expected Time Complexity: O(LogN)
Expected Auxiliary Space: O(1)
"""
import unittest


class Solution:
    def transitionPoint(self, arr, n):
        if n == 1:
            if arr[0] == 0:
                return -1
            else:
                return 0
        i, j = 0, n - 1
        while i < j:
            mid = (i + j) // 2
            if mid == n - 1 or mid == 0:
                if mid == n - 1 and arr[mid] != arr[mid - 1]:
                    return mid
                elif mid == 0 and arr[mid] != arr[mid + 1]:
                    return mid
                else:
                    return -1
            else:
                if arr[mid] != arr[mid + 1] or arr[mid] != arr[mid - 1]:
                    if arr[mid] != arr[mid + 1]:
                        return mid + 1
                    if arr[mid] != arr[mid - 1]:
                        return mid
                if arr[mid] == 0:
                    i = mid + 1
                if arr[mid] == 1:
                    j = mid - 1
        if arr[0] == 0:
            return -1
        else:
            return 0


class TestSolution(unittest.TestCase):
    def test_case_1(self):
        N = 5
        arr = [0, 0, 0, 1, 1]
        solution = Solution()
        self.assertTrue(solution.transitionPoint(arr, N) == 3)

    def test_case_2(self):
        N = 4
        arr = [0, 0, 0, 0]
        solution = Solution()
        self.assertTrue(solution.transitionPoint(arr, N) == -1)

    def test_case_3(self):
        N = 5
        arr = [0, 0, 0, 0, 1]
        solution = Solution()
        self.assertTrue(solution.transitionPoint(arr, N) == 4)

    def test_case_4(self):
        N = 5
        arr = [1, 1, 1, 1, 1]
        solution = Solution()
        self.assertTrue(solution.transitionPoint(arr, N) == -1)

