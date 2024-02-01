class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = ListNode(-1)
        self.tail = self.head

    def get(self, index: int) -> int:
        i = 0
        curr = self.head.next
        while curr:
            if i == index:
                return curr.val
            i += 1
            curr = curr.next
        return -1

    def insertHead(self, val: int) -> None:
        newHead = ListNode(val)
        newHead.next = self.head.next
        self.head.next = newHead
        if not newHead.next:
            self.tail = newHead

    def insertTail(self, val: int) -> None:
        self.tail.next = ListNode(val)
        self.tail = self.tail.next

    def remove(self, index: int) -> bool:
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
        ans = []
        curr = self.head.next
        while curr:
            ans.append(curr.val)
            curr = curr.next
        return ans
