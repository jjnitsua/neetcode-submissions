class Solution:
    def __init__(self):
        self.m = 0

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        self.root_l(root)
        return self.m

    def root_l(self, root):
        if not root:
            return 0

        left = self.root_l(root.left)
        right = self.root_l(root.right)

        l = left + right
        self.m = max(self.m, l)

        return 1 + max(left, right)