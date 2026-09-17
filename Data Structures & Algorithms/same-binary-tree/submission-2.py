# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if p and not q :
            return False
        if q and not p:
            return False
        pq=deque([p])
        qq=deque([q])

        while pq and qq:
            n1=pq.popleft()
            n2=qq.popleft()
            if n1.val != n2.val :
                return False
            if n1.left and n2.left:
                pq.append(n1.left)
                qq.append(n2.left)
            elif n1.left or n2.left:
                return False
            if n1.right and n2.right:
                pq.append(n1.right)
                qq.append(n2.right)
            elif n1.right or n2.right:
                return False

        return True