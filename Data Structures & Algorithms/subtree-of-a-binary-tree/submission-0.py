# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        a=deque([root])
        while a : 
            node=a.popleft()
            if node.val==subRoot.val: 
                compareRoot=node
                q=deque([subRoot])
                c=deque([compareRoot])
                match=True
                while q and c: 
                    subnode=q.popleft()
                    comparenode=c.popleft()

                    if subnode is None and comparenode is None:
                        continue
                    if subnode is None or comparenode is None or subnode.val!=comparenode.val: 
                        match=False
                        break
                    q.append(subnode.left)
                    c.append(comparenode.left)
                    q.append(subnode.right)
                    c.append(comparenode.right)
                if match:
                    return True
            if node.left:
                a.append(node.left)
            if node.right:
                a.append(node.right)
        return False
