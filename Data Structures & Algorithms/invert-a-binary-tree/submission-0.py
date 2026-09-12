# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def swap(self, node):
        if node is None:
            return
        t = node.left
        node.left = node.right
        node.right = t
        self.swap(node.left)
        self.swap(node.right)

    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        node = root
        self.swap(node)
        return root
