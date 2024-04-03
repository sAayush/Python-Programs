class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class RevList:
    def reverseList(self, head: [ListNode]) -> [ListNode]:
        # if not head or not head.next:
        #     return head
        # prev = None
        # current = head
        # while current:
        #     next_node = current.next
        #     current.next = prev
        #     prev = current
        #     current = next_node
        # return prev
        prev_node = None
        current_node = head

        while current_node is not None:
            next_node = current_node.next
            current_node.next = prev_node
            prev_node = current_node
            current_node = next_node

        return prev_node