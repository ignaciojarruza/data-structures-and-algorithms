from Helper.ListNode import ListNode

class LinkedList:
    """
    Represents a singly linked list.

    Attributes:
    - head (ListNode): The head of the linked list.
    - tail (ListNode): The tail of the linked list.
    """

    def __init__(self):
        """
        Initializes an empty linked list with a dummy node.
        """
        self.head = ListNode(-1)
        self.tail = self.head

    def get(self, index: int) -> int:
        """
        Retrieves the value of the desired index node (0-indexed).

        Parameters:
        - index (int): The index of the desired node.

        Returns:
        - int: The value at the desired index. Returns -1 if index is invalid.
        """
        i = 0
        curr = self.head.next
        while curr:
            if i == index:
                return curr.val
            i += 1
            curr = curr.next
        return -1

    def insertHead(self, val: int) -> None:
        """
        Inserts a new element at the beginning of the linked list.

        Parameters:
        - val (int): The value to be inserted to the head of the linked list.
        """
        newHead = ListNode(val)
        newHead.next = self.head.next
        self.head.next = newHead
        if not newHead.next:
            self.tail = newHead

    def insertTail(self, val: int) -> None:
        """
        Inserts an element at the end of the LinkedList.

        Parameters:
        - val (int): The value to be inserted to the tail of the linked list.
        """
        self.tail.next = ListNode(val)
        self.tail = self.tail.next

    def remove(self, index: int) -> bool:
        """
        Removes the node at the desired index (0-indexed).

        Parameters:
        - index (int): The index of the element to be removed.

        Returns:
        - bool: Returns true if element successfully removed, false otherwise.
        """
        i = 0
        curr = self.head
        while i < index and curr:
            i += 1
            curr = curr.next
        if curr and curr.next:
            if curr.next == self.tail:
                self.tail == curr
            curr.next = curr.next.next
        return False

    def getValues(self) -> List[int]:
        """
        Retrieves all the values in the Linked List as a list.

        Returns:
        - List[int]: All of the values inside of the linked list.
        """
        ans = []
        curr = self.head.next
        while curr:
            ans.append(curr.val)
            curr = curr.next
        return ans
