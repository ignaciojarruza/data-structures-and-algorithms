class ListNode:
    """
    Represents a node in a singly linked list.

    Attributes:
        val (int)   : The value stored in the node
        next (ListNode): Reference to the next node in the linked list.
    """

    def __init__(self, val):
        """
        Initializes a new ListNode with the given value.

        Parameters:
            val (int): The value to be stored in the node.
        """
        self.val = val
        self.next = None


class LinkedList:
    """
    Represents a singly linked list.

    Attributes:
        head (ListNode): The dummy node at the beginning of the list.
        tail (ListNode): Points to the last node in the list.
    """

    def __init__(self):
        """
        Initializes an empty linked list with a dummy node.
        The dummy node simplifies operations at the beginning of the list.
        """
        self.head = ListNode(-1)
        self.tail = self.head

    def insertEnd(self, val):
        """
        Inserts a new node with the given value at the end of the linked list.

        Parameters:
            val (int): The value to be inserted.
        """
        self.tail.next = ListNode(val)
        self.tail = self.tail.next

    def remove(self, index):
        """
        Removes an element at the specified index from the linked list.

        Parameters:
            index (int):    The index of the node to be removed.

        Raises:
            IndexError: If the index is out of bounds.
        """
        if index < 0:
            raise IndexError("Index must be non-negative")

        i = 0
        curr = self.head
        while i < index and curr:
            curr = curr.next
            i += 1

        if i != index or not curr.next:
            raise IndexError("Index out of bounds")

        # Remove the node ahead of curr
        if curr and curr.next:
            if curr.next == self.tail:
                self.tail = curr
            curr.next = curr.next.next

    def print(self):
        """
        Prints the elements of the linked list in order.
        """
        curr = self.head.next
        while curr:
            print(curr.val, " -> ", end="")
            curr = curr.next
        print()


# Example Usage
if __name__ == "__main__":
    myList = LinkedList()

    # Inserting elements at the end
    myList.insertEnd(1)
    myList.insertEnd(2)
    myList.insertEnd(3)

    # Printing the linked list
    myList.print()  # Output: 1 -> 2 -> 3

    # Removing a node at index 1
    myList.remove(1)

    # Printing the updated linked list
    myList.print()  # Output: 1 -> 3
