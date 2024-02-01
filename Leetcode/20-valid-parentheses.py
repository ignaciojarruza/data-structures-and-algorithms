import unittest

"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
"""

"""
Determines whether a given string of parentheses is valid.
Parameters:
    s(str)  : input string containing parentheses
Return:
    bool:   returns True if string contains valid arrangement of parentheses, false otherwise 
"""


class Solution:
    def validParentheses(self, s: str) -> bool:
        stack = []
        pairs = {"{": "}", "(": ")", "[": "]"}
        for char in s:
            if char in pairs:
                stack.append(char)
            elif len(stack) == 0 or pairs[stack.pop()] != char:
                return False
        return len(stack) == 0


class Test(unittest.TestCase):
    def test_solution(self):
        solution = Solution()
        self.assertEqual(solution.validParentheses("()"), True)
        self.assertEqual(solution.validParentheses("()[]{}"), True)
        self.assertEqual(solution.validParentheses("(}"), False)


if __name__ == "__main__":
    unittest.main()
