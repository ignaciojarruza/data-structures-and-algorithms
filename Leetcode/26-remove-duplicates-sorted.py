from typing import List
import unittest

"""
Leetcode 26: Remove Duplicates from Sorted Array

Given an integer array nums sorted in non-decreasing order, 
remove the duplicates in-place such that each unique element appears only once.
The relative order of the elements should be kept the same.
Then return the number of unique elements in nums.
"""

"""
Removes duplicate elements from a given sorted array 'nums'. It operates in-place
and returns the length of the modified array with unique elements.

Parameters:
    self:   the instance of the class
    nums:   a list of integers representing the sorted array with possible duplicates

Return:
    k:  an integer representing the length of the modified array with unique elements

Time Complexity:
    O(n)
Space Complexity:
    O(1)
"""


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        j = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[j] = nums[i]
                j += 1
        return j


"""
Test Cases
"""


class Test(unittest.TestCase):
    def test_solution(self):
        solution = Solution()
        self.assertEqual(solution.removeDuplicates([1, 1, 2]), 2, "Correct Answer: 6")
        self.assertEqual(
            solution.removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]),
            5,
            "Correct Answer is 5",
        )


if __name__ == "__main__":
    unittest.main()
