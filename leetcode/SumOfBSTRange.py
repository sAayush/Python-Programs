class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class SumRange:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        sum = 0
        if root is None:
            return 0
        if low <= root.val <= high:
            sum += root.val

        if root.val > low:
            sum += self.rangeSumBST(root.left, low, high)

        if root.val < high:
            sum += self.rangeSumBST(root.right, low, high)

        return sum


if __name__ == '__main__':
    s = SumRange()
    print(s.rangeSumBST([10, 5, 15, 3, 7, None, 18], 7, 15))
    print(s.rangeSumBST([10, 5, 15, 3, 7, 13, 18, 1, None, 6], 6, 10))