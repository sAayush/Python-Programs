class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class TreeDiameter:
    def diameterOfBinaryTree(self, root: [TreeNode]) -> int:
        self.ans = 0
        def depth(node):
            if not node: return 0
            L = depth(node.left)
            R = depth(node.right)
            self.ans = max(self.ans, L+R)
            return max(L, R) + 1
        depth(root)
        return self.ans


if __name__ == '__main__':
    p = TreeNode(1, TreeNode(2), TreeNode(3), TreeNode(4), TreeNode(5))
    s = TreeDiameter()
    print(s.diameterOfBinaryTree(p))
