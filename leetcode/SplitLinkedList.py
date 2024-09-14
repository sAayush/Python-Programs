class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class SplitLinked:
    def splitListToParts(self, head: ListNode, k: int):
        size = self.countNodes(head)
        part_size = size // k
        remainder = size % k
        parts = []
        
        for i in range(k):
            part = head
            for j in range(part_size + (i < remainder) - 1):
                if head:
                    head = head.next
            if head:
                head.next , head = None, head.next
                
            
            parts.append(part)
            
        return parts
                
        
    def countNodes(self, head: ListNode) -> int:
        count = 0
        while head:
            count += 1
            head = head.next
        return count


if __name__ == '__main__':
    sl = SplitLinked()
    
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    
    k = 5
    
    print(sl.splitListToParts(head, k))
    
    