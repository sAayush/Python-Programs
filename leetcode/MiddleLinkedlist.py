class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class MiddleList:
    def middleNode(self, head: [ListNode]) -> [ListNode]:
        if not head or not head.next:
            return head
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow


if __name__ == '__main__':
    ml = MiddleList()
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    print(ml.middleNode(head))
