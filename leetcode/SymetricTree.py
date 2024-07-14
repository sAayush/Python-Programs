class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
    
class Solution:
    def isSymmetric(self, root: [TreeNode]) -> bool:
        if root is None:
            return True
        return self.isMirror(root.left, root.right)
    
    def isMirror(self, left: TreeNode, right: TreeNode) -> bool:
        if left is None and right is None:
            return True
        if left is None or right is None:
            return False
        if left.val != right.val:
            return False
        return self.isMirror(left.left, right.right) and self.isMirror(left.right, right.left)