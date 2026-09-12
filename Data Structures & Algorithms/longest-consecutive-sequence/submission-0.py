class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        s=set(nums)
        sequence_starter=set()
        for n in s :
            if n-1 in s:
                continue
            else :
                sequence_starter.add(n)
        
        l=0
        res=0
        for n in sequence_starter:
            l=1
            i=n
            while True : 
                if i+1 in s:
                    l+=1
                    i+=1
                else :
                    break
            if l>res:
                res=l
         
        return res






            