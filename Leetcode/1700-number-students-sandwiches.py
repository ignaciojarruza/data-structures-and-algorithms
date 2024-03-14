from typing import List
import unittest
"""
Leetcode: 1700 Number of Students Unable to Eat Lunch

The school cafeteria offers circular and square sandwiches at lunch break, referred to by numbers 0 and 1 respectively. All students stand in a queue. Each student either prefers square or circular sandwiches.

The number of sandwiches in the cafeteria is equal to the number of students. The sandwiches are placed in a stack. At each step:

If the student at the front of the queue prefers the sandwich on the top of the stack, they will take it and leave the queue.
Otherwise, they will leave it and go to the queue's end.
This continues until none of the queue students want to take the top sandwich and are thus unable to eat.

You are given two integer arrays students and sandwiches where sandwiches[i] is the type of the i​​​​​​th sandwich in the stack (i = 0 is the top of the stack) and students[j] is the preference of the j​​​​​​th student in the initial queue (j = 0 is the front of the queue). Return the number of students that are unable to eat.
"""

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]):
        """
        Counts the number of students unable to eat sandwiches. 

        Parameters:
            students (List[int]):   sandwich preference of each student
            sandwiches (List[int]): type of sandwich in the stack
        
        Returns:
            int:    Number of students that are unable to eat.
        """
        while (len(students) != 0):
            if (sandwiches[0] not in students):
                return len(students)
            if (students[0] == sandwiches[0]):
                students.pop(0)
                sandwiches.pop(0)
            else:
                student = students.pop(0)
                students.append(student)
        return len(students)
    
class Test(unittest.TestCase):
    def test_solution(self):
        solution = Solution()
        self.assertEqual(
            solution.countStudents([1, 1, 0, 0], [0, 1, 0, 1]),
            0,
            "Expected Output: 0"
        )
        self.assertEqual(
            solution.countStudents([1, 1, 1, 0, 0, 1], [1, 0, 0, 0, 1, 1]),
            3,
            "Expected Output: 3"
        )
if __name__ == "__main__":
    unittest.main()