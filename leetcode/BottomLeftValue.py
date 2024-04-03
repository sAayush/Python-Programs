class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class TreeLeft:
    def findBottomLeftValue(self, root: [TreeNode]) -> int:
        queue = [root]
        while queue:
            node = queue.pop(0)
            if node.right:
                queue.append(node.right)
            if node.left:
                queue.append(node.left)
        return node.val


if __name__ == '__main__':
    tl = TreeLeft()
    print(tl.findBottomLeftValue(TreeNode(2, TreeNode(1), TreeNode(3))))
