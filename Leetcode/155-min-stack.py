"""
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the MinStack class:

    MinStack() initializes the stack object.
    void push(int val) pushes the element val onto the stack.
    void pop() removes the element on the top of the stack.
    int top() gets the top element of the stack.
    int getMin() retrieves the minimum element in the stack.

You must implement a solution with O(1) time complexity for each function.
"""

"""
The MinStack class is designed to implement a stack with constant-time retrieval of the 
minimum element in the stack.

Time Complexity: O(1)
Space Complexity: O(n)
"""


class MinStack:
    """
    Initializes an emptu 'MinStack' object with two empty lists.
        stack:  for the main stack
        minStack: for tracking the minimum element at each position
    """

    def __init__(self):
        self.stack = []
        self.minStack = []

    """
    Adds the specified value to the main stack. Determines the minimum value
    up to the current position and updates the 'minStack' accordignly.
    
    Parameters:
        val(int)    : The value to be pushed onto the stack.
    """

    def push(self, val: int) -> None:
        self.stack.append(val)
        val = min(val, self.minStack[-1] if self.minStack else val)
        self.minStack.append(val)

    """
    Removes the top element from both the main stack and the minStack.
    """

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    """
    Returs the top element of the main stack (without removal).
    
    Returns:
        int: Top element of the miain stack.
    """

    def top(self) -> int:
        return self.stack[-1]

    """
    Returns the minimum element in the main stack without removing it.
    """

    def getMin(self) -> int:
        return self.minStack[-1]
