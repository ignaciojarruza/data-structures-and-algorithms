from typing import List
import unittest

"""
You are keeping the scores for a baseball game with strange rules. At the beginning of the game, you start with an empty record.

You are given a list of strings operations, where operations[i] is the ith operation you must apply to the record and is one of the following:

An integer x.
Record a new score of x.
'+'.
Record a new score that is the sum of the previous two scores.
'D'.
Record a new score that is the double of the previous score.
'C'.
Invalidate the previous score, removing it from the record.
Return the sum of all the scores on the record after applying all the operations.
"""


class Solution:
    def calculatePoints(self, operations: List[str]) -> int:
        """
        Calculates the total score based on a list of operations on a given input list.

        Parameters:
            operations (List[str]): A list of strings representing operations on a socre.
            Valid operations include:
                '+'     : Adds the last two scores and appends the result.
                'D'     : Doubles the last score and appends the result.
                'C'     : Removes the last score from the list.
                Integer : Appends the integer to the lsit as a score.

        Returns:
            int:    The total score obtained after performing all the operations."""
        solution = []
        for item in operations:
            if item == "+":
                solution.append(solution[-1] + solution[-2])
            elif item == "D":
                solution.append(2 * solution[-1])
            elif item == "C":
                solution.remove(solution[-1])
            else:
                solution.append(int(item))
        return sum(solution)


class Test(unittest.TestCase):
    def test_solution(self):
        solution = Solution()
        self.assertEqual(
            solution.calculatePoints(["5", "2", "C", "D", "+"]),
            30,
            "Correct Solution: 30",
        )


if __name__ == "__main__":
    unittest.main()
