class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l=0
        r=0
        maxf=0
        count=defaultdict(int)
        res=0
        for r in range(0,len(s)):
            count[s[r]]=1+count.get(s[r],0)
            maxf=max(maxf,count[s[r]])
            check=(r-l+1)-maxf
            if check>k:
                while check>k:
                    count[s[l]]-=1
                    l+=1
                    check=(r-l+1)-maxf
            res = max(res, r - l + 1)
        return res  



            
