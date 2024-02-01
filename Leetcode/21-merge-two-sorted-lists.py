"""
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by 
splicing together the nodes of the first two lists.

Return the head of the merged linked list.
"""
from dataStructures import ListNode


class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        """
        Merges two pre-sorted singly linked lists.

        Parameters:
        - list1 (ListNode): linked list 1 to be merged. Already pre-sorted.
        - list2 (ListNode): linked list 2 to be merged. Already pre-sorted.

        Returns:
        - ListNode: the merged linked list.

        Time Complexity: O(n)
        """
        if not list1:
            return list2
        if not list2:
            return list1
        littleNode, bigNode = (
            (list1, list2) if list1.val <= list2.val else (list2, list1)
        )
        littleNode.next = self.mergeTwoLists(littleNode.next, bigNode)
        return littleNode
