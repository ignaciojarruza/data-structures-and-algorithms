from typing import List
import unittest

"""
Given an integer array nums of length n, you want to create an array ans of length 2n where ans[i] == nums[i] and ans[i + n] == nums[i] for 0 <= i < n (0-indexed).

Specifically, ans is the concatenation of two nums arrays.

Return the array ans.
"""

"""
Concatenates the given list 'nums' with itself without using the '+' operator
to add arrays together.

Parameters:
    nums (List[int]):   The input list to be concatenated

Returns:
    List[int]:  The concatenated list.
"""


class Solution:
    def concatenateArray(self, nums: List[int]):
        # one liner: return ans+ans
        # without using + operator
        answer = []
        for i in range(2):
            for item in nums:
                answer.append(item)
        return answer


"""
Test Cases
"""


class Test(unittest.TestCase):
    def test_solution(self):
        solution = Solution()
        self.assertEqual(
            solution.concatenateArray([1, 2, 1]),
            [1, 2, 1, 1, 2, 1],
            "Correct Answer is [1, 2, 1, 1, 2, 1]",
        )
        self.assertEqual(
            solution.concatenateArray([1, 3, 2, 1]),
            [1, 3, 2, 1, 1, 3, 2, 1],
            "Correct Answer is [1, 3, 2, 1, 1, 3, 2, 1]",
        )


if __name__ == "__main__":
    unittest.main()
