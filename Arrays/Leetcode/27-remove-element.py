from typing import List
import unittest

"""
Leetcode 27: Remove Element

Given an integer array nums and an integer val, remove all
occurrences of val in nums in-place. The order of the elements may 
not be changed. Then return the number of elements in nums 
which are not equal to val.

Consider the number of elements in nums which are not equal to val be k, 
to get accepted, you need to do the following things:

Change the array nums such that the first k elements of nums contain the elements 
which are not equal to val. The remaining elements of nums are not important as well as the size of nums.
Return k.
"""

"""
Removes all occurrences of a specified value 'val' from the given list 'nums'
in-place.
Parameters:
    nums (List[int]):   List of integers from which elements need to be removed.
    val (int)       :   The value to be removed from the list.

Returns:
    int: The length of the modified list after removal of elements.

Time Complexity: O(n)
Space Complexity: O(1)
"""


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        index = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[index] = nums[i]
                index += 1
        return index


"""
Test Cases
"""


class Test(unittest.TestCase):
    def test_solution(self):
        solution = Solution()
        self.assertEquals(solution.removeElement([3, 2, 2, 3], 3), 2)
        self.assertEquals(solution.removeElement([0, 1, 2, 2, 3, 0, 4, 2], 2), 5)


if __name__ == "__main__":
    unittest.main()
