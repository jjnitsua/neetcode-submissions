# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        curr=head
        arr=[]
        while curr: 
           arr.append(curr)
           curr=curr.next
        
        l=len(arr)

        i=0
        j=l-1

        if l==1:
            return

        for c in range (0,l):
            if c%2==0:
                if c==l-1:
                    arr[i].next=None
                    break
                arr[i].next=arr[j]
                i+=1
            else:
                if c==l-1:
                    arr[j].next=None
                    break
                arr[j].next=arr[i]
                j-=1
            
        return