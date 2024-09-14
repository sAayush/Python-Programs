class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class SpiralMatrix:
    def spiralMatrix(self, m: int, n: int, head: ListNode) -> list[list[int]]:
        matrix = []
        for i in range(m):
            matrix.append([-1] * n)
        
        top = 0
        bottom = m - 1
        left = 0
        right = n - 1
        
        while top <= bottom and left <= right:
            for i in range(left, right + 1):
                if head:
                    matrix[top][i] = head.val
                    head = head.next
            top += 1
            
            for i in range(top, bottom + 1):
                if head:
                    matrix[i][right] = head.val
                    head = head.next
            right -= 1
            
            for i in range(right, left -1, -1):
                if head:
                    matrix[bottom][i] = head.val
                    head = head.next
            bottom -= 1
            
            for i in range(bottom, top - 1, -1):
                if head:
                    matrix[i][left] = head.val
                    head = head.next
            left += 1
            
        return matrix
            
    

if __name__ == '__main__':
    sm = SpiralMatrix()
    
    head = ListNode(3)
    head.next = ListNode(0)
    head.next.next = ListNode(2)
    head.next.next.next = ListNode(6)
    head.next.next.next.next = ListNode(8)
    head.next.next.next.next.next = ListNode(1)
    head.next.next.next.next.next.next = ListNode(7)
    head.next.next.next.next.next.next.next = ListNode(9)
    head.next.next.next.next.next.next.next.next = ListNode(4)
    head.next.next.next.next.next.next.next.next.next = ListNode(2)
    head.next.next.next.next.next.next.next.next.next.next = ListNode(5)
    head.next.next.next.next.next.next.next.next.next.next.next = ListNode(5)
    head.next.next.next.next.next.next.next.next.next.next.next.next = ListNode(0)


    m = 3
    n = 5
    
    print(sm.spiralMatrix(m, n, head))