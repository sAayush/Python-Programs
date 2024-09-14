class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class DeleteNodes:
    def modifiedList(self, nums: list[int], head: ListNode) -> ListNode:
        if not head:
            return head
        
        toDelete = set(nums)
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        curr = head
        
        while curr:
            if curr.val in toDelete:
                prev.next = curr.next
            else:
                prev = curr
            curr = curr.next
            
        return dummy.next


if __name__ == '__main__':
    dn = DeleteNodes()
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    head.next.next.next.next.next = ListNode(6)

    result = dn.modifiedList([1, 2, 6], head)
    while result:
        print(result.val)
        result = result.next
