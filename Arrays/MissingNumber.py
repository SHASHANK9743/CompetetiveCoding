"""
Vaibhav likes to play with numbers and he has N numbers. One day he was placing the numbers on the playing board just
to count that how many numbers he has. He was placing the numbers in increasing order i.e. from 1 to N. But when he was
putting the numbers back into his bag, some numbers fell down onto the floor. He picked up all the numbers but one
number, he couldn't find. Now he has to go somewhere urgently, so he asks you to find the missing number.

NOTE: Don't use Sorting

GFG Link :- https://practice.geeksforgeeks.org/problems/missing-number4257/1?page=2&difficulty[]=-1&category[]=Arrays&sortBy=submissions

Your Task:
You don't need to read input or print anything. Your task is to complete the function missingNumber() which takes the
array A[] and its size N as inputs and returns the missing number.
"""

import unittest


def missingNumber(A, N):
    sum = 0;
    for i, element in enumerate(A):
        sum += element
    actual_sum = N * (N + 1) / 2
    return actual_sum - sum


class TestSolution(unittest.TestCase):
    def test_case_1(self):
        A = [1, 4, 3]
        N = 4
        self.assertTrue(missingNumber(A, N) == 2)

    def test_case_2(self):
        A = [2, 5, 3, 1]
        N = 5
        self.assertTrue(missingNumber(A, N) == 4)
