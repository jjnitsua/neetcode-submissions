class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        charcount=defaultdict(int)
        if len(s2)<len(s1):
            return False

        for c in s1:
            charcount[c]=1+charcount.get(c,0)

        l=0
        r=0
        for i in range(0,len(s2)):
            if s2[i] in charcount:
                l=i
                r=i
                break
        
        while r<len(s2):
            if s2[r] not in charcount or charcount[s2[r]]==0:
                charcount[s2[l]]=1+charcount.get(s2[l],0)
                l+=1
            if s2[r] in charcount and charcount[s2[r]]>0:
                charcount[s2[r]]-=1
                r+=1
            if r-l >=len(s1):
                return True
        
        return False


            

                

        
