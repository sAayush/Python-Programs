class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class OddEven:
    def isEvenOddTree(self, root: [TreeNode]) -> bool:
        queue = [root]
        level = 0
        while queue:
            prev = 0 if level % 2 == 0 else 10**6
            for i in range(len(queue)):
                node = queue.pop(0)
                if level % 2 == 0:
                    if node.val % 2 == 0 or node.val <= prev:
                        return False
                else:
                    if node.val % 2 != 0 or node.val >= prev:
                        return False
                prev = node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            level += 1
        return True


if __name__ == '__main__':
    p = TreeNode(1, TreeNode(10, TreeNode(3), TreeNode(4)), TreeNode(6, TreeNode(7), TreeNode(9)))
    s = OddEven()
    print(s.isEvenOddTree(p))
