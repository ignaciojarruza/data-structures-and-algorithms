from Helper.ListNode import ListNode
        
class Queue:
    def __init__(self):
        self.left = self.right = None

    def enqueue(self, val):
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
        # Queue is empty
        if not self.left:
            return None
        
        # Remove left node from queue and return value
        val = self.left.val
        self.left = self.left.next
        if not self.left:
            self.right = None
        return val
        