class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


class LinkedList:
    def __init__(self):
        # init the list with a 'dummy' node which makes
        # removing a node from the beginning of the list easier
        self.head = ListNode(-1)
        self.tail = self.head

    def insertEnd(self, val):
        self.tail.next = ListNode(val)
        self.tail = self.tail.next

    def remove(self, index):
        i = 0
        curr = self.head
        while i < index and curr:
            cur = curr.next
            i += 1

        # Remove the node ahead of curr
        if curr and curr.next:
            self.tail = curr
        curr.next = curr.next.next

    def print(self):
        curr = self.head.next
        while curr:
            print(curr.val, " -> ", end="")
            curr = curr.next
        print()
