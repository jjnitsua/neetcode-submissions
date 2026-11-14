# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        mins = min(p.val, q.val)
        maxs = max(p.val, q.val)
        r = self.result(root, mins, maxs)
        return r

    def result(self, node, mins, maxs):
        if mins < node.val < maxs:
            return node
        elif maxs < node.val:
            return self.result(node.left, mins, maxs)
        elif mins > node.val:
            return self.result(node.right, mins, maxs)
        else:
            return node
        