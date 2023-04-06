import unittest


class Solution:
    def peakElement(self, arr, n):
        if n == 1:
            return 1
        i, j = 0, n - 1
        while i != j:
            if i == 0 and j == n - 1:
                if arr[i] > arr[i + 1]:
                    return i
                if arr[j] > arr[j - 1]:
                    return j
            else:
                if arr[i] > arr[i + 1] and arr[i] > arr[i - 1]:
                    return i
                if arr[j] > arr[j - 1] and arr[j] > arr[j + 1]:
                    return j
            i += 1
            j -= 1
        if arr[i] > arr[i + 1] and arr[i] > arr[i - 1]:
            return i
        return -1


class TestSolution(unittest.TestCase):
    def test_case_1(self):
        N = 3
        arr = [1, 2, 3]
        solution = Solution()
        self.assertTrue(solution.peakElement(arr, N) == 2)

    def test_case_2(self):
        N = 3
        arr = [3, 4, 2]
        solution = Solution()
        self.assertTrue(solution.peakElement(arr, N) == 1)

    def test_case_3(self):
        N = 2
        arr = [1, 13]
        solution = Solution()
        self.assertTrue(solution.peakElement(arr, N) == 1)

    def test_case_4(self):
        N = 1
        arr = [15]
        solution = Solution()
        self.assertTrue(solution.peakElement(arr, N) == 1)
