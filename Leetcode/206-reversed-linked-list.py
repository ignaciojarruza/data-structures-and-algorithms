"""
Given the head of a singly linked list, reverse thelist, and return the reversed list.
"""
from dataStructures import ListNode


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        """
        Reverses a singly linked list.

        Parameters:
        - head (ListNode)   : the head of the linked list to be reversed.

        Returns:
        - ListNode: the reversed linked list.

        Time Complexity: O(n)
        """
        curr = head
        reversedList = None
        while curr:
            nextNode = curr.next
            curr.next = reversedList
            reversedList = curr
            curr = nextNode
        return reversedList
