"""
Given an integer x, return true if x is a palindrome, and false
otherwise.
"""


class Solution:
    """
    Determines whether the integer is a palindrome.

    Parameters:
    - x (int)   : integer

    Returns:
    - bool  : True if integer is palindrome, false otherwise.
    """

    def isPalindrome(self, x: int) -> bool:
        return str(x) == str(x)[::-1]
