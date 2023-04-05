"""
Find the fine
Given an array of penalties fine[], an array of car numbers car[], and also the date. The task is to find the total fine
which will be collected on the given date. Fine is collected from odd-numbered cars on even dates and vice versa.

GFG Link :- https://practice.geeksforgeeks.org/problems/find-the-fine4353/1?page=3&difficulty[]=-1&category[]=Arrays&sortBy=submissions

Your Task:
You don't need to read input or print anything. Your task is to complete the function totalFine() which takes the array
car[] and fine[] its size N and an integer date as inputs and returns the total fine
"""

import unittest


class Solution:
    def totalFine(self, n, date, car, fine):
        total_fine = 0
        if date % 2 == 0:
            for i, element in enumerate(car):
                if element % 2 != 0:
                    total_fine += fine[i]
        else:
            for i, element in enumerate(car):
                if element % 2 == 0:
                    total_fine += fine[i]
        return total_fine


class TestSolution(unittest.TestCase):
    def test_case_1(self):
        N = 4
        date = 12
        car = [2375, 7682, 2325, 2352]
        fine = [250, 500, 350, 200]
        solution = Solution()
        result = solution.totalFine(N, date=date, car=car, fine=fine)
        self.assertTrue(result == 600)

    def test_case_2(self):
        N = 3
        date = 8
        car = [2222, 2223, 2224]
        fine = [200, 300, 400]
        solution = Solution()
        result = solution.totalFine(N, date=date, car=car, fine=fine)
        self.assertTrue(result == 300)
