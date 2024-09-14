class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class TreeList:
    def isSubPath(self, head: ListNode, root: TreeNode) -> bool:
        if not root:
            return False
        return self.dfs(head, root) or self.isSubPath(head, root.left) or self.isSubPath(head, root.right)
    
    def dfs(self, head, root):
        if not head:
            return True
        if not root:
            return False
        return head.val == root.val and (self.dfs(head.next, root.left) or self.dfs(head.next, root.right)) 
    

if __name__ == '__main__':
    t = TreeList()
    
    head = ListNode(4)
    head.next = ListNode(2)
    head.next.next = ListNode(8)
    
    root = TreeNode(1)
    root.left = TreeNode(4)
    root.right = TreeNode(4)
    root.left.right = TreeNode(2)
    root.left.right.left = TreeNode(1)
    root.left.right.right = TreeNode(8)
    root.left.right.left.left = TreeNode(4)
    root.left.right.left.right = TreeNode(2)
    root.left.right.left.left.left = TreeNode(6)
    
    print(t.isSubPath(head, root))
    