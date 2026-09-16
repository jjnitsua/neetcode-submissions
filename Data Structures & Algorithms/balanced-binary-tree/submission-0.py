# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        flag=True
        def check(root):
            nonlocal flag
            if not root : 
                return 0
            l=check(root.left)
            r=check(root.right)
            if abs(l-r)>1:
                flag=False
            return 1+max(l,r)

        check(root)
        return flag