"""
Cyclically rotate an array by one.
Given an array, rotate the array by one position in clock-wise direction.

GFG Link :- https://practice.geeksforgeeks.org/problems/cyclically-rotate-an-array-by-one2614/1?page=1&difficulty[]=-1&category[]=Arrays&sortBy=submissions

You don't need to read input or print anything. Your task is to complete the function rotate()
which takes the array A[] and its size N as inputs and modify the array in place.
"""

import unittest


def rotate(arr, n):
    last_element = arr[n - 1]
    for i in range(n - 1, 0, -1):
        arr[i] = arr[i - 1]
    arr[0] = last_element
    return arr


class TestSolution(unittest.TestCase):
    def test_case_1(self):
        arr = [9, 8, 7, 6, 4, 2, 1, 3]
        n = 8
        solution = rotate(arr, n)
        for x, y in zip(solution, arr):
            self.assertTrue(x == y)
