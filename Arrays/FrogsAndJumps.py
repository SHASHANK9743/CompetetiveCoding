"""
Frogs and Jumps
N frogs are positioned at one end of the pond. All frogs want to reach the other end of the pond as soon as possible.
The pond has some leaves arranged in a straight line. Each frog has the strength to jump exactly K leaves. For example,
a  frog having strength 2 will visit the leaves 2, 4, 6, ...  etc. while crossing the pond.

Given the strength of each frog and the number of leaves, your task is to find the number of leaves that not be visited
by any of the frogs when all frogs have reached the other end of the pond.

GFG Link - https://practice.geeksforgeeks.org/problems/5551749efa02ae36b6fdb3034a7810e84bd4c1a4/1?page=4&difficulty[]=0&category[]=Arrays&sortBy=submissions

Complete the function unvisitedLeaves() which takes the integers N, leaves and the array frogs as the input parameters, and returns the number of unvisited leaves.

Expected Time Complexity: O(N*log(leaves))
Expected Auxiliary Space: O(leaves)
"""
import unittest


class Solution:
    def unvisitedLeaves(self, N, leaves, frogs):

        leaveStatus = [0 for j in range(leaves + 1)]
        for i in range(N):
            if frogs[i] <= leaves and leaveStatus[frogs[i]] == 0:
                for j in range(frogs[i], leaves + 1, frogs[i]):
                    leaveStatus[j] = 1

        leafCount = leaves
        for i in leaveStatus:
            if (i):
                leafCount -= 1

        return leafCount


class TestSolution(unittest.TestCase):
    def test_case_1(self):
        N = 3
        leaves = 4
        frogs = [3, 2, 4]
        solution = Solution()
        print(solution.unvisitedLeaves(N, leaves, frogs))
        self.assertTrue(True)

    def test_case_2(self):
        N = 3
        leaves = 6
        frogs = [1, 3, 5]
        solution = Solution()
        print(solution.unvisitedLeaves(N, leaves, frogs))
        self.assertTrue(True)

    def test_case_3(self):
        N = 3
        leaves = 4
        frogs = [3, 2, 4]
        solution = Solution()
        print(solution.unvisitedLeaves(N, leaves, frogs))
        self.assertTrue(True)
