class ListNode:
    """
    Represents a single node in a singly linked list.

    Attributes:
    - val (int): The value stored in the node.
    - next (ListNode): The next node in the linked list.
    """

    def __init__(self, val):
        """
        ListNode constructor to initialize a new node with a give value.

        Parameters:
        - val (int): The value to be stored in the node.
        """
        self.val = val
        self.next = None