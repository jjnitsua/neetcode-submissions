# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root == None : 
            return None
        queue = deque([root])

        while queue : 
            n=queue.popleft()
            if n.left or n.right :
                n.left,n.right=n.right,n.left
            if n.left != None:
                queue.append(n.left)
            if n.right != None:
                queue.append(n.right)

        return root