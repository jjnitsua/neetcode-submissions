# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr=head
        arr=[]
        while curr: 
           arr.append(curr)
           curr=curr.next
        
        l=len(arr)
        if l==1:
            return None
        if l-n-1>=0:
            if l-n+1<=l-1:
                arr[l-n-1].next=arr[l-n+1]
            else:
                arr[l-n-1].next=None
        else:
            head=arr[l-n+1]
        
        return head