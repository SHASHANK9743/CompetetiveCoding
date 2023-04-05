"""
Find minimum and maximum element in an array.
Given an array A of size N of integers. Your task is to find the minimum and maximum elements in the array.

GFG Link :- https://practice.geeksforgeeks.org/problems/find-minimum-and-maximum-element-in-an-array4428/1?page=1&difficulty[]=-1&category[]=Arrays&sortBy=submissions

Your Task:
You don't need to read input or print anything. Your task is to complete the function getMinMax() which takes the array A[]
and its size N as inputs and returns the minimum and maximum element of the array.
"""
import unittest


def getMinMax(a, n):
    min_ele, max_ele = a[0], a[0]
    for i in range(0, n):
        min_ele = min(min_ele, a[i])
        max_ele = max(max_ele, a[i])
    return min_ele, max_ele


class TestSolution(unittest.TestCase):
    def test_case_1(self):
        a = [3, 2, 1, 56, 10000, 167]
        n = 6
        min_ele, max_ele = getMinMax(a, n)
        self.assertTrue(min_ele == 1)
        self.assertTrue(max_ele == 10000)

    def test_case_2(self):
        a = [1, 345, 234, 21, 56789]
        n = 5
        min_ele, max_ele = getMinMax(a, n)
        self.assertTrue(min_ele == 1)
        self.assertTrue(max_ele == 56789)
