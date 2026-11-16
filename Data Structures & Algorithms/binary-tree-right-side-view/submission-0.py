# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res=[]
        if root:
            queue = deque([root])
        else :
            return res
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
                res=res+[r[-1]]
        
        return res        
    