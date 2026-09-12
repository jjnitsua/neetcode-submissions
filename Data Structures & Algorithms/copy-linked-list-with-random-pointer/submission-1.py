"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        curr=head
        dic={}
        if head==None:
            return None
        while curr:
            new=Node(curr.val,None,None)
            dic[curr]=new
            curr=curr.next
        curr=head
        while curr:
            if curr.random!=None:
                dic[curr].random=dic[curr.random]
            else:
                dic[curr].random=None
            dic[curr].next = dic[curr.next] if curr.next else None
            curr=curr.next
        return dic[head]