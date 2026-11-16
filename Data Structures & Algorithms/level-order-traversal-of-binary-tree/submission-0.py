# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root:
            queue = deque([root])
        else :
            queue=deque()
        res=[]
        while queue:
            lq=len(queue)
            r=[]
            
            for i in range(lq):
                node=queue.popleft()
                if node.left: 
                    queue.append(node.left)
                if node.right: 
                    queue.append(node.right)
                r.append(node.val)
            if r: 
                res=res+[r]
        
        return res