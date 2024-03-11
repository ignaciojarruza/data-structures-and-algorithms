from Helper.ListNode import ListNode
        
class Queue:
    """
    Implementation of a Queue data structure.

    Attributes:
        left (ListNode): Pointer to the leftmost node in the queue.
        right (ListNode): Pointer to the rightmost node in the queue.

    Methods:
        __init__(): Initializes an empty Queue.
        enqueue(val): Adds a new element to the right end of the queue.
        dequeue(): Removes and returns the leftmost element from the queue.
    """
    def __init__(self):
        """
        Initializes an empty Queue.
        """
        self.left = self.right = None

    def enqueue(self, val):
        """
        Adds a new element to the right end of the queue.

        Args:
            val: The value to be added to the queue.
        """
        #Create new node to add
        newNode = ListNode(val)

        # Queue is non-empty
        if self.right:
            self.right.next = newNode
            self.right = self.right.next

        # Queue is empty
        else:
            self.left = self.right = newNode   

    def dequeue(self):
        """
        Removes and returns the leftmost element from the queue.
        
        Returns:
            The value of the leftmost element in the queue. Return None if the queue is empty.
        """
        # Queue is empty
        if not self.left:
            return None
        
        # Remove left node from queue and return value
        val = self.left.val
        self.left = self.left.next
        if not self.left:
            self.right = None
        return val
        