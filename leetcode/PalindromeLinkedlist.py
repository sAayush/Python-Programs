class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class LinkedPalin:
    def isPalindrome(self, head: ListNode) -> bool:
        if head is None:
            return True
        slow = head
        fast = head
        while fast.next is not None and fast.next.next is not None:
            slow = slow.next
            fast = fast.next.next
        slow = self.reverse(slow.next)
        fast = head
        while slow is not None:
            if slow.val != fast.val:
                return False
            slow = slow.next
            fast = fast.next
        return True

    def reverse(self, head: ListNode) -> ListNode:
        prev = None
        current = head
        while current is not None:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        return prev


if __name__ == '__main__':
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(2)
    head.next.next.next = ListNode(1)
    linked_palin = LinkedPalin()
    print(linked_palin.isPalindrome(head))
